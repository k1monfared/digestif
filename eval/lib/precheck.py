#!/usr/bin/env python3
"""Deterministic pre-checks for point-hierarchy outputs. No API calls.

Computes cheap approximations of what the LLM judges measure, so token
spend can target what scripts cannot decide:

1. citation coverage        (Judge Cov proxy, from graph.json)
2. exact and near duplicates (Judge Con proxy)
3. number and approximator survival per passage subtree (Judge F proxy
   for the most common precision fault class)
4. compression stats

Usage:
    python3 precheck.py <sample-dir-or-run-dir> [--json out.json]

Prints a per-sample summary plus flagged items. Stdlib only.
"""
import difflib
import json
import re
import sys
from pathlib import Path

NUMBER_RE = re.compile(
    r"(?:(?:over|about|nearly|more than|fewer than|around|roughly|up to|under|almost|~)\s+)?"
    r"(?:\d+\s*/\s*\d+|(?:[$€£])?\d[\d,]*(?:\.\d+)?(?:\s*(?:percent|%|million|billion|thousand))?)(?![\w])",
    re.I,
)


def norm(s):
    s = s.lower()
    s = re.sub(r"[\u2018\u2019\u201c\u201d]", "'", s)
    s = re.sub(r"(?<=\d),(?=\d)", "", s)
    s = re.sub(r"[^\w\s.$%/]", " ", s)
    return re.sub(r"\s+", " ", s).strip()


def numbers_in(text):
    # mask fenced code, URLs, DOIs, and list markers so non-prose digits are skipped
    text = re.sub(r"```.*?```", " ", text, flags=re.S)
    text = re.sub(r"`[^`]*`", " ", text)
    text = re.sub(r"https?://\S+|doi:\S*|10\.\d{4,}/\S*", " ", text, flags=re.I)
    text = re.sub(r"(?m)^\s*(?:\d+[.)]|[-*])\s+", " ", text)
    out = set()
    for m in NUMBER_RE.finditer(text):
        token = m.group(0).strip().lower()
        token = re.sub(r"(?<=\d),(?=\d)", "", token)
        token = re.sub(r"\s*/\s*", "/", token)
        token = token.strip(",. ")
        token = re.sub(r"\s+", " ", token)
        if re.search(r"\d", token):
            out.add(token)
    return out


def subtree_texts(nodes):
    children = {}
    for n in nodes:
        nid = n["id"]
        parent = None if nid == "0" else (nid.rsplit(".", 1)[0] if "." in nid else "0")
        if parent is not None:
            children.setdefault(parent, []).append(nid)
    by_id = {n["id"]: n for n in nodes}

    def collect(nid):
        text = by_id[nid]["text"]
        for c in children.get(nid, []):
            text += " " + collect(c)
        return text

    return {n["id"]: norm(collect(n["id"])) for n in nodes}


def looks_like_code(text):
    if "```" in text:
        return True
    if re.search(r"(?m)^(?:def |import |from |class |return |print\(|@)", text):
        return True
    indented = sum(1 for line in text.splitlines() if re.match(r"^(?:\s{4,}|\t)\S", line))
    return indented >= 2


def check_sample(sd):
    graph_path = sd / "graph.json"
    if not graph_path.exists():
        return None
    g = json.loads(graph_path.read_text(encoding="utf-8"))
    passages = g["meta"]["passages"]
    nodes = g["nodes"]
    cited = set()
    for n in nodes:
        cited.update(n.get("source", []))
    coverage = len(cited) / len(passages) if passages else 0.0

    subtrees = subtree_texts(nodes)
    graph_norm = norm(" ".join(n["text"] for n in nodes))

    citers = {}
    for n in nodes:
        for ref in n.get("source", []):
            citers.setdefault(ref, []).append(n["id"])

    dropped = []
    misplaced = []
    for ref, passage in passages.items():
        # skip code blocks and frontmatter, their digits are not prose claims
        if looks_like_code(passage) or re.search(r"(?m)^\s*(title|date|tags|layout):", passage):
            continue
        nums = numbers_in(passage)
        if not nums:
            continue
        # a number from a passage must appear in the subtree of at least one
        # node citing that passage (or anywhere in the graph, then it moved)
        citer_text = " ".join(subtrees.get(cid, "") for cid in citers.get(ref, []))
        citer_variants = {citer_text, citer_text.replace(" / ", "/")}
        for token in sorted(nums):
            bare = token.lstrip("$€£")
            if any(token in t or (bare and bare in t) for t in citer_variants):
                continue
            if token in graph_norm or (bare and bare in graph_norm):
                misplaced.append({"passage": ref, "number": token})
            else:
                dropped.append({"passage": ref, "number": token,
                                "citers": citers.get(ref, [])})

    norm_texts = {}
    for n in nodes:
        norm_texts.setdefault(norm(n["text"]), []).append(n["id"])
    exact_dups = {k: v for k, v in norm_texts.items() if len(v) > 1 and len(k) > 12}

    near_dups = []
    for i in range(len(nodes)):
        for j in range(i + 1, len(nodes)):
            ta = norm(nodes[i]["text"])
            tb = norm(nodes[j]["text"])
            if ta == tb or len(ta) < 15 or len(tb) < 15:
                continue
            ratio = difflib.SequenceMatcher(None, ta, tb).ratio()
            if ratio >= 0.88:
                near_dups.append({"a": nodes[i]["id"], "b": nodes[j]["id"], "ratio": round(ratio, 3)})

    source_words = sum(len(p.split()) for p in passages.values())
    node_words = sum(len(n["text"].split()) for n in nodes)

    return {
        "sample": sd.name,
        "nodes": len(nodes),
        "passages": len(passages),
        "coverage": round(coverage, 4),
        "uncited_passages": sorted(set(passages) - cited),
        "exact_duplicate_groups": list(exact_dups.values()),
        "near_duplicates": near_dups,
        "numbers_dropped": dropped,
        "numbers_misplaced": misplaced,
        "source_words": source_words,
        "node_words": node_words,
        "compression": round(node_words / source_words, 3) if source_words else 0,
    }


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if not args:
        print(__doc__)
        sys.exit(2)
    target = Path(args[0])
    samples = sorted(d for d in target.iterdir() if d.is_dir() and (d / "graph.json").exists()) \
        if target.is_dir() else [target]
    if not samples:
        samples = [target]
    results = []
    for sd in samples:
        r = check_sample(sd)
        if r is None:
            continue
        results.append(r)
        print(f"== {r['sample']}")
        print(f"   coverage {r['coverage']} ({r['passages'] - len(r['uncited_passages'])}/{r['passages']}), "
              f"nodes {r['nodes']}, compression {r['compression']}")
        print(f"   duplicates: {len(r['exact_duplicate_groups'])} exact groups, "
              f"{len(r['near_duplicates'])} near pairs")
        print(f"   numbers: {len(r['numbers_dropped'])} dropped, "
              f"{len(r['numbers_misplaced'])} moved across branches")
        for d in r["numbers_dropped"][:6]:
            print(f"     DROPPED {d['number']} from {d['passage']} cited by {d['citers']}")
        for m in r["numbers_misplaced"][:4]:
            print(f"     moved   {m['number']} from {m['passage']}")
        if r["uncited_passages"]:
            print(f"   UNCITED: {r['uncited_passages'][:10]}")
    if "--json" in sys.argv:
        out = Path(sys.argv[sys.argv.index("--json") + 1])
        out.write_text(json.dumps(results, ensure_ascii=False, indent=1), encoding="utf-8")
        print(f"wrote {out}")


if __name__ == "__main__":
    main()
