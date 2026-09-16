# Failure report: 20260911_1922_ph-v0.3.0

Generated: 2026-09-16 by `eval/lib/failures.py`.

## Summary

* claims judged: 700
* non-supported claims: 19 (partial 19, unverifiable 0, contradicted 0, critical 0)
* non-present key points: 27
* duplicate labels: 63, trivia labels: 21

Per sample detail follows. Every entry cites its claim or point id, the deciding evidence, and the judge's reasoning so a human can audit or overturn it.

## 01_what_is_mathematics

Verdict: Borderline (weighted 0.7752, precision 0.969, must recall 1.0, redundancy 0.062)

### Non-supported claims

* C041 [Partially supported, Minor] loglog 3.10
  * claim: Load-bearing activities are framing, noticing gaps, deciding attention; proving is the gym training finding.
  * evidence: Problem framing, noticing what's missing, deciding what's worth attention, those look load-bearing... And proving is the gym where the finding is trained.
  * why: SOURCE hedges with 'look load-bearing'; node asserts as definite, dropping the hedge, though list is accurate.
* C051 [Partially supported, Minor] loglog 4.3
  * claim: Goodhart: correlated goals let one proxy rest; ungrounded AI plus financial incentives break correlation.
  * evidence: AI optimization threatens to break the correlation. Generative AI is ungrounded by nature, and AI companies have financial incentives
  * why: SOURCE says AI 'threatens to' break the correlation; node states it as an accomplished fact, dropping the hedge.
* C078 [Partially supported, Minor] loglog 6.3
  * claim: Random possibly-unqualified voices beat experts; paid relatable urgency beats challenge, supporting priors.
  * evidence: And often it supports your current understanding, far better than it challenges it.
  * why: SOURCE hedges with 'often'; the node states prior-support as an absolute fact, dropping the hedge.
* C097 [Partially supported, Minor] loglog 7.2
  * claim: Neighborhood creative carpenter vanished; fixing cheap Ikea beats nobody buying new.
  * evidence: the carpenter who wants to be creative can't make a living at it anymore. At best they spend their time fixing Ikea furniture. But Ikea furniture became so cheap that nobody fixes it.
  * why: Vanished-carpenter part is supported, but the second clause is garbled and adds a 'beats' comparison absent from the source.

### Concision flags

* C009 Duplicate of C126: Restates First Proof result already stated in appendix.
* C014 Duplicate of C126: Restates First Proof result and cost with looser phrasing.
* C019 Duplicate of C115: Restates proving-as-chore, finding-as-real claim.
* C041 Duplicate of C123: Restates proving-as-gym training claim.
* C059 Duplicate of C003: Recaps professor producing-versus-checking motif.
* C062 Duplicate of C013: Restates AI-proposes, humans-digest split.
* C068 Duplicate of C031: Restates process-as-product thesis.
* C090 Duplicate of C112: Restates floor/ceiling and social-layer claim.
* C021 Trivia: Image reference, no argument content.
* C110 Trivia: Bare thought-experiment reference, no content.

### Fix list

* Restore the dropped hedges on the two thesis-level partials that affect Must-have points: C041 (3.10, SOURCE says 'look load-bearing', node asserts definite 'are') and C051 (4.3, SOURCE says AI 'threatens to' break the correlation, node asserts it as accomplished). This is the highest-leverage fix because these drive the Borderline call.
* Restore the 'often' hedge on C078 (6.3) where the node states prior-support as an absolute fact.
* Repair the garbled clause and remove the unsupported 'beats nobody buying new' comparison in C097 (7.2).
* Merge the 8 duplicate claims (C009/C014 -> C126, C019 -> C115, C041 -> C123, C059 -> C003, C062 -> C013, C068 -> C031, C090 -> C112) and drop the 2 trivia (C021 image reference, C110 thought-experiment reference) to drive redundancy 0.062 toward 0.0; note C041 also appears in the faithfulness partial list, so fixing the hedge and the duplicate together is efficient.

## 02_case_for_transparent_government

Verdict: Pass (weighted 0.7632, precision 0.98, must recall 1.0, redundancy 0.144)

### Non-supported claims

* C032 [Partially supported, Minor] loglog 5.3.1
  * claim: OPEN tracks 70 corruption-prone tasks, including construction, environmental, and urban planning permits, in real time.
  * evidence: tracks 70 municipal tasks most prone to corruption - construction permits, environmental regulation, urban planning - and shows citizens... in real time.
  * why: Number 70 is correct, but SOURCE lists environmental regulation and urban planning, not permits, and ties real time to showing citizens.
* C068 [Partially supported, Minor] loglog 6.9
  * claim: The NSA abandoned the program in 2018: it no longer made sense.
  * evidence: The NSA itself reportedly abandoned the program in 2018, telling the White House it "no longer made sense."
  * why: Node states as flat fact what source hedges with 'reportedly', dropping the attribution qualifier.
