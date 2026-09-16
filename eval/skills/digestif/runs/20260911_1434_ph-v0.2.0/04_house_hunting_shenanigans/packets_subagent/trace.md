# Judge trace: 04_house_hunting_shenanigans (judge model muse-spark-1.3-contributor-free 2026-09-11)

## Judge F: faithfulness (30 claims, all Supported, precision 1.0)

Atomization policy: one leaf bullet yields one claim, except L23 which packs two
independent facts (sale price, bet payoff) and is split into C23 and C24. Title
L01 and Summary L02 each yield one meta/interpretation claim. The Cross-links
block (file lines 30-35) and the Coverage footer (line 36) are skipped as
boilerplate: they assert relations between loglog nodes, not new source facts,
and counting them would manufacture duplicates.

Strict checks performed on every number, date, name, and negation:

- C04 (linger months vs vanish in 1-2 days): the 1-2 day half is exact. Months
  renders the source's unspecified long time inside a year-long search; a
  harmless compression that changes nothing actionable, so Supported rather than
  Partial. A stricter reader could mark it Partial Minor; it would not move any
  gate (precision would be 0.9667, still above 0.95).
- C05/C07/C08/C10/C11/C14/C15/C16/C18/C22/C23/C24/C25/C27: every figure
  verified digit by digit (30K below, 10K below advice, midnight, Sat 10:30am,
  20K cut, 5K above counter, 10K below sale, 5-10% lever, 7 months, 5%).
  Entities N, J, C, L never swapped; the fix request is attributed to C and the
  listing switch J-to-C, matching source.
- C12/C13/C19/C21/C26/C28: hedges preserved (looks like, Seems like, buyer
  believes) and nested-source claims carry [reported] tags, so no absolutizing.
- C18: two-hour rounds less than 2 hours; harmless rounding of L's own words.
- No flipped or dropped negations found (never-open stance in C20 kept intact).
- No outside knowledge used; every verdict cites a short source span.

Result: supported 30, partially 0, unverifiable 0, contradicted 0,
critical_errors 0, precision 30/30 = 1.0, fail_list empty.

## Judge Cov: coverage (9 must + 6 nice, must_recall 1.0, overall 0.8667)

Blind checklist built from source before mapping: market setup, Wednesday
rejection, Friday sweet offer plus N advice, silence-to-extension plus
suspicion, Saturday cut-to-counter, Sunday spat plus refusal, Monday rules,
below-asking outcome plus coffee, lever reflection (must); listing switch, nap,
7-month anecdote, embedded debrief, seller occupation, first-house foil (nice).

Mapping notes: K03 keeps price, terms, deadline, and advice together across
L06-L08. K05 keeps the full Saturday chain including the disclosure letter.
K06 keeps all four Sunday beats (complaint, rebuttal, refusal, in-person).
K13 is Present because 6.3/6.4 carry duration, outcome, takeaway, discipline,
bluff detection, and both failure halves; only the keep-modify-add
recommendation detail is thinned, which is below the point core. Missing:
K14 (seller teaches car dealerships) and K15 (first house went way above
asking), both Nice to have, polish only.

Metrics: must 9/9 present so must_recall 1.0; overall 13 of 15 present so
13/15 = 0.8667.

## Judge Con: concision (30 scored, 30 unique, redundancy 0.0, trivia 0.0)

Duplicate sweep: themes (C03, C06, C11, C17, C21, C26) each introduce a frame
whose children add figures or voices, so none repeats. Title C01 vs summary C02
differ by standoff plus vindication verdict. C23 vs C24 differ by bet payoff
beyond sale price. C29 vs C30 differ by discipline, bluff detection, and
failures. No intro-body-recap restatement anywhere. Trivia sweep: every claim
maps to a Must or Nice point, and all number, caveat, negation, and entity
claims are exempt by rule regardless. structured_tokens 502 by whitespace count
of output.log; tokens_per_unique_claim 502/30 = 16.73. prune_list empty.

## Judge Top: overall (Pass, weighted 0.80)

Gates: critical 0 <= 0 pass; precision 1.0 >= 0.95 pass; must_recall 1.0 >= 0.9
pass; redundancy 0.0 <= 0.15 pass. No Partial or Unverifiable claims, so the
Borderline trigger does not fire. Computation: 0.4*1.0 + 0.4*1.0 - 0.2*0.0 =
0.80. No tradeoff: full marks on both weighted aspects with zero redundancy
penalty. Fix list ordered by leverage: add K14/K15 color first (only remaining
gap), nothing to fix on faithfulness or redundancy.
