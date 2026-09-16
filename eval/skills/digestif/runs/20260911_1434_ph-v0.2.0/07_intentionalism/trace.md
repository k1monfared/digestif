# Judge trace (scripted pipeline, opencode-go/deepseek-v4.1-flash)

## Judge F (faithfulness), opencode-go/deepseek-v4.1-flash

```json
{
 "judge": "faithfulness",
 "judge_version": "1.0.0",
 "model": "opencode-go/deepseek-v4.1-flash (opencode) scripted pipeline 2026-09-15",
 "source_id": "07_intentionalism",
 "claims": [
  {
   "claim_id": "C001",
   "loglog_ids": [
    "0"
   ],
   "claim_text": "Life structurally favors proposers over receivers, so practice intending before choosing.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "It's about whether they propose or receive.",
   "reasoning": "SOURCE's thesis and closing call to practice intention match the summary."
  },
  {
   "claim_id": "C002",
   "loglog_ids": [
    "1"
   ],
   "claim_text": "Gale-Shapley 1962 stable-matching work revealed proposer-receiver asymmetry.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "In 1962, mathematician-economists David Gale and Lloyd Shapley",
   "reasoning": "Date, names, and the proposer-receiver discovery all appear in SOURCE."
  },
  {
   "claim_id": "C003",
   "loglog_ids": [
    "1.1"
   ],
   "claim_text": "Deferred acceptance: one side proposes in order, other tentatively accepts or rejects.",
   "claim_type": "definition",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "one side makes proposals in order of preference, and the other side accepts or tentatively rejects",
   "reasoning": "Definition matches SOURCE almost verbatim."
  },
  {
   "claim_id": "C004",
   "loglog_ids": [
    "1.2"
   ],
   "claim_text": "Proposers get best stable partner; receivers get worst; extremes are provable.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "each individual proposer ends up with the best stable partner",
   "reasoning": "SOURCE states best for proposers, worst for receivers, provably extreme."
  },
  {
   "claim_id": "C005",
   "loglog_ids": [
    "1.3"
   ],
   "claim_text": "Better outcomes come from proposing versus receiving, not talent or luck.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "nothing to do with talent, luck",
   "reasoning": "SOURCE explicitly excludes talent and luck."
  },
  {
   "claim_id": "C006",
   "loglog_ids": [
    "2"
   ],
   "claim_text": "Most real situations share proposer-receiver structure without running exact algorithm.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "most real-world situations don't follow the exact Gale-Shapley algorithm",
   "reasoning": "SOURCE states real cases share the structure but not the exact algorithm."
  },
  {
   "claim_id": "C007",
   "loglog_ids": [
    "2.1"
   ],
   "claim_text": "Receiver quiz: Netflix scroll, displayed phones, posted jobs, proximity friendships.",
   "claim_type": "meta",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "scroll through recommendations until something looked good enough",
   "reasoning": "All four examples appear in SOURCE with the same receiver framing."
  },
  {
   "claim_id": "C008",
   "loglog_ids": [
    "2.2"
   ],
   "claim_text": "Most of us mostly receive, choosing from presented rather than pursuing wanted.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "For most of these, most of us are receivers.",
   "reasoning": "SOURCE states most of us are receivers choosing from presented options."
  },
  {
   "claim_id": "C009",
   "loglog_ids": [
    "3"
   ],
   "claim_text": "Receiving yields acceptable outcomes that quietly fall short of best.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "You get acceptable ones. Good enough ones.",
   "reasoning": "SOURCE contrasts acceptable outcomes with what would serve you best."
  },
  {
   "claim_id": "C010",
   "loglog_ids": [
    "3.1"
   ],
   "claim_text": "Informal proposer-receiver structures systematically favor whoever proposes.",
   "claim_type": "causal_link",
   "verdict": "Partially supported",
   "severity": "Minor",
   "evidence_quote": "the outcomes tend to favor whoever's doing the proposing",
   "reasoning": "SOURCE hedges with 'tend to'; loglog states it as absolute systematic fact."
  },
  {
   "claim_id": "C011",
   "loglog_ids": [
    "3.2"
   ],
   "claim_text": "Comfortable outcomes block revolt; system stays stable by never screwing badly.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "doesn't screw you badly enough to make you revolt",
   "reasoning": "SOURCE says stability arises because outcomes are not bad enough to revolt."
  },
  {
   "claim_id": "C012",
   "loglog_ids": [
    "3.3"
   ],
   "claim_text": "Without practicing specific wanting, people cannot know what they miss.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "You don't even know what you're missing, because you've never practiced wanting something specific",
   "reasoning": "SOURCE directly states the causal link."
  },
  {
   "claim_id": "C013",
   "loglog_ids": [
    "4"
   ],
   "claim_text": "Proposing needs intention, but intention develops through proposing.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "You need intention to propose, but you develop intention through proposing.",
   "reasoning": "Matches SOURCE's chicken-and-egg statement."
  },
  {
   "claim_id": "C014",
   "loglog_ids": [
    "4.1"
   ],
   "claim_text": "Presented choices reveal least-disliked option, not what anyone would pursue freely.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "reveal which option you dislike least among what's available",
   "reasoning": "SOURCE states choices reveal least-disliked, not freely pursued wants."
  },
  {
   "claim_id": "C015",
   "loglog_ids": [
    "4.2"
   ],
   "claim_text": "The trap: intention is prerequisite and product of proposing.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "This is the trap. You need intention to propose, but you develop intention through proposing.",
   "reasoning": "SOURCE labels this the trap with both directions."
  },
  {
   "claim_id": "C016",
   "loglog_ids": [
    "4.3"
   ],
   "claim_text": "Algorithm-fed songs and swiped partners may be reactions mistaken for preferences.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "preferences\" are just reactions to what gets put in front of them",
   "reasoning": "SOURCE makes the same point using music and dating examples."
  },
  {
   "claim_id": "C017",
   "loglog_ids": [
    "5"
   ],
   "claim_text": "Intention muscle builds progressively from small exercises upward.",
   "claim_type": "recommendation",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "The muscle of intention and initiative builds progressively.",
   "reasoning": "Matches SOURCE's progression claim."
  },
  {
   "claim_id": "C018",
   "loglog_ids": [
    "5.1"
   ],
   "claim_text": "Tonight decide the feeling wanted, then seek it without scrolling recommendations.",
   "claim_type": "recommendation",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "Don't open Netflix and see what it suggests.",
   "reasoning": "SOURCE gives the same tonight exercise and warnings."
  },
  {
   "claim_id": "C019",
   "loglog_ids": [
    "5.2"
   ],
   "claim_text": "Repeated practice surfaces patterns that become preferences then values.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "Those patterns become preferences. Those preferences become values.",
   "reasoning": "SOURCE states the exact chain."
  },
  {
   "claim_id": "C020",
   "loglog_ids": [
    "5.3"
   ],
   "claim_text": "Values come from practice, not from thought alone.",
   "claim_type": "recommendation",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "You can't think your way into values. You have to practice your way into them.",
   "reasoning": "Matches SOURCE verbatim in meaning."
  },
  {
   "claim_id": "C021",
   "loglog_ids": [
    "6"
   ],
   "claim_text": "Major decisions mostly evaluate presented options, mistaking receipt for agency.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "This feels like agency because you're choosing. But you're choosing as a receiver",
   "reasoning": "SOURCE says most evaluate presented options while feeling agency."
  },
  {
   "claim_id": "C022",
   "loglog_ids": [
    "6.1"
   ],
   "claim_text": "Intentional seekers of work, partners, cities gain systematically better outcomes.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "those people end up with systematically better outcomes",
   "reasoning": "SOURCE lists the same three domains and outcome."
  },
  {
   "claim_id": "C023",
   "loglog_ids": [
    "6.2"
   ],
   "claim_text": "Advantage comes from structural side, not superior smarts or luck.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "Not because they're smarter or luckier.",
   "reasoning": "SOURCE explicitly denies smarter or luckier."
  },
  {
   "claim_id": "C024",
   "loglog_ids": [
    "7"
   ],
   "claim_text": "Receiver majorities let systems optimize for proposers instead of users.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "When most people are receivers, entire systems shift to optimize for whoever's doing the proposing.",
   "reasoning": "Matches SOURCE's collective effect claim."
  },
  {
   "claim_id": "C025",
   "loglog_ids": [
    "7.1"
   ],
   "claim_text": "Products, dating apps, feeds maximize engagement over genuine need or compatibility.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "they optimize for engagement among available profiles",
   "reasoning": "All three platform examples match SOURCE."
  },
  {
   "claim_id": "C026",
   "loglog_ids": [
    "7.2"
   ],
   "claim_text": "Platforms take optimal outcomes while users get participation-sustaining good-enough.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "good enough to keep you participating, but not actually serving your best interests",
   "reasoning": "Matches SOURCE's platform versus user outcome split."
  },
  {
   "claim_id": "C027",
   "loglog_ids": [
    "7.3"
   ],
   "claim_text": "Leaving feels harder than accepting; stability means resistance to change.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "That's stability (resistance to change). That's why the system persists.",
   "reasoning": "Matches SOURCE verbatim."
  },
  {
   "claim_id": "C028",
   "loglog_ids": [
    "8"
   ],
   "claim_text": "Understanding disadvantage changes nothing without switching to proposing.",
   "claim_type": "recommendation",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "doesn't go away because you understand it. You have to actually switch positions.",
   "reasoning": "Matches SOURCE's breaking-out claim."
  },
  {
   "claim_id": "C029",
   "loglog_ids": [
    "8.1"
   ],
   "claim_text": "Proposing means deciding first, pursuing specifics, creating chances, accepting friction.",
   "claim_type": "definition",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "Being willing to create opportunities rather than waiting for them",
   "reasoning": "All four bullet points derive from SOURCE's list."
  },
  {
   "claim_id": "C030",
   "loglog_ids": [
    "8.2"
   ],
   "claim_text": "Ask what is wanted before every decision, then act despite inconvenience.",
   "claim_type": "recommendation",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "before every major decision and most minor ones",
   "reasoning": "Matches SOURCE including the inconvenience clause."
  },
  {
   "claim_id": "C031",
   "loglog_ids": [
    "8.3"
   ],
   "claim_text": "Most refuse the effort; comfort plus atrophied wanting keeps receivers receiving.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "Most people won't do this. It's effortful.",
   "reasoning": "SOURCE states most won't, comfort suffices, and capacity is lost."
  },
  {
   "claim_id": "C032",
   "loglog_ids": [
    "8.4"
   ],
   "claim_text": "Shifters gain structurally better outcomes even outside exact mathematics.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "Systematically better. Not just incrementally—structurally.",
   "reasoning": "Matches SOURCE's claim for those who shift."
  },
  {
   "claim_id": "C033",
   "loglog_ids": [
    "8.5"
   ],
   "claim_text": "Dynamic existence is settled; only willingness to act remains open.",
   "claim_type": "meta",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "The question is whether you're willing to do something about it.",
   "reasoning": "SOURCE frames existence as settled and willingness as the open question."
  },
  {
   "claim_id": "C034",
   "loglog_ids": [
    "9"
   ],
   "claim_text": "Start tomorrow morning with the first hour, then scale practice upward.",
   "claim_type": "recommendation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Start with tomorrow morning. ... Then scale up. Apply it to bigger decisions.",
   "reasoning": "Source explicitly advises starting tomorrow morning and then scaling to larger decisions."
  },
  {
   "claim_id": "C035",
   "loglog_ids": [
    "9.1"
   ],
   "claim_text": "Name calm, energy, connection, or solitude; pursue it instead of notifications.",
   "claim_type": "recommendation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "do you want calm? Energy? Connection? Solitude? ... Then pursue that.",
   "reasoning": "Source lists exactly these four options and advises pursuing the chosen one over notifications."
  },
  {
   "claim_id": "C036",
   "loglog_ids": [
    "9.2"
   ],
   "claim_text": "Notice scrolling versus intending; log satisfaction across small choices for a week.",
   "claim_type": "recommendation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Notice how different this feels from scrolling ... Do this for a week with small things ... Notice what actually satisfies you",
   "reasoning": "Source prescribes noticing the contrast and tracking satisfaction over a week of small choices."
  },
  {
   "claim_id": "C037",
   "loglog_ids": [
    "9.3"
   ],
   "claim_text": "Scale to jobs, dating, purchases by deciding criteria before browsing options.",
   "claim_type": "recommendation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Before looking at job postings, decide what kind of work you want ... Before swiping on dating apps ... Before browsing products",
   "reasoning": "Source gives exactly these three domains and the decide-first ordering."
  },
  {
   "claim_id": "C038",
   "loglog_ids": [
    "9.4"
   ],
   "claim_text": "Muscle enables intentions, intentions become values, values make proposers.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "The muscle enables larger intentions. Larger intentions become values. Values make you a proposer.",
   "reasoning": "Nearly verbatim restatement of the source's causal chain."
  },
  {
   "claim_id": "C039",
   "loglog_ids": [
    "9.5"
   ],
   "claim_text": "Proposers end better across math and mess, not from specialness but position.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "proposers—whether in the pure mathematics ... or in the messy approximations of real life—end up with better outcomes. Not because they're special.",
   "reasoning": "Source states the same outcome across both settings and attributes it to position, not specialness."
  },
  {
   "claim_id": "C040",
   "loglog_ids": [
    "10"
   ],
   "claim_text": "Appendix gives progressive exercises for entertainment, shopping, jobs, relationships, days.",
   "claim_type": "meta",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "practicing intention in progressively larger domains. Here are specific exercises for the scenarios mentioned throughout this post.",
   "reasoning": "Appendix covers entertainment, shopping, jobs, relationships, and daily micro-practices as listed."
  },
  {
   "claim_id": "C041",
   "loglog_ids": [
    "10.1"
   ],
   "claim_text": "Entertainment: name intention week one, seek week two, protect with timers week three.",
   "claim_type": "recommendation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Week 1: Name your intention ... Week 2: Seek intentionally ... Week 3: Protect your intention ... Set a timer",
   "reasoning": "Source lays out the same three weekly stages including timers in week three."
  },
  {
   "claim_id": "C042",
   "loglog_ids": [
    "10.2"
   ],
   "claim_text": "Shopping: define problem, list must-haves, research features, ignore layout, 24-hour rule.",
   "claim_type": "recommendation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Define the problem ... List must-haves ... Research intentionally ... Ignore the store layout ... 24-hour rule",
   "reasoning": "All five listed steps appear in the source's numbered shopping list."
  },
  {
   "claim_id": "C043",
   "loglog_ids": [
    "10.3"
   ],
   "claim_text": "Toothpaste drill: identify need, find ingredient, buy it, notice packaging-free choosing.",
   "claim_type": "recommendation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Research which ingredient addresses that need ... find that ingredient, buy it ... comparing packaging",
   "reasoning": "Source's toothpaste practice run matches each step."
  },
  {
   "claim_id": "C044",
   "loglog_ids": [
    "10.4"
   ],
   "claim_text": "Career: set five non-negotiables, approach firms directly, apply only to strong matches.",
   "claim_type": "recommendation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Write 5 non-negotiables ... Contact people at those companies ... Only apply to roles that match at least 4 of your 5 criteria",
   "reasoning": "Source specifies five criteria, direct outreach, and applying only to sufficiently matching roles."
  },
  {
   "claim_id": "C045",
   "loglog_ids": [
    "10.5"
   ],
   "claim_text": "Dating: write relationship vision, require value alignment, filter first dates intentionally.",
   "claim_type": "recommendation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Write your relationship intention ... Identify values alignment ... First date filter: Ask questions that reveal value alignment",
   "reasoning": "Source lists these dating steps in the same order and intent."
  },
  {
   "claim_id": "C046",
   "loglog_ids": [
    "10.6"
   ],
   "claim_text": "Friendship: name needed qualities, join matching communities, initiate specific activities.",
   "claim_type": "recommendation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Name what you need ... Join specific communities ... Initiate based on intention: Invite people to do specific things",
   "reasoning": "Source's friendship steps match the node."
  },
  {
   "claim_id": "C047",
   "loglog_ids": [
    "10.7"
   ],
   "claim_text": "Daily: three morning intentions, evening proposer review, ten-second pause before choices.",
   "claim_type": "recommendation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "What are my three intentions for today? ... Evening review ... pause for 10 seconds",
   "reasoning": "Source contains each of the three daily micro-practices at the stated quantities."
  },
  {
   "claim_id": "C048",
   "loglog_ids": [
    "10.8"
   ],
   "claim_text": "Journal situation, mode, outcome; thirty days reveal proposer satisfaction pattern.",
   "claim_type": "recommendation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "three columns: Situation ... Mode ... Outcome ... After 30 days ... Proposer entries will show higher satisfaction.",
   "reasoning": "Source specifies the three columns and the 30-day proposer-satisfaction pattern."
  },
  {
   "claim_id": "C049",
   "loglog_ids": [
    "10.9"
   ],
   "claim_text": "Intention means asking what is wanted before others answer; small reps grow capacity.",
   "claim_type": "definition",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "It's about practicing the question \"what do I want?\" before someone else provides the answer. Start small. The muscle builds. The capacity grows.",
   "reasoning": "Source defines intention the same way and describes small starts growing capacity."
  }
 ],
 "metrics": {
  "total_claims": 49,
  "supported": 48,
  "partially_supported": 1,
  "unverifiable": 0,
  "contradicted": 0,
  "critical_errors": 0,
  "faithfulness_precision": 0.9796
 },
 "fail_list": [
  "C010"
 ]
}
```

