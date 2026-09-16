#!/usr/bin/env python3
"""Deterministic tooling for point-hierarchy graphs.

One graph.json per text is the single source of truth. Everything else
(outline.log, graph.html) is generated from it by this script. No LLM
touches the generated artifacts.

Subcommands:
  validate    check structural and citation integrity, exit 1 on errors
  stats       coverage, tree-ness, hubs, cycles
  renumber    rewrite node ids so they follow tree position exactly
  locate      add the full source text and passage character offsets
  render      generate outline.log and graph.html together
  to-outline  generate a loglog outline from the graph
  to-html     generate the interactive viewer from the graph
"""

import argparse
import json
import re
import sys
from pathlib import Path

NODE_TYPES = {
    "summary", "theme", "claim", "evidence", "example", "counterpoint",
    "rebuttal", "nuance", "concession", "contradiction", "implicit",
}

ATTRIBUTIONS = {"author", "reported", "counter", "conceded", "n/a"}

DEFAULT_EDGE_TYPES = {
    "supports":     {"direction": "directed",  "inverse": "supported-by",   "style": "solid green"},
    "exemplifies":  {"direction": "directed",  "inverse": "exemplified-by", "style": "dotted green"},
    "contradicts":  {"direction": "symmetric", "inverse": "contradicts",    "style": "solid red"},
    "qualifies":    {"direction": "directed",  "inverse": "qualified-by",   "style": "dashed blue"},
    "concedes":     {"direction": "directed",  "inverse": "conceded-by",    "style": "dashed gray"},
    "restates":     {"direction": "symmetric", "inverse": "restates",       "style": "dotted gray"},
    "precondition": {"direction": "directed",  "inverse": "prerequisite-of","style": "solid orange"},
    "contains":     {"direction": "directed",  "inverse": "contained-in",   "style": "tree"},
}

WORD_CAP = 25
ID_RE = re.compile(r"^(0|[1-9][0-9]*(\.[1-9][0-9]*)*)$")
REF_RE = re.compile(r"^¶\S+$")


class GraphError(Exception):
    pass


def merged_registry(g):
    reg = {k: dict(v) for k, v in DEFAULT_EDGE_TYPES.items()}
    for name, entry in (g.get("meta", {}).get("edgeTypes") or {}).items():
        merged = dict(reg.get(name, {}))
        merged.update(entry)
        reg[name] = merged
    return reg


def parent_of(nid):
    if nid == "0":
        return None
    return nid.rsplit(".", 1)[0] if "." in nid else "0"


def depth_of(nid):
    return 0 if nid == "0" else nid.count(".") + 1


def num_key(nid):
    return tuple(int(p) for p in nid.split("."))


def passage_key(ref):
    m = re.match(r"^¶(\d+)", str(ref))
    return (0, int(m.group(1))) if m else (1, str(ref))


def load_graph(path):
    try:
        with open(path, encoding="utf-8") as f:
            g = json.load(f)
    except json.JSONDecodeError as exc:
        raise GraphError(f"{path}: not valid JSON: {exc}")
    if not isinstance(g, dict):
        raise GraphError(f"{path}: top level must be an object")
    return g


def node_map(g):
    return {n.get("id"): n for n in g.get("nodes", [])}


def children_map(g):
    nodes = node_map(g)
    ch = {nid: [] for nid in nodes}
    for e in g.get("edges", []):
        if e.get("type") == "contains" and e.get("from") in nodes and e.get("to") in nodes:
            ch[e["from"]].append(e["to"])
    for k in ch:
        ch[k].sort(key=num_key)
    return ch


def check_refs(refs, passages, owner, errors, what="node"):
    for r in refs or []:
        r = str(r)
        if not REF_RE.match(r):
            errors.append(f"{what} {owner}: malformed passage ref '{r}' (expected ¶n)")
        elif r not in passages:
            errors.append(f"{what} {owner}: cites {r} which is not defined in meta.passages")