* C135 [Partially supported, Minor] loglog 7.5.12
  * claim: Documented audits, custody chains, and counts would starve conspiracies.
  * evidence: the conspiracy theories would have less room to grow
  * why: Source says conspiracies would have less room to grow; node strengthens to starve, an absolute elimination claim.
* C143 [Partially supported, Minor] loglog 7.6.6
  * claim: SIPRI: military transparency builds inter-state trust and prevents waste.
  * evidence: "transparency in military matters is generally considered essential for building trust between states" and "can help prevent wasteful spending."
  * why: Node states absolutes; source hedges with generally considered, essential, and can help prevent.
* C170 [Partially supported, Minor] loglog 7.8.4
  * claim: Citizens prize transparency's idea but dislike disclosures' messy content.
  * evidence: citizens value the *idea* of transparency but may react negatively to the *content* of actual disclosures
  * why: Source hedges with may react negatively; node states the dislike as settled fact.

### Concision flags

* C006 Duplicate of C001: Section 2 heading restates summary mandate; adds only publicly available.
* C084 Duplicate of C020: Repeats work-product-versus-health-records distinction from 4.3.
* C122 Duplicate of C118: Restates build-capacity-not-reduce-information recommendation from 7.4.10.
* C133 Duplicate of C020: Work-product-versus-personal-records analogy repeats 4.3.
* C144 Duplicate of C064: Snowden catastrophe-prediction failure restates 6.5 pattern.
* C174 Duplicate of C134: Election-conspiracy-from-opacity restates opacity-conspiracy link in 7.5.11.
* C176 Duplicate of C016: Latent-availability-deters-misconduct restates availability-over-consumption in 3.4.
* C177 Duplicate of C014: CEOs-need-not-read-every-email restates reviewability claim in 3.2.
* C208 Duplicate of C205: Speed-accountability-as-consequences restates 8.2 with 100% emphasis.
* C215 Duplicate of C012: You-are-CEO closing restates citizen-principal claim in 3.
* C217 Duplicate of C026: Register restates 1766 first-FOI-law claim from 5.2.1.
* C218 Duplicate of C028: Register restates Chydenius Hats-Caps origin from 5.2.3.
* C221 Duplicate of C047: Register restates 20M portal-visit figure from 5.5.2.
* C222 Duplicate of C049: Register restates 60GB/27-year pension find from 5.5.4.
* C223 Duplicate of C032: Register restates OPEN 70-task scope from 5.3.1.
* C224 Duplicate of C036: Register restates corruption-participation link from 5.3.5.
* C225 Duplicate of C052: Register restates 30-business-day cabinet window from 5.6.1.
* C226 Duplicate of C056: Register restates Pol.is mechanism from 5.7.1.
* C227 Duplicate of C193: Register restates Iceland rejected draft from 7.10.4.
* C228 Duplicate of C072: Register restates FREEDOM Act gains and limits from 6.13.
* C229 Duplicate of C075: Register restates GDPR acceleration from 6.16.
* C230 Duplicate of C065: Register restates 2020 illegality rulings from 6.6.
* C231 Duplicate of C081: Register restates Pew 66% figure from 7.1.1.
* C232 Duplicate of C082: Register restates ABC poll history from 7.1.2.
* C233 Duplicate of C088: Register restates IMF-Cambridge friction evidence from 7.2.1.
* C235 Duplicate of C099: Register restates Oman backchannel from 7.3.2.
* C236 Duplicate of C110: Register restates 50-state lobbyist study from 7.4.2.
* C238 Duplicate of C110: Register restates Harden-Kirkland study plus Irish trial figures.
* C239 Duplicate of C125: Register restates Brennan 735-official survey from 7.5.2.
* C240 Duplicate of C129: Register restates doxxing-swatting and AI harassment from 7.5.6.
* C241 Duplicate of C140: Register restates 22-state and Chicago poll figures from 7.6.2-7.6.4.
* C242 Duplicate of C143: Register restates Brennan overclassification and SIPRI trust from 7.6.5-7.6.6.
* C243 Duplicate of C152: Register restates 43-state populism dataset from 7.7.2.
* C244 Duplicate of C157: Register restates Stanford short-termism warning from 7.7.7.
* C245 Duplicate of C167: Register restates Harvard misinformation panel from 7.8.1.
* C246 Duplicate of C194: Register restates OGP 75-country autopsy from 7.10.5.
* C079 Trivia: Roadmap transition announcing ten objections; filler with no substantive content.
* C216 Trivia: Appendix header counting sources; restated header with no substantive content.

### Fix list

* Merge the register recap duplicates C217-C246 (30 entries) plus C006/C084/C122/C133/C144/C174/C176/C177/C208/C215 to pull redundancy well below the 0.15 cap.
* Fix C032: say environmental regulation and urban planning (not 'permits'), and tie 'real time' to showing citizens, matching 5.3.1.
* Fix C068: restore the 'reportedly' hedge for the NSA's 2018 abandonment per 6.9.
* Soften absolute framings to match hedged sources: C135 ('starve' vs 'less room to grow', 7.5.12), C143 (SIPRI 'can help prevent'/'generally considered', 7.6.6), C170 (citizens 'may react negatively', 7.8.4).

