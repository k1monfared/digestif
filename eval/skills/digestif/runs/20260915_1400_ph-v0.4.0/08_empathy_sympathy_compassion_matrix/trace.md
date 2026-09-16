# Judge trace (scripted pipeline, opencode-go/deepseek-v4.1-flash)

## Judge F (faithfulness), opencode-go/deepseek-v4.1-flash

```json
{
 "judge": "faithfulness",
 "judge_version": "1.0.0",
 "model": "opencode-go/deepseek-v4.1-flash (opencode) scripted pipeline 2026-09-15",
 "source_id": "08_empathy_sympathy_compassion_matrix",
 "claims": [
  {
   "claim_id": "C001",
   "loglog_ids": [
    "0"
   ],
   "claim_text": "Feature matrix contrasts cognitive and affective empathy, sympathy, and compassion across five profiles from psychopath to integrated ideal.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "The four component columns (cognitive and affective empathy, sympathy, compassion)... psychopath, sociopath, empath, altruist, and the integrated ideal.",
   "reasoning": "Source names these four components and five profiles in the same order."
  },
  {
   "claim_id": "C002",
   "loglog_ids": [
    "1"
   ],
   "claim_text": "Cold-control block groups rows present in both dark profiles plus the psychopath-only control row.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "four blocks... present in both, in the psychopath only, in the sociopath only, and in neither.",
   "reasoning": "Rows 1-4 match the present-in-both block plus the psychopath-only row; note 6 calls that cold instrumental control."
  },
  {
   "claim_id": "C003",
   "loglog_ids": [
    "1.1"
   ],
   "claim_text": "Accurate modeling: cognitive ✓, affective ~, sympathy ~, compassion ✓; psychopath ✓, sociopath ~, empath ~, altruist ✓, integrated ✓.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "| Accurately modeling the other's mental state | ✓ | ~ | ~ | ✓ | ✓ | ~ | ~ | ✓ | ✓ |",
   "reasoning": "Every mark matches the source table row exactly."
  },
  {
   "claim_id": "C004",
   "loglog_ids": [
    "1.2"
   ],
   "claim_text": "Boundary kept: cognitive ✓, affective blank, sympathy ✓, compassion ✓; psychopath ✓, sociopath ~, empath blank, altruist ✓, integrated ✓.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "| Maintains self/other boundary | ✓ |   | ✓ | ✓ | ✓ | ~ |   | ✓ | ✓ |",
   "reasoning": "Marks and blanks match the source row precisely."
  },
  {
   "claim_id": "C005",
   "loglog_ids": [
    "1.3"
   ],
   "claim_text": "Manipulators row: cognitive ✓ only; psychopath ✓, sociopath ~, all others blank.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "| Can exist in manipulators / con artists | ✓ |   |   |   | ✓ | ~ |   |   |   |",
   "reasoning": "Correctly reports cognitive ✓, psychopath ✓, sociopath ~, rest blank."
  },
  {
   "claim_id": "C006",
   "loglog_ids": [
    "1.4"
   ],
   "claim_text": "Controlled/instrumental, not reactive/impulsive: cognitive ✓, sympathy ~, compassion ✓; psychopath ✓, altruist ✓, integrated ✓; affective, sociopath, empath blank.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "| Controlled / instrumental rather than reactive / impulsive | ✓ |   | ~ | ✓ | ✓ |   |   | ✓ | ✓ |",
   "reasoning": "Marks and blanks match the source row; negation kept intact."
  },
  {
   "claim_id": "C007",
   "loglog_ids": [
    "2"
   ],
   "claim_text": "Affective-care block: rows the sociopath has and the psychopath lacks, mostly partial marks.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "four blocks... in the sociopath only...",
   "reasoning": "Rows 5-12 are the sociopath-only block, psychopath blank, dominantly ~ marks."
  },
  {
   "claim_id": "C008",
   "loglog_ids": [
    "2.1"
   ],
   "claim_text": "Sharing/mirroring emotion: affective ✓; sociopath ~, empath ✓, altruist ~, integrated ✓; others blank.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "| Actually sharing / mirroring the emotion |   | ✓ |   |   |   | ~ | ✓ | ~ | ✓ |",
   "reasoning": "All marks and blanks match the source row."
  },
  {
   "claim_id": "C009",
   "loglog_ids": [
    "2.2"
   ],
   "claim_text": "Capacity to care at all: affective ~, sympathy ✓, compassion ✓; sociopath ✓, empath ✓, altruist ✓, integrated ✓; psychopath blank.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "| Capacity to genuinely care about the person *at all* |   | ~ | ✓ | ✓ |   | ✓ | ✓ | ✓ | ✓ |",
   "reasoning": "Marks match source exactly, including psychopath blank."
  },
  {
   "claim_id": "C010",
   "loglog_ids": [
    "2.3"
   ],
   "claim_text": "Motivation to help/act: affective ~, sympathy ~, compassion ✓; sociopath ~, empath ~, altruist ✓, integrated ✓; psychopath blank.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "| Motivation to help or act |   | ~ | ~ | ✓ |   | ~ | ~ | ✓ | ✓ |",
   "reasoning": "Full row reproduced accurately."
  },
  {
   "claim_id": "C011",
   "loglog_ids": [
    "2.4"
   ],
   "claim_text": "Guilt/remorse after harm: empath ✓; affective ~, sympathy ~, compassion ~, sociopath ~, altruist ~, integrated ~; cognitive and psychopath blank.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "| Produces guilt / remorse after causing harm |   | ~ | ~ | ~ |   | ~ | ✓ | ~ | ~ |",
   "reasoning": "Only empath ✓, all listed ~ marks and two blanks match source."
  },
  {
   "claim_id": "C012",
   "loglog_ids": [
    "2.5"
   ],
   "claim_text": "Contagion/burnout risk: affective ✓, empath ✓; sympathy ~, sociopath ~, integrated ~; others blank.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "| Risk of emotional contagion and burnout |   | ✓ | ~ |   |   | ~ | ✓ |   | ~ |",
   "reasoning": "Marks and blanks match source row."
  },
  {
   "claim_id": "C013",
   "loglog_ids": [
    "2.6"
   ],
   "claim_text": "Vivid/similar bias: affective ✓, sociopath ✓, empath ✓; cognitive ~, sympathy ~, integrated ~; others blank.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "| Biased toward vivid, similar individuals | ~ | ✓ | ~ |   |   | ✓ | ✓ |   | ~ |",
   "reasoning": "Reproduced correctly, including altruist blank."
  },
  {
   "claim_id": "C014",
   "loglog_ids": [
    "2.7"
   ],
   "claim_text": "Ends, not means (Kantianism): compassion ✓, empath ✓, altruist ✓, integrated ✓; affective ~, sympathy ~, sociopath ~; cognitive and psychopath blank.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "| Treats people as ends, not means (Kantianism) |   | ~ | ~ | ✓ |   | ~ | ✓ | ✓ | ✓ |",
   "reasoning": "Negation and all marks preserved correctly."
  },
  {
   "claim_id": "C015",
   "loglog_ids": [
    "2.8"
   ],
   "claim_text": "Dignity and worth (Humanism): sympathy ✓, compassion ✓, empath ✓, altruist ✓, integrated ✓; affective ~, sociopath ~; cognitive and psychopath blank.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "| Values each person's dignity and worth (Humanism) |   | ~ | ✓ | ✓ |   | ~ | ✓ | ✓ | ✓ |",
   "reasoning": "Rows marks match source exactly."
  },
  {
   "claim_id": "C016",
   "loglog_ids": [
    "3"
   ],
   "claim_text": "Neither-dark block: beyond in-group, faith, and scalability rows, blank for both dark profiles.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "four blocks... in neither.",
   "reasoning": "Rows 13-15 are the neither block; psychopath and sociopath are blank there."
  },
  {
   "claim_id": "C017",
   "loglog_ids": [
    "3.1"
   ],
   "claim_text": "Beyond a vivid/similar in-group: sympathy ~, compassion ✓, altruist ✓, integrated ✓; all others blank.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "| Concern reaches *beyond* a vivid / similar in-group |   |   | ~ | ✓ |   |   |   | ✓ | ✓ |",
   "reasoning": "Marks match, including both dark profile blanks."
  },
  {
   "claim_id": "C018",
   "loglog_ids": [
    "3.2"
   ],
   "claim_text": "Fundamentally good (Faith in Humanity): sympathy ~, compassion ~, empath ✓, altruist ✓, integrated ✓; both dark profiles blank.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "| Believes people are fundamentally good (Faith in Humanity) |   |   | ~ | ~ |   |   | ✓ | ✓ | ✓ |",
   "reasoning": "Reproduced accurately with both dark columns blank."
  },
  {
   "claim_id": "C019",
   "loglog_ids": [
    "3.3"
   ],
   "claim_text": "Sustainable/scalable guide: cognitive ~, sympathy ~, compassion ✓, altruist ✓, integrated ✓; others blank.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "| Sustainable and scalable as a moral guide | ~ |   | ~ | ✓ |   |   |   | ✓ | ✓ |",
   "reasoning": "Marks and blanks match source row."
  },
  {
   "claim_id": "C020",
   "loglog_ids": [
    "4"
   ],
   "claim_text": "Notes interpret the matrix rows and limit its scope to ideal types.",
   "claim_type": "meta",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Treat these two columns as ideal types, not categories.",
   "reasoning": "Notes explain rows and repeatedly frame profiles as ideal types."
  },
  {
   "claim_id": "C021",
   "loglog_ids": [
    "4.1"
   ],
   "claim_text": "Sympathy is '~' on modeling minds: one can pity while badly misreading; understanding helps but isn't constitutive, unlike cognitive empathy.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "you can pity someone while badly misreading them... isn't constitutive of it, the way it is for cognitive empathy.",
   "reasoning": "Mirrors note 1 including the negation about constitutive understanding."
  },
  {
   "claim_id": "C022",
   "loglog_ids": [
    "4.2"
   ],
   "claim_text": "Affective empathy's care is '~': contagion can happen involuntarily, without real concern, and simply make one want to get away.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "emotional contagion can happen involuntarily, without any real concern for the person... simply want to get away",
   "reasoning": "Matches note 2 including the negated 'without any real concern'."
  },
  {
   "claim_id": "C023",
   "loglog_ids": [
    "4.3"
   ],
   "claim_text": "'Manipulators' row is the sharpest diagnostic and essentially the psychopath's signature: cognitive empathy alone is compatible with cruelty.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "sharpest diagnostic... essentially the psychopath's signature. Cognitive empathy alone is compatible with cruelty",
   "reasoning": "Direct restatement of note 3."
  },
  {
   "claim_id": "C024",
   "loglog_ids": [
    "4.4"
   ],
   "claim_text": "Sustainability row reflects the Bloom/Singer argument (Paul Bloom's Against Empathy; Tania Singer's research), a position not a consensus; critics warn of abstract, paternalistic compassion.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "reflects the Bloom/Singer argument... which is a position, not a consensus. Critics reply that compassion... risks becoming abstract or paternalistic.",
   "reasoning": "Names, attribution, and hedge all preserved from note 4."
  },
  {
   "claim_id": "C025",
   "loglog_ids": [
    "4.5"
   ],
   "claim_text": "Boundary maintenance is the structural difference: partially merging with the other's state drives both motivational power and burnout/bias problems.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Boundary maintenance is the structural difference... partially merging with the other's state, which is what drives both its motivational power and its burnout and bias problems.",
   "reasoning": "Causal claim matches note 5 exactly."
  },
  {
   "claim_id": "C026",
   "loglog_ids": [
    "4.6"
   ],
   "claim_text": "Dark-column reading: psychopath is the cognitive column standing alone; sociopath is affect plus sympathy clamped to a narrow in-group, stripped of regulation.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "The psychopath is the cognitive column standing alone. The sociopath is affective empathy plus sympathy clamped to an in-group and stripped of regulation.",
   "reasoning": "Absolute wording matches note 10; source note 6 says 'close to' but note 10 states it plainly."
  },
  {
   "claim_id": "C027",
   "loglog_ids": [
    "4.7"
   ],
   "claim_text": "Asymmetry: almost everything the psychopath has, the sociopath shares in degraded form; the psychopath's one distinguishing possession is cold instrumental control.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "almost everything the psychopath has, the sociopath also has in degraded form... the psychopath's one distinguishing possession is cold instrumental control",
   "reasoning": "Direct restatement of note 6."
  },
  {
   "claim_id": "C028",
   "loglog_ids": [
    "4.8"
   ],
   "claim_text": "Etiology deliberately left out: psychopathy is often theorized as innate, sociopathy as environmentally acquired; causes don't describe the response's shape.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "psychopathy is often theorized as innate and temperamental, sociopathy as environmentally acquired. That is a claim about *causes*, not about the shape of the response",
   "reasoning": "Hedge 'often' retained; only 'and temperamental' compressed, no meaning change."
  },
  {
   "claim_id": "C029",
   "loglog_ids": [
    "4.9"
   ],
   "claim_text": "Clinical caveat: the two profiles aren't formal diagnoses; both fall under Antisocial Personality Disorder; the split is a contested, largely theoretical convention.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "\"psychopath\" and \"sociopath\" are not formal diagnoses. Both fall under Antisocial Personality Disorder... contested, largely theoretical convention.",
   "reasoning": "Negation and all qualifiers match note 8."
  },
  {
   "claim_id": "C030",
   "loglog_ids": [
    "4.10"
   ],
   "claim_text": "Terminology varies: some authors use 'empathic concern' roughly where the table says compassion; this table uses the neutral research sense of sympathy.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Some authors use \"empathic concern\" roughly where this table uses \"compassion\"... This table uses the more neutral research sense.",
   "reasoning": "Matches note 9; the added 'of sympathy' resolves the source's contextual antecedent."
  },
  {
   "claim_id": "C031",
   "loglog_ids": [
    "4.11"
   ],
   "claim_text": "Empath profile: affective column maxed and unregulated, failing boundary, scope, and scalability; inherits the sociopath's distortions, so not the moral ideal.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "the empath is the affective column maxed out and unregulated... failing on boundary, scope, and scalability... inherits the sociopath's distortions, so it is not the moral ideal.",
   "reasoning": "Matches note 10 including the negated conclusion."
  },
  {
   "claim_id": "C032",
   "loglog_ids": [
    "4.12"
   ],
   "claim_text": "Altruist profile: compassion column embodied, matching the research 'Light Triad' (Kaufman et al., 2019).",
   "claim_type": "name_or_entity",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "The altruist is the compassion column embodied, matching the research \"Light Triad\"... from Kaufman et al., 2019",
   "reasoning": "Attribution and year match note 10 exactly."
  },
  {
   "claim_id": "C033",
   "loglog_ids": [
    "4.13"
   ],
   "claim_text": "Integrated ideal: the only column scoring well across every block, including the 'present in neither' rows; true opposite of both dark profiles.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "The integrated ideal is the only column that scores well across every block, including the \"present in neither\" rows, so it is the true opposite of both dark profiles at once.",
   "reasoning": "Direct restatement of note 10."
  },
  {
   "claim_id": "C034",
   "loglog_ids": [
    "4.14"
   ],
   "claim_text": "Kantianism row is essentially the inverse of the manipulators row; Humanism overlaps the caring and beyond-the-in-group rows.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "\"Treats people as ends, not means\" (Kantianism) is essentially the inverse of the \"manipulators\" row... \"Values each person's dignity and worth\" (Humanism) overlaps with the caring and beyond-the-in-group rows.",
   "reasoning": "Matches note 11, negation preserved."
  },
  {
   "claim_id": "C035",
   "loglog_ids": [
    "4.15"
   ],
   "claim_text": "Only Faith in Humanity adds a genuinely new dimension, an attitude rather than an empathy component; both dark profiles score blank there.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Only \"Believes people are fundamentally good\" (Faith in Humanity) adds a genuinely new dimension... which is why both dark profiles score blank",
   "reasoning": "Matches note 11 including 'Only' and the blank dark profiles."
  }
 ],
 "metrics": {
  "total_claims": 35,
  "supported": 35,
  "partially_supported": 0,
  "unverifiable": 0,
  "contradicted": 0,
  "critical_errors": 0,
  "faithfulness_precision": 1.0
 },
 "fail_list": []
}
```

