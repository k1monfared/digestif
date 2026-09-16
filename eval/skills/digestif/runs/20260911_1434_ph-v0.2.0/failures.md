# Failure report: 20260911_1434_ph-v0.2.0

Generated: 2026-09-16 by `eval/lib/failures.py`.

## Summary

* claims judged: 493
* non-supported claims: 23 (partial 21, unverifiable 1, contradicted 1, critical 1)
* non-present key points: 57
* duplicate labels: 29, trivia labels: 29

Per sample detail follows. Every entry cites its claim or point id, the deciding evidence, and the judge's reasoning so a human can audit or overturn it.

## 01_what_is_mathematics

Verdict: Fail (weighted 0.6855, precision 0.9231, must recall 0.8214, redundancy 0.0615)

### Non-supported claims

* C001 [Partially supported, Minor] loglog 0
  * claim: Mathematics was never the production of proofs but the judgment of which patterns deserve proving.
  * evidence: mathematics was never the production of theorems. It was a process of thinking, and the process was the product. ... It was always both: finding patterns, and proving them.
  * why: Source says the process of thinking was the product and math was always both finding and proving; node narrows the product to judgment alone.
* C005 [Partially supported, Harmless] loglog 2
  * claim: In 2026 AI produced publication-quality proofs of novel problems for hundreds of dollars.
  * evidence: solved seven of ten unpublished problems to publication quality, for ten to a thousand dollars of compute each ... for a few hundred to a few thousand dollars of compute
  * why: Source gives ten to a thousand dollars (or a few hundred to a few thousand); 'hundreds' narrows the band but matches the looser quote.
* C022 [Partially supported, Minor] loglog 4.2
  * claim: Cognitive offloading and confident AI tone worsen the illusion of explanatory depth.
  * evidence: Cognitive offloading is the tendency to delegate mental effort ... AI ... produces plausible explanations in a confident tone, so both student and instructor can mistake the output for the learning.
  * why: Source defines offloading and the illusion separately; it attributes the mistaken learning to confident AI tone, not to offloading worsening the illusion.
* C042 [Partially supported, Minor] loglog 6.6
  * claim: Compute budgets and self-solving applications will set the agenda; the shift takes decades.
  * evidence: I'm not sure about timing, it might take years, probably decades, not months though.
  * why: Source hedges timing as 'probably decades' and 'not sure'; node states 'takes decades' as fact, dropping the hedge.
* C054 [Unverifiable, Minor] loglog 7.4
  * claim: Like the unheard falling tree, unexamined consensus leaves meaning unresolved.
  * evidence: Somewhat relatedly, this also reminds me of the the thought experiment of a tree falling in a jungle
  * why: Source only links the tree thought experiment without stating what it is meant to show.

### Non-present key points

* K01 [Nice to have, Partial]
  * point: Occasion and interlocutors: responds to a viral LinkedIn complaint from a math professor comparing research to grading a clever student willing to lie, and engages Terence Tao's ICM 2026 lecture plus Amir Moradifam's essay, agreeing but pushing one step further.
  * loglog: L005, L016, L030
  * why: L005 captures the professor's viral post and L016/L030 reference Tao's hypothesis, but the loglog never names Tao's ICM 2026 lecture or Amir Moradifam's essay, so the interlocutors are only half present.
* K03 [Must have, Partial]
  * point: The 2026 results that broke the old answer: First Proof's test had four systems solve 7 of 10 unpublished problems to publication quality at $10-$1000 compute each, with problem choice not automated; an AI produced a machine-checked Lean proof of Erdos #728; and an OpenAI model disproved Erdos's 1946 planar unit distance conjecture with at least n^(1+epsilon) unit distances.
  * loglog: L006, L007, L008
  * why: L007 and L008 retain the 7-of-10 result, the Erdos #728 Lean proof, and the 1946 unit-distance disproof, but the per-problem $10-$1000 compute figure, the 'First Proof' name, and the n^(1+epsilon) construction are dropped. Must have point with dropped numbers, so Partial.
* K05 [Must have, Partial]
  * point: Verification is human work too and is being automated; the Voevodsky case (Fields Medal 2002, Deligne finding a wrong key lemma, another main theorem false for years unnoticed) shows human verification is unreliable, so AI verification at a comparable error rate looks like business as usual; the AI error rate is assumed not measured and machine volume compounds mistakes.
  * loglog: L016, L017, L018, L019, L020
  * why: L017-L020 keep the Deligne wrong-lemma case, the false-for-years theorem, the business-as-usual inference, and the assumed-not-measured caveat, but the Fields Medal 2002 detail is dropped. Must have with a dropped number, so Partial.
* K08 [Must have, Partial]
  * point: Tao's exposition argument: AI-polished proofs are almost too flawless, dwell on trivialities, rush past novel parts, fail to connect to prior literature, and remove the friction that makes readers slow down and learn; even human mistakes can helpfully mark where the work is, as in Thurston's point that success is measured by whether work helps people understand and think more clearly.
  * loglog: L027, L028
  * why: L027 keeps the trivia, rushing, and lost-friction elements and L028 the Thurston point, but the failure to connect to prior literature and the helpful-role-of-human-mistakes element are dropped, narrowing the argument.
* K09 [Must have, Partial]
  * point: Tao's conditional Working Hypothesis and pipeline: via Goodhart's law, historically correlated community goals can diverge under AI optimization; the goal 'solve as many unsolved problems as possible' must be refined with verification, exposition, community acceptance, and canonicalization, with digestion now the bottleneck; on erdosproblems.com many likely-correct AI proofs await human verification; recommendations include normalizing responsible disclosure, reducing emphasis on generation and being first, increasing emphasis on exposition, publication, and canonicalization, endorsing the Leiden Declaration, and requiring authors to demonstrate an expert-level talk on the result.
  * loglog: L030, L031, L032, L033, L034, L035
  * why: L032-L035 keep Goodhart's law, the four refined stages, digestion as bottleneck, and disclosure/first-past-posting/clear-talk rules, but the erdosproblems.com backlog and the Leiden Declaration endorsement are absent, so the recommendation set is incomplete.
* K10 [Must have, Partial]
  * point: Moradifam's research-side account and epistemology: Davies and AlphaTensor show ML as an intuition pump, with AI proposing and humans formalizing and digesting; accepted-but-opaque results (four-color theorem, classification of finite simple groups) are used as tools despite no single person holding the proof, and understanding shifts from constructive to hermeneutic; his thesis is that as routine tasks are automated, problem framing, judgment, and taste become more visible and valuable.
  * loglog: L014, L015
  * why: L014 and L015 preserve the intuition-pump examples and the constructive-to-hermeneutic shift, but the four-color theorem and finite-simple-groups examples and the framing/judgment/taste thesis are dropped, so scope is narrowed.

### Concision flags

* C009 Duplicate of C008: Conjecture generators only restate that machines propose, never decide importance.
* C010 Duplicate of C001: Finding-as-real-thing restates the summary thesis; proving/chore split already in C001.
* C020 Duplicate of C001: Section 4 opener repeats the math-is-not-proof-production thesis already in C001.
* C055 Duplicate of C001: Section 8 recap restates the summary thesis; automation nuance appears elsewhere.