## Judge Cov (coverage), opencode-go/deepseek-v4.1-flash

```json
{
 "judge": "coverage",
 "judge_version": "1.0.0",
 "model": "opencode-go/deepseek-v4.1-flash (opencode) scripted pipeline 2026-09-15",
 "source_id": "07_intentionalism",
 "key_points": [
  {
   "point_id": "K01",
   "point_text": "Central thesis: proposers systematically end up with better outcomes than receivers, and this is not because of talent, luck, or the quality of their choices.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L002",
    "L006",
    "L040"
   ],
   "evidence_quote": "Nuance: Better outcomes come from proposing versus receiving, not talent or luck.",
   "reasoning": "Thesis is stated at L002 and the causal exclusion of talent/luck is captured explicitly at L006. L040 restates ending better by position rather than specialness."
  },
  {
   "point_id": "K02",
   "point_text": "In 1962 mathematicians-economists David Gale and Lloyd Shapley worked on creating stable pairings between two groups and proved a stable matching (no unmatched pair preferring each other) always exists.",
   "weight": "Must have",
   "presence": "Partial",
   "loglog_ids": [
    "L003"
   ],
   "evidence_quote": "1 Gale-Shapley 1962 stable-matching work revealed proposer-receiver asymmetry.",
   "reasoning": "The date 1962, the names Gale-Shapley, and the stable-matching subject are retained, but the existence proof (a stable matching always exists) and the definition of stability (no blocking pair) are dropped. Must-have point with a lost claim, so Partial."
  },
  {
   "point_id": "K03",
   "point_text": "Their deferred acceptance algorithm works by having one side propose in order of preference while the other side accepts or tentatively rejects based on its preferences.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L004"
   ],
   "evidence_quote": "Evidence: Deferred acceptance: one side proposes in order, other tentatively accepts or rejects.",
   "reasoning": "Mechanism is fully captured: one side proposes in order, the other tentatively accepts or rejects. 'In order' preserves the preference-ordering substance."
  },
  {
   "point_id": "K04",
   "point_text": "Core mathematical result: proposers each get their best possible stable partner and receivers each get their worst possible stable partner, a provably extreme gap, not a slight difference.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L005",
    "L052"
   ],
   "evidence_quote": "Proposers get best stable partner; receivers get worst; extremes are provable.",
   "reasoning": "Both extremes and their provability are captured at L005, with the cross-link L052 confirming the closing verdict restates the mathematical extreme."
  },
  {
   "point_id": "K05",
   "point_text": "Most real-world situations do not follow the exact algorithm but share the same proposer/receiver structure, so the same pattern of advantage should be expected even when only approximate.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L007",
    "L011"
   ],
   "evidence_quote": "Most real situations share proposer-receiver structure without running exact algorithm.",
   "reasoning": "L007 states the structural generalization, and L011 adds that informal structures systematically favor whoever proposes, preserving the expected-advantage inference."
  },
  {
   "point_id": "K06",
   "point_text": "Everyday illustrations show most people are receivers: choosing Netflix by scrolling, picking among displayed phones, applying to posted jobs, accepting friendships formed by proximity.",
   "weight": "Nice to have",
   "presence": "Present",
   "loglog_ids": [
    "L008"
   ],
   "evidence_quote": "Receiver quiz: Netflix scroll, displayed phones, posted jobs, proximity friendships.",
   "reasoning": "All four illustrations appear in the same line, covering the receiver examples provided."
  },
  {
   "point_id": "K07",
   "point_text": "The insidious part is that receivers get acceptable, good-enough outcomes, so they never feel dissatisfied enough to change, and the system stays stable (self-sustaining) while quietly giving them less than they could have.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L010",
    "L012"
   ],
   "evidence_quote": "Receiving yields acceptable outcomes that quietly fall short of best.",
   "reasoning": "L010 captures good-enough outcomes that quietly fall short, and L012 captures comfortable outcomes blocking revolt and stability keeping the system intact."
  },
  {
   "point_id": "K08",
   "point_text": "Chicken-and-egg trap: you need intention to propose, but you develop intention through proposing; choosing among presented options only reveals what you dislike least, not what you would pursue.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L014",
    "L015",
    "L016"
   ],
   "evidence_quote": "Presented choices reveal least-disliked option, not what anyone would pursue freely.",
   "reasoning": "The mutual dependence of intention and proposing is at L014/L016, and the least-disliked versus freely-pursued distinction is preserved at L015."
  },
  {
   "point_id": "K09",
   "point_text": "Training ground: the muscle of intention builds progressively, so start small by intentionally deciding what you want from the next hour before opening any app, rather than scrolling until something catches you.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L018",
    "L019"
   ],
   "evidence_quote": "Intention muscle builds progressively from small exercises upward.",
   "reasoning": "L018 states progressive muscle building, L019 gives the small proximal exercise of deciding the feeling wanted then seeking it without scrolling recommendations. The 'before opening any app' framing is approximated by avoiding recommendations."
  },
  {
   "point_id": "K10",
   "point_text": "You cannot think your way into values, you have to practice your way into them: repeated intentional acts yield patterns, patterns become preferences, preferences become values.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L020",
    "L021"
   ],
   "evidence_quote": "Values come from practice, not from thought alone.",
   "reasoning": "L020 preserves the patterns to preferences to values chain, and L021 preserves the practice-over-thought claim."
  },
  {
   "point_id": "K11",
   "point_text": "Structural disadvantage does not disappear with understanding, you must actually switch positions, and proposing means deciding what you want before seeing options, pursuing specifics, creating opportunities, and accepting friction against default flows.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L029",
    "L030"
   ],
   "evidence_quote": "Understanding disadvantage changes nothing without switching to proposing.",
   "reasoning": "L029 states understanding is insufficient without switching, and L030 lists the four acts of proposing including accepting friction."
  },
  {
   "point_id": "K12",
   "point_text": "Collective effect: when most people are receivers, systems optimize for the proposers, namely the platforms, which capture optimal outcomes (attention, data, money) while users get only good-enough outcomes.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L025",
    "L026",
    "L027"
   ],
   "evidence_quote": "Platforms take optimal outcomes while users get participation-sustaining good-enough.",
   "reasoning": "L025 states receiver majorities let systems optimize for proposers, L026 gives the engagement-over-need examples, and L027 captures platforms taking optimal while users get good-enough."
  },
  {
   "point_id": "K13",
   "point_text": "Most people will not make the shift because it is effortful, the receiver position is comfortable, and after years of receiver mode many have lost the capacity to know what they would want to propose.",
   "weight": "Nice to have",
   "presence": "Present",
   "loglog_ids": [
    "L032"
   ],
   "evidence_quote": "Most refuse the effort; comfort plus atrophied wanting keeps receivers receiving.",
   "reasoning": "L032 preserves both causes: refusal of effort, comfort, and atrophied wanting closing the loop on lost capacity."
  },
  {
   "point_id": "K14",
   "point_text": "Practical progression: begin with tomorrow morning before checking your phone, practice for a week on small things (breakfast, evening activities, weekend plans), then scale to bigger decisions like work, relationships, and purchases.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L035",
    "L037",
    "L038"
   ],
   "evidence_quote": "Start tomorrow morning with the first hour, then scale practice upward.",
   "reasoning": "L035 begins tomorrow morning, L037 covers a week of logging small choices, and L038 scales to jobs, dating, and purchases. The specific small-thing menu is generalized but the progression is intact."
  },
  {
   "point_id": "K15",
   "point_text": "Appendix concrete tools: domain exercises (entertainment, shopping with must-haves and 24-hour rule over $100, career with 5 non-negotiables and applying only when 4 of 5 match, relationships), daily pause and journaling practices, and a 30-day tracking journal showing proposers report higher satisfaction.",
   "weight": "Nice to have",
   "presence": "Partial",
   "loglog_ids": [
    "L041",
    "L043",
    "L045",
    "L048",
    "L049"
   ],
   "evidence_quote": "Journal situation, mode, outcome; thirty days reveal proposer satisfaction pattern.",
   "reasoning": "All domains and practices are present, but the specific numeric thresholds are dropped: the $100 bar for the shopping 24-hour rule and the 4-of-5 match rule in career. Nice-to-have, so this lowers polish rather than recall of a must-have."
  }
 ],
 "metrics": {
  "total_points": 15,
  "must_have_total": 12,
  "must_have_present": 11,
  "must_have_partial": 1,
  "must_have_missing": 0,
  "overall_present": 13,
  "must_recall": 0.9583,
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
 "source_id": "07_intentionalism",
 "claims": [
  {
   "claim_id": "C001",
   "loglog_ids": [
    "0"
   ],
   "claim_text": "Life structurally favors proposers over receivers, so practice intending before choosing.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "It's about whether they propose or receive.",
   "reasoning": "SOURCE's thesis and closing call to practice intention match the summary."
  },
  {
   "claim_id": "C002",
   "loglog_ids": [
    "1"
   ],
   "claim_text": "Gale-Shapley 1962 stable-matching work revealed proposer-receiver asymmetry.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "In 1962, mathematician-economists David Gale and Lloyd Shapley",
   "reasoning": "Date, names, and the proposer-receiver discovery all appear in SOURCE."
  },
  {
   "claim_id": "C003",
   "loglog_ids": [
    "1.1"
   ],
   "claim_text": "Deferred acceptance: one side proposes in order, other tentatively accepts or rejects.",
   "claim_type": "definition",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "one side makes proposals in order of preference, and the other side accepts or tentatively rejects",
   "reasoning": "Definition matches SOURCE almost verbatim."
  },
  {
   "claim_id": "C004",
   "loglog_ids": [
    "1.2"
   ],
   "claim_text": "Proposers get best stable partner; receivers get worst; extremes are provable.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "each individual proposer ends up with the best stable partner",
   "reasoning": "SOURCE states best for proposers, worst for receivers, provably extreme."
  },
  {
   "claim_id": "C005",
   "loglog_ids": [
    "1.3"
   ],
   "claim_text": "Better outcomes come from proposing versus receiving, not talent or luck.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "nothing to do with talent, luck",
   "reasoning": "SOURCE explicitly excludes talent and luck."
  },
  {
   "claim_id": "C006",
   "loglog_ids": [
    "2"
   ],
   "claim_text": "Most real situations share proposer-receiver structure without running exact algorithm.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "most real-world situations don't follow the exact Gale-Shapley algorithm",
   "reasoning": "SOURCE states real cases share the structure but not the exact algorithm."
  },
  {
   "claim_id": "C007",
   "loglog_ids": [
    "2.1"
   ],
   "claim_text": "Receiver quiz: Netflix scroll, displayed phones, posted jobs, proximity friendships.",
   "claim_type": "meta",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "scroll through recommendations until something looked good enough",
   "reasoning": "All four examples appear in SOURCE with the same receiver framing."
  },
  {
   "claim_id": "C008",
   "loglog_ids": [
    "2.2"
   ],
   "claim_text": "Most of us mostly receive, choosing from presented rather than pursuing wanted.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "For most of these, most of us are receivers.",
   "reasoning": "SOURCE states most of us are receivers choosing from presented options."
  },
  {
   "claim_id": "C009",
   "loglog_ids": [
    "3"
   ],
   "claim_text": "Receiving yields acceptable outcomes that quietly fall short of best.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "You get acceptable ones. Good enough ones.",
   "reasoning": "SOURCE contrasts acceptable outcomes with what would serve you best."
  },
  {
   "claim_id": "C010",
   "loglog_ids": [
    "3.1"
   ],
   "claim_text": "Informal proposer-receiver structures systematically favor whoever proposes.",
   "claim_type": "causal_link",
   "verdict": "Partially supported",
   "severity": "Minor",
   "evidence_quote": "the outcomes tend to favor whoever's doing the proposing",
   "reasoning": "SOURCE hedges with 'tend to'; loglog states it as absolute systematic fact."
  },
  {
   "claim_id": "C011",
   "loglog_ids": [
    "3.2"
   ],
   "claim_text": "Comfortable outcomes block revolt; system stays stable by never screwing badly.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "doesn't screw you badly enough to make you revolt",
   "reasoning": "SOURCE says stability arises because outcomes are not bad enough to revolt."
  },
  {
   "claim_id": "C012",
   "loglog_ids": [
    "3.3"
   ],
   "claim_text": "Without practicing specific wanting, people cannot know what they miss.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "You don't even know what you're missing, because you've never practiced wanting something specific",
   "reasoning": "SOURCE directly states the causal link."
  },
  {
   "claim_id": "C013",
   "loglog_ids": [
    "4"
   ],
   "claim_text": "Proposing needs intention, but intention develops through proposing.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "You need intention to propose, but you develop intention through proposing.",
   "reasoning": "Matches SOURCE's chicken-and-egg statement."
  },
  {
   "claim_id": "C014",
   "loglog_ids": [
    "4.1"
   ],
   "claim_text": "Presented choices reveal least-disliked option, not what anyone would pursue freely.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "reveal which option you dislike least among what's available",
   "reasoning": "SOURCE states choices reveal least-disliked, not freely pursued wants."
  },
  {
   "claim_id": "C015",
   "loglog_ids": [
    "4.2"
   ],
   "claim_text": "The trap: intention is prerequisite and product of proposing.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "This is the trap. You need intention to propose, but you develop intention through proposing.",
   "reasoning": "SOURCE labels this the trap with both directions."
  },
  {
   "claim_id": "C016",
   "loglog_ids": [
    "4.3"
   ],
   "claim_text": "Algorithm-fed songs and swiped partners may be reactions mistaken for preferences.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "preferences\" are just reactions to what gets put in front of them",
   "reasoning": "SOURCE makes the same point using music and dating examples."
  },
  {
   "claim_id": "C017",
   "loglog_ids": [
    "5"
   ],
   "claim_text": "Intention muscle builds progressively from small exercises upward.",
   "claim_type": "recommendation",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "The muscle of intention and initiative builds progressively.",
   "reasoning": "Matches SOURCE's progression claim."
  },
  {
   "claim_id": "C018",
   "loglog_ids": [
    "5.1"
   ],
   "claim_text": "Tonight decide the feeling wanted, then seek it without scrolling recommendations.",
   "claim_type": "recommendation",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "Don't open Netflix and see what it suggests.",
   "reasoning": "SOURCE gives the same tonight exercise and warnings."
  },
  {
   "claim_id": "C019",
   "loglog_ids": [
    "5.2"
   ],
   "claim_text": "Repeated practice surfaces patterns that become preferences then values.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "Those patterns become preferences. Those preferences become values.",
   "reasoning": "SOURCE states the exact chain."
  },
  {
   "claim_id": "C020",
   "loglog_ids": [
    "5.3"
   ],
   "claim_text": "Values come from practice, not from thought alone.",
   "claim_type": "recommendation",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "You can't think your way into values. You have to practice your way into them.",
   "reasoning": "Matches SOURCE verbatim in meaning."
  },
  {
   "claim_id": "C021",
   "loglog_ids": [
    "6"
   ],
   "claim_text": "Major decisions mostly evaluate presented options, mistaking receipt for agency.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "This feels like agency because you're choosing. But you're choosing as a receiver",
   "reasoning": "SOURCE says most evaluate presented options while feeling agency."
  },
  {
   "claim_id": "C022",
   "loglog_ids": [
    "6.1"
   ],
   "claim_text": "Intentional seekers of work, partners, cities gain systematically better outcomes.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "those people end up with systematically better outcomes",
   "reasoning": "SOURCE lists the same three domains and outcome."
  },
  {
   "claim_id": "C023",
   "loglog_ids": [
    "6.2"
   ],
   "claim_text": "Advantage comes from structural side, not superior smarts or luck.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "Not because they're smarter or luckier.",
   "reasoning": "SOURCE explicitly denies smarter or luckier."
  },
  {
   "claim_id": "C024",
   "loglog_ids": [
    "7"
   ],
   "claim_text": "Receiver majorities let systems optimize for proposers instead of users.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "When most people are receivers, entire systems shift to optimize for whoever's doing the proposing.",
   "reasoning": "Matches SOURCE's collective effect claim."
  },
  {
   "claim_id": "C025",
   "loglog_ids": [
    "7.1"
   ],
   "claim_text": "Products, dating apps, feeds maximize engagement over genuine need or compatibility.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "they optimize for engagement among available profiles",
   "reasoning": "All three platform examples match SOURCE."
  },
  {
   "claim_id": "C026",
   "loglog_ids": [
    "7.2"
   ],
   "claim_text": "Platforms take optimal outcomes while users get participation-sustaining good-enough.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "good enough to keep you participating, but not actually serving your best interests",
   "reasoning": "Matches SOURCE's platform versus user outcome split."
  },
  {
   "claim_id": "C027",
   "loglog_ids": [
    "7.3"
   ],
   "claim_text": "Leaving feels harder than accepting; stability means resistance to change.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "That's stability (resistance to change). That's why the system persists.",
   "reasoning": "Matches SOURCE verbatim."
  },
  {
   "claim_id": "C028",
   "loglog_ids": [
    "8"
   ],
   "claim_text": "Understanding disadvantage changes nothing without switching to proposing.",
   "claim_type": "recommendation",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "doesn't go away because you understand it. You have to actually switch positions.",
   "reasoning": "Matches SOURCE's breaking-out claim."
  },
  {
   "claim_id": "C029",
   "loglog_ids": [
    "8.1"
   ],
   "claim_text": "Proposing means deciding first, pursuing specifics, creating chances, accepting friction.",
   "claim_type": "definition",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "Being willing to create opportunities rather than waiting for them",
   "reasoning": "All four bullet points derive from SOURCE's list."
  },
  {
   "claim_id": "C030",
   "loglog_ids": [
    "8.2"
   ],
   "claim_text": "Ask what is wanted before every decision, then act despite inconvenience.",
   "claim_type": "recommendation",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "before every major decision and most minor ones",
   "reasoning": "Matches SOURCE including the inconvenience clause."
  },
  {
   "claim_id": "C031",
   "loglog_ids": [
    "8.3"
   ],
   "claim_text": "Most refuse the effort; comfort plus atrophied wanting keeps receivers receiving.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "Most people won't do this. It's effortful.",
   "reasoning": "SOURCE states most won't, comfort suffices, and capacity is lost."
  },
  {
   "claim_id": "C032",
   "loglog_ids": [
    "8.4"
   ],
   "claim_text": "Shifters gain structurally better outcomes even outside exact mathematics.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "Systematically better. Not just incrementally—structurally.",
   "reasoning": "Matches SOURCE's claim for those who shift."
  },
  {
   "claim_id": "C033",
   "loglog_ids": [
    "8.5"
   ],
   "claim_text": "Dynamic existence is settled; only willingness to act remains open.",
   "claim_type": "meta",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "The question is whether you're willing to do something about it.",
   "reasoning": "SOURCE frames existence as settled and willingness as the open question."
  },
  {
   "claim_id": "C034",
   "loglog_ids": [
    "9"
   ],
   "claim_text": "Start tomorrow morning with the first hour, then scale practice upward.",
   "claim_type": "recommendation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Start with tomorrow morning. ... Then scale up. Apply it to bigger decisions.",
   "reasoning": "Source explicitly advises starting tomorrow morning and then scaling to larger decisions."
  },
  {
   "claim_id": "C035",
   "loglog_ids": [
    "9.1"
   ],
   "claim_text": "Name calm, energy, connection, or solitude; pursue it instead of notifications.",
   "claim_type": "recommendation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "do you want calm? Energy? Connection? Solitude? ... Then pursue that.",
   "reasoning": "Source lists exactly these four options and advises pursuing the chosen one over notifications."
  },
  {
   "claim_id": "C036",
   "loglog_ids": [
    "9.2"
   ],
   "claim_text": "Notice scrolling versus intending; log satisfaction across small choices for a week.",
   "claim_type": "recommendation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Notice how different this feels from scrolling ... Do this for a week with small things ... Notice what actually satisfies you",
   "reasoning": "Source prescribes noticing the contrast and tracking satisfaction over a week of small choices."
  },
  {
   "claim_id": "C037",
   "loglog_ids": [
    "9.3"
   ],
   "claim_text": "Scale to jobs, dating, purchases by deciding criteria before browsing options.",
   "claim_type": "recommendation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Before looking at job postings, decide what kind of work you want ... Before swiping on dating apps ... Before browsing products",
   "reasoning": "Source gives exactly these three domains and the decide-first ordering."
  },
  {
   "claim_id": "C038",
   "loglog_ids": [
    "9.4"
   ],
   "claim_text": "Muscle enables intentions, intentions become values, values make proposers.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "The muscle enables larger intentions. Larger intentions become values. Values make you a proposer.",
   "reasoning": "Nearly verbatim restatement of the source's causal chain."
  },
  {
   "claim_id": "C039",
   "loglog_ids": [
    "9.5"
   ],
   "claim_text": "Proposers end better across math and mess, not from specialness but position.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "proposers—whether in the pure mathematics ... or in the messy approximations of real life—end up with better outcomes. Not because they're special.",
   "reasoning": "Source states the same outcome across both settings and attributes it to position, not specialness."
  },
  {
   "claim_id": "C040",
   "loglog_ids": [
    "10"
   ],
   "claim_text": "Appendix gives progressive exercises for entertainment, shopping, jobs, relationships, days.",
   "claim_type": "meta",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "practicing intention in progressively larger domains. Here are specific exercises for the scenarios mentioned throughout this post.",
   "reasoning": "Appendix covers entertainment, shopping, jobs, relationships, and daily micro-practices as listed."
  },
  {
   "claim_id": "C041",
   "loglog_ids": [
    "10.1"
   ],
   "claim_text": "Entertainment: name intention week one, seek week two, protect with timers week three.",
   "claim_type": "recommendation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Week 1: Name your intention ... Week 2: Seek intentionally ... Week 3: Protect your intention ... Set a timer",
   "reasoning": "Source lays out the same three weekly stages including timers in week three."
  },
  {
   "claim_id": "C042",
   "loglog_ids": [
    "10.2"
   ],
   "claim_text": "Shopping: define problem, list must-haves, research features, ignore layout, 24-hour rule.",
   "claim_type": "recommendation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Define the problem ... List must-haves ... Research intentionally ... Ignore the store layout ... 24-hour rule",
   "reasoning": "All five listed steps appear in the source's numbered shopping list."
  },
  {
   "claim_id": "C043",
   "loglog_ids": [
    "10.3"
   ],
   "claim_text": "Toothpaste drill: identify need, find ingredient, buy it, notice packaging-free choosing.",
   "claim_type": "recommendation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Research which ingredient addresses that need ... find that ingredient, buy it ... comparing packaging",
   "reasoning": "Source's toothpaste practice run matches each step."
  },
  {
   "claim_id": "C044",
   "loglog_ids": [
    "10.4"
   ],
   "claim_text": "Career: set five non-negotiables, approach firms directly, apply only to strong matches.",
   "claim_type": "recommendation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Write 5 non-negotiables ... Contact people at those companies ... Only apply to roles that match at least 4 of your 5 criteria",
   "reasoning": "Source specifies five criteria, direct outreach, and applying only to sufficiently matching roles."
  },
  {
   "claim_id": "C045",
   "loglog_ids": [
    "10.5"
   ],
   "claim_text": "Dating: write relationship vision, require value alignment, filter first dates intentionally.",
   "claim_type": "recommendation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Write your relationship intention ... Identify values alignment ... First date filter: Ask questions that reveal value alignment",
   "reasoning": "Source lists these dating steps in the same order and intent."
  },
  {
   "claim_id": "C046",
   "loglog_ids": [
    "10.6"
   ],
   "claim_text": "Friendship: name needed qualities, join matching communities, initiate specific activities.",
   "claim_type": "recommendation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Name what you need ... Join specific communities ... Initiate based on intention: Invite people to do specific things",
   "reasoning": "Source's friendship steps match the node."
  },
  {
   "claim_id": "C047",
   "loglog_ids": [
    "10.7"
   ],
   "claim_text": "Daily: three morning intentions, evening proposer review, ten-second pause before choices.",
   "claim_type": "recommendation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "What are my three intentions for today? ... Evening review ... pause for 10 seconds",
   "reasoning": "Source contains each of the three daily micro-practices at the stated quantities."
  },
  {
   "claim_id": "C048",
   "loglog_ids": [
    "10.8"
   ],
   "claim_text": "Journal situation, mode, outcome; thirty days reveal proposer satisfaction pattern.",
   "claim_type": "recommendation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "three columns: Situation ... Mode ... Outcome ... After 30 days ... Proposer entries will show higher satisfaction.",
   "reasoning": "Source specifies the three columns and the 30-day proposer-satisfaction pattern."
  },
  {
   "claim_id": "C049",
   "loglog_ids": [
    "10.9"
   ],
   "claim_text": "Intention means asking what is wanted before others answer; small reps grow capacity.",
   "claim_type": "definition",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "It's about practicing the question \"what do I want?\" before someone else provides the answer. Start small. The muscle builds. The capacity grows.",
   "reasoning": "Source defines intention the same way and describes small starts growing capacity."
  }
 ],
 "metrics": {
  "total_claims": 49,
  "supported": 48,
  "partially_supported": 1,
  "unverifiable": 0,
  "contradicted": 0,
  "critical_errors": 0,
  "faithfulness_precision": 0.9796
 },
 "fail_list": [
  "C010"
 ]
}
```

