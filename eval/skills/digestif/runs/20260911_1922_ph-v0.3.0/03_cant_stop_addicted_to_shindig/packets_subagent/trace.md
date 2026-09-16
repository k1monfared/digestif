# Trace: 03_cant_stop_addicted_to_shindig (skill v0.3.0, judged 2026-09-12)

## Judge F (faithfulness, v1.0.0)
Method: read source.txt (710 lines) and output.log (47 lines) fully. Atomized propositional lines L02-L37 into 37 claims C01-C37, splitting dual-fact L31 into C30 (opponent-aware negative result) and C31 (web/code release); skipped L01 title, L38+ cross-links, coverage footer. Every number rechecked against source: ladder 3-5-7-9-11-13, 16.67% versus 2.78% with exact 6x, ways ladder, 13/3 approx 4.3x, 171/1296 13.2%, 834/1296 64.4% with 24/1296 overlaps and triple 0, 4.88 versus 4.33, 22.73 versus 20.18, 1193/1296 92.0% Q1.43, 568/1296 43.8% Q1.05, 37 excellent at 85%+ with median 79.6%, clean 39.8%/2.3%, 1.32 over 0.4 keep, 1.12 over 0.46 stop with correct polarity, 38 strategies with 1000/2500/3.6M scale, 10.5 (median 9, sd 5.73, 7.50 busts), 69.84% (132696/190000) with Heuristic(1.5) 66.46%, log(0.5)/log(P) rule, #1 speed versus #11 at 58.90%, +11.18% (P1 55.59%) with +31.24% bias, +-13.6%, 171 versus 834 steps at ~8 hours, [3,5,8,10,12,14] at +-3.09%, [4,7,11,14,17,20] at +-2.17% with linear +-3.32%. Outcome: 37 Supported, precision 1.0, critical 0, fail_list empty.

## Judge Cov (coverage, v1.0.0)
Phase 1 blind: 12 points (rules, 2-dice, 4-dice derivations, table match, expected rolls, combos, clean rates, stopping rule, continuation as Nice to have, tournament, paradox plus first-player, design plus advice). Phase 2: all Present. must_recall = 11/11 = 1.0; overall_recall = 12/12 = 1.0; missing_list empty.

## Judge Con (concision, v1.0.0)
Labeled all 37 F claims: duplicates 0 (C30/C31 share a line but state distinct facts), trivia 0 (every line maps to a key point). scored 37, unique 37, redundancy 0.0. structured_tokens 671 (wc -w); tokens_per_unique 671/37 = 18.1. prune_list empty.

## Judge Top (overall, v1.0.0)
Gates: critical 0, precision 1.0 >= 0.95, must_recall 1.0 >= 0.9, redundancy 0.0 <= 0.15, all pass. No Partial/Unverifiable: Pass. weighted = 0.4*1.0+0.4*1.0-0.2*0.0 = 0.80. No leveraged fixes.
