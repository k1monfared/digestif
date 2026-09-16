#!/usr/bin/env python3
"""Aggregate per-sample judge JSON files into a corpus report.

Usage:
    python3 aggregate.py <skill-dir> <run-dir>

Example:
    python3 eval/lib/aggregate.py eval/skills/point-hierarchy eval/skills/point-hierarchy/runs/20260911_0000_v1

Reads each sample dir for judge_faithfulness.json, judge_coverage.json,
judge_concision.json, judge_top.json and writes report.md plus summary.json
into the run dir. Uses stdlib only.
"""
import json
import sys
from pathlib import Path


def load_json(path):
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def main():
    if len(sys.argv) != 3:
        print(__doc__)
        sys.exit(2)
    skill_dir = Path(sys.argv[1])
    run_dir = Path(sys.argv[2])
    corpus_path = skill_dir / "corpus.json"
    corpus = load_json(corpus_path)
    rows = []
    for item in corpus["items"]:
        sid = item["id"]
        sdir = run_dir / sid
        row = {"id": sid, "words": item.get("words", 0)}
        for key, fname in [
            ("faithfulness", "judge_faithfulness.json"),
            ("coverage", "judge_coverage.json"),
            ("concision", "judge_concision.json"),
            ("top", "judge_top.json"),
        ]:
            fpath = sdir / fname
            if fpath.exists():
                data = load_json(fpath)
                row[key] = data.get("metrics", data)
                if key == "top":
                    row["verdict"] = data.get("verdict", "missing")
                    row["weighted_score"] = data.get("weighted_score")
            else:
                row[key] = None
                if key == "top":
                    row["verdict"] = "missing"
        rows.append(row)

    scored = [r for r in rows if r.get("top") is not None]
    n_fail = sum(1 for r in scored if r.get("verdict") == "Fail")
    n_pass = sum(1 for r in scored if r.get("verdict") == "Pass")
    n_border = sum(1 for r in scored if r.get("verdict") == "Borderline")

    def avg(get):
        vals = [get(r) for r in scored if get(r) is not None]
        return sum(vals) / len(vals) if vals else None

    summary = {
        "total_samples": len(rows),
        "scored_samples": len(scored),
        "pass": n_pass,
        "borderline": n_border,
        "fail": n_fail,
        "avg_faithfulness_precision": avg(
            lambda r: (r["faithfulness"] or {}).get("faithfulness_precision")
        ),
        "avg_must_recall": avg(
            lambda r: (r["coverage"] or {}).get("metrics", {}).get("must_recall")
            if "metrics" in (r["coverage"] or {})
            else (r["coverage"] or {}).get("must_recall")
        ),
        "avg_redundancy": avg(
            lambda r: (r["concision"] or {}).get("redundancy_rate")
        ),
        "avg_weighted_score": avg(lambda r: r.get("weighted_score")),
    }

    with open(run_dir / "summary.json", "w", encoding="utf-8") as fh:
        json.dump({"summary": summary, "rows": rows}, fh, indent=2, ensure_ascii=False)

    lines = []
    lines.append("# Eval report")
    lines.append("")
    lines.append(f"Skill dir: {skill_dir}")
    lines.append(f"Run dir: {run_dir}")
    lines.append("")
    lines.append("## Summary")
    lines.append("")
    for key, val in summary.items():
        lines.append(f"* {key}: {val}")
    lines.append("")
    lines.append("## Per sample")
    lines.append("")
    lines.append("| id | words | verdict | weighted | faithfulness | must_recall | redundancy |")
    lines.append("| --- | --- | --- | --- | --- | --- | --- |")
    for r in rows:
        f = (r.get("faithfulness") or {}).get("faithfulness_precision", "?")
        c = r.get("coverage") or {}
        must = c.get("must_recall", c.get("metrics", {}).get("must_recall", "?")) if c else "?"
        red = (r.get("concision") or {}).get("redundancy_rate", "?")
        lines.append(
            f"| {r['id']} | {r['words']} | {r.get('verdict')} "
            f"| {r.get('weighted_score')} | {f} | {must} | {red} |"
        )
    lines.append("")
    lines.append("## Fix backlog")
    lines.append("")
    lines.append("Collect fix_list entries from each judge_top.json, ordered by frequency.")
    lines.append("Use trace.md files in each sample dir for judge reasoning audit.")
    lines.append("")
    with open(run_dir / "report.md", "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines))
    print(f"Wrote {run_dir / 'summary.json'} and {run_dir / 'report.md'}")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