## Judge Cov (coverage), opencode-go/deepseek-v4.1-flash

```json
{
 "judge": "coverage",
 "judge_version": "1.0.0",
 "model": "opencode-go/deepseek-v4.1-flash (opencode) scripted pipeline 2026-09-15",
 "source_id": "08_empathy_sympathy_compassion_matrix",
 "key_points": [
  {
   "point_id": "K01",
   "point_text": "Central purpose: a feature matrix comparing four components (cognitive empathy, affective empathy, sympathy, compassion) against five whole-person profiles (psychopath, sociopath, empath, altruist, integrated ideal), the profiles arranged darkest to lightest.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L001",
    "L002"
   ],
   "evidence_quote": "Feature matrix contrasts cognitive and affective empathy, sympathy, and compassion across five profiles from psychopath to integrated ideal.",
   "reasoning": "L002 names all four components and the five profiles from psychopath to integrated ideal, matching the organizing thesis. The darkest-to-lightest ordering is implicit in 'from psychopath to integrated ideal' and the source mapping at L001."
  },
  {
   "point_id": "K02",
   "point_text": "Rows are ordered by the two dark profiles' contrast and split into four blocks separated by blank dividers: present in both, psychopath only, sociopath only, and neither.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L003",
    "L008",
    "L017"
   ],
   "evidence_quote": "Theme: Cold-control block: rows present in both dark profiles, plus the psychopath-only control row. ... Affective-care block: rows the sociopath has and the psychopath lacks ... Neither-dark block",
   "reasoning": "The three explicit themes plus the interpretive notes block (L021) reproduce the block structure: present-in-both/psychopath-only (L003), sociopath-only (L008), and neither (L017)."
  },
  {
   "point_id": "K03",
   "point_text": "Sympathy gets a partial (~) on modeling the other's mind because you can pity someone while badly misreading them; accurate understanding helps sympathy but is not constitutive of it, unlike cognitive empathy.",
   "weight": "Nice to have",
   "presence": "Present",
   "loglog_ids": [
    "L022"
   ],
   "evidence_quote": "Sympathy is '~' on modeling minds: one can pity while badly misreading; understanding helps but isn't constitutive, unlike cognitive empathy.",
   "reasoning": "L022 captures the partial mark, the pity-with-misreading reason, and the contrast with cognitive empathy."
  },
  {
   "point_id": "K04",
   "point_text": "Affective empathy gets a partial (~) on capacity to care because emotional contagion can occur involuntarily without real concern, e.g., catching someone's anxiety and wanting to get away from them.",
   "weight": "Nice to have",
   "presence": "Present",
   "loglog_ids": [
    "L023"
   ],
   "evidence_quote": "Affective empathy's care is '~': contagion can happen involuntarily, without real concern, and simply make one want to get away.",
   "reasoning": "L023 preserves the partial mark, the involuntary-contagion rationale, and the get-away example."
  },
  {
   "point_id": "K05",
   "point_text": "The manipulators/con-artist row is the sharpest diagnostic for the cognitive/affective split and is essentially the psychopath's signature: cognitive empathy alone is compatible with cruelty, since a con artist models minds precisely without resonating with or caring about them.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L006",
    "L024",
    "L040"
   ],
   "evidence_quote": "'Manipulators' row is the sharpest diagnostic and essentially the psychopath's signature: cognitive empathy alone is compatible with cruelty.",
   "reasoning": "L024 states the diagnostic/signature claim and the cognitive-empathy-alone-compatible-with-cruelty point; L040 reasons it supports the split; L006 records the row's scores."
  },
  {
   "point_id": "K06",
   "point_text": "The sustainable-and-scalable row reflects the Bloom/Singer argument (Paul Bloom's Against Empathy and Tania Singer's compassion-training research); it is a position, not a consensus, and critics reply that compassion without empathic grounding risks becoming abstract or paternalistic.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L025",
    "L041"
   ],
   "evidence_quote": "Sustainability row reflects the Bloom/Singer argument (Paul Bloom's Against Empathy; Tania Singer's research), a position not a consensus; critics warn of abstract, paternalistic compassion.",
   "reasoning": "L025 names both authors and works, flags it as a position not a consensus, and preserves the critics' abstract/paternalistic warning. The contested qualifier is intact."
  },
  {
   "point_id": "K07",
   "point_text": "Boundary maintenance is the structural difference between affective empathy and everything else: affective empathy means partially merging with the other's state, which drives both its motivational power and its burnout and bias problems.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L026",
    "L042",
    "L043"
   ],
   "evidence_quote": "Boundary maintenance is the structural difference: partially merging with the other's state drives both motivational power and burnout/bias problems.",
   "reasoning": "L026 preserves the structural-difference claim and both consequences; L042/L043 tie it to the motivation and burnout/bias rows."
  },
  {
   "point_id": "K08",
   "point_text": "Reading the two dark profiles as columns: the psychopath is close to the cognitive-empathy column standing alone (accurate modeling with affective and caring machinery deleted), while the sociopath is close to affective empathy and sympathy clamped to a narrow in-group and stripped of regulation; the psychopath's one distinguishing possession is cold instrumental control, while a whole cluster of affective and caring rows belongs to the sociopath and not the psychopath.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L027",
    "L028",
    "L044"
   ],
   "evidence_quote": "psychopath is the cognitive column standing alone; sociopath is affect plus sympathy clamped to a narrow in-group, stripped of regulation. ... almost everything the psychopath has, the sociopath shares in degraded form; the psychopath's one distinguishing possession is cold instrumental control.",
   "reasoning": "L027 and L028 together capture both column readings, the in-group clamping, stripping of regulation, and the asymmetry of cold instrumental control as the psychopath's one possession. The caring/affective cluster belonging to the sociopath is implicit in the block themes (L008) and degraded-form statement."
  },
  {
   "point_id": "K09",
   "point_text": "Etiology is deliberately excluded as a row: psychopathy is often theorized as innate/temperamental and sociopathy as environmentally acquired, but that concerns causes rather than the shape of the response, so it does not belong in a feature table and would muddy the logic.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L029"
   ],
   "evidence_quote": "Etiology deliberately left out: psychopathy is often theorized as innate, sociopathy as environmentally acquired; causes don't describe the response's shape.",
   "reasoning": "L029 preserves the deliberate exclusion, both etiological theories, and the cause-versus-shape justification."
  },
  {
   "point_id": "K10",
   "point_text": "Clinical caveat: 'psychopath' and 'sociopath' are not formal diagnoses; both fall under Antisocial Personality Disorder, and the split between them is a contested, largely theoretical convention. Treat the two columns as ideal types, not categories.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L021",
    "L030"
   ],
   "evidence_quote": "Clinical caveat: the two profiles aren't formal diagnoses; both fall under Antisocial Personality Disorder; the split is a contested, largely theoretical convention.",
   "reasoning": "L030 preserves all three qualifiers; L021 frames the whole notes block as limiting scope to ideal types."
  },
  {
   "point_id": "K11",
   "point_text": "Terminology caveat: usage varies across the literature, some authors use 'empathic concern' roughly where this table uses 'compassion', and pop-psych usage (e.g., Brené Brown) treats 'sympathy' as inherently distancing; this table uses the more neutral research sense.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L031"
   ],
   "evidence_quote": "Terminology varies: some authors use 'empathic concern' roughly where the table says compassion; this table uses the neutral research sense of sympathy.",
   "reasoning": "L031 preserves the variation-in-usage claim, the empathic-concern/compassion overlap, and the neutral-research-sense resolution. The Brené Brown pop-psych example is omitted, but it is an illustrative aside rather than a load-bearing condition; the core caveat and its resolution survive intact."
  },
  {
   "point_id": "K12",
   "point_text": "The empath column is the affective column maxed out and unregulated, which is why it lights up emotion-sharing, contagion, and vividness bias while failing on boundary, scope, and scalability; it is the opposite of the psychopath's coldness but inherits the sociopath's distortions, so it is not the moral ideal.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L032"
   ],
   "evidence_quote": "Empath profile: affective column maxed and unregulated, failing boundary, scope, and scalability; inherits the sociopath's distortions, so not the moral ideal.",
   "reasoning": "L032 preserves the maxed/unregulated affective reading, the failures on boundary/scope/scalability, the inherited distortions, and the not-the-moral-ideal conclusion."
  },
  {
   "point_id": "K13",
   "point_text": "The altruist column is the compassion column embodied and matches the research 'Light Triad' (Kantianism, Humanism, and Faith in Humanity, from Kaufman et al., 2019).",
   "weight": "Nice to have",
   "presence": "Present",
   "loglog_ids": [
    "L033",
    "L015",
    "L016",
    "L019"
   ],
   "evidence_quote": "Altruist profile: compassion column embodied, matching the research 'Light Triad' (Kaufman et al., 2019).",
   "reasoning": "L033 preserves the compassion-embodied mapping, the Light Triad label, and the Kaufman attribution. The three Light Triad components are not enumerated there but appear as distinct rows (Kantianism L015, Humanism L016, Faith in Humanity L019), so the meaning is available."
  },
  {
   "point_id": "K14",
   "point_text": "The integrated ideal is the only column that scores well across every block, including the 'present in neither' rows, so it is the true opposite of both dark profiles at once.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L034"
   ],
   "evidence_quote": "Integrated ideal: the only column scoring well across every block, including the 'present in neither' rows; true opposite of both dark profiles.",
   "reasoning": "L034 preserves the uniqueness claim, the inclusion of the neither-dark rows, and the true-opposite conclusion."
  },
  {
   "point_id": "K15",
   "point_text": "The three Light Triad rows partly restate earlier rows: Kantianism is essentially the inverse of the manipulators row, Humanism overlaps the caring and beyond-the-in-group rows, and only Faith in Humanity adds a genuinely new dimension (an attitude rather than an empathy component), which is why both dark profiles score blank on it.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L035",
    "L036",
    "L038",
    "L039"
   ],
   "evidence_quote": "Kantianism row is essentially the inverse of the manipulators row; Humanism overlaps the caring and beyond-the-in-group rows. ... Only Faith in Humanity adds a genuinely new dimension, an attitude rather than an empathy component; both dark profiles score blank there.",
   "reasoning": "L035/L036 preserve the redundancy claims and the novel-dimension point; L038/L039 cross-link the restatements to the manipulators and caring/in-group rows."
  }
 ],
 "metrics": {
  "total_points": 15,
  "must_have_total": 12,
  "must_have_present": 12,
  "must_have_partial": 0,
  "must_have_missing": 0,
  "overall_present": 15,
  "must_recall": 1.0,
  "overall_recall": 1.0
 },
 "missing_list": []
}
```

