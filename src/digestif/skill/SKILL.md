---
name: digestif
description: Extract a rooted, fully cited idea graph from any text. The graph.json is the single working artifact the LLM iterates on. The loglog outline and the interactive zoomable viewer are generated afterwards by deterministic Python, never by the LLM.
allowed-tools: Read, Write, Edit, Bash
argument-hint: [path-to-text or pasted text]
tags: [analysis, loglog, knowledge-graph]
version: 0.4.0
---

# Digestif

Turn a text into one rooted idea graph. The root is a single-sentence summary of the whole document. Its children are the main points. Below them sit the details of each point, and below those the evidence, examples, counterpoints, and nuances, as deep as the text goes. Typed links connect any two ideas across any distance: this evidence supports that claim, this detail contradicts that one, this example illustrates two different points at once.

Nothing from the text is dropped, nothing is invented, and every idea points back to the exact passage it came from.

## Artifacts and the iron rule

One run produces three files:

```
name.graph.json     canonical working file, the LLM creates and edits this
name.outline.log    generated loglog outline, for reading and printing
name.graph.html     generated interactive viewer, for exploring
```

The iron rule: `graph.json` is the only file the LLM ever writes after the source is split into passages. The outline and the viewer are produced by `scripts/graph.py` and must never be hand-written or hand-edited. This is what makes hallucination mechanically detectable instead of a matter of trust.

All commands run from the skill directory:

```bash
python3 scripts/graph.py validate name.graph.json    # integrity + citation check, exit 1 on error
python3 scripts/graph.py stats name.graph.json       # coverage, tree-ness, hubs, cycles
python3 scripts/graph.py renumber name.graph.json -i # canonicalize node ids after restructuring
python3 scripts/graph.py locate name.graph.json source.txt -i # add sourceText and passage offsets
python3 scripts/graph.py render name.graph.json      # outline.log and graph.html in one step
python3 scripts/graph.py to-outline name.graph.json -o name.outline.log
python3 scripts/graph.py to-html name.graph.json -o name.graph.html
```

Any graph that passes `validate` renders, whatever its size, depth, or shape: hundreds of nodes, any number of layers, custom node types listed in the schema, and custom edge types declared in `meta.edgeTypes`. The viewer reads everything from the graph: node colors from the node types, legend and edge styling from the edge-type registry, layers from the tree depth. Nothing in the viewer is specific to one document.

## Graph schema

```json
{
  "meta": {
    "title": "short title",
    "source": "original file name",
    "sourceText": "full text of the source, added by locate",
    "passages": { "¶1": "exact text of first passage", "¶2": "..." },
    "spans": { "¶1": [0, 42], "¶2": [43, 152] }
  },
  "nodes": [
    { "id": "0", "type": "summary", "text": "one-sentence summary",
      "attribution": "author", "source": ["¶1", "¶5"] },
    { "id": "1", "type": "claim", "text": "...", "attribution": "author", "source": ["¶2"] }
  ],
  "edges": [
    { "from": "0", "to": "1", "type": "contains" },
    { "from": "1.1.2", "to": "2", "type": "supports", "source": ["¶7"], "note": "why" }
  ]
}
```

- **passages**: before extraction, split the source into passages: paragraphs, or sentence clusters for dense text. Store the exact text of each passage under `¶1`, `¶2`, ... This is the anti-hallucination anchor: every claim in the graph is checked against these strings, and the viewer shows them on click.
- **spans and sourceText**: citations are tracked two ways. The copied passage text is the anchor, and the character offsets into the full source are the location. Never hand-write these: after the passages are in place, run `locate`, which finds each passage verbatim in the source file and fills `meta.sourceText` and `meta.spans` mechanically. `validate` then enforces the pair: `sourceText[start:end]` must equal the copied passage exactly, so the two representations cannot drift apart. The viewer uses the spans to show the full source with the cited sentences highlighted.
- **ids**: positional paths. Root is `"0"`, its children `"1"`, `"2"`, ..., their children `"1.1"`, `"1.2"`, ... The `contains` edges must mirror the id structure exactly. After restructuring, run `renumber` instead of renumbering by hand.
- **node types**: summary, theme, claim, evidence, example, counterpoint, rebuttal, nuance, concession, contradiction, implicit.
- **attribution**: author, reported, counter, conceded, n/a. Never promote a position out of context: a sentence like "the author says critics claim P, but P is false" must yield a counterpoint node with attribution `counter`, never a claim that P.
- **edge types** (built-ins): contains (the tree), supports, exemplifies, contradicts, qualifies, concedes, restates, precondition. Directed except contradicts and restates. Multi-target is just multiple edges: one example illustrating two points is two `exemplifies` edges from one node.
- **extension**: if no built-in type fits, declare a new type in `meta.edgeTypes` with a direction (`directed` or `symmetric`), an `inverse` name, and a `style` (pattern plus color, for example `dotted purple`). The validator accepts anything declared there and rejects anything undeclared. Prefer built-ins. Declare a new type only when the relation recurs and genuinely does not fit.

