# Digestif

Turn any text into a **rooted, fully cited idea graph**: a one-sentence summary on top, main points below it, and then the details, evidence, examples, counterpoints, and nuances as deep as the text goes. Typed links connect ideas across the whole document. Every node cites the exact passages it came from, and deterministic Python checks that the citations exist, that nothing is uncovered, and that the quotes match the source character for character.

```bash
digestif build essay.md
```

One command runs the extraction through the agent CLI you already have installed, validates the result, repairs it when needed, and writes a run folder containing:

| File | What it is |
| --- | --- |
| `graph.json` | The canonical artifact. Nodes, typed edges, citations, character offsets. The only file the LLM writes |
| `outline.log` | A readable loglog outline generated from the graph |
| `graph.html` | A self-contained interactive viewer, opens in the browser automatically |
| `aligned.html` | The aligned reading view: the original text as written, with the points beside the passages they come from |
| `validation.txt` | The final validator and citation-locator output |
| `run.log` | Every agent invocation and validation round, for audit |

No API keys, no configuration. The thinking is done by Claude Code, Codex, or opencode in headless mode, reusing the login you already have. Everything after the graph exists is plain Python: rendering, checking, and the viewer.

**Live example**: [k1monfared.com/digestif](https://k1monfared.com/digestif/) is the generated viewer on a real run of this tool over a 6,600 word blog post. The same artifacts are kept in `docs/example/`.

## Install

```bash
pipx install git+https://github.com/k1monfared/digestif
# or
uv tool install git+https://github.com/k1monfared/digestif
```

Python 3.9 or newer. The validator, renderer, and viewer generator are standard library only.

## Requirements

The extraction step needs one installed and logged in agent CLI:

| Backend | What digestif runs | Login |
| --- | --- | --- |
| Claude Code | `claude -p "..." --allowedTools Read Write Edit Bash` | `claude auth login` |
| Codex | `codex exec "..." --sandbox workspace-write` | `codex login` |
| opencode | `opencode run "..." --auto` | `opencode auth login` |
| anything else | `--agent-cmd "tool --prompt-file {prompt_file} --cwd {cwd}"` | whatever your tool needs |

Check the environment at any time:

```bash
digestif agents    # which backends are installed and logged in
digestif doctor    # full check, including the renderer
```

Prefer not to use a CLI agent, or want to use a chat window? Manual mode works with any interface:

```bash
digestif prep essay.md
# open the printed folder in your agent of choice, paste the one sentence it prints
digestif finish digestif-runs/essay-20260915-1800
```

`prep` writes the workspace and prints the instruction. `finish` validates, optionally repairs through an agent, locates citations, renders, and opens the viewer.

## Commands

```
digestif build INPUT            full pipeline: agent, validate, repair, render, open
digestif prep INPUT             prepare a workspace for any agent, no LLM call
digestif finish RUN_DIR         validate, repair if an agent is available, render, open
digestif fitsegid INPUT         graph back to cited prose, the inverse of build
digestif align RUN_DIR          build and open the aligned reading view
digestif render GRAPH_JSON      deterministic only: outline.log, graph.html, aligned.html
digestif validate GRAPH_JSON    integrity and citation check, exit 1 on errors
digestif open RUN_DIR           open a finished run in the browser
digestif agents                 list detected agent CLIs and readiness
digestif doctor                 environment check
digestif install-skill          install the skills into an agent config
```

`fitsegid` accepts a run directory or a `graph.json`, plus `--lod max|<layers>` (default `max`, lossless) or `--words N`, and the same `--agent`, `--model`, `--agent-cmd`, `--retries`, and `--timeout` flags as `finish`.

`build` accepts `--agent`, `--model`, `--agent-cmd`, `--out`, `--slug`, `--retries` (default 2), `--timeout` (default 1800 seconds per agent call), `--no-open`, and `--dry-run`. The input can be a path or `-` to read from stdin.

## Run layout

```
digestif-runs/essay-20260915-1800/
  source.txt        the exact input text
  graph.json        the canonical graph
  outline.log       generated loglog outline
  graph.html        generated interactive viewer
  aligned.html      generated aligned reading view
  AGENTS.md         the task file the agent followed
  CLAUDE.md         wrapper for Claude Code
  prompt.md         the exact prompt used
  skill/            the digestif skill, copied for the run
  run.log           agent output, command lines, validation rounds
  validation.txt    final validator and locate output
  repair.md         present only when a repair round was needed
  fitsegid.md       cited prose, added by `digestif fitsegid` (the inverse)
  fitsegid-clean.md the reading copy, generated by strip-prose
  fitsegid.html     the two-pane review viewer, prose against the graph
  FITSEGID.md       the inverse task file the agent followed
```

## The viewer

The generated `graph.html` is one self-contained file, no server and no network access needed:

- The root summary, then main points, then details, as a zoomable tree with typed cross-links drawn across branches.
- Scroll moves, shift+scroll moves sideways, ctrl+scroll zooms at the cursor, ctrl+= and ctrl+- zoom from the keyboard. On touch screens pinch zooms the graph, one finger pans it, and the page itself does not zoom while you are on the canvas. The graph area has no scrollbars, panning is by drag, scroll, and pinch.
- The keyboard follows four rules, the same in this viewer and in the aligned view:
  - Arrows move. Up and down go to the previous or next node at the same depth across the whole document, in tree order, opening a folded branch when the next one is inside it. Left goes to the parent, right goes to the first child and shows it if it was folded. Ctrl+J folds or unfolds the selected node. Space does nothing.
  - Enter goes into the selected node's links, Escape comes out. Enter opens the sidebar on the node's links out and in, up and down pick one, and its far end gets a dashed ring. Enter on a link follows it to the other end, Enter again follows it back. Escape leaves the links on whichever end you are at. A node without links shows a short hint instead.
  - Back and forward retrace every node you visited, as in a browser: arrow moves, clicks, and following links. Backspace or Alt+Left goes back, Alt+Right goes forward, and the node returns to the spot on screen where it was. Inside the links, flipping between the two ends is only a preview, so just the end where you leave counts. A small pill in the top bar names where back goes and works as a back button.
  - Ctrl+digits set how much is shown: Ctrl+1..9 show that many layers, Ctrl+0 shows all of them, Ctrl+Alt+1..9 show that many layers and keep the selected branch open.
- The selected node's edges are bold and stay bold even when the node is panned out of view, so you can trace a link to its far end.
- Click or tap an edge to highlight it. A small card appears with the relation type, the note that explains how the relation holds when the graph carries one, a follow button whose arrow points in the direction of travel relative to the selected node, and a close button. The card is fully clickable, following smoothly pans the graph to the other end, and a click on close or Escape dismisses it.
- Every view transition is animated the same way, a quarter second ease-out pan: keyboard navigation, clicking links in and out in the sidebar, jumping from a source sentence, and following an edge. Panning and zooming by hand stay direct and instant.
- Searching keeps only the matches and their ancestor path: matches keep the highlight ring, the parent chain stays as a faded skeleton, the hidden branches leave no empty space behind because the skeleton is laid out compactly, and everything returns to the original layout when the search is cleared.
- Edges that span the view stay visible even when both of their endpoints are off screen, so a long connection crossing the viewport can always be traced instead of disappearing at the edge of the screen.
- The sidebar is docked to the right edge, top to bottom, with a thin divider. A small pill in the middle of the divider drags left and right to resize it. The sidebar header, with the node title and the Source toggle, stays in place while the content below it scrolls. Its body shows the selected node: type, attribution, its cited excerpts expanded by default, and every relation with its color.
- A toggle button in the top right opens and closes the sidebar. It sits in the top right corner of the graph when the sidebar is closed, and becomes part of the sidebar header when it is open. This works the same on every screen size. Clicking or tapping a node selects it but no longer opens the sidebar, and Enter opens it on the selected node's links.
- Help and Legend sit as two separate buttons in the top bar, each opening a small popover. The top bar lays itself out in two clean rows on narrow screens instead of wrapping raggedly.
- On small screens the sidebar becomes a drawer at 88 percent of the width, toggled by the same button, and it overlays the graph instead of shrinking it.
- The Source toggle in the sidebar switches between the excerpts and the full source text. The selected node's sentences are tinted in its type color, related nodes' sentences in the color of the relation, claim blue, evidence green, contradicts red, and so on. Clicking a highlighted sentence jumps to a node that cites it.

## The aligned reading view

`aligned.html` shows the original text exactly as written, with the graph's points beside it. Live example: [k1monfared.com/digestif/example/aligned.html](https://k1monfared.com/digestif/example/aligned.html).

- Each depth gets its own column: main points first, then their children, and so on. Only the main points show at first, and `+` on a point adds its children in the next column, one branch at a time. `−` hides them again.
- A point sits next to the earliest passage it cites. The text breaks into rows at those passages, so each point lines up with the sentence where it starts, and opening deeper points adds more breaks.
- A thin colored bar beside the text marks every passage a point cites. A point that draws on several separate places has one bar per place. Clicking a bar jumps to the next place and wraps from the last back to the first, so all of a point's source can be read in order.
- Each column header folds that column to a thin strip, to make room without changing the row breaks or the bars. Clicking the strip opens it again.
- Clicking a point selects it and tints its passages in the text.
- Cross-links are drawn as curves between the cards, in the same colors and dash styles as the graph view, whenever both ends are showing. The selected point's links are bold and the rest fade. Clicking a link opens the same small card as in the graph view, with the relation, its note, and a follow button that scrolls to the other end and selects it.
- The keyboard is the same as in the graph view, see the four rules above, with columns in place of layers. The links list opens as a small panel in the top right corner. Every move is a short animated scroll, and folding keeps the selected card where it was on screen.
- Search keeps only the matching points and their parents, marks the matches, and shows how many there are. Escape in the box clears it.
- Help and Legend in the top bar list the controls and the colors.

`build` and `finish` write it automatically. For an older run, `digestif align digestif-runs/<run>` builds and opens it. It needs a located graph, one that went through `graph.py locate`, because it uses the passage offsets in `meta.spans`.

## The skills

The extraction method is a skill in `src/digestif/skill/`, and its inverse, `fitsegid`, is a second skill in `src/digestif/skill-fitsegid/`. Both are usable on their own with any agent that reads `SKILL.md`. The command line tool copies the extraction skill into every run workspace, and the inverse skill when you run `fitsegid`. `install-skill` puts both into your agent config:

```bash
digestif install-skill --target claude     # ~/.claude/skills/{digestif,fitsegid}
digestif install-skill --target opencode   # opencode skills directory
digestif install-skill --target project    # ./.claude/skills/
digestif install-skill --dir /some/path    # anywhere
digestif install-skill --skill fitsegid    # only the inverse skill
```

Add `--link` to symlink instead of copying.

## The inverse: fitsegid

`fitsegid` is `digestif` reversed, letter for letter. Where digestif condenses a text into a graph, fitsegid tells the graph back as prose: the main points, the reasons under them, the evidence, the objections and rebuttals, in an order a reader can follow, with no filler and nothing invented.

One command produces `fitsegid.md`, the cited prose, and `fitsegid-clean.md`, the same text with the citation markers stripped for reading:

```bash
digestif fitsegid digestif-runs/essay-20260915-1800
digestif fitsegid digestif-runs/essay-20260915-1800 --lod 2     # stop at the details layer
digestif fitsegid digestif-runs/essay-20260915-1800 --words 400 # or aim for a length
```

Every sentence ends with the node ids it is built from, and a small manifest declares the level of detail:

```
---
skill: fitsegid
lod: max
dropped: []
---

Cities should ban cars from their centers, though only after public transit expands. [0]
Critics argue that car bans hurt businesses. [1.1] Retail revenue rose in Madrid and Oslo after restrictions. [1.1.1, 1.1]
```

`fitsegid` is grounded the same way digestif is. A deterministic checker, `src/digestif/skill-fitsegid/scripts/fitsegid.py`, rejects any orphan sentence with no citation, any citation to an unknown node, any node that is neither written into the prose nor listed in `dropped`, and any layer count contradicted by the citations. It warns when a number or a capitalized name in a sentence appears nowhere in the nodes it cites, and when a counter or conceded node is stated without attribution. Nothing is invented, and nothing disappears silently: the manifest says exactly what was left out, and `--lod max` (the default) leaves nothing out at all. The same checker can run against an `outline.log` when the graph is not at hand.

`digestif fitsegid` also builds `fitsegid.html`, a review viewer for judging how well the prose maps onto the graph. Each paragraph of the prose is a row, with the main points it introduces as notes in a margin column on the right, and a bar in the gutter spans the run of paragraphs that belong to each main point. Hovering a paragraph or a note highlights everything that belongs to the same main points, clicking pins that highlight, and paragraphs with no citation are flagged in the margin. A paragraph whose bars belong to several main points is the one that is really talking to several of them at once.

## Why the checking matters

`graph.json` stores the source split into passages under `meta.passages`, and every node cites passage keys. Character offsets into the full text live in `meta.sourceText` and `meta.spans`, filled mechanically by `digestif` after the agent finishes. The validator rejects any citation that does not exist, any passage nobody cites, any structural break, and any offset whose slice does not equal the copied passage character for character. Invention is a mechanical failure here, not a matter of trust. The coverage line, for example `Coverage: 34 of 34 passages cited`, is counted, not estimated.

## Evaluation

The extraction quality is measured on a frozen corpus of 12 blog posts (11 English, 1 Farsi, 639 to 6741 words, several genres) with four reference-free judges, one per aspect: faithfulness (every claim supported by its cited passage), coverage (every must-have key point present), concision (no redundancy), and an overall verdict. A sample passes only when faithfulness precision is at least 0.95, must-have recall at least 0.90, and redundancy at most 0.15, with zero critical contradictions. Scores below are from the scripted judge pipeline, judge `opencode-go/deepseek-v4.1-flash`, 2026-09-15. Compare runs only when the judge model matches.

### Progression

| Version | Pass | Borderline | Fail | Faithfulness | Must-have recall | Redundancy | Weighted score |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.2.0 | 0 | 2 | 10 | 0.957 | 0.842 | 0.057 | 0.708 |
| 0.3.0 | 1 | 4 | 7 | 0.967 | 0.921 | 0.063 | 0.743 |
| 0.4.0 | 4 | 7 | 1 | 0.988 | 0.994 | 0.082 | 0.776 |

### Current version, per sample

| Sample | Words | Verdict | Weighted | Faithfulness | Must recall | Redundancy |
| --- | --- | --- | --- | --- | --- | --- |
| 01_what_is_mathematics | 6618 | Borderline | 0.778 | 0.985 | 1.000 | 0.080 |
| 02_case_for_transparent_government | 6741 | Pass | 0.777 | 1.000 | 1.000 | 0.117 |
| 03_cant_stop_addicted_to_shindig | 5799 | Borderline | 0.780 | 0.989 | 1.000 | 0.077 |
| 04_house_hunting_shenanigans | 3801 | Pass | 0.765 | 0.980 | 1.000 | 0.137 |
| 05_manufacturing_taste | 2918 | Borderline | 0.768 | 0.992 | 0.969 | 0.082 |
| 06_valuing_consistency | 2920 | Borderline | 0.779 | 0.992 | 1.000 | 0.089 |
| 07_intentionalism | 2643 | Borderline | 0.781 | 0.993 | 1.000 | 0.082 |
| 08_empathy_sympathy_compassion_matrix | 1321 | Pass | 0.794 | 1.000 | 1.000 | 0.029 |
| 09_not_even_wrong | 1345 | Pass | 0.779 | 1.000 | 1.000 | 0.105 |
| 10_parde_begardan_fa | 639 | Fail | 0.766 | 0.966 | 1.000 | 0.103 |
| 11_finding_a_phone | 3120 | Borderline | 0.771 | 0.983 | 0.955 | 0.017 |
| 12_lets_talk_privacy | 2803 | Borderline | 0.780 | 0.982 | 1.000 | 0.064 |

The remaining failures are dominated by redundancy just under the gate on long pieces and one Farsi sample, which is flagged experimental.

### Reproducing the evaluation

The whole harness lives in `eval/`, with the corpus, judge prompts, and every past run kept as an audit trail. Each sample folder holds the source, the generated outline, the four raw judge outputs, and the full judge reasoning.

```bash
./eval/run_eval.sh digestif v1                       # new run skeleton, corpus copied in
# produce output.log per sample with the skill under test
python3 eval/lib/judge_run.py all eval/skills/digestif/runs/<stamp>_v1/<sample>
python3 eval/lib/aggregate.py eval/skills/digestif eval/skills/digestif/runs/<stamp>_v1
python3 eval/lib/check.py eval/skills/digestif eval/skills/digestif/runs/<stamp>_v1
python3 eval/lib/failures.py eval/skills/digestif/runs/<stamp>_v1
```

`failures.py` writes the consolidated audit report, listing every unsupported claim, missing key point, and concision flag with evidence, so any verdict can be reviewed or overturned. See `eval/README.md` for the judge packet format, provider options (`JUDGE_PROVIDER`, `JUDGE_MODEL`), token reduction flags, and the zero cost precheck.

## Development

```bash
pip install -e ".[dev]"
pytest -q                     # CLI pipeline tests with a fake agent, no LLM calls
bash tests/test_graph.sh      # validator, locator, renderer suite
bash tests/test_fitsegid.sh   # inverse prose checker suite
bash tests/test_ui.sh         # headless browser suites for both viewers, need node and playwright, skip otherwise
```

All of these run in CI on every push except the UI suite, which runs in its own job.

## License

GPL-3.0-only. See LICENSE.
