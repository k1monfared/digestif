# Eval harness, multi skill

One harness scores many skills. Each skill owns its corpus, prompts, config, and runs. Shared code lives in `eval/lib`.

## Layout

```text
eval/
  README.md
  run_eval.sh
  lib/
    aggregate.py
    check.py
    compare.py
    failures.py
    judge_run.py
    precheck.py
  skills/
    digestif/
      config.json
      corpus.json
      prompts/
        judge_faithfulness.md
        judge_coverage.md
        judge_concision.md
        judge_top.md
      corpus/sources/
      runs/YYYYMMDD_HHMM_label/
        config.snapshot.json
        RUNLOG.md
        report.md
        summary.json
        failures.md
        failures.json
        <sample-id>/
          source.txt
          output.log
          judge_faithfulness.json
          judge_coverage.json
          judge_concision.json
          judge_top.json
          trace.md
```

## Add a new skill eval

1. Copy `skills/digestif` to `skills/<new-skill>` as a layout reference.
2. Replace `corpus.json`, `corpus/sources`, `config.json`, and files in `prompts`.
3. Keep the same per sample file names so `aggregate.py` and `check.py` work unchanged.
4. Create a run with `./run_eval.sh <new-skill> v1`.

## Run workflow

```bash
./eval/run_eval.sh digestif v1
# fill output.log per sample with the skill under test
# then run the judges either scripted (below) or manually with the 4 prompt files
python3 eval/lib/aggregate.py eval/skills/digestif eval/skills/digestif/runs/<stamp>_v1
python3 eval/lib/check.py eval/skills/digestif eval/skills/digestif/runs/<stamp>_v1
python3 eval/lib/failures.py eval/skills/digestif/runs/<stamp>_v1
```

`failures.py` writes the consolidated audit report for the run: `failures.md` for humans and `failures.json` for tooling. It lists every non-supported claim, every non-present key point, every concision flag, and the top judge fix lists, each with its ids, evidence, and reasoning, so a reviewer can audit or overturn any verdict.

## Scripted judge pipeline

`eval/lib/judge_run.py` runs the four judges as fresh model calls, one phase per invocation, so no context accumulates between phases. It writes raw per-phase results under `<sample>/packets/`, merges them into the canonical `judge_*.json` files, recomputes all metrics from the raw labels, and appends the full reasoning transcripts to `<sample>/trace.md`.

```bash
# default provider: opencode CLI with deepseek-v4.1-flash
python3 eval/lib/judge_run.py all eval/skills/digestif/runs/<stamp>_v1/<sample-id>

# alternative providers
JUDGE_PROVIDER=nvidia JUDGE_MODEL=nvidia/nemotron-3-ultra-550b-a55b python3 eval/lib/judge_run.py all <sample-dir>
JUDGE_PROVIDER=gemini JUDGE_MODEL=gemini-3.8-flash python3 eval/lib/judge_run.py all <sample-dir>
```

Subcommands: `prep` (build packets from graph.json and output.log), `faith N` (faithfulness per part), `cov_check` (blind checklist from source), `cov_map` (map checklist to outline), `con` (concision labels), `top` (overall verdict), `merge` (assemble canonical JSONs and trace), `all` (everything in order).

Notes:

* The judge prompts in `skills/<skill>/prompts/` are the single source of truth, read at runtime by both the scripted pipeline and manual runs.
* Faithfulness is split into parts of at most 35 nodes (env `FAITH_PART_LIMIT`). Each part sees the full source plus its nodes so no claim is judged without context.
* The `packets/` directory keeps every raw model response for audit, including ones later overwritten by a re-run.
* Model name and date are recorded in every merged JSON. Compare runs only when scored with the same judge model.

Token reduction options (for large corpora or tight quotas):

* `FAITH_SCOPE=evidence` drops the repeated full source from each faith part and sends only the node plus its cited passages, with root and branch headers as context. Measured 2.0x smaller faith input across the 12 sample corpus. Tradeoff: cross-passage contradictions outside the cited evidence are no longer visible to this judge.
* Coverage checklists are cached under `skills/<skill>/corpus/checklists/<sample>.json` because they depend only on the source, not on the skill version. Re-runs skip that call entirely (271 KB of input saved per 12 sample run).
* `eval/lib/precheck.py` gives zero API cost approximations of the judge metrics for review triage: citation coverage, exact and near duplicates, and number survival per passage subtree. Precise on prose, noisy on code blocks and probability tables, so treat its flags as a review queue, not verdicts.

## Audit rule

Every verdict must trace to evidence. Judge JSON files hold scores. `trace.md` holds full reasoning transcripts. `config.snapshot.json` pins weights per run. Use the fix_list fields in `judge_top.json` files as the backlog for skill improvement.