def validate(g):
    errors, warns = [], []
    meta = g.get("meta")
    if not isinstance(meta, dict):
        return ["meta object is missing"], [], {"cited": 0, "total": 0}
    if not str(meta.get("title", "")).strip():
        errors.append("meta.title is missing or empty")
    passages = meta.get("passages")
    if not isinstance(passages, dict) or not passages:
        errors.append("meta.passages must be a non-empty object mapping ¶n to exact source text")
        passages = {}

    nodes_list = g.get("nodes")
    if not isinstance(nodes_list, list) or not nodes_list:
        errors.append("nodes must be a non-empty list")
        nodes_list = []
    nodes = {}
    for n in nodes_list:
        if not isinstance(n, dict):
            errors.append("every node must be an object")
            continue
        nid = n.get("id")
        if not isinstance(nid, str):
            errors.append(f"node {nid!r}: id must be a string")
            continue
        if nid in nodes:
            errors.append(f"duplicate node id '{nid}'")
        nodes[nid] = n
        if not ID_RE.match(nid):
            errors.append(f"node {nid}: id must be '0' or dot-separated positive ints like '2.1'")
            continue
        ntype = n.get("type")
        if ntype not in NODE_TYPES:
            errors.append(f"node {nid}: unknown type '{ntype}' (allowed: {', '.join(sorted(NODE_TYPES))})")
        elif ntype == "summary" and nid != "0":
            errors.append(f"node {nid}: type 'summary' is reserved for the root node")
        text = n.get("text")
        if not isinstance(text, str) or not text.strip():
            errors.append(f"node {nid}: text is missing or empty")
        elif len(text.split()) > WORD_CAP:
            warns.append(f"node {nid}: text exceeds {WORD_CAP} words ({len(text.split())}), keep nodes atomic")
        attr = n.get("attribution", "n/a")
        if attr not in ATTRIBUTIONS:
            errors.append(f"node {nid}: unknown attribution '{attr}' (allowed: {', '.join(sorted(ATTRIBUTIONS))})")
        src = n.get("source")
        if not isinstance(src, list) or not src:
            errors.append(f"node {nid}: source citations are missing, every node must cite where it comes from")
        else:
            check_refs(src, passages, nid, errors)

    if "0" not in nodes:
        errors.append("there must be exactly one root node with id '0'")
    else:
        root = nodes["0"]
        if root.get("type") != "summary":
            errors.append("root node '0' must have type 'summary'")
        if not isinstance(root.get("text"), str) or not str(root.get("text", "")).strip():
            errors.append("root node '0': summary text is missing")
        elif len(root["text"].split()) > 30:
            warns.append("root summary exceeds 30 words, keep it to one short sentence")
        if not isinstance(root.get("source"), list) or not root.get("source"):
            errors.append("root summary must cite the passages it summarizes")

    reg = merged_registry(g)
    for name, entry in reg.items():
        if not isinstance(entry, dict) or entry.get("direction") not in ("directed", "symmetric"):
            errors.append(f"edge type registry entry '{name}' needs direction 'directed' or 'symmetric'")

    contains_into, contains_seen = {}, set()
    for e in g.get("edges", []):
        if not isinstance(e, dict):
            errors.append("every edge must be an object")
            continue
        f, t, ty = e.get("from"), e.get("to"), e.get("type")
        label = f"edge {f}->{t} ({ty})"
        if ty not in reg:
            errors.append(f"{label}: undeclared type, add it to meta.edgeTypes or use a built-in")
        elif (reg[ty].get("direction") == "symmetric" and isinstance(f, str) and isinstance(t, str)
              and ID_RE.match(f) and ID_RE.match(t) and num_key(f) > num_key(t)):
            warns.append(f"{label}: symmetric edge stored reversed, canonical form is {t}->{f}")
        if f not in nodes:
            errors.append(f"{label}: unknown source node")
        if t not in nodes:
            errors.append(f"{label}: unknown target node")
        if f == t:
            errors.append(f"{label}: self loops are not allowed")
        check_refs(e.get("source"), passages, f"{f}->{t}", errors, what="edge")
        if ty == "contains":
            key = (f, t)
            if key in contains_seen:
                errors.append(f"{label}: duplicate contains edge")
            contains_seen.add(key)
            if f in nodes and t in nodes and parent_of(t) != f:
                errors.append(f"{label}: contradicts id structure, parent of '{t}' is '{parent_of(t)}'")
            contains_into[t] = contains_into.get(t, 0) + 1

    for nid, n in nodes.items():
        if not isinstance(nid, str) or not ID_RE.match(nid):
            continue
        if nid == "0":
            if nid in contains_into:
                errors.append("root node '0' must not have an incoming contains edge")
        else:
            p = parent_of(nid)
            if p not in nodes:
                errors.append(f"node {nid}: parent '{p}' does not exist")
            elif contains_into.get(nid, 0) == 0:
                errors.append(f"node {nid}: no contains edge from parent '{p}'")
            elif contains_into.get(nid, 0) > 1:
                errors.append(f"node {nid}: has multiple contains parents")

    spans = meta.get("spans")
    source_text = meta.get("sourceText")
    if spans is not None:
        if not isinstance(spans, dict):
            errors.append("meta.spans must be an object mapping ¶n to [start, end]")
        elif not isinstance(source_text, str) or not source_text:
            errors.append("meta.spans is present but meta.sourceText is missing, run locate to fill both")
        else:
            prev_end = -1
            for pref in sorted(passages, key=passage_key):
                if pref not in spans:
                    errors.append(f"meta.spans is missing an entry for {pref}")
                    continue
                span = spans[pref]
                if (not isinstance(span, list) or len(span) != 2
                        or not all(isinstance(x, int) for x in span)):
                    errors.append(f"meta.spans[{pref}] must be [start, end] integers")
                    continue
                s, e = span
                if s < 0 or e < s or e > len(source_text):
                    errors.append(f"meta.spans[{pref}] out of range: [{s}, {e}] for {len(source_text)} chars")
                    continue
                if source_text[s:e] != passages[pref]:
                    errors.append(f"meta.spans[{pref}] does not match meta.passages[{pref}]: source text at [{s}, {e}] differs from the copied passage")
                if s < prev_end:
                    warns.append(f"meta.spans[{pref}] starts before the previous passage ends, spans overlap or are out of order")
                prev_end = e
            extra = [k for k in spans if k not in passages]
            if extra:
                errors.append(f"meta.spans has entries with no passage: {', '.join(extra)}")
    elif isinstance(source_text, str) and source_text:
        warns.append("meta.sourceText is present without meta.spans, run locate to add offsets")

    cited = set()
    for n in nodes_list:
        if isinstance(n, dict):
            cited.update(str(r) for r in n.get("source") or [])
    for e in g.get("edges", []):
        if isinstance(e, dict):
            cited.update(str(r) for r in e.get("source") or [])
    uncited = sorted((p for p in passages if p not in cited), key=passage_key)
    if uncited:
        warns.append(f"{len(uncited)} passage(s) not cited by any node: {', '.join(uncited)}")

    info = {"cited": len([p for p in passages if p in cited]), "total": len(passages),
            "uncited": uncited}
    return errors, warns, info


