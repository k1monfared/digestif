# Eval report

Skill dir: /home/k1/public/digestif/eval/skills/digestif
Run dir: /home/k1/public/digestif/eval/skills/digestif/runs/20260915_1400_ph-v0.4.0

## Summary

* total_samples: 12
* scored_samples: 12
* pass: 4
* borderline: 7
* fail: 1
* avg_faithfulness_precision: 0.988425
* avg_must_recall: 0.9936083333333333
* avg_redundancy: 0.08185
* avg_weighted_score: 0.7764383333333335

## Per sample

| id | words | verdict | weighted | faithfulness | must_recall | redundancy |
| --- | --- | --- | --- | --- | --- | --- |
| 01_what_is_mathematics | 6618 | Borderline | 0.7781 | 0.9854 | 1.0 | 0.0803 |
| 02_case_for_transparent_government | 6741 | Pass | 0.77664 | 1.0 | 1.0 | 0.1168 |
| 03_cant_stop_addicted_to_shindig | 5799 | Borderline | 0.7802 | 0.989 | 1.0 | 0.0769 |
| 04_house_hunting_shenanigans | 3801 | Pass | 0.7647 | 0.9804 | 1.0 | 0.1373 |
| 05_manufacturing_taste | 2918 | Borderline | 0.76784 | 0.9918 | 0.9688 | 0.082 |
| 06_valuing_consistency | 2920 | Borderline | 0.77902 | 0.9919 | 1.0 | 0.0887 |
| 07_intentionalism | 2643 | Borderline | 0.78058 | 0.9925 | 1.0 | 0.0821 |
| 08_empathy_sympathy_compassion_matrix | 1321 | Pass | 0.79428 | 1.0 | 1.0 | 0.0286 |
| 09_not_even_wrong | 1345 | Pass | 0.7789 | 1.0 | 1.0 | 0.1053 |
| 10_parde_begardan_fa | 639 | Fail | 0.76552 | 0.9655 | 1.0 | 0.1034 |
| 11_finding_a_phone | 3120 | Borderline | 0.77148 | 0.9828 | 0.9545 | 0.0172 |
| 12_lets_talk_privacy | 2803 | Borderline | 0.78 | 0.9818 | 1.0 | 0.0636 |

## Fix backlog

Collect fix_list entries from each judge_top.json, ordered by frequency.
Use trace.md files in each sample dir for judge reasoning audit.
