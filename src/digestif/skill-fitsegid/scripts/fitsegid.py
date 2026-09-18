#!/usr/bin/env python3
"""Deterministic checker for fitsegid prose, the inverse of digestif.

Digestif condenses a text into a cited idea graph. Fitsegid tells that graph
back as prose. This script is the only non-LLM check in that direction: it
proves that every sentence of the prose is grounded in graph nodes, that every
node survives into the prose or is listed as intentionally dropped, and that
numbers and names did not appear out of nowhere.

Subcommands:
  check-prose  verify NAME.fitsegid.md against graph.json or an outline.log
  strip-prose  remove citations and frontmatter, writing the clean reading copy

The prose is the only file an LLM writes. The clean copy is generated here.
"""

import argparse
import json
import re
import sys
from pathlib import Path

ID_RE = re.compile(r"^(0|[1-9][0-9]*(\.[1-9][0-9]*)*)$")
CITATION_BLOCK_RE = re.compile(r"(?<![!\[])\[([0-9][0-9.,\s]*)\](?!\s*[:(])")
NUMBER_RE = re.compile(r"\d[\d,]*(?:\.\d+)?")
WORD_RE = re.compile(r"[A-Za-z][A-Za-z'-]*")
SENT_BOUNDARY_RE = re.compile(r"[.!?]+(?:\s*\[[0-9][0-9.,\s]*\])*")
ATTR_RE = re.compile(r"\s*\[([a-z/]+)\]\s*$")
REFS_RE = re.compile(r"\s*\((¶[^()]*)\)\s*$")
NODE_RE = re.compile(r"^(\d+(?:\.\d+)*)\s+(.*)$")
TYPE_RE = re.compile(
    r"^(Summary|Theme|Claim|Evidence|Example|Counterpoint|Rebuttal|Nuance|"
    r"Concession|Contradiction|Implicit):\s*(.*)$",
    re.S,
)

CUE_WORDS = (
    "argu", "claim", "say", "said", "critic", "suggest", "concede", "admit",
    "objection", "oppos", "counter", "may", "might", "report", "accord",
    "allege", "supposed", "purport", "insist", "maintain", "assert",
)

COMMON_CAPS = {
    "The", "This", "That", "These", "Those", "There", "Their", "They", "Then",
    "Thus", "But", "And", "Yet", "So", "However", "Admittedly", "Indeed",
    "Still", "Nevertheless", "Because", "While", "When", "If", "Once", "Both",
    "Each", "Every", "Most", "Some", "No", "Not", "Only", "Even", "Such",
    "What", "Which", "Who", "Where", "His", "Her", "Its", "Our", "We", "You",
    "He", "She", "It", "In", "On", "At", "For", "To", "By", "As", "A", "An",
    "I",
}


class FitsegidError(Exception):
    pass


def parent_of(nid):
    if nid == "0":
        return None
    return nid.rsplit(".", 1)[0] if "." in nid else "0"


def depth_of(nid):
    return 0 if nid == "0" else nid.count(".") + 1


def num_key(nid):
    return tuple(int(p) for p in nid.split("."))


def load_graph(path):
    try:
        with open(path, encoding="utf-8") as f:
            g = json.load(f)
    except json.JSONDecodeError as exc:
        raise FitsegidError(f"{path}: not valid JSON: {exc}")
    except OSError as exc:
        raise FitsegidError(f"cannot read {path}: {exc}")
    if not isinstance(g, dict):
        raise FitsegidError(f"{path}: top level must be an object")
    nodes = {}
    for n in g.get("nodes", []):
        if isinstance(n, dict) and isinstance(n.get("id"), str):
            nodes[n["id"]] = n
    passages = (g.get("meta") or {}).get("passages") or {}
    return nodes, passages


def parse_outline(text):
    """Recover nodes from a loglog outline.log produced by digestif."""
    nodes = {}
    in_cross = False
    for raw in text.splitlines():
        if not raw.strip():
            continue
        indent = len(raw) - len(raw.lstrip(" "))
        s = raw.strip()
        if indent == 0:
            continue
        if indent == 4:
            if s.startswith("- Cross-links"):
                in_cross = True
            elif s.startswith("- Coverage:") or s.startswith("- Uncited"):
                in_cross = False
            elif s.startswith("Summary:"):
                body = REFS_RE.sub("", s[len("Summary:"):].strip()).strip()
                nodes["0"] = {"id": "0", "type": "summary", "text": body,
                              "attribution": "author", "source": []}
            continue
        if indent < 8 or in_cross or not s.startswith("- "):
            continue
        body = s[2:].strip()
        m = NODE_RE.match(body)
        if not m:
            continue
        nid, rest = m.group(1), m.group(2)
        rest, attribution = _strip_attr(rest)
        rest, refs = _strip_refs(rest)
        t = TYPE_RE.match(rest)
        ntype, text = (t.group(1).lower(), t.group(2)) if t else ("claim", rest)
        nodes[nid] = {"id": nid, "type": ntype, "text": text.strip(),
                      "attribution": attribution, "source": refs}
    return nodes, {}


