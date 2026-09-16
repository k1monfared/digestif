# Failure report: 20260915_1400_ph-v0.4.0

Generated: 2026-09-16 by `eval/lib/failures.py`.

## Summary

* claims judged: 1331
* non-supported claims: 14 (partial 13, unverifiable 0, contradicted 1, critical 1)
* non-present key points: 2
* duplicate labels: 116, trivia labels: 49

Per sample detail follows. Every entry cites its claim or point id, the deciding evidence, and the judge's reasoning so a human can audit or overturn it.

## 01_what_is_mathematics

Verdict: Borderline (weighted 0.7781, precision 0.9854, must recall 1.0, redundancy 0.0803)

### Non-supported claims

* C003 [Partially supported, Minor] loglog 0
  * claim: Mathematics is shifting toward deciding which patterns matter.
  * evidence: I am speculating that the mix is shifting: as proving and verification get automated, the weight moves to deciding which patterns matter
  * why: Source hedges with "I am speculating"; the node states the shift as fact, dropping the qualifier.
* C077 [Partially supported, Minor] loglog 3
  * claim: Tao's pipeline: proof abundance threatens to break the correlation of the community's goals, and the bottleneck shifts to digestion, the work treated as low prestige.
  * evidence: AI optimization threatens to break the correlation. ... The bottleneck shifts to proof digestion, and digestion is the work we currently treat as low prestige.
  * why: Bottleneck-low-prestige part is exact, but source attributes the correlation break to AI optimization, not proof abundance itself.
* C179 [Partially supported, Minor] loglog 6.12.3
  * claim: Citation networks already made the pre-AI canon path-dependent, so an attention-mediated canon would be worse.
  * evidence: If citation networks already made the pre-AI mathematical canon path-dependent, an attention-mediated canon would be worse
  * why: Source frames the antecedent conditionally with 'If'; node asserts it as established fact, dropping the condition.
* C241 [Partially supported, Minor] loglog 9.2
  * claim: Many mathematicians publish anything they can prove, and much of science works that way.
  * evidence: I know of mathematicians who will publish anything they can prove. In fact much of science works that way.
  * why: Source says 'I know of mathematicians', an existence claim; loglog strengthens it to 'Many', an unsupported quantifier upgrade.

### Concision flags

* C001 Duplicate of C025: Summary restates proof production automated; 1.9 carries no less.
* C002 Duplicate of C034: Summary restates verification automated; 1.13 states it fully.
* C003 Duplicate of C246: Summary thesis restated at 9.4 speculation on shifting weight.
* C004 Duplicate of C239: Summary claim restated fully at 9.1.1.
* C005 Duplicate of C250: Summary home claim restated at 9.5.
* C026 Duplicate of C013: Restates First Proof result already given at 1.5.
* C027 Duplicate of C015: Restates choosing stayed human already at 1.5.2.
* C072 Duplicate of C071: Restates friction removal and reader learning loss.
* C113 Duplicate of C024: Restates the split already given at 1.8.
* C124 Duplicate of C090: Restates acceptance external and unoptimizable.
* C125 Duplicate of C122: Restates both locate importance on stable ground.
* C151 Duplicate of C144: Restates same-for-math, adding only timing.
* C168 Duplicate of C140: Restates engagement replacing checkable standing.
* C211 Duplicate of C101: Restates the digestion bottleneck at 7.4.
* C212 Duplicate of C201: Restates middle emptying loses legible, checkable people.
* C231 Duplicate of C213: Restates attention economy manufacturing hollow agreement.
* C238 Duplicate of C237: Restates importance as the real constraint.
* C239 Duplicate of C183: Recaps checkability floor and structural ceiling.
* C253 Duplicate of C110: Restates finding, judgment, taste becoming visible.
* C262 Duplicate of C204: Retells woodworking craft-does-not-die in conclusion.
* C268 Duplicate of C049: Restates process-product as struggle is product.
* C269 Duplicate of C067: Restates proving-as-gym image.
* C076 Trivia: Aside about slides; no argumentative weight.
* C109 Trivia: One-line filler restating the inversion already implied.
* C229 Trivia: Quip adding no substantive claim.
* C233 Trivia: Pointer to thought experiment, no new information.

### Fix list

