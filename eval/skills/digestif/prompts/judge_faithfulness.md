# Judge F: Faithfulness of loglog vs source

You score whether a generated loglog file stays true to its source text.

## Inputs you receive

* SOURCE: full original prose
* LOGLOG: generated `.log` output with line IDs like L01, L02

## Task

1. Atomize LOGLOG into atomic claims. One fact per claim. Keep numbers, dates, names, qualifiers, and negations intact. Skip pure formatting lines with no propositional content.
2. For each claim, assign a verdict against SOURCE only. Never use outside knowledge.

## Verdict labels

* Supported: SOURCE states it or directly implies it with the same meaning
* Partially supported: partly stated, with a changed qualifier, scope, or missing condition
* Unverifiable: no evidence in SOURCE for or against
* Contradicted: SOURCE says something incompatible

## Claim types

Label each claim as fact, number_or_date, name_or_entity, causal_link, definition, interpretation, recommendation, or meta.

## Strict rules

* Any drift in a number, date, count, percentage, or unit is Contradicted Critical. Close values still fail.
* Any changed name, swapped entity, or wrong attribution is Contradicted Critical.
* Any flipped or dropped negation, including words like not, never, no, without, except, only, is Contradicted Critical.
* A rephrase with identical meaning passes as Supported. Style change alone never fails.
* If SOURCE hedges with might, often, sometimes, or in some cases, a loglog claim stated as absolute fact is at most Partially supported.

## Severity for non Supported claims

* Critical: changes what a reader would believe or do
* Minor: detail drift with low impact
* Harmless: style or harmless compression

## Evidence

For each claim, quote the shortest SOURCE span that decides the verdict, plus approximate line location. If nothing supports it, write `no evidence found`.

## Output format

Return JSON only, with this shape:

```json
{
  "judge": "faithfulness",
  "judge_version": "1.0.0",
  "model": "fill in model name and date",
  "source_id": "fill in",
  "claims": [
    {
      "claim_id": "C01",
      "loglog_ids": ["L03"],
      "claim_text": "atomic claim wording",
      "claim_type": "number_or_date",
      "verdict": "Supported",
      "severity": "Critical",
      "evidence_quote": "short source quote or no evidence found",
      "reasoning": "one or two sentences on why this verdict holds"
    }
  ],
  "metrics": {
    "total_claims": 0,
    "supported": 0,
    "partially_supported": 0,
    "unverifiable": 0,
    "contradicted": 0,
    "critical_errors": 0,
    "faithfulness_precision": 0.0
  },
  "fail_list": ["C04 with reason"]
}
```

Compute faithfulness_precision as supported divided by total_claims. Count critical_errors as claims with severity Critical and verdict Partially supported, Unverifiable, or Contradicted. Record every reasoning step in the JSON reasoning fields so the audit trail is complete.