### Fix list

* Raise must-have recall by restoring the dropped numbers and named sources in K03 (the $10-$1000 per-problem compute figure, the 'First Proof' name, and the n^(1+epsilon) unit-distance construction) via L006-L008, since these are Must have with concrete facts the loglog flattens.
* Complete K09 by adding the erdosproblems.com likely-correct AI proof backlog and the Leiden Declaration endorsement to L032-L035, and complete K05 by restoring the Fields Medal 2002 detail (L017-L020) so both Must have nodes stop being Partial.
* Fix the faithfulness partials that weigh on Must have points: C022 (4.2) currently asserts offloading worsens the illusion of explanatory depth where the source attributes the mistake to confident AI tone, and C042 (6.6) states 'takes decades' as fact while the source hedges 'probably decades, not sure'.
* Tighten the remaining interpretation partials to match source hedging: C001 (0) narrows math's product to judgment though the source says the process of thinking was the product and math was 'always both', and C054 (7.4) asserts what the falling-tree analogy means when the source only links the thought experiment.
* Merge the safe duplicates C009/C010/C020/C055 into their bases to keep redundancy comfortably below the max as the other fixes add restored detail.

## 02_case_for_transparent_government

Verdict: Fail (weighted 0.67704, precision 0.9506, must recall 0.7667, redundancy 0.0494)

### Non-supported claims

* C021 [Partially supported, Minor] loglog 5.3
  * claim: Estonia's X-Road links thousands of services with signed, logged, breach-free exchange.
  * evidence: no major security breaches in over 20 years
  * why: Source says no major breaches; 'breach-free' drops the qualifier 'major', overstating the claim.
* C034 [Partially supported, Minor] loglog 6.4
  * claim: Secret courts and committees failed because secrecy captured the overseers themselves.
  * evidence: They failed because they operated inside the secrecy structure ... Oversight that is itself secret is oversight that can be captured, co-opted, or simply worn down by institutional pressure.
  * why: SOURCE hedges capture with 'can be ... or simply worn down' while node asserts capture as the fact.
* C041 [Contradicted, Critical] loglog 7.1.2
  * claim: Pew and Roper surveys record citizen-data fears and six decades of opinion.
  * evidence: Historical overview of American public opinion on government transparency from 1950s to present
  * why: Source dates the Roper overview 1950s to present, roughly seven decades, not six. Numeric drift fails.
* C045 [Partially supported, Minor] loglog 7.3
  * claim: Objection: diplomacy needs secrecy, from backchannels to Cold War hotlines.
  * evidence: Cold War backchannels between the US and Soviet Union helped manage rivalry and avoid direct confrontation.
  * why: Backchannels supported, but source says Cold War backchannels, not hotlines, a substituted term.

### Non-present key points

* K07 [Must have, Partial]
  * point: Estonia 2001: X-Road connects 929+ institutions, 1,887 information systems, 3,000+ digital services; every transaction timestamped, cryptographically signed, and logged; ranks 2nd in UN E-Government Development Index with no major breaches in 20+ years, proving feasibility and that will, not technology, is the bottleneck.
  * loglog: L022, L023
  * why: The core mechanism (signed, logged, breach-free exchange) survives, but the point's defining scale numbers (929 institutions, 1,887 systems, 3,000 services), the 2001 date, the 2nd-place EGDI ranking, and the 20-year no-breach figure are all collapsed to 'thousands.' Losing the concrete scale weakens the stated feasibility argument.
* K08 [Must have, Partial]
  * point: Brazil 2004: Transparency Portal publishes all federal spending (contracts, transfers, salaries, travel, credit card) with 20+ million accesses/year; Transparency Card sends real-time political spending notifications (430,000+ cards, 20+ million notifications); journalists using the Access to Information Law uncovered 60GB of pension data going back 27 years.
  * loglog: L024, L025
  * why: The portal's 20 million yearly visits and the 27-year pension disclosure are captured, but the 2004 date, the entire Transparency Card component (430,000 cards, 20 million notifications), and the 60GB figure are absent, substantially narrowing the point.
* K10 [Must have, Partial]
  * point: Recurring pattern: secret programs are later revealed as illegal or built on lies, and internal oversight failed because it operated inside the same secrecy bubble. Examples: Pentagon Papers 1971 (Vietnam unwinnable), COINTELPRO 1971 (illegal surveillance of civil rights leaders), Snowden 2013 (NSA bulk metadata, PRISM, surveilling foreign leaders).
  * loglog: L030, L031, L032, L035
  * why: The pattern claim and the three named cases (Pentagon Papers, COINTELPRO, Snowden), plus the failed-oversight mechanism (L035), are present. However the identifying dates (1971, 1971, 2013) and the substantive details of each case (Vietnam deception, civil-rights surveillance, PRISM and foreign-leader targeting) are dropped, narrowing the evidence.
* K11 [Must have, Partial]
  * point: Snowden aftermath: Sept 2020 Ninth Circuit ruled NSA bulk phone record collection illegal and possibly unconstitutional under FISA; Stone found no evidence it stopped attacks; NSA abandoned it in 2018; USA FREEDOM Act 2015 reined in spying; tech transparency reporting, default HTTPS, and EU GDPR followed; operational harm uncertain but legality and oversight failures are not.
  * loglog: L033, L036, L037
  * why: The legality ruling, the no-attacks-stopped finding, the FREEDOM Act and downstream reforms (transparency reports, HTTPS, GDPR), and the conceded uncertainty about operational harm (L037) are all present. Lost are the 2020 Ninth Circuit and 2018/2015 dates, the FISA relevance requirement, and Stone's name, so the point is partial.
* K12 [Must have, Partial]
  * point: Privacy and harassment objections: privacy fears (66% concerned about government data collection; 86% opposed to online public records) concern citizen data, not visible government decisions, a direction confusion; official threats are real (Brennan Center 2024, 735 officials: 38% threatened, 34% know a resignation, up from 22% in 2023), so publish decisions while protecting personal data; much harassment stems from opaque processes.
  * loglog: L041, L042, L054, L055, L056
  * why: The direction-confusion rebuttal, the citizen-data polls (L042), and the threat statistic (38% threatened per L055) plus the 'a third know resignations' figure are present. The specific poll numbers 66% and 86%, the Brennan Center 2024 attribution, 735 respondents, and the 22%-to-34% rise are dropped, so precision is lost.
* K13 [Must have, Partial]
  * point: Secrecy-based objections rebutted: gridlock confuses speed with documentation (NZ shows transparency documents at current speed); diplomacy (JCPOA Oman backchannel, Camp David, Cold War) and markets (Fed FOMC minutes three weeks, transcripts five years; TTIP harmed by secrecy) justify only temporary operational secrecy with time-delayed release (30-90 days), never permanent secrecy; national security is overused and the burden of proof should be reversed.
  * loglog: L044, L046, L047, L059, L060, L061
  * why: The gridlock rebuttal (L044), diplomacy and national-security objections with the 30-90 day temporary-secrecy rule (L047), and the burden-flip recommendation (L060) are preserved. The specific supporting examples (Oman JCPOA, Camp David, FOMC three-week/five-year delays, TTIP) are dropped, thinning the argument.
