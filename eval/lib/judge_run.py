#!/usr/bin/env python3
"""Scripted judge pipeline for the digestif eval.

Runs each judge phase as a fresh Gemini API call (no shared context, no
subagent size limits), saves raw JSON results under <sample>/packets/,
merges them into the canonical judge_*.json files, and appends reasoning
transcripts to <sample>/trace.md.

Usage:
    python3 judge_run.py prep     <sample-dir>
    python3 judge_run.py faith    <sample-dir> [part]
    python3 judge_run.py cov_check <sample-dir>
    python3 judge_run.py cov_map  <sample-dir>
    python3 judge_run.py con      <sample-dir>
    python3 judge_run.py top      <sample-dir>
    python3 judge_run.py merge    <sample-dir>
    python3 judge_run.py all      <sample-dir>

Env: GEMINI_API_KEY, JUDGE_MODEL (default gemini-3.6-flash). Stdlib only.
"""
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

SKILL_DIR = Path(__file__).resolve().parent.parent / "skills" / "digestif"
PROMPTS = SKILL_DIR / "prompts"
CONFIG = SKILL_DIR / "config.json"
PROVIDER = os.environ.get("JUDGE_PROVIDER", "opencode")
if PROVIDER == "opencode":
    MODEL = os.environ.get("JUDGE_MODEL", "opencode-go/deepseek-v4.1-flash")
    API = ""
    KEY_ENV = ""
    MODEL_TAG = f"{MODEL} (opencode) scripted pipeline 2026-09-15"
elif PROVIDER == "nvidia":
    MODEL = os.environ.get("JUDGE_MODEL", "nvidia/nemotron-3-ultra-550b-a55b")
    API = "https://integrate.api.nvidia.com/v1/chat/completions"
    KEY_ENV = "NVIDIA_API_KEY"
    MODEL_TAG = f"{MODEL} (nvidia) scripted pipeline 2026-09-15"
else:
    MODEL = os.environ.get("JUDGE_MODEL", "gemini-3.8-flash")
    API = "https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={key}"
    KEY_ENV = "GEMINI_API_KEY"
    MODEL_TAG = f"{MODEL} (gemini) scripted pipeline 2026-09-15"
PART_LIMIT = int(os.environ.get("FAITH_PART_LIMIT", "35"))  # max nodes per faithfulness part
FAITH_SCOPE = os.environ.get("FAITH_SCOPE", "full")  # "full" sends the whole source, "evidence" sends only cited passages
CHECKLIST_DIR = SKILL_DIR / "corpus" / "checklists"


def log(msg):
    print(msg, flush=True)


def read(path):
    return Path(path).read_text(encoding="utf-8")


def numbered_outline(text):
    lines = []
    for raw in text.splitlines():
        line = raw.rstrip()
        if line.strip():
            lines.append(line)
    width = max(3, len(str(len(lines))))
    return "\n".join(f"L{i+1:0{width}d}: {line}" for i, line in enumerate(lines))


def node_branch(nid):
    return nid.split(".")[0]


def prep(sample_dir):
    sd = Path(sample_dir)
    out = sd / "packets"
    out.mkdir(exist_ok=True)
    source = read(sd / "source.txt")
    outline = read(sd / "output.log")
    numbered = numbered_outline(outline)
    (out / "source.txt").write_text(source, encoding="utf-8")
    (out / "outline_numbered.txt").write_text(numbered, encoding="utf-8")

    graph_path = sd / "graph.json"
    graph = json.loads(graph_path.read_text(encoding="utf-8")) if graph_path.exists() else None

    if graph:
        passages = graph["meta"]["passages"]
        nodes = graph["nodes"]
        by_branch = {}
        for n in nodes:
            by_branch.setdefault(node_branch(n["id"]), []).append(n)
        # greedy pack branches into parts of at most PART_LIMIT nodes
        parts, current = [], []
        for branch in sorted(by_branch, key=lambda b: (b != "0", int(b) if b.isdigit() else 0)):
            group = by_branch[branch]
            if current and len(current) + len(group) > PART_LIMIT:
                parts.append(current)
                current = []
            current.extend(group)
        if current:
            parts.append(current)
        for i, part_nodes in enumerate(parts, 1):
            records = []
            for n in part_nodes:
                ev = []
                for ref in n.get("source", []):
                    txt = passages.get(ref, "<missing>")
                    ev.append({"ref": ref, "text": txt})
                records.append({
                    "id": n["id"], "type": n.get("type"),
                    "attribution": n.get("attribution"),
                    "text": n["text"], "evidence": ev,
                })
            payload = {"sample": sd.name, "part": i, "of": len(parts), "nodes": records}
            (out / f"faith_part{i:02d}.json").write_text(
                json.dumps(payload, ensure_ascii=False, indent=1), encoding="utf-8")
        log(f"prep: {len(parts)} faith part(s), {len(nodes)} nodes, outline {len(outline.splitlines())} lines")
    else:
        log("prep: no graph.json, only source and outline written")


