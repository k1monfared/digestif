#!/usr/bin/env python3
"""Consolidated failure report for an eval run. Audit companion to aggregate.py.

Usage:
    python3 failures.py <run-dir>

Reads every sample's judge_*.json and writes <run-dir>/failures.json plus
<run-dir>/failures.md. The report lists every non-Supported claim with its
evidence and reasoning, every non-Present key point, every concision flag,
and every top judge verdict with its fix list. Stdlib only.
"""
import json
import sys
from datetime import date
from pathlib import Path


def load(path):
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def build(run_dir):
    run = Path(run_dir)
    report = {"run": run.name, "generated": str(date.today()), "samples": {}, "summary": {}}
    counts = {"claims": 0, "non_supported": 0, "partial": 0, "unverifiable": 0,
              "contradicted": 0, "critical": 0, "points_non_present": 0,
              "duplicates": 0, "trivia": 0}
    for sdir in sorted(d for d in run.iterdir() if d.is_dir()):
        fid = sdir / "judge_faithfulness.json"
        if not fid.exists():
            continue
        faith = load(fid)
        cov = load(sdir / "judge_coverage.json") if (sdir / "judge_coverage.json").exists() else {}
        con = load(sdir / "judge_concision.json") if (sdir / "judge_concision.json").exists() else {}
        top = load(sdir / "judge_top.json") if (sdir / "judge_top.json").exists() else {}

        claims = faith.get("claims", [])
        bad_claims = [c for c in claims if c.get("verdict") != "Supported"]
        points = cov.get("key_points", [])
        bad_points = [p for p in points if p.get("presence") != "Present"]
        labels = con.get("labels", [])
        dupes = [l for l in labels if l.get("label") == "Duplicate"]
        trivia = [l for l in labels if l.get("label") == "Trivia"]

        counts["claims"] += len(claims)
        counts["non_supported"] += len(bad_claims)
        counts["partial"] += sum(1 for c in bad_claims if c.get("verdict") == "Partially supported")
        counts["unverifiable"] += sum(1 for c in bad_claims if c.get("verdict") == "Unverifiable")
        counts["contradicted"] += sum(1 for c in bad_claims if c.get("verdict") == "Contradicted")
        counts["critical"] += sum(1 for c in bad_claims if c.get("severity") == "Critical")
        counts["points_non_present"] += len(bad_points)
        counts["duplicates"] += len(dupes)
        counts["trivia"] += len(trivia)

        report["samples"][sdir.name] = {
            "verdict": top.get("verdict"),
            "weighted_score": top.get("weighted_score"),
            "faithfulness_metrics": faith.get("metrics", {}),
            "coverage_metrics": cov.get("metrics", {}),
            "concision_metrics": con.get("metrics", {}),
            "non_supported_claims": bad_claims,
            "non_present_points": bad_points,
            "duplicate_labels": dupes,
            "trivia_labels": trivia,
            "top_fix_list": top.get("fix_list", []),
            "top_tradeoff_note": top.get("tradeoff_note", ""),
        }
    report["summary"] = counts
    return report


def render_md(report):
    lines = []
    lines.append(f"# Failure report: {report['run']}")
    lines.append("")
    lines.append(f"Generated: {report['generated']} by `eval/lib/failures.py`.")
    lines.append("")
    s = report["summary"]
    lines.append("## Summary")
    lines.append("")
    lines.append(f"* claims judged: {s['claims']}")
    lines.append(f"* non-supported claims: {s['non_supported']} "
                 f"(partial {s['partial']}, unverifiable {s['unverifiable']}, contradicted {s['contradicted']}, critical {s['critical']})")
    lines.append(f"* non-present key points: {s['points_non_present']}")
    lines.append(f"* duplicate labels: {s['duplicates']}, trivia labels: {s['trivia']}")
    lines.append("")
    lines.append("Per sample detail follows. Every entry cites its claim or point id, the "
                 "deciding evidence, and the judge's reasoning so a human can audit or overturn it.")
    lines.append("")
    for sid, data in report["samples"].items():
        lines.append(f"## {sid}")
        lines.append("")
        lines.append(f"Verdict: {data['verdict']} "
                     f"(weighted {data['weighted_score']}, "
                     f"precision {data['faithfulness_metrics'].get('faithfulness_precision')}, "
                     f"must recall {data['coverage_metrics'].get('must_recall')}, "
                     f"redundancy {data['concision_metrics'].get('redundancy_rate')})")
        lines.append("")
        if data["non_supported_claims"]:
            lines.append("### Non-supported claims")
            lines.append("")
            for c in data["non_supported_claims"]:
                lines.append(f"* {c.get('claim_id')} [{c.get('verdict')}, {c.get('severity')}] "
                             f"loglog {', '.join(c.get('loglog_ids', []))}")
                lines.append(f"  * claim: {c.get('claim_text')}")
                lines.append(f"  * evidence: {c.get('evidence_quote')}")
                lines.append(f"  * why: {c.get('reasoning')}")
            lines.append("")
        if data["non_present_points"]:
            lines.append("### Non-present key points")
            lines.append("")
            for p in data["non_present_points"]:
                lines.append(f"* {p.get('point_id')} [{p.get('weight')}, {p.get('presence')}]")
                lines.append(f"  * point: {p.get('point_text')}")
                lines.append(f"  * loglog: {', '.join(p.get('loglog_ids', [])) or 'none'}")
                lines.append(f"  * why: {p.get('reasoning')}")
            lines.append("")
        if data["duplicate_labels"] or data["trivia_labels"]:
            lines.append("### Concision flags")
            lines.append("")
            for l in data["duplicate_labels"]:
                lines.append(f"* {l.get('claim_id')} Duplicate of {l.get('canonical_id')}: {l.get('reasoning')}")
            for l in data["trivia_labels"]:
                lines.append(f"* {l.get('claim_id')} Trivia: {l.get('reasoning')}")
            lines.append("")
        if data["top_fix_list"]:
            lines.append("### Fix list")
            lines.append("")
            for f in data["top_fix_list"]:
                lines.append(f"* {f}")
            lines.append("")
    return "\n".join(lines) + "\n"


def main():
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(2)
    run = Path(sys.argv[1])
    report = build(run)
    (run / "failures.json").write_text(json.dumps(report, ensure_ascii=False, indent=1), encoding="utf-8")
    (run / "failures.md").write_text(render_md(report), encoding="utf-8")
    s = report["summary"]
    print(f"{run.name}: {s['non_supported']} non-supported claims, "
          f"{s['points_non_present']} non-present points, "
          f"{s['duplicates']} duplicates, {s['trivia']} trivia entries written to failures.md and failures.json")


if __name__ == "__main__":
    main()