## Judge F (faithfulness), opencode-go/deepseek-v4.1-flash

```json
{
 "judge": "faithfulness",
 "judge_version": "1.0.0",
 "model": "opencode-go/deepseek-v4.1-flash (opencode) scripted pipeline 2026-09-15",
 "source_id": "08_empathy_sympathy_compassion_matrix",
 "claims": [
  {
   "claim_id": "C001",
   "loglog_ids": [
    "0"
   ],
   "claim_text": "Feature matrix contrasts cognitive and affective empathy, sympathy, and compassion across five profiles from psychopath to integrated ideal.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "The four component columns (cognitive and affective empathy, sympathy, compassion)... psychopath, sociopath, empath, altruist, and the integrated ideal.",
   "reasoning": "Source names these four components and five profiles in the same order."
  },
  {
   "claim_id": "C002",
   "loglog_ids": [
    "1"
   ],
   "claim_text": "Cold-control block groups rows present in both dark profiles plus the psychopath-only control row.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "four blocks... present in both, in the psychopath only, in the sociopath only, and in neither.",
   "reasoning": "Rows 1-4 match the present-in-both block plus the psychopath-only row; note 6 calls that cold instrumental control."
  },
  {
   "claim_id": "C003",
   "loglog_ids": [
    "1.1"
   ],
   "claim_text": "Accurate modeling: cognitive ✓, affective ~, sympathy ~, compassion ✓; psychopath ✓, sociopath ~, empath ~, altruist ✓, integrated ✓.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "| Accurately modeling the other's mental state | ✓ | ~ | ~ | ✓ | ✓ | ~ | ~ | ✓ | ✓ |",
   "reasoning": "Every mark matches the source table row exactly."
  },
  {
   "claim_id": "C004",
   "loglog_ids": [
    "1.2"
   ],
   "claim_text": "Boundary kept: cognitive ✓, affective blank, sympathy ✓, compassion ✓; psychopath ✓, sociopath ~, empath blank, altruist ✓, integrated ✓.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "| Maintains self/other boundary | ✓ |   | ✓ | ✓ | ✓ | ~ |   | ✓ | ✓ |",
   "reasoning": "Marks and blanks match the source row precisely."
  },
  {
   "claim_id": "C005",
   "loglog_ids": [
    "1.3"
   ],
   "claim_text": "Manipulators row: cognitive ✓ only; psychopath ✓, sociopath ~, all others blank.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "| Can exist in manipulators / con artists | ✓ |   |   |   | ✓ | ~ |   |   |   |",
   "reasoning": "Correctly reports cognitive ✓, psychopath ✓, sociopath ~, rest blank."
  },
  {
   "claim_id": "C006",
   "loglog_ids": [
    "1.4"
   ],
   "claim_text": "Controlled/instrumental, not reactive/impulsive: cognitive ✓, sympathy ~, compassion ✓; psychopath ✓, altruist ✓, integrated ✓; affective, sociopath, empath blank.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "| Controlled / instrumental rather than reactive / impulsive | ✓ |   | ~ | ✓ | ✓ |   |   | ✓ | ✓ |",
   "reasoning": "Marks and blanks match the source row; negation kept intact."
  },
  {
   "claim_id": "C007",
   "loglog_ids": [
    "2"
   ],
   "claim_text": "Affective-care block: rows the sociopath has and the psychopath lacks, mostly partial marks.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "four blocks... in the sociopath only...",
   "reasoning": "Rows 5-12 are the sociopath-only block, psychopath blank, dominantly ~ marks."
  },
  {
   "claim_id": "C008",
   "loglog_ids": [
    "2.1"
   ],
   "claim_text": "Sharing/mirroring emotion: affective ✓; sociopath ~, empath ✓, altruist ~, integrated ✓; others blank.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "| Actually sharing / mirroring the emotion |   | ✓ |   |   |   | ~ | ✓ | ~ | ✓ |",
   "reasoning": "All marks and blanks match the source row."
  },
  {
   "claim_id": "C009",
   "loglog_ids": [
    "2.2"
   ],
   "claim_text": "Capacity to care at all: affective ~, sympathy ✓, compassion ✓; sociopath ✓, empath ✓, altruist ✓, integrated ✓; psychopath blank.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "| Capacity to genuinely care about the person *at all* |   | ~ | ✓ | ✓ |   | ✓ | ✓ | ✓ | ✓ |",
   "reasoning": "Marks match source exactly, including psychopath blank."
  },
  {
   "claim_id": "C010",
   "loglog_ids": [
    "2.3"
   ],
   "claim_text": "Motivation to help/act: affective ~, sympathy ~, compassion ✓; sociopath ~, empath ~, altruist ✓, integrated ✓; psychopath blank.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "| Motivation to help or act |   | ~ | ~ | ✓ |   | ~ | ~ | ✓ | ✓ |",
   "reasoning": "Full row reproduced accurately."
  },
  {
   "claim_id": "C011",
   "loglog_ids": [
    "2.4"
   ],
   "claim_text": "Guilt/remorse after harm: empath ✓; affective ~, sympathy ~, compassion ~, sociopath ~, altruist ~, integrated ~; cognitive and psychopath blank.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "| Produces guilt / remorse after causing harm |   | ~ | ~ | ~ |   | ~ | ✓ | ~ | ~ |",
   "reasoning": "Only empath ✓, all listed ~ marks and two blanks match source."
  },
  {
   "claim_id": "C012",
   "loglog_ids": [
    "2.5"
   ],
   "claim_text": "Contagion/burnout risk: affective ✓, empath ✓; sympathy ~, sociopath ~, integrated ~; others blank.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "| Risk of emotional contagion and burnout |   | ✓ | ~ |   |   | ~ | ✓ |   | ~ |",
   "reasoning": "Marks and blanks match source row."
  },
  {
   "claim_id": "C013",
   "loglog_ids": [
    "2.6"
   ],
   "claim_text": "Vivid/similar bias: affective ✓, sociopath ✓, empath ✓; cognitive ~, sympathy ~, integrated ~; others blank.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "| Biased toward vivid, similar individuals | ~ | ✓ | ~ |   |   | ✓ | ✓ |   | ~ |",
   "reasoning": "Reproduced correctly, including altruist blank."
  },
  {
   "claim_id": "C014",
   "loglog_ids": [
    "2.7"
   ],
   "claim_text": "Ends, not means (Kantianism): compassion ✓, empath ✓, altruist ✓, integrated ✓; affective ~, sympathy ~, sociopath ~; cognitive and psychopath blank.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "| Treats people as ends, not means (Kantianism) |   | ~ | ~ | ✓ |   | ~ | ✓ | ✓ | ✓ |",
   "reasoning": "Negation and all marks preserved correctly."
  },
  {
   "claim_id": "C015",
   "loglog_ids": [
    "2.8"
   ],
   "claim_text": "Dignity and worth (Humanism): sympathy ✓, compassion ✓, empath ✓, altruist ✓, integrated ✓; affective ~, sociopath ~; cognitive and psychopath blank.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "| Values each person's dignity and worth (Humanism) |   | ~ | ✓ | ✓ |   | ~ | ✓ | ✓ | ✓ |",
   "reasoning": "Rows marks match source exactly."
  },
  {
   "claim_id": "C016",
   "loglog_ids": [
    "3"
   ],
   "claim_text": "Neither-dark block: beyond in-group, faith, and scalability rows, blank for both dark profiles.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "four blocks... in neither.",
   "reasoning": "Rows 13-15 are the neither block; psychopath and sociopath are blank there."
  },
  {
   "claim_id": "C017",
   "loglog_ids": [
    "3.1"
   ],
   "claim_text": "Beyond a vivid/similar in-group: sympathy ~, compassion ✓, altruist ✓, integrated ✓; all others blank.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "| Concern reaches *beyond* a vivid / similar in-group |   |   | ~ | ✓ |   |   |   | ✓ | ✓ |",
   "reasoning": "Marks match, including both dark profile blanks."
  },
  {
   "claim_id": "C018",
   "loglog_ids": [
    "3.2"
   ],
   "claim_text": "Fundamentally good (Faith in Humanity): sympathy ~, compassion ~, empath ✓, altruist ✓, integrated ✓; both dark profiles blank.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "| Believes people are fundamentally good (Faith in Humanity) |   |   | ~ | ~ |   |   | ✓ | ✓ | ✓ |",
   "reasoning": "Reproduced accurately with both dark columns blank."
  },
  {
   "claim_id": "C019",
   "loglog_ids": [
    "3.3"
   ],
   "claim_text": "Sustainable/scalable guide: cognitive ~, sympathy ~, compassion ✓, altruist ✓, integrated ✓; others blank.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "| Sustainable and scalable as a moral guide | ~ |   | ~ | ✓ |   |   |   | ✓ | ✓ |",
   "reasoning": "Marks and blanks match source row."
  },
  {
   "claim_id": "C020",
   "loglog_ids": [
    "4"
   ],
   "claim_text": "Notes interpret the matrix rows and limit its scope to ideal types.",
   "claim_type": "meta",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Treat these two columns as ideal types, not categories.",
   "reasoning": "Notes explain rows and repeatedly frame profiles as ideal types."
  },
  {
   "claim_id": "C021",
   "loglog_ids": [
    "4.1"
   ],
   "claim_text": "Sympathy is '~' on modeling minds: one can pity while badly misreading; understanding helps but isn't constitutive, unlike cognitive empathy.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "you can pity someone while badly misreading them... isn't constitutive of it, the way it is for cognitive empathy.",
   "reasoning": "Mirrors note 1 including the negation about constitutive understanding."
  },
  {
   "claim_id": "C022",
   "loglog_ids": [
    "4.2"
   ],
   "claim_text": "Affective empathy's care is '~': contagion can happen involuntarily, without real concern, and simply make one want to get away.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "emotional contagion can happen involuntarily, without any real concern for the person... simply want to get away",
   "reasoning": "Matches note 2 including the negated 'without any real concern'."
  },
  {
   "claim_id": "C023",
   "loglog_ids": [
    "4.3"
   ],
   "claim_text": "'Manipulators' row is the sharpest diagnostic and essentially the psychopath's signature: cognitive empathy alone is compatible with cruelty.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "sharpest diagnostic... essentially the psychopath's signature. Cognitive empathy alone is compatible with cruelty",
   "reasoning": "Direct restatement of note 3."
  },
  {
   "claim_id": "C024",
   "loglog_ids": [
    "4.4"
   ],
   "claim_text": "Sustainability row reflects the Bloom/Singer argument (Paul Bloom's Against Empathy; Tania Singer's research), a position not a consensus; critics warn of abstract, paternalistic compassion.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "reflects the Bloom/Singer argument... which is a position, not a consensus. Critics reply that compassion... risks becoming abstract or paternalistic.",
   "reasoning": "Names, attribution, and hedge all preserved from note 4."
  },
  {
   "claim_id": "C025",
   "loglog_ids": [
    "4.5"
   ],
   "claim_text": "Boundary maintenance is the structural difference: partially merging with the other's state drives both motivational power and burnout/bias problems.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Boundary maintenance is the structural difference... partially merging with the other's state, which is what drives both its motivational power and its burnout and bias problems.",
   "reasoning": "Causal claim matches note 5 exactly."
  },
  {
   "claim_id": "C026",
   "loglog_ids": [
    "4.6"
   ],
   "claim_text": "Dark-column reading: psychopath is the cognitive column standing alone; sociopath is affect plus sympathy clamped to a narrow in-group, stripped of regulation.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "The psychopath is the cognitive column standing alone. The sociopath is affective empathy plus sympathy clamped to an in-group and stripped of regulation.",
   "reasoning": "Absolute wording matches note 10; source note 6 says 'close to' but note 10 states it plainly."
  },
  {
   "claim_id": "C027",
   "loglog_ids": [
    "4.7"
   ],
   "claim_text": "Asymmetry: almost everything the psychopath has, the sociopath shares in degraded form; the psychopath's one distinguishing possession is cold instrumental control.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "almost everything the psychopath has, the sociopath also has in degraded form... the psychopath's one distinguishing possession is cold instrumental control",
   "reasoning": "Direct restatement of note 6."
  },
  {
   "claim_id": "C028",
   "loglog_ids": [
    "4.8"
   ],
   "claim_text": "Etiology deliberately left out: psychopathy is often theorized as innate, sociopathy as environmentally acquired; causes don't describe the response's shape.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "psychopathy is often theorized as innate and temperamental, sociopathy as environmentally acquired. That is a claim about *causes*, not about the shape of the response",
   "reasoning": "Hedge 'often' retained; only 'and temperamental' compressed, no meaning change."
  },
  {
   "claim_id": "C029",
   "loglog_ids": [
    "4.9"
   ],
   "claim_text": "Clinical caveat: the two profiles aren't formal diagnoses; both fall under Antisocial Personality Disorder; the split is a contested, largely theoretical convention.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "\"psychopath\" and \"sociopath\" are not formal diagnoses. Both fall under Antisocial Personality Disorder... contested, largely theoretical convention.",
   "reasoning": "Negation and all qualifiers match note 8."
  },
  {
   "claim_id": "C030",
   "loglog_ids": [
    "4.10"
   ],
   "claim_text": "Terminology varies: some authors use 'empathic concern' roughly where the table says compassion; this table uses the neutral research sense of sympathy.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Some authors use \"empathic concern\" roughly where this table uses \"compassion\"... This table uses the more neutral research sense.",
   "reasoning": "Matches note 9; the added 'of sympathy' resolves the source's contextual antecedent."
  },
  {
   "claim_id": "C031",
   "loglog_ids": [
    "4.11"
   ],
   "claim_text": "Empath profile: affective column maxed and unregulated, failing boundary, scope, and scalability; inherits the sociopath's distortions, so not the moral ideal.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "the empath is the affective column maxed out and unregulated... failing on boundary, scope, and scalability... inherits the sociopath's distortions, so it is not the moral ideal.",
   "reasoning": "Matches note 10 including the negated conclusion."
  },
  {
   "claim_id": "C032",
   "loglog_ids": [
    "4.12"
   ],
   "claim_text": "Altruist profile: compassion column embodied, matching the research 'Light Triad' (Kaufman et al., 2019).",
   "claim_type": "name_or_entity",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "The altruist is the compassion column embodied, matching the research \"Light Triad\"... from Kaufman et al., 2019",
   "reasoning": "Attribution and year match note 10 exactly."
  },
  {
   "claim_id": "C033",
   "loglog_ids": [
    "4.13"
   ],
   "claim_text": "Integrated ideal: the only column scoring well across every block, including the 'present in neither' rows; true opposite of both dark profiles.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "The integrated ideal is the only column that scores well across every block, including the \"present in neither\" rows, so it is the true opposite of both dark profiles at once.",
   "reasoning": "Direct restatement of note 10."
  },
  {
   "claim_id": "C034",
   "loglog_ids": [
    "4.14"
   ],
   "claim_text": "Kantianism row is essentially the inverse of the manipulators row; Humanism overlaps the caring and beyond-the-in-group rows.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "\"Treats people as ends, not means\" (Kantianism) is essentially the inverse of the \"manipulators\" row... \"Values each person's dignity and worth\" (Humanism) overlaps with the caring and beyond-the-in-group rows.",
   "reasoning": "Matches note 11, negation preserved."
  },
  {
   "claim_id": "C035",
   "loglog_ids": [
    "4.15"
   ],
   "claim_text": "Only Faith in Humanity adds a genuinely new dimension, an attitude rather than an empathy component; both dark profiles score blank there.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Only \"Believes people are fundamentally good\" (Faith in Humanity) adds a genuinely new dimension... which is why both dark profiles score blank",
   "reasoning": "Matches note 11 including 'Only' and the blank dark profiles."
  }
 ],
 "metrics": {
  "total_claims": 35,
  "supported": 35,
  "partially_supported": 0,
  "unverifiable": 0,
  "contradicted": 0,
  "critical_errors": 0,
  "faithfulness_precision": 1.0
 },
 "fail_list": []
}
```