def cross_edges(g):
    return [e for e in g.get("edges", []) if e.get("type") != "contains"]


def cross_cycles(g):
    residual_in, residual_out = {}, {}
    for e in cross_edges(g):
        f, t = e.get("from"), e.get("to")
        if f == t:
            continue
        residual_out.setdefault(f, set()).add(t)
        residual_in.setdefault(t, set()).add(f)
    changed = True
    while changed:
        changed = False
        for n in list(residual_out):
            if not residual_out.get(n) and not residual_in.get(n):
                continue
            if not residual_out.get(n):
                for p in residual_in.pop(n, set()):
                    residual_out.get(p, set()).discard(n)
                residual_in.pop(n, None)
                residual_out.pop(n, None)
                changed = True
            elif not residual_in.get(n):
                for c in list(residual_out.get(n, ())):
                    residual_in.get(c, set()).discard(n)
                residual_out.pop(n, None)
                changed = True
    involved = set(residual_out) | set(residual_in)
    return [e for e in cross_edges(g) if e.get("from") in involved and e.get("to") in involved]


def hub_nodes(g, top=5):
    degree = {}
    for e in cross_edges(g):
        for end in (e.get("from"), e.get("to")):
            degree[end] = degree.get(end, 0) + 1
    ranked = sorted(degree.items(), key=lambda kv: (-kv[1], num_key(kv[0])))
    return ranked[:top]


