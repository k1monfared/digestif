# 07_intentionalism

1. Generate loglog into output.log using the skill under test.
2. Run Judge F prompt, save JSON as judge_faithfulness.json.
3. Run Judge Cov prompt, save JSON as judge_coverage.json.
4. Run Judge Con prompt, save JSON as judge_concision.json.
5. Run Judge Top prompt, save JSON as judge_top.json.
6. Append full judge reasoning transcripts to trace.md.
7. From run dir, run aggregate.py then check.py.