## Judge Cov (coverage), opencode-go/deepseek-v4.1-flash

```json
{
 "judge": "coverage",
 "judge_version": "1.0.0",
 "model": "opencode-go/deepseek-v4.1-flash (opencode) scripted pipeline 2026-09-15",
 "source_id": "08_empathy_sympathy_compassion_matrix",
 "key_points": [
  {
   "point_id": "K01",
   "point_text": "Central purpose: a feature matrix comparing four components (cognitive empathy, affective empathy, sympathy, compassion) against five whole-person profiles (psychopath, sociopath, empath, altruist, integrated ideal), the profiles arranged darkest to lightest.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L001",
    "L002"
   ],
   "evidence_quote": "Feature matrix contrasts cognitive and affective empathy, sympathy, and compassion across five profiles from psychopath to integrated ideal.",
   "reasoning": "L002 names all four components and the five profiles from psychopath to integrated ideal, matching the organizing thesis. The darkest-to-lightest ordering is implicit in 'from psychopath to integrated ideal' and the source mapping at L001."
  },
  {
   "point_id": "K02",
   "point_text": "Rows are ordered by the two dark profiles' contrast and split into four blocks separated by blank dividers: present in both, psychopath only, sociopath only, and neither.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L003",
    "L008",
    "L017"
   ],
   "evidence_quote": "Theme: Cold-control block: rows present in both dark profiles, plus the psychopath-only control row. ... Affective-care block: rows the sociopath has and the psychopath lacks ... Neither-dark block",
   "reasoning": "The three explicit themes plus the interpretive notes block (L021) reproduce the block structure: present-in-both/psychopath-only (L003), sociopath-only (L008), and neither (L017)."
  },
  {
   "point_id": "K03",
   "point_text": "Sympathy gets a partial (~) on modeling the other's mind because you can pity someone while badly misreading them; accurate understanding helps sympathy but is not constitutive of it, unlike cognitive empathy.",
   "weight": "Nice to have",
   "presence": "Present",
   "loglog_ids": [
    "L022"
   ],
   "evidence_quote": "Sympathy is '~' on modeling minds: one can pity while badly misreading; understanding helps but isn't constitutive, unlike cognitive empathy.",
   "reasoning": "L022 captures the partial mark, the pity-with-misreading reason, and the contrast with cognitive empathy."
  },
  {
   "point_id": "K04",
   "point_text": "Affective empathy gets a partial (~) on capacity to care because emotional contagion can occur involuntarily without real concern, e.g., catching someone's anxiety and wanting to get away from them.",
   "weight": "Nice to have",
   "presence": "Present",
   "loglog_ids": [
    "L023"
   ],
   "evidence_quote": "Affective empathy's care is '~': contagion can happen involuntarily, without real concern, and simply make one want to get away.",
   "reasoning": "L023 preserves the partial mark, the involuntary-contagion rationale, and the get-away example."
  },
  {
   "point_id": "K05",
   "point_text": "The manipulators/con-artist row is the sharpest diagnostic for the cognitive/affective split and is essentially the psychopath's signature: cognitive empathy alone is compatible with cruelty, since a con artist models minds precisely without resonating with or caring about them.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L006",
    "L024",
    "L040"
   ],
   "evidence_quote": "'Manipulators' row is the sharpest diagnostic and essentially the psychopath's signature: cognitive empathy alone is compatible with cruelty.",
   "reasoning": "L024 states the diagnostic/signature claim and the cognitive-empathy-alone-compatible-with-cruelty point; L040 reasons it supports the split; L006 records the row's scores."
  },
  {
   "point_id": "K06",
   "point_text": "The sustainable-and-scalable row reflects the Bloom/Singer argument (Paul Bloom's Against Empathy and Tania Singer's compassion-training research); it is a position, not a consensus, and critics reply that compassion without empathic grounding risks becoming abstract or paternalistic.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L025",
    "L041"
   ],
   "evidence_quote": "Sustainability row reflects the Bloom/Singer argument (Paul Bloom's Against Empathy; Tania Singer's research), a position not a consensus; critics warn of abstract, paternalistic compassion.",
   "reasoning": "L025 names both authors and works, flags it as a position not a consensus, and preserves the critics' abstract/paternalistic warning. The contested qualifier is intact."
  },
  {
   "point_id": "K07",
   "point_text": "Boundary maintenance is the structural difference between affective empathy and everything else: affective empathy means partially merging with the other's state, which drives both its motivational power and its burnout and bias problems.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L026",
    "L042",
    "L043"
   ],
   "evidence_quote": "Boundary maintenance is the structural difference: partially merging with the other's state drives both motivational power and burnout/bias problems.",
   "reasoning": "L026 preserves the structural-difference claim and both consequences; L042/L043 tie it to the motivation and burnout/bias rows."
  },
  {
   "point_id": "K08",
   "point_text": "Reading the two dark profiles as columns: the psychopath is close to the cognitive-empathy column standing alone (accurate modeling with affective and caring machinery deleted), while the sociopath is close to affective empathy and sympathy clamped to a narrow in-group and stripped of regulation; the psychopath's one distinguishing possession is cold instrumental control, while a whole cluster of affective and caring rows belongs to the sociopath and not the psychopath.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L027",
    "L028",
    "L044"
   ],
   "evidence_quote": "psychopath is the cognitive column standing alone; sociopath is affect plus sympathy clamped to a narrow in-group, stripped of regulation. ... almost everything the psychopath has, the sociopath shares in degraded form; the psychopath's one distinguishing possession is cold instrumental control.",
   "reasoning": "L027 and L028 together capture both column readings, the in-group clamping, stripping of regulation, and the asymmetry of cold instrumental control as the psychopath's one possession. The caring/affective cluster belonging to the sociopath is implicit in the block themes (L008) and degraded-form statement."
  },
  {
   "point_id": "K09",
   "point_text": "Etiology is deliberately excluded as a row: psychopathy is often theorized as innate/temperamental and sociopathy as environmentally acquired, but that concerns causes rather than the shape of the response, so it does not belong in a feature table and would muddy the logic.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L029"
   ],
   "evidence_quote": "Etiology deliberately left out: psychopathy is often theorized as innate, sociopathy as environmentally acquired; causes don't describe the response's shape.",
   "reasoning": "L029 preserves the deliberate exclusion, both etiological theories, and the cause-versus-shape justification."
  },
  {
   "point_id": "K10",
   "point_text": "Clinical caveat: 'psychopath' and 'sociopath' are not formal diagnoses; both fall under Antisocial Personality Disorder, and the split between them is a contested, largely theoretical convention. Treat the two columns as ideal types, not categories.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L021",
    "L030"
   ],
   "evidence_quote": "Clinical caveat: the two profiles aren't formal diagnoses; both fall under Antisocial Personality Disorder; the split is a contested, largely theoretical convention.",
   "reasoning": "L030 preserves all three qualifiers; L021 frames the whole notes block as limiting scope to ideal types."
  },
  {
   "point_id": "K11",
   "point_text": "Terminology caveat: usage varies across the literature, some authors use 'empathic concern' roughly where this table uses 'compassion', and pop-psych usage (e.g., Brené Brown) treats 'sympathy' as inherently distancing; this table uses the more neutral research sense.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L031"
   ],
   "evidence_quote": "Terminology varies: some authors use 'empathic concern' roughly where the table says compassion; this table uses the neutral research sense of sympathy.",
   "reasoning": "L031 preserves the variation-in-usage claim, the empathic-concern/compassion overlap, and the neutral-research-sense resolution. The Brené Brown pop-psych example is omitted, but it is an illustrative aside rather than a load-bearing condition; the core caveat and its resolution survive intact."
  },
  {
   "point_id": "K12",
   "point_text": "The empath column is the affective column maxed out and unregulated, which is why it lights up emotion-sharing, contagion, and vividness bias while failing on boundary, scope, and scalability; it is the opposite of the psychopath's coldness but inherits the sociopath's distortions, so it is not the moral ideal.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L032"
   ],
   "evidence_quote": "Empath profile: affective column maxed and unregulated, failing boundary, scope, and scalability; inherits the sociopath's distortions, so not the moral ideal.",
   "reasoning": "L032 preserves the maxed/unregulated affective reading, the failures on boundary/scope/scalability, the inherited distortions, and the not-the-moral-ideal conclusion."
  },
  {
   "point_id": "K13",
   "point_text": "The altruist column is the compassion column embodied and matches the research 'Light Triad' (Kantianism, Humanism, and Faith in Humanity, from Kaufman et al., 2019).",
   "weight": "Nice to have",
   "presence": "Present",
   "loglog_ids": [
    "L033",
    "L015",
    "L016",
    "L019"
   ],
   "evidence_quote": "Altruist profile: compassion column embodied, matching the research 'Light Triad' (Kaufman et al., 2019).",
   "reasoning": "L033 preserves the compassion-embodied mapping, the Light Triad label, and the Kaufman attribution. The three Light Triad components are not enumerated there but appear as distinct rows (Kantianism L015, Humanism L016, Faith in Humanity L019), so the meaning is available."
  },
  {
   "point_id": "K14",
   "point_text": "The integrated ideal is the only column that scores well across every block, including the 'present in neither' rows, so it is the true opposite of both dark profiles at once.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L034"
   ],
   "evidence_quote": "Integrated ideal: the only column scoring well across every block, including the 'present in neither' rows; true opposite of both dark profiles.",
   "reasoning": "L034 preserves the uniqueness claim, the inclusion of the neither-dark rows, and the true-opposite conclusion."
  },
  {
   "point_id": "K15",
   "point_text": "The three Light Triad rows partly restate earlier rows: Kantianism is essentially the inverse of the manipulators row, Humanism overlaps the caring and beyond-the-in-group rows, and only Faith in Humanity adds a genuinely new dimension (an attitude rather than an empathy component), which is why both dark profiles score blank on it.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L035",
    "L036",
    "L038",
    "L039"
   ],
   "evidence_quote": "Kantianism row is essentially the inverse of the manipulators row; Humanism overlaps the caring and beyond-the-in-group rows. ... Only Faith in Humanity adds a genuinely new dimension, an attitude rather than an empathy component; both dark profiles score blank there.",
   "reasoning": "L035/L036 preserve the redundancy claims and the novel-dimension point; L038/L039 cross-link the restatements to the manipulators and caring/in-group rows."
  }
 ],
 "metrics": {
  "total_points": 15,
  "must_have_total": 12,
  "must_have_present": 12,
  "must_have_partial": 0,
  "must_have_missing": 0,
  "overall_present": 15,
  "must_recall": 1.0,
  "overall_recall": 1.0
 },
 "missing_list": []
}
```