def cmd_validate(args):
    g = load_graph(args.graph)
    errors, warns, info = validate(g)
    nodes = node_map(g)
    n_edges = len(g.get("edges", []))
    for w in warns:
        print(f"warning: {w}")
    for e in errors:
        print(f"error: {e}")
    cov = f"coverage {info['cited']}/{info['total']} passages"
    if errors:
        print(f"INVALID: {len(errors)} error(s), {len(warns)} warning(s). {cov}. "
              f"{len(nodes)} nodes, {n_edges} edges.")
        return 1
    print(f"OK: graph is valid. {len(nodes)} nodes, {n_edges} edges. {cov}. "
          f"{len(warns)} warning(s).")
    return 0


def cmd_stats(args):
    g = load_graph(args.graph)
    errors, warns, info = validate(g)
    nodes = node_map(g)
    edges = g.get("edges", [])
    crosses = cross_edges(g)

    by_type, by_depth = {}, {}
    for n in nodes.values():
        by_type[n.get("type", "?")] = by_type.get(n.get("type", "?"), 0) + 1
        if isinstance(n.get("id"), str) and ID_RE.match(n.get("id", "")):
            d = depth_of(n["id"])
            by_depth[d] = by_depth.get(d, 0) + 1
    by_etype = {}
    for e in edges:
        by_etype[e.get("type", "?")] = by_etype.get(e.get("type", "?"), 0) + 1
    hubs = hub_nodes(g)
    cycles = cross_cycles(g)

    report = {
        "nodes": len(nodes),
        "edges": len(edges),
        "cross_edges": len(crosses),
        "coverage": {"cited": info["cited"], "total": info["total"]},
        "uncited_passages": info["uncited"],
        "nodes_by_type": by_type,
        "nodes_by_depth": {str(k): by_depth[k] for k in sorted(by_depth)},
        "edges_by_type": by_etype,
        "max_depth": max(by_depth) if by_depth else 0,
        "tree_ratio": round(1 - len(crosses) / len(edges), 3) if edges else None,
        "hub_nodes": [{"id": nid, "cross_degree": d, "text": nodes.get(nid, {}).get("text", "")}
                      for nid, d in hubs],
        "cyclic_cross_edges": len(cycles),
        "warnings": warns,
        "errors": errors,
    }
    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        print(f"nodes: {report['nodes']}  edges: {report['edges']}  "
              f"cross-edges: {report['cross_edges']}  max depth: {report['max_depth']}")
        print(f"coverage: {info['cited']}/{info['total']} passages cited")
        if info["uncited"]:
            print(f"uncited: {', '.join(info['uncited'])}")
        print("nodes by type: " + ", ".join(f"{k} {v}" for k, v in sorted(by_type.items())))
        print("nodes by layer: " + ", ".join(f"L{k} {v}" for k, v in sorted(by_depth.items())))
        print("edges by type: " + ", ".join(f"{k} {v}" for k, v in sorted(by_etype.items())))
        print(f"tree ratio: {report['tree_ratio']}")
        print("hubs (most cross-linked):")
        for h in hubs:
            print(f"  {h[0]}  degree {h[1]}  {nodes.get(h[0], {}).get('text', '')[:60]}")
        print(f"cyclic cross-edges: {report['cyclic_cross_edges']}")
        for w in warns:
            print(f"warning: {w}")
        for e in errors:
            print(f"error: {e}")
    return 0


def cmd_renumber(args):
    g = load_graph(args.graph)
    errors, _, _ = validate(g)
    if errors and not args.force:
        for e in errors:
            print(f"error: {e}", file=sys.stderr)
        print("refusing to renumber an invalid graph, use --force to override", file=sys.stderr)
        return 1
    ch = {nid: [] for nid in node_map(g)}
    for n in g["nodes"]:
        p = parent_of(n["id"])
        if p in ch:
            ch[p].append(n["id"])
    nodes_by_id = node_map(g)
    mapping = {}
    new_nodes = []

    def visit(nid, new_id):
        mapping[nid] = new_id
        nn = dict(nodes_by_id[nid])
        nn["id"] = new_id
        new_nodes.append(nn)
        for i, c in enumerate(ch[nid], 1):
            visit(c, str(i) if new_id == "0" else f"{new_id}.{i}")

    visit("0", "0")
    for e in g.get("edges", []):
        e["from"] = mapping.get(e["from"], e["from"])
        e["to"] = mapping.get(e["to"], e["to"])
    g["nodes"] = new_nodes
    moved = sum(1 for old, new in mapping.items() if old != new)
    if args.verbose:
        for old, new in mapping.items():
            if old != new:
                print(f"{old} -> {new}")
    out = json.dumps(g, ensure_ascii=False, indent=2) + "\n"
    if args.in_place:
        Path(args.graph).write_text(out, encoding="utf-8")
        print(f"renumbered {len(mapping)} nodes ({moved} id changes) in {args.graph}")
    else:
        sys.stdout.write(out)
    return 0