## Judge Cov (coverage), opencode-go/deepseek-v4.1-flash

```json
{
 "judge": "coverage",
 "judge_version": "1.0.0",
 "model": "opencode-go/deepseek-v4.1-flash (opencode) scripted pipeline 2026-09-15",
 "source_id": "07_intentionalism",
 "key_points": [
  {
   "point_id": "K01",
   "point_text": "Central thesis: proposers systematically end up with better outcomes than receivers, and this is not because of talent, luck, or the quality of their choices.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L002",
    "L006",
    "L040"
   ],
   "evidence_quote": "Nuance: Better outcomes come from proposing versus receiving, not talent or luck.",
   "reasoning": "Thesis is stated at L002 and the causal exclusion of talent/luck is captured explicitly at L006. L040 restates ending better by position rather than specialness."
  },
  {
   "point_id": "K02",
   "point_text": "In 1962 mathematicians-economists David Gale and Lloyd Shapley worked on creating stable pairings between two groups and proved a stable matching (no unmatched pair preferring each other) always exists.",
   "weight": "Must have",
   "presence": "Partial",
   "loglog_ids": [
    "L003"
   ],
   "evidence_quote": "1 Gale-Shapley 1962 stable-matching work revealed proposer-receiver asymmetry.",
   "reasoning": "The date 1962, the names Gale-Shapley, and the stable-matching subject are retained, but the existence proof (a stable matching always exists) and the definition of stability (no blocking pair) are dropped. Must-have point with a lost claim, so Partial."
  },
  {
   "point_id": "K03",
   "point_text": "Their deferred acceptance algorithm works by having one side propose in order of preference while the other side accepts or tentatively rejects based on its preferences.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L004"
   ],
   "evidence_quote": "Evidence: Deferred acceptance: one side proposes in order, other tentatively accepts or rejects.",
   "reasoning": "Mechanism is fully captured: one side proposes in order, the other tentatively accepts or rejects. 'In order' preserves the preference-ordering substance."
  },
  {
   "point_id": "K04",
   "point_text": "Core mathematical result: proposers each get their best possible stable partner and receivers each get their worst possible stable partner, a provably extreme gap, not a slight difference.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L005",
    "L052"
   ],
   "evidence_quote": "Proposers get best stable partner; receivers get worst; extremes are provable.",
   "reasoning": "Both extremes and their provability are captured at L005, with the cross-link L052 confirming the closing verdict restates the mathematical extreme."
  },
  {
   "point_id": "K05",
   "point_text": "Most real-world situations do not follow the exact algorithm but share the same proposer/receiver structure, so the same pattern of advantage should be expected even when only approximate.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L007",
    "L011"
   ],
   "evidence_quote": "Most real situations share proposer-receiver structure without running exact algorithm.",
   "reasoning": "L007 states the structural generalization, and L011 adds that informal structures systematically favor whoever proposes, preserving the expected-advantage inference."
  },
  {
   "point_id": "K06",
   "point_text": "Everyday illustrations show most people are receivers: choosing Netflix by scrolling, picking among displayed phones, applying to posted jobs, accepting friendships formed by proximity.",
   "weight": "Nice to have",
   "presence": "Present",
   "loglog_ids": [
    "L008"
   ],
   "evidence_quote": "Receiver quiz: Netflix scroll, displayed phones, posted jobs, proximity friendships.",
   "reasoning": "All four illustrations appear in the same line, covering the receiver examples provided."
  },
  {
   "point_id": "K07",
   "point_text": "The insidious part is that receivers get acceptable, good-enough outcomes, so they never feel dissatisfied enough to change, and the system stays stable (self-sustaining) while quietly giving them less than they could have.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L010",
    "L012"
   ],
   "evidence_quote": "Receiving yields acceptable outcomes that quietly fall short of best.",
   "reasoning": "L010 captures good-enough outcomes that quietly fall short, and L012 captures comfortable outcomes blocking revolt and stability keeping the system intact."
  },
  {
   "point_id": "K08",
   "point_text": "Chicken-and-egg trap: you need intention to propose, but you develop intention through proposing; choosing among presented options only reveals what you dislike least, not what you would pursue.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L014",
    "L015",
    "L016"
   ],
   "evidence_quote": "Presented choices reveal least-disliked option, not what anyone would pursue freely.",
   "reasoning": "The mutual dependence of intention and proposing is at L014/L016, and the least-disliked versus freely-pursued distinction is preserved at L015."
  },
  {
   "point_id": "K09",
   "point_text": "Training ground: the muscle of intention builds progressively, so start small by intentionally deciding what you want from the next hour before opening any app, rather than scrolling until something catches you.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L018",
    "L019"
   ],
   "evidence_quote": "Intention muscle builds progressively from small exercises upward.",
   "reasoning": "L018 states progressive muscle building, L019 gives the small proximal exercise of deciding the feeling wanted then seeking it without scrolling recommendations. The 'before opening any app' framing is approximated by avoiding recommendations."
  },
  {
   "point_id": "K10",
   "point_text": "You cannot think your way into values, you have to practice your way into them: repeated intentional acts yield patterns, patterns become preferences, preferences become values.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L020",
    "L021"
   ],
   "evidence_quote": "Values come from practice, not from thought alone.",
   "reasoning": "L020 preserves the patterns to preferences to values chain, and L021 preserves the practice-over-thought claim."
  },
  {
   "point_id": "K11",
   "point_text": "Structural disadvantage does not disappear with understanding, you must actually switch positions, and proposing means deciding what you want before seeing options, pursuing specifics, creating opportunities, and accepting friction against default flows.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L029",
    "L030"
   ],
   "evidence_quote": "Understanding disadvantage changes nothing without switching to proposing.",
   "reasoning": "L029 states understanding is insufficient without switching, and L030 lists the four acts of proposing including accepting friction."
  },
  {
   "point_id": "K12",
   "point_text": "Collective effect: when most people are receivers, systems optimize for the proposers, namely the platforms, which capture optimal outcomes (attention, data, money) while users get only good-enough outcomes.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L025",
    "L026",
    "L027"
   ],
   "evidence_quote": "Platforms take optimal outcomes while users get participation-sustaining good-enough.",
   "reasoning": "L025 states receiver majorities let systems optimize for proposers, L026 gives the engagement-over-need examples, and L027 captures platforms taking optimal while users get good-enough."
  },
  {
   "point_id": "K13",
   "point_text": "Most people will not make the shift because it is effortful, the receiver position is comfortable, and after years of receiver mode many have lost the capacity to know what they would want to propose.",
   "weight": "Nice to have",
   "presence": "Present",
   "loglog_ids": [
    "L032"
   ],
   "evidence_quote": "Most refuse the effort; comfort plus atrophied wanting keeps receivers receiving.",
   "reasoning": "L032 preserves both causes: refusal of effort, comfort, and atrophied wanting closing the loop on lost capacity."
  },
  {
   "point_id": "K14",
   "point_text": "Practical progression: begin with tomorrow morning before checking your phone, practice for a week on small things (breakfast, evening activities, weekend plans), then scale to bigger decisions like work, relationships, and purchases.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L035",
    "L037",
    "L038"
   ],
   "evidence_quote": "Start tomorrow morning with the first hour, then scale practice upward.",
   "reasoning": "L035 begins tomorrow morning, L037 covers a week of logging small choices, and L038 scales to jobs, dating, and purchases. The specific small-thing menu is generalized but the progression is intact."
  },
  {
   "point_id": "K15",
   "point_text": "Appendix concrete tools: domain exercises (entertainment, shopping with must-haves and 24-hour rule over $100, career with 5 non-negotiables and applying only when 4 of 5 match, relationships), daily pause and journaling practices, and a 30-day tracking journal showing proposers report higher satisfaction.",
   "weight": "Nice to have",
   "presence": "Partial",
   "loglog_ids": [
    "L041",
    "L043",
    "L045",
    "L048",
    "L049"
   ],
   "evidence_quote": "Journal situation, mode, outcome; thirty days reveal proposer satisfaction pattern.",
   "reasoning": "All domains and practices are present, but the specific numeric thresholds are dropped: the $100 bar for the shopping 24-hour rule and the 4-of-5 match rule in career. Nice-to-have, so this lowers polish rather than recall of a must-have."
  }
 ],
 "metrics": {
  "total_points": 15,
  "must_have_total": 12,
  "must_have_present": 11,
  "must_have_partial": 1,
  "must_have_missing": 0,
  "overall_present": 13,
  "must_recall": 0.9583,
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
 "source_id": "07_intentionalism",
 "labels": [
  {
   "claim_id": "C001",
   "loglog_ids": [
    "0"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Top-level thesis, canonical source for proposer-advantage later restated."
  },
  {
   "claim_id": "C002",
   "loglog_ids": [
    "1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Historical fact about Gale-Shapley, unique background not repeated."
  },
  {
   "claim_id": "C003",
   "loglog_ids": [
    "1.1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Definition of deferred acceptance mechanism, distinct content."
  },
  {
   "claim_id": "C004",
   "loglog_ids": [
    "1.2"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Canonical mathematical proposer extreme, later recaps depend on it."
  },
  {
   "claim_id": "C005",
   "loglog_ids": [
    "1.3"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Canonical structural-not-talent-or-luck claim, first appearance."
  },
  {
   "claim_id": "C006",
   "loglog_ids": [
    "2"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Scope claim that real situations mirror the structure, distinct."
  },
  {
   "claim_id": "C007",
   "loglog_ids": [
    "2.1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Concrete receiver examples add specific detail."
  },
  {
   "claim_id": "C008",
   "loglog_ids": [
    "2.2"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Prevalence observation, distinct from the structural claim."
  },
  {
   "claim_id": "C009",
   "loglog_ids": [
    "3"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "General receiver-shortfall claim, first statement."
  },
  {
   "claim_id": "C010",
   "loglog_ids": [
    "3.1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Partially supported causal claim, kept visible and distinct."
  },
  {
   "claim_id": "C011",
   "loglog_ids": [
    "3.2"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Stability-via-comfort mechanism, new causal detail."
  },
  {
   "claim_id": "C012",
   "loglog_ids": [
    "3.3"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Ignorance from not practicing wanting, distinct."
  },
  {
   "claim_id": "C013",
   "loglog_ids": [
    "4"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Canonical intention-prerequisite-and-product claim, first statement."
  },
  {
   "claim_id": "C014",
   "loglog_ids": [
    "4.1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Least-disliked-choice nuance, distinct from example C016."
  },
  {
   "claim_id": "C015",
   "loglog_ids": [
    "4.2"
   ],
   "label": "Duplicate",
   "canonical_id": "C013",
   "reasoning": "Same prerequisite-product content as C013, only adds trap label."
  },
  {
   "claim_id": "C016",
   "loglog_ids": [
    "4.3"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Concrete algorithm and swipe example adds specificity."
  },
  {
   "claim_id": "C017",
   "loglog_ids": [
    "5"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Progressive muscle-building thesis, first statement."
  },
  {
   "claim_id": "C018",
   "loglog_ids": [
    "5.1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Tonight-feeling exercise, first appearance."
  },
  {
   "claim_id": "C019",
   "loglog_ids": [
    "5.2"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Canonical practice-to-patterns-to-values chain."
  },
  {
   "claim_id": "C020",
   "loglog_ids": [
    "5.3"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Negation not-from-thought-alone, negations never trivia."
  },
  {
   "claim_id": "C021",
   "loglog_ids": [
    "6"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Presented-options agency confusion, distinct."
  },
  {
   "claim_id": "C022",
   "loglog_ids": [
    "6.1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Seekers gain better outcomes, distinct from C032 extension."
  },
  {
   "claim_id": "C023",
   "loglog_ids": [
    "6.2"
   ],
   "label": "Duplicate",
   "canonical_id": "C005",
   "reasoning": "Restates C005 structural-over-personal-ability point."
  },
  {
   "claim_id": "C024",
   "loglog_ids": [
    "7"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Receiver-majority system-incentive claim, distinct."
  },
  {
   "claim_id": "C025",
   "loglog_ids": [
    "7.1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Platform engagement example, new specificity."
  },
  {
   "claim_id": "C026",
   "loglog_ids": [
    "7.2"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Platform optimal-vs-good-enough supports C009 but adds platform detail."
  },
  {
   "claim_id": "C027",
   "loglog_ids": [
    "7.3"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Switching-cost and resistance-to-change claim, distinct from C011."
  },
  {
   "claim_id": "C028",
   "loglog_ids": [
    "8"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Understanding-without-switching claim, distinct."
  },
  {
   "claim_id": "C029",
   "loglog_ids": [
    "8.1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Definition of proposing actions, distinct."
  },
  {
   "claim_id": "C030",
   "loglog_ids": [
    "8.2"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Canonical ask-what-wanted-before-deciding instruction."
  },
  {
   "claim_id": "C031",
   "loglog_ids": [
    "8.3"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Refusal and atrophied-wanting mechanism, distinct."
  },
  {
   "claim_id": "C032",
   "loglog_ids": [
    "8.4"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Shifters gain outside exact math, extends C022 with new scope."
  },
  {
   "claim_id": "C033",
   "loglog_ids": [
    "8.5"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Closing meta on willingness, distinct."
  },
  {
   "claim_id": "C034",
   "loglog_ids": [
    "9"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Concrete first-hour timing adds schedule detail to C017."
  },
  {
   "claim_id": "C035",
   "loglog_ids": [
    "9.1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Adds four feeling categories, new enumeration."
  },
  {
   "claim_id": "C036",
   "loglog_ids": [
    "9.2"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Scrolling-awareness and journaling exercise, new."
  },
  {
   "claim_id": "C037",
   "loglog_ids": [
    "9.3"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Domain-scaling recap with criteria-first, adds domains."
  },
  {
   "claim_id": "C038",
   "loglog_ids": [
    "9.4"
   ],
   "label": "Duplicate",
   "canonical_id": "C019",
   "reasoning": "Repeats C019 practice-to-values ladder as muscle-to-proposers chain."
  },
  {
   "claim_id": "C039",
   "loglog_ids": [
    "9.5"
   ],
   "label": "Duplicate",
   "canonical_id": "C004",
   "reasoning": "Restates C004 proposer-advantage and mathematical extreme."
  },
  {
   "claim_id": "C040",
   "loglog_ids": [
    "10"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Appendix roadmap, structural meta, distinct."
  },
  {
   "claim_id": "C041",
   "loglog_ids": [
    "10.1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Entertainment exercise, distinct recommendation."
  },
  {
   "claim_id": "C042",
   "loglog_ids": [
    "10.2"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Shopping exercise, distinct recommendation."
  },
  {
   "claim_id": "C043",
   "loglog_ids": [
    "10.3"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Toothpaste drill, distinct recommendation."
  },
  {
   "claim_id": "C044",
   "loglog_ids": [
    "10.4"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Career exercise, distinct recommendation."
  },
  {
   "claim_id": "C045",
   "loglog_ids": [
    "10.5"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Dating exercise, distinct recommendation."
  },
  {
   "claim_id": "C046",
   "loglog_ids": [
    "10.6"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Friendship exercise, distinct recommendation."
  },
  {
   "claim_id": "C047",
   "loglog_ids": [
    "10.7"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Daily routine exercise, distinct recommendation."
  },
  {
   "claim_id": "C048",
   "loglog_ids": [
    "10.8"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Journaling exercise, distinct recommendation."
  },
  {
   "claim_id": "C049",
   "loglog_ids": [
    "10.9"
   ],
   "label": "Duplicate",
   "canonical_id": "C030",
   "reasoning": "Restates ask-what-wanted (C030) and small-reps (C017), no new information."
  }
 ],
 "metrics": {
  "scored_claims": 49,
  "unique": 44,
  "duplicates": 5,
  "trivia": 0,
  "redundancy_rate": 0.102,
  "trivia_rate": 0.0,
  "structured_tokens": 502,
  "tokens_per_unique_claim": 11.41
 },
 "prune_list": [
  "C015 duplicates C013, safe to merge",
  "C023 duplicates C005, safe to merge",
  "C038 duplicates C019, safe to merge",
  "C039 duplicates C004, safe to merge",
  "C049 duplicates C030, safe to merge"
 ]
}
```