## Judge Con (concision), opencode-go/deepseek-v4.1-flash

```json
{
 "judge": "concision",
 "judge_version": "1.0.0",
 "model": "opencode-go/deepseek-v4.1-flash (opencode) scripted pipeline 2026-09-15",
 "source_id": "08_empathy_sympathy_compassion_matrix",
 "labels": [
  {
   "claim_id": "C001",
   "loglog_ids": [
    "0"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Thesis summary stating the matrix's overall contrast; not restated elsewhere."
  },
  {
   "claim_id": "C002",
   "loglog_ids": [
    "1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Defines cold-control block grouping logic, substantive structural information."
  },
  {
   "claim_id": "C003",
   "loglog_ids": [
    "1.1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Accurate-modeling row scores; distinct data not repeated."
  },
  {
   "claim_id": "C004",
   "loglog_ids": [
    "1.2"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Boundary-kept row scores; distinct data."
  },
  {
   "claim_id": "C005",
   "loglog_ids": [
    "1.3"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Manipulators row scores; distinct data."
  },
  {
   "claim_id": "C006",
   "loglog_ids": [
    "1.4"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Controlled/instrumental row scores; distinct data."
  },
  {
   "claim_id": "C007",
   "loglog_ids": [
    "2"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Defines affective-care block grouping; substantive structural information."
  },
  {
   "claim_id": "C008",
   "loglog_ids": [
    "2.1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Sharing/mirroring row scores; distinct data."
  },
  {
   "claim_id": "C009",
   "loglog_ids": [
    "2.2"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Capacity-to-care row scores; distinct data."
  },
  {
   "claim_id": "C010",
   "loglog_ids": [
    "2.3"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Motivation-to-help row scores; distinct data."
  },
  {
   "claim_id": "C011",
   "loglog_ids": [
    "2.4"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Guilt/remorse row scores; distinct data."
  },
  {
   "claim_id": "C012",
   "loglog_ids": [
    "2.5"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Contagion/burnout row scores; distinct data."
  },
  {
   "claim_id": "C013",
   "loglog_ids": [
    "2.6"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Vivid/similar bias row scores; distinct data."
  },
  {
   "claim_id": "C014",
   "loglog_ids": [
    "2.7"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Kantianism row scores; distinct data, read before C034 recap."
  },
  {
   "claim_id": "C015",
   "loglog_ids": [
    "2.8"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Humanism row scores; distinct data, read before C034 recap."
  },
  {
   "claim_id": "C016",
   "loglog_ids": [
    "3"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Defines neither-dark block grouping; substantive structural information."
  },
  {
   "claim_id": "C017",
   "loglog_ids": [
    "3.1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Beyond in-group row scores; distinct data."
  },
  {
   "claim_id": "C018",
   "loglog_ids": [
    "3.2"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Faith-in-humanity row scores; distinct data."
  },
  {
   "claim_id": "C019",
   "loglog_ids": [
    "3.3"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Sustainability row scores; distinct data."
  },
  {
   "claim_id": "C020",
   "loglog_ids": [
    "4"
   ],
   "label": "Trivia",
   "canonical_id": null,
   "reasoning": "Restated section header; scope caveat already carried by clinical note 4.9."
  },
  {
   "claim_id": "C021",
   "loglog_ids": [
    "4.1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Explains why sympathy is partial on modeling minds; new interpretation."
  },
  {
   "claim_id": "C022",
   "loglog_ids": [
    "4.2"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Explains affective empathy's partial care; new interpretation."
  },
  {
   "claim_id": "C023",
   "loglog_ids": [
    "4.3"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Manipulators row as diagnostic; adds interpretation beyond row data."
  },
  {
   "claim_id": "C024",
   "loglog_ids": [
    "4.4"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Bloom/Singer provenance and critics; new sourced caveat."
  },
  {
   "claim_id": "C025",
   "loglog_ids": [
    "4.5"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Boundary maintenance as causal difference; new causal link."
  },
  {
   "claim_id": "C026",
   "loglog_ids": [
    "4.6"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Dark-column synthesis; new interpretive reading."
  },
  {
   "claim_id": "C027",
   "loglog_ids": [
    "4.7"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Psychopath/sociopath asymmetry framing; adds relation not stated earlier."
  },
  {
   "claim_id": "C028",
   "loglog_ids": [
    "4.8"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Etiology omission caveat; distinct methodological note."
  },
  {
   "claim_id": "C029",
   "loglog_ids": [
    "4.9"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Clinical caveat about contested diagnosis; distinct caveat."
  },
  {
   "claim_id": "C030",
   "loglog_ids": [
    "4.10"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Terminology caveat; distinct caveat."
  },
  {
   "claim_id": "C031",
   "loglog_ids": [
    "4.11"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Empath profile synthesis; new cross-block interpretation."
  },
  {
   "claim_id": "C032",
   "loglog_ids": [
    "4.12"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Altruist Light Triad mapping; new named entity reference."
  },
  {
   "claim_id": "C033",
   "loglog_ids": [
    "4.13"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Integrated ideal synthesis; new cross-block interpretation."
  },
  {
   "claim_id": "C034",
   "loglog_ids": [
    "4.14"
   ],
   "label": "Duplicate",
   "canonical_id": "C014",
   "reasoning": "Recap of Kantianism and Humanism row relations already stated; near-duplicates C014 and C015."
  },
  {
   "claim_id": "C035",
   "loglog_ids": [
    "4.15"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Faith in humanity as new dimension; interpretation absent earlier."
  }
 ],
 "metrics": {
  "scored_claims": 35,
  "unique": 33,
  "duplicates": 1,
  "trivia": 1,
  "redundancy_rate": 0.0286,
  "trivia_rate": 0.0286,
  "structured_tokens": 90,
  "tokens_per_unique_claim": 2.727272727272727
 },
 "prune_list": [
  "C020 trivia: restated 'Notes' Theme header, low information, safe to drop",
  "C034 duplicates C014 (also near-duplicates C015): recap of Kantianism/Humanism row relations, safe to merge into C014"
 ]
}
```

## Judge F (faithfulness), opencode-go/deepseek-v4.1-flash