## Non-negotiable rules

1. **Every node cites**: `source` is mandatory on every node, including the root summary. A node whose source you cannot name must not exist.
2. **Full coverage**: every passage appears in at least one citation. `validate` warns on uncited passages, and a finished graph has none.
3. **Rooted and honest at the top**: exactly one root, type `summary`, one short sentence (30 words or fewer), citing the passages it summarizes.
4. **Atomic nodes**: one idea per node, 25 words or fewer, phrased to be readable out of context. Split anything fused. Nuance travels with the claim it qualifies, as a `qualifies` edge or a nuance child.
5. **Single attachment, many links**: each idea lives at exactly one place in the tree. Everything else is a cross edge, never a duplicate node.
6. **Restate, never delete**: when the same claim recurs, keep the strongest node and record the recurrence as a `restates` edge. Circularity stays visible, never silently resolved.
7. **Precision survives compression**: every number, date, count, percentage, unit, range, approximator, hedge, conditional, negation, scope word, and limiting adjective in a cited passage must survive into its node with meaning intact. This applies to every node type, including summary, theme, and header nodes: a parent that absolutizes what its child hedges is defective, even when the child is right. Never narrow a range (tens to thousands stays tens to thousands, never hundreds). Never generalize a scoped figure (a week of battery on one model stays scoped to that model, never a general requirement). Never round or drop an approximator (over 3,400 stays over 3,400, never 3,400; about 40 stays about 40). Never absolutize a hedged claim (often, tend to, might, if mechanisms are right, I think). Counts keep all parts (38 strategies across 14 families, never 38 families). Limiting adjectives such as credible, relevant, major, and minor stay attached to what they limit. A node that drops any of these is defective even when its gist is right.

## Extraction passes

Read the text from the beginning in every pass. Each pass has one job.

### Pass 0: Survey

Read the whole text without annotating. Record genre, length, who is speaking, whether it holds one argument or several. Split it into passages and write the exact passage texts into `meta.passages`. Then run `locate` against the source file to add `meta.sourceText` and `meta.spans`; if it reports a passage not found verbatim, fix the passage copy, never the source. For texts over roughly 5000 words, decide chunk boundaries now.

### Pass 1: Skeleton

Read from the beginning again. Write the candidate root summary and the main-point nodes, ids `1`, `2`, `3`, each with its citations. Expect 3 to 9 main points for a normal text. This pass produces a hypothesis, expect to revise it.

### Pass 2: Trace

Read from the beginning a third time. For every passage, note which node(s) it serves and in what role (states a point, evidence, example, counterpoint, concession, transition, digression). Flag passages whose load-bearing content is a number, date, range, approximator, conditional, or limiting adjective, so the Fidelity check knows which nodes carry precision cargo. The text may wander, this ledger is what lets the graph reorganize without losing anything.

### Pass 3: Assembly

Read from the beginning a fourth time, ledger in hand, and build the full `graph.json`. Every ledger row must end up attached to exactly one node. Add `contains` edges mirroring the nesting, then add cross edges wherever one idea supports, contradicts, exemplifies, qualifies, or conditions another, across any distance.

### Pass 4: Deduplication and circularity

Find recurrences and circles. Merge repeats into the strongest node plus `restates` edges, but first check each recurrence for new content or shifted scope: shifted scope is a development, not a duplicate. Check header nodes against their children at the same time: a header whose text adds nothing over a child is a duplicate, abstract it to the level above the child's content or fold it away. Represent unresolved circles with cross edges in both directions and a `contradiction` node explaining them.

## Distillation loop

The first assembly is rarely clean. Iterate on `graph.json`: split fused nodes, merge repeats, re-parent misplacements, sharpen the summary, add missing cross edges. After every round run `validate` and `stats`. Watch `tree ratio` (share of edges that are structural), `hub nodes` (the load-bearing ideas), and `cyclic cross-edges`. Stop when validation is clean, coverage is full, and the stats are stable across a round.

## Verification

After the loop settles, three checks in order. Fix failures and re-run the failed check.

