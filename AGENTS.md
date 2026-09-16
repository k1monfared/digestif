# Digestif

Turn any text into a rooted, fully cited idea graph. The agent does the reading through the skill in `src/digestif/skill/`. Everything after that is deterministic Python: `graph.py` validates, and renders the loglog outline and the interactive viewer.

## Layout

- `src/digestif/skill/` — the extraction skill, the source of truth. `SKILL.md`, `scripts/graph.py`, `templates/viewer.html`, `examples/`
- `src/digestif/` — the CLI: `cli.py`, `pipeline.py`, `agents.py`
- `tests/` — renderer suite (`test_graph.sh`), headless UI suite (`test_ui.js`, `test_ui.sh`), CLI pipeline tests with a fake agent (`test_cli.py`), fixtures
- `eval/` — the multi skill evaluation harness with the frozen 12 sample digestif corpus, judge prompts, and every historical run as an audit trail
- `docs/` — the GitHub Pages example: the interactive viewer on a real run of this tool
- `digestif-runs/` — run workspaces (gitignored), one folder per build

## Rules

- The agent's only writable artifact is `graph.json`. Never edit `outline.log` or `graph.html`, they are regenerated.
- The source of truth for the skill is this repo. If the author's skills collection vendors a copy, it syncs from here, never the reverse.
- Tests must pass before any commit: `bash tests/test_graph.sh`, `pytest -q`, and `bash tests/test_ui.sh` when node and playwright are available.

## Commands

```bash
pip install -e ".[dev]"
digestif build essay.md
digestif prep essay.md && digestif finish digestif-runs/<run>
digestif validate graph.json && digestif render graph.json
```

## Status

- TODO: move the evaluation harness from the author's skills repo into this one once the running evaluation finishes. See TODO.md.