def _strip_attr(rest):
    m = ATTR_RE.search(rest)
    if m:
        return rest[:m.start()].rstrip(), m.group(1)
    return rest, "n/a"


def _strip_refs(rest):
    m = REFS_RE.search(rest)
    if m:
        return rest[:m.start()].rstrip(), [r.strip() for r in m.group(1).split(",")]
    return rest, []


def parse_frontmatter(text, errors):
    if not text.lstrip("\ufeff").startswith("---"):
        errors.append("frontmatter: file must start with '---' and a lod line")
        return {}, text
    lines = text.lstrip("\ufeff").splitlines()
    end = None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            end = i
            break
    if end is None:
        errors.append("frontmatter: missing closing '---'")
        return {}, text
    meta = {}
    for line in lines[1:end]:
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if ":" not in line:
            errors.append(f"frontmatter: bad line '{line}', expected key: value")
            continue
        key, value = line.split(":", 1)
        meta[key.strip()] = value.strip()
    return meta, "\n".join(lines[end + 1:])


def split_sentences(block):
    sentences, start = [], 0
    for m in SENT_BOUNDARY_RE.finditer(block):
        end = m.end()
        if end == len(block) or block[end].isspace():
            chunk = block[start:end].strip()
            if chunk:
                sentences.append(chunk)
            start = end
    tail = block[start:].strip()
    if tail:
        sentences.append(tail)
    return sentences


def citations_in(text, errors, where):
    ids = []
    for m in CITATION_BLOCK_RE.finditer(text):
        for token in m.group(1).replace(",", " ").split():
            if ID_RE.match(token):
                ids.append(token)
            else:
                errors.append(f"{where}: malformed citation '[{token}]'")
    return ids


def material(nodes, passages, ids):
    parts = []
    for nid in ids:
        node = nodes.get(nid)
        if not node:
            continue
        parts.append(str(node.get("text", "")))
        for ref in node.get("source") or []:
            if ref in passages:
                parts.append(str(passages[ref]))
    return "\n".join(parts)


def check(nodes, passages, prose):
    errors, warns = [], []
    meta, body = parse_frontmatter(prose, errors)

    lod = meta.get("lod")
    if lod is None:
        errors.append("frontmatter: 'lod' is missing (use 'max' or a layer count)")
        lod = "max"
    elif lod != "max" and not lod.isdigit():
        errors.append(f"frontmatter: lod '{lod}' must be 'max' or a whole number of layers")
    raw_dropped = meta.get("dropped", "[]")
    try:
        parsed = json.loads(raw_dropped)
        if not isinstance(parsed, list):
            raise ValueError("not a list")
        dropped = [str(d) for d in parsed]
    except (json.JSONDecodeError, ValueError, TypeError):
        errors.append("frontmatter: 'dropped' must be a JSON list like [] or [\"1.2\"]")
        dropped = []
    dropped_set = set(dropped)

    if lod == "max" and dropped_set:
        errors.append("frontmatter: lod is 'max' but dropped is not empty, max means lossless")

    for d in dropped_set:
        if d not in nodes:
            errors.append(f"frontmatter: dropped '{d}' is not a node in the graph")

    sentences = []
    for lineno, line in enumerate(body.splitlines(), 1):
        s = line.strip()
        if not s or s.startswith("#"):
            continue
        if s[:2] in ("- ", "* ", "+ "):
            s = s[2:].strip()
        for sent in split_sentences(s):
            sentences.append((lineno, sent))

    first_seen, cited_all = {}, set()
    for idx, (lineno, sent) in enumerate(sentences):
        cited = citations_in(sent, errors, f"line {lineno}")
        where = f"line {lineno}"
        if not cited:
            errors.append(f"{where}: sentence has no citation: '{_trim(sent)}'")
            continue
        clean = CITATION_BLOCK_RE.sub("", sent).strip()
        mat = material(nodes, passages, cited)
        low = mat.lower()

        for c in cited:
            if c not in nodes:
                errors.append(f"{where}: cites '{c}' which is not a node")
            elif c in dropped_set:
                errors.append(f"{where}: cites '{c}' which is listed as dropped")
            cited_all.add(c)
            first_seen.setdefault(c, idx)

        for num in NUMBER_RE.findall(clean):
            plain = num.replace(",", "")
            if num not in mat and plain not in low.replace(",", ""):
                warns.append(f"{where}: number '{num}' does not appear in the cited nodes or passages")

        if any(nodes.get(c, {}).get("attribution") in ("counter", "conceded") for c in cited):
            if not any(cue in clean.lower() for cue in CUE_WORDS):
                warns.append(f"{where}: uses a counter or conceded node without attributing it")

        words = WORD_RE.findall(clean)
        for j, word in enumerate(words):
            if j == 0 or len(word) < 2 or not word[0].isupper():
                continue
            if word in COMMON_CAPS:
                continue
            if word not in mat and word.lower() not in low:
                warns.append(f"{where}: '{word}' does not appear in the cited nodes or passages")

    for nid in nodes:
        if nid not in cited_all and nid not in dropped_set:
            errors.append(f"node {nid} is neither cited in the prose nor listed in dropped")

    if lod.isdigit():
        limit = int(lod)
        for nid in nodes:
            if depth_of(nid) > limit and nid not in dropped_set:
                errors.append(f"node {nid} is deeper than lod {limit} but is not listed in dropped")
        for nid in sorted(cited_all, key=num_key):
            if depth_of(nid) > limit:
                errors.append(f"node {nid} is cited but deeper than lod {limit}")

    for nid, idx in first_seen.items():
        p = parent_of(nid)
        if p in first_seen and first_seen[p] > idx:
            warns.append(f"node {nid} is cited before its parent {p}")

    stats = {
        "nodes": len(nodes),
        "cited": len(cited_all),
        "dropped": len(dropped_set),
        "sentences": len(sentences),
        "citations": sum(len(citations_in(s, [], "")) for _, s in sentences),
        "lod": lod,
    }
    return errors, sorted(set(warns)), stats