* Restore causal attribution in C077 (loglog 3): source says AI optimization threatens to break the correlation, not proof abundance itself; this sits on the Tao-pipeline Must have point.
* Re-add the speculation qualifier in C003 (loglog 0): change the asserted shift to 'I am speculating that the mix is shifting' so the deciding-which-patterns point is not stated as fact.
* Restore the conditional in C179 (loglog 6.12.3): keep 'If citation networks already made the canon path-dependent' rather than asserting it as established.
* Downgrade the quantifier in C241 (loglog 9.2): 'Many mathematicians' should read 'mathematicians I know of' per the existence claim in source.
* Prune redundancy to push below current 0.0803: C026/C027 restatements, C113, C211, C239, C262, C268, C269 are the cheapest single-line drops; C003 also duplicates C246.

## 02_case_for_transparent_government

Verdict: Pass (weighted 0.77664, precision 1.0, must recall 1.0, redundancy 0.1168)

### Concision flags

* C079 Duplicate of C022: Repeats C022 privacy-tech feasibility; adds nothing new.
* C088 Duplicate of C045: Repeats NZ 30-day release already in C045.
* C108 Duplicate of C089: Repeats C089 opacity-versus-accountability point.
* C109 Duplicate of C105: Repeats C105 build-capacity-not-reduce-information recommendation.
* C130 Duplicate of C055: Repeats C055 predicted-catastrophe pattern using Snowden.
* C133 Duplicate of C095: Repeats C095 temporary operational secrecy concession.
* C134 Duplicate of C096: Repeats C096 post-conclusion disclosure recommendation.
* C158 Duplicate of C120: Repeats C120 conspiracy-theories-need-information-gaps claim.
* C167 Duplicate of C096: Repeats C096 time-delayed transparency recommendation.
* C189 Duplicate of C183: Repeats C183 measuring-stick claim.
* C198 Duplicate of C024: Appendix recap of C024 Sweden 1766 claim.
* C199 Duplicate of C034: Appendix recap of C034 X-Road claim.
* C200 Duplicate of C040: Appendix recap of C040 Brazil portal claim.
* C201 Duplicate of C043: Near-verbatim repeat of C043 pension-data finding.
* C202 Duplicate of C030: Appendix recap of C030 Seoul OPEN claim.
* C204 Duplicate of C063: Appendix recap of C063 USA FREEDOM claim.
* C205 Duplicate of C074: Appendix recap of C074 Pew numbers.
* C206 Duplicate of C082: Appendix recap of C082-C084 efficiency sources.
* C207 Duplicate of C092: Appendix recap of C092 diplomacy backchannel evidence.
* C208 Duplicate of C099: Appendix recap of C099-C104 special-interest studies.
* C209 Duplicate of C112: Appendix recap of C112-C118 safety survey.
* C210 Duplicate of C124: Appendix recap of C124-C130 security sources.
* C211 Duplicate of C138: Appendix recap of C138 populism objection and sources.
* C212 Duplicate of C153: Appendix recap of C153 misinformation objection.
* C213 Duplicate of C176: Appendix recap of C176 OGP structural-barrier evidence.
* C009 Trivia: Draft-status note, no argumentative content, low information value.
* C010 Trivia: Meta aside about author stance; adds no substantive point.
* C091 Trivia: Concession filler, no substantive information.
* C111 Trivia: Concession filler, no substantive content beyond transition.
* C137 Trivia: Meta aside about the author, no substantive point.
* C152 Trivia: Meta aside about the author, no substantive point.
* C193 Trivia: Bridging transition, no substantive information.

### Fix list

* Collapse the appendix recap duplicates flagged by Judge Con (C198-C213 mapping to C024/C030/C034/C040/C043/C055/C063/C074/C082/C092/C099/C112/C120/C124/C138/C153/C176), since they add length with zero coverage gain and are the largest single block of the 25 duplicates.
* Merge the near-verbatim and same-idea inline duplicates before the appendix: C201/C043 (60GB pension data), C079/C022, C088/C045, C108/C089, C109/C105, C130/C055, C133/C095, C134/C096, C158/C120, C167/C096, C189/C183.
* Trim or drop the 7 trivia claims (trivia_rate 0.0327) identified by the concision judge to push redundancy further under the 0.15 gate ahead of future edits.