```json
{
 "judge": "faithfulness",
 "judge_version": "1.0.0",
 "model": "opencode-go/deepseek-v4.1-flash (opencode) scripted pipeline 2026-09-15",
 "source_id": "08_empathy_sympathy_compassion_matrix",
 "claims": [
  {
   "claim_id": "C001",
   "loglog_ids": [
    "0"
   ],
   "claim_text": "Feature matrix contrasts cognitive and affective empathy, sympathy, and compassion across five profiles from psychopath to integrated ideal.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "The four component columns (cognitive and affective empathy, sympathy, compassion)... psychopath, sociopath, empath, altruist, and the integrated ideal.",
   "reasoning": "Source names these four components and five profiles in the same order."
  },
  {
   "claim_id": "C002",
   "loglog_ids": [
    "1"
   ],
   "claim_text": "Cold-control block groups rows present in both dark profiles plus the psychopath-only control row.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "four blocks... present in both, in the psychopath only, in the sociopath only, and in neither.",
   "reasoning": "Rows 1-4 match the present-in-both block plus the psychopath-only row; note 6 calls that cold instrumental control."
  },
  {
   "claim_id": "C003",
   "loglog_ids": [
    "1.1"
   ],
   "claim_text": "Accurate modeling: cognitive ✓, affective ~, sympathy ~, compassion ✓; psychopath ✓, sociopath ~, empath ~, altruist ✓, integrated ✓.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "| Accurately modeling the other's mental state | ✓ | ~ | ~ | ✓ | ✓ | ~ | ~ | ✓ | ✓ |",
   "reasoning": "Every mark matches the source table row exactly."
  },
  {
   "claim_id": "C004",
   "loglog_ids": [
    "1.2"
   ],
   "claim_text": "Boundary kept: cognitive ✓, affective blank, sympathy ✓, compassion ✓; psychopath ✓, sociopath ~, empath blank, altruist ✓, integrated ✓.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "| Maintains self/other boundary | ✓ |   | ✓ | ✓ | ✓ | ~ |   | ✓ | ✓ |",
   "reasoning": "Marks and blanks match the source row precisely."
  },
  {
   "claim_id": "C005",
   "loglog_ids": [
    "1.3"
   ],
   "claim_text": "Manipulators row: cognitive ✓ only; psychopath ✓, sociopath ~, all others blank.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "| Can exist in manipulators / con artists | ✓ |   |   |   | ✓ | ~ |   |   |   |",
   "reasoning": "Correctly reports cognitive ✓, psychopath ✓, sociopath ~, rest blank."
  },
  {
   "claim_id": "C006",
   "loglog_ids": [
    "1.4"
   ],
   "claim_text": "Controlled/instrumental, not reactive/impulsive: cognitive ✓, sympathy ~, compassion ✓; psychopath ✓, altruist ✓, integrated ✓; affective, sociopath, empath blank.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "| Controlled / instrumental rather than reactive / impulsive | ✓ |   | ~ | ✓ | ✓ |   |   | ✓ | ✓ |",
   "reasoning": "Marks and blanks match the source row; negation kept intact."
  },
  {
   "claim_id": "C007",
   "loglog_ids": [
    "2"
   ],
   "claim_text": "Affective-care block: rows the sociopath has and the psychopath lacks, mostly partial marks.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "four blocks... in the sociopath only...",
   "reasoning": "Rows 5-12 are the sociopath-only block, psychopath blank, dominantly ~ marks."
  },
  {
   "claim_id": "C008",
   "loglog_ids": [
    "2.1"
   ],
   "claim_text": "Sharing/mirroring emotion: affective ✓; sociopath ~, empath ✓, altruist ~, integrated ✓; others blank.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "| Actually sharing / mirroring the emotion |   | ✓ |   |   |   | ~ | ✓ | ~ | ✓ |",
   "reasoning": "All marks and blanks match the source row."
  },
  {
   "claim_id": "C009",
   "loglog_ids": [
    "2.2"
   ],
   "claim_text": "Capacity to care at all: affective ~, sympathy ✓, compassion ✓; sociopath ✓, empath ✓, altruist ✓, integrated ✓; psychopath blank.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "| Capacity to genuinely care about the person *at all* |   | ~ | ✓ | ✓ |   | ✓ | ✓ | ✓ | ✓ |",
   "reasoning": "Marks match source exactly, including psychopath blank."
  },
  {
   "claim_id": "C010",
   "loglog_ids": [
    "2.3"
   ],
   "claim_text": "Motivation to help/act: affective ~, sympathy ~, compassion ✓; sociopath ~, empath ~, altruist ✓, integrated ✓; psychopath blank.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "| Motivation to help or act |   | ~ | ~ | ✓ |   | ~ | ~ | ✓ | ✓ |",
   "reasoning": "Full row reproduced accurately."
  },
  {
   "claim_id": "C011",
   "loglog_ids": [
    "2.4"
   ],
   "claim_text": "Guilt/remorse after harm: empath ✓; affective ~, sympathy ~, compassion ~, sociopath ~, altruist ~, integrated ~; cognitive and psychopath blank.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "| Produces guilt / remorse after causing harm |   | ~ | ~ | ~ |   | ~ | ✓ | ~ | ~ |",
   "reasoning": "Only empath ✓, all listed ~ marks and two blanks match source."
  },
  {
   "claim_id": "C012",
   "loglog_ids": [
    "2.5"
   ],
   "claim_text": "Contagion/burnout risk: affective ✓, empath ✓; sympathy ~, sociopath ~, integrated ~; others blank.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "| Risk of emotional contagion and burnout |   | ✓ | ~ |   |   | ~ | ✓ |   | ~ |",
   "reasoning": "Marks and blanks match source row."
  },
  {
   "claim_id": "C013",
   "loglog_ids": [
    "2.6"
   ],
   "claim_text": "Vivid/similar bias: affective ✓, sociopath ✓, empath ✓; cognitive ~, sympathy ~, integrated ~; others blank.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "| Biased toward vivid, similar individuals | ~ | ✓ | ~ |   |   | ✓ | ✓ |   | ~ |",
   "reasoning": "Reproduced correctly, including altruist blank."
  },
  {
   "claim_id": "C014",
   "loglog_ids": [
    "2.7"
   ],
   "claim_text": "Ends, not means (Kantianism): compassion ✓, empath ✓, altruist ✓, integrated ✓; affective ~, sympathy ~, sociopath ~; cognitive and psychopath blank.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "| Treats people as ends, not means (Kantianism) |   | ~ | ~ | ✓ |   | ~ | ✓ | ✓ | ✓ |",
   "reasoning": "Negation and all marks preserved correctly."
  },
  {
   "claim_id": "C015",
   "loglog_ids": [
    "2.8"
   ],
   "claim_text": "Dignity and worth (Humanism): sympathy ✓, compassion ✓, empath ✓, altruist ✓, integrated ✓; affective ~, sociopath ~; cognitive and psychopath blank.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "| Values each person's dignity and worth (Humanism) |   | ~ | ✓ | ✓ |   | ~ | ✓ | ✓ | ✓ |",
   "reasoning": "Rows marks match source exactly."
  },
  {
   "claim_id": "C016",
   "loglog_ids": [
    "3"
   ],
   "claim_text": "Neither-dark block: beyond in-group, faith, and scalability rows, blank for both dark profiles.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "four blocks... in neither.",
   "reasoning": "Rows 13-15 are the neither block; psychopath and sociopath are blank there."
  },
  {
   "claim_id": "C017",
   "loglog_ids": [
    "3.1"
   ],
   "claim_text": "Beyond a vivid/similar in-group: sympathy ~, compassion ✓, altruist ✓, integrated ✓; all others blank.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "| Concern reaches *beyond* a vivid / similar in-group |   |   | ~ | ✓ |   |   |   | ✓ | ✓ |",
   "reasoning": "Marks match, including both dark profile blanks."
  },
  {
   "claim_id": "C018",
   "loglog_ids": [
    "3.2"
   ],
   "claim_text": "Fundamentally good (Faith in Humanity): sympathy ~, compassion ~, empath ✓, altruist ✓, integrated ✓; both dark profiles blank.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "| Believes people are fundamentally good (Faith in Humanity) |   |   | ~ | ~ |   |   | ✓ | ✓ | ✓ |",
   "reasoning": "Reproduced accurately with both dark columns blank."
  },
  {
   "claim_id": "C019",
   "loglog_ids": [
    "3.3"
   ],
   "claim_text": "Sustainable/scalable guide: cognitive ~, sympathy ~, compassion ✓, altruist ✓, integrated ✓; others blank.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "| Sustainable and scalable as a moral guide | ~ |   | ~ | ✓ |   |   |   | ✓ | ✓ |",
   "reasoning": "Marks and blanks match source row."
  },
  {
   "claim_id": "C020",
   "loglog_ids": [
    "4"
   ],
   "claim_text": "Notes interpret the matrix rows and limit its scope to ideal types.",
   "claim_type": "meta",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Treat these two columns as ideal types, not categories.",
   "reasoning": "Notes explain rows and repeatedly frame profiles as ideal types."
  },
  {
   "claim_id": "C021",
   "loglog_ids": [
    "4.1"
   ],
   "claim_text": "Sympathy is '~' on modeling minds: one can pity while badly misreading; understanding helps but isn't constitutive, unlike cognitive empathy.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "you can pity someone while badly misreading them... isn't constitutive of it, the way it is for cognitive empathy.",
   "reasoning": "Mirrors note 1 including the negation about constitutive understanding."
  },
  {
   "claim_id": "C022",
   "loglog_ids": [
    "4.2"
   ],
   "claim_text": "Affective empathy's care is '~': contagion can happen involuntarily, without real concern, and simply make one want to get away.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "emotional contagion can happen involuntarily, without any real concern for the person... simply want to get away",
   "reasoning": "Matches note 2 including the negated 'without any real concern'."
  },
  {
   "claim_id": "C023",
   "loglog_ids": [
    "4.3"
   ],
   "claim_text": "'Manipulators' row is the sharpest diagnostic and essentially the psychopath's signature: cognitive empathy alone is compatible with cruelty.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "sharpest diagnostic... essentially the psychopath's signature. Cognitive empathy alone is compatible with cruelty",
   "reasoning": "Direct restatement of note 3."
  },
  {
   "claim_id": "C024",
   "loglog_ids": [
    "4.4"
   ],
   "claim_text": "Sustainability row reflects the Bloom/Singer argument (Paul Bloom's Against Empathy; Tania Singer's research), a position not a consensus; critics warn of abstract, paternalistic compassion.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "reflects the Bloom/Singer argument... which is a position, not a consensus. Critics reply that compassion... risks becoming abstract or paternalistic.",
   "reasoning": "Names, attribution, and hedge all preserved from note 4."
  },
  {
   "claim_id": "C025",
   "loglog_ids": [
    "4.5"
   ],
   "claim_text": "Boundary maintenance is the structural difference: partially merging with the other's state drives both motivational power and burnout/bias problems.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Boundary maintenance is the structural difference... partially merging with the other's state, which is what drives both its motivational power and its burnout and bias problems.",
   "reasoning": "Causal claim matches note 5 exactly."
  },
  {
   "claim_id": "C026",
   "loglog_ids": [
    "4.6"
   ],
   "claim_text": "Dark-column reading: psychopath is the cognitive column standing alone; sociopath is affect plus sympathy clamped to a narrow in-group, stripped of regulation.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "The psychopath is the cognitive column standing alone. The sociopath is affective empathy plus sympathy clamped to an in-group and stripped of regulation.",
   "reasoning": "Absolute wording matches note 10; source note 6 says 'close to' but note 10 states it plainly."
  },
  {
   "claim_id": "C027",
   "loglog_ids": [
    "4.7"
   ],
   "claim_text": "Asymmetry: almost everything the psychopath has, the sociopath shares in degraded form; the psychopath's one distinguishing possession is cold instrumental control.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "almost everything the psychopath has, the sociopath also has in degraded form... the psychopath's one distinguishing possession is cold instrumental control",
   "reasoning": "Direct restatement of note 6."
  },
  {
   "claim_id": "C028",
   "loglog_ids": [
    "4.8"
   ],
   "claim_text": "Etiology deliberately left out: psychopathy is often theorized as innate, sociopathy as environmentally acquired; causes don't describe the response's shape.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "psychopathy is often theorized as innate and temperamental, sociopathy as environmentally acquired. That is a claim about *causes*, not about the shape of the response",
   "reasoning": "Hedge 'often' retained; only 'and temperamental' compressed, no meaning change."
  },
  {
   "claim_id": "C029",
   "loglog_ids": [
    "4.9"
   ],
   "claim_text": "Clinical caveat: the two profiles aren't formal diagnoses; both fall under Antisocial Personality Disorder; the split is a contested, largely theoretical convention.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "\"psychopath\" and \"sociopath\" are not formal diagnoses. Both fall under Antisocial Personality Disorder... contested, largely theoretical convention.",
   "reasoning": "Negation and all qualifiers match note 8."
  },
  {
   "claim_id": "C030",
   "loglog_ids": [
    "4.10"
   ],
   "claim_text": "Terminology varies: some authors use 'empathic concern' roughly where the table says compassion; this table uses the neutral research sense of sympathy.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Some authors use \"empathic concern\" roughly where this table uses \"compassion\"... This table uses the more neutral research sense.",
   "reasoning": "Matches note 9; the added 'of sympathy' resolves the source's contextual antecedent."
  },
  {
   "claim_id": "C031",
   "loglog_ids": [
    "4.11"
   ],
   "claim_text": "Empath profile: affective column maxed and unregulated, failing boundary, scope, and scalability; inherits the sociopath's distortions, so not the moral ideal.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "the empath is the affective column maxed out and unregulated... failing on boundary, scope, and scalability... inherits the sociopath's distortions, so it is not the moral ideal.",
   "reasoning": "Matches note 10 including the negated conclusion."
  },
  {
   "claim_id": "C032",
   "loglog_ids": [
    "4.12"
   ],
   "claim_text": "Altruist profile: compassion column embodied, matching the research 'Light Triad' (Kaufman et al., 2019).",
   "claim_type": "name_or_entity",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "The altruist is the compassion column embodied, matching the research \"Light Triad\"... from Kaufman et al., 2019",
   "reasoning": "Attribution and year match note 10 exactly."
  },
  {
   "claim_id": "C033",
   "loglog_ids": [
    "4.13"
   ],
   "claim_text": "Integrated ideal: the only column scoring well across every block, including the 'present in neither' rows; true opposite of both dark profiles.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "The integrated ideal is the only column that scores well across every block, including the \"present in neither\" rows, so it is the true opposite of both dark profiles at once.",
   "reasoning": "Direct restatement of note 10."
  },
  {
   "claim_id": "C034",
   "loglog_ids": [
    "4.14"
   ],
   "claim_text": "Kantianism row is essentially the inverse of the manipulators row; Humanism overlaps the caring and beyond-the-in-group rows.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "\"Treats people as ends, not means\" (Kantianism) is essentially the inverse of the \"manipulators\" row... \"Values each person's dignity and worth\" (Humanism) overlaps with the caring and beyond-the-in-group rows.",
   "reasoning": "Matches note 11, negation preserved."
  },
  {
   "claim_id": "C035",
   "loglog_ids": [
    "4.15"
   ],
   "claim_text": "Only Faith in Humanity adds a genuinely new dimension, an attitude rather than an empathy component; both dark profiles score blank there.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Only \"Believes people are fundamentally good\" (Faith in Humanity) adds a genuinely new dimension... which is why both dark profiles score blank",
   "reasoning": "Matches note 11 including 'Only' and the blank dark profiles."
  }
 ],
 "metrics": {
  "total_claims": 35,
  "supported": 35,
  "partially_supported": 0,
  "unverifiable": 0,
  "contradicted": 0,
  "critical_errors": 0,
  "faithfulness_precision": 1.0
 },
 "fail_list": []
}
```

