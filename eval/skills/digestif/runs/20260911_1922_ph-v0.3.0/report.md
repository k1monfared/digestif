# Eval report

Skill dir: eval/skills/digestif
Run dir: eval/skills/digestif/runs/20260911_1922_ph-v0.3.0

## Summary

* total_samples: 12
* scored_samples: 12
* pass: 1
* borderline: 4
* fail: 7
* avg_faithfulness_precision: 0.9667833333333333
* avg_must_recall: 0.921175
* avg_redundancy: 0.06309166666666667
* avg_weighted_score: 0.7425733333333334

## Per sample

| id | words | verdict | weighted | faithfulness | must_recall | redundancy |
| --- | --- | --- | --- | --- | --- | --- |
| 01_what_is_mathematics | 6618 | Borderline | 0.7752 | 0.969 | 1.0 | 0.062 |
| 02_case_for_transparent_government | 6741 | Pass | 0.7632 | 0.98 | 1.0 | 0.144 |
| 03_cant_stop_addicted_to_shindig | 5799 | Fail | 0.7516 | 1.0 | 0.8929 | 0.0278 |
| 04_house_hunting_shenanigans | 3801 | Fail | 0.72 | 0.9714 | 0.8571 | 0.0571 |
| 05_manufacturing_taste | 2918 | Fail | 0.72948 | 1.0 | 0.875 | 0.1026 |
| 06_valuing_consistency | 2920 | Borderline | 0.76572 | 1.0 | 0.9643 | 0.1 |
| 07_intentionalism | 2643 | Fail | 0.72778 | 0.9444 | 0.9167 | 0.0833 |
| 08_empathy_sympathy_compassion_matrix | 1321 | Fail | 0.7511 | 0.9355 | 0.9583 | 0.0323 |
| 09_not_even_wrong | 1345 | Borderline | 0.7685 | 1.0 | 0.9667 | 0.0909 |
| 10_parde_begardan_fa | 639 | Fail | 0.7417 | 0.9167 | 0.9375 | 0.0 |
| 11_finding_a_phone | 3120 | Fail | 0.6561 | 0.913 | 0.7273 | 0.0 |
| 12_lets_talk_privacy | 2803 | Borderline | 0.7605 | 0.9714 | 0.9583 | 0.0571 |

## Fix backlog

Collect fix_list entries from each judge_top.json, ordered by frequency.
Use trace.md files in each sample dir for judge reasoning audit.