## 03_cant_stop_addicted_to_shindig

Verdict: Borderline (weighted 0.7802, precision 0.989, must recall 1.0, redundancy 0.0769)

### Non-supported claims

* C001 [Partially supported, Minor] loglog 0
  * claim: Can't Stop's four-dice probabilities and forced-move rule make it nearly balanced, and simulations show probabilistic, consistent play wins, though going first is a large advantage.
  * evidence: The game heavily favors middle columns.
  * why: Probabilistic consistency and first-player advantage are supported, but source says combination play is badly imbalanced, not 'nearly balanced'.

### Concision flags

* C021 Duplicate of C009: Explicit conclusion recap of section 2; adds nothing.
* C036 Duplicate of C029: Explicit conclusion recap of section 4; adds nothing.
* C062 Duplicate of C057: Conclusion recap of probabilistic dominance; repeats C057/C044.
* C063 Duplicate of C050: Conclusion recap of consistency-beats-speed; repeats C050.
* C071 Duplicate of C064: Conclusion recap of first-player advantage; adds nothing.
* C076 Duplicate of C035: Restates 4.7 balancing mechanism per cross-link; same point.
* C087 Duplicate of C072: Conclusion recap of design conclusion; adds nothing.
* C008 Trivia: Web artifact mention, low analytical value for the argument.
* C056 Trivia: Matrix/CSV artifact mention, no analytical value.
* C091 Trivia: Code/data link meta, no analytical value.

### Fix list

* Fix C001: source loglog line 0 says combination play is 'badly imbalanced' and 'heavily favors middle columns', so soften 'nearly balanced' on the Must-have balance point.
* Fix C076: merge into C035, same balancing mechanism, redundant.
* Fix C021/C036/C062/C063/C071/C087: merge section recaps into their originals C009/C029/C057/C050/C064/C072.
* Cut low-value artifact claims C008, C056, C091, which add trivia without supporting a point.

## 04_house_hunting_shenanigans

Verdict: Pass (weighted 0.7647, precision 0.9804, must recall 1.0, redundancy 0.1373)

### Non-supported claims

* C036 [Partially supported, Minor] loglog 4.4
  * claim: Naps are super rare for him, about once every few years, usually when a big load is lifted.
  * evidence: It is super rare for me to take a nap in the afternoon, like once every few years.
  * why: Source restricts rarity to afternoon naps, node generalizes to all naps, dropping that scope qualifier.
* C047 [Partially supported, Minor] loglog 4.15
  * claim: N thought the other offer was at that price but had a condition they disliked; the buyer didn't buy any of it.
  * evidence: He thinks the other offer is actually at this price but there might be a condition in there that they don't like it.
  * why: Source hedges with 'might be a condition', node states 'had a condition' as settled fact.

### Concision flags

* C009 Duplicate of C010: Theme header restating the 30K maximum-affordability offer already in C010.
* C032 Duplicate of C039: Theme header restating the 20K drop already in C039.
* C067 Duplicate of C065: Second statement of N seeing the team as incompetent; no new content.
* C070 Duplicate of C075: Theme header restating the 10K-below sale already in C075.
* C085 Duplicate of C084: Repeats the Claude debrief intro from C084 with no new detail.
* C087 Duplicate of C020: AI recap of the full-asking first offer already in C020.
* C088 Duplicate of C039: AI recap of pivots already in C031, C039, C050.
* C090 Duplicate of C021: Recaps strategic moves already stated in C021 and C029.
* C091 Duplicate of C072: Restates the realtor manipulation lesson already in C072.
* C095 Duplicate of C072: Same manipulation and asymmetry framing as C072 and C091.
* C097 Duplicate of C069: Repeats the weekend's information value already claimed in C069.
* C098 Duplicate of C084: Meta line repeating that the post includes AI analysis, already in C084.
* C099 Duplicate of C029: Successes recap the bluff detection already in C029 and C064.
* C102 Duplicate of C094: Recommendation list overlapping C094's improvements list.
* C002 Trivia: Section header restating context already carried by C004 and C007.
* C007 Trivia: Structural description of table columns; presentation detail, low value.
* C017 Trivia: Section header restating House B events delivered by its children.
* C055 Trivia: Section header restating the email exchange detailed in its children.
* C077 Trivia: Section header restating reflections delivered by 7.1 through 7.5.