## Judge Cov (coverage), opencode-go/deepseek-v4.1-flash

```json
{
 "judge": "coverage",
 "judge_version": "1.0.0",
 "model": "opencode-go/deepseek-v4.1-flash (opencode) scripted pipeline 2026-09-15",
 "source_id": "08_empathy_sympathy_compassion_matrix",
 "key_points": [
  {
   "point_id": "K01",
   "point_text": "Central purpose: a feature matrix comparing four components (cognitive empathy, affective empathy, sympathy, compassion) against five whole-person profiles (psychopath, sociopath, empath, altruist, integrated ideal), the profiles arranged darkest to lightest.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L001",
    "L002"
   ],
   "evidence_quote": "Feature matrix contrasts cognitive and affective empathy, sympathy, and compassion across five profiles from psychopath to integrated ideal.",
   "reasoning": "L002 names all four components and the five profiles from psychopath to integrated ideal, matching the organizing thesis. The darkest-to-lightest ordering is implicit in 'from psychopath to integrated ideal' and the source mapping at L001."
  },
  {
   "point_id": "K02",
   "point_text": "Rows are ordered by the two dark profiles' contrast and split into four blocks separated by blank dividers: present in both, psychopath only, sociopath only, and neither.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L003",
    "L008",
    "L017"
   ],
   "evidence_quote": "Theme: Cold-control block: rows present in both dark profiles, plus the psychopath-only control row. ... Affective-care block: rows the sociopath has and the psychopath lacks ... Neither-dark block",
   "reasoning": "The three explicit themes plus the interpretive notes block (L021) reproduce the block structure: present-in-both/psychopath-only (L003), sociopath-only (L008), and neither (L017)."
  },
  {
   "point_id": "K03",
   "point_text": "Sympathy gets a partial (~) on modeling the other's mind because you can pity someone while badly misreading them; accurate understanding helps sympathy but is not constitutive of it, unlike cognitive empathy.",
   "weight": "Nice to have",
   "presence": "Present",
   "loglog_ids": [
    "L022"
   ],
   "evidence_quote": "Sympathy is '~' on modeling minds: one can pity while badly misreading; understanding helps but isn't constitutive, unlike cognitive empathy.",
   "reasoning": "L022 captures the partial mark, the pity-with-misreading reason, and the contrast with cognitive empathy."
  },
  {
   "point_id": "K04",
   "point_text": "Affective empathy gets a partial (~) on capacity to care because emotional contagion can occur involuntarily without real concern, e.g., catching someone's anxiety and wanting to get away from them.",
   "weight": "Nice to have",
   "presence": "Present",
   "loglog_ids": [
    "L023"
   ],
   "evidence_quote": "Affective empathy's care is '~': contagion can happen involuntarily, without real concern, and simply make one want to get away.",
   "reasoning": "L023 preserves the partial mark, the involuntary-contagion rationale, and the get-away example."
  },
  {
   "point_id": "K05",
   "point_text": "The manipulators/con-artist row is the sharpest diagnostic for the cognitive/affective split and is essentially the psychopath's signature: cognitive empathy alone is compatible with cruelty, since a con artist models minds precisely without resonating with or caring about them.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L006",
    "L024",
    "L040"
   ],
   "evidence_quote": "'Manipulators' row is the sharpest diagnostic and essentially the psychopath's signature: cognitive empathy alone is compatible with cruelty.",
   "reasoning": "L024 states the diagnostic/signature claim and the cognitive-empathy-alone-compatible-with-cruelty point; L040 reasons it supports the split; L006 records the row's scores."
  },
  {
   "point_id": "K06",
   "point_text": "The sustainable-and-scalable row reflects the Bloom/Singer argument (Paul Bloom's Against Empathy and Tania Singer's compassion-training research); it is a position, not a consensus, and critics reply that compassion without empathic grounding risks becoming abstract or paternalistic.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L025",
    "L041"
   ],
   "evidence_quote": "Sustainability row reflects the Bloom/Singer argument (Paul Bloom's Against Empathy; Tania Singer's research), a position not a consensus; critics warn of abstract, paternalistic compassion.",
   "reasoning": "L025 names both authors and works, flags it as a position not a consensus, and preserves the critics' abstract/paternalistic warning. The contested qualifier is intact."
  },
  {
   "point_id": "K07",
   "point_text": "Boundary maintenance is the structural difference between affective empathy and everything else: affective empathy means partially merging with the other's state, which drives both its motivational power and its burnout and bias problems.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L026",
    "L042",
    "L043"
   ],
   "evidence_quote": "Boundary maintenance is the structural difference: partially merging with the other's state drives both motivational power and burnout/bias problems.",
   "reasoning": "L026 preserves the structural-difference claim and both consequences; L042/L043 tie it to the motivation and burnout/bias rows."
  },
  {
   "point_id": "K08",
   "point_text": "Reading the two dark profiles as columns: the psychopath is close to the cognitive-empathy column standing alone (accurate modeling with affective and caring machinery deleted), while the sociopath is close to affective empathy and sympathy clamped to a narrow in-group and stripped of regulation; the psychopath's one distinguishing possession is cold instrumental control, while a whole cluster of affective and caring rows belongs to the sociopath and not the psychopath.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L027",
    "L028",
    "L044"
   ],
   "evidence_quote": "psychopath is the cognitive column standing alone; sociopath is affect plus sympathy clamped to a narrow in-group, stripped of regulation. ... almost everything the psychopath has, the sociopath shares in degraded form; the psychopath's one distinguishing possession is cold instrumental control.",
   "reasoning": "L027 and L028 together capture both column readings, the in-group clamping, stripping of regulation, and the asymmetry of cold instrumental control as the psychopath's one possession. The caring/affective cluster belonging to the sociopath is implicit in the block themes (L008) and degraded-form statement."
  },
  {
   "point_id": "K09",
   "point_text": "Etiology is deliberately excluded as a row: psychopathy is often theorized as innate/temperamental and sociopathy as environmentally acquired, but that concerns causes rather than the shape of the response, so it does not belong in a feature table and would muddy the logic.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L029"
   ],
   "evidence_quote": "Etiology deliberately left out: psychopathy is often theorized as innate, sociopathy as environmentally acquired; causes don't describe the response's shape.",
   "reasoning": "L029 preserves the deliberate exclusion, both etiological theories, and the cause-versus-shape justification."
  },
  {
   "point_id": "K10",
   "point_text": "Clinical caveat: 'psychopath' and 'sociopath' are not formal diagnoses; both fall under Antisocial Personality Disorder, and the split between them is a contested, largely theoretical convention. Treat the two columns as ideal types, not categories.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L021",
    "L030"
   ],
   "evidence_quote": "Clinical caveat: the two profiles aren't formal diagnoses; both fall under Antisocial Personality Disorder; the split is a contested, largely theoretical convention.",
   "reasoning": "L030 preserves all three qualifiers; L021 frames the whole notes block as limiting scope to ideal types."
  },
  {
   "point_id": "K11",
   "point_text": "Terminology caveat: usage varies across the literature, some authors use 'empathic concern' roughly where this table uses 'compassion', and pop-psych usage (e.g., Brené Brown) treats 'sympathy' as inherently distancing; this table uses the more neutral research sense.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L031"
   ],
   "evidence_quote": "Terminology varies: some authors use 'empathic concern' roughly where the table says compassion; this table uses the neutral research sense of sympathy.",
   "reasoning": "L031 preserves the variation-in-usage claim, the empathic-concern/compassion overlap, and the neutral-research-sense resolution. The Brené Brown pop-psych example is omitted, but it is an illustrative aside rather than a load-bearing condition; the core caveat and its resolution survive intact."
  },
  {
   "point_id": "K12",
   "point_text": "The empath column is the affective column maxed out and unregulated, which is why it lights up emotion-sharing, contagion, and vividness bias while failing on boundary, scope, and scalability; it is the opposite of the psychopath's coldness but inherits the sociopath's distortions, so it is not the moral ideal.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L032"
   ],
   "evidence_quote": "Empath profile: affective column maxed and unregulated, failing boundary, scope, and scalability; inherits the sociopath's distortions, so not the moral ideal.",
   "reasoning": "L032 preserves the maxed/unregulated affective reading, the failures on boundary/scope/scalability, the inherited distortions, and the not-the-moral-ideal conclusion."
  },
  {
   "point_id": "K13",
   "point_text": "The altruist column is the compassion column embodied and matches the research 'Light Triad' (Kantianism, Humanism, and Faith in Humanity, from Kaufman et al., 2019).",
   "weight": "Nice to have",
   "presence": "Present",
   "loglog_ids": [
    "L033",
    "L015",
    "L016",
    "L019"
   ],
   "evidence_quote": "Altruist profile: compassion column embodied, matching the research 'Light Triad' (Kaufman et al., 2019).",
   "reasoning": "L033 preserves the compassion-embodied mapping, the Light Triad label, and the Kaufman attribution. The three Light Triad components are not enumerated there but appear as distinct rows (Kantianism L015, Humanism L016, Faith in Humanity L019), so the meaning is available."
  },
  {
   "point_id": "K14",
   "point_text": "The integrated ideal is the only column that scores well across every block, including the 'present in neither' rows, so it is the true opposite of both dark profiles at once.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L034"
   ],
   "evidence_quote": "Integrated ideal: the only column scoring well across every block, including the 'present in neither' rows; true opposite of both dark profiles.",
   "reasoning": "L034 preserves the uniqueness claim, the inclusion of the neither-dark rows, and the true-opposite conclusion."
  },
  {
   "point_id": "K15",
   "point_text": "The three Light Triad rows partly restate earlier rows: Kantianism is essentially the inverse of the manipulators row, Humanism overlaps the caring and beyond-the-in-group rows, and only Faith in Humanity adds a genuinely new dimension (an attitude rather than an empathy component), which is why both dark profiles score blank on it.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L035",
    "L036",
    "L038",
    "L039"
   ],
   "evidence_quote": "Kantianism row is essentially the inverse of the manipulators row; Humanism overlaps the caring and beyond-the-in-group rows. ... Only Faith in Humanity adds a genuinely new dimension, an attitude rather than an empathy component; both dark profiles score blank there.",
   "reasoning": "L035/L036 preserve the redundancy claims and the novel-dimension point; L038/L039 cross-link the restatements to the manipulators and caring/in-group rows."
  }
 ],
 "metrics": {
  "total_points": 15,
  "must_have_total": 12,
  "must_have_present": 12,
  "must_have_partial": 0,
  "must_have_missing": 0,
  "overall_present": 15,
  "must_recall": 1.0,
  "overall_recall": 1.0
 },
 "missing_list": []
}
```