* K14 [Must have, Partial]
  * point: Empirical misuse concerns acknowledged then rebutted: Harden and Kirkland find open meetings bring more lobbying and no better opinion correlation; 2024 Irish experiment finds lobbying transparency does not raise trust; Kyle and Gultchin (43 countries, 1990-2018) find populists 4x more likely to damage democracy and countries falling ~5 CPI places; misinformation reduces perceived transparency. Answer: build citizen capacity and better transparency, not less transparency.
  * loglog: L051, L052, L053, L063, L064, L067, L068
  * why: The Harden-Kirkland finding, the Irish experiment, the populist-damage rebuttal, and the misinformation/perceived-transparency point are all present with the citizen-capacity prescription (L052). The quantified findings (43 countries, 1990-2018, 4x, ~5 CPI places) are absent, so the empirical force is diluted.

### Concision flags

* C009 Duplicate of C002: Repeats corporate-secrecy-would-fail analogy across branches.
* C010 Duplicate of C008: Restates availability matters, not consumption.
* C060 Duplicate of C046: Repeats temporary-secrecy-then-publish recommendation in security branch.
* C071 Duplicate of C046: Repeats delay-then-publish recommendation in markets branch.
* C016 Trivia: Source list only, restates parent fact with low argument value.
* C017 Trivia: Citation index restating the Nordic comparison, little new content.
* C020 Trivia: Source list only, repeats OPEN fact without new argument.
* C022 Trivia: Source list only, low value beyond parent X-Road claim.
* C024 Trivia: Source list only, restates parent Brazil facts.
* C027 Trivia: Source list only, low value beyond parent vTaiwan claim.
* C033 Trivia: Source list only, repeats bulk-collection outcome.
* C038 Trivia: Section intro framing, a restated header with no argument.
* C044 Trivia: Source list only, low value beyond parent deliberation point.
* C048 Trivia: Source list only, restates backchannel dilemma.
* C052 Trivia: Source list only, low value beyond lobbyist argument.
* C056 Trivia: Source list only, repeats threat and protection facts.
* C061 Trivia: Source list only, restates overclassification point.
* C065 Trivia: Source list only, low value beyond populism claim.
* C069 Trivia: Source list only, restates perceived-opacity finding.
* C075 Trivia: Source list only, low value beyond resistance claim.
* C076 Trivia: Status note requesting feedback, procedural not argumentative.

### Fix list

* Resolve Critical contradicted claim C041: source dates the Roper overview 1950s to present (roughly seven decades), so correct 'six decades' to 'seven decades' (or '1950s to present') at loglog 7.1.2.
* Raise must_recall by restoring stripped concrete evidence in the seven Partial Must-have points, highest leverage first: K07 (929 institutions, 1,887 systems, 3,000+ services, 2001, 2nd EGDI, 20+ years no major breach), K08 (2004 date, Transparency Card 430,000+ cards / 20M+ notifications, 60GB), K11 (Sept 2020 Ninth Circuit, FISA relevance, Stone, 2018/2015 dates), K12 (66%, 86%, Brennan Center 2024, 735 officials, 22%-to-38% rise), K13 (Oman JCPOA, Camp David, FOMC 3-week/5-year, TTIP).
* Soften overstatements on Minor Partials: C021 restore 'major' qualifier ('breach-free' becomes 'no major breaches'), C034 hedge capture ('can be captured or worn down' rather than asserted fact), C045 replace 'hotlines' with 'backchannels'.
* Trim trivia (trivia_rate 0.2099, C016-C075 source-list evidence nodes are not gated but folding them into parents raises signal density without lowering recall).

## 03_cant_stop_addicted_to_shindig

Verdict: Fail (weighted 0.63844, precision 0.9688, must recall 0.6429, redundancy 0.0312)

### Non-supported claims

* C021 [Partially supported, Minor] loglog 5.1
  * claim: 38 strategy families tested across single-player and head-to-head simulations.
  * evidence: I tested 38 strategies across 14 different strategic families
  * why: Number 38 is right for strategies, but source reports 14 families, not 38, mislabeling the count.

### Non-present key points

* K02 [Must have, Partial]
  * point: Game rules: roll four dice, pair them to move markers on columns 2 through 12, need three completed columns to win; column lengths are 3,5,7,9,11,13,11,9,7,5,3.
  * loglog: L003, L004
  * why: Rules captured but exact column lengths (3,5,7,9,11,13,11,9,7,5,3) are not enumerated, only the 3-to-13 range. Dropped numbers make this Partial.
* K04 [Must have, Partial]
  * point: Two-dice baseline: sum 7 is most likely at 16.67%, exactly 6 times more likely than sum 2 at 2.78%.
  * loglog: L008
  * why: 16.67% and the 6x ratio are present, but the 2.78% baseline probability for sum 2 is dropped. Dropped number caps at Partial.
* K06 [Must have, Partial]
  * point: Expected rolls to complete a column = length / probability; column 2 needs about 22.73 rolls while column 7 needs about 20.18, so 7 is slightly faster despite being 4x longer.
  * loglog: L014
  * why: The qualitative finding is retained, but the exact expected values 22.73 and 20.18 are dropped. Dropped numbers make this Partial.
* K07 [Must have, Partial]
  * point: Column combinations matter: {6,7,8} succeeds 92.0% of the time versus 43.8% for {2,3,12}; all 165 three-column combinations were analyzed, with 37 rated excellent (>=85% success) and a median success of 79.6%.
  * loglog: L015, L016
  * why: 92%, 43.8%, 37 and 79.6% captured, but the total count of 165 combinations and the >=85% excellent threshold are dropped. Dropped numbers cap at Partial.
* K09 [Must have, Partial]
  * point: Stopping heuristic: keep rolling if (P_success x Q) > (P_bust x U), where Q is expected markers advanced and U is unsaved progress; example on {6,7,8} says roll (1.32 > 0.4) and on {2,3,12} says stop (1.12 > 0.46).
  * loglog: L017, L018
  * why: The heuristic's conceptual form and the directional decisions survive, but the explicit inequality and the numeric values 1.32/0.4 and 1.12/0.46 are dropped. Partial.
* K10 [Must have, Partial]
  * point: Tournament of 38 strategies across 2,500 head-to-head games each (3.6M total games) found FiftyPercentSurvival the champion at 69.84% win rate, and probabilistic strategies dominate the top rankings.
  * loglog: L021, L022, L024
  * why: 38 strategies, 3.6M games and 69.84% all present, but the 2,500 games per head-to-head pairing is dropped. Dropped number makes this Partial.