## Judge F (faithfulness), opencode-go/deepseek-v4.1-flash

```json
{
 "judge": "faithfulness",
 "judge_version": "1.0.0",
 "model": "opencode-go/deepseek-v4.1-flash (opencode) scripted pipeline 2026-09-15",
 "source_id": "07_intentionalism",
 "claims": [
  {
   "claim_id": "C001",
   "loglog_ids": [
    "0"
   ],
   "claim_text": "Life structurally favors proposers over receivers, so practice intending before choosing.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "It's about whether they propose or receive.",
   "reasoning": "SOURCE's thesis and closing call to practice intention match the summary."
  },
  {
   "claim_id": "C002",
   "loglog_ids": [
    "1"
   ],
   "claim_text": "Gale-Shapley 1962 stable-matching work revealed proposer-receiver asymmetry.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "In 1962, mathematician-economists David Gale and Lloyd Shapley",
   "reasoning": "Date, names, and the proposer-receiver discovery all appear in SOURCE."
  },
  {
   "claim_id": "C003",
   "loglog_ids": [
    "1.1"
   ],
   "claim_text": "Deferred acceptance: one side proposes in order, other tentatively accepts or rejects.",
   "claim_type": "definition",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "one side makes proposals in order of preference, and the other side accepts or tentatively rejects",
   "reasoning": "Definition matches SOURCE almost verbatim."
  },
  {
   "claim_id": "C004",
   "loglog_ids": [
    "1.2"
   ],
   "claim_text": "Proposers get best stable partner; receivers get worst; extremes are provable.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "each individual proposer ends up with the best stable partner",
   "reasoning": "SOURCE states best for proposers, worst for receivers, provably extreme."
  },
  {
   "claim_id": "C005",
   "loglog_ids": [
    "1.3"
   ],
   "claim_text": "Better outcomes come from proposing versus receiving, not talent or luck.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "nothing to do with talent, luck",
   "reasoning": "SOURCE explicitly excludes talent and luck."
  },
  {
   "claim_id": "C006",
   "loglog_ids": [
    "2"
   ],
   "claim_text": "Most real situations share proposer-receiver structure without running exact algorithm.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "most real-world situations don't follow the exact Gale-Shapley algorithm",
   "reasoning": "SOURCE states real cases share the structure but not the exact algorithm."
  },
  {
   "claim_id": "C007",
   "loglog_ids": [
    "2.1"
   ],
   "claim_text": "Receiver quiz: Netflix scroll, displayed phones, posted jobs, proximity friendships.",
   "claim_type": "meta",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "scroll through recommendations until something looked good enough",
   "reasoning": "All four examples appear in SOURCE with the same receiver framing."
  },
  {
   "claim_id": "C008",
   "loglog_ids": [
    "2.2"
   ],
   "claim_text": "Most of us mostly receive, choosing from presented rather than pursuing wanted.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "For most of these, most of us are receivers.",
   "reasoning": "SOURCE states most of us are receivers choosing from presented options."
  },
  {
   "claim_id": "C009",
   "loglog_ids": [
    "3"
   ],
   "claim_text": "Receiving yields acceptable outcomes that quietly fall short of best.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "You get acceptable ones. Good enough ones.",
   "reasoning": "SOURCE contrasts acceptable outcomes with what would serve you best."
  },
  {
   "claim_id": "C010",
   "loglog_ids": [
    "3.1"
   ],
   "claim_text": "Informal proposer-receiver structures systematically favor whoever proposes.",
   "claim_type": "causal_link",
   "verdict": "Partially supported",
   "severity": "Minor",
   "evidence_quote": "the outcomes tend to favor whoever's doing the proposing",
   "reasoning": "SOURCE hedges with 'tend to'; loglog states it as absolute systematic fact."
  },
  {
   "claim_id": "C011",
   "loglog_ids": [
    "3.2"
   ],
   "claim_text": "Comfortable outcomes block revolt; system stays stable by never screwing badly.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "doesn't screw you badly enough to make you revolt",
   "reasoning": "SOURCE says stability arises because outcomes are not bad enough to revolt."
  },
  {
   "claim_id": "C012",
   "loglog_ids": [
    "3.3"
   ],
   "claim_text": "Without practicing specific wanting, people cannot know what they miss.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "You don't even know what you're missing, because you've never practiced wanting something specific",
   "reasoning": "SOURCE directly states the causal link."
  },
  {
   "claim_id": "C013",
   "loglog_ids": [
    "4"
   ],
   "claim_text": "Proposing needs intention, but intention develops through proposing.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "You need intention to propose, but you develop intention through proposing.",
   "reasoning": "Matches SOURCE's chicken-and-egg statement."
  },
  {
   "claim_id": "C014",
   "loglog_ids": [
    "4.1"
   ],
   "claim_text": "Presented choices reveal least-disliked option, not what anyone would pursue freely.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "reveal which option you dislike least among what's available",
   "reasoning": "SOURCE states choices reveal least-disliked, not freely pursued wants."
  },
  {
   "claim_id": "C015",
   "loglog_ids": [
    "4.2"
   ],
   "claim_text": "The trap: intention is prerequisite and product of proposing.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "This is the trap. You need intention to propose, but you develop intention through proposing.",
   "reasoning": "SOURCE labels this the trap with both directions."
  },
  {
   "claim_id": "C016",
   "loglog_ids": [
    "4.3"
   ],
   "claim_text": "Algorithm-fed songs and swiped partners may be reactions mistaken for preferences.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "preferences\" are just reactions to what gets put in front of them",
   "reasoning": "SOURCE makes the same point using music and dating examples."
  },
  {
   "claim_id": "C017",
   "loglog_ids": [
    "5"
   ],
   "claim_text": "Intention muscle builds progressively from small exercises upward.",
   "claim_type": "recommendation",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "The muscle of intention and initiative builds progressively.",
   "reasoning": "Matches SOURCE's progression claim."
  },
  {
   "claim_id": "C018",
   "loglog_ids": [
    "5.1"
   ],
   "claim_text": "Tonight decide the feeling wanted, then seek it without scrolling recommendations.",
   "claim_type": "recommendation",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "Don't open Netflix and see what it suggests.",
   "reasoning": "SOURCE gives the same tonight exercise and warnings."
  },
  {
   "claim_id": "C019",
   "loglog_ids": [
    "5.2"
   ],
   "claim_text": "Repeated practice surfaces patterns that become preferences then values.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "Those patterns become preferences. Those preferences become values.",
   "reasoning": "SOURCE states the exact chain."
  },
  {
   "claim_id": "C020",
   "loglog_ids": [
    "5.3"
   ],
   "claim_text": "Values come from practice, not from thought alone.",
   "claim_type": "recommendation",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "You can't think your way into values. You have to practice your way into them.",
   "reasoning": "Matches SOURCE verbatim in meaning."
  },
  {
   "claim_id": "C021",
   "loglog_ids": [
    "6"
   ],
   "claim_text": "Major decisions mostly evaluate presented options, mistaking receipt for agency.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "This feels like agency because you're choosing. But you're choosing as a receiver",
   "reasoning": "SOURCE says most evaluate presented options while feeling agency."
  },
  {
   "claim_id": "C022",
   "loglog_ids": [
    "6.1"
   ],
   "claim_text": "Intentional seekers of work, partners, cities gain systematically better outcomes.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "those people end up with systematically better outcomes",
   "reasoning": "SOURCE lists the same three domains and outcome."
  },
  {
   "claim_id": "C023",
   "loglog_ids": [
    "6.2"
   ],
   "claim_text": "Advantage comes from structural side, not superior smarts or luck.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "Not because they're smarter or luckier.",
   "reasoning": "SOURCE explicitly denies smarter or luckier."
  },
  {
   "claim_id": "C024",
   "loglog_ids": [
    "7"
   ],
   "claim_text": "Receiver majorities let systems optimize for proposers instead of users.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "When most people are receivers, entire systems shift to optimize for whoever's doing the proposing.",
   "reasoning": "Matches SOURCE's collective effect claim."
  },
  {
   "claim_id": "C025",
   "loglog_ids": [
    "7.1"
   ],
   "claim_text": "Products, dating apps, feeds maximize engagement over genuine need or compatibility.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "they optimize for engagement among available profiles",
   "reasoning": "All three platform examples match SOURCE."
  },
  {
   "claim_id": "C026",
   "loglog_ids": [
    "7.2"
   ],
   "claim_text": "Platforms take optimal outcomes while users get participation-sustaining good-enough.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "good enough to keep you participating, but not actually serving your best interests",
   "reasoning": "Matches SOURCE's platform versus user outcome split."
  },
  {
   "claim_id": "C027",
   "loglog_ids": [
    "7.3"
   ],
   "claim_text": "Leaving feels harder than accepting; stability means resistance to change.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "That's stability (resistance to change). That's why the system persists.",
   "reasoning": "Matches SOURCE verbatim."
  },
  {
   "claim_id": "C028",
   "loglog_ids": [
    "8"
   ],
   "claim_text": "Understanding disadvantage changes nothing without switching to proposing.",
   "claim_type": "recommendation",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "doesn't go away because you understand it. You have to actually switch positions.",
   "reasoning": "Matches SOURCE's breaking-out claim."
  },
  {
   "claim_id": "C029",
   "loglog_ids": [
    "8.1"
   ],
   "claim_text": "Proposing means deciding first, pursuing specifics, creating chances, accepting friction.",
   "claim_type": "definition",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "Being willing to create opportunities rather than waiting for them",
   "reasoning": "All four bullet points derive from SOURCE's list."
  },
  {
   "claim_id": "C030",
   "loglog_ids": [
    "8.2"
   ],
   "claim_text": "Ask what is wanted before every decision, then act despite inconvenience.",
   "claim_type": "recommendation",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "before every major decision and most minor ones",
   "reasoning": "Matches SOURCE including the inconvenience clause."
  },
  {
   "claim_id": "C031",
   "loglog_ids": [
    "8.3"
   ],
   "claim_text": "Most refuse the effort; comfort plus atrophied wanting keeps receivers receiving.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "Most people won't do this. It's effortful.",
   "reasoning": "SOURCE states most won't, comfort suffices, and capacity is lost."
  },
  {
   "claim_id": "C032",
   "loglog_ids": [
    "8.4"
   ],
   "claim_text": "Shifters gain structurally better outcomes even outside exact mathematics.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "Systematically better. Not just incrementally—structurally.",
   "reasoning": "Matches SOURCE's claim for those who shift."
  },
  {
   "claim_id": "C033",
   "loglog_ids": [
    "8.5"
   ],
   "claim_text": "Dynamic existence is settled; only willingness to act remains open.",
   "claim_type": "meta",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "The question is whether you're willing to do something about it.",
   "reasoning": "SOURCE frames existence as settled and willingness as the open question."
  },
  {
   "claim_id": "C034",
   "loglog_ids": [
    "9"
   ],
   "claim_text": "Start tomorrow morning with the first hour, then scale practice upward.",
   "claim_type": "recommendation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Start with tomorrow morning. ... Then scale up. Apply it to bigger decisions.",
   "reasoning": "Source explicitly advises starting tomorrow morning and then scaling to larger decisions."
  },
  {
   "claim_id": "C035",
   "loglog_ids": [
    "9.1"
   ],
   "claim_text": "Name calm, energy, connection, or solitude; pursue it instead of notifications.",
   "claim_type": "recommendation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "do you want calm? Energy? Connection? Solitude? ... Then pursue that.",
   "reasoning": "Source lists exactly these four options and advises pursuing the chosen one over notifications."
  },
  {
   "claim_id": "C036",
   "loglog_ids": [
    "9.2"
   ],
   "claim_text": "Notice scrolling versus intending; log satisfaction across small choices for a week.",
   "claim_type": "recommendation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Notice how different this feels from scrolling ... Do this for a week with small things ... Notice what actually satisfies you",
   "reasoning": "Source prescribes noticing the contrast and tracking satisfaction over a week of small choices."
  },
  {
   "claim_id": "C037",
   "loglog_ids": [
    "9.3"
   ],
   "claim_text": "Scale to jobs, dating, purchases by deciding criteria before browsing options.",
   "claim_type": "recommendation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Before looking at job postings, decide what kind of work you want ... Before swiping on dating apps ... Before browsing products",
   "reasoning": "Source gives exactly these three domains and the decide-first ordering."
  },
  {
   "claim_id": "C038",
   "loglog_ids": [
    "9.4"
   ],
   "claim_text": "Muscle enables intentions, intentions become values, values make proposers.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "The muscle enables larger intentions. Larger intentions become values. Values make you a proposer.",
   "reasoning": "Nearly verbatim restatement of the source's causal chain."
  },
  {
   "claim_id": "C039",
   "loglog_ids": [
    "9.5"
   ],
   "claim_text": "Proposers end better across math and mess, not from specialness but position.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "proposers—whether in the pure mathematics ... or in the messy approximations of real life—end up with better outcomes. Not because they're special.",
   "reasoning": "Source states the same outcome across both settings and attributes it to position, not specialness."
  },
  {
   "claim_id": "C040",
   "loglog_ids": [
    "10"
   ],
   "claim_text": "Appendix gives progressive exercises for entertainment, shopping, jobs, relationships, days.",
   "claim_type": "meta",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "practicing intention in progressively larger domains. Here are specific exercises for the scenarios mentioned throughout this post.",
   "reasoning": "Appendix covers entertainment, shopping, jobs, relationships, and daily micro-practices as listed."
  },
  {
   "claim_id": "C041",
   "loglog_ids": [
    "10.1"
   ],
   "claim_text": "Entertainment: name intention week one, seek week two, protect with timers week three.",
   "claim_type": "recommendation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Week 1: Name your intention ... Week 2: Seek intentionally ... Week 3: Protect your intention ... Set a timer",
   "reasoning": "Source lays out the same three weekly stages including timers in week three."
  },
  {
   "claim_id": "C042",
   "loglog_ids": [
    "10.2"
   ],
   "claim_text": "Shopping: define problem, list must-haves, research features, ignore layout, 24-hour rule.",
   "claim_type": "recommendation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Define the problem ... List must-haves ... Research intentionally ... Ignore the store layout ... 24-hour rule",
   "reasoning": "All five listed steps appear in the source's numbered shopping list."
  },
  {
   "claim_id": "C043",
   "loglog_ids": [
    "10.3"
   ],
   "claim_text": "Toothpaste drill: identify need, find ingredient, buy it, notice packaging-free choosing.",
   "claim_type": "recommendation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Research which ingredient addresses that need ... find that ingredient, buy it ... comparing packaging",
   "reasoning": "Source's toothpaste practice run matches each step."
  },
  {
   "claim_id": "C044",
   "loglog_ids": [
    "10.4"
   ],
   "claim_text": "Career: set five non-negotiables, approach firms directly, apply only to strong matches.",
   "claim_type": "recommendation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Write 5 non-negotiables ... Contact people at those companies ... Only apply to roles that match at least 4 of your 5 criteria",
   "reasoning": "Source specifies five criteria, direct outreach, and applying only to sufficiently matching roles."
  },
  {
   "claim_id": "C045",
   "loglog_ids": [
    "10.5"
   ],
   "claim_text": "Dating: write relationship vision, require value alignment, filter first dates intentionally.",
   "claim_type": "recommendation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Write your relationship intention ... Identify values alignment ... First date filter: Ask questions that reveal value alignment",
   "reasoning": "Source lists these dating steps in the same order and intent."
  },
  {
   "claim_id": "C046",
   "loglog_ids": [
    "10.6"
   ],
   "claim_text": "Friendship: name needed qualities, join matching communities, initiate specific activities.",
   "claim_type": "recommendation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Name what you need ... Join specific communities ... Initiate based on intention: Invite people to do specific things",
   "reasoning": "Source's friendship steps match the node."
  },
  {
   "claim_id": "C047",
   "loglog_ids": [
    "10.7"
   ],
   "claim_text": "Daily: three morning intentions, evening proposer review, ten-second pause before choices.",
   "claim_type": "recommendation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "What are my three intentions for today? ... Evening review ... pause for 10 seconds",
   "reasoning": "Source contains each of the three daily micro-practices at the stated quantities."
  },
  {
   "claim_id": "C048",
   "loglog_ids": [
    "10.8"
   ],
   "claim_text": "Journal situation, mode, outcome; thirty days reveal proposer satisfaction pattern.",
   "claim_type": "recommendation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "three columns: Situation ... Mode ... Outcome ... After 30 days ... Proposer entries will show higher satisfaction.",
   "reasoning": "Source specifies the three columns and the 30-day proposer-satisfaction pattern."
  },
  {
   "claim_id": "C049",
   "loglog_ids": [
    "10.9"
   ],
   "claim_text": "Intention means asking what is wanted before others answer; small reps grow capacity.",
   "claim_type": "definition",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "It's about practicing the question \"what do I want?\" before someone else provides the answer. Start small. The muscle builds. The capacity grows.",
   "reasoning": "Source defines intention the same way and describes small starts growing capacity."
  }
 ],
 "metrics": {
  "total_claims": 49,
  "supported": 48,
  "partially_supported": 1,
  "unverifiable": 0,
  "contradicted": 0,
  "critical_errors": 0,
  "faithfulness_precision": 0.9796
 },
 "fail_list": [
  "C010"
 ]
}
```