def fmt_reflist(refs):
    return "(" + ", ".join(str(r) for r in refs) + ")" if refs else ""


def node_line(n):
    nid = n["id"]
    parts = []
    if nid != "0":
        parts.append(nid)
    if n.get("type") not in ("claim", "summary"):
        parts.append(str(n.get("type", ""))[:1].upper() + str(n.get("type", ""))[1:] + ":")
    parts.append(n.get("text", ""))
    refs = fmt_reflist(n.get("source"))
    if refs:
        parts.append(refs)
    if n.get("attribution") not in ("author", "n/a", None):
        parts.append(f"[{n['attribution']}]")
    return "- " + " ".join(parts)


def to_outline_text(g):
    errors, warns, info = validate(g)
    if errors:
        for e in errors:
            print(f"error: {e}", file=sys.stderr)
        raise GraphError("refusing to render an invalid graph")
    meta = g.get("meta", {})
    nodes = node_map(g)
    ch = children_map(g)
    lines = []
    header = f"- {meta.get('title', 'Untitled')}"
    if meta.get("source"):
        header += f" (source: {meta['source']})"
    lines.append(header)
    if "0" in nodes:
        lines.append("    " + node_line(nodes["0"]).replace("- ", "Summary: ", 1))

    def walk(nid, depth):
        for c in ch.get(nid, []):
            lines.append("    " * depth + node_line(nodes[c]))
            walk(c, depth + 1)

    if "0" in nodes:
        walk("0", 2)
    crosses = sorted(cross_edges(g),
                     key=lambda e: (num_key(e["from"]), num_key(e["to"]), str(e["type"])))
    lines.append("    - Cross-links")
    if crosses:
        for e in crosses:
            bits = [f"{e['from']} {e['type']} {e['to']}"]
            refs = fmt_reflist(e.get("source"))
            if refs:
                bits.append(refs)
            if e.get("note"):
                bits.append(f"note: {e['note']}")
            lines.append("        - " + " ".join(bits))
    else:
        lines.append("        - none")
    cov = f"- Coverage: {info['cited']} of {info['total']} passages cited"
    lines.append("    " + cov)
    if info["uncited"]:
        lines.append("    - Uncited passages: " + ", ".join(info["uncited"]))
    return "\n".join(lines) + "\n"


def cmd_locate(args):
    g = load_graph(args.graph)
    try:
        text = Path(args.source).read_text(encoding="utf-8")
    except OSError as exc:
        print(f"error: cannot read source {args.source}: {exc}", file=sys.stderr)
        return 1
    passages = (g.get("meta") or {}).get("passages") or {}
    if not passages:
        print("error: meta.passages is empty, nothing to locate", file=sys.stderr)
        return 1
    spans = {}
    cursor = 0
    for pref in sorted(passages, key=passage_key):
        ptext = str(passages[pref])
        pos = text.find(ptext, cursor)
        if pos == -1:
            before = text.find(ptext)
            if before == -1:
                print(f"error: passage {pref} not found verbatim in {args.source}", file=sys.stderr)
            else:
                print(f"error: passage {pref} found before an earlier passage, passages are out of order", file=sys.stderr)
            return 1
        spans[pref] = [pos, pos + len(ptext)]
        cursor = pos + len(ptext)
    meta = g.setdefault("meta", {})
    meta["sourceText"] = text
    meta["spans"] = spans
    out = json.dumps(g, ensure_ascii=False, indent=2) + "\n"
    if args.in_place:
        Path(args.graph).write_text(out, encoding="utf-8")
        print(f"located {len(spans)} passages in {len(text)} chars, wrote {args.graph}")
    else:
        sys.stdout.write(out)
    return 0


def cmd_to_outline(args):
    g = load_graph(args.graph)
    text = to_outline_text(g)
    if args.out:
        Path(args.out).write_text(text, encoding="utf-8")
        print(f"wrote {args.out}")
    else:
        sys.stdout.write(text)
    return 0