* K11 [Must have, Partial]
  * point: Consistency beats speed: GreedyUntil1Col is fastest (10.5 turns) but only ranks #11 at 58.90% due to high variance and bust rate, while FiftyPercentSurvival at 11.3 turns wins most.
  * loglog: L023, L024, L025
  * why: The core contrast and 10.5-turn speed are present, but the #11 ranking, 58.90% win rate and FiftyPercentSurvival's 11.3 turns are dropped. Partial.
* K12 [Must have, Partial]
  * point: Significant first-player advantage: P1 wins 55.59% of games for a +11.18% edge, larger than chess (~5%) or Go (~7%); GreedyUntil1Col shows extreme bias at +31.24%.
  * loglog: L026
  * why: 55.59%, 11.18% and the chess/Go comparison are retained, but the GreedyUntil1Col +31.24% extreme-bias figure is dropped. Partial.
* K13 [Must have, Partial]
  * point: Balance analysis: single-column completion times deviate at most +/-13.6% from 20 rolls, an optimal board one step from current reaches +/-3.09%, and a 20-step board reaches +/-2.17%.
  * loglog: L028, L029
  * why: The 13.6% deviation and the one-step improvement idea are present, but the explicit +/-3.09% and +/-2.17% figures are dropped. Partial.
* K15 [Must have, Partial]
  * point: Recommendations: players should use FiftyPercentSurvival and aim for columns 5-9 while avoiding forced activation of 2-3 and 11-12; designers should prioritize playability and use rules to compensate for imbalance, considering handicaps for turn order.
  * loglog: L031, L032
  * why: The 5-9 target, edge avoidance and playability advice are present, but the explicit FiftyPercentSurvival player recommendation and the turn-order handicap suggestion are not captured. Partial.

### Concision flags

* C024 Duplicate of C020: Restates C020 consistency-over-speed; greedy loss already given in C022.
* C032 Trivia: Reproducibility meta-note maps to no analysis point, low value at this length.

### Fix list