def _trim(text, limit=60):
    text = " ".join(text.split())
    return text if len(text) <= limit else text[: limit - 1] + "…"


def cmd_check(args):
    try:
        prose = Path(args.prose).read_text(encoding="utf-8")
    except OSError as exc:
        print(f"error: cannot read prose {args.prose}: {exc}", file=sys.stderr)
        return 1
    if args.outline and args.graph:
        print("error: pass either a graph.json or --outline, not both", file=sys.stderr)
        return 1
    try:
        if args.outline:
            nodes, passages = parse_outline(
                Path(args.outline).read_text(encoding="utf-8"))
            source = args.outline
        else:
            graph_path = args.graph
            if graph_path and Path(graph_path).is_dir():
                graph_path = str(Path(graph_path) / "graph.json")
            if not graph_path:
                print("error: pass a graph.json (or --outline outline.log)", file=sys.stderr)
                return 1
            nodes, passages = load_graph(graph_path)
            source = graph_path
    except FitsegidError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    if not nodes:
        print(f"error: no nodes found in {source}", file=sys.stderr)
        return 1

    errors, warns, stats = check(nodes, passages, prose)
    if args.strict:
        errors = errors + warns
        warns = []
    for w in warns:
        print(f"warning: {w}")
    for e in errors:
        print(f"error: {e}")
    summary = (f"{stats['cited']}/{stats['nodes']} nodes realized, "
               f"{stats['dropped']} dropped, {stats['sentences']} sentences, "
               f"{stats['citations']} citations, lod {stats['lod']}")
    if errors:
        print(f"INVALID: {len(errors)} error(s), {len(warns)} warning(s). {summary}.")
        return 1
    print(f"OK: prose is grounded. {summary}. {len(warns)} warning(s).")
    return 0


def strip_citations(text):
    text = CITATION_BLOCK_RE.sub("", text)
    text = re.sub(r"[ \t]{2,}", " ", text)
    text = "\n".join(line.rstrip() for line in text.splitlines())
    return re.sub(r"\n{3,}", "\n\n", text).strip() + "\n"


def cmd_strip(args):
    try:
        prose = Path(args.prose).read_text(encoding="utf-8")
    except OSError as exc:
        print(f"error: cannot read prose {args.prose}: {exc}", file=sys.stderr)
        return 1
    meta, body = parse_frontmatter(prose, [])
    clean = strip_citations(body)
    if args.out:
        out = Path(args.out)
    else:
        p = Path(args.prose)
        out = p.with_name(p.stem + "-clean" + p.suffix)
    out.write_text(clean, encoding="utf-8")
    print(f"wrote {out}")
    return 0


def main(argv=None):
    p = argparse.ArgumentParser(prog="fitsegid.py", description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)

    c = sub.add_parser("check-prose", help="verify prose against a graph or outline")
    c.add_argument("prose", help="path to NAME.fitsegid.md")
    c.add_argument("graph", nargs="?", help="path to graph.json or a run directory")
    c.add_argument("--outline", help="use a digestif outline.log instead of graph.json")
    c.add_argument("--strict", action="store_true", help="treat warnings as errors")
    c.set_defaults(func=cmd_check)

    s = sub.add_parser("strip-prose", help="write the clean copy without citations")
    s.add_argument("prose", help="path to NAME.fitsegid.md")
    s.add_argument("-o", "--out", help="output path, default NAME.fitsegid-clean.md")
    s.set_defaults(func=cmd_strip)

    args = p.parse_args(argv)
    try:
        return args.func(args)
    except FitsegidError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
