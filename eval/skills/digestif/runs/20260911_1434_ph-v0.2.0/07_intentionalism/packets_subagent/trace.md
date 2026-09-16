# Judge trace: 07_intentionalism (run 20260911_1434_ph-v0.2.0, model muse-spark-1.3-contributor-free 2026-09-11)

## Judge F: Faithfulness (52 atomic claims, physical lines L01-L50 as loglog IDs; cross-links L51-L55 and coverage line L56 excluded as boilerplate with no source-fact content)

Atomization policy: one claim per content bullet, except the Summary (L02) which contains two distinct propositions (structural claim C02 + prescription C03) and section 1 (L03) which contains a dated-fact claim (C04) plus an asymmetry-finding claim (C05). Section 8.1 (L30) lists four behaviors but they form a single source list, kept as one claim (C32).

Verdict walkthrough:
- C01 (title): Supported. Source line 8 gives the thesis verbatim ("whether they propose or receive").
- C02/C03 (summary halves): Supported. C02 compresses lines 24/44; C03 compresses the decide-first prescription (line 105, 68-70).
- C04: Supported. Year 1962, both names, stable-pairings topic match source line 12 exactly. Checked strictly per number/date rule: no drift.
- C05-C07: Supported. Asymmetry discovery (line 14), deferred-acceptance mechanics (line 16), best/worst provable extreme (lines 16, 18) all near-verbatim.
- C08: Supported. "Not talent or luck" from line 6; dropping "quality of choices" is flagged Nuance in the outline itself and is harmless compression.
- C09: Supported. Generalization-with-limit from lines 22/36; hedges preserved.
- C10: Supported. All four receiver examples verified at lines 28/30/32/34 with matching receive-mode framing.
- C11-C15: Supported. Mostly-receiver diagnosis (36), acceptable-but-shortfall (40/42), informal-structure favoring (44), no-revolt stability (46), unpracticed wanting (48). On C13 I considered flagging the dropped "tend to" (source line 44 "outcomes tend to favor"), but "systematically" is the source's own adverb for this exact pattern (lines 24, 114) and the informal-scope qualifier is preserved, so this is a generic mechanism statement with identical meaning, not an overclaim. Distinction from C33 below: C33 absolutizes a prescriptive scope ("every decision"), while C13 preserves its descriptive scope.
- C16-C18: Supported. Chicken-and-egg thesis (52/56), least-disliked mechanism (54). C18 duplicates C16 but duplication is a concision matter, never a faithfulness fail; the verdict stays Supported.
- C19: Supported. Both music (58) and dating (60) examples plus the reactions-as-preferences gloss (62).
- C20-C23: Supported. Progressive muscle (66), tonight exercise with both "don't" negations (68/70), patterns-to-values chain (72), practice-over-thought with negation (74).
- C24-C26: Supported. Presented-options diagnosis with "most" hedges (80/82), seeker examples (84), structural-side negation (86).
- C27-C30: Supported. System optimization (90), three engagement examples (92), optimal-vs-good-enough split (94), leaving-harder stability gloss (96, verbatim incl. parenthetical).
- C31-C32: Supported. Switch imperative with negation (100); all four proposing behaviors verified against lines 105/106/107/108.
- C33: Partially supported, Harmless. Source line 110 scopes the prescription to "every major decision and most minor ones"; the outline writes "every decision". Per the hedge rule this is at most Partial. Harmless because major-plus-most-minor is practically every decision and no reader action changes; listed in fail_list for the forward skill to restore the qualifier.
- C34-C36: Supported. Most-refuse (112), shifter payoff with exact-math qualifier (114), settled-dynamic framing with isn't/is contrast (116/118).
- C37-C42: Supported. Tomorrow-morning start plus scale-up (122/132), four named states (124/126), week log (128/130), three scale-up domains (132), muscle ladder verbatim (134), math-and-mess payoff with specialness negation (136/138).
- C43-C52 (appendix): Supported. All ten appendix claims verified with load-bearing numbers intact: 5 non-negotiables and 4-of-5 (C47), 24-hour rule (C45), 10 seconds and three intentions (C50), 30 days and three journal columns (C51). No number drift anywhere, which is why critical_errors is 0.
- No Contradicted, no Unverifiable, no negation flips. faithfulness_precision = 51/52 = 0.9808.

## Judge Cov: Coverage (checklist built blind from source, then mapped)

Blind checklist rationale: thesis (K01), the 1962 result plus algorithm (K02) plus best/worst extreme (K03) as separate points because the extreme is the load-bearing finding, generalization with limit (K04), examples plus diagnosis (K05), shortfall plus stability (K06), structural cause (K07), trap plus mechanism (K08), training principle plus exercise (K09), chain plus practice-over-thought (K10), agency illusion (K11), collective effect with three sub-elements (K12), switch imperative plus four behaviors (K13), entry point plus scale-up (K14) as Must-haves; appendix detail as one Nice-to-have (K15) since it is long but subordinate. Mapping: every Must-have Present with loglog IDs cited; C33's qualifier drop does not demote K13 because the four behaviors (8.1) carry the point intact. must_recall = 14/14 = 1.0, overall_recall = 15/15 = 1.0, missing_list empty.

## Judge Con: Concision (52 scored claims; cross-links and coverage line treated as Boilerplate, excluded)

Duplicate hunt: C18 fully entailed by C16 (canonical C16); C26 fully entailed by C08 (canonical C08); C42 fully entailed by C35+C26 jointly, canonical C35 since the math/mess scope repeats the shifter payoff. Near-misses judged Unique with reasons: C13 vs C07 differ in scope (informal vs stable-matching); C41 adds the "values make proposers" consequence absent from C22; C52 adds the "before someone else provides the answer" operationalization beyond C23. Trivia hunt: every Supported claim maps to K01-K15 (appendix details to K15, examples to K05/K11/K12), and numbers/caveats/negations are never trivia by rule, so trivia = 0. Metrics: scored 52, unique 49, duplicates 3, redundancy 3/52 = 0.0577, tokens 791 (wc -w), tpu 791/49 = 16.14. Prune list cites the three merges.

## Judge Top: Overall

Gates from config.json: critical max 0 (have 0), precision min 0.95 (have 0.9808), must_recall min 0.9 (have 1.0), redundancy max 0.15 (have 0.0577). All pass. Borderline considered and rejected: the lone Partial (C33, Harmless) does not demote any Must-have point's presence. weighted = 0.4*0.9808+0.4*1.0-0.2*0.0577 = 0.7808. Verdict Pass. Fix list ordered by leverage: qualifier restore first (only faithfulness item), then the three merges cheapest-first.