* Recover the 10 Partial must-haves by restoring dropped numbers, not prose: K02 column lengths (3,5,7,9,11,13,11,9,7,5,3), K04 sum-2 baseline 2.78%, K06 expected rolls 22.73 vs 20.18, K07 the 165 total combinations and >=85% excellent threshold, K09 the inequality and values 1.32/0.4 vs 1.12/0.46.
* Finish the remaining dropped figures on K10 (2,500 games per head-to-head), K11 (#11 rank, 58.90%, 11.3 turns), K12 (GreedyUntil1Col +31.24%), K13 (+/-3.09% and +/-2.17%), and K15 (explicit FiftyPercentSurvival player pick and turn-order handicap).
* Correct C021 to say 14 strategic families tested, not 38 families, to clear the sole Partially supported claim (0.9688 -> 1.0 faithfulness).
* Optionally apply the prune list (merge C024 into C020, trim cross-links L035-L038, move C032 to appendix) after coverage numbers are restored.

## 04_house_hunting_shenanigans

Verdict: Fail (weighted 0.7, precision 0.9643, must recall 0.7857, redundancy 0.0)

### Non-supported claims

* C003 [Partially supported, Minor] loglog 1.1
  * claim: Some houses linger unsold for months; others vanish within one or two days.
  * evidence: stay for a loooooong time and there are some that are gone in usually 1-2 days
  * why: The 1-2 days matches, but source says only a vague 'loooooong time', not the unit 'months'.

### Non-present key points

* K03 [Must have, Partial]
  * point: By Thursday 6pm the offer was not accepted and the sellers were moving forward with other offers.
  * loglog: L005
  * why: The failure is captured, but the Thursday 6pm timing and the detail that sellers were advancing other offers are dropped. The point is mentioned only as a flat 'fails', so a reader loses the resolution detail.
* K07 [Must have, Partial]
  * point: Saturday morning produced nothing, so the author suspected his offer was being kept open as leverage against other buyers and asked for disclosure of the other offer.
  * loglog: L012
  * why: The suspicion that his offer was leverage is captured, but the explicit request for disclosure of the other offer is not present in the Saturday mapping (the written-disclosure rule appears later at L022 as a Monday rule). A key action is lost.
* K09 [Must have, Partial]
  * point: On Saturday 7pm the seller's realtor's partner C asked N to 'fix' the price drop; meanwhile J's name was replaced by C on the REW site and removed from all four of her listings, which the author read as the seller being angry over losing $20K.
  * loglog: L015
  * why: The 'fix the drop' request and the listing switch are captured, but the number of affected listings ('all four') is dropped and the author's interpretation that the seller was angry over the 20K loss is absent. Dropped number forces Partial.
* K11 [Must have, Missing]
  * point: On Sunday 8am the author instructed N to resubmit at 10K below the asking price, remove every favorable term, and give until 11am, as his best and final offer, rejecting N's push to meet or exceed the counteroffer.
  * loglog: none
  * why: The Sunday section (L017-L020) covers the email spat and a stance of in-person presentation with no open offer, but nowhere records the 10K-below resubmit, the removal of every favorable term, the 11am deadline, or the best-and-final framing. The operative numbers and terms are entirely absent.
* K12 [Must have, Partial]
  * point: On Sunday the author read the forwarded emails between N and the assistant L, which were unprofessional and appeared to scapegoat the assistant; the author noted they had thrown the assistant under the bus.
  * loglog: L018, L019
  * why: The existence of the Sunday email exchange is captured through L018/L019 and the conflict note L034, but the framing is inverted: LOGLOG records L calling the deadline unprofessional rather than the author reading the N-L emails as unprofessional and scapegoating L. The interpretation is lost.

### Concision flags

* C002 Trivia: Restated section header, market content fully carried by C003 and C004.
* C005 Trivia: Restated header previewing Friday section, detail held in C006-C009.
* C010 Trivia: Restated header summarizing Saturday duel covered by C013 and C015.
* C016 Trivia: Restated header for Sunday spat, detail held in C017-C019.
* C020 Trivia: Restated header, aftermath content carried by C021-C023.
* C024 Trivia: Restated header, reflections carried by C025-C028.

### Fix list

* Restore Must-have K11 (Sunday best-and-final: resubmit 10K below asking, strip all favorable terms, 11am deadline, reject N's counter): entirely absent from L017-L020, cite K11
* Repair Must-have K03 partial: add the Thursday 6pm timing and that sellers moved to other offers, currently flattened to 'offer fails' at L005
* Repair Must-have K07 partial: add the explicit request to disclose the other offer on Saturday, currently only the leverage suspicion at L012 (disclosure rule mis-sequenced to L022)
* Repair Must-have K09 partial: add 'all four' listings and the author's anger-over-20K-loss reading at L015
* Repair Must-have K12 partial: invert the framing so the author reads the N-L emails as unprofessional and scapegoating L, not merely L calling the deadline unprofessional at L018/L019

## 05_manufacturing_taste

Verdict: Fail (weighted 0.71472, precision 0.9412, must recall 0.875, redundancy 0.0588)

### Non-supported claims

* C041 [Partially supported, Minor] loglog 7.1
  * claim: Quality may be partly constituted socially, making decomposition ill-posed.
  * evidence: then the whole decomposition may be ill-posed
  * why: Source hedges ill-posed with 'may'; node states the consequence as fact, dropping the hedge.
* C048 [Partially supported, Minor] loglog 8.4
  * claim: Leipzig job decided it; 20 to 50 equals forgotten for missing that post.
  * evidence: there were probably 20 to 50 of his contemporaries who were equally great
  * why: Range 20 to 50 matches, but source hedges with 'probably'; node states it as fact.
* C051 [Partially supported, Minor] loglog 8.7
  * claim: Future canons will reward distribution and algorithms over musical merit.
  * evidence: if the mechanisms in this simulation are right, then whoever survives into the canon of the 2000s will have more to do with who had the best distribution deals and the most favorable algorithms than with who made the best music.
  * why: Source conditions this on the mechanisms being right; node drops the conditional and states it as fact.

### Non-present key points

* K06 [Must have, Partial]
  * point: Mere exposure: Zajonc 1968, Bornstein 1989 meta-analysis of 208 experiments, r=0.26; peaks at moderate exposure and reverses with overexposure.
  * loglog: L012
  * why: Years and effect size r=0.26 survive, but the 208-experiment meta-analysis count is dropped and the inverted-U qualifier (peaks at moderate exposure, reverses with overexposure) is entirely absent, which materially reduces the claim's precision.
* K07 [Must have, Partial]
  * point: Salganik MusicLab 2006: 14,341 participants judged 48 unknown songs; social-count vs independent conditions; same song ranked 1st or 40th from random early downloads.
  * loglog: L014
  * why: The striking rank instability is kept, but the sample size (14,341 participants), the 48-song set, and the presence of an independent-judgment control condition are all dropped, narrowing the study's scope.
* K12 [Must have, Partial]
  * point: 18th-century Vienna stylized model (300 composers, few wealthy patrons, strong word-of-mouth, no recording): counterfactual distance 0.97 near maximum, only 2.5% of canonical composers shared.
  * loglog: L030
  * why: The head-line results (300 composers, 0.97 distance, 2.5 percent overlap) are exact, but the scenario's defining conditions, few wealthy patrons, strong word-of-mouth, and especially the 'no recording' negation, are dropped, so a new reader cannot tell what makes the Vienna setup distinct or why contingency is near maximal.
* K13 [Must have, Partial]
  * point: Robustness: varying every parameter by ±50%, the most important factor is how steeply money converts into attention (convex makes rich get richer and quality barely matter; concave leaves room for quality).
  * loglog: L033, L034
  * why: The ±50% sweep and the primacy of capital-to-exposure steepness are present, but the convex-vs-concave distinction, which is the mechanism explaining why steepness matters, is dropped.

### Concision flags

* C034 Duplicate of C008: Verdict restates Story 3 mechanism already in C008; only wins is new.
* C039 Duplicate of C022: Restates popularity-proxy point already made by C022 per cross-link.
* C048 Duplicate of C025: Restates single-post-decides-fame pattern already in C025 per cross-link.
* C035 Trivia: Pure filler transition announcing below; no informational content.
* C040 Trivia: Generic restated header; adds no specifics beyond section title.

### Fix list

* Raise must_recall above 0.9 by completing the four Partial Must-haves: restore K06 inverted-U qualifier and 208-experiment meta-analysis count, K07 14,341 participants/48 songs/independent control, K12 Vienna defining conditions (few patrons, word-of-mouth, no recording), K13 convex-vs-concave mechanism.
* Raise faithfulness_precision above 0.95 by restoring the dropped hedges on C041 ('may be ill-posed'), C048 ('probably' 20 to 50), and C051 (conditional 'if the mechanisms are right'), or downgrade those node statements to matches the source's modality.
* Merge C034 into C008, C039 into C022, and remove trivia C035 and C040 to shave length, freeing budget for the Must-have completions which are the binding constraint.

## 06_valuing_consistency

Verdict: Fail (weighted 0.7286, precision 0.9524, must recall 0.8929, redundancy 0.0476)

### Non-supported claims

* C028 [Partially supported, Minor] loglog 6.4
  * claim: Revision and laundering can reach identical anchors, indistinguishable inside and out.
  * evidence: From outside they are indistinguishable. Often from inside too.
  * why: Source hedges inside indistinguishability with often, but the claim states it as absolute.
* C040 [Partially supported, Minor] loglog 10.1
  * claim: Evaluate process not output, though process stays mostly invisible and unfalsifiable.
  * evidence: The process is mostly invisible, and the stories people tell about it afterward are mostly unfalsifiable.
  * why: Source calls the process invisible but attributes unfalsifiability to the stories told about it, not to the process itself.

### Non-present key points

* K05 [Must have, Partial]
  * point: Modest woman solved: anchor a = 0 and responsiveness w = 0.2. Her output moved (from -0.1 to 0.1) but her rule never did, a fixed anchor at neutral conceding a fixed twenty percent of the distance toward society.
  * loglog: L009, L010
  * why: Anchor 0, w 0.2, and the fixed-rule observation are all present, but the illustrative output values (-0.1 to 0.1) are dropped. Per the strict rule, a Must have with a dropped number is at most Partial.
* K09 [Must have, Partial]
  * point: The spectrum of w postures: above 1 amplifier, exactly 1 absolute conformist, between 0 and 1 partial conformist, exactly 0 independent, between -1 and 0 partial contrarian, exactly -1 absolute contrarian. The independent is the only posture that needs no information about the reference, so absolute conformist and absolute contrarian are closer to each other than either is to the independent.
  * loglog: L018, L019
  * why: The existence of a posture spectrum and the independence/mirroring claim are present, but the six named values and threshold boundaries are not enumerated (only 'amplifier to extremist rebel'). A reader cannot recover the full taxonomy from the loglog, so Partial.
* K11 [Must have, Partial]
  * point: Retirement investing example: the 110-minus-age equity rule (about 85 percent stocks at 25, about 50 percent at 60) shows that behavior moving with a reference need not be inconsistency. Holding 85 percent equities at 65 because you have always been aggressive is refusal to let a correctly varying function vary, not conviction. Same form as the clothing conformist, opposite moral verdict.
  * loglog: L023, L024
  * why: The 110-minus-age rule and the same-form/opposite-verdict contrast survive, but the 85/50 percent figures, the ages 25/60, and the 65-year-old refusal scenario are dropped. A Must have with dropped numbers is at most Partial.

### Concision flags

* C038 Duplicate of C036: Restates underdetermination without prior prediction; only flattering-default rejection is new.
* C039 Duplicate of C001: Section 10 recap restating thesis and swinging-woman one-rule point already made.
* C041 Trivia: Meta scope note on unexplored cases; no main point, low information value.

### Fix list

* K09: enumerate the six named w postures with their threshold boundaries (amplifier >1, absolute conformist =1, partial conformist 0<w<1, independent =0, partial contrarian -1<w<0, absolute contrarian =-1) instead of the single paraphrase 'amplifier to extremist rebel'
* K11: restore the dropped numbers 85 percent at 25 and 50 percent at 60 plus the 65-year-old refusal scenario to upgrade this Must have from Partial to Present
* K05: restore the illustrative output values (-0.1 to 0.1) for the modest-woman case so the fixed-rule demonstration carries its full evidence
* C028: soften the absolute 'indistinguishable inside and out' to match the source hedge 'often from inside too'
* C040: attribute unfalsifiability to the stories told about the process, not the process itself, per loglog 10.1

## 07_intentionalism

Verdict: Borderline (weighted 0.75476, precision 0.9796, must recall 0.9583, redundancy 0.102)

### Non-supported claims

* C010 [Partially supported, Minor] loglog 3.1
  * claim: Informal proposer-receiver structures systematically favor whoever proposes.
  * evidence: the outcomes tend to favor whoever's doing the proposing
  * why: SOURCE hedges with 'tend to'; loglog states it as absolute systematic fact.

### Non-present key points

* K02 [Must have, Partial]
  * point: In 1962 mathematicians-economists David Gale and Lloyd Shapley worked on creating stable pairings between two groups and proved a stable matching (no unmatched pair preferring each other) always exists.
  * loglog: L003
  * why: The date 1962, the names Gale-Shapley, and the stable-matching subject are retained, but the existence proof (a stable matching always exists) and the definition of stability (no blocking pair) are dropped. Must-have point with a lost claim, so Partial.
* K15 [Nice to have, Partial]
  * point: Appendix concrete tools: domain exercises (entertainment, shopping with must-haves and 24-hour rule over $100, career with 5 non-negotiables and applying only when 4 of 5 match, relationships), daily pause and journaling practices, and a 30-day tracking journal showing proposers report higher satisfaction.
  * loglog: L041, L043, L045, L048, L049
  * why: All domains and practices are present, but the specific numeric thresholds are dropped: the $100 bar for the shopping 24-hour rule and the 4-of-5 match rule in career. Nice-to-have, so this lowers polish rather than recall of a must-have.

### Concision flags

* C015 Duplicate of C013: Same prerequisite-product content as C013, only adds trap label.
* C023 Duplicate of C005: Restates C005 structural-over-personal-ability point.
* C038 Duplicate of C019: Repeats C019 practice-to-values ladder as muscle-to-proposers chain.
* C039 Duplicate of C004: Restates C004 proposer-advantage and mathematical extreme.
* C049 Duplicate of C030: Restates ask-what-wanted (C030) and small-reps (C017), no new information.

### Fix list

* K02 (Must have, L003): restore the guarantee that a stable matching always exists and the stability definition (no blocking pair preferring each other); this is the only Must-have recall loss and the top lever.
* C010 (Minor, 3.1): hedge the absolute claim 'systematically favor whoever proposes' back to SOURCE's 'tend to favor' to clear the last partial support.
* K15 (Nice to have, L041/L043/L045/L048/L049): reinsert the dropped numeric thresholds, the $100 bar for the 24-hour shopping rule and the 4-of-5 career match rule, to convert a Partial to Present.
* Merge duplicate claims C015/C013, C023/C005, C038/C019, C039/C004, C049/C030 to push redundancy further below the 0.15 cap.

## 08_empathy_sympathy_compassion_matrix

Verdict: Borderline (weighted 0.7507, precision 1.0, must recall 0.9167, redundancy 0.08)

### Non-present key points

* K06 [Must have, Partial]
  * point: The sustainable-and-scalable row reflects the Bloom/Singer argument (Paul Bloom's Against Empathy and Tania Singer's compassion-training research); it is a position, not a consensus, and critics reply that compassion without empathic grounding risks becoming abstract or paternalistic.
  * loglog: L013, L014
  * why: The row, the Bloom/Singer attribution, and the 'position not a consensus' caveat are all present, but the critics' counterargument (compassion without empathic grounding risks becoming abstract or paternalistic) is entirely absent. A must-have qualifier element is dropped, capping this at Partial.
* K15 [Must have, Partial]
  * point: The three Light Triad rows partly restate earlier rows: Kantianism is essentially the inverse of the manipulators row, Humanism overlaps the caring and beyond-the-in-group rows, and only Faith in Humanity adds a genuinely new dimension (an attitude rather than an empathy component), which is why both dark profiles score blank on it.
  * loglog: L022
  * why: The redundancy thesis and the novel-Faith row are captured, and the Kantianism/manipulators mapping is present. However the Humanism overlap mapping and the explanation for why both dark profiles go blank on Faith in Humanity are dropped, so this must-have loses some of its justifying detail.

### Concision flags

* C012 Duplicate of C011: Restates compassion alone leading helping and sustainability; adds no information.
* C015 Duplicate of C014: Only control being psychopath-only restates C014; degradation nuance is minor.

### Fix list

* K06: add the critics' counterargument that compassion without empathic grounding risks becoming abstract or paternalistic, the single missing qualifier that caps this Must-have at Partial.
* K15: restore the Humanism-overlap mapping and the explanation for why both dark profiles score blank on Faith in Humanity, both dropped justifying details.
* Merge C012 into C011 and C015 into C014 to remove the only redundancy (rate 0.08, still below 0.15 max).

## 09_not_even_wrong

Verdict: Fail (weighted 0.7358, precision 0.9375, must recall 0.9333, redundancy 0.0625)

### Non-supported claims

* C014 [Partially supported, Minor] loglog 3.3
  * claim: Algorithms build echo chambers while frequent posts fake personal authenticity.
  * evidence: frequent, seemingly unfiltered posts from these figures create a sense of personal connection and authenticity
  * why: Echo chambers supported, but source says posts create authenticity and 'seemingly unfiltered', not that they fake it.
* C032 [Partially supported, Minor] loglog 7.4
  * claim: The author discloses Claude Sonnet 3.5 help and recommends two skepticism books.
  * evidence: [disclaimenr: the content below is written with the help of Claude-sonnet-3.5] ... Calling Bullshit ... The Age of Surveillance Capitalism
  * why: Disclosure supported, but only Calling Bullshit is a skepticism book; Zuboff's book is said not to address this topic directly.

### Non-present key points

* K02 [Must have, Partial]
  * point: The 'not even wrong' concept, popularized by physicist Wolfgang Pauli, describes ideas so fundamentally flawed they cannot be meaningfully evaluated as correct or incorrect.
  * loglog: L003
  * why: The definition is captured exactly and correctly. However, the point bundles the attribution to Wolfgang Pauli, which is entirely absent from the loglog. A reader loses the origin/anchor of the term, so this counts as a dropped qualifier/narrowed point.
* K03 [Must have, Partial]
  * point: Sir Michael Atiyah, at age 89 and already holding both the Fields Medal and Abel Prize, claimed to have solved the Riemann hypothesis, a problem open since 1859.
  * loglog: L004
  * why: Atiyah and his Riemann-claim are mentioned, but the concrete facts that give the point its weight (age 89, Fields Medal, Abel Prize, open since 1859) are all dropped. A Must-have point with dropped numbers/dates is at most Partial.

### Concision flags

* C016 Duplicate of C015: Reruns the same four factors with synonyms; adds nothing new.
* C030 Duplicate of C001: Recaps the shared-standards thesis; science analogy is cosmetic.

### Fix list

* Raise faithfulness precision above 0.95 by tightening C014 (3.3): source says posts 'create a sense of personal connection and authenticity' and are 'seemingly unfiltered', not that they 'fake personal authenticity'. Drop or reword 'fake' to the sourced framing.
* Fix C032 (7.4): only 'Calling Bullshit' is a skepticism book. Zuboff's 'The Age of Surveillance Capitalism' is noted as not addressing this topic directly, so the 'two skepticism books' bundling overstates the source. Restate as one skepticism book plus one related critique.
* Recover key point K02 (L003): it is Partial because the Wolfgang Pauli attribution is absent. Add the Pauli origin so the Must-have point is fully anchored.
* Recover key point K03 (L004): it is Partial because age 89, Fields Medal, Abel Prize, and 'open since 1859' were all dropped. Restore the concrete numbers/dates to promote it from Partial to Present.
* Merge duplicates C016 into C015 and C030 into C001 to trim redundancy further (already below max, low priority).

## 10_parde_begardan_fa

Verdict: Fail (weighted 0.7, precision 0.9583, must recall 0.8125, redundancy 0.0417)

### Non-supported claims

* C003 [Partially supported, Minor] loglog 1.1
  * claim: سنتور گوشه اتاق بود و خاله «زرد ملیجه» را نواخت.
  * evidence: یه آهنگ هم برامون زد، «زرد ملیجه» بود فکر کنم
  * why: Source hedges the song with فکر کنم (I think); loglog states it as certain, dropping the hedge.

### Non-present key points

* K01 [Must have, Partial]
  * point: At age 7, at his aunt's house, the author first encountered the santur his cousin had just bought; the cousin let him sit at it and taught him how to hold the mizrab, and he had to be dragged away from it at night's end.
  * loglog: L003, L005
  * why: Age 7, the aunt's house, the santur, and being dragged away at night are captured. But the source's actor is the cousin who bought the santur and taught him to hold the mizrab. Loglog reassigns the instrument to the aunt (سنتور خاله) and omits the cousin and the mizrab lesson, so the central origin detail is narrowed.
* K02 [Nice to have, Partial]
  * point: The first tune he heard on that santur was likely 'Zard Maliheh' (زرد ملیجه), one of the first songs taught to santur beginners.
  * loglog: L004
  * why: Zard Maliheh as the tune heard is captured, but the qualifier that it is one of the first songs taught to santur beginners is dropped. Also the source hedges the identification ('likely'), which is lost.
* K03 [Must have, Partial]
  * point: After six months of nagging and sulking, his family finally bought him a santur for 20,000 toman, discounted to 18,000 toman.
  * loglog: L006
  * why: Six months of insistence and the 18,000-toman purchase price are present, but the original 20,000-toman list price and the discount are dropped. A Must have point with a dropped number is at most Partial.
* K04 [Nice to have, Partial]
  * point: He started lessons six months later; the teacher initially came to his home because their city had no school, and only later did the Ershad office open a class where the teacher taught.
  * loglog: L008
  * why: The teacher coming home because the city had no school is captured, but the six-month delay before lessons and the later Ershad office class are omitted, narrowing the background.
* K11 [Must have, Partial]
  * point: With the unstinting help of family, friends, officials, and clerics/community leaders, the instrument finally reached him today.
  * loglog: L019
  * why: The arrival with help from family, friends, and officials is captured, but the clerics/community leaders are omitted and the 'today' timing is dropped, narrowing the credited helper set and the event's immediacy.
* K13 [Nice to have, Partial]
  * point: He felt like a penned fattened sheep set loose, running without pause: he skipped lunch and played so long his back ached.
  * loglog: L023
  * why: Skipping lunch and playing until his back hurt are captured, but the leading sheep-set-loose metaphor is dropped, losing the point's most distinctive image.

### Concision flags

* C023 Duplicate of C004: Restates C004's late-night scene; cross-link confirms the repeat.
* C021 Trivia: Theme header restates 6.1 and 6.3 with no number, caveat, or new detail.

### Fix list

* Raise must_have recall above 0.9 by fully landing the three Must-have partials: K01 (restore the cousin as instrument-buyer and the mizrab lesson from L003/L005), K03 (restore the 20,000-toman list price and discount from L006), K11 (restore clerics/community leaders and the 'today' timing from L019).
* Restore the source hedge on C003 / L004: the song identification is 'فکر کنم' (I think), currently stated as certain in loglog line 1.1; this is the only Partially supported claim and drives faithfulness_precision to 0.9583.
* Recover the dropped descriptive detail on Nice-to-have partials K02 (one of the first songs taught to beginners), K04 (six-month lesson delay and Ershad office class), and K13 (the penned fattened-sheep set-loose metaphor from L023) once the Must-haves are fixed.
* Merge duplicate C023 into C004 and drop or rewrite the C021 header restatement to trim the residual trivia without touching coverage.

## 11_finding_a_phone

Verdict: Fail (weighted 0.71318, precision 0.9355, must recall 0.8636, redundancy 0.0323)

### Non-supported claims

* C010 [Partially supported, Minor] loglog 4.1
  * claim: Wanted week-long battery, waterproofing, SD slot, jack, decent mic, and customization.
  * evidence: Long battery life; waterproofing and shockproofing; SD card slots and headphone jacks; decent mic and speaker quality; customization options
  * why: Source requirement is 'Long battery life'; 'week-long' comes from a Ulefone feature, adding a duration not required.
* C026 [Partially supported, Minor] loglog 9.2
  * claim: The Edge 40 comparison failed: it has no SD card slot.
  * evidence: it seems like it doesn't have sd card slot!
  * why: Source hedges with 'seems like'; node states the absence as certain fact.

### Non-present key points

* K03 [Nice to have, Partial]
  * point: After a period with no phone, he bought the Motorola Droid on day one. It was one of the first Android smartphones widely available in the U.S. and became a centerpiece of his life.
  * loglog: L003, L005
  * why: Day-one purchase and centerpiece role are captured, but the qualifier that it was one of the first Android smartphones widely available in the U.S. is dropped, narrowing the significance.
* K06 [Must have, Partial]
  * point: His must-have phone features: long battery life, waterproofing and shockproofing, SD card slots and headphone jacks, decent mic and speaker quality, and customization options.
  * loglog: L011, L015
  * why: Most requirements are captured, but the stated list drops shockproofing and speaker quality. Shockproofing reappears only as a Ulefone feature (L015), not as a stated requirement, so the enumerated must-have list is incomplete.
* K08 [Must have, Partial]
  * point: He criticizes Apple and Google for deliberately limiting offline use by removing SD card slots and offering minimal onboard storage to push cloud services.
  * loglog: L013
  * why: The accusation and intent (deliberate, to push cloud) are captured, but the specific mechanism that gives it substance, removing SD card slots and minimal onboard storage, is dropped, so the claim is narrowed.
* K13 [Nice to have, Partial]
  * point: He used gpt-4o-mini to write Python scraping code and claude-3.5 sonnet (after several prompts) to clean the dataframe into the wanted columns; the result mostly works but he has not checked it and assumes several errors.
  * loglog: L022, L023, L024
  * why: The pipeline roles (scraping DataFrame/CSV, cleaning to wanted columns) and the unverified/assumed-faulty caveat are captured, but the specific model names gpt-4o-mini and claude-3.5 sonnet are dropped.
* K15 [Must have, Partial]
  * point: Update 2025-01-05: he tried the TCL 50 XE NXTPAPER for a couple of weeks. It was weak on performance, ran uncomfortably hot on a video call, and its screen was much worse, almost unreadable in direct or lamp light compared with regular screens; the camera was average; the paper and ink color modes were good ideas but poorly implemented with many restrictions, and it was not true e-ink as he had expected. He returned it and next plans to try the Motorola G85, having wanted the more waterproof IP68 G75 but being unable to find it in stores; the G85 is only water repellent and Motorola cameras are generally not expected to be good.
  * loglog: L029, L030, L031, L032
  * why: Core verdicts are captured: heat on calls, unreadable screen in direct light, paper/ink modes poorly implemented with restrictions, return of the TCL, and the G85 as the water-repellent fallback after the IP68 G75 proved unavailable. Dropped details weaken it: the model name 'TCL 50 XE NXTPAPER', weak performance, average camera, the 'not true e-ink as expected' expectation, the video-call (vs call) qualifier, and the general warning that Motorola cameras are not good.

### Concision flags

* C009 Duplicate of C010: Re-lists C010 positives plus C011 negatives with no new content.

### Fix list

* Restore the dropped must-have specifics on the partial points: K06 add shockproofing and speaker quality as stated requirements; K08 add the mechanism (removed SD card slots, minimal onboard storage); K15 add the missing model name TCL 50 XE NXTPAPER and the weak-performance, average-camera, not-true-e-ink details. These three Must-have partials are the direct cause of must_recall 0.8636.
* Tighten C010 to the source requirement: write 'long battery life' rather than 'week-long battery', which injects a duration only present as a Ulefone feature (loglog 4.1).
* Tighten C026 to match the source hedge: 'it seems like it does not have an SD card slot' rather than asserting the absence as certain (loglog 9.2). These two partials hold precision at 0.9355.
* Merge the requirements re-listing noted in the prune list (C009 duplicates C010 and C011) into the evidence lines, which is safe and does not affect the failed gates.

## 12_lets_talk_privacy

Verdict: Fail (weighted 0.697, precision 0.9697, must recall 0.8333, redundancy 0.1212)

### Non-supported claims

* C030 [Partially supported, Minor] loglog 8.5
  * claim: Trust-minimizing needs client-side crypto, zero-knowledge servers, reproducible audited builds.
  * evidence: All cryptography happens client-side ... The server never sees anything that could decrypt your data ... open-source AND reproducibly built AND you can verify what's running
  * why: SOURCE says reproducibly built and verifiable, not 'audited'; added qualifier slightly changes the third condition.

### Non-present key points

* K03 [Must have, Partial]
  * point: For WhatsApp the answer is unclear: if implemented as claimed and with no secret backdoors they cannot access data, but the app is not open source and not truly auditable, so external audits can never prove the negative (that access is impossible).
  * loglog: L005, L028
  * why: Closed-source and unverifiability are captured, but the loglog hardens the original open question into a firm verdict ('likely accesses') rather than preserving 'the answer is unclear' and the cannot-prove-a-negative framing. Scope is narrowed, so Partial.
* K04 [Must have, Partial]
  * point: Evidence against WhatsApp/Meta: the 2021 privacy policy changes allowing data sharing with Facebook for relevant offers and ads across Meta products, plus prior security failures such as storing hundreds of millions of passwords in plaintext, make it almost certain they can and do access message content.
  * loglog: L005, L021
  * why: Ad-data sharing and the plaintext-failure evidence are present, and 'hundreds of millions' survives, but the 2021 date of the privacy policy change is dropped. A Must have point missing a key date is at most Partial.
* K07 [Must have, Partial]
  * point: Proton Mail model: the private key is generated in the browser and encrypted with your password using bcrypt and AES-256, then stored encrypted on Proton's servers, so the server holds only an encrypted private key.
  * loglog: L010, L011
  * why: Browser-side generation and password-encrypted server storage are captured, and bcrypt appears, but AES-256 is never named. A Must have point with a dropped technical number is at most Partial.
* K11 [Must have, Partial]
  * point: Signal's approach: by default history is stored only on your device and deleted from servers after delivery. Device switching offers three options: manual local backup protected by a 30-digit passphrase, direct device-to-device local transfer, or Secure Backups encrypted with a 64-character recovery key Signal never sees.
  * loglog: L016, L017
  * why: The on-device storage model and all three migration options are present with the correct qualifiers, but the 30-digit passphrase and 64-character recovery key numbers are dropped. A Must have point with dropped numbers is at most Partial.
* K14 [Nice to have, Partial]
  * point: Real-world examples: Facebook in 2019 logged roughly 200-600 million passwords in plaintext in internal logs for years, searchable by over 20,000 employees with archives dating to 2012, claiming it was unintentional. Adobe's 2013 breach exposed plaintext password hints, and many small services use plaintext or unsalted MD5. Proton's loss of old emails after an email/SMS password reset suggests genuine inability to decrypt, though this is not proof.
  * loglog: L021, L022, L030
  * why: The three examples and the Proton caveat are present, with years 2019/2013 and 'hundreds of millions' retained, but the 200-600 million range, 20,000 employees, 2012 archive date, and MD5 specificity are dropped. Nice to have, so this is a polish issue rather than a failure.

### Concision flags

* C024 Duplicate of C001: Section 7 triad restates the summary's WhatsApp/Proton/Signal comparison.
* C025 Duplicate of C018: Section 8 thesis restates section 6 unverifiable password-storage claim.
* C029 Duplicate of C020: Same Adobe, Facebook, small-service breach examples already given in 6.2.
* C031 Duplicate of C001: Applied-trust triad repeats the summary/comparison service mapping.
* C033 Trivia: Meta sources line, no argumentative value, restates header-level citations.

### Fix list

* Restore the dropped specifics in the four Partial Must have points to lift must_recall above 0.9: add AES-256 to K07 (L010/L011), add the 30-digit passphrase and 64-character recovery key to K11 (L016/L017), add the 2021 date to K04 (L005/L021), and restore K03's original unanswered framing ('the answer is unclear' and cannot prove a negative) instead of the hardened 'likely accesses' verdict (L005/L028).
* Merge duplicates to free length budget while keeping redundancy under 0.15: C024 into C001, C025 into C018, C029 into C020, C031 into C001, and cut trivia C033 (meta sources line).
* Soften C030 'reproducible audited builds' to 'reproducibly built and verifiable' to clear the sole Partially supported Minor claim and keep faithfulness_precision above the 0.95 gate.