### Fix list

* Restore the scope qualifier in C036: change 'naps are super rare' to 'afternoon naps are super rare' to match loglog 4.4.
* Soften C047 from settled fact to hedge ('might have a condition') per loglog 4.15.
* Merge the 14 duplicate pairs (C009/C010, C032/C039, C067/C065, C070/C075, C085/C084, C087/C020, C088/C039, C090/C021, C091/C072, C095/C072, C097/C069, C098/C084, C099/C029, C102/C094) to push redundancy further under the 0.15 cap.
* Prune section-header/structural trivia C002, C017, C055, C077, C007.

## 05_manufacturing_taste

Verdict: Borderline (weighted 0.76784, precision 0.9918, must recall 0.9688, redundancy 0.082)

### Non-supported claims

* C035 [Partially supported, Minor] loglog 3.2.3
  * claim: The same song ranked 1st in one version of the world and 40th in another, purely from random early differences in downloads.
  * evidence: the same song could rank 1st in one version of the world and 40th in another, purely because of random early differences in who happened to download it first
  * why: Numbers 1 and 40 match, but source hedges with "could"; loglog states "ranked" as certain fact.

### Non-present key points

* K10 [Must have, Partial]
  * point: Counterfactual experiment: holding every composer's talent constant and reshuffling only resources over 200 runs produced a counterfactual distance of 0.88 on a 0-to-1 scale; only the top 10% of talent had a meaningful shot (~1 in 4), and the 50th to 90th percentile faced fame as essentially a lottery.
  * loglog: L057, L058, L059, L060
  * why: The core numbers (0.88, top 10%, ~1 in 4, 50th-90th lottery) and the talent-constant/reshuffle setup are fully present. However, the stated run count of 200 for this specific experiment is omitted; L047-L048 give run counts only for the main experiments generally. Because this is a Must have point with a dropped number, per the strict rule it is capped at Partial even though the substance is intact.

### Concision flags

* C059 Duplicate of C019: Restates middle-is-luck as a lottery; cross-linked to 2.3.3.
* C060 Duplicate of C007: Cross-linked restatement of the Haydn question from 1.5.
* C061 Duplicate of C007: Same Esterházy counterfactual as 1.5, restated with its answer.
* C080 Duplicate of C001: Conclusion restates the opening summary thesis with little added.
* C082 Duplicate of C072: Repeats lost equally-gifted composers from 4.5.4.
* C090 Duplicate of C088: Punchline repeats the exposure-bottleneck claim from 5.3.1.
* C105 Duplicate of C069: Cross-linked restatement of the 2.5% overlap from 4.5.1.
* C110 Duplicate of C081: Cross-linked restatement of the qualified-greatest claim from 5.1.
* C113 Duplicate of C092: Repeats canon contingency and inevitability already stated in 5.4.1.
* C119 Duplicate of C092: Third restatement of contingency claim from 5.4.1.
* C009 Trivia: Housekeeping meta about this being a less formal paper; no substantive point.
* C040 Trivia: Transition restating section 3 theme and previewing interaction.
* C111 Trivia: Bare pointer to the simulation verdict already conveyed; adds nothing.

### Fix list

* K10 (L057-L060): restore the explicit run count of 200 for the counterfactual experiment so the Must have point is fully supported and must_recall rises toward 1.0
* C035 (3.2.3): reinstate the source hedge, change 'ranked 1st ... and 40th' to 'could rank 1st ... and 40th', to clear the sole non-supported claim
* Prune the 10 duplicate claims per the concision list (e.g. C059/C019, C060/C061/C007, C090/C088) to lower redundancy without touching coverage

## 06_valuing_consistency

Verdict: Borderline (weighted 0.77902, precision 0.9919, must recall 1.0, redundancy 0.0887)

### Non-supported claims

* C090 [Partially supported, Minor] loglog 6.11
  * claim: But the same trajectory falls out of a much less flattering process: aging brings assets, income, and things to lose from redistribution.
  * evidence: As people age they typically acquire assets, income, and things to lose from redistribution.
  * why: Source hedges with 'typically'; loglog states 'aging brings' as absolute, dropping the qualifier.