## Judge Cov (coverage), opencode-go/deepseek-v4.1-flash

```json
{
 "judge": "coverage",
 "judge_version": "1.0.0",
 "model": "opencode-go/deepseek-v4.1-flash (opencode) scripted pipeline 2026-09-15",
 "source_id": "07_intentionalism",
 "key_points": [
  {
   "point_id": "K01",
   "point_text": "Central thesis: proposers systematically end up with better outcomes than receivers, and this is not because of talent, luck, or the quality of their choices.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L002",
    "L006",
    "L040"
   ],
   "evidence_quote": "Nuance: Better outcomes come from proposing versus receiving, not talent or luck.",
   "reasoning": "Thesis is stated at L002 and the causal exclusion of talent/luck is captured explicitly at L006. L040 restates ending better by position rather than specialness."
  },
  {
   "point_id": "K02",
   "point_text": "In 1962 mathematicians-economists David Gale and Lloyd Shapley worked on creating stable pairings between two groups and proved a stable matching (no unmatched pair preferring each other) always exists.",
   "weight": "Must have",
   "presence": "Partial",
   "loglog_ids": [
    "L003"
   ],
   "evidence_quote": "1 Gale-Shapley 1962 stable-matching work revealed proposer-receiver asymmetry.",
   "reasoning": "The date 1962, the names Gale-Shapley, and the stable-matching subject are retained, but the existence proof (a stable matching always exists) and the definition of stability (no blocking pair) are dropped. Must-have point with a lost claim, so Partial."
  },
  {
   "point_id": "K03",
   "point_text": "Their deferred acceptance algorithm works by having one side propose in order of preference while the other side accepts or tentatively rejects based on its preferences.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L004"
   ],
   "evidence_quote": "Evidence: Deferred acceptance: one side proposes in order, other tentatively accepts or rejects.",
   "reasoning": "Mechanism is fully captured: one side proposes in order, the other tentatively accepts or rejects. 'In order' preserves the preference-ordering substance."
  },
  {
   "point_id": "K04",
   "point_text": "Core mathematical result: proposers each get their best possible stable partner and receivers each get their worst possible stable partner, a provably extreme gap, not a slight difference.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L005",
    "L052"
   ],
   "evidence_quote": "Proposers get best stable partner; receivers get worst; extremes are provable.",
   "reasoning": "Both extremes and their provability are captured at L005, with the cross-link L052 confirming the closing verdict restates the mathematical extreme."
  },
  {
   "point_id": "K05",
   "point_text": "Most real-world situations do not follow the exact algorithm but share the same proposer/receiver structure, so the same pattern of advantage should be expected even when only approximate.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L007",
    "L011"
   ],
   "evidence_quote": "Most real situations share proposer-receiver structure without running exact algorithm.",
   "reasoning": "L007 states the structural generalization, and L011 adds that informal structures systematically favor whoever proposes, preserving the expected-advantage inference."
  },
  {
   "point_id": "K06",
   "point_text": "Everyday illustrations show most people are receivers: choosing Netflix by scrolling, picking among displayed phones, applying to posted jobs, accepting friendships formed by proximity.",
   "weight": "Nice to have",
   "presence": "Present",
   "loglog_ids": [
    "L008"
   ],
   "evidence_quote": "Receiver quiz: Netflix scroll, displayed phones, posted jobs, proximity friendships.",
   "reasoning": "All four illustrations appear in the same line, covering the receiver examples provided."
  },
  {
   "point_id": "K07",
   "point_text": "The insidious part is that receivers get acceptable, good-enough outcomes, so they never feel dissatisfied enough to change, and the system stays stable (self-sustaining) while quietly giving them less than they could have.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L010",
    "L012"
   ],
   "evidence_quote": "Receiving yields acceptable outcomes that quietly fall short of best.",
   "reasoning": "L010 captures good-enough outcomes that quietly fall short, and L012 captures comfortable outcomes blocking revolt and stability keeping the system intact."
  },
  {
   "point_id": "K08",
   "point_text": "Chicken-and-egg trap: you need intention to propose, but you develop intention through proposing; choosing among presented options only reveals what you dislike least, not what you would pursue.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L014",
    "L015",
    "L016"
   ],
   "evidence_quote": "Presented choices reveal least-disliked option, not what anyone would pursue freely.",
   "reasoning": "The mutual dependence of intention and proposing is at L014/L016, and the least-disliked versus freely-pursued distinction is preserved at L015."
  },
  {
   "point_id": "K09",
   "point_text": "Training ground: the muscle of intention builds progressively, so start small by intentionally deciding what you want from the next hour before opening any app, rather than scrolling until something catches you.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L018",
    "L019"
   ],
   "evidence_quote": "Intention muscle builds progressively from small exercises upward.",
   "reasoning": "L018 states progressive muscle building, L019 gives the small proximal exercise of deciding the feeling wanted then seeking it without scrolling recommendations. The 'before opening any app' framing is approximated by avoiding recommendations."
  },
  {
   "point_id": "K10",
   "point_text": "You cannot think your way into values, you have to practice your way into them: repeated intentional acts yield patterns, patterns become preferences, preferences become values.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L020",
    "L021"
   ],
   "evidence_quote": "Values come from practice, not from thought alone.",
   "reasoning": "L020 preserves the patterns to preferences to values chain, and L021 preserves the practice-over-thought claim."
  },
  {
   "point_id": "K11",
   "point_text": "Structural disadvantage does not disappear with understanding, you must actually switch positions, and proposing means deciding what you want before seeing options, pursuing specifics, creating opportunities, and accepting friction against default flows.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L029",
    "L030"
   ],
   "evidence_quote": "Understanding disadvantage changes nothing without switching to proposing.",
   "reasoning": "L029 states understanding is insufficient without switching, and L030 lists the four acts of proposing including accepting friction."
  },
  {
   "point_id": "K12",
   "point_text": "Collective effect: when most people are receivers, systems optimize for the proposers, namely the platforms, which capture optimal outcomes (attention, data, money) while users get only good-enough outcomes.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L025",
    "L026",
    "L027"
   ],
   "evidence_quote": "Platforms take optimal outcomes while users get participation-sustaining good-enough.",
   "reasoning": "L025 states receiver majorities let systems optimize for proposers, L026 gives the engagement-over-need examples, and L027 captures platforms taking optimal while users get good-enough."
  },
  {
   "point_id": "K13",
   "point_text": "Most people will not make the shift because it is effortful, the receiver position is comfortable, and after years of receiver mode many have lost the capacity to know what they would want to propose.",
   "weight": "Nice to have",
   "presence": "Present",
   "loglog_ids": [
    "L032"
   ],
   "evidence_quote": "Most refuse the effort; comfort plus atrophied wanting keeps receivers receiving.",
   "reasoning": "L032 preserves both causes: refusal of effort, comfort, and atrophied wanting closing the loop on lost capacity."
  },
  {
   "point_id": "K14",
   "point_text": "Practical progression: begin with tomorrow morning before checking your phone, practice for a week on small things (breakfast, evening activities, weekend plans), then scale to bigger decisions like work, relationships, and purchases.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L035",
    "L037",
    "L038"
   ],
   "evidence_quote": "Start tomorrow morning with the first hour, then scale practice upward.",
   "reasoning": "L035 begins tomorrow morning, L037 covers a week of logging small choices, and L038 scales to jobs, dating, and purchases. The specific small-thing menu is generalized but the progression is intact."
  },
  {
   "point_id": "K15",
   "point_text": "Appendix concrete tools: domain exercises (entertainment, shopping with must-haves and 24-hour rule over $100, career with 5 non-negotiables and applying only when 4 of 5 match, relationships), daily pause and journaling practices, and a 30-day tracking journal showing proposers report higher satisfaction.",
   "weight": "Nice to have",
   "presence": "Partial",
   "loglog_ids": [
    "L041",
    "L043",
    "L045",
    "L048",
    "L049"
   ],
   "evidence_quote": "Journal situation, mode, outcome; thirty days reveal proposer satisfaction pattern.",
   "reasoning": "All domains and practices are present, but the specific numeric thresholds are dropped: the $100 bar for the shopping 24-hour rule and the 4-of-5 match rule in career. Nice-to-have, so this lowers polish rather than recall of a must-have."
  }
 ],
 "metrics": {
  "total_points": 15,
  "must_have_total": 12,
  "must_have_present": 11,
  "must_have_partial": 1,
  "must_have_missing": 0,
  "overall_present": 13,
  "must_recall": 0.9583,
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
 "source_id": "07_intentionalism",
 "labels": [
  {
   "claim_id": "C001",
   "loglog_ids": [
    "0"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Top-level thesis, canonical source for proposer-advantage later restated."
  },
  {
   "claim_id": "C002",
   "loglog_ids": [
    "1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Historical fact about Gale-Shapley, unique background not repeated."
  },
  {
   "claim_id": "C003",
   "loglog_ids": [
    "1.1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Definition of deferred acceptance mechanism, distinct content."
  },
  {
   "claim_id": "C004",
   "loglog_ids": [
    "1.2"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Canonical mathematical proposer extreme, later recaps depend on it."
  },
  {
   "claim_id": "C005",
   "loglog_ids": [
    "1.3"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Canonical structural-not-talent-or-luck claim, first appearance."
  },
  {
   "claim_id": "C006",
   "loglog_ids": [
    "2"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Scope claim that real situations mirror the structure, distinct."
  },
  {
   "claim_id": "C007",
   "loglog_ids": [
    "2.1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Concrete receiver examples add specific detail."
  },
  {
   "claim_id": "C008",
   "loglog_ids": [
    "2.2"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Prevalence observation, distinct from the structural claim."
  },
  {
   "claim_id": "C009",
   "loglog_ids": [
    "3"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "General receiver-shortfall claim, first statement."
  },
  {
   "claim_id": "C010",
   "loglog_ids": [
    "3.1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Partially supported causal claim, kept visible and distinct."
  },
  {
   "claim_id": "C011",
   "loglog_ids": [
    "3.2"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Stability-via-comfort mechanism, new causal detail."
  },
  {
   "claim_id": "C012",
   "loglog_ids": [
    "3.3"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Ignorance from not practicing wanting, distinct."
  },
  {
   "claim_id": "C013",
   "loglog_ids": [
    "4"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Canonical intention-prerequisite-and-product claim, first statement."
  },
  {
   "claim_id": "C014",
   "loglog_ids": [
    "4.1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Least-disliked-choice nuance, distinct from example C016."
  },
  {
   "claim_id": "C015",
   "loglog_ids": [
    "4.2"
   ],
   "label": "Duplicate",
   "canonical_id": "C013",
   "reasoning": "Same prerequisite-product content as C013, only adds trap label."
  },
  {
   "claim_id": "C016",
   "loglog_ids": [
    "4.3"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Concrete algorithm and swipe example adds specificity."
  },
  {
   "claim_id": "C017",
   "loglog_ids": [
    "5"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Progressive muscle-building thesis, first statement."
  },
  {
   "claim_id": "C018",
   "loglog_ids": [
    "5.1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Tonight-feeling exercise, first appearance."
  },
  {
   "claim_id": "C019",
   "loglog_ids": [
    "5.2"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Canonical practice-to-patterns-to-values chain."
  },
  {
   "claim_id": "C020",
   "loglog_ids": [
    "5.3"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Negation not-from-thought-alone, negations never trivia."
  },
  {
   "claim_id": "C021",
   "loglog_ids": [
    "6"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Presented-options agency confusion, distinct."
  },
  {
   "claim_id": "C022",
   "loglog_ids": [
    "6.1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Seekers gain better outcomes, distinct from C032 extension."
  },
  {
   "claim_id": "C023",
   "loglog_ids": [
    "6.2"
   ],
   "label": "Duplicate",
   "canonical_id": "C005",
   "reasoning": "Restates C005 structural-over-personal-ability point."
  },
  {
   "claim_id": "C024",
   "loglog_ids": [
    "7"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Receiver-majority system-incentive claim, distinct."
  },
  {
   "claim_id": "C025",
   "loglog_ids": [
    "7.1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Platform engagement example, new specificity."
  },
  {
   "claim_id": "C026",
   "loglog_ids": [
    "7.2"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Platform optimal-vs-good-enough supports C009 but adds platform detail."
  },
  {
   "claim_id": "C027",
   "loglog_ids": [
    "7.3"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Switching-cost and resistance-to-change claim, distinct from C011."
  },
  {
   "claim_id": "C028",
   "loglog_ids": [
    "8"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Understanding-without-switching claim, distinct."
  },
  {
   "claim_id": "C029",
   "loglog_ids": [
    "8.1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Definition of proposing actions, distinct."
  },
  {
   "claim_id": "C030",
   "loglog_ids": [
    "8.2"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Canonical ask-what-wanted-before-deciding instruction."
  },
  {
   "claim_id": "C031",
   "loglog_ids": [
    "8.3"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Refusal and atrophied-wanting mechanism, distinct."
  },
  {
   "claim_id": "C032",
   "loglog_ids": [
    "8.4"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Shifters gain outside exact math, extends C022 with new scope."
  },
  {
   "claim_id": "C033",
   "loglog_ids": [
    "8.5"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Closing meta on willingness, distinct."
  },
  {
   "claim_id": "C034",
   "loglog_ids": [
    "9"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Concrete first-hour timing adds schedule detail to C017."
  },
  {
   "claim_id": "C035",
   "loglog_ids": [
    "9.1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Adds four feeling categories, new enumeration."
  },
  {
   "claim_id": "C036",
   "loglog_ids": [
    "9.2"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Scrolling-awareness and journaling exercise, new."
  },
  {
   "claim_id": "C037",
   "loglog_ids": [
    "9.3"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Domain-scaling recap with criteria-first, adds domains."
  },
  {
   "claim_id": "C038",
   "loglog_ids": [
    "9.4"
   ],
   "label": "Duplicate",
   "canonical_id": "C019",
   "reasoning": "Repeats C019 practice-to-values ladder as muscle-to-proposers chain."
  },
  {
   "claim_id": "C039",
   "loglog_ids": [
    "9.5"
   ],
   "label": "Duplicate",
   "canonical_id": "C004",
   "reasoning": "Restates C004 proposer-advantage and mathematical extreme."
  },
  {
   "claim_id": "C040",
   "loglog_ids": [
    "10"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Appendix roadmap, structural meta, distinct."
  },
  {
   "claim_id": "C041",
   "loglog_ids": [
    "10.1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Entertainment exercise, distinct recommendation."
  },
  {
   "claim_id": "C042",
   "loglog_ids": [
    "10.2"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Shopping exercise, distinct recommendation."
  },
  {
   "claim_id": "C043",
   "loglog_ids": [
    "10.3"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Toothpaste drill, distinct recommendation."
  },
  {
   "claim_id": "C044",
   "loglog_ids": [
    "10.4"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Career exercise, distinct recommendation."
  },
  {
   "claim_id": "C045",
   "loglog_ids": [
    "10.5"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Dating exercise, distinct recommendation."
  },
  {
   "claim_id": "C046",
   "loglog_ids": [
    "10.6"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Friendship exercise, distinct recommendation."
  },
  {
   "claim_id": "C047",
   "loglog_ids": [
    "10.7"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Daily routine exercise, distinct recommendation."
  },
  {
   "claim_id": "C048",
   "loglog_ids": [
    "10.8"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Journaling exercise, distinct recommendation."
  },
  {
   "claim_id": "C049",
   "loglog_ids": [
    "10.9"
   ],
   "label": "Duplicate",
   "canonical_id": "C030",
   "reasoning": "Restates ask-what-wanted (C030) and small-reps (C017), no new information."
  }
 ],
 "metrics": {
  "scored_claims": 49,
  "unique": 44,
  "duplicates": 5,
  "trivia": 0,
  "redundancy_rate": 0.102,
  "trivia_rate": 0.0,
  "structured_tokens": 502,
  "tokens_per_unique_claim": 11.41
 },
 "prune_list": [
  "C015 duplicates C013, safe to merge",
  "C023 duplicates C005, safe to merge",
  "C038 duplicates C019, safe to merge",
  "C039 duplicates C004, safe to merge",
  "C049 duplicates C030, safe to merge"
 ]
}
```

