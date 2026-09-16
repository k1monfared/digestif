# Judge trace: 05_manufacturing_taste (judge model muse-spark-1.3-contributor-free 2026-09-11)

## Judge F: faithfulness (52 claims, 51 Supported + 1 Partial Minor, precision 0.9808)

Atomization policy: one leaf bullet yields one claim; every bullet carries a
single fact except L04, L20, L25, L27, L30, which pack co-stated figures that
were verified figure by figure inside one claim each. Title L01 and Summary L02
are meta/interpretation claims. The Cross-links block (lines 53-62) and
Coverage footer (line 63) are skipped as boilerplate relational notes.

Figure-by-figure verification: 200-500 Vienna composers and 3,400 IMSLP
survivors (C04); Zajonc 1968, Bornstein 1989, r 0.26 (C12); MusicLab 2006 with
1st-vs-40th ranks (C14); 1,000 producers, 10,000 consumers, thousands of runs,
360-plus per condition with power analysis (C20); p below 0.0001 (C22); 200
replay runs (C24); distance 0.88 with top-decile 1-in-4 and middle lottery
(C25); ablation 0.32/0.35/0.46/0.46 (C27); 44% jump (C28); Vienna 300, 0.97,
2.5% shared (C30); blind auditions 5% to 25% (C39); 20-50 Leipzig equals (C49).
External-study and historical claims carry [reported] tags where the outline
set them, and hedges (may have, likely, very likely, probably, may) are
preserved everywhere except one place.

The one exception is C52 (8.7): source conditions the future-canon prediction
twice (I honestly don't know; if the mechanisms in this simulation are right,
then whoever survives...). The outline states it absolutely, so per the hedge
rule it is at most Partially supported. Low-stakes closing speculation, so
severity Minor, not Critical. No contradictions, no unverifiable claims, no
name swaps (Haydn, Esterhazy, Zajonc, Bornstein, Salganik, Merton, Bach, Bieber
all correct), no dropped negations.

Result: supported 51, partial 1, contradicted 0, critical_errors 0, precision
51/52 = 0.9808, fail_list names C52 only.

## Judge Cov: coverage (12 must + 3 nice, must_recall 1.0, overall 0.9)

Blind checklist from source: canon puzzle, three stories plus analogy, three
mechanisms with key evidence, simulation design, social-influence result plus
proxy trap, replay experiment, ablation plus exclusion verdict, stylized
Vienna, robustness, Story-3 verdict plus four implications, caveats, closing
answer (must); Hadi opener, repo/paper links, 50M-vs-500 illustration (nice).

Mapping notes: K03 is Present because the thinned sample sizes (208
experiments; 14,341 participants, 48 songs) are supporting detail below the
point core, not dropped numbers or conditions of the point itself; all key
numbers (years, r 0.26, ranks, attribution) are intact. K12 is Present with an
explicit note that C52 drops the conditional inside it, which is why the Top
judge fires Borderline. K13 is Partial (Bieber frame present via section 8,
Hadi unattributed). K14 Missing (no repo or paper citation anywhere). K15
Present via 5.13.

Metrics: must 12/12 present so must_recall 1.0; overall 13 present plus one
partial over 15 points so (13 + 0.5)/15 = 0.9.

## Judge Con: concision (52 scored, 51 unique, 1 trivia, redundancy 0.0)

Duplicate sweep against the outline's own cross-link restatement flags: 5.2
vs 6.5 differ in scope (recommendation algorithms vs canon-as-best plus
curricula), 5.5 vs 8.4 differ (Haydn counterfactual vs Leipzig job plus 20-50
range), so each teaches something new and both pairs stay Unique. Themes vs
children all add frames versus figures. Trivia sweep: C36 (6.1, Implications
worth spelling out below) is a filler transition restating the source segue
with no information beyond announcing C37-C40, so Trivia; everything else maps
to a Must or Nice point, and number/caveat/negation claims are exempt by rule.
C52 stays visible as Unique per the never-hide-a-verdict rule. structured_tokens
889 by whitespace count; tokens_per_unique_claim 889/51 = 17.43; trivia_rate
1/52 = 0.0192. prune_list names only the C36 fold.

## Judge Top: overall (Borderline, weighted 0.7923)

Gates all pass (critical 0, precision 0.9808, must_recall 1.0, redundancy 0.0),
but Partial claim C52 sits inside Must-have K12, so the Borderline rule
requires human review of that one qualifier loss. Computation: 0.4*0.9808 +
0.4*1.0 - 0.2*0.0 = 0.7923. Tradeoff: full must-recall at zero redundancy, so
length is justified. Fix list by leverage: reattach the conditional to C52
first (clears Borderline), then repo/paper links and Hadi attribution, then
the optional C36 fold.