### Concision flags

* C029 Duplicate of C028: Restates C028 that the output-observed gap vanishes at deeper layers.
* C031 Duplicate of C030: Repeats C030's invisible drift and moral-weight location.
* C041 Duplicate of C039: Restates C039 as a formula, adding no new claim.
* C050 Duplicate of C047: Restates C047 that only the Independent needs no reference information.
* C069 Duplicate of C067: Restates C067's same-form opposite-verdict conclusion.
* C082 Duplicate of C081: Image restating C081's hysteresis with no new claim.
* C092 Duplicate of C085: Restates C085's identical-outcome point plus retrospective story already implied.
* C107 Duplicate of C106: Pithy restatement of C106, no new claim.
* C108 Duplicate of C085: Restates the identical-behavior and identical-retrospection already asserted.
* C119 Duplicate of C009: Restates C009 that behavioral consistency was only a bad proxy.
* C123 Duplicate of C111: Restates C111 that only the advance question is trusted.
* C010 Trivia: Restated purpose line, no claim beyond C002 and C009.
* C033 Trivia: Economist vocabulary aside, no argumentative contribution.
* C110 Trivia: Rhetorical transition, no claim beyond the surrounding lines.
* C117 Trivia: Recap header about the word splitting, no new claim.

### Fix list

* C090 (loglog 6.11): restore the source's 'typically' qualifier so 'aging brings assets' reads 'as people age they typically acquire assets', removing the unsupported absolute causal phrasing that affects this Must-have point.
* Merge the 11 duplicate claims flagged by concision (C029, C031, C041, C050, C069, C082, C092, C107, C108, C119, C123) to lower redundancy further, though redundancy already passes at 0.0887.

## 07_intentionalism

Verdict: Borderline (weighted 0.78058, precision 0.9925, must recall 1.0, redundancy 0.0821)

### Non-supported claims