## 03_cant_stop_addicted_to_shindig

Verdict: Fail (weighted 0.7516, precision 1.0, must recall 0.8929, redundancy 0.0278)

### Non-present key points

* K11 [Must have, Partial]
  * point: Consistency beats speed: GreedyUntil1Col is fastest (10.5 turns) but only ranks #11 at 58.90% due to high variance and bust rate, while FiftyPercentSurvival at 11.3 turns wins most.
  * loglog: L026, L029
  * why: The core claim and most figures (10.5 turns, #11, 58.90%, variance via sd 5.73 and 7.50 busts, consistency beats speed) are captured by L026 and L029. However the champion FiftyPercentSurvival's 11.3-turn count is not stated anywhere, a dropped number, which per the strict rule caps this Must have at Partial.
* K12 [Must have, Partial]
  * point: Significant first-player advantage: P1 wins 55.59% of games for a +11.18% edge, larger than chess (~5%) or Go (~7%); GreedyUntil1Col shows extreme bias at +31.24%.
  * loglog: L030
  * why: L030 captures the primary statistics (55.59%, +11.18%, +31.24%). The comparative anchors against chess (~5%) and Go (~7%) are absent, so the 'larger than' framing is lost. Dropped comparative numbers make this Must have Partial.
* K15 [Must have, Partial]
  * point: Recommendations: players should use FiftyPercentSurvival and aim for columns 5-9 while avoiding forced activation of 2-3 and 11-12; designers should prioritize playability and use rules to compensate for imbalance, considering handicaps for turn order.
  * loglog: L037
  * why: L037 captures the 50% rule, columns 5-9 target, designer playability priority, and handicaps for turn order. The specific condition to avoid forced activation of columns 2-3 and 11-12 is not stated, a dropped actionable condition, capping this Must have at Partial.

### Concision flags

* C001 Duplicate of C009: Summary recaps body points (flatten odds, dominance, consistency, playability); adds no new claim beyond C009 and peers.

### Fix list

* Restore the dropped champion turn count in K11: state that FiftyPercentSurvival wins in 11.3 turns (loglog L026/L029), so the consistency-beats-speed contrast is complete.
* Restore the comparative anchors in K12: chess (~5%) and Go (~7%) first-player edges (loglog L030), so the 'larger than' framing is not lost.
* Restore the avoided-activation condition in K15: explicitly warn against forcing activation of columns 2-3 and 11-12 (loglog L037).
* Prune C001, which duplicates C009/C013/C026/C031; pure recap with no unique content (redundancy only 0.0278, so low leverage but harmless to compress).

## 04_house_hunting_shenanigans

Verdict: Fail (weighted 0.72, precision 0.9714, must recall 0.8571, redundancy 0.0571)

### Non-supported claims

* C003 [Partially supported, Harmless] loglog 1.1
  * claim: Many houses linger very long; some vanish in 1-2 days.
  * evidence: some that are gone in usually 1-2 days
  * why: Numbers match but source qualifier 'usually' is dropped, making the 1-2 day turnover slightly more absolute.

### Non-present key points

* K07 [Must have, Partial]
  * point: Saturday morning produced nothing, so the author suspected his offer was being kept open as leverage against other buyers and asked for disclosure of the other offer.
  * loglog: L015, L021
  * why: The suspicion of leverage is captured (L015) and the silent Saturday is captured (L021), but the explicit request that the rival offer be disclosed is not shown at this stage, so the actionable request component is dropped.
* K09 [Must have, Partial]
  * point: On Saturday 7pm the seller's realtor's partner C asked N to 'fix' the price drop; meanwhile J's name was replaced by C on the REW site and removed from all four of her listings, which the author read as the seller being angry over losing $20K.
  * loglog: L019, L040
  * why: The listing/name swap and the seller-anger interpretation are present (L019 with L040 cross-link), but C's demand that N 'fix' the price drop is absent, so the episode is narrowed.
* K12 [Must have, Partial]
  * point: On Sunday the author read the forwarded emails between N and the assistant L, which were unprofessional and appeared to scapegoat the assistant; the author noted they had thrown the assistant under the bus.
  * loglog: L023, L024
  * why: The email exchange content is captured, but the author's interpretation that the emails scapegoated the assistant / threw L under the bus is not represented, losing the point's evaluative core.
* K15 [Must have, Partial]
  * point: The closing thesis: realtors have built a system that serves them while buyers and sellers are like pawns in a chess game, and society has given up fighting for change in countless processes from phone holders and laptops to stocks, taxes, cars, and houses.
  * loglog: L031
  * why: The realtor system self-serving and pawn metaphor are captured, but the broader societal argument (giving up fighting for change across phone holders, laptops, stocks, taxes, cars, houses) is missing, so the thesis is narrowed.

### Concision flags

* C033 Duplicate of C017: Recaps tactics already given in C014, C017, C019, C028; no new fact.
* C034 Duplicate of C025: Cross-link marks 6.4/8.3 restatement; debrief adds no new fact.
* C001 Trivia: Top-level summary restates whole narrative with no specifics, expendable at this length.

### Fix list

* K12: restore the author's evaluative core, that the forwarded N-L emails scapegoated L and threw the assistant under the bus (L023/L024); this is the largest single Must-have content gap.
* K15: extend the closing thesis beyond the pawn metaphor to the societal give-up argument (phone holders, laptops, stocks, taxes, cars, houses) per L031, so the conclusion is not narrowed.
* K09: add C's demand that N 'fix' the price drop on Saturday 7pm (L019), keeping the existing REW name-swap and $20K seller-anger reading.
* K07: include the explicit request that the rival offer be disclosed, not just the leverage suspicion and silent Saturday (L015/L021).
* C003: retain the source qualifier 'usually' on the 1-2 day house turnover (1.1) to remove the only Partially supported claim.

## 05_manufacturing_taste

Verdict: Fail (weighted 0.72948, precision 1.0, must recall 0.875, redundancy 0.1026)

### Non-present key points

* K02 [Must have, Partial]
  * point: Forgotten scale: 200 to 500 Viennese composers, 3,400 IMSLP Classical-era composers, several hundred on Wikipedia, fewer than 20 remembered.
  * loglog: L003
  * why: Captures Viennese range, the 3,400 catalogue figure, and fewer than 20, but drops the 'Wikipedia lists several hundred' number. Must-have point with a dropped number is at most Partial.
* K08 [Must have, Partial]
  * point: Model setup: three agent types (producers, consumers, gatekeepers); uncorrelated quality and capital; 1,000 producers, 10,000 consumers, ~2 min, 360+ runs, power analysis.
  * loglog: L017, L018, L019
  * why: Producer/consumer counts, runtime, and run count are intact, but the gatekeeper agent type and the formal power analysis are missing, narrowing the setup description.
* K12 [Must have, Partial]
  * point: Stylized 18th-century Vienna model (300 composers, few patrons, strong word-of-mouth, no recording): distance 0.97, 2.5 percent of canonical composers shared.
  * loglog: L026
  * why: The distance and shared-percent numbers plus composer count survive, but the defining conditions (few wealthy patrons, strong word-of-mouth, no recording) are dropped, narrowing the scope.
* K15 [Must have, Partial]
  * point: Caveats: quality assumed real and stable (debatable); calibration from Salganik teenagers on pop songs over weeks generalizing to 18th-century aristocrats over decades; omits genre formation, critical discourse, tech change, cultural politics.
  * loglog: L034
  * why: The core caveats appear, but the Salganik-teenagers-over-weeks calibration detail and the omitted critical discourse and technological change are dropped, so the caveat set is narrowed.

### Concision flags

* C003 Duplicate of C001: Patronage-versus-merit framing restates the thesis already given.
* C019 Duplicate of C001: Results recap restates thesis and repeats body results below.
* C028 Duplicate of C009: Conclusion restates Floors and Ceilings hypothesis nearly verbatim.
* C034 Duplicate of C029: Final verdict restates Bach-positioning nuance.
* C006 Trivia: Restated section header listing hypotheses detailed below.
* C011 Trivia: Restated header enumerating three mechanisms detailed below.

### Fix list

* Restore the dropped numbers on the four Partial Must-have points: K02 add the 'Wikipedia lists several hundred' count; K12 add the defining conditions (few wealthy patrons, strong word-of-mouth, no recording). These are the cheapest recall gains and alone would lift must_recall to 1.0.
* K08: add the gatekeeper agent type and the formal power analysis to complete the model-setup description.
* K15: re-add the Salganik teenagers-over-weeks calibration detail plus the omitted critical discourse and technological change caveats.
* Optional after recall is fixed: fold the four duplicates (C003/C019 into C001, C028 into C009, C034 into C029) and drop the two section-header trivia restatements (C006, C011) to push redundancy_rate down further, though it is already under the gate.

## 06_valuing_consistency

Verdict: Borderline (weighted 0.76572, precision 1.0, must recall 0.9643, redundancy 0.1)

### Non-present key points

* K09 [Must have, Partial]
  * point: The spectrum of w postures: above 1 amplifier, exactly 1 absolute conformist, between 0 and 1 partial conformist, exactly 0 independent, between -1 and 0 partial contrarian, exactly -1 absolute contrarian. The independent is the only posture that needs no information about the reference, so absolute conformist and absolute contrarian are closer to each other than either is to the independent.
  * loglog: L016, L017
  * why: The full spectrum of postures is enumerated correctly across L016 and L017, but the key insight that the independent is the only posture needing no reference information, and therefore that the two absolutes are closer to each other than to the independent, is absent. A reader would get the taxonomy but miss the structural point, so Partial.
* K15 [Nice to have, Partial]
  * point: Background asides: PS1 notes the author deliberately did not explore cases where the anchor is closer to or farther from the reference, having no meaningful examples. PS2 notes an economist might call the anchor endogenous and the reference exogenous, and that the model is the simplest linear convex combination whose coefficient is not restricted to between 0 and 1, permitting the amplifier region.
  * loglog: L030, L009
  * why: PS1 is fully captured in L030, and the endogenous/exogenous half of PS2 is in L009, but the detail that the coefficient is unconstrained (not restricted to 0 to 1, which is what permits the amplifier region) is dropped. Half the aside survives, so Partial.

### Concision flags

* C012 Duplicate of C001: Body restatement of thesis that hidden anchor drift carries moral weight.
* C022 Duplicate of C017: Recap repeats reference-kind dependence with no new content.
* C033 Duplicate of C031: Restates indistinguishability using a phrase; nothing substantively new.
* C040 Duplicate of C001: Recap restates bad-proxy thesis; no new information.

### Fix list

* K09 (Must have, Partial): restore the missing structural claim that the independent posture is the only one needing no information about the reference, and therefore the two absolutes are closer to each other than to the independent. The L016/L017 spectrum enumeration alone leaves this payoff unstated.
* K15 (Nice to have, Partial): add the dropped half of PS2, that the model coefficient is unconstrained (not restricted to 0 to 1), which is what permits the amplifier region (L009).
* Merge redundancy without losing content: C012 duplicates C001, C022 duplicates C017, C033 duplicates C031, C040 duplicates C001. This can lower redundancy_rate from 0.1 toward 0 with no coverage cost.

## 07_intentionalism

Verdict: Fail (weighted 0.72778, precision 0.9444, must recall 0.9167, redundancy 0.0833)

### Non-supported claims

* C006 [Partially supported, Minor] loglog 3
  * claim: Real situations skip the exact algorithm but share the propose-respond structure.
  * evidence: most real-world situations don't follow the exact Gale-Shapley algorithm
  * why: Source hedges with most; node states it universally, dropping the quantifier.
* C010 [Partially supported, Minor] loglog 4.1
  * claim: Decent differs from best-serving; structure favors proposers without conspiracy.
  * evidence: the outcomes tend to favor whoever's doing the proposing
  * why: Source hedges with tend to; node states structure favors as absolute.

### Non-present key points

* K02 [Must have, Partial]
  * point: In 1962 mathematicians-economists David Gale and Lloyd Shapley worked on creating stable pairings between two groups and proved a stable matching (no unmatched pair preferring each other) always exists.
  * loglog: L004
  * why: Year 1962, names, and the stability definition (no unmatched pair would break) survive, but the dropped condition that they proved a stable matching always exists is a key result. Per the rule on dropped conditions, capped at Partial.
* K03 [Must have, Partial]
  * point: Their deferred acceptance algorithm works by having one side propose in order of preference while the other side accepts or tentatively rejects based on its preferences.
  * loglog: L005
  * why: Deferred acceptance is named, but the actual mechanism (one side proposes down its preference list, the other tentatively accepts/rejects) is never described. A new reader learns the outcome but not how the algorithm runs, so the point is narrowed.

### Concision flags

* C001 Duplicate of C002: Summary restates C002's core hook; adds no new information.
* C030 Duplicate of C019: Closing recap repeats proposer-win thesis and C017 practice chain.
* C031 Duplicate of C016: Cross-link L042 confirms drill repeats the tonight exercise C016.
* C026 Trivia: Meta transition to action plan; low information, maps to no point.

### Fix list

* Restore source hedging in C006 (loglog 3): the node universalizes 'most real-world situations' into 'Real situations', which drops the quantifier and pushes precision below the 0.95 gate.
* Restore source hedging in C010 (loglog 4.1): change the absolute 'structure favors proposers' back to 'outcomes tend to favor whoever is proposing'.
* Add the mechanism to K03 (loglog L005): state that proposers move down their preference list while receivers tentatively accept or reject, so readers learn how deferred acceptance runs, not only its outcome.
* State the existence guarantee in K02 (loglog L004): deferred acceptance always yields a stable matching when one exists, closing the dropped-condition gap.

## 08_empathy_sympathy_compassion_matrix

Verdict: Fail (weighted 0.7511, precision 0.9355, must recall 0.9583, redundancy 0.0323)

### Non-supported claims

* C002 [Partially supported, Minor] loglog 1
  * claim: Cold-control block: modeling, boundary, manipulators, control across components and dark profiles.
  * evidence: in four blocks separated by blank dividers: present in both, in the psychopath only, in the sociopath only, and in neither.
  * why: Source puts modeling/boundary/manipulators in 'present in both' but control in 'psychopath only'; node merges across that block boundary.
* C026 [Partially supported, Minor] loglog 4.6
  * claim: Psychopath is cog alone; sociopath is clamped affect-sympathy minus regulation.
  * evidence: the psychopath is close to the *cognitive-empathy column standing alone*
  * why: Source hedges with 'close to', the node states these mappings as absolute, dropping the approximation qualifier.

### Non-present key points

* K12 [Must have, Partial]
  * point: The empath column is the affective column maxed out and unregulated, which is why it lights up emotion-sharing, contagion, and vividness bias while failing on boundary, scope, and scalability; it is the opposite of the psychopath's coldness but inherits the sociopath's distortions, so it is not the moral ideal.
  * loglog: L031, L009, L013, L014
  * why: The core characterization (maxed, unregulated affect) and its scoring cells survive, but the explicit failure modes (boundary, scope, scalability) and the crucial correction that the empath is not the moral ideal, inheriting the sociopath's distortions, are dropped, so the qualifier/nuance is lost.

### Concision flags

* C026 Duplicate of C007: Recaps dark-block asymmetry already asserted by theme 2; adds only rephrasing, no new data.
* C020 Trivia: Generic section header; scope-to-ideal-types content already carried by C027 and C028.

### Fix list

* Raise faithfulness_precision above 0.95 by resolving C002: honor the four-block divider and stop merging 'control' (psychopath-only) into the 'present in both' modeling/boundary/manipulators block (loglog 1).
* Fix C026: restore the approximation qualifier 'close to' for the psychopath-as-cognition-alone mapping instead of stating it as absolute (loglog 4.6), and merge it into C007 to remove the duplicate.
* Recover the dropped nuance in must-have K12: re-add the empath failure modes (boundary, scope, scalability) and the correction that the empath is not the moral ideal because it inherits the sociopath's distortions (L031, L009, L013, L014).
* Prune C020 (generic header trivia) and merge C026 into C007 to keep redundancy below the 0.15 max after edits.

## 09_not_even_wrong

Verdict: Borderline (weighted 0.7685, precision 1.0, must recall 0.9667, redundancy 0.0909)

### Non-present key points

* K05 [Must have, Partial]
  * point: The 'not even wrong' pattern extends far beyond mathematics: politicians, business leaders, and celebrities use compelling rhetoric that sounds credible but operates outside the boundaries where traditional evaluation is possible.
  * loglog: L006, L018, L019
  * why: Extension beyond math is captured generally as 'leaders' but the specific categories named in the source (politicians, business leaders, celebrities) are narrowed to a generic 'leaders', losing the breadth of the claim.

### Concision flags

* C016 Duplicate of C015: Restates C015's core: aligned factors shape evaluation and override scrutiny.
* C021 Duplicate of C018: Restates C018's core: judge claims independently of investment or opposition.
* C001 Trivia: Recap that restates the five theme claims; adds no new information beyond the body.

### Fix list

* Expand K05 from generic 'leaders' back to the source's named categories (politicians, business leaders, celebrities) at L006/L018/L019 to convert the Partial into Present.
* Demote or drop C001, which recaps C002-C018, to raise uniqueness without losing content.
* Merge duplicate pairs C016/C015 and C021/C018 to remove the two duplicates and lower redundancy below 0.0909.

## 10_parde_begardan_fa

Verdict: Fail (weighted 0.7417, precision 0.9167, must recall 0.9375, redundancy 0.0)

### Non-supported claims

* C006 [Partially supported, Minor] loglog 2
  * claim: با تخفیف سنتور خریدم و با سازی گنده‌تر از خودم کلاس رفتم.
  * evidence: بالاخره برام یه سنتور خریدن... با تخفیف شد ۱۸هزار تومن... سازم از خودم گنده‌تر بود
  * why: Source says family bought it for him; claim states 'I bought', shifting agency. Discount and oversized santur are supported.
* C008 [Partially supported, Harmless] loglog 2.2
  * claim: اول استاد به خانه می‌آمد؛ اتاق پذیرایی سرد بود، حداقل اینطور یادم مانده.
  * evidence: استادم میومد خونه... سنتورم تو اتاق پذیرایی بود... سردتر از بقیه اتاقها. حداقل اینطور تو ذهن من مونده
  * why: Comparative 'colder than other rooms' is flattened to 'cold', though the memory hedge is retained.

### Non-present key points

* K08 [Must have, Partial]
  * point: Recently a santur was built inspired by the harp, with a set of keys allowing any note to be lowered by a quarter or half step in a fraction of a second.
  * loglog: L017, L018
  * why: The harp-inspired keyed santur, the quarter/half-step change, and the fraction-of-a-second speed are all present. But the loglog says the keys make notes 'زیرتر' (higher), reversing the source's 'lowered' direction. This directional inversion is a meaning change on a Must have point, so at most Partial.

### Concision flags

* C002 Trivia: Restated section header; the concrete detail lives in C003-C005 and the summary.
* C006 Trivia: Restated section header; all substance carried by C007-C010.
* C011 Trivia: Restated section header; limitation and tuning cost detailed in C013-C015.
* C016 Trivia: Restated section header; the quarter-tone mechanism is developed in C017-C019.
* C020 Trivia: Restated section header; the return and one-week trip recur concretely in C023-C024.

### Fix list

* Repair claim C006: source says the family bought the santur (بالاخره برام یه سنتور خریدن) but the draft states 'I bought it' (با تخفیف سنتور خریدم), shifting agency. Correcting this one claim raises supported to 23/24 = 0.9583, clearing the 0.95 precision gate.
* Repair claim C008: source says the room was 'colder than the other rooms' (سردتر از بقیه اتاقها) but the draft flattens it to merely 'cold' (سرد بود). Restore the comparative to convert this from Partially supported to supported.
* Fix point K08: the loglog says the harp-inspired keys make notes زیرتر (higher), inverting the source's 'lowered by a quarter or half step' direction. This directional inversion is a meaning change on a Must have point and must be corrected to preserve both recall and factual accuracy.

## 11_finding_a_phone

Verdict: Fail (weighted 0.6561, precision 0.913, must recall 0.7273, redundancy 0.0)

### Non-supported claims

* C016 [Partially supported, Minor] loglog 4.1
  * claim: Declined Pixel over lock-in years and extra charges; O1 gave names, wrong specs.
  * evidence: It gave me a bunch of them with generally wrong specs, but the model names where correct.
  * why: Source says 'generally wrong specs'; node drops the hedge and states specs simply wrong.
* C021 [Partially supported, Minor] loglog 5.1
  * claim: Only Fairphone 4 from 2021 and Moto G Power matched; Edge 40 lacks SD.
  * evidence: it seems like it doesn't have sd card slot!
  * why: Filter result is right, but source hedges Edge 40 SD while node states it as fact.

### Non-present key points

* K01 [Must have, Partial]
  * point: Central thesis: phones are tools, not status symbols. The author wants a device that fits his life, solves his problems, and respects his choices, rather than one that decides what is important for him or forces him to conform to its limitations.
  * loglog: L002
  * why: L002 captures the problem-solving-over-ecosystems thrust but drops the 'tools not status symbols' framing and the explicit demand that the device respect his choices rather than decide what matters for him. Core direction present, defining stance narrowed.
* K03 [Nice to have, Partial]
  * point: After a period with no phone, he bought the Motorola Droid on day one. It was one of the first Android smartphones widely available in the U.S. and became a centerpiece of his life.
  * loglog: L004
  * why: Day-one purchase and life-centerpiece role are captured, but the background qualifier that it was one of the first Android smartphones widely available in the U.S. is absent.
* K05 [Must have, Partial]
  * point: He experimented with many device types (small and large screens, physical keyboards, stylus-equipped phones, smartwatches) but concluded these phones were not built for people like him, but to sell unwanted features, push ads, and lock users into ecosystems he avoided, shifting his focus to functionality over flashiness.
  * loglog: L006, L002, L028
  * why: Smartwatch experimentation and the move away from ecosystems appear, but the substantive indictment that phones are not built for people like him, sell unwanted features, push ads, and lock users in is not stated. Scope of the criticism is largely lost.
* K11 [Must have, Partial]
  * point: Near Black Friday he was fooled by a network provider deal and ordered the latest Google Pixel, but grew anxious about a multi-year lock-in and the remaining payments while knowing the device would limit his choices; extra charges appeared and he declined them and returned to the market.
  * loglog: L017
  * why: L017 captures the Pixel decline, multi-year lock-in, and extra charges, but drops the Black Friday deal context, the sense of being fooled, the remaining-payments anxiety, and the concern that the device would limit his choices.
* K12 [Must have, Partial]
  * point: He asked OpenAI's O1 model for a list of phones from smaller companies meeting his desired features (5G, e-sim, SD card, good battery, waterproof, decent camera). The specs it gave were generally wrong but the model names were correct, so he found specs on gsmarena.com.
  * loglog: L017, L031
  * why: L017 and L031 preserve that O1 returned correct model names but generally wrong specs, and the GSMArena link is implied by L018. The requested feature list (5G, eSIM, SD, battery, waterproof, camera) and the 'smaller companies' scope are not stated.
* K13 [Nice to have, Partial]
  * point: He used gpt-4o-mini to write Python scraping code and claude-3.5 sonnet (after several prompts) to clean the dataframe into the wanted columns; the result mostly works but he has not checked it and assumes several errors.
  * loglog: L018, L019, L020, L032
  * why: The iterative Claude cleaning and the unverified, error-assuming status are captured, but the specific gpt-4o-mini and claude-3.5 sonnet model names are not given.
* K14 [Must have, Partial]
  * point: Filtering for 5G + eSIM + SD card slot left only the Fairphone 4 and Moto G Power (2024); their cameras are not great, screen sizes too big, and the Fairphone 4 seems too old (2021), so he may expand the search. He noticed the Motorola Edge 40 did not appear because it lacks an SD card slot.
  * loglog: L022
  * why: L022 preserves the two-match result, the Fairphone 4's 2021 age, and the Edge 40 exclusion over SD. Dropped are the 2024 model year, the camera and oversized-screen complaints, and the possible broadening of the search.
* K15 [Must have, Partial]
  * point: Update 2025-01-05: he tried the TCL 50 XE NXTPAPER for a couple of weeks. It was weak on performance, ran uncomfortably hot on a video call, and its screen was much worse, almost unreadable in direct or lamp light compared with regular screens; the camera was average; the paper and ink color modes were good ideas but poorly implemented with many restrictions, and it was not true e-ink as he had expected. He returned it and next plans to try the Motorola G85, having wanted the more waterproof IP68 G75 but being unable to find it in stores; the G85 is only water repellent and Motorola cameras are generally not expected to be good.
  * loglog: L023, L024
  * why: The durability verdict, heat on calls, unreadable screen, paper/ink mode failure, return, G85 plan, and unavailable IP68 G75 are captured. Missing are the 2025-01-05 date, the TCL 50 XE NXTPAPER model name, the two-week trial, the average camera, and the note that Motorola cameras are generally not expected to be good.

### Concision flags

* C002 Trivia: Restated section header; condenses C003 and C005 before the detail lines.
* C006 Trivia: Restated section header summarizing C007 and C008 without new information.
* C010 Trivia: Restated section header recapping C011 through C014.
* C015 Trivia: Restated section header summarizing C016 through C019.
* C020 Trivia: Restated section header recapping C021 through C023.

### Fix list

* Raise must-have recall: K01, K05, K11, K12, K14, K15 are all Partial; each must state its defining content, not just the headline. Prioritize K01 (tools-not-status-symbols thesis), K05 (phones not built for people like him, sell unwanted features, push ads, lock in ecosystems), and K11 (Black Friday deal, being fooled, remaining-payments anxiety, device limiting his choices).
* K12/K13: add the concrete model names and requested feature set (gpt-4o-mini scraping code, claude-3.5 sonnet cleaning, 5G/eSIM/SD/battery/waterproof/camera, smaller companies) to move Partial to Present.
* K14/K15: restore dropped specifics (Moto G Power 2024 model year, camera and oversized-screen complaints, TCL 50 XE NXTPAPER name, 2025-01-05 date, two-week trial, average camera, G75 IP68 waterproofness, Motorola cameras generally weak) to clear the recall gate.
* C016 and C021: preserve source hedges ('generally wrong specs', Edge 40 SD uncertainty) so the claims do not overstate; this lifts faithfulness_precision above 0.95.
* C002/C006/C010/C015/C020: drop the five restated theme-header bullets to cut trivia_rate 0.2174 without any coverage loss.

## 12_lets_talk_privacy

Verdict: Borderline (weighted 0.7605, precision 0.9714, must recall 0.9583, redundancy 0.0571)

### Non-supported claims

* C001 [Partially supported, Minor] loglog 0
  * claim: Encrypted chats still trust providers; only client-held keys minimize that trust.
  * evidence: With Signal using recovery keys, the attack surface is much smaller
  * why: Source ranks Signal's client-controlled keys as smaller attack surface but never asserts exclusivity of 'only client-held keys', so scope is overstated.

### Non-present key points

* K11 [Must have, Partial]
  * point: Signal's approach: by default history is stored only on your device and deleted from servers after delivery. Device switching offers three options: manual local backup protected by a 30-digit passphrase, direct device-to-device local transfer, or Secure Backups encrypted with a 64-character recovery key Signal never sees.
  * loglog: L019, L020
  * why: L019 captures all three switching options with the 30-digit and 64-character figures, and L020 notes physical-presence constraints. However the default condition that history is stored only on the device and deleted from servers after delivery is not stated, a dropped scope qualifier for a Must have point.

### Concision flags

* C023 Duplicate of C031: Restates 8.3 breach numbers; cross-link L043 marks 6.2 as restatement.
* C033 Duplicate of C026: Restates 7.2 three-model comparison; cross-link L045 confirms restatement.
* C003 Trivia: Setup context about Omid; maps to no must/nice point and carries low information value.

### Fix list

* Restore the dropped scope qualifier in K11: state that history is stored only on your device and deleted from servers after delivery, in addition to the three device-switching options (L019/L020).
* Narrow C001 to match the source: Signal's client-controlled keys yield a smaller attack surface, rather than asserting that only client-held keys minimize provider trust (source quote: 'With Signal using recovery keys, the attack surface is much smaller').
* Merge duplicate pair C023/C031 and C033/C026 to lift the unique-claim ratio, and drop the trivia claim C003.
* If any slack remains after K11, spend it on the C001 nuance rather than new material, since redundancy headroom (0.0571 vs 0.15) is still ample and coverage is the binding constraint.