def call_opencode(system_text, user_text):
    import subprocess
    prompt = (
        system_text
        + "\n\nReturn only the final JSON object as your entire reply. Do not use tools, do not read or write files.\n\n"
        + user_text
    )
    proc = subprocess.run(
        ["opencode", "run", "-m", MODEL, "--format", "json"],
        input=prompt, capture_output=True, text=True, timeout=900, cwd="/tmp",
    )
    texts = []
    for line in proc.stdout.splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            ev = json.loads(line)
        except json.JSONDecodeError:
            continue
        if ev.get("type") == "text":
            texts.append(ev.get("part", {}).get("text", ""))
    return "\n".join(t for t in texts if t)


def api_call(system_text, user_text, max_tokens=32000):
    if PROVIDER == "opencode":
        delays = [10, 20, 40, 60]
        for attempt in range(len(delays) + 1):
            try:
                text = call_opencode(system_text, user_text)
            except Exception as exc:
                if attempt < len(delays):
                    log(f"  retry {attempt+1} after opencode error: {exc} sleeping {delays[attempt]}s")
                    time.sleep(delays[attempt])
                    continue
                raise
            if text.strip():
                return text
            if attempt < len(delays):
                log(f"  retry {attempt+1} after empty opencode response: sleeping {delays[attempt]}s")
                time.sleep(delays[attempt])
                continue
            raise RuntimeError("empty opencode response")
        raise RuntimeError("opencode retries exhausted")

    key = os.environ[KEY_ENV]
    if PROVIDER == "nvidia":
        url = API
        body = {
            "model": MODEL,
            "messages": [
                {"role": "system", "content": system_text},
                {"role": "user", "content": user_text},
            ],
            "temperature": 0.1,
            "max_tokens": max_tokens,
            "response_format": {"type": "json_object"},
        }
        headers = {"Content-Type": "application/json", "Authorization": f"Bearer {key}"}
    else:
        url = API.format(model=MODEL, key=key)
        body = {
            "system_instruction": {"parts": [{"text": system_text}]},
            "contents": [{"parts": [{"text": user_text}]}],
            "generationConfig": {
                "temperature": 0.1,
                "maxOutputTokens": max_tokens,
                "responseMimeType": "application/json",
            },
        }
        headers = {"Content-Type": "application/json"}
    req = urllib.request.Request(
        url, data=json.dumps(body).encode("utf-8"), headers=headers, method="POST")

    delays = [5, 10, 20, 40, 60, 60, 60, 60]
    payload = None
    for attempt in range(len(delays) + 1):
        try:
            with urllib.request.urlopen(req, timeout=600) as resp:
                payload = json.loads(resp.read().decode("utf-8"))
        except urllib.error.HTTPError as exc:
            detail = exc.read().decode("utf-8", "replace")[:300]
            retryable = exc.code in (408, 429, 500, 502, 503, 504) or "UNAVAILABLE" in detail or "high demand" in detail
            if retryable and attempt < len(delays):
                log(f"  retry {attempt+1} after HTTP {exc.code}: sleeping {delays[attempt]}s")
                time.sleep(delays[attempt])
                continue
            raise RuntimeError(f"HTTP {exc.code}: {detail}") from exc
        err = payload.get("error") if isinstance(payload, dict) else None
        if err:
            status = err.get("status") if isinstance(err, dict) else None
            if status in ("UNAVAILABLE", "RESOURCE_EXHAUSTED") and attempt < len(delays):
                log(f"  retry {attempt+1} after error body: sleeping {delays[attempt]}s")
                time.sleep(delays[attempt])
                continue
            raise RuntimeError(f"error body: {json.dumps(err)[:300]}")

        if PROVIDER == "nvidia":
            choices = payload.get("choices") or []
            if choices:
                cand = choices[0]
                text = cand.get("message", {}).get("content") or ""
                finish = cand.get("finish_reason")
            else:
                text, finish = "", None
        else:
            cands = payload.get("candidates") or []
            if cands:
                cand = cands[0]
                text = "\n".join(p.get("text", "") for p in cand.get("content", {}).get("parts", []) if p.get("text"))
                finish = cand.get("finishReason")
            else:
                text, finish = "", None

        if not text.strip():
            if attempt < len(delays):
                log(f"  retry {attempt+1} after empty response: sleeping {delays[attempt]}s")
                time.sleep(delays[attempt])
                continue
            raise RuntimeError(f"empty response: {json.dumps(payload)[:400]}")
        if finish in ("length", "MAX_TOKENS"):
            log("  warning: response hit token cap, JSON may be truncated")
        return text
    raise RuntimeError("api retries exhausted")