* C131 [Partially supported, Minor] loglog 10.6.4
  * claim: After 30 days the pattern is clear: proposer entries show higher satisfaction, and this evidence motivates continued practice.
  * evidence: After 30 days, you'll see the pattern clearly. Proposer entries will show higher satisfaction.
  * why: Source presents future prediction ('you'll see', 'will show'); node asserts it as present fact.

### Concision flags

* C027 Duplicate of C024: Verbatim restatement of the trap already asserted as theme.
* C030 Duplicate of C023: Preferences-as-reactions repeats never-practiced-wanting point.
* C042 Duplicate of C017: Reasserts most people are receivers, already generalized in C017.
* C047 Duplicate of C010: Those people end better restates systematic proposer advantage.
* C055 Duplicate of C022: System persists because good enough repeats self-sustaining claim.
* C066 Duplicate of C031: Lost capacity to know wants repeats C031.
* C072 Duplicate of C034: Decide what you want before phone repeats start-tonight practice.
* C080 Duplicate of C010: Proposers end better repeats the core advantage claim.
* C081 Duplicate of C048: Not special, other side of equation restates C048.
* C133 Duplicate of C063: Practicing what-do-I-want-first repeats the ask-what-you-want imperative.
* C134 Duplicate of C079: Muscle builds and capacity grows restates the muscle sequence.
* C082 Trivia: Appendix announcement only; pure navigation, no argument content.
* C083 Trivia: Entertainment agenda header restating its children.
* C111 Trivia: Relationships agenda header restating its children.
* C119 Trivia: Daily micro-practices agenda header restating its children.

### Fix list

* Re-tense C131 (loglog 10.6.4) to match the source's predictive framing: change 'proposer entries show higher satisfaction' to 'the source predicts proposer entries will show higher satisfaction after 30 days', since the quote is 'you'll see ... will show'.
* Merge the 11 listed duplicates, starting with the verbatim trap restatements: C027 into C024 and C030 into C023, then C042/C047/C055/C066/C072/C080/C081/C133/C134.
* Cut agenda-header restatements C082, C083, C111, C119, which only restate their children and add no unique claim.
* Trim trivia (4 items, trivia_rate 0.0299) to push redundancy closer to zero and raise weighted score toward 0.8.

## 08_empathy_sympathy_compassion_matrix

Verdict: Pass (weighted 0.79428, precision 1.0, must recall 1.0, redundancy 0.0286)

### Concision flags

* C034 Duplicate of C014: Recap of Kantianism and Humanism row relations already stated; near-duplicates C014 and C015.
* C020 Trivia: Restated section header; scope caveat already carried by clinical note 4.9.

### Fix list

* Merge C034 into C014 (it also near-duplicates C015), collapsing the three Kantianism/Humanism relation recaps into one canonical statement.
* Drop C020 (trivia restatement of the 'Notes' Theme header); it carries no information beyond the section label.

## 09_not_even_wrong

Verdict: Pass (weighted 0.7789, precision 1.0, must recall 1.0, redundancy 0.1053)

### Concision flags

* C024 Duplicate of C001: Restates summary thesis that factors override scrutiny; no new proposition.
* C030 Duplicate of C027: Same advice as C027 with a heuristic question; no new proposition.
* C034 Duplicate of C027: Repeats separating evaluation from support, already stated in C027.
* C035 Duplicate of C033: Repeats independent evaluation and not-for/against from C033.
* C026 Trivia: Roadmap header restating section structure; low information value.
* C032 Trivia: Meta description of the closing; restated header, low value.

### Fix list

* Merge C024 into C001 to remove the one body-level duplicate (no factual impact).
* Merge C030 and C034 into C027, and C035 into C033, to cut the remaining 3 duplicate claims and lower redundancy_rate further.
* Prune restated headers C026 and C032 from the scored body to reduce trivia_rate from 0.0526 and improve tokens_per_unique_claim (currently 25.1).

## 10_parde_begardan_fa

Verdict: Fail (weighted 0.76552, precision 0.9655, must recall 1.0, redundancy 0.1034)

### Non-supported claims

* C008 [Contradicted, Critical] loglog 2
  * claim: سنتور را با تخفیف خریدم و یادگیری را با دشواری‌های ساز و مکان شروع کردم.
  * evidence: بالاخره برام یه سنتور خریدن. ۲۰هزار تومن، با تخفیف شد ۱۸هزار تومن.
  * why: Source says the santur was bought for the author (خریدن), but the node attributes the purchase to the author (خریدم): wrong attribution.

### Concision flags

* C021 Duplicate of C020: Rapid key retuning restated; reader learns nothing new beyond C020.
* C027 Duplicate of C002: Recaps the first-night scene (C002/C003) and kid metaphor (C016); adds no information.
* C029 Duplicate of C028: Same travel-longing as C028; only a rhetorical inversion is added.

### Fix list

* Fix C008 (loglog id 2): change 'سنتور را با تخفیف خریدم' to reflect that the santur was bought for the author (برام یه سنتور خریدن), not by the author, since wrong attribution contradicts the source quote 'بالاخره برام یه سنتور خریدن. ۲۰هزار تومن، با تخفیف شد ۱۸هزار تومن.'
* Remove C021 (merge into C020), C027 (recap echoing C002/C016), and C029 (merge into C028) to drop redundancy_rate from 0.1034 toward ~0 without any coverage loss.

## 11_finding_a_phone

Verdict: Borderline (weighted 0.77148, precision 0.9828, must recall 0.9545, redundancy 0.0172)

### Non-supported claims

* C033 [Partially supported, Minor] loglog 5.1.1
  * claim: Ordered a latest Google Pixel on a Black Friday deal, thinking to maybe try the always-connected life; people generally said good things.
  * evidence: just as black Friday was approaching I got fooled by a deal from my network provider and ordered a latest version of google pixel
  * why: Source says a network-provider deal as Black Friday approached; loglog recasts it as a Black Friday deal and drops the provider.

### Non-present key points

* K15 [Must have, Partial]
  * point: Update 2025-01-05: he tried the TCL 50 XE NXTPAPER for a couple of weeks; weak performance, uncomfortably hot video calls, much worse almost-unreadable screen in direct or lamp light, average camera; paper and ink color modes were good ideas but poorly implemented with many restrictions and not true e-ink. He returned it and next plans the Motorola G85, wanting the more waterproof IP68 G75 but unable to find it in stores; G85 is only water repellent and Motorola cameras generally not expected to be good.
  * loglog: L055, L056, L057, L058, L059
  * why: All substantive content is captured, but the update date 2025-01-05 is dropped entirely. The rubric requires dates as key numbers, so a Must have point lacking its date is capped at Partial.

### Concision flags

* C030 Duplicate of C001: Closing recap of same journey and anti-gimmick thesis, no new point.
* C002 Trivia: Restated section header summarizing C003-C008, adds no new information.
* C009 Trivia: Section header restating C010-C016, no information beyond children.
* C012 Trivia: Filler transition restating theme 2 functionality-over-flashiness, no new fact.
* C017 Trivia: Section header restating C018-C023, redundant summary.
* C024 Trivia: Section header restating C025-C029, no new information.
* C031 Trivia: Section header restating C032 and C036, redundant.
* C032 Trivia: Sub-header restating C033-C035, redundant.
* C036 Trivia: Section header restating C037-C046, no new information.
* C047 Trivia: Section header restating C048 and C053, redundant.
* C048 Trivia: Sub-header restating C049-C052, no new information.
* C053 Trivia: Sub-header restating C054-C058, redundant.

### Fix list

* Restore the dropped date in K15 (loglog L055-L059) so the TCL 50 XE NXTPAPER return update carries its 2025-01-05 timestamp and upgrades from Partial to Present; this is the single gate-relevant gap.
* Correct C033 (loglog 5.1.1): source says a deal from his network provider as Black Friday approached, not a Black Friday deal; restore the provider attribution to remove the lone Partial claim.
* Prune or merge the 12 flagged header/transition claims (C002, C009, C012, C017, C024, C030, C031, C032, C036, C047, C048, C053) to cut trivia_rate (0.1897) without touching coverage.

## 12_lets_talk_privacy

Verdict: Borderline (weighted 0.78, precision 0.9818, must recall 1.0, redundancy 0.0636)

### Non-supported claims

* C005 [Partially supported, Minor] loglog 1.3
  * claim: If the purpose is only to defeat a man-in-the-middle attack, most implementations should be good enough.
  * evidence: If the purpose is that a man-in-the-middle attack will not likely compromise your data, then most implementations of this should be good enough
  * why: Source hedges with "not likely compromise"; node strengthens to "defeat" and adds "only", dropping the probabilistic qualifier.
* C018 [Partially supported, Minor] loglog 2.8
  * claim: Encryption is locking something with a key: one that only locks and that everyone has, and a master key only the receiver holds.
  * evidence: I think of encryption as locking something and having a key (usually a pair of keys, the one that only locks it and everyone has that, and a master key that only the receiver of the data has it
  * why: Source frames this as the author's model and hedges "usually a pair of keys"; node states it as a flat definition.

### Concision flags

* C023 Duplicate of C022: Billboard analogy restates C022 with no new proposition.
* C075 Duplicate of C052: Infrastructure not breached restates item 3.12.3 with no new content.
* C088 Duplicate of C027: Table row recaps the provider rogue-device point from 2.15.
* C101 Duplicate of C077: Facebook plaintext logging recap; only adds figures to the same fact.
* C103 Duplicate of C078: Adobe 2013 plaintext hints restated with brute-force note.
* C104 Duplicate of C079: Small-services plaintext/MD5 restated with breach discovery.
* C109 Duplicate of C083: Bottom line restates the section 6 trust-basis claim nearly verbatim.
* C035 Trivia: Pure signpost introducing the login sequence; no independent content.
* C049 Trivia: Signpost to the trust list; supplies no facts itself.
* C076 Trivia: Lead-in to the examples; filler framing with no fact.
* C087 Trivia: Restated header describing the comparison tables; no new claim.
* C091 Trivia: Restated header for the verification theme; no independent claim.

### Fix list

* Fix C005 (loglog 1.3): restore the source hedge, change 'defeat a man-in-the-middle attack' back to 'will not likely compromise your data' and drop 'only', so the probabilistic qualifier survives.
* Fix C018 (loglog 2.8): frame the encryption statement as the author's model with the source hedge 'usually a pair of keys' instead of asserting it as a flat definition.
* Prune the seven duplication pairs (C023/C022, C075/C052, C088/C027, C101/C077, C103/C078, C104/C079, C109/C083) and the five trivia signposts/headers (C035, C049, C076, C087, C091) to push redundancy (0.0636) and trivia (0.0455) further down.

