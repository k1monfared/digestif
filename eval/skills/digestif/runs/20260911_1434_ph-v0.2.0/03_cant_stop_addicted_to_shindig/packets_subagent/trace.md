# Judge trace: 03_cant_stop_addicted_to_shindig (model muse-spark-1.3-contributor-free 2026-09-11)

Scope: SDIR source.txt (710 lines) vs output.log (39 physical lines).
Atomization: L01 title header skipped (no propositional content). L02-L33 mapped to C01-C32 one claim per line. L34 section header plus L35-L38 cross-links skipped as structural meta. L39 coverage footer skipped as boilerplate. Number-dense sample: every fraction, percentage, and count checked digit by digit against source.

## Judge F transcript (faithfulness, precision 31/32 = 0.9688, critical 0)

Method: source only, no outside knowledge. Strict number checking throughout.

- C01 (L02 summary): Supported. All four compressed findings match the conclusion section.
- C02-C05 (L03-L06): Supported. Push-your-luck rules, 2-to-12 geometry with 3-to-13 steps and three-to-win, forced-move rule near-verbatim, and the {6,7,8} plus (1,1,3,4) example with identical forced outcome.
- C06 (L07 flattening): Supported. Stated in both the analysis question and the conclusion numbers.
- C07-C11 (L08-L12): Supported. Two-dice 16.67 and 6x exact; three pairings exact; P(2) condition plus 171/1296 plus 13.2 exact; P(7) method plus 834/1296 plus 64.4 exact; ratios 4.88 and 4.33 exact with matching designer inference.
- C12-C15 (L13-L16): Supported. Combinations thesis, near-20 clustering with 7-faster-than-2, 92.0 versus 43.8, and the 37-excellent plus 79.6-median plus 43.8-worst distribution all exact.
- C16-C19 (L17-L20): Supported. Heuristic formula with matching variables, both worked examples with matching stakes and stop/roll decisions, both clean percentages exact, continuation leaning with the quantitative hedge preserved (hedged source kept hedged).
- C20 (L21 simulations verdict): Supported. 3.6M count exact; probabilistic-dominance plus consistency-over-speed verdict matches findings.
- C21 (L22 38 strategy families): Contradicted, Minor. Source counts 38 strategies across 14 families; claim promotes families to 38. The 38 figure is real but attached to the wrong taxonomic level. No conclusion rests on the family count (all findings cite strategy names), so impact is Minor rather than Critical.
- C22-C25 (L23-L26): Supported. GreedyUntil1Col 10.5 plus 7.5 exact; FiftyPercentSurvival 69.84 plus below-50 rule exact; consistency lesson plus pure-greedy failure stated; first-player 55.59 plus 11.18 plus chess/Go comparison all exact.
- C26-C32 (L27-L33): Supported. Balance verdict, 13.6 bound exact, 4x improvement exact, contamination mechanism, player plus designer takeaways, 5-9 targeting advice, artifact availability.
- Severity note: supported number claims marked Critical for stakes; the single contradiction assessed Minor impact, hence critical_errors 0. No flipped negations, no swapped entities.

## Judge Cov transcript (coverage, must_recall 12.5/13 = 0.9615, overall 14.5/15 = 0.9667)

Blind checklist from source before mapping: rules, two-dice, four-dice, ratio match, expected rolls, combos, stopping, clean moves, continuation, simulations, first-player, balance, takeaways (13 Must), plus linear variants and artifacts (2 Nice). Mapping: 12 Must Present, 1 Must Partial. K10 (simulations) Partial because the family count contradicts the source number; per the conflict rule no credit is taken from the contradicted count itself, while everything else in K10 (scale, champion, win rate, paradox, greedy failure) rests on Supported claims and holds. Both Nice points Present.

## Judge Con transcript (concision, redundancy 0.0, trivia 0.0)

32 claims labeled, all 32 Unique. No duplicates: contamination moral (C29) adds the design reading distinct from clean-move evidence (C18); takeaway header (C30) adds the normative verdict distinct from the consistency finding (C24); the three domain-adjacent claims each carry distinct numbers. No trivia: every claim maps to a Must or Nice point, and numbers, caveats, and negations are never trivia by rule. C21 keeps Unique despite its Contradicted verdict per the rule that concision never hides a faithfulness verdict. Density: 542 words over 32 unique claims = 16.94 tokens per unique claim, the densest of the three samples.

## Judge Top transcript (weighted 0.7721, verdict Borderline)

Gates: critical 0 vs max 0 pass; must_recall 0.9615 vs min 0.9 pass; precision 0.9688 vs min 0.95 pass; redundancy 0.0 vs max 0.15 pass. No Fail on gates. Borderline because the single Contradicted count touches Must point K10 and advises human review despite Minor impact. Computation 0.4*0.9688 + 0.4*0.9615 - 0.2*0.0 = 0.7721. Tradeoff: highest recall at zero redundancy, length fully justified. One one-line fix (38 strategies across 14 families) moves precision to 1.0 and must_recall to 1.0 for a clean 0.8 Pass.
