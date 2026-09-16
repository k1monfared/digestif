# Eval report

Skill dir: eval/skills/digestif
Run dir: eval/skills/digestif/runs/20260911_1434_ph-v0.2.0

## Summary

* total_samples: 12
* scored_samples: 12
* pass: 0
* borderline: 2
* fail: 10
* avg_faithfulness_precision: 0.95675
* avg_must_recall: 0.8418583333333333
* avg_redundancy: 0.057350000000000005
* avg_weighted_score: 0.7079783333333333

## Per sample

| id | words | verdict | weighted | faithfulness | must_recall | redundancy |
| --- | --- | --- | --- | --- | --- | --- |
| 01_what_is_mathematics | 6618 | Fail | 0.6855 | 0.9231 | 0.8214 | 0.0615 |
| 02_case_for_transparent_government | 6741 | Fail | 0.67704 | 0.9506 | 0.7667 | 0.0494 |
| 03_cant_stop_addicted_to_shindig | 5799 | Fail | 0.63844 | 0.9688 | 0.6429 | 0.0312 |
| 04_house_hunting_shenanigans | 3801 | Fail | 0.7 | 0.9643 | 0.7857 | 0.0 |
| 05_manufacturing_taste | 2918 | Fail | 0.71472 | 0.9412 | 0.875 | 0.0588 |
| 06_valuing_consistency | 2920 | Fail | 0.7286 | 0.9524 | 0.8929 | 0.0476 |
| 07_intentionalism | 2643 | Borderline | 0.75476 | 0.9796 | 0.9583 | 0.102 |
| 08_empathy_sympathy_compassion_matrix | 1321 | Borderline | 0.7507 | 1.0 | 0.9167 | 0.08 |
| 09_not_even_wrong | 1345 | Fail | 0.7358 | 0.9375 | 0.9333 | 0.0625 |
| 10_parde_begardan_fa | 639 | Fail | 0.7 | 0.9583 | 0.8125 | 0.0417 |
| 11_finding_a_phone | 3120 | Fail | 0.71318 | 0.9355 | 0.8636 | 0.0323 |
| 12_lets_talk_privacy | 2803 | Fail | 0.697 | 0.9697 | 0.8333 | 0.1212 |

## Fix backlog

Collect fix_list entries from each judge_top.json, ordered by frequency.
Use trace.md files in each sample dir for judge reasoning audit.