1. **Mechanical**: `validate` passes with zero errors, zero uncited passages, and warnings either zero or understood. `stats` shows sane structure.
2. **Fidelity**: re-read every node's text against its cited passage text in `meta.passages`. This is a judgment check the script cannot do for you. Run this checklist per node, including summary, theme, and header nodes, and fix failures before moving on:
    - Numbers: every number, date, count, percentage, and unit in the passage appears in the node exactly, no rounding, no dropped parts.
    - Approximators: over, about, nearly, more than, around, and their kin stay attached to their number. over 3,400 never becomes 3,400.
    - Ranges stay wide: a range is never narrowed and a scoped figure never generalized.
    - Hedges and conditionals: often, tend to, might, sometimes, if, unless, I think, and their kin survive. A hedged source stated as absolute fact is a defect, including when the hedge lives in a child node and the header states the absolute.
    - Negations: not, never, no, without, except, only keep their polarity. A flipped or dropped negation is a Critical defect.
    - Scope words and limiting adjectives: every, most, some, major, minor, credible, relevant, and their kin match the source scope.
    - Attribution: the node carries the right attribution and no counterpoint is promoted to a claim.
    - No overclaim: the node asserts nothing beyond its source. A node asserting more than its source must be narrowed or split, then re-run Fidelity for it.
3. **Render**: run `render` (or `to-outline` and `to-html`), read the outline once as a reader. In the viewer, the sidebar has a Source toggle that switches between the cited excerpts and the full source text, with the selected node's sentences tinted in its type color and related nodes' sentences in their relation colors; clicking a highlighted sentence jumps to a node that cites it. The sidebar's left edge drags to resize it without moving the graph. If a layer reads wrong, the graph is wrong: fix the graph, never the outline. While reading, also check that no branch restates an earlier branch without adding information: a restated branch means a missed `restates` edge or a duplicate node from Pass 4. Apply the same test between a header node and its children: a header that repeats a child's content without adding a level of abstraction is duplication, so abstract the header or fold it away.

Failure routing:

- A node asserts more than its source: narrow it or split it, re-run Fidelity for it.
- Attribution error: fix the attribution, re-run Fidelity for that subtree.
- Orphan passage: trace it in Pass 2 terms, attach a node, re-run validate.
- Skeleton-level failure, a main point is wrong or missing: redo Pass 1 and 2 for that region only, re-verify everything.
- If a third loop still finds skeleton-level failures, stop. The text is incoherent at that spot. Represent the tangle with contradiction and restates edges and say so in the stats note.

## Worked example

Input `examples/car-ban.txt`, one paragraph, split into five passages. The graph `examples/car-ban.graph.json` has a summary root, three main points, ten nodes, three cross edges:

- `1.1.1 supports 1.1`: the Madrid and Oslo study rebuts the business-harm objection
- `2.2 supports 1`: the bike-lane analogy supports the main claim
- `3 qualifies 1`: transit-first is a scope limit on the ban

Generate everything:

```bash
python3 scripts/graph.py validate examples/car-ban.graph.json
python3 scripts/graph.py to-outline examples/car-ban.graph.json -o examples/car-ban.outline.log
python3 scripts/graph.py to-html examples/car-ban.graph.json -o examples/car-ban.graph.html
```

The outline reads:

```
- Car ban paragraph, point graph (source: car-ban.txt)
    Summary: Cities should ban car traffic from centers, but only after transit expands, since business-harm and elitism objections fail. (¶1, ¶5)
        - 1 Cities should ban cars from their centers. (¶1)
            - 1.1 Counterpoint: Car bans hurt businesses. (¶2) [counter]
                - 1.1.1 Rebuttal: Retail revenue rose in Madrid and Oslo after restrictions. (¶2)
        - 2 Counterpoint: Car bans only work in wealthy cities. (¶4) [counter]
            ...
```

The viewer opens the layered reading: the root tells you what the text is about, one layer down the main points, one more layer the details, with cross edges drawn even between collapsed branches.

## Edge cases

- **No clear argument** in narrative text: use `theme` nodes for the top layer and say so in `meta.title` or a note. Do not manufacture claims the text does not make.
- **Author revises their own claim**: keep both versions as separate nodes with a `restates` edge and a note, or a `contradiction` node if they truly conflict.
- **Unresolvable circle**: cross edges both ways, leave it open.
- **Detail fitting two places**: attach under the more specific node, cross edge from the other.
- **Very long text**: chunked extraction, then one global assembly with chunk-level nodes under the root.
- **Restructured tree**: never renumber ids by hand, run `renumber`, which rewrites every cross-edge reference.

## References

- `loglog` skill: the outline is loglog format, convert further with `loglog convert name.outline.log --to markdown`
- `paper-summarizer`: for academic PDFs, extract takeaways first, then build the graph from them
- `blog-edit-inventory` and `blog-edit-clarity`: related point extraction for blog editing, lossy by design, while this skill is lossless
- `tests/test_graph.sh` in the skills repo covers the tooling end to end
