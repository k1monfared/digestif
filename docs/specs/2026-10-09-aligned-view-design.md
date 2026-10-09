# Aligned reading view

Status: approved design, implemented in `src/digestif/skill/templates/aligned.html`.

## Goal

Read the original text top to bottom while its idea structure appears beside it. The source is shown exactly as written. The graph's points sit to the right of the text they come from, one column per depth, and the reader reveals deeper points one branch at a time.

## Data

Built from a located `graph.json` only, no LLM involved:

- `meta.sourceText`, the full original text
- `meta.spans`, the character range of every passage `¶n`
- `nodes`, each citing passage keys in `source`
- `contains` edges, the tree

A graph without `meta.sourceText` and `meta.spans` cannot be aligned. Run `graph.py locate` first.

## Layout

- The root summary is a header above everything.
- Column 0 is the source text. Column $d$ holds the visible nodes at depth $d$, so main points are column 1, their children column 2, and so on.
- A visible node is placed once, at its **anchor**, the earliest passage it cites in source order. Siblings with the same anchor stack in the same cell.
- The anchors of all visible nodes are the **cut points**. They split the source into rows: a row runs from one cut point up to the next. Each row is as tall as its tallest cell, so the text gains line breaks exactly where a point needs to start. Whitespace and paragraph breaks inside the source are preserved.
- Each depth column has a thin bar lane on its left. Every visible node draws a bar in its lane beside every line of every passage it cites, one bar per contiguous run of cited passages. Nodes in the same column whose runs overlap get side by side sub-lanes. A bar takes the node's type color.

## Interaction

- **Expand per node.** A card with children shows `+`. Clicking it shows those children in the next column and adds their cut points. `−` hides them and all deeper descendants, and removes the cut points no visible node needs any more. Initially only the main points are visible.
- **Fold a column.** Each column header has a fold control. A folded column shrinks to a thin strip labeled `L<d>`. Cards are hidden, but rows, cut points and bars stay exactly as they were. Clicking the strip reopens it.
- **Bar cycling.** Clicking a bar scrolls to the node's next run of cited passages and briefly tints it. After the last run it wraps to the first, so every passage of a node can be read in order.
- **Select.** Clicking a card tints all of its cited passages in its type color and emphasizes its bars. Clicking it again, or Escape, clears the selection.
- The clicked card keeps its position on screen when expanding or collapsing changes the rows above it.

## Graph view parity (added 2026-10-09)

The aligned view mirrors the graph viewer's keyboard and mouse model, minus the parts a scrolling document does not need (sidebar, zoom, drag panning, search).

- **Visibility model**, the same as the graph viewer: a layer count plus per node folds and opens. A node is shown when its parent is shown and not folded, and either its depth is within the layer count, its parent was opened, or it is forced open by focus. `+` and `−` fold and open single nodes and select them.
- **Keys**: up and down move through the visible cards in top to bottom screen order. Left folds an open card, otherwise selects its parent. Right opens a card and selects its first child, or moves to the next card on a leaf. Space folds or opens the selected card. Ctrl+1..9 show that many columns and move a deeper selection up to its ancestor in the last column. Ctrl+0 shows everything. Ctrl+Alt+1..9 show that many columns and keep the selected branch open. Escape closes a popover, then the edge card, then the selection.
- **Anchoring and motion**: folding keeps the selected card at the same screen position. Selection changes, edge follows and bar jumps scroll with a quarter second ease out.
- **Edges**: every non-`contains` edge whose two ends are visible is drawn as a curve in an SVG layer above the text and below the cards. Cards in different columns connect side to side. Cards in the same column connect with an arc bulging to the right. Color, dash and arrowhead come from the edge type registry, as in the graph viewer. The selected card's edges are bold and drawn on top, the rest are dimmed.
- **Edge card**: clicking an edge highlights it and opens a card with the relation and its note. The card's follow arrow points toward the other end relative to the selected card. Clicking it scrolls to and selects that end.
- **Help and Legend** buttons open popovers listing the controls, the node type colors and the edge styles.

## Files and commands

- `src/digestif/skill/templates/aligned.html`, self-contained template with a `__GRAPH_JSON__` token, no network access.
- `graph.py to-aligned graph.json [-o aligned.html]` validates, refuses a graph without spans, and writes the file.
- `graph.py render` also writes `aligned.html` when the graph has spans, and prints a note and skips it otherwise. `build` and `finish` therefore produce it automatically.
- `digestif align <run_dir | graph.json> [--no-open]` regenerates and opens it, for older runs.

## Tests

- `tests/test_graph.sh`: `to-aligned` output, refusal of invalid and unlocated graphs, `render` writing or skipping the file.
- `tests/test_ui.js`: initial state, text fidelity, card to passage alignment, expand and collapse, column folding, bar cycling with wraparound, selection tint.
- `tests/test_cli.py`: `digestif align` on a run directory and on a graph, `build` producing `aligned.html`.

## Out of scope

Cross-link edges between cards, search, and a mobile drawer. On narrow screens the columns scroll sideways.

## Shared keyboard model and links navigation (added 2026-10-09)

Both viewers follow the same four rules, chosen to stay small enough to remember.

1. **Arrows move.** Up and down go to the previous or next node at the same depth across the whole document, in tree order in both views, so 1.1.3, 1.1.4, then 2.1.1. When the next one sits in a folded branch, that branch opens. Branches passed through stay open. Left goes to the parent and never folds. Right goes to the first child, showing it if it was folded. Folding has its own key, Ctrl+J, next to the `+`/`−` buttons. Space does nothing.
2. **Enter goes in, Escape comes out.** Enter opens the selected node's links: one list, outgoing links first, then incoming, walked with up and down only. The highlighted link is drawn bold and its far end gets a dashed ring. Enter on a link moves the selection to the far end, Enter again moves it back, so Enter flips between the two ends. Up and down always pick within the starting node's list and return to the starting node. Escape leaves the links with the selection on whichever end it is on. Left, right and space do nothing inside the links. A node with no links shows a short hint. In the graph view the list is the sidebar's links section, in the aligned view a small panel in the top right corner. Following into a folded branch opens the path to it.
3. **Back and forward retrace every visit.** Every change of the selected node is a visit: arrow moves, clicks, `+`/`−` clicks, link rows, edge cards, and leaving the links on the far end. Inside the links, flipping ends and picking rows are previews, so only the end where you leave counts. Clearing the selection and Ctrl+digits moving it to an ancestor are not visits. The same node twice in a row is stored once, and the stack keeps the last 200. Backspace or Alt+Left go back, Alt+Right goes forward, a new visit clears the forward stack, and the node returns to the screen position it had when you left it. A pill in the top bar names where back goes and works as a back button.
4. **Ctrl+digits set how much is shown**, unchanged.

The aligned view also gets the graph view's search: a box in the top bar keeps only matching points and their ancestors, marks the matches, and shows the count. Escape in the box clears it, and Ctrl+digits clear it too. Following a link to a point outside the search results clears the search.
