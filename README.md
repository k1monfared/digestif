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
digestif render GRAPH_JSON      deterministic only: outline.log and graph.html
digestif validate GRAPH_JSON    integrity and citation check, exit 1 on errors
digestif open RUN_DIR           open a finished run in the browser
digestif agents                 list detected agent CLIs and readiness
digestif doctor                 environment check
digestif install-skill          install the skill into an agent config
```

`build` accepts `--agent`, `--model`, `--agent-cmd`, `--out`, `--slug`, `--retries` (default 2), `--timeout` (default 1800 seconds per agent call), `--no-open`, and `--dry-run`. The input can be a path or `-` to read from stdin.

## Run layout

```
digestif-runs/essay-20260915-1800/
  source.txt        the exact input text
  graph.json        the canonical graph
  outline.log       generated loglog outline
  graph.html        generated interactive viewer
  AGENTS.md         the task file the agent followed
  CLAUDE.md         wrapper for Claude Code
  prompt.md         the exact prompt used
  skill/            the digestif skill, copied for the run
  run.log           agent output, command lines, validation rounds
  validation.txt    final validator and locate output
  repair.md         present only when a repair round was needed
```

## The viewer

The generated `graph.html` is one self-contained file, no server and no network access needed:

- The root summary, then main points, then details, as a zoomable tree with typed cross-links drawn across branches.
- Scroll moves, shift+scroll moves sideways, ctrl+scroll zooms at the cursor, ctrl+= and ctrl+- zoom from the keyboard.
- Arrows navigate in top to bottom order, left folds or goes to the parent, right unfolds and descends, space folds the selected branch.
- Ctrl+1..9 show that many layers, Ctrl+0 shows all of them, Ctrl+Alt+1..9 focus the selected branch.
- The sidebar shows the selected node: type, attribution, its cited excerpts expanded by default, and every relation with its color. Its left edge drags to resize the panel.
- The Source toggle in the sidebar switches between the excerpts and the full source text. The selected node's sentences are tinted in its type color, related nodes' sentences in the color of the relation, claim blue, evidence green, contradicts red, and so on. Clicking a highlighted sentence jumps to a node that cites it.

## The skill

The extraction method is a skill in `src/digestif/skill/`, usable on its own with any agent that reads `SKILL.md`. The command line tool copies it into every run workspace, and `install-skill` puts it into your agent config:

```bash
digestif install-skill --target claude     # ~/.claude/skills/digestif
digestif install-skill --target opencode   # opencode skills directory
digestif install-skill --target project    # ./.claude/skills/digestif
digestif install-skill --dir /some/path    # anywhere
```

Add `--link` to symlink instead of copying.

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
pytest -q                    # CLI pipeline tests with a fake agent, no LLM calls
bash tests/test_graph.sh     # validator, locator, renderer suite
bash tests/test_ui.sh        # headless browser suite, needs node and playwright, skips otherwise
```

All three run in CI on every push.

## License

GPL-3.0-only. See LICENSE.
