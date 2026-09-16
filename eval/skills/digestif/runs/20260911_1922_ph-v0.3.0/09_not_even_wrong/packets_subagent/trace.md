# Judge trace: 09_not_even_wrong (skill v0.3.0, judged 2026-09-12)

Atomization note: output.log carries no L-IDs, so loglog_ids use outline node numbers, each exactly one file line. Title, Summary, Cross-links, Coverage lines excluded as scaffolding with no independent propositional content beyond the numbered nodes.

## Judge F (faithfulness): 21/21 Supported, precision 1.0, critical_errors 0

Transcript: negation-heavy sample, so every not/never/no/without/only polarity was checked word by word. C01 keeps cannot-be-evaluated (l.10). C06 keeps isn't-just-protection (l.20). C09 keeps the might hedge and unfalsifiable (l.25). C12 keeps often (l.30). C13 keeps tend and seemingly-unfiltered (l.32). C14 keeps not-purely-rational plus all four bullets (l.35-39). C15 keeps can (l.41). C16 keeps ultimately-rejected, often-escape, lacks-frameworks (l.43). C21 keeps doesn't-directly-talk (l.75). Numbers exact: 89, Fields plus Abel, Riemann, 1859 (C03); thousands-or-millions (C11). The Would-I-believe test (C18) is verbatim in meaning; its credible-sources compression states nothing false, so Supported here (flagged for coverage instead). No outside knowledge used; book characterizations come from l.71-75 only. fail_list empty.

## Judge Cov (coverage): 14 points, must_recall 0.96, overall_recall 0.96

Transcript: checklist built blind from source: definition-plus-Pauli, Atiyah case, leaders extension, investment loop, spillover-plus-pairing, cycle-plus-identity, social-proof-plus-tribal, amplification, vulnerability thesis, standards asymmetry, individual paths, societal paths, beyond-tribal close, books (Nice). Mapping: 12 Must Present, 1 Must Partial (K11: counter-narratives drops the credible-sources-in-relevant-domains qualifier, a lost qualifier narrowing scope, hence at most Partial per spec), 1 Nice Present. must_recall = (12 + 0.5)/13 = 0.9615, reported 0.96; overall = (13 + 0.5)/14 = 0.9643, reported 0.96. Per the Contradicted-credit rule there was nothing to discount. missing_list holds K11 with reason.

## Judge Con (concision): 21 scored, 0 duplicates, 0 trivia, redundancy 0.0

Transcript: pair-checked plausible repeats (C08 cycle vs C06/C07 mechanisms; C20 close vs C17-C19 prescriptions; C10 header vs children). Each adds links, framing, or content from a distinct source passage, so all Unique. Every claim maps to a key point; no filler. structured_tokens 417 by wc -w; tokens_per_unique_claim = 417/21 = 19.86. prune_list empty.

## Judge Top (overall): Pass, weighted_score 0.78

Transcript: all gates pass (critical 0, precision 1.0 >= 0.95, must_recall 0.96 >= 0.9, redundancy 0.0 <= 0.15). Computation: 0.4*1.0 + 0.4*0.9615 - 0.2*0.0 = 0.7846, reported 0.78. Borderline considered and rejected: the condition requires a Partial or Unverifiable claim affecting a Must-have point, and Judge F has none (all Supported); the K11 Partial is a coverage mapping, already priced into must_recall. fix_list ordered by leverage: the 5.1 qualifier restoration first, then an explicit no-further-fixes note.
