# Judge trace: 06_valuing_consistency (judge model muse-spark-1.3-contributor-free 2026-09-11)

## Judge F: faithfulness (43 claims, 42 Supported + 1 Partial Minor, precision 0.9767)

Atomization policy: one leaf bullet yields one claim; L18 packs the spectrum
endpoints but was verified endpoint by endpoint inside C18. Title L01 and
Summary L02 are meta/interpretation claims. The Cross-links block (lines 44-50)
and Coverage footer (line 51) are skipped as boilerplate relational notes.

Strict number verification: modest solution anchor 0 with w 0.2 at minus 0.1
and 0.1 against society minus 0.5 and 0.5 (C09); swinger at 0.9 and minus 0.9
with anchor 0 and w 1.8 (C11); contrarian at 0.2 and minus 0.2 with w minus 0.4
(C16); investing 110-minus-age with 85% at 25 and 50% at 60 (C23); equation
transcription exact (C07). Equation derivations were checked for sign errors:
subtracting the modest pair gives w 0.2, the swinger pair gives w 1.8, the
contrarian pair gives w minus 0.4, all matching both source and outline. No
name or entity drift (no person names beyond the mother story, correctly kept);
no flipped negations (never-open analogues n/a; resist/track split kept on the
right reference kinds in C21). Hedges preserved (may, IMHO, perhaps rendered
as resembles, likely-style closers) except one place.

The exception is C29 (6.4): source says twins are indistinguishable from
outside and Often from inside too, while the outline says indistinguishable
inside and out. Per the hedge rule this is at most Partially supported; a
single-word qualifier loss, so Minor. No contradictions, nothing unverifiable.

Result: supported 42, partial 1, contradicted 0, critical_errors 0, precision
42/43 = 0.9767, fail_list names C29 only.

## Judge Cov: coverage (13 must + 2 nice, must_recall 0.9615, overall 0.9667)

Blind checklist from source: vague-word puzzle plus story plus swing verdict,
equation plus definitions, modest numbers, swinger numbers, three layers plus
drift, contrarian, spectrum table, reference kinds plus investing, four cells
plus splits plus footnote, aphorism dual process, three complications, prior
prediction test, closing verdict (must); PS1 and PS2 concessions (nice).

Mapping notes: K07 is Partial because section 4 compresses the six-row
spectrum into endpoints (amplifier to extremist rebel) plus the independence
exclusivity, dropping the middle rows, notably the absolute conformist whose
anchor drops out with no fixed point to reconstruct belief from. That
narrowing is exactly the at-most-Partial case for a Must point with dropped
content. K09 is Present with an explicit note that C29 drops Often inside it,
which is why Top fires Borderline rather than failing coverage. All other
musts and both nice points are fully Present, including both PS concessions
with their [conceded] tags.

Metrics: must (12 + 0.5)/13 = 0.9615; overall (14 + 0.5)/15 = 0.9667.

## Judge Con: concision (43 scored, 43 unique, redundancy 0.0, trivia 0.0)

Duplicate sweep: C40 (closing pair) was checked against C12 (equal
consistency) and C24 (opposite verdicts) and kept Unique because it adds the
investor-failure half and the back-to-mom's-story framing, standard synthesis
with new content. Themes vs children all add frames versus figures throughout.
Trivia sweep: every claim maps to a Must or Nice point, and equation, number,
caveat, and negation claims are exempt by rule. C29 stays visible as Unique
per the never-hide-a-verdict rule. structured_tokens 716 by whitespace count;
tokens_per_unique_claim 716/43 = 16.65; trivia_rate 0.0. prune_list empty.

## Judge Top: overall (Borderline, weighted 0.7753)

Gates all pass (critical 0, precision 0.9767, must_recall 0.9615, redundancy
0.0), but Partial claim C29 sits inside Must-have K09, so the Borderline rule
requires human review of that one hedge loss. Computation: 0.4*0.9767 +
0.4*0.9615 - 0.2*0.0 = 0.7753. Tradeoff: the outline earns its length with
near-complete recall at zero redundancy; closing the K07 gap costs a little
length rather than pruning. Fix list by leverage: reattach Often to C29 first
(clears Borderline), then spell out the spectrum middle rows, nothing to prune.