def render_html(g, out):
    embedded = json.loads(json.dumps(g))
    embedded.setdefault("meta", {})["edgeTypes"] = merged_registry(g)
    template_path = Path(__file__).resolve().parent.parent / "templates" / "viewer.html"
    try:
        template = template_path.read_text(encoding="utf-8")
    except OSError as exc:
        raise GraphError(f"cannot read viewer template {template_path}: {exc}")
    if "__GRAPH_JSON__" not in template:
        raise GraphError(f"viewer template {template_path} has no __GRAPH_JSON__ token")
    payload = json.dumps(embedded, ensure_ascii=False).replace("</", "<\\/")
    Path(out).write_text(template.replace("__GRAPH_JSON__", payload), encoding="utf-8")


def cmd_to_html(args):
    g = load_graph(args.graph)
    errors, _, _ = validate(g)
    if errors and not args.force:
        for e in errors:
            print(f"error: {e}", file=sys.stderr)
        print("refusing to render an invalid graph, use --force to override", file=sys.stderr)
        return 1
    out = args.out or str(Path(args.graph).with_suffix("").with_name(
        Path(args.graph).stem.replace(".graph", "") + ".graph.html"))
    try:
        render_html(g, out)
    except GraphError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    print(f"wrote {out}")
    return 0


def cmd_render(args):
    g = load_graph(args.graph)
    errors, _, _ = validate(g)
    if errors and not args.force:
        for e in errors:
            print(f"error: {e}", file=sys.stderr)
        print("refusing to render an invalid graph, use --force to override", file=sys.stderr)
        return 1
    base = Path(args.graph)
    outdir = Path(args.outdir) if args.outdir else base.parent
    outdir.mkdir(parents=True, exist_ok=True)
    if base.stem == "graph":
        outline_path = outdir / "outline.log"
        html_path = outdir / "graph.html"
    else:
        stem = base.stem[:-6] if base.stem.endswith(".graph") else base.stem
        outline_path = outdir / f"{stem}.outline.log"
        html_path = outdir / f"{stem}.graph.html"
    outline_path.write_text(to_outline_text(g), encoding="utf-8")
    try:
        render_html(g, html_path)
    except GraphError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    print(f"wrote {outline_path}")
    print(f"wrote {html_path}")
    return 0


def main(argv=None):
    p = argparse.ArgumentParser(prog="graph.py", description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)

    v = sub.add_parser("validate", help="check graph integrity and citations")
    v.add_argument("graph")
    v.set_defaults(func=cmd_validate)

    s = sub.add_parser("stats", help="coverage, tree-ness, hubs, cycles")
    s.add_argument("graph")
    s.add_argument("--json", action="store_true", help="machine-readable output")
    s.set_defaults(func=cmd_stats)

    r = sub.add_parser("renumber", help="rewrite node ids to canonical tree positions")
    r.add_argument("graph")
    r.add_argument("-i", "--in-place", action="store_true")
    r.add_argument("-f", "--force", action="store_true")
    r.add_argument("-v", "--verbose", action="store_true")
    r.set_defaults(func=cmd_renumber)

    lo = sub.add_parser("locate", help="add sourceText and passage character offsets from the source file")
    lo.add_argument("graph")
    lo.add_argument("source")
    lo.add_argument("-i", "--in-place", action="store_true")
    lo.set_defaults(func=cmd_locate)

    o = sub.add_parser("to-outline", help="generate loglog outline")
    o.add_argument("graph")
    o.add_argument("-o", "--out", help="output .log path, default stdout")
    o.set_defaults(func=cmd_to_outline)

    h = sub.add_parser("to-html", help="generate interactive viewer")
    h.add_argument("graph")
    h.add_argument("-o", "--out", help="output .html path, default next to the graph")
    h.add_argument("-f", "--force", action="store_true")
    h.set_defaults(func=cmd_to_html)

    rn = sub.add_parser("render", help="generate outline and viewer in one step")
    rn.add_argument("graph")
    rn.add_argument("-o", "--outdir", help="output directory, default next to the graph")
    rn.add_argument("-f", "--force", action="store_true")
    rn.set_defaults(func=cmd_render)

    args = p.parse_args(argv)
    try:
        return args.func(args)
    except GraphError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