## Judge Top (overall), opencode-go/deepseek-v4.1-flash

```json
{
 "judge": "overall",
 "judge_version": "1.0.0",
 "model": "opencode/deepseek-v4.1-flash 2026-09-15",
 "source_id": "point-hierarchy",
 "inputs": {
  "faithfulness_precision": 0.9796,
  "critical_errors": 0,
  "must_recall": 0.9583,
  "overall_recall": 0.9333,
  "redundancy_rate": 0.102,
  "trivia_rate": 0.0
 },
 "weights_used": {
  "faithfulness_precision": 0.4,
  "coverage_must_recall": 0.4,
  "redundancy_penalty": 0.2
 },
 "computation": "weighted score = 0.4*0.9796 + 0.4*0.9583 - 0.2*0.102 = 0.39184 + 0.38332 - 0.0204 = 0.75476",
 "weighted_score": 0.75476,
 "verdict": "Borderline",
 "tradeoff_note": "All numeric gates pass cleanly (precision 0.9796 >= 0.95, must recall 0.9583 >= 0.9, redundancy 0.102 <= 0.15) with zero critical errors, but Must-have point K02 is only Partial (lost the existence proof and stability definition) and C010 is a Minor partial hedge, so human review is advised.",
 "fix_list": [
  "K02 (Must have, L003): restore the guarantee that a stable matching always exists and the stability definition (no blocking pair preferring each other); this is the only Must-have recall loss and the top lever.",
  "C010 (Minor, 3.1): hedge the absolute claim 'systematically favor whoever proposes' back to SOURCE's 'tend to favor' to clear the last partial support.",
  "K15 (Nice to have, L041/L043/L045/L048/L049): reinsert the dropped numeric thresholds, the $100 bar for the 24-hour shopping rule and the 4-of-5 career match rule, to convert a Partial to Present.",
  "Merge duplicate claims C015/C013, C023/C005, C038/C019, C039/C004, C049/C030 to push redundancy further below the 0.15 cap."
 ],
 "reasoning": "Hard gates first. critical_errors = 0, which equals critical_contradicted_max = 0, so no Critical fail. faithfulness_precision = 0.9796 >= faithfulness_precision_min = 0.95, pass. must_recall = 0.9583 >= must_recall_min = 0.9, pass. redundancy_rate = 0.102 <= redundancy_max = 0.15, pass. No hard gate is missed and no Critical error exists, so the sample cannot be a Fail. Tradeoff among passes: weighted score = 0.4*(0.9796) + 0.4*(0.9583) - 0.2*(0.102) = 0.39184 + 0.38332 - 0.0204 = 0.75476. Concision plays no rescue role here because there is no faithfulness or coverage fail; it only contributes a 0.0204 penalty, and its low redundancy (0.102) is well under cap so no coverage-driven length needs trimming. Borderline trigger applies: gates pass on numbers, but Must-have K02 is Partial. Judge Cov marks K02 Partial because the 1962 date, Gale-Shapley names, and stable-matching subject survive while two substantive claims are dropped, the existence proof ('a stable matching always exists') and the stability definition ('no unmatched pair preferring each other'), evidence quote L003 'Gale-Shapley 1962 stable-matching work revealed proposer-receiver asymmetry.' A Partial on a Must have point is exactly the Borderline condition, so I name K02. The faithfulness side has one non-critical partial: C010 (loglog 3.1), where SOURCE hedges 'the outcomes tend to favor whoever's doing the proposing' but the loglog states the systematic absolute; severity Minor, so it does not force a Fail but reinforces Borderline. Coverage loss is concentrated in two points (K02 Must have Partial; K15 Nice-to-have Partial missing the $100 and 4-of-5 thresholds), with 11/12 Must-haves fully Present and 0 Must-haves Missing, so the loss is a completeness gap, not a hole. Faithfulness precision 48/49 supported with 0 contradicted and 0 unverifiable is strong. Verdict: Borderline, human review on K02 and C010 before shipping.",
 "verdict_reasoning_summary": "Gates pass numerically (no critical, precision 0.9796>=0.95, must_recall 0.9583>=0.9, redundancy 0.102<=0.15); weighted_score 0.75476; Borderline due to Partial Must-have K02 and Minor partial C010."
}
```