def api_json(system_text, user_text, attempts=3):
    last = None
    for i in range(attempts):
        raw = api_call(system_text, user_text)
        try:
            return parse_json(raw)
        except json.JSONDecodeError as exc:
            last = exc
            log(f"  json parse failed (attempt {i+1}/{attempts}): {exc}")
            time.sleep(3)
    raise RuntimeError(f"unparseable JSON after {attempts} attempts: {last}")


def parse_json(text):
    text = text.strip()
    if text.startswith("```"):
        text = re.sub(r"^```[a-zA-Z]*\n?", "", text)
        text = re.sub(r"\n?```$", "", text)
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        m = re.search(r"\{.*\}", text, re.S)
        if not m:
            raise
        return json.loads(m.group(0))


def spec(name):
    return read(PROMPTS / name)


def run_phase(sample_dir, phase, part=None):
    sd = Path(sample_dir)
    pk = sd / "packets"
    prompt_file = {
        "faith": "judge_faithfulness.md",
        "cov_check": "judge_coverage.md",
        "cov_map": "judge_coverage.md",
        "con": "judge_concision.md",
        "top": "judge_top.md",
    }[phase]
    system = spec(prompt_file)
    source = read(pk / "source.txt")
    numbered = read(pk / "outline_numbered.txt")

    if phase == "faith":
        part_file = pk / f"faith_part{part:02d}.json"
        nodes = json.loads(read(part_file))
        if FAITH_SCOPE == "evidence":
            graph = json.loads(read(sd / "graph.json"))
            by_id = {n["id"]: n for n in graph["nodes"]}
            ctx_ids = set()
            for n in nodes["nodes"]:
                nid = n["id"]
                while nid != "0":
                    nid = nid.rsplit(".", 1)[0] if "." in nid else "0"
                    ctx_ids.add(nid)
            ctx = [{"id": i, "text": by_id[i]["text"]} for i in sorted(ctx_ids) if i in by_id]
            user = (
                "SETTING (root summary and branch headers, for context only):\n"
                + json.dumps(ctx, ensure_ascii=False, indent=1)
                + "\n\nLOGLOG NODES TO JUDGE (this part, with their cited evidence passages):\n"
                + json.dumps(nodes, ensure_ascii=False, indent=1)
                + "\n\nJudge every node in this part as one atomic claim against its cited evidence passages. "
                "The setting block is context, not evidence. If a node's text asserts more than its evidence supports, "
                "or drops a number, hedge, negation, or scope word, mark the claim Partially supported or Contradicted as the spec requires. "
                "Return the JSON object exactly as the spec shows, with claims for this part only. "
                "Keep each reasoning field under 30 words. Return JSON only, no markdown fences."
            )
        else:
            user = (
                "SOURCE (full original prose):\n" + source
                + "\n\nLOGLOG NODES TO JUDGE (this part):\n"
                + json.dumps(nodes, ensure_ascii=False, indent=1)
                + "\n\nJudge every node in this part as one atomic claim (use the node text and its evidence passages). "
                "Return the JSON object exactly as the spec shows, with claims for this part only. "
                "Keep each reasoning field under 30 words. Return JSON only, no markdown fences."
            )
        parsed = api_json(system, user)
        (pk / f"faith_result{part:02d}.json").write_text(
            json.dumps(parsed, ensure_ascii=False, indent=1), encoding="utf-8")
        log(f"faith part {part}: {len(parsed.get('claims', []))} claims")
        return

    if phase == "cov_check":
        CHECKLIST_DIR.mkdir(parents=True, exist_ok=True)
        cache = CHECKLIST_DIR / f"{sd.name}.json"
        if cache.exists():
            parsed = json.loads(read(cache))
            (pk / "cov_check_result.json").write_text(
                json.dumps(parsed, ensure_ascii=False, indent=1), encoding="utf-8")
            log(f"cov_check: {len(parsed.get('key_points', []))} points (cached)")
            return
        user = (
            "SOURCE (full original prose):\n" + source
            + "\n\nPhase 1 only: build the blind checklist of 8 to 15 key points as the spec describes. "
            "Return JSON only with key_points, metrics placeholders filled as zeros where unknown, "
            "and empty missing_list. No markdown fences."
        )
        parsed = api_json(system, user)
        (pk / "cov_check_result.json").write_text(
            json.dumps(parsed, ensure_ascii=False, indent=1), encoding="utf-8")
        cache.write_text(json.dumps(parsed, ensure_ascii=False, indent=1), encoding="utf-8")
        log(f"cov_check: {len(parsed.get('key_points', []))} points (cached for future runs)")
        return

    if phase == "cov_map":
        checklist = json.loads(read(pk / "cov_check_result.json"))
        user = (
            "KEY POINTS (already built, do not rebuild them):\n"
            + json.dumps(checklist.get("key_points", []), ensure_ascii=False, indent=1)
            + "\n\nLOGLOG (numbered lines):\n" + numbered
            + "\n\nPhase 2 only: map every key point to the loglog and assign Present, Partial, or Missing. "
            "Return the full JSON object per the spec with all points, evidence quotes, and computed metrics. "
            "Return JSON only, no markdown fences."
        )
        parsed = api_json(system, user)
        (pk / "cov_map_result.json").write_text(
            json.dumps(parsed, ensure_ascii=False, indent=1), encoding="utf-8")
        log(f"cov_map: {len(parsed.get('key_points', []))} points mapped")
        return

    if phase == "con":
        faith = json.loads(read(sd / "judge_faithfulness.json"))
        claims = [
            {k: c.get(k) for k in ("claim_id", "loglog_ids", "claim_text", "claim_type", "verdict")}
            for c in faith.get("claims", [])
        ]
        user = (
            "CLAIMS with verdicts from the faithfulness judge:\n"
            + json.dumps(claims, ensure_ascii=False, indent=1)
            + "\n\nLOGLOG (numbered lines):\n" + numbered
            + "\n\nLabel every claim Unique, Duplicate, Trivia, or Boilerplate per the spec, cite the canonical "
            "claim_id for duplicates, and compute the metrics. Return the full JSON object per the spec. "
            "Keep each reasoning field under 25 words. Return JSON only, no markdown fences."
        )
        parsed = api_json(system, user)
        (pk / "con_result.json").write_text(
            json.dumps(parsed, ensure_ascii=False, indent=1), encoding="utf-8")
        log(f"con: {len(parsed.get('labels', []))} labels")
        return

    if phase == "top":
        config = read(CONFIG)
        f = json.loads(read(sd / "judge_faithfulness.json"))
        c = json.loads(read(sd / "judge_coverage.json"))
        k = json.loads(read(sd / "judge_concision.json"))
        non_supported = [cl for cl in f.get("claims", []) if cl.get("verdict") != "Supported"]
        partial_points = [p for p in c.get("key_points", []) if p.get("presence") != "Present"]
        user = (
            "CONFIG (gates and weights):\n" + config
            + "\n\nFAITHFULNESS metrics:\n" + json.dumps(f.get("metrics", {}), indent=1)
            + "\nNon-Supported claims:\n" + json.dumps(non_supported, ensure_ascii=False, indent=1)
            + "\n\nCOVERAGE metrics:\n" + json.dumps(c.get("metrics", {}), indent=1)
            + "\nNon-Present key points:\n" + json.dumps(partial_points, ensure_ascii=False, indent=1)
            + "\n\nCONCISION metrics:\n" + json.dumps(k.get("metrics", {}), indent=1)
            + "\nPrune list:\n" + json.dumps(k.get("prune_list", []), ensure_ascii=False)
            + "\n\nApply the decision policy and return the JSON object per the spec with the computation shown. "
            "Return JSON only, no markdown fences."
        )
        parsed = api_json(system, user)
        (pk / "top_result.json").write_text(
            json.dumps(parsed, ensure_ascii=False, indent=1), encoding="utf-8")
        log(f"top: {parsed.get('verdict')} weighted {parsed.get('weighted_score')}")
        return

    raise SystemExit(f"unknown phase {phase}")


