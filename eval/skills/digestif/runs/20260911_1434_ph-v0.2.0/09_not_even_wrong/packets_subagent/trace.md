# Judge trace: 09_not_even_wrong (run 20260911_1434_ph-v0.2.0, model muse-spark-1.3-contributor-free 2026-09-11)

## Judge F: Faithfulness (34 atomic claims; cross-links L34-L45 and coverage line L46 excluded as boilerplate)

Atomization: one claim per content line (L01, L03-L33), except the Summary (L02) split into the escape-thesis (C02) and the cause-plus-prescription (C03). Every not/never/no/without/only in the outline was checked against source polarity (see verdicts).

Polarity walkthrough (the brief's focus):
- C06 "not simply incorrect": source line 14 identical. Pass.
- C09 "isn't just protecting / it's dissonance": source line 18 identical. Pass.
- C17 "not purely rational": source line 35 identical. Pass.
- C21 "without accepting": line 47. C22 "doesn't transfer": line 48. C23 "isn't about critics for critics' sake": line 49. C24 "if I hadn't invested": line 50. C29 skepticism/opposition double negation: line 56. C31 "isn't for/against, it's tools": line 59. All pass with polarity intact.
- Zero flipped or dropped negations anywhere, hence critical_errors 0.

Other verdict reasoning:
- C02 (summary escape-thesis): the 'often' hedge from line 43 is absent in the summary sentence, but this is a generic phenomenon statement and the hedge is explicitly retained in body claim C19, so the outline does not absolutize. Supported. Contrast with C16 below, where the hedge-drop compounds with a spin.
- C05: 'late' fairly rephrases 'near end of life / age 89'; dropped color (prizes, 1859, Pauli) is non-load-bearing. Supported.
- C10: 'accept' is not a strengthening because the source's own spillover sentence says 'easier to accept' (line 21). Supported.
- C12: conditional-to-generic ('when fulfilled' to 'fulfilled X backs Y') preserves the mechanism and the evidentiary-standards contrast. Supported.
- C14: 'thousands' from 'thousands or millions' is logical entailment of an illustrative range, not a count drift; the strict number rule targets load-bearing figures. Supported.
- C16: Partially supported, Minor. Two compounding strengthenings in one claim: dropped 'tend to' on the algorithm half and 'create a sense of authenticity' spun into 'fake personal authenticity'. Mechanism (echo chambers, frequent-post authenticity) correctly described, so Minor, not Critical. Sole fail_list entry.
- C34: disclosure name exact; 'skepticism books' is a loose but harmless descriptor since both books are presented as relevant recommendations and the outline claims nothing false about their contents. Supported.
Result: 33/34 Supported, precision 33/34 = 0.9706, critical_errors 0.

## Judge Cov: Coverage (checklist built blind from source, then mapped)

Blind checklist: concept (K01), Atiyah illustration (K02), beyond-math bridge (K03), loop with mechanism (K04), spillover plus credibility transfer (K05), three entrenchment channels (K06), vulnerability thesis plus four factors (K07), frameworks asymmetry (K08), four individual (K09) and four societal (K10) prescriptions, close with sympathy-plus-rigor (K11) as Must-haves; disclosure plus books (K12) as Nice-to-have. Mapping: all 11 Must-haves Present. K02 stays Present (not Partial) because the dropped specifics are illustrative color, recorded here for audit rather than penalized, since coverage scores what matters. K06 stays Present because the Contradicted-only downgrade rule does not demote on a Partial, and C16's mechanism is intact alongside C13-C15. must_recall 1.0, overall 1.0, missing_list empty.

## Judge Con: Concision (34 scored claims; C16 stays scored as Unique because Partial is not Contradicted and its mechanism detail is new)

Duplicate hunt: none. Headers (C13, C20, C25) each add framing while details live in sub-claims; C06 adds the key negation beyond C04; C18 enumerates beyond C17; C31 adds the for/against angle beyond C30. Trivia: 0, every claim maps to K01-K12 and negations/caveats are never trivia. Metrics: scored 34, unique 34, redundancy 0.0, tokens 612 (wc -w), tpu 18.0. prune_list empty.

## Judge Top: Overall

Gates: critical 0, precision 0.9706 >= 0.95, must_recall 1.0 >= 0.9, redundancy 0.0 <= 0.15. All pass. Borderline considered and rejected: the lone Partial (C16, Minor) leaves K06 Present, so no Must-have point's presence is affected. weighted = 0.4*0.9706+0.4*1.0-0.2*0.0 = 0.7882. Verdict Pass. Fix list ordered by leverage: C16 reword first (only faithfulness item), dropped color last (optional, budget-dependent).