## Judge Con (concision), opencode-go/deepseek-v4.1-flash

```json
{
 "judge": "concision",
 "judge_version": "1.0.0",
 "model": "opencode-go/deepseek-v4.1-flash (opencode) scripted pipeline 2026-09-15",
 "source_id": "08_empathy_sympathy_compassion_matrix",
 "labels": [
  {
   "claim_id": "C001",
   "loglog_ids": [
    "0"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Thesis summary stating the matrix's overall contrast; not restated elsewhere."
  },
  {
   "claim_id": "C002",
   "loglog_ids": [
    "1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Defines cold-control block grouping logic, substantive structural information."
  },
  {
   "claim_id": "C003",
   "loglog_ids": [
    "1.1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Accurate-modeling row scores; distinct data not repeated."
  },
  {
   "claim_id": "C004",
   "loglog_ids": [
    "1.2"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Boundary-kept row scores; distinct data."
  },
  {
   "claim_id": "C005",
   "loglog_ids": [
    "1.3"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Manipulators row scores; distinct data."
  },
  {
   "claim_id": "C006",
   "loglog_ids": [
    "1.4"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Controlled/instrumental row scores; distinct data."
  },
  {
   "claim_id": "C007",
   "loglog_ids": [
    "2"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Defines affective-care block grouping; substantive structural information."
  },
  {
   "claim_id": "C008",
   "loglog_ids": [
    "2.1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Sharing/mirroring row scores; distinct data."
  },
  {
   "claim_id": "C009",
   "loglog_ids": [
    "2.2"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Capacity-to-care row scores; distinct data."
  },
  {
   "claim_id": "C010",
   "loglog_ids": [
    "2.3"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Motivation-to-help row scores; distinct data."
  },
  {
   "claim_id": "C011",
   "loglog_ids": [
    "2.4"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Guilt/remorse row scores; distinct data."
  },
  {
   "claim_id": "C012",
   "loglog_ids": [
    "2.5"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Contagion/burnout row scores; distinct data."
  },
  {
   "claim_id": "C013",
   "loglog_ids": [
    "2.6"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Vivid/similar bias row scores; distinct data."
  },
  {
   "claim_id": "C014",
   "loglog_ids": [
    "2.7"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Kantianism row scores; distinct data, read before C034 recap."
  },
  {
   "claim_id": "C015",
   "loglog_ids": [
    "2.8"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Humanism row scores; distinct data, read before C034 recap."
  },
  {
   "claim_id": "C016",
   "loglog_ids": [
    "3"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Defines neither-dark block grouping; substantive structural information."
  },
  {
   "claim_id": "C017",
   "loglog_ids": [
    "3.1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Beyond in-group row scores; distinct data."
  },
  {
   "claim_id": "C018",
   "loglog_ids": [
    "3.2"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Faith-in-humanity row scores; distinct data."
  },
  {
   "claim_id": "C019",
   "loglog_ids": [
    "3.3"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Sustainability row scores; distinct data."
  },
  {
   "claim_id": "C020",
   "loglog_ids": [
    "4"
   ],
   "label": "Trivia",
   "canonical_id": null,
   "reasoning": "Restated section header; scope caveat already carried by clinical note 4.9."
  },
  {
   "claim_id": "C021",
   "loglog_ids": [
    "4.1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Explains why sympathy is partial on modeling minds; new interpretation."
  },
  {
   "claim_id": "C022",
   "loglog_ids": [
    "4.2"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Explains affective empathy's partial care; new interpretation."
  },
  {
   "claim_id": "C023",
   "loglog_ids": [
    "4.3"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Manipulators row as diagnostic; adds interpretation beyond row data."
  },
  {
   "claim_id": "C024",
   "loglog_ids": [
    "4.4"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Bloom/Singer provenance and critics; new sourced caveat."
  },
  {
   "claim_id": "C025",
   "loglog_ids": [
    "4.5"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Boundary maintenance as causal difference; new causal link."
  },
  {
   "claim_id": "C026",
   "loglog_ids": [
    "4.6"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Dark-column synthesis; new interpretive reading."
  },
  {
   "claim_id": "C027",
   "loglog_ids": [
    "4.7"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Psychopath/sociopath asymmetry framing; adds relation not stated earlier."
  },
  {
   "claim_id": "C028",
   "loglog_ids": [
    "4.8"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Etiology omission caveat; distinct methodological note."
  },
  {
   "claim_id": "C029",
   "loglog_ids": [
    "4.9"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Clinical caveat about contested diagnosis; distinct caveat."
  },
  {
   "claim_id": "C030",
   "loglog_ids": [
    "4.10"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Terminology caveat; distinct caveat."
  },
  {
   "claim_id": "C031",
   "loglog_ids": [
    "4.11"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Empath profile synthesis; new cross-block interpretation."
  },
  {
   "claim_id": "C032",
   "loglog_ids": [
    "4.12"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Altruist Light Triad mapping; new named entity reference."
  },
  {
   "claim_id": "C033",
   "loglog_ids": [
    "4.13"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Integrated ideal synthesis; new cross-block interpretation."
  },
  {
   "claim_id": "C034",
   "loglog_ids": [
    "4.14"
   ],
   "label": "Duplicate",
   "canonical_id": "C014",
   "reasoning": "Recap of Kantianism and Humanism row relations already stated; near-duplicates C014 and C015."
  },
  {
   "claim_id": "C035",
   "loglog_ids": [
    "4.15"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Faith in humanity as new dimension; interpretation absent earlier."
  }
 ],
 "metrics": {
  "scored_claims": 35,
  "unique": 33,
  "duplicates": 1,
  "trivia": 1,
  "redundancy_rate": 0.0286,
  "trivia_rate": 0.0286,
  "structured_tokens": 90,
  "tokens_per_unique_claim": 2.727272727272727
 },
 "prune_list": [
  "C020 trivia: restated 'Notes' Theme header, low information, safe to drop",
  "C034 duplicates C014 (also near-duplicates C015): recap of Kantianism/Humanism row relations, safe to merge into C014"
 ]
}
```

## Judge Top (overall), opencode-go/deepseek-v4.1-flash

```json
{
 "judge": "overall",
 "judge_version": "1.0.0",
 "model": "deepseek-v4.1-flash, 2026-09-15",
 "source_id": "point-hierarchy run (as provided in inputs)",
 "inputs": {
  "faithfulness_precision": 1.0,
  "critical_errors": 0,
  "must_recall": 1.0,
  "overall_recall": 1.0,
  "redundancy_rate": 0.0286,
  "trivia_rate": 0.0286
 },
 "weights_used": {
  "faithfulness_precision": 0.4,
  "coverage_must_recall": 0.4,
  "redundancy_penalty": 0.2
 },
 "computation": "weighted_score = 0.4 * 1.0 (faithfulness_precision) + 0.4 * 1.0 (must_recall) - 0.2 * 0.0286 (redundancy_rate) = 0.4 + 0.4 - 0.00572 = 0.79428",
 "weighted_score": 0.79428,
 "verdict": "Pass",
 "tradeoff_note": "All three aspect judges agree: 35/35 claims supported, 12/12 must-have points present, and redundancy is well under the 0.15 max, so no length-for-coverage tradeoff is needed. The only concision cost is one trivial restatement (C020) and one duplicate (C034), which are cosmetic rather than structural.",
 "fix_list": [
  "Merge C034 into C014 (it also near-duplicates C015), collapsing the three Kantianism/Humanism relation recaps into one canonical statement.",
  "Drop C020 (trivia restatement of the 'Notes' Theme header); it carries no information beyond the section label."
 ],
 "reasoning": "Gate checks, in policy order. (1) Hard fails by critical errors: faithfulness reports critical_errors = 0, which is <= config.pass_gates.critical_contradicted_max = 0, so no critical fail. All 35 claims are classified supported with empty Non-Supported list, so there is no contradicted or partially_supported claim, and thus no quote re-read of SOURCE was required since the faithfulness and coverage judges do not conflict on any fact. (2) Faithfulness gate: faithfulness_precision = 1.0 >= config.pass_gates.faithfulness_precision_min = 0.95, pass with margin 0.05. (3) Coverage gate: must_recall = 1.0 >= config.pass_gates.must_recall_min = 0.9, pass with margin 0.10; must_have_present 12 of 12, must_have_partial 0, must_have_missing 0, and the Non-Present key points list is empty. overall_recall = 1.0 with 15 of 15 total_points present. (4) Concision is not a hard gate on its own, but redundancy_rate = 0.0286 is far below config.pass_gates.redundancy_max = 0.15, so the length cost is fully justified and no pruning is forced. The scored claim base is 35 with 33 unique, 1 duplicate (C034) and 1 trivia (C020); note that C034 is flagged as both duplicate of C014 and near-duplicate of C015, so the 1 duplicate count slightly understates the overlap cluster, but even treating the whole cluster as redundant the rate remains clearly under 0.15. tokens_per_unique_claim = 2.727 is not a gate and does not change the verdict. (5) Weighted score: 0.4*1.0 + 0.4*1.0 - 0.2*0.0286 = 0.79428, computed only because all gates passed, per the top_policy of ranking passes by weighted score. (6) Borderline check: the policy says to use Borderline when gates pass numerically but a Partial or Unverifiable claim affects a Must-have point. Here partially_supported = 0, unverifiable = 0, and all 12 must-have points are fully present, so there is no claim to name and Borderline is not warranted. Everything points to a clean Pass: the only residual work is the two-item prune list (C020, C034), which improves tokens without touching faithfulness or coverage. Verdict: Pass at weighted_score 0.79428."
}
```
