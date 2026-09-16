# Digestif

Turn any text into a **rooted, fully cited idea graph**: a one-sentence summary on top, main points below it, details, evidence, counterpoints, and typed links connecting ideas across the whole text. Every node cites the exact passages it came from, and the deterministic tooling checks it.

One command:

```bash
digestif build essay.md
```

It runs the extraction through the agent CLI you already have installed (Claude Code, Codex, or opencode), validates the result, repairs it if needed, and writes a run folder with a readable loglog outline and an interactive, zoomable viewer, then opens the viewer in your browser. No API keys, no configuration, it reuses your existing agent login.

## Install

```bash
pipx install git+https://github.com/k1monfared/digestif
# or
uv tool install git+https://github.com/k1monfared/digestif
```

Requires Python 3.9 or newer. The renderer and validator are stdlib only.

## Requirements for extraction

The thinking step is done by an LLM agent, driven headlessly. You need one of these installed and logged in:

| Agent | Headless command used | Login |
| --- | --- | --- |
| Claude Code | `claude -p ... --allowedTools Read Write Edit Bash` | `claude auth login` |
| Codex | `codex exec ... --sandbox workspace-write` | `codex login` |
| opencode | `opencode run ... --auto` | `opencode auth login` |
| anything else | `--agent-cmd "your-tool --prompt-file {prompt_file} --cwd {cwd}"` | your choice |

Check what is detected:

```bash
digestif agents
digestif doctor
```

No agent CLI, or you prefer a chat window? Use manual mode:

```bash
digestif prep essay.md        # writes the workspace and prints one sentence to paste into any agent
# ... let the agent produce graph.json ...
digestif finish digestif-runs/essay-20260915-1800
```

## Commands

```
digestif build INPUT            full pipeline: agent, validate, repair, render, open
digestif prep INPUT             prepare a workspace for any agent, no LLM call
digestif finish RUN_DIR         validate, repair if an agent is given, render, open
digestif render GRAPH_JSON      deterministic only: outline.log and graph.html
digestif validate GRAPH_JSON    integrity and citation check
digestif open RUN_DIR           open a finished run in the browser
digestif agents                 list detected agent CLIs
digestif doctor                 environment check
digestif install-skill          install the digestif skill into an agent config
```

Useful flags for `build`: `--agent`, `--model`, `--out`, `--retries`, `--timeout`, `--no-open`, `--dry-run`, `--agent-cmd`.

## Output

```
digestif-runs/essay-20260915-1800/
  source.txt        the exact input text
  graph.json        the canonical artifact, the only thing the agent writes
  outline.log       generated loglog outline
  graph.html        generated interactive viewer
  AGENTS.md         the task file the agent followed
  CLAUDE.md         wrapper for Claude Code
  skill/            the digestif skill used for this run
  run.log           agent output and every validation round
  validation.txt    final validator and locate output
```

## The skill

The extraction itself is a skill, `src/digestif/skill/`, usable on its own with any agent that reads `SKILL.md`. Install it into your agent's config:

```bash
digestif install-skill --target claude       # ~/.claude/skills/digestif
digestif install-skill --target opencode     # the opencode skills directory
digestif install-skill --target project      # ./.claude/skills/digestif
digestif install-skill --dir /some/path      # anywhere
```

Add `--link` to symlink instead of copying.

## What is checked, and why that matters

`graph.json` stores the source text split into passages under `meta.passages`, and every node cites passage keys. `digestif validate` rejects any citation that does not exist, any passage nobody cites, and any structural break. A second representation, character offsets in `meta.sourceText` and `meta.spans`, is filled mechanically by `digestif` after the agent finishes, and the validator enforces that `sourceText[start:end]` equals the copied passage exactly. Invention is a mechanical failure here, not a matter of trust. The viewer's source panel highlights the selected node's sentences in its type color and related sentences in their relation colors.

## Development

```bash
pip install -e ".[dev]"
bash tests/test_graph.sh     # renderer and validator suite
pytest -q                    # CLI pipeline tests with a fake agent, no LLM calls
bash tests/test_ui.sh        # headless browser suite, needs node + playwright (skips otherwise)
```

## Status

- The evaluation harness that scored the extraction quality lives in the author's skills repo for now. It moves here once the currently running evaluation finishes, and this note gets deleted then.

## License

GPL-3.0-only. See LICENSE.
