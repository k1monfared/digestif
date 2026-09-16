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
   "claim_text": "The matrix separates cognitive and affective empathy, sympathy, and compassion, then profiles psychopath, sociopath, empath, altruist, and integrated ideal.",
   "claim_type": "definition",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "The four component columns (cognitive and affective empathy, sympathy, compassion) sit left of the double rule. The five to the right are whole-person profiles ... psychopath, sociopath, empath, altruist, and the integrated ideal.",
   "reasoning": "Source names the same four components and five profiles in the same order."
  },
  {
   "claim_id": "C002",
   "loglog_ids": [
    "1"
   ],
   "claim_text": "Four components sit left of the double rule; five dark-to-light profiles sit right.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "The four component columns ... sit left of the double rule. The five to the right are whole-person profiles, arranged darkest to lightest",
   "reasoning": "Direct restatement of source layout and darkest-to-lightest ordering."
  },
  {
   "claim_id": "C003",
   "loglog_ids": [
    "1.1"
   ],
   "claim_text": "Rows fall in four blocks: present in both, psychopath only, sociopath only, neither.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "four blocks separated by blank dividers: present in both, in the psychopath only, in the sociopath only, and in neither.",
   "reasoning": "Exact parallel to the source's four block names."
  },
  {
   "claim_id": "C004",
   "loglog_ids": [
    "2"
   ],
   "claim_text": "Cognitive empathy means accurate modeling, boundary, and control; it survives in manipulators.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Can exist in manipulators / con artists: cognitive check only ... Controlled / instrumental rather than reactive / impulsive: cognitive check",
   "reasoning": "Table gives cognitive checks on modeling, boundary, manipulators, and control as stated."
  },
  {
   "claim_id": "C005",
   "loglog_ids": [
    "2.1"
   ],
   "claim_text": "The psychopath column is essentially the cognitive-empathy column standing alone.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "the psychopath is close to the cognitive-empathy column standing alone",
   "reasoning": "Note 6 and Note 10 both state this; 'essentially' matches 'standing alone'."
  },
  {
   "claim_id": "C006",
   "loglog_ids": [
    "2.2"
   ],
   "claim_text": "Sympathy earns only partial on modeling: pity can badly misread people.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Sympathy gets \"~\" on modeling the other's mind because you can pity someone while badly misreading them.",
   "reasoning": "Source explicitly gives sympathy a tilde for misreading while pitying."
  },
  {
   "claim_id": "C007",
   "loglog_ids": [
    "3"
   ],
   "claim_text": "Affective empathy means sharing emotion, with contagion, burnout, and vividness bias.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Actually sharing / mirroring the emotion ... Risk of emotional contagion and burnout: affective check ... Biased toward vivid, similar individuals: ... affective check",
   "reasoning": "Table assigns affective checks to sharing, contagion/burnout, and vividness bias."
  },
  {
   "claim_id": "C008",
   "loglog_ids": [
    "3.1"
   ],
   "claim_text": "Affective empathy lacks boundary maintenance, unlike everything else in the table.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Boundary maintenance is the structural difference between affective empathy and everything else in the table",
   "reasoning": "Note 5 states boundary is the structural difference for affective empathy."
  },
  {
   "claim_id": "C009",
   "loglog_ids": [
    "3.2"
   ],
   "claim_text": "Affective empathy earns only partial on caring: contagion can occur without concern.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Affective empathy gets \"~\" on \"capacity to care\": emotional contagion can happen involuntarily, without any real concern for the person",
   "reasoning": "Note 2 states the tilde and the without-concern condition exactly."
  },
  {
   "claim_id": "C010",
   "loglog_ids": [
    "3.3"
   ],
   "claim_text": "The sociopath resembles affective empathy plus sympathy clamped to an in-group, unregulated.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "the sociopath is close to the affective-empathy and sympathy columns clamped to a narrow in-group and stripped of regulation",
   "reasoning": "Note 6 matches the affective/sympathy clamp and loss of regulation."
  },
  {
   "claim_id": "C011",
   "loglog_ids": [
    "4"
   ],
   "claim_text": "Compassion alone combines caring, motivation to help, wide scope, and sustainability.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Motivation to help or act: ... compassion check ... Concern reaches beyond a vivid / similar in-group: ... compassion check ... Sustainable and scalable as a moral guide: ... compassion check",
   "reasoning": "Among the four components only compassion is checked on all listed rows."
  },
  {
   "claim_id": "C012",
   "loglog_ids": [
    "4.1"
   ],
   "claim_text": "Only compassion scores full marks on helping motivation and sustainable scalable guidance.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Motivation to help or act: affective partial, sympathy partial, compassion check ... Sustainable and scalable as a moral guide: cognitive partial, sympathy partial, compassion check",
   "reasoning": "Only compassion carries a check on both rows among components."
  },
  {
   "claim_id": "C013",
   "loglog_ids": [
    "4.2"
   ],
   "claim_text": "The Bloom and Singer pro-compassion case is a position, not a consensus.",
   "claim_type": "reported",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "the Bloom/Singer argument ... which is a position, not a consensus",
   "reasoning": "Note 4 states the position-not-consensus framing verbatim."
  },
  {
   "claim_id": "C014",
   "loglog_ids": [
    "5"
   ],
   "claim_text": "The psychopath keeps only cold instrumental control; the sociopath holds the affective cluster.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "cold instrumental control is the psychopath's one distinguishing possession, while a whole cluster of affective and caring rows belongs to the sociopath and not the psychopath",
   "reasoning": "Note 6 states both halves of the asymmetry."
  },
  {
   "claim_id": "C015",
   "loglog_ids": [
    "5.1"
   ],
   "claim_text": "Almost all psychopath traits recur degraded in sociopath; only control is psychopath-only.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "almost everything the psychopath has, the sociopath also has in degraded form, so the psychopath's one distinguishing possession is cold instrumental control",
   "reasoning": "Direct paraphrase preserving the quantifier 'almost' and the single distinguishing trait."
  },
  {
   "claim_id": "C016",
   "loglog_ids": [
    "5.2"
   ],
   "claim_text": "Emotion-sharing, caring, helping, guilt, and contagion rows belong to sociopath, not psychopath.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Block sociopath-only rows. Actually sharing / mirroring the emotion ... Capacity to genuinely care ... Motivation to help or act ... Produces guilt / remorse ... Risk of emotional contagion and burnout",
   "reasoning": "These rows are listed in the sociopath-only block, absent for psychopath."
  },
  {
   "claim_id": "C017",
   "loglog_ids": [
    "6"
   ],
   "claim_text": "The empath maximizes affect unregulated, so it is not the moral ideal.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "The empath is the affective column maxed out and unregulated ... it is not the moral ideal",
   "reasoning": "Note 10 states maxed-out/unregulated and not-the-moral-ideal."
  },
  {
   "claim_id": "C018",
   "loglog_ids": [
    "6.1"
   ],
   "claim_text": "The empath lights up sharing, contagion, and bias but fails boundary, scope, and scalability.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "it lights up emotion-sharing, contagion, and vividness bias while failing on boundary, scope, and scalability",
   "reasoning": "Note 10 lists exactly these successes and failures."
  },
  {
   "claim_id": "C019",
   "loglog_ids": [
    "6.2"
   ],
   "claim_text": "The altruist embodies compassion and the Light Triad: Kantianism, Humanism, Faith in Humanity.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "The altruist is the compassion column embodied, matching the research \"Light Triad\" (Kantianism, Humanism, and Faith in Humanity, from Kaufman et al., 2019)",
   "reasoning": "Note 10 names the same three Light Triad components for the altruist."
  },
  {
   "claim_id": "C020",
   "loglog_ids": [
    "6.3"
   ],
   "claim_text": "The integrated ideal alone scores well across every block, opposing both dark profiles.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "The integrated ideal is the only column that scores well across every block ... so it is the true opposite of both dark profiles at once",
   "reasoning": "Note 10 states only-column and true-opposite claims."
  },
  {
   "claim_id": "C021",
   "loglog_ids": [
    "6.4"
   ],
   "claim_text": "Kantianism inverts the manipulators row; only Faith in Humanity adds a new dimension.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "'Treats people as ends, not means' (Kantianism) is essentially the inverse of the 'manipulators' row ... Only 'Believes people are fundamentally good' (Faith in Humanity) adds a genuinely new dimension",
   "reasoning": "Note 11 states both the inversion and the sole new dimension."
  },
  {
   "claim_id": "C022",
   "loglog_ids": [
    "7"
   ],
   "claim_text": "The table limits its scope deliberately and treats dark columns as ideal types.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Etiology is deliberately left out as a row ... Treat these two columns as ideal types, not categories.",
   "reasoning": "Notes 7 and 8 support the deliberate scope limit and ideal-types framing."
  },
  {
   "claim_id": "C023",
   "loglog_ids": [
    "7.1"
   ],
   "claim_text": "Etiology stays out: causal origin is not a response shape.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "That is a claim about causes, not about the shape of the response, so it does not belong in a feature table.",
   "reasoning": "Note 7 gives the same causes-versus-response rationale."
  },
  {
   "claim_id": "C024",
   "loglog_ids": [
    "7.2"
   ],
   "claim_text": "Psychopath and sociopath are not formal diagnoses; both fall under antisocial personality disorder.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "\"psychopath\" and \"sociopath\" are not formal diagnoses. Both fall under Antisocial Personality Disorder",
   "reasoning": "Note 8 states both the non-diagnosis and APD inclusion."
  },
  {
   "claim_id": "C025",
   "loglog_ids": [
    "7.3"
   ],
   "claim_text": "Terminology varies; empathic concern and pop-psych sympathy differ from table usage.",
   "claim_type": "definition",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "usage varies across the literature. Some authors use \"empathic concern\" roughly where this table uses \"compassion,\" and pop-psych usage (e.g. Brené Brown) treats \"sympathy\" as inherently distancing.",
   "reasoning": "Note 9 states both terminology variants and the neutral research sense used."
  }
 ],
 "metrics": {
  "total_claims": 25,
  "supported": 25,
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
    "L002",
    "L003"
   ],
   "evidence_quote": "The matrix separates cognitive and affective empathy, sympathy, and compassion, then profiles psychopath, sociopath, empath, altruist, and integrated ideal. ... Four components sit left of the double rule; five dark-to-light profiles sit right.",
   "reasoning": "L002 names all four components and all five profiles; L003 captures the dark-to-light ordering and the left/right split. Organizing thesis fully intact."
  },
  {
   "point_id": "K02",
   "point_text": "Rows are ordered by the two dark profiles' contrast and split into four blocks separated by blank dividers: present in both, psychopath only, sociopath only, and neither.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L004"
   ],
   "evidence_quote": "Rows fall in four blocks: present in both, psychopath only, sociopath only, neither.",
   "reasoning": "All four block labels are reproduced exactly. The framing that ordering serves the dark-profile contrast is covered by the surrounding structure, core content intact."
  },
  {
   "point_id": "K03",
   "point_text": "Sympathy gets a partial (~) on modeling the other's mind because you can pity someone while badly misreading them; accurate understanding helps sympathy but is not constitutive of it, unlike cognitive empathy.",
   "weight": "Nice to have",
   "presence": "Present",
   "loglog_ids": [
    "L007"
   ],
   "evidence_quote": "Nuance: Sympathy earns only partial on modeling: pity can badly misread people.",
   "reasoning": "The partial mark and the reason (pity misreads) are both captured. The added contrast with cognitive empathy is a refinement, but the cell explanation is delivered."
  },
  {
   "point_id": "K04",
   "point_text": "Affective empathy gets a partial (~) on capacity to care because emotional contagion can occur involuntarily without real concern, e.g., catching someone's anxiety and wanting to get away from them.",
   "weight": "Nice to have",
   "presence": "Present",
   "loglog_ids": [
    "L010"
   ],
   "evidence_quote": "Nuance: Affective empathy earns only partial on caring: contagion can occur without concern.",
   "reasoning": "Partial mark and the contagion-without-concern reason both present. The anxiety example is dropped, but this is a Nice to have illustration and the claim is intact."
  },
  {
   "point_id": "K05",
   "point_text": "The manipulators/con-artist row is the sharpest diagnostic for the cognitive/affective split and is essentially the psychopath's signature: cognitive empathy alone is compatible with cruelty, since a con artist models minds precisely without resonating with or caring about them.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L005",
    "L006"
   ],
   "evidence_quote": "Cognitive empathy means accurate modeling, boundary, and control; it survives in manipulators. ... The psychopath column is essentially the cognitive-empathy column standing alone.",
   "reasoning": "L005 places cognitive empathy in manipulators, L006 makes the psychopath the cognitive column standing alone, which carries the separability-of-caring claim. The cruelty/coldness implication survives in the 'standing alone' formulation."
  },
  {
   "point_id": "K06",
   "point_text": "The sustainable-and-scalable row reflects the Bloom/Singer argument (Paul Bloom's Against Empathy and Tania Singer's compassion-training research); it is a position, not a consensus, and critics reply that compassion without empathic grounding risks becoming abstract or paternalistic.",
   "weight": "Must have",
   "presence": "Partial",
   "loglog_ids": [
    "L013",
    "L014"
   ],
   "evidence_quote": "Only compassion scores full marks on helping motivation and sustainable scalable guidance. ... The Bloom and Singer pro-compassion case is a position, not a consensus.",
   "reasoning": "The row, the Bloom/Singer attribution, and the 'position not a consensus' caveat are all present, but the critics' counterargument (compassion without empathic grounding risks becoming abstract or paternalistic) is entirely absent. A must-have qualifier element is dropped, capping this at Partial."
  },
  {
   "point_id": "K07",
   "point_text": "Boundary maintenance is the structural difference between affective empathy and everything else: affective empathy means partially merging with the other's state, which drives both its motivational power and its burnout and bias problems.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L008",
    "L009"
   ],
   "evidence_quote": "Affective empathy means sharing emotion, with contagion, burnout, and vividness bias. ... Affective empathy lacks boundary maintenance, unlike everything else in the table.",
   "reasoning": "L009 marks boundary maintenance as the distinguishing structural feature; L008 ties the merging to burnout and vividness bias. Mechanism and its consequences both captured."
  },
  {
   "point_id": "K08",
   "point_text": "Reading the two dark profiles as columns: the psychopath is close to the cognitive-empathy column standing alone (accurate modeling with affective and caring machinery deleted), while the sociopath is close to affective empathy and sympathy clamped to a narrow in-group and stripped of regulation; the psychopath's one distinguishing possession is cold instrumental control, while a whole cluster of affective and caring rows belongs to the sociopath and not the psychopath.",
   "weight": "Must have",
   "present": "",
   "presence": "Present",
   "loglog_ids": [
    "L006",
    "L011",
    "L015",
    "L016",
    "L017"
   ],
   "evidence_quote": "The psychopath keeps only cold instrumental control; the sociopath holds the affective cluster. ... only control is psychopath-only. ... The sociopath resembles affective empathy plus sympathy clamped to an in-group, unregulated.",
   "reasoning": "L011 gives the clamped, unregulated sociopath, L006 gives psychopath as cognitive column alone, and L015/L016/L017 give the control-only vs affective-cluster asymmetry. The full analytical payoff is captured."
  },
  {
   "point_id": "K09",
   "point_text": "Etiology is deliberately excluded as a row: psychopathy is often theorized as innate/temperamental and sociopathy as environmentally acquired, but that concerns causes rather than the shape of the response, so it does not belong in a feature table and would muddy the logic.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L023",
    "L024"
   ],
   "evidence_quote": "The table limits its scope deliberately. ... Etiology stays out: causal origin is not a response shape.",
   "reasoning": "The exclusion and its rationale (cause vs response shape) are stated. The innate/environmental detail is a supporting illustration but the scope decision and justification, which is what a reader needs, are intact."
  },
  {
   "point_id": "K10",
   "point_text": "Clinical caveat: 'psychopath' and 'sociopath' are not formal diagnoses; both fall under Antisocial Personality Disorder, and the split between them is a contested, largely theoretical convention. Treat the two columns as ideal types, not categories.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L023",
    "L025"
   ],
   "evidence_quote": "Psychopath and sociopath are not formal diagnoses; both fall under antisocial personality disorder. ... treats dark columns as ideal types.",
   "reasoning": "The not-formal-diagnoses claim, the ASPD grouping, and the ideal-type instruction are all present. The 'contested theoretical convention' clause is softened but the operative limiting qualifiers that prevent clinical misreading are captured."
  },
  {
   "point_id": "K11",
   "point_text": "Terminology caveat: usage varies across the literature, some authors use 'empathic concern' roughly where this table uses 'compassion', and pop-psych usage (e.g., Brené Brown) treats 'sympathy' as inherently distancing; this table uses the more neutral research sense.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L026"
   ],
   "evidence_quote": "Terminology varies; empathic concern and pop-psych sympathy differ from table usage.",
   "reasoning": "Captures usage variation, the 'empathic concern' term, and the pop-psych 'sympathy' divergence. The Brené Brown attribution is omitted but the semantic point defining the table's word choices is delivered."
  },
  {
   "point_id": "K12",
   "point_text": "The empath column is the affective column maxed out and unregulated, which is why it lights up emotion-sharing, contagion, and vividness bias while failing on boundary, scope, and scalability; it is the opposite of the psychopath's coldness but inherits the sociopath's distortions, so it is not the moral ideal.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L018",
    "L019"
   ],
   "evidence_quote": "The empath maximizes affect unregulated, so it is not the moral ideal. ... The empath lights up sharing, contagion, and bias but fails boundary, scope, and scalability.",
   "reasoning": "L018 gives maxed-out unregulated affect and the not-ideal verdict; L019 gives the exact set of failures. The core corrective claim is fully mapped."
  },
  {
   "point_id": "K13",
   "point_text": "The altruist column is the compassion column embodied and matches the research 'Light Triad' (Kantianism, Humanism, and Faith in Humanity, from Kaufman et al., 2019).",
   "weight": "Nice to have",
   "presence": "Present",
   "loglog_ids": [
    "L020"
   ],
   "evidence_quote": "The altruist embodies compassion and the Light Triad: Kantianism, Humanism, Faith in Humanity.",
   "reasoning": "Compassion embodiment and all three Light Triad components are present. The Kaufman 2019 citation is dropped but that is a secondary attribution on a Nice to have point."
  },
  {
   "point_id": "K14",
   "point_text": "The integrated ideal is the only column that scores well across every block, including the 'present in neither' rows, so it is the true opposite of both dark profiles at once.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L021"
   ],
   "evidence_quote": "The integrated ideal alone scores well across every block, opposing both dark profiles.",
   "reasoning": "Uniqueness (alone), all-block coverage, and dual opposition to both dark profiles are all present. Normative endpoint captured."
  },
  {
   "point_id": "K15",
   "point_text": "The three Light Triad rows partly restate earlier rows: Kantianism is essentially the inverse of the manipulators row, Humanism overlaps the caring and beyond-the-in-group rows, and only Faith in Humanity adds a genuinely new dimension (an attitude rather than an empathy component), which is why both dark profiles score blank on it.",
   "weight": "Must have",
   "presence": "Partial",
   "loglog_ids": [
    "L022"
   ],
   "evidence_quote": "Kantianism inverts the manipulators row; only Faith in Humanity adds a new dimension.",
   "reasoning": "The redundancy thesis and the novel-Faith row are captured, and the Kantianism/manipulators mapping is present. However the Humanism overlap mapping and the explanation for why both dark profiles go blank on Faith in Humanity are dropped, so this must-have loses some of its justifying detail."
  }
 ],
 "metrics": {
  "total_points": 15,
  "must_have_total": 12,
  "must_have_present": 10,
  "must_have_partial": 2,
  "must_have_missing": 0,
  "overall_present": 13,
  "must_recall": 0.9167,
  "overall_recall": 0.9333
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
   "claim_text": "The matrix separates cognitive and affective empathy, sympathy, and compassion, then profiles psychopath, sociopath, empath, altruist, and integrated ideal.",
   "claim_type": "definition",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "The four component columns (cognitive and affective empathy, sympathy, compassion) sit left of the double rule. The five to the right are whole-person profiles ... psychopath, sociopath, empath, altruist, and the integrated ideal.",
   "reasoning": "Source names the same four components and five profiles in the same order."
  },
  {
   "claim_id": "C002",
   "loglog_ids": [
    "1"
   ],
   "claim_text": "Four components sit left of the double rule; five dark-to-light profiles sit right.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "The four component columns ... sit left of the double rule. The five to the right are whole-person profiles, arranged darkest to lightest",
   "reasoning": "Direct restatement of source layout and darkest-to-lightest ordering."
  },
  {
   "claim_id": "C003",
   "loglog_ids": [
    "1.1"
   ],
   "claim_text": "Rows fall in four blocks: present in both, psychopath only, sociopath only, neither.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "four blocks separated by blank dividers: present in both, in the psychopath only, in the sociopath only, and in neither.",
   "reasoning": "Exact parallel to the source's four block names."
  },
  {
   "claim_id": "C004",
   "loglog_ids": [
    "2"
   ],
   "claim_text": "Cognitive empathy means accurate modeling, boundary, and control; it survives in manipulators.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Can exist in manipulators / con artists: cognitive check only ... Controlled / instrumental rather than reactive / impulsive: cognitive check",
   "reasoning": "Table gives cognitive checks on modeling, boundary, manipulators, and control as stated."
  },
  {
   "claim_id": "C005",
   "loglog_ids": [
    "2.1"
   ],
   "claim_text": "The psychopath column is essentially the cognitive-empathy column standing alone.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "the psychopath is close to the cognitive-empathy column standing alone",
   "reasoning": "Note 6 and Note 10 both state this; 'essentially' matches 'standing alone'."
  },
  {
   "claim_id": "C006",
   "loglog_ids": [
    "2.2"
   ],
   "claim_text": "Sympathy earns only partial on modeling: pity can badly misread people.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Sympathy gets \"~\" on modeling the other's mind because you can pity someone while badly misreading them.",
   "reasoning": "Source explicitly gives sympathy a tilde for misreading while pitying."
  },
  {
   "claim_id": "C007",
   "loglog_ids": [
    "3"
   ],
   "claim_text": "Affective empathy means sharing emotion, with contagion, burnout, and vividness bias.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Actually sharing / mirroring the emotion ... Risk of emotional contagion and burnout: affective check ... Biased toward vivid, similar individuals: ... affective check",
   "reasoning": "Table assigns affective checks to sharing, contagion/burnout, and vividness bias."
  },
  {
   "claim_id": "C008",
   "loglog_ids": [
    "3.1"
   ],
   "claim_text": "Affective empathy lacks boundary maintenance, unlike everything else in the table.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Boundary maintenance is the structural difference between affective empathy and everything else in the table",
   "reasoning": "Note 5 states boundary is the structural difference for affective empathy."
  },
  {
   "claim_id": "C009",
   "loglog_ids": [
    "3.2"
   ],
   "claim_text": "Affective empathy earns only partial on caring: contagion can occur without concern.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Affective empathy gets \"~\" on \"capacity to care\": emotional contagion can happen involuntarily, without any real concern for the person",
   "reasoning": "Note 2 states the tilde and the without-concern condition exactly."
  },
  {
   "claim_id": "C010",
   "loglog_ids": [
    "3.3"
   ],
   "claim_text": "The sociopath resembles affective empathy plus sympathy clamped to an in-group, unregulated.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "the sociopath is close to the affective-empathy and sympathy columns clamped to a narrow in-group and stripped of regulation",
   "reasoning": "Note 6 matches the affective/sympathy clamp and loss of regulation."
  },
  {
   "claim_id": "C011",
   "loglog_ids": [
    "4"
   ],
   "claim_text": "Compassion alone combines caring, motivation to help, wide scope, and sustainability.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Motivation to help or act: ... compassion check ... Concern reaches beyond a vivid / similar in-group: ... compassion check ... Sustainable and scalable as a moral guide: ... compassion check",
   "reasoning": "Among the four components only compassion is checked on all listed rows."
  },
  {
   "claim_id": "C012",
   "loglog_ids": [
    "4.1"
   ],
   "claim_text": "Only compassion scores full marks on helping motivation and sustainable scalable guidance.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Motivation to help or act: affective partial, sympathy partial, compassion check ... Sustainable and scalable as a moral guide: cognitive partial, sympathy partial, compassion check",
   "reasoning": "Only compassion carries a check on both rows among components."
  },
  {
   "claim_id": "C013",
   "loglog_ids": [
    "4.2"
   ],
   "claim_text": "The Bloom and Singer pro-compassion case is a position, not a consensus.",
   "claim_type": "reported",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "the Bloom/Singer argument ... which is a position, not a consensus",
   "reasoning": "Note 4 states the position-not-consensus framing verbatim."
  },
  {
   "claim_id": "C014",
   "loglog_ids": [
    "5"
   ],
   "claim_text": "The psychopath keeps only cold instrumental control; the sociopath holds the affective cluster.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "cold instrumental control is the psychopath's one distinguishing possession, while a whole cluster of affective and caring rows belongs to the sociopath and not the psychopath",
   "reasoning": "Note 6 states both halves of the asymmetry."
  },
  {
   "claim_id": "C015",
   "loglog_ids": [
    "5.1"
   ],
   "claim_text": "Almost all psychopath traits recur degraded in sociopath; only control is psychopath-only.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "almost everything the psychopath has, the sociopath also has in degraded form, so the psychopath's one distinguishing possession is cold instrumental control",
   "reasoning": "Direct paraphrase preserving the quantifier 'almost' and the single distinguishing trait."
  },
  {
   "claim_id": "C016",
   "loglog_ids": [
    "5.2"
   ],
   "claim_text": "Emotion-sharing, caring, helping, guilt, and contagion rows belong to sociopath, not psychopath.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Block sociopath-only rows. Actually sharing / mirroring the emotion ... Capacity to genuinely care ... Motivation to help or act ... Produces guilt / remorse ... Risk of emotional contagion and burnout",
   "reasoning": "These rows are listed in the sociopath-only block, absent for psychopath."
  },
  {
   "claim_id": "C017",
   "loglog_ids": [
    "6"
   ],
   "claim_text": "The empath maximizes affect unregulated, so it is not the moral ideal.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "The empath is the affective column maxed out and unregulated ... it is not the moral ideal",
   "reasoning": "Note 10 states maxed-out/unregulated and not-the-moral-ideal."
  },
  {
   "claim_id": "C018",
   "loglog_ids": [
    "6.1"
   ],
   "claim_text": "The empath lights up sharing, contagion, and bias but fails boundary, scope, and scalability.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "it lights up emotion-sharing, contagion, and vividness bias while failing on boundary, scope, and scalability",
   "reasoning": "Note 10 lists exactly these successes and failures."
  },
  {
   "claim_id": "C019",
   "loglog_ids": [
    "6.2"
   ],
   "claim_text": "The altruist embodies compassion and the Light Triad: Kantianism, Humanism, Faith in Humanity.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "The altruist is the compassion column embodied, matching the research \"Light Triad\" (Kantianism, Humanism, and Faith in Humanity, from Kaufman et al., 2019)",
   "reasoning": "Note 10 names the same three Light Triad components for the altruist."
  },
  {
   "claim_id": "C020",
   "loglog_ids": [
    "6.3"
   ],
   "claim_text": "The integrated ideal alone scores well across every block, opposing both dark profiles.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "The integrated ideal is the only column that scores well across every block ... so it is the true opposite of both dark profiles at once",
   "reasoning": "Note 10 states only-column and true-opposite claims."
  },
  {
   "claim_id": "C021",
   "loglog_ids": [
    "6.4"
   ],
   "claim_text": "Kantianism inverts the manipulators row; only Faith in Humanity adds a new dimension.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "'Treats people as ends, not means' (Kantianism) is essentially the inverse of the 'manipulators' row ... Only 'Believes people are fundamentally good' (Faith in Humanity) adds a genuinely new dimension",
   "reasoning": "Note 11 states both the inversion and the sole new dimension."
  },
  {
   "claim_id": "C022",
   "loglog_ids": [
    "7"
   ],
   "claim_text": "The table limits its scope deliberately and treats dark columns as ideal types.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Etiology is deliberately left out as a row ... Treat these two columns as ideal types, not categories.",
   "reasoning": "Notes 7 and 8 support the deliberate scope limit and ideal-types framing."
  },
  {
   "claim_id": "C023",
   "loglog_ids": [
    "7.1"
   ],
   "claim_text": "Etiology stays out: causal origin is not a response shape.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "That is a claim about causes, not about the shape of the response, so it does not belong in a feature table.",
   "reasoning": "Note 7 gives the same causes-versus-response rationale."
  },
  {
   "claim_id": "C024",
   "loglog_ids": [
    "7.2"
   ],
   "claim_text": "Psychopath and sociopath are not formal diagnoses; both fall under antisocial personality disorder.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "\"psychopath\" and \"sociopath\" are not formal diagnoses. Both fall under Antisocial Personality Disorder",
   "reasoning": "Note 8 states both the non-diagnosis and APD inclusion."
  },
  {
   "claim_id": "C025",
   "loglog_ids": [
    "7.3"
   ],
   "claim_text": "Terminology varies; empathic concern and pop-psych sympathy differ from table usage.",
   "claim_type": "definition",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "usage varies across the literature. Some authors use \"empathic concern\" roughly where this table uses \"compassion,\" and pop-psych usage (e.g. Brené Brown) treats \"sympathy\" as inherently distancing.",
   "reasoning": "Note 9 states both terminology variants and the neutral research sense used."
  }
 ],
 "metrics": {
  "total_claims": 25,
  "supported": 25,
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
    "L002",
    "L003"
   ],
   "evidence_quote": "The matrix separates cognitive and affective empathy, sympathy, and compassion, then profiles psychopath, sociopath, empath, altruist, and integrated ideal. ... Four components sit left of the double rule; five dark-to-light profiles sit right.",
   "reasoning": "L002 names all four components and all five profiles; L003 captures the dark-to-light ordering and the left/right split. Organizing thesis fully intact."
  },
  {
   "point_id": "K02",
   "point_text": "Rows are ordered by the two dark profiles' contrast and split into four blocks separated by blank dividers: present in both, psychopath only, sociopath only, and neither.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L004"
   ],
   "evidence_quote": "Rows fall in four blocks: present in both, psychopath only, sociopath only, neither.",
   "reasoning": "All four block labels are reproduced exactly. The framing that ordering serves the dark-profile contrast is covered by the surrounding structure, core content intact."
  },
  {
   "point_id": "K03",
   "point_text": "Sympathy gets a partial (~) on modeling the other's mind because you can pity someone while badly misreading them; accurate understanding helps sympathy but is not constitutive of it, unlike cognitive empathy.",
   "weight": "Nice to have",
   "presence": "Present",
   "loglog_ids": [
    "L007"
   ],
   "evidence_quote": "Nuance: Sympathy earns only partial on modeling: pity can badly misread people.",
   "reasoning": "The partial mark and the reason (pity misreads) are both captured. The added contrast with cognitive empathy is a refinement, but the cell explanation is delivered."
  },
  {
   "point_id": "K04",
   "point_text": "Affective empathy gets a partial (~) on capacity to care because emotional contagion can occur involuntarily without real concern, e.g., catching someone's anxiety and wanting to get away from them.",
   "weight": "Nice to have",
   "presence": "Present",
   "loglog_ids": [
    "L010"
   ],
   "evidence_quote": "Nuance: Affective empathy earns only partial on caring: contagion can occur without concern.",
   "reasoning": "Partial mark and the contagion-without-concern reason both present. The anxiety example is dropped, but this is a Nice to have illustration and the claim is intact."
  },
  {
   "point_id": "K05",
   "point_text": "The manipulators/con-artist row is the sharpest diagnostic for the cognitive/affective split and is essentially the psychopath's signature: cognitive empathy alone is compatible with cruelty, since a con artist models minds precisely without resonating with or caring about them.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L005",
    "L006"
   ],
   "evidence_quote": "Cognitive empathy means accurate modeling, boundary, and control; it survives in manipulators. ... The psychopath column is essentially the cognitive-empathy column standing alone.",
   "reasoning": "L005 places cognitive empathy in manipulators, L006 makes the psychopath the cognitive column standing alone, which carries the separability-of-caring claim. The cruelty/coldness implication survives in the 'standing alone' formulation."
  },
  {
   "point_id": "K06",
   "point_text": "The sustainable-and-scalable row reflects the Bloom/Singer argument (Paul Bloom's Against Empathy and Tania Singer's compassion-training research); it is a position, not a consensus, and critics reply that compassion without empathic grounding risks becoming abstract or paternalistic.",
   "weight": "Must have",
   "presence": "Partial",
   "loglog_ids": [
    "L013",
    "L014"
   ],
   "evidence_quote": "Only compassion scores full marks on helping motivation and sustainable scalable guidance. ... The Bloom and Singer pro-compassion case is a position, not a consensus.",
   "reasoning": "The row, the Bloom/Singer attribution, and the 'position not a consensus' caveat are all present, but the critics' counterargument (compassion without empathic grounding risks becoming abstract or paternalistic) is entirely absent. A must-have qualifier element is dropped, capping this at Partial."
  },
  {
   "point_id": "K07",
   "point_text": "Boundary maintenance is the structural difference between affective empathy and everything else: affective empathy means partially merging with the other's state, which drives both its motivational power and its burnout and bias problems.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L008",
    "L009"
   ],
   "evidence_quote": "Affective empathy means sharing emotion, with contagion, burnout, and vividness bias. ... Affective empathy lacks boundary maintenance, unlike everything else in the table.",
   "reasoning": "L009 marks boundary maintenance as the distinguishing structural feature; L008 ties the merging to burnout and vividness bias. Mechanism and its consequences both captured."
  },
  {
   "point_id": "K08",
   "point_text": "Reading the two dark profiles as columns: the psychopath is close to the cognitive-empathy column standing alone (accurate modeling with affective and caring machinery deleted), while the sociopath is close to affective empathy and sympathy clamped to a narrow in-group and stripped of regulation; the psychopath's one distinguishing possession is cold instrumental control, while a whole cluster of affective and caring rows belongs to the sociopath and not the psychopath.",
   "weight": "Must have",
   "present": "",
   "presence": "Present",
   "loglog_ids": [
    "L006",
    "L011",
    "L015",
    "L016",
    "L017"
   ],
   "evidence_quote": "The psychopath keeps only cold instrumental control; the sociopath holds the affective cluster. ... only control is psychopath-only. ... The sociopath resembles affective empathy plus sympathy clamped to an in-group, unregulated.",
   "reasoning": "L011 gives the clamped, unregulated sociopath, L006 gives psychopath as cognitive column alone, and L015/L016/L017 give the control-only vs affective-cluster asymmetry. The full analytical payoff is captured."
  },
  {
   "point_id": "K09",
   "point_text": "Etiology is deliberately excluded as a row: psychopathy is often theorized as innate/temperamental and sociopathy as environmentally acquired, but that concerns causes rather than the shape of the response, so it does not belong in a feature table and would muddy the logic.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L023",
    "L024"
   ],
   "evidence_quote": "The table limits its scope deliberately. ... Etiology stays out: causal origin is not a response shape.",
   "reasoning": "The exclusion and its rationale (cause vs response shape) are stated. The innate/environmental detail is a supporting illustration but the scope decision and justification, which is what a reader needs, are intact."
  },
  {
   "point_id": "K10",
   "point_text": "Clinical caveat: 'psychopath' and 'sociopath' are not formal diagnoses; both fall under Antisocial Personality Disorder, and the split between them is a contested, largely theoretical convention. Treat the two columns as ideal types, not categories.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L023",
    "L025"
   ],
   "evidence_quote": "Psychopath and sociopath are not formal diagnoses; both fall under antisocial personality disorder. ... treats dark columns as ideal types.",
   "reasoning": "The not-formal-diagnoses claim, the ASPD grouping, and the ideal-type instruction are all present. The 'contested theoretical convention' clause is softened but the operative limiting qualifiers that prevent clinical misreading are captured."
  },
  {
   "point_id": "K11",
   "point_text": "Terminology caveat: usage varies across the literature, some authors use 'empathic concern' roughly where this table uses 'compassion', and pop-psych usage (e.g., Brené Brown) treats 'sympathy' as inherently distancing; this table uses the more neutral research sense.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L026"
   ],
   "evidence_quote": "Terminology varies; empathic concern and pop-psych sympathy differ from table usage.",
   "reasoning": "Captures usage variation, the 'empathic concern' term, and the pop-psych 'sympathy' divergence. The Brené Brown attribution is omitted but the semantic point defining the table's word choices is delivered."
  },
  {
   "point_id": "K12",
   "point_text": "The empath column is the affective column maxed out and unregulated, which is why it lights up emotion-sharing, contagion, and vividness bias while failing on boundary, scope, and scalability; it is the opposite of the psychopath's coldness but inherits the sociopath's distortions, so it is not the moral ideal.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L018",
    "L019"
   ],
   "evidence_quote": "The empath maximizes affect unregulated, so it is not the moral ideal. ... The empath lights up sharing, contagion, and bias but fails boundary, scope, and scalability.",
   "reasoning": "L018 gives maxed-out unregulated affect and the not-ideal verdict; L019 gives the exact set of failures. The core corrective claim is fully mapped."
  },
  {
   "point_id": "K13",
   "point_text": "The altruist column is the compassion column embodied and matches the research 'Light Triad' (Kantianism, Humanism, and Faith in Humanity, from Kaufman et al., 2019).",
   "weight": "Nice to have",
   "presence": "Present",
   "loglog_ids": [
    "L020"
   ],
   "evidence_quote": "The altruist embodies compassion and the Light Triad: Kantianism, Humanism, Faith in Humanity.",
   "reasoning": "Compassion embodiment and all three Light Triad components are present. The Kaufman 2019 citation is dropped but that is a secondary attribution on a Nice to have point."
  },
  {
   "point_id": "K14",
   "point_text": "The integrated ideal is the only column that scores well across every block, including the 'present in neither' rows, so it is the true opposite of both dark profiles at once.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L021"
   ],
   "evidence_quote": "The integrated ideal alone scores well across every block, opposing both dark profiles.",
   "reasoning": "Uniqueness (alone), all-block coverage, and dual opposition to both dark profiles are all present. Normative endpoint captured."
  },
  {
   "point_id": "K15",
   "point_text": "The three Light Triad rows partly restate earlier rows: Kantianism is essentially the inverse of the manipulators row, Humanism overlaps the caring and beyond-the-in-group rows, and only Faith in Humanity adds a genuinely new dimension (an attitude rather than an empathy component), which is why both dark profiles score blank on it.",
   "weight": "Must have",
   "presence": "Partial",
   "loglog_ids": [
    "L022"
   ],
   "evidence_quote": "Kantianism inverts the manipulators row; only Faith in Humanity adds a new dimension.",
   "reasoning": "The redundancy thesis and the novel-Faith row are captured, and the Kantianism/manipulators mapping is present. However the Humanism overlap mapping and the explanation for why both dark profiles go blank on Faith in Humanity are dropped, so this must-have loses some of its justifying detail."
  }
 ],
 "metrics": {
  "total_points": 15,
  "must_have_total": 12,
  "must_have_present": 10,
  "must_have_partial": 2,
  "must_have_missing": 0,
  "overall_present": 13,
  "must_recall": 0.9167,
  "overall_recall": 0.9333
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
    "L002"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Summary names all four components and five profiles, the document's core inventory."
  },
  {
   "claim_id": "C002",
   "loglog_ids": [
    "L003"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Adds left/right layout of the double rule, not stated elsewhere."
  },
  {
   "claim_id": "C003",
   "loglog_ids": [
    "L004"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Introduces the four row blocks, a distinct structural axis."
  },
  {
   "claim_id": "C004",
   "loglog_ids": [
    "L005"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Defines cognitive empathy's parts and survival in manipulators."
  },
  {
   "claim_id": "C005",
   "loglog_ids": [
    "L006"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Maps the psychopath column onto cognitive empathy, new evidence."
  },
  {
   "claim_id": "C006",
   "loglog_ids": [
    "L007"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Sympathy partial-modeling caveat is new."
  },
  {
   "claim_id": "C007",
   "loglog_ids": [
    "L008"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Defines affective empathy's sharing, contagion, burnout, bias."
  },
  {
   "claim_id": "C008",
   "loglog_ids": [
    "L009"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Missing boundary is a distinct structural nuance of affective empathy."
  },
  {
   "claim_id": "C009",
   "loglog_ids": [
    "L010"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Contagion-without-concern limits affective empathy; new caveat."
  },
  {
   "claim_id": "C010",
   "loglog_ids": [
    "L011"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Sociopath's clamped affective composition is new content."
  },
  {
   "claim_id": "C011",
   "loglog_ids": [
    "L012"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Compassion's four-part combination is the branch's core claim."
  },
  {
   "claim_id": "C012",
   "loglog_ids": [
    "L013"
   ],
   "label": "Duplicate",
   "canonical_id": "C011",
   "reasoning": "Restates compassion alone leading helping and sustainability; adds no information."
  },
  {
   "claim_id": "C013",
   "loglog_ids": [
    "L014"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Bloom and Singer position caveat is new."
  },
  {
   "claim_id": "C014",
   "loglog_ids": [
    "L015"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Psychopath/sociopath control split is the branch's core claim."
  },
  {
   "claim_id": "C015",
   "loglog_ids": [
    "L016"
   ],
   "label": "Duplicate",
   "canonical_id": "C014",
   "reasoning": "Only control being psychopath-only restates C014; degradation nuance is minor."
  },
  {
   "claim_id": "C016",
   "loglog_ids": [
    "L017"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Enumerates specific affective rows owned by sociopath; new detail."
  },
  {
   "claim_id": "C017",
   "loglog_ids": [
    "L018"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Empath is not the moral ideal; new verdict."
  },
  {
   "claim_id": "C018",
   "loglog_ids": [
    "L019"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Lists empat's specific failed dimensions; new evidence."
  },
  {
   "claim_id": "C019",
   "loglog_ids": [
    "L020"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Altruist's Light Triad mapping is new."
  },
  {
   "claim_id": "C020",
   "loglog_ids": [
    "L021"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Integrated ideal scoring across every block is new."
  },
  {
   "claim_id": "C021",
   "loglog_ids": [
    "L022"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Kantianism inversion nuance is new."
  },
  {
   "claim_id": "C022",
   "loglog_ids": [
    "L023"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Deliberate scope and ideal-type disclaimer is new."
  },
  {
   "claim_id": "C023",
   "loglog_ids": [
    "L024"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Etiology exclusion is new."
  },
  {
   "claim_id": "C024",
   "loglog_ids": [
    "L025"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "ASPD non-diagnosis fact is new."
  },
  {
   "claim_id": "C025",
   "loglog_ids": [
    "L026"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Terminology divergence caveat is new."
  }
 ],
 "metrics": {
  "scored_claims": 25,
  "unique": 23,
  "duplicates": 2,
  "trivia": 0,
  "redundancy_rate": 0.08,
  "trivia_rate": 0.0,
  "structured_tokens": 308,
  "tokens_per_unique_claim": 13.39
 },
 "prune_list": [
  "C012 duplicates C011, safe to merge",
  "C015 duplicates C014, safe to merge"
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
   "claim_text": "The matrix separates cognitive and affective empathy, sympathy, and compassion, then profiles psychopath, sociopath, empath, altruist, and integrated ideal.",
   "claim_type": "definition",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "The four component columns (cognitive and affective empathy, sympathy, compassion) sit left of the double rule. The five to the right are whole-person profiles ... psychopath, sociopath, empath, altruist, and the integrated ideal.",
   "reasoning": "Source names the same four components and five profiles in the same order."
  },
  {
   "claim_id": "C002",
   "loglog_ids": [
    "1"
   ],
   "claim_text": "Four components sit left of the double rule; five dark-to-light profiles sit right.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "The four component columns ... sit left of the double rule. The five to the right are whole-person profiles, arranged darkest to lightest",
   "reasoning": "Direct restatement of source layout and darkest-to-lightest ordering."
  },
  {
   "claim_id": "C003",
   "loglog_ids": [
    "1.1"
   ],
   "claim_text": "Rows fall in four blocks: present in both, psychopath only, sociopath only, neither.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "four blocks separated by blank dividers: present in both, in the psychopath only, in the sociopath only, and in neither.",
   "reasoning": "Exact parallel to the source's four block names."
  },
  {
   "claim_id": "C004",
   "loglog_ids": [
    "2"
   ],
   "claim_text": "Cognitive empathy means accurate modeling, boundary, and control; it survives in manipulators.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Can exist in manipulators / con artists: cognitive check only ... Controlled / instrumental rather than reactive / impulsive: cognitive check",
   "reasoning": "Table gives cognitive checks on modeling, boundary, manipulators, and control as stated."
  },
  {
   "claim_id": "C005",
   "loglog_ids": [
    "2.1"
   ],
   "claim_text": "The psychopath column is essentially the cognitive-empathy column standing alone.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "the psychopath is close to the cognitive-empathy column standing alone",
   "reasoning": "Note 6 and Note 10 both state this; 'essentially' matches 'standing alone'."
  },
  {
   "claim_id": "C006",
   "loglog_ids": [
    "2.2"
   ],
   "claim_text": "Sympathy earns only partial on modeling: pity can badly misread people.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Sympathy gets \"~\" on modeling the other's mind because you can pity someone while badly misreading them.",
   "reasoning": "Source explicitly gives sympathy a tilde for misreading while pitying."
  },
  {
   "claim_id": "C007",
   "loglog_ids": [
    "3"
   ],
   "claim_text": "Affective empathy means sharing emotion, with contagion, burnout, and vividness bias.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Actually sharing / mirroring the emotion ... Risk of emotional contagion and burnout: affective check ... Biased toward vivid, similar individuals: ... affective check",
   "reasoning": "Table assigns affective checks to sharing, contagion/burnout, and vividness bias."
  },
  {
   "claim_id": "C008",
   "loglog_ids": [
    "3.1"
   ],
   "claim_text": "Affective empathy lacks boundary maintenance, unlike everything else in the table.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Boundary maintenance is the structural difference between affective empathy and everything else in the table",
   "reasoning": "Note 5 states boundary is the structural difference for affective empathy."
  },
  {
   "claim_id": "C009",
   "loglog_ids": [
    "3.2"
   ],
   "claim_text": "Affective empathy earns only partial on caring: contagion can occur without concern.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Affective empathy gets \"~\" on \"capacity to care\": emotional contagion can happen involuntarily, without any real concern for the person",
   "reasoning": "Note 2 states the tilde and the without-concern condition exactly."
  },
  {
   "claim_id": "C010",
   "loglog_ids": [
    "3.3"
   ],
   "claim_text": "The sociopath resembles affective empathy plus sympathy clamped to an in-group, unregulated.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "the sociopath is close to the affective-empathy and sympathy columns clamped to a narrow in-group and stripped of regulation",
   "reasoning": "Note 6 matches the affective/sympathy clamp and loss of regulation."
  },
  {
   "claim_id": "C011",
   "loglog_ids": [
    "4"
   ],
   "claim_text": "Compassion alone combines caring, motivation to help, wide scope, and sustainability.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Motivation to help or act: ... compassion check ... Concern reaches beyond a vivid / similar in-group: ... compassion check ... Sustainable and scalable as a moral guide: ... compassion check",
   "reasoning": "Among the four components only compassion is checked on all listed rows."
  },
  {
   "claim_id": "C012",
   "loglog_ids": [
    "4.1"
   ],
   "claim_text": "Only compassion scores full marks on helping motivation and sustainable scalable guidance.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Motivation to help or act: affective partial, sympathy partial, compassion check ... Sustainable and scalable as a moral guide: cognitive partial, sympathy partial, compassion check",
   "reasoning": "Only compassion carries a check on both rows among components."
  },
  {
   "claim_id": "C013",
   "loglog_ids": [
    "4.2"
   ],
   "claim_text": "The Bloom and Singer pro-compassion case is a position, not a consensus.",
   "claim_type": "reported",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "the Bloom/Singer argument ... which is a position, not a consensus",
   "reasoning": "Note 4 states the position-not-consensus framing verbatim."
  },
  {
   "claim_id": "C014",
   "loglog_ids": [
    "5"
   ],
   "claim_text": "The psychopath keeps only cold instrumental control; the sociopath holds the affective cluster.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "cold instrumental control is the psychopath's one distinguishing possession, while a whole cluster of affective and caring rows belongs to the sociopath and not the psychopath",
   "reasoning": "Note 6 states both halves of the asymmetry."
  },
  {
   "claim_id": "C015",
   "loglog_ids": [
    "5.1"
   ],
   "claim_text": "Almost all psychopath traits recur degraded in sociopath; only control is psychopath-only.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "almost everything the psychopath has, the sociopath also has in degraded form, so the psychopath's one distinguishing possession is cold instrumental control",
   "reasoning": "Direct paraphrase preserving the quantifier 'almost' and the single distinguishing trait."
  },
  {
   "claim_id": "C016",
   "loglog_ids": [
    "5.2"
   ],
   "claim_text": "Emotion-sharing, caring, helping, guilt, and contagion rows belong to sociopath, not psychopath.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Block sociopath-only rows. Actually sharing / mirroring the emotion ... Capacity to genuinely care ... Motivation to help or act ... Produces guilt / remorse ... Risk of emotional contagion and burnout",
   "reasoning": "These rows are listed in the sociopath-only block, absent for psychopath."
  },
  {
   "claim_id": "C017",
   "loglog_ids": [
    "6"
   ],
   "claim_text": "The empath maximizes affect unregulated, so it is not the moral ideal.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "The empath is the affective column maxed out and unregulated ... it is not the moral ideal",
   "reasoning": "Note 10 states maxed-out/unregulated and not-the-moral-ideal."
  },
  {
   "claim_id": "C018",
   "loglog_ids": [
    "6.1"
   ],
   "claim_text": "The empath lights up sharing, contagion, and bias but fails boundary, scope, and scalability.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "it lights up emotion-sharing, contagion, and vividness bias while failing on boundary, scope, and scalability",
   "reasoning": "Note 10 lists exactly these successes and failures."
  },
  {
   "claim_id": "C019",
   "loglog_ids": [
    "6.2"
   ],
   "claim_text": "The altruist embodies compassion and the Light Triad: Kantianism, Humanism, Faith in Humanity.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "The altruist is the compassion column embodied, matching the research \"Light Triad\" (Kantianism, Humanism, and Faith in Humanity, from Kaufman et al., 2019)",
   "reasoning": "Note 10 names the same three Light Triad components for the altruist."
  },
  {
   "claim_id": "C020",
   "loglog_ids": [
    "6.3"
   ],
   "claim_text": "The integrated ideal alone scores well across every block, opposing both dark profiles.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "The integrated ideal is the only column that scores well across every block ... so it is the true opposite of both dark profiles at once",
   "reasoning": "Note 10 states only-column and true-opposite claims."
  },
  {
   "claim_id": "C021",
   "loglog_ids": [
    "6.4"
   ],
   "claim_text": "Kantianism inverts the manipulators row; only Faith in Humanity adds a new dimension.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "'Treats people as ends, not means' (Kantianism) is essentially the inverse of the 'manipulators' row ... Only 'Believes people are fundamentally good' (Faith in Humanity) adds a genuinely new dimension",
   "reasoning": "Note 11 states both the inversion and the sole new dimension."
  },
  {
   "claim_id": "C022",
   "loglog_ids": [
    "7"
   ],
   "claim_text": "The table limits its scope deliberately and treats dark columns as ideal types.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Etiology is deliberately left out as a row ... Treat these two columns as ideal types, not categories.",
   "reasoning": "Notes 7 and 8 support the deliberate scope limit and ideal-types framing."
  },
  {
   "claim_id": "C023",
   "loglog_ids": [
    "7.1"
   ],
   "claim_text": "Etiology stays out: causal origin is not a response shape.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "That is a claim about causes, not about the shape of the response, so it does not belong in a feature table.",
   "reasoning": "Note 7 gives the same causes-versus-response rationale."
  },
  {
   "claim_id": "C024",
   "loglog_ids": [
    "7.2"
   ],
   "claim_text": "Psychopath and sociopath are not formal diagnoses; both fall under antisocial personality disorder.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "\"psychopath\" and \"sociopath\" are not formal diagnoses. Both fall under Antisocial Personality Disorder",
   "reasoning": "Note 8 states both the non-diagnosis and APD inclusion."
  },
  {
   "claim_id": "C025",
   "loglog_ids": [
    "7.3"
   ],
   "claim_text": "Terminology varies; empathic concern and pop-psych sympathy differ from table usage.",
   "claim_type": "definition",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "usage varies across the literature. Some authors use \"empathic concern\" roughly where this table uses \"compassion,\" and pop-psych usage (e.g. Brené Brown) treats \"sympathy\" as inherently distancing.",
   "reasoning": "Note 9 states both terminology variants and the neutral research sense used."
  }
 ],
 "metrics": {
  "total_claims": 25,
  "supported": 25,
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
    "L002",
    "L003"
   ],
   "evidence_quote": "The matrix separates cognitive and affective empathy, sympathy, and compassion, then profiles psychopath, sociopath, empath, altruist, and integrated ideal. ... Four components sit left of the double rule; five dark-to-light profiles sit right.",
   "reasoning": "L002 names all four components and all five profiles; L003 captures the dark-to-light ordering and the left/right split. Organizing thesis fully intact."
  },
  {
   "point_id": "K02",
   "point_text": "Rows are ordered by the two dark profiles' contrast and split into four blocks separated by blank dividers: present in both, psychopath only, sociopath only, and neither.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L004"
   ],
   "evidence_quote": "Rows fall in four blocks: present in both, psychopath only, sociopath only, neither.",
   "reasoning": "All four block labels are reproduced exactly. The framing that ordering serves the dark-profile contrast is covered by the surrounding structure, core content intact."
  },
  {
   "point_id": "K03",
   "point_text": "Sympathy gets a partial (~) on modeling the other's mind because you can pity someone while badly misreading them; accurate understanding helps sympathy but is not constitutive of it, unlike cognitive empathy.",
   "weight": "Nice to have",
   "presence": "Present",
   "loglog_ids": [
    "L007"
   ],
   "evidence_quote": "Nuance: Sympathy earns only partial on modeling: pity can badly misread people.",
   "reasoning": "The partial mark and the reason (pity misreads) are both captured. The added contrast with cognitive empathy is a refinement, but the cell explanation is delivered."
  },
  {
   "point_id": "K04",
   "point_text": "Affective empathy gets a partial (~) on capacity to care because emotional contagion can occur involuntarily without real concern, e.g., catching someone's anxiety and wanting to get away from them.",
   "weight": "Nice to have",
   "presence": "Present",
   "loglog_ids": [
    "L010"
   ],
   "evidence_quote": "Nuance: Affective empathy earns only partial on caring: contagion can occur without concern.",
   "reasoning": "Partial mark and the contagion-without-concern reason both present. The anxiety example is dropped, but this is a Nice to have illustration and the claim is intact."
  },
  {
   "point_id": "K05",
   "point_text": "The manipulators/con-artist row is the sharpest diagnostic for the cognitive/affective split and is essentially the psychopath's signature: cognitive empathy alone is compatible with cruelty, since a con artist models minds precisely without resonating with or caring about them.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L005",
    "L006"
   ],
   "evidence_quote": "Cognitive empathy means accurate modeling, boundary, and control; it survives in manipulators. ... The psychopath column is essentially the cognitive-empathy column standing alone.",
   "reasoning": "L005 places cognitive empathy in manipulators, L006 makes the psychopath the cognitive column standing alone, which carries the separability-of-caring claim. The cruelty/coldness implication survives in the 'standing alone' formulation."
  },
  {
   "point_id": "K06",
   "point_text": "The sustainable-and-scalable row reflects the Bloom/Singer argument (Paul Bloom's Against Empathy and Tania Singer's compassion-training research); it is a position, not a consensus, and critics reply that compassion without empathic grounding risks becoming abstract or paternalistic.",
   "weight": "Must have",
   "presence": "Partial",
   "loglog_ids": [
    "L013",
    "L014"
   ],
   "evidence_quote": "Only compassion scores full marks on helping motivation and sustainable scalable guidance. ... The Bloom and Singer pro-compassion case is a position, not a consensus.",
   "reasoning": "The row, the Bloom/Singer attribution, and the 'position not a consensus' caveat are all present, but the critics' counterargument (compassion without empathic grounding risks becoming abstract or paternalistic) is entirely absent. A must-have qualifier element is dropped, capping this at Partial."
  },
  {
   "point_id": "K07",
   "point_text": "Boundary maintenance is the structural difference between affective empathy and everything else: affective empathy means partially merging with the other's state, which drives both its motivational power and its burnout and bias problems.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L008",
    "L009"
   ],
   "evidence_quote": "Affective empathy means sharing emotion, with contagion, burnout, and vividness bias. ... Affective empathy lacks boundary maintenance, unlike everything else in the table.",
   "reasoning": "L009 marks boundary maintenance as the distinguishing structural feature; L008 ties the merging to burnout and vividness bias. Mechanism and its consequences both captured."
  },
  {
   "point_id": "K08",
   "point_text": "Reading the two dark profiles as columns: the psychopath is close to the cognitive-empathy column standing alone (accurate modeling with affective and caring machinery deleted), while the sociopath is close to affective empathy and sympathy clamped to a narrow in-group and stripped of regulation; the psychopath's one distinguishing possession is cold instrumental control, while a whole cluster of affective and caring rows belongs to the sociopath and not the psychopath.",
   "weight": "Must have",
   "present": "",
   "presence": "Present",
   "loglog_ids": [
    "L006",
    "L011",
    "L015",
    "L016",
    "L017"
   ],
   "evidence_quote": "The psychopath keeps only cold instrumental control; the sociopath holds the affective cluster. ... only control is psychopath-only. ... The sociopath resembles affective empathy plus sympathy clamped to an in-group, unregulated.",
   "reasoning": "L011 gives the clamped, unregulated sociopath, L006 gives psychopath as cognitive column alone, and L015/L016/L017 give the control-only vs affective-cluster asymmetry. The full analytical payoff is captured."
  },
  {
   "point_id": "K09",
   "point_text": "Etiology is deliberately excluded as a row: psychopathy is often theorized as innate/temperamental and sociopathy as environmentally acquired, but that concerns causes rather than the shape of the response, so it does not belong in a feature table and would muddy the logic.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L023",
    "L024"
   ],
   "evidence_quote": "The table limits its scope deliberately. ... Etiology stays out: causal origin is not a response shape.",
   "reasoning": "The exclusion and its rationale (cause vs response shape) are stated. The innate/environmental detail is a supporting illustration but the scope decision and justification, which is what a reader needs, are intact."
  },
  {
   "point_id": "K10",
   "point_text": "Clinical caveat: 'psychopath' and 'sociopath' are not formal diagnoses; both fall under Antisocial Personality Disorder, and the split between them is a contested, largely theoretical convention. Treat the two columns as ideal types, not categories.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L023",
    "L025"
   ],
   "evidence_quote": "Psychopath and sociopath are not formal diagnoses; both fall under antisocial personality disorder. ... treats dark columns as ideal types.",
   "reasoning": "The not-formal-diagnoses claim, the ASPD grouping, and the ideal-type instruction are all present. The 'contested theoretical convention' clause is softened but the operative limiting qualifiers that prevent clinical misreading are captured."
  },
  {
   "point_id": "K11",
   "point_text": "Terminology caveat: usage varies across the literature, some authors use 'empathic concern' roughly where this table uses 'compassion', and pop-psych usage (e.g., Brené Brown) treats 'sympathy' as inherently distancing; this table uses the more neutral research sense.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L026"
   ],
   "evidence_quote": "Terminology varies; empathic concern and pop-psych sympathy differ from table usage.",
   "reasoning": "Captures usage variation, the 'empathic concern' term, and the pop-psych 'sympathy' divergence. The Brené Brown attribution is omitted but the semantic point defining the table's word choices is delivered."
  },
  {
   "point_id": "K12",
   "point_text": "The empath column is the affective column maxed out and unregulated, which is why it lights up emotion-sharing, contagion, and vividness bias while failing on boundary, scope, and scalability; it is the opposite of the psychopath's coldness but inherits the sociopath's distortions, so it is not the moral ideal.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L018",
    "L019"
   ],
   "evidence_quote": "The empath maximizes affect unregulated, so it is not the moral ideal. ... The empath lights up sharing, contagion, and bias but fails boundary, scope, and scalability.",
   "reasoning": "L018 gives maxed-out unregulated affect and the not-ideal verdict; L019 gives the exact set of failures. The core corrective claim is fully mapped."
  },
  {
   "point_id": "K13",
   "point_text": "The altruist column is the compassion column embodied and matches the research 'Light Triad' (Kantianism, Humanism, and Faith in Humanity, from Kaufman et al., 2019).",
   "weight": "Nice to have",
   "presence": "Present",
   "loglog_ids": [
    "L020"
   ],
   "evidence_quote": "The altruist embodies compassion and the Light Triad: Kantianism, Humanism, Faith in Humanity.",
   "reasoning": "Compassion embodiment and all three Light Triad components are present. The Kaufman 2019 citation is dropped but that is a secondary attribution on a Nice to have point."
  },
  {
   "point_id": "K14",
   "point_text": "The integrated ideal is the only column that scores well across every block, including the 'present in neither' rows, so it is the true opposite of both dark profiles at once.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L021"
   ],
   "evidence_quote": "The integrated ideal alone scores well across every block, opposing both dark profiles.",
   "reasoning": "Uniqueness (alone), all-block coverage, and dual opposition to both dark profiles are all present. Normative endpoint captured."
  },
  {
   "point_id": "K15",
   "point_text": "The three Light Triad rows partly restate earlier rows: Kantianism is essentially the inverse of the manipulators row, Humanism overlaps the caring and beyond-the-in-group rows, and only Faith in Humanity adds a genuinely new dimension (an attitude rather than an empathy component), which is why both dark profiles score blank on it.",
   "weight": "Must have",
   "presence": "Partial",
   "loglog_ids": [
    "L022"
   ],
   "evidence_quote": "Kantianism inverts the manipulators row; only Faith in Humanity adds a new dimension.",
   "reasoning": "The redundancy thesis and the novel-Faith row are captured, and the Kantianism/manipulators mapping is present. However the Humanism overlap mapping and the explanation for why both dark profiles go blank on Faith in Humanity are dropped, so this must-have loses some of its justifying detail."
  }
 ],
 "metrics": {
  "total_points": 15,
  "must_have_total": 12,
  "must_have_present": 10,
  "must_have_partial": 2,
  "must_have_missing": 0,
  "overall_present": 13,
  "must_recall": 0.9167,
  "overall_recall": 0.9333
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
    "L002"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Summary names all four components and five profiles, the document's core inventory."
  },
  {
   "claim_id": "C002",
   "loglog_ids": [
    "L003"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Adds left/right layout of the double rule, not stated elsewhere."
  },
  {
   "claim_id": "C003",
   "loglog_ids": [
    "L004"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Introduces the four row blocks, a distinct structural axis."
  },
  {
   "claim_id": "C004",
   "loglog_ids": [
    "L005"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Defines cognitive empathy's parts and survival in manipulators."
  },
  {
   "claim_id": "C005",
   "loglog_ids": [
    "L006"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Maps the psychopath column onto cognitive empathy, new evidence."
  },
  {
   "claim_id": "C006",
   "loglog_ids": [
    "L007"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Sympathy partial-modeling caveat is new."
  },
  {
   "claim_id": "C007",
   "loglog_ids": [
    "L008"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Defines affective empathy's sharing, contagion, burnout, bias."
  },
  {
   "claim_id": "C008",
   "loglog_ids": [
    "L009"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Missing boundary is a distinct structural nuance of affective empathy."
  },
  {
   "claim_id": "C009",
   "loglog_ids": [
    "L010"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Contagion-without-concern limits affective empathy; new caveat."
  },
  {
   "claim_id": "C010",
   "loglog_ids": [
    "L011"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Sociopath's clamped affective composition is new content."
  },
  {
   "claim_id": "C011",
   "loglog_ids": [
    "L012"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Compassion's four-part combination is the branch's core claim."
  },
  {
   "claim_id": "C012",
   "loglog_ids": [
    "L013"
   ],
   "label": "Duplicate",
   "canonical_id": "C011",
   "reasoning": "Restates compassion alone leading helping and sustainability; adds no information."
  },
  {
   "claim_id": "C013",
   "loglog_ids": [
    "L014"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Bloom and Singer position caveat is new."
  },
  {
   "claim_id": "C014",
   "loglog_ids": [
    "L015"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Psychopath/sociopath control split is the branch's core claim."
  },
  {
   "claim_id": "C015",
   "loglog_ids": [
    "L016"
   ],
   "label": "Duplicate",
   "canonical_id": "C014",
   "reasoning": "Only control being psychopath-only restates C014; degradation nuance is minor."
  },
  {
   "claim_id": "C016",
   "loglog_ids": [
    "L017"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Enumerates specific affective rows owned by sociopath; new detail."
  },
  {
   "claim_id": "C017",
   "loglog_ids": [
    "L018"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Empath is not the moral ideal; new verdict."
  },
  {
   "claim_id": "C018",
   "loglog_ids": [
    "L019"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Lists empat's specific failed dimensions; new evidence."
  },
  {
   "claim_id": "C019",
   "loglog_ids": [
    "L020"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Altruist's Light Triad mapping is new."
  },
  {
   "claim_id": "C020",
   "loglog_ids": [
    "L021"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Integrated ideal scoring across every block is new."
  },
  {
   "claim_id": "C021",
   "loglog_ids": [
    "L022"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Kantianism inversion nuance is new."
  },
  {
   "claim_id": "C022",
   "loglog_ids": [
    "L023"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Deliberate scope and ideal-type disclaimer is new."
  },
  {
   "claim_id": "C023",
   "loglog_ids": [
    "L024"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Etiology exclusion is new."
  },
  {
   "claim_id": "C024",
   "loglog_ids": [
    "L025"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "ASPD non-diagnosis fact is new."
  },
  {
   "claim_id": "C025",
   "loglog_ids": [
    "L026"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Terminology divergence caveat is new."
  }
 ],
 "metrics": {
  "scored_claims": 25,
  "unique": 23,
  "duplicates": 2,
  "trivia": 0,
  "redundancy_rate": 0.08,
  "trivia_rate": 0.0,
  "structured_tokens": 308,
  "tokens_per_unique_claim": 13.39
 },
 "prune_list": [
  "C012 duplicates C011, safe to merge",
  "C015 duplicates C014, safe to merge"
 ]
}
```

## Judge Top (overall), opencode-go/deepseek-v4.1-flash

```json
{
 "judge": "overall",
 "judge_version": "1.0.0",
 "model": "deepseek-v4.1-flash 2026-09-15",
 "source_id": "unspecified",
 "inputs": {
  "faithfulness_precision": 1.0,
  "critical_errors": 0,
  "must_recall": 0.9167,
  "overall_recall": 0.9333,
  "redundancy_rate": 0.08,
  "trivia_rate": 0.0
 },
 "weights_used": {
  "faithfulness_precision": 0.4,
  "coverage_must_recall": 0.4,
  "redundancy_penalty": 0.2
 },
 "computation": "weighted_score = 0.4*1.0 + 0.4*0.9167 - 0.2*0.08 = 0.40000 + 0.36668 - 0.01600 = 0.75068",
 "weighted_score": 0.7507,
 "verdict": "Borderline",
 "tradeoff_note": "All hard gates clear, but two Must-have points (K06, K15) are only Partial, so a human should judge whether the dropped qualifiers change the argument. Redundancy (0.08) is well under max, so no length penalty is warranted and no coverage gain needs trimming.",
 "fix_list": [
  "K06: add the critics' counterargument that compassion without empathic grounding risks becoming abstract or paternalistic, the single missing qualifier that caps this Must-have at Partial.",
  "K15: restore the Humanism-overlap mapping and the explanation for why both dark profiles score blank on Faith in Humanity, both dropped justifying details.",
  "Merge C012 into C011 and C015 into C014 to remove the only redundancy (rate 0.08, still below 0.15 max)."
 ],
 "reasoning": "Gate checks against config pass_gates. critical_contradicted_max=0: faithfulness critical_errors=0, so no critical fail. faithfulness_precision_min=0.95: measured 1.0 (25/25 supported, 0 partial, 0 unverifiable, 0 contradicted), passes with headroom. must_recall_min=0.9: measured 0.9167 (10 present + 2 partial*0.5 = 11 of 12 must-haves), passes by a 0.0167 margin. redundancy_max=0.15 is treated as the length-cost ceiling under top_policy: measured redundancy_rate=0.08, below max, so no coverage gain is disallowed on length grounds. No hard gate is missed and no Critical error exists, so the sample is not a Fail. Weighted score per aspect_weights: 0.4*faithfulness_precision(1.0)=0.40000, 0.4*must_recall(0.9167)=0.36668, minus 0.2*redundancy(0.08)=0.01600, giving 0.75068. Concision does not rescue or sink this: with 0.08 redundancy and 0 trivia, its only role is tie-breaking and neither Partial point is offset by concision. Borderline is triggered by policy item 4: gates pass on the numbers, but two Must-have points carry Partial status. K06 (loglog L013, L014) captures the sustainable-and-scalable row, the Bloom/Singer attribution, and the 'position not a consensus' caveat, yet drops the critics' reply about abstract or paternalistic compassion, a Must-have qualifier. K15 (loglog L022) captures the redundancy thesis and the novel Faith in Humanity row plus the Kantianism/manipulators mapping, but drops the Humanism overlap mapping and the reason both dark profiles go blank on Faith in Humanity. Both are named for human review, so the verdict is Borderline rather than Pass despite the clean faithfulness record and passing recall."
}
```