def merge(sample_dir):
    sd = Path(sample_dir)
    pk = sd / "packets"
    trace = sd / "trace.md"
    if not trace.exists():
        trace.write_text(f"# Judge trace (scripted pipeline, {MODEL})\n", encoding="utf-8")

    # faithfulness
    part_files = sorted(pk.glob("faith_result*.json"))
    claims = []
    for pf in part_files:
        data = json.loads(read(pf))
        for cl in data.get("claims", []):
            claims.append(cl)
    claims = [cl for cl in claims
              if (cl.get("claim_text") or "").strip()
              and cl.get("verdict") in ("Supported", "Partially supported", "Unverifiable", "Contradicted")]
    for i, cl in enumerate(claims, 1):
        cl["claim_id"] = f"C{i:03d}"
    total = len(claims)
    counts = {v: 0 for v in ("Supported", "Partially supported", "Unverifiable", "Contradicted")}
    critical = 0
    for cl in claims:
        v = cl.get("verdict", "")
        if v in counts:
            counts[v] += 1
        if cl.get("severity") == "Critical" and v != "Supported":
            critical += 1
    fam = {
        "judge": "faithfulness", "judge_version": "1.0.0",
        "model": MODEL_TAG,
        "source_id": sd.name, "claims": claims,
        "metrics": {
            "total_claims": total,
            "supported": counts["Supported"],
            "partially_supported": counts["Partially supported"],
            "unverifiable": counts["Unverifiable"],
            "contradicted": counts["Contradicted"],
            "critical_errors": critical,
            "faithfulness_precision": round(counts["Supported"] / total, 4) if total else 0.0,
        },
        "fail_list": [cl["claim_id"] for cl in claims
                      if cl.get("verdict") != "Supported"],
    }
    (sd / "judge_faithfulness.json").write_text(
        json.dumps(fam, ensure_ascii=False, indent=2), encoding="utf-8")

    # coverage (only if mapped)
    cov_out = None
    cov_path = pk / "cov_map_result.json"
    if cov_path.exists():
        cov = json.loads(read(cov_path))
        points = cov.get("key_points", [])
        must_total = sum(1 for p in points if p.get("weight") == "Must have")
        must_present = sum(1 for p in points if p.get("weight") == "Must have" and p.get("presence") == "Present")
        must_partial = sum(1 for p in points if p.get("weight") == "Must have" and p.get("presence") == "Partial")
        present = sum(1 for p in points if p.get("presence") == "Present")
        partial = sum(1 for p in points if p.get("presence") == "Partial")
        must_recall = ((must_present + 0.5 * must_partial) / must_total) if must_total else 0.0
        overall_recall = ((present + 0.5 * partial) / len(points)) if points else 0.0
        cov_out = {
            "judge": "coverage", "judge_version": "1.0.0",
            "model": MODEL_TAG,
            "source_id": sd.name, "key_points": points,
            "metrics": {
                "total_points": len(points),
                "must_have_total": must_total,
                "must_have_present": must_present,
                "must_have_partial": must_partial,
                "must_have_missing": must_total - must_present - must_partial,
                "overall_present": present,
                "must_recall": round(must_recall, 4),
                "overall_recall": round(overall_recall, 4),
            },
            "missing_list": cov.get("missing_list", []),
        }
        (sd / "judge_coverage.json").write_text(
            json.dumps(cov_out, ensure_ascii=False, indent=2), encoding="utf-8")

    # concision (only if labeled)
    con_out = None
    con_path = pk / "con_result.json"
    if con_path.exists():
        con = json.loads(read(con_path))
        labels = con.get("labels", [])
        dups = sum(1 for l in labels if l.get("label") == "Duplicate")
        trivia = sum(1 for l in labels if l.get("label") == "Trivia")
        scored = len(labels)
        con_out = {
            "judge": "concision", "judge_version": "1.0.0",
            "model": MODEL_TAG,
            "source_id": sd.name, "labels": labels,
            "metrics": {
                "scored_claims": scored,
                "unique": sum(1 for l in labels if l.get("label") == "Unique"),
                "duplicates": dups,
                "trivia": trivia,
                "redundancy_rate": round(dups / scored, 4) if scored else 0.0,
                "trivia_rate": round(trivia / scored, 4) if scored else 0.0,
                "structured_tokens": con.get("metrics", {}).get("structured_tokens", 0),
                "tokens_per_unique_claim": con.get("metrics", {}).get("tokens_per_unique_claim", 0.0),
            },
            "prune_list": con.get("prune_list", []),
        }
        (sd / "judge_concision.json").write_text(
            json.dumps(con_out, ensure_ascii=False, indent=2), encoding="utf-8")

    # top (only if decided)
    top = None
    top_path = pk / "top_result.json"
    if top_path.exists():
        top = json.loads(read(top_path))
        (sd / "judge_top.json").write_text(
            json.dumps(top, ensure_ascii=False, indent=2), encoding="utf-8")

    # trace
    with trace.open("a", encoding="utf-8") as fh:
        fh.write(f"\n## Judge F (faithfulness), {MODEL}\n\n")
        fh.write("```json\n" + json.dumps(fam, ensure_ascii=False, indent=1) + "\n```\n")
        if cov_out:
            fh.write(f"\n## Judge Cov (coverage), {MODEL}\n\n")
            fh.write("```json\n" + json.dumps(cov_out, ensure_ascii=False, indent=1) + "\n```\n")
        if con_out:
            fh.write(f"\n## Judge Con (concision), {MODEL}\n\n")
            fh.write("```json\n" + json.dumps(con_out, ensure_ascii=False, indent=1) + "\n```\n")
        if top:
            fh.write(f"\n## Judge Top (overall), {MODEL}\n\n")
            fh.write("```json\n" + json.dumps(top, ensure_ascii=False, indent=1) + "\n```\n")
    log(f"merge: {total} claims, precision {fam['metrics']['faithfulness_precision']}"
        + (f", must_recall {cov_out['metrics']['must_recall']}" if cov_out else "")
        + (f", redundancy {con_out['metrics']['redundancy_rate']}" if con_out else "")
        + (f", verdict {top.get('verdict')}" if top else ""))


def all_phases(sample_dir):
    pk = Path(sample_dir) / "packets"
    prep(sample_dir)
    parts = sorted(pk.glob("faith_part*.json"))
    for pf in parts:
        m = re.search(r"(\d+)$", pf.stem)
        run_phase(sample_dir, "faith", int(m.group(1)))
        time.sleep(5)
    run_phase(sample_dir, "cov_check")
    time.sleep(5)
    run_phase(sample_dir, "cov_map")
    time.sleep(5)
    merge(sample_dir)
    run_phase(sample_dir, "con")
    time.sleep(5)
    merge(sample_dir)
    run_phase(sample_dir, "top")
    merge(sample_dir)


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        raise SystemExit(2)
    cmd, sample = sys.argv[1], sys.argv[2]
    if cmd == "prep":
        prep(sample)
    elif cmd == "faith":
        run_phase(sample, "faith", int(sys.argv[3]))
    elif cmd in ("cov_check", "cov_map", "con", "top"):
        run_phase(sample, cmd)
    elif cmd == "merge":
        merge(sample)
    elif cmd == "all":
        all_phases(sample)
    else:
        raise SystemExit(f"unknown command {cmd}")


if __name__ == "__main__":
    main()
