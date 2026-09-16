# Judge trace (scripted pipeline, opencode-go/deepseek-v4.1-flash)

## Judge F (faithfulness), opencode-go/deepseek-v4.1-flash

```json
{
 "judge": "faithfulness",
 "judge_version": "1.0.0",
 "model": "opencode-go/deepseek-v4.1-flash (opencode) scripted pipeline 2026-09-15",
 "source_id": "02_case_for_transparent_government",
 "claims": [
  {
   "claim_id": "C001",
   "loglog_ids": [
    "0"
   ],
   "claim_text": "Citizens are governments' CEO-principals, so every decision should be fully documented and traceable, with objections answered and precedents proving feasibility.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "None",
   "evidence_quote": "every government decision should be fully documented and publicly available ... You are the principal ... Pieces of this system already exist",
   "reasoning": "Summary tracks the thesis, principal-agent framing, and the objections and precedents sections of the source."
  },
  {
   "claim_id": "C002",
   "loglog_ids": [
    "1"
   ],
   "claim_text": "A manager hiding a million-dollar decision would be fired, yet governments do the same.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "None",
   "evidence_quote": "You'd fire them. ... That's how your government operates.",
   "reasoning": "Source states the owner would fire the manager and later says government operates the same way."
  },
  {
   "claim_id": "C003",
   "loglog_ids": [
    "1.1"
   ],
   "claim_text": "Manager refused to explain a million-dollar decision, citing lost leverage.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "None",
   "evidence_quote": "If you know how I make these decisions, I lose my leverage.",
   "reasoning": "Direct paraphrase of the manager's quoted refusal about the million-dollar budget decision."
  },
  {
   "claim_id": "C004",
   "loglog_ids": [
    "1.2"
   ],
   "claim_text": "An owner would sue, force disclosure, and fire that manager.",
   "claim_type": "claim",
   "verdict": "Supported",
   "severity": "None",
   "evidence_quote": "You'd take them to court. You'd force disclosure. You'd fire them.",
   "reasoning": "Matches the source's three listed responses exactly."
  },
  {
   "claim_id": "C005",
   "loglog_ids": [
    "1.3"
   ],
   "claim_text": "Governments refuse with classified, security, operations, and speed excuses.",
   "claim_type": "claim",
   "verdict": "Supported",
   "severity": "None",
   "evidence_quote": "you're told it's classified. It's a matter of national security. It would compromise ongoing operations. It would slow things down.",
   "reasoning": "All four cited excuses map directly to the source's listed justifications."
  },
  {
   "claim_id": "C006",
   "loglog_ids": [
    "2"
   ],
   "claim_text": "Every government decision should be fully documented and publicly available.",
   "claim_type": "recommendation",
   "verdict": "Supported",
   "severity": "None",
   "evidence_quote": "every government decision should be fully documented and publicly available",
   "reasoning": "Verbatim restatement of the source's central proposition."
  },
  {
   "claim_id": "C007",
   "loglog_ids": [
    "2.1"
   ],
   "claim_text": "Document data used, considerations made, and who was involved.",
   "claim_type": "recommendation",
   "verdict": "Supported",
   "severity": "None",
   "evidence_quote": "What data was used ... What considerations were made ... Who was involved",
   "reasoning": "First three items of the source's chain list, preserved."
  },
  {
   "claim_id": "C008",
   "loglog_ids": [
    "2.2"
   ],
   "claim_text": "Document alternatives considered, arguments for and against, implementation steps.",
   "claim_type": "recommendation",
   "verdict": "Supported",
   "severity": "None",
   "evidence_quote": "What alternatives were considered ... arguments for and against ... How it will be implemented",
   "reasoning": "Maps to the middle items of the source's documentation chain list."
  },
  {
   "claim_id": "C009",
   "loglog_ids": [
    "2.3"
   ],
   "claim_text": "Document evaluation, course-correction plans, and reconsideration terms.",
   "claim_type": "recommendation",
   "verdict": "Supported",
   "severity": "None",
   "evidence_quote": "How it will be evaluated ... course-correction plans ... When and how it will be reconsidered, and what it takes to change it",
   "reasoning": "Covers the final items of the source's documentation chain list."
  },
  {
   "claim_id": "C010",
   "loglog_ids": [
    "2.4"
   ],
   "claim_text": "Competent boards and CEOs already demand this basic accountability.",
   "claim_type": "claim",
   "verdict": "Supported",
   "severity": "None",
   "evidence_quote": "This is what any competent board of directors expects ... It's what any CEO expects ... It's basic accountability.",
   "reasoning": "Aligns with the source's board, CEO, and basic accountability statements."
  },
  {
   "claim_id": "C011",
   "loglog_ids": [
    "2.5"
   ],
   "claim_text": "It sounds radical only because the opposite was normalized.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "None",
   "evidence_quote": "The only thing that makes it sound radical is that we've normalized the opposite.",
   "reasoning": "Near-verbatim, with the restrictive 'only' preserved as in the source."
  },
  {
   "claim_id": "C012",
   "loglog_ids": [
    "3"
   ],
   "claim_text": "In democracy citizens are principals; officials are their employee-agents.",
   "claim_type": "claim",
   "verdict": "Supported",
   "severity": "None",
   "evidence_quote": "You are the principal in a principal-agent relationship ... is an agent working on your behalf ... They are your employees.",
   "reasoning": "Faithfully captures the source's principal-agent and employees framing."
  },
  {
   "claim_id": "C013",
   "loglog_ids": [
    "3.1"
   ],
   "claim_text": "Every servant from licensing clerk to president works for you.",
   "claim_type": "claim",
   "verdict": "Supported",
   "severity": "None",
   "evidence_quote": "Every public servant, from the clerk at your local licensing office to the president, is an agent working on your behalf.",
   "reasoning": "Same endpoints and scope as the source span."
  },
  {
   "claim_id": "C014",
   "loglog_ids": [
    "3.2"
   ],
   "claim_text": "CEOs need not read everything, but reviewability shapes behavior.",
   "claim_type": "claim",
   "verdict": "Supported",
   "severity": "None",
   "evidence_quote": "The CEO doesn't read every email. But they *could*. And that knowledge - that anything could be reviewed at any time - shapes behavior.",
   "reasoning": "Preserves both the non-consumption point and the behavioral effect of reviewability."
  },
  {
   "claim_id": "C015",
   "loglog_ids": [
    "3.3"
   ],
   "claim_text": "A company letting managers classify emails would go bankrupt within a year.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "None",
   "evidence_quote": "That company would be bankrupt within a year, eaten alive by internal corruption and incompetence",
   "reasoning": "Timeline and outcome match the source's hypothetical exactly."
  },
  {
   "claim_id": "C016",
   "loglog_ids": [
    "3.4"
   ],
   "claim_text": "Availability matters, not consumption: trace decisions affecting your life.",
   "claim_type": "nuance",
   "verdict": "Supported",
   "severity": "None",
   "evidence_quote": "The distinction between \"availability\" and \"consumption\" is crucial ... if a decision affects your community, your livelihood, your children's future - you *can* trace it back.",
   "reasoning": "Reflects the source's availability-versus-consumption distinction and traceability point."
  },
  {
   "claim_id": "C017",
   "loglog_ids": [
    "4"
   ],
   "claim_text": "Transparency flows from government to citizens, never the reverse.",
   "claim_type": "definition",
   "verdict": "Supported",
   "severity": "None",
   "evidence_quote": "the government's decisions, data, and processes flow *to* citizens. Not the other way around.",
   "reasoning": "One-directional claim matches the source's directional definition and negation."
  },
  {
   "claim_id": "C018",
   "loglog_ids": [
    "4.1"
   ],
   "claim_text": "Decisions visible, processes traceable, officials accountable to citizens.",
   "claim_type": "definition",
   "verdict": "Supported",
   "severity": "None",
   "evidence_quote": "Government decisions being visible to citizens. Government processes being traceable by citizens. Government officials being accountable to citizens.",
   "reasoning": "Direct restatement of the source's 'This is about' list."
  },
  {
   "claim_id": "C019",
   "loglog_ids": [
    "4.2"
   ],
   "claim_text": "Not tax returns, medical records, or citizens surveilling each other.",
   "claim_type": "definition",
   "verdict": "Supported",
   "severity": "None",
   "evidence_quote": "This is NOT about: Your tax returns ... Your medical records being public. Citizens surveilling each other.",
   "reasoning": "Negated exclusions preserved exactly from the source's 'This is NOT about' list."
  },
  {
   "claim_id": "C020",
   "loglog_ids": [
    "4.3"
   ],
   "claim_text": "CEOs see work product, not employees' medical records.",
   "claim_type": "definition",
   "verdict": "Supported",
   "severity": "None",
   "evidence_quote": "The CEO sees employee work product. The CEO does not publish employees' medical records to angry customers.",
   "reasoning": "Preserves the work-product versus medical-records contrast and the negation."
  },
  {
   "claim_id": "C021",
   "loglog_ids": [
    "4.4"
   ],
   "claim_text": "Publish $X/$Y/$Z/$W spending, not John Smith's $47,000 taxes.",
   "claim_type": "example",
   "verdict": "Supported",
   "severity": "None",
   "evidence_quote": "spent it as follows: $Y on healthcare, $Z on defense, $W on infrastructure ... It does *not* mean: \"John Smith paid $47,000 in taxes last year.\"",
   "reasoning": "Example structure and the $47,000 figure match the source exactly."
  },
  {
   "claim_id": "C022",
   "loglog_ids": [
    "4.5"
   ],
   "claim_text": "Aggregation, anonymization, and differential privacy make separation technically straightforward.",
   "claim_type": "claim",
   "verdict": "Supported",
   "severity": "None",
   "evidence_quote": "Privacy-preserving approaches - aggregate data, anonymization, differential privacy - make this technically straightforward.",
   "reasoning": "All three named techniques and the 'straightforward' qualifier match the source."
  },
  {
   "claim_id": "C023",
   "loglog_ids": [
    "5"
   ],
   "claim_text": "Pieces of this system already exist and prove it works.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Pieces of this system already exist around the world... several have gone far enough to prove it works.",
   "reasoning": "SOURCE asserts existing pieces and that several cases prove it works; identical meaning."
  },
  {
   "claim_id": "C024",
   "loglog_ids": [
    "5.1"
   ],
   "claim_text": "No country nears complete transparency, but several prove feasibility.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "No country has achieved anything close to complete transparency, but several have gone far enough to prove it works.",
   "reasoning": "Direct paraphrase preserving the concession and the feasibility claim."
  },
  {
   "claim_id": "C025",
   "loglog_ids": [
    "5.2"
   ],
   "claim_text": "Sweden's 260-year openness shows transparency endures without collapse.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Two hundred and sixty years later, Sweden still operates under this principle... The country has not collapsed.",
   "reasoning": "260 years, endurance, and non-collapse are all stated in SOURCE."
  },
  {
   "claim_id": "C026",
   "loglog_ids": [
    "5.2.1"
   ],
   "claim_text": "In 1766 Sweden passed the world's first freedom-of-information law.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "In 1766, Sweden passed the Freedom of the Press Act - the world's first freedom of information law.",
   "reasoning": "Date and superlative match SOURCE exactly."
  },
  {
   "claim_id": "C027",
   "loglog_ids": [
    "5.2.2"
   ],
   "claim_text": "It abolished censorship and is now constitutional.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "It abolished censorship... It's now part of the Swedish constitution.",
   "reasoning": "Both facts appear verbatim in SOURCE."
  },
  {
   "claim_id": "C028",
   "loglog_ids": [
    "5.2.3"
   ],
   "claim_text": "Finnish-Swedish priest-politician Chydenius drove Hats-versus-Caps explicitly anti-corruption law.",
   "claim_type": "name_or_entity",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Anders Chydenius, a Finnish-Swedish priest and politician, drove the legislation through parliament. The motivation was explicitly anti-corruption.",
   "reasoning": "Name, roles, driving role, and anti-corruption motive all match; Hats/Caps context is adjacent."
  },
  {
   "claim_id": "C029",
   "loglog_ids": [
    "5.2.4"
   ],
   "claim_text": "Offentlighetsprincipen keeps documents public by default 260 years on.",
   "claim_type": "definition",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Two hundred and sixty years later, Sweden still operates under this principle. It's called offentlighetsprincipen... Government documents are public by default.",
   "reasoning": "Term, default-public rule, and 260-year persistence all stated."
  },
  {
   "claim_id": "C030",
   "loglog_ids": [
    "5.2.5"
   ],
   "claim_text": "Nordics consistently rank among least corrupt, most effective democracies.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Nordic countries consistently rank among the least corrupt and most effective democracies in the world.",
   "reasoning": "Near-verbatim restatement."
  },
  {
   "claim_id": "C031",
   "loglog_ids": [
    "5.3"
   ],
   "claim_text": "Seoul's 1999 OPEN system made bribery-prone permitting visible.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "In 1999, Seoul launched the OPEN system... shows citizens exactly who made what decision.",
   "reasoning": "Year and the visibility of corruption-prone tasks match."
  },
  {
   "claim_id": "C032",
   "loglog_ids": [
    "5.3.1"
   ],
   "claim_text": "OPEN tracks 70 corruption-prone tasks, including construction, environmental, and urban planning permits, in real time.",
   "claim_type": "number_or_date",
   "verdict": "Partially supported",
   "severity": "Minor",
   "evidence_quote": "tracks 70 municipal tasks most prone to corruption - construction permits, environmental regulation, urban planning - and shows citizens... in real time.",
   "reasoning": "Number 70 is correct, but SOURCE lists environmental regulation and urban planning, not permits, and ties real time to showing citizens."
  },
  {
   "claim_id": "C033",
   "loglog_ids": [
    "5.3.2"
   ],
   "claim_text": "Citizens see exactly who decided what at each process point.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "shows citizens exactly who made what decision, at which point in the process, in real time.",
   "reasoning": "Direct restatement of SOURCE."
  },
  {
   "claim_id": "C034",
   "loglog_ids": [
    "5.3.3"
   ],
   "claim_text": "Previously invisible processing let officials demand speed-up bribes unprovably.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "This opacity enabled bribery: officials could demand payments to \"move things along\" and nobody could prove it.",
   "reasoning": "Opacity-to-bribery causal link and unprovability all stated."
  },
  {
   "claim_id": "C035",
   "loglog_ids": [
    "5.3.4"
   ],
   "claim_text": "Visibility eliminated that bribery leverage entirely.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Making the process visible eliminated that leverage entirely.",
   "reasoning": "Verbatim in meaning."
  },
  {
   "claim_id": "C036",
   "loglog_ids": [
    "5.3.5"
   ],
   "claim_text": "Corruption decreases as e-participation increases; UN, OECD, World Bank recognized it.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "\"corruption decreases as e-participation increases.\" The system was recognized by the UN, OECD, and World Bank.",
   "reasoning": "Quote and the three recognizing bodies match SOURCE."
  },
  {
   "claim_id": "C037",
   "loglog_ids": [
    "5.4"
   ],
   "claim_text": "Estonia's 2001 X-Road proves transparency infrastructure scales.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "### Estonia: The Infrastructure Proof (2001)... If your objection is \"this can't scale,\" look at Estonia's X-Road.",
   "reasoning": "Year and scale-proof framing both supported."
  },
  {
   "claim_id": "C038",
   "loglog_ids": [
    "5.4.1"
   ],
   "claim_text": "X-Road links 929+ institutions, 1,887 systems, 3,000+ services, timestamped, signed, logged.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "connecting 929+ institutions, 1,887 information systems, and 3,000+ digital services. Every transaction is timestamped and cryptographically signed. All data access is logged.",
   "reasoning": "All three figures and the three properties match SOURCE."
  },
  {
   "claim_id": "C039",
   "loglog_ids": [
    "5.4.2"
   ],
   "claim_text": "Citizens can see who accessed their data and why.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Citizens can see who accessed their data and why.",
   "reasoning": "Verbatim."
  },
  {
   "claim_id": "C040",
   "loglog_ids": [
    "5.4.3"
   ],
   "claim_text": "Estonia ranks 2nd on the UN E-Government Development Index.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Estonia now ranks 2nd in the UN E-Government Development Index.",
   "reasoning": "Rank and index match."
  },
  {
   "claim_id": "C041",
   "loglog_ids": [
    "5.4.4"
   ],
   "claim_text": "No major breaches in over 20 years despite constant cyber attacks.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "The system has had no major security breaches in over 20 years, despite constant cyber attacks.",
   "reasoning": "Negation, duration, and qualifier preserved."
  },
  {
   "claim_id": "C042",
   "loglog_ids": [
    "5.4.5"
   ],
   "claim_text": "X-Road is MIT-licensed open source, deployed in 20+ countries.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "It's open source (MIT license) and deployed in 20+ countries.",
   "reasoning": "License and deployment count match."
  },
  {
   "claim_id": "C043",
   "loglog_ids": [
    "5.4.6"
   ],
   "claim_text": "X-Road proves every-email-available infrastructure is technically feasible.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "X-Road proves the \"every email available up the chain\" infrastructure is technically feasible.",
   "reasoning": "Identical claim in SOURCE."
  },
  {
   "claim_id": "C044",
   "loglog_ids": [
    "5.4.7"
   ],
   "claim_text": "The technology is feasible; the bottleneck is will.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "The technology is not the bottleneck. The will is.",
   "reasoning": "Meaning preserved."
  },
  {
   "claim_id": "C045",
   "loglog_ids": [
    "5.5"
   ],
   "claim_text": "Brazil's 2004 Transparency Portal follows all federal money.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "### Brazil: Following the Money (2004)... publishes all federal spending.",
   "reasoning": "Year heading and all-federal-spending scope match."
  },
  {
   "claim_id": "C046",
   "loglog_ids": [
    "5.5.1"
   ],
   "claim_text": "It publishes contracts, transfers, salaries, travel, and credit-card transactions.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "contracts, transfers, salaries, travel expenses, and government credit card transactions.",
   "reasoning": "All five categories match SOURCE."
  },
  {
   "claim_id": "C047",
   "loglog_ids": [
    "5.5.2"
   ],
   "claim_text": "The portal receives over 20 million accesses per year.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "It receives over 20 million accesses per year.",
   "reasoning": "Verbatim figure."
  },
  {
   "claim_id": "C048",
   "loglog_ids": [
    "5.5.3"
   ],
   "claim_text": "Transparency Card sent 20+ million notifications via 430,000+ active cards.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "over 430,000 active cards, 20+ million notifications sent.",
   "reasoning": "Both counts match."
  },
  {
   "claim_id": "C049",
   "loglog_ids": [
    "5.5.4"
   ],
   "claim_text": "Journalists uncovered 60GB of hidden pension payments spanning 27 years.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "they uncovered 60GB of hidden pension payment data going back 27 years.",
   "reasoning": "Amount and span match."
  },
  {
   "claim_id": "C050",
   "loglog_ids": [
    "5.5.5"
   ],
   "claim_text": "Give citizens CEO tools and they find the fraud.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "This is what happens when you give citizens the tools to be CEOs: they find the fraud.",
   "reasoning": "Restatement preserving meaning."
  },
  {
   "claim_id": "C051",
   "loglog_ids": [
    "5.6"
   ],
   "claim_text": "New Zealand publishes cabinet papers by default since 2019.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Since 2019, New Zealand has proactively published all Cabinet papers and minutes online.",
   "reasoning": "Year, actor, and default publishing match."
  },
  {
   "claim_id": "C052",
   "loglog_ids": [
    "5.6.1"
   ],
   "claim_text": "All papers and minutes appear online within 30 business days.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "all Cabinet papers and minutes online within 30 business days of decisions being made.",
   "reasoning": "Window and scope match."
  },
  {
   "claim_id": "C053",
   "loglog_ids": [
    "5.6.2"
   ],
   "claim_text": "Cabinet deliberations are typically the world's most protected government information.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "cabinet deliberations are typically the most protected category of government information anywhere in the world.",
   "reasoning": "Hedge 'typically' and superlative preserved."
  },
  {
   "claim_id": "C054",
   "loglog_ids": [
    "5.6.3"
   ],
   "claim_text": "Government has not halted; ministers still deliberate; citizens see why.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "The government has not ground to a halt. Ministers have not stopped deliberating. What has changed is that citizens can see why.",
   "reasoning": "All three negations and the affirmative claim preserved."
  },
  {
   "claim_id": "C055",
   "loglog_ids": [
    "5.7"
   ],
   "claim_text": "Taiwan's vTaiwan crowdsources laws through consensus-finding deliberation.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Taiwan's vTaiwan platform uses Pol.is to let citizens participate in policy deliberation... surfaces statements that find cross-group consensus.",
   "reasoning": "Actor, method, and consensus mechanism match."
  },
  {
   "claim_id": "C056",
   "loglog_ids": [
    "5.7.1"
   ],
   "claim_text": "Pol.is takes agree-disagree votes with no replies, surfacing cross-group consensus.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "vote agree or disagree (no replies allowed - this prevents flame wars), and an algorithm surfaces statements that find cross-group consensus.",
   "reasoning": "Voting mode, no-replies rule, and consensus surfacing all present."
  },
  {
   "claim_id": "C057",
   "loglog_ids": [
    "5.7.2"
   ],
   "claim_text": "By 2018, 26 issues processed; 80% led to government action.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "By 2018, 26 issues had been processed, and 80% led to government action.",
   "reasoning": "Year, count, and percentage match exactly."
  },
  {
   "claim_id": "C058",
   "loglog_ids": [
    "5.7.3"
   ],
   "claim_text": "Participation is downstream of transparency, not core transparency itself.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "This isn't core transparency - it's what becomes possible downstream of transparency.",
   "reasoning": "Negation and downstream framing preserved."
  },
  {
   "claim_id": "C059",
   "loglog_ids": [
    "6"
   ],
   "claim_text": "Secret programs recur as illegal; secret oversight reliably fails to catch them.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "a recurring pattern in which government programs, shielded by secrecy, are later revealed to be illegal or built on lies... secret oversight reliably fails to prevent illegal secret programs",
   "reasoning": "Source asserts the recurring illegality pattern and reliable oversight failure. Dropped 'or built on lies' is harmless compression."
  },
  {
   "claim_id": "C060",
   "loglog_ids": [
    "6.1"
   ],
   "claim_text": "In 1971 Pentagon Papers showed government knew Vietnam was unwinnable while publicly claiming progress.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "In 1971, the Pentagon Papers revealed that the US government knew the Vietnam War was unwinnable while publicly claiming progress.",
   "reasoning": "Loglog restates the source sentence with year, actor, and claim intact."
  },
  {
   "claim_id": "C061",
   "loglog_ids": [
    "6.2"
   ],
   "claim_text": "Media, Pennsylvania break-in exposed COINTELPRO's illegal surveillance and disruption.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "activists broke into an FBI office in Media, Pennsylvania, and exposed COINTELPRO - a program of illegal surveillance, infiltration, and disruption",
   "reasoning": "Location, target, and program attributes match the source exactly."
  },
  {
   "claim_id": "C062",
   "loglog_ids": [
    "6.3"
   ],
   "claim_text": "COINTELPRO targeted civil rights leaders and political dissidents.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "targeting civil rights leaders and political dissidents",
   "reasoning": "Direct restatement of the source's target list."
  },
  {
   "claim_id": "C063",
   "loglog_ids": [
    "6.4"
   ],
   "claim_text": "In 2013 Snowden revealed bulk metadata collection from millions of Americans, PRISM, and leader surveillance.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "In 2013, Edward Snowden leaked classified documents revealing the NSA was bulk-collecting phone metadata from millions of Americans... through PRISM, and surveilling foreign leaders",
   "reasoning": "Year, actor, bulk collection, PRISM, and foreign-leader surveillance match the source."
  },
  {
   "claim_id": "C064",
   "loglog_ids": [
    "6.5"
   ],
   "claim_text": "Each disclosure was predicted catastrophic yet revealed illegality, unconstitutionality, or deliberate deception.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "In each case, the government predicted catastrophe from disclosure. In each case, the programs turned out to be illegal, unconstitutional, or based on deliberate deception",
   "reasoning": "The paired source sentences directly assert both the catastrophe prediction and the revealed outcomes."
  },
  {
   "claim_id": "C065",
   "loglog_ids": [
    "6.6"
   ],
   "claim_text": "In September 2020 the Ninth Circuit ruled bulk collection illegal, possibly unconstitutional.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "In September 2020, the US Ninth Circuit Court of Appeals ruled that the NSA's bulk phone record collection was illegal and possibly unconstitutional.",
   "reasoning": "Court, date, and both qualifiers match the source."
  },
  {
   "claim_id": "C066",
   "loglog_ids": [
    "6.7"
   ],
   "claim_text": "The court required FISA relevance to a particular authorized investigation.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "the government failed to satisfy FISA's requirement to show \"relevance to a particular authorized investigation.\"",
   "reasoning": "Quoted FISA requirement is reproduced accurately."
  },
  {
   "claim_id": "C067",
   "loglog_ids": [
    "6.8"
   ],
   "claim_text": "Stone found no evidence bulk collection stopped any terror attacks.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Geoffrey R. Stone, found \"no evidence that the bulk collection of phone data had stopped any terror attacks.\"",
   "reasoning": "The finding and attribution to Stone match the source quote."
  },
  {
   "claim_id": "C068",
   "loglog_ids": [
    "6.9"
   ],
   "claim_text": "The NSA abandoned the program in 2018: it no longer made sense.",
   "claim_type": "number_or_date",
   "verdict": "Partially supported",
   "severity": "Minor",
   "evidence_quote": "The NSA itself reportedly abandoned the program in 2018, telling the White House it \"no longer made sense.\"",
   "reasoning": "Node states as flat fact what source hedges with 'reportedly', dropping the attribution qualifier."
  },
  {
   "claim_id": "C069",
   "loglog_ids": [
    "6.10"
   ],
   "claim_text": "FISA courts, committees, and inspectors general failed inside the secrecy structure.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "The FISA court, congressional intelligence committees, and inspectors general all existed. They failed because they operated inside the secrecy structure",
   "reasoning": "All three oversight bodies and the failure cause match the source."
  },
  {
   "claim_id": "C070",
   "loglog_ids": [
    "6.11"
   ],
   "claim_text": "Secret oversight can be captured, co-opted, or worn down institutionally.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Oversight that is itself secret is oversight that can be captured, co-opted, or simply worn down by institutional pressure.",
   "reasoning": "Node reproduces the source's three mechanisms and the 'can' hedge."
  },
  {
   "claim_id": "C071",
   "loglog_ids": [
    "6.12"
   ],
   "claim_text": "The 2015 USA FREEDOM Act first reined in NSA spying in over 30 years.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "The USA FREEDOM Act (2015) became the first legislation to rein in NSA spying in over 30 years.",
   "reasoning": "Year, statute, and the 30-year first characterize the source verbatim."
  },
  {
   "claim_id": "C072",
   "loglog_ids": [
    "6.13"
   ],
   "claim_text": "It ended bulk metadata collection and required releasing significant FISC opinions.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "It ended bulk collection of phone metadata and required the Foreign Intelligence Surveillance Court to release significant opinions.",
   "reasoning": "Both effects match the source; FISC is the source's named court."
  },
  {
   "claim_id": "C073",
   "loglog_ids": [
    "6.14"
   ],
   "claim_text": "The tech sector adopted transparency reporting on data requests.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "The tech sector adopted transparency reporting on government data requests.",
   "reasoning": "Direct restatement of the source claim."
  },
  {
   "claim_id": "C074",
   "loglog_ids": [
    "6.15"
   ],
   "claim_text": "HTTPS became default on most websites.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "HTTPS encryption became the default on most websites.",
   "reasoning": "Verbatim match including the 'most websites' scope."
  },
  {
   "claim_id": "C075",
   "loglog_ids": [
    "6.16"
   ],
   "claim_text": "The EU's GDPR was accelerated by the revelations.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "The EU's GDPR was accelerated by the revelations.",
   "reasoning": "Direct restatement of the causal claim."
  },
  {
   "claim_id": "C076",
   "loglog_ids": [
    "6.17"
   ],
   "claim_text": "Operational harm is genuinely uncertain; illegality is not.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Whether these disclosures caused operational harm is genuinely uncertain... But the legality question is not uncertain. The programs were illegal.",
   "reasoning": "Node preserves both the uncertainty and its contrast with settled illegality."
  },
  {
   "claim_id": "C077",
   "loglog_ids": [
    "6.18"
   ],
   "claim_text": "Snowden is the symptom of absent designed-in transparency, not the solution.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Snowden is not the solution. Snowden is the symptom of a system where the only alternative to permanent secrecy is uncontrolled disclosure.",
   "reasoning": "Node keeps both negations and maps 'absence of a model' to designed-in transparency."
  },
  {
   "claim_id": "C078",
   "loglog_ids": [
    "6.19"
   ],
   "claim_text": "Designed-in traceability would surface illegality early without bulk-leak damage.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Designed-in transparency - where citizens can trace decisions by default - would have made the illegal programs visible before they scaled, without the collateral damage of a bulk leak.",
   "reasoning": "Early visibility and avoided bulk-leak damage match the source claim closely."
  },
  {
   "claim_id": "C079",
   "loglog_ids": [
    "7"
   ],
   "claim_text": "Ten objections follow, some power-protecting, some genuinely concerned; each gets honest engagement.",
   "claim_type": "meta",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Some come from officials protecting their power. But some come from citizens with genuine concerns. These deserve honest engagement.",
   "reasoning": "Source names both objection sources and promises honest engagement; ten subsequent headings enumerate ten objections."
  },
  {
   "claim_id": "C080",
   "loglog_ids": [
    "7.1"
   ],
   "claim_text": "Privacy objection: transparency will violate my privacy.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "### \"My Privacy Will Be Violated\"",
   "reasoning": "Matches the source heading naming the privacy objection."
  },
  {
   "claim_id": "C081",
   "loglog_ids": [
    "7.1.1"
   ],
   "claim_text": "2019 Pew: 66% fear collection, 64% fear use, 6% very confident.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "66% of Americans are concerned about government data collection, and 64% are concerned about how the government uses their data. Only 6% are \"very confident\"",
   "reasoning": "All three percentages and the 2019 Pew attribution match the source exactly."
  },
  {
   "claim_id": "C082",
   "loglog_ids": [
    "7.1.2"
   ],
   "claim_text": "A 2000 ABC poll: 86% said agencies should not publish such records online.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "2000 ABC News poll ... 86% said government agencies should *not* make public records ... available online.",
   "reasoning": "Date, percentage, and the negation about publishing records online all match."
  },
  {
   "claim_id": "C083",
   "loglog_ids": [
    "7.1.3"
   ],
   "claim_text": "Polls fear citizen data held by government, not visible government decisions.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "fear about *citizen data* held by government. Not fear about *government decisions* being visible to citizens.",
   "reasoning": "Direct restatement of the source's distinction, including the negation."
  },
  {
   "claim_id": "C084",
   "loglog_ids": [
    "7.1.4"
   ],
   "claim_text": "Quarterly-report review differs from publishing employee health records.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "The CEO reviewing quarterly reports is not the same as the CEO publishing employee health records.",
   "reasoning": "Paraphrase preserves the source's comparison and negation."
  },
  {
   "claim_id": "C085",
   "loglog_ids": [
    "7.1.5"
   ],
   "claim_text": "$50 million infrastructure-allocation transparency needs no neighbor's personal data.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "allocate $50 million in infrastructure spending. It does not mean: \"Here is the personal information of every citizen...\"",
   "reasoning": "Amount and the contrast with personal data match the source."
  },
  {
   "claim_id": "C086",
   "loglog_ids": [
    "7.1.6"
   ],
   "claim_text": "Bundled record systems should be separated, not kept wholly secret.",
   "claim_type": "recommendation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "the solution is to separate them, not to keep everything secret.",
   "reasoning": "Direct restatement preserving the separation recommendation and negation."
  },
  {
   "claim_id": "C087",
   "loglog_ids": [
    "7.2"
   ],
   "claim_text": "Objection: if every action is public, deliberation dies and processes paralyze.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "if every action is public, deliberation becomes impossible. Officials will be afraid to propose ideas. Processes will be paralyzed.",
   "reasoning": "Tracks the source's stated fear about deliberation and paralysis."
  },
  {
   "claim_id": "C088",
   "loglog_ids": [
    "7.2.1"
   ],
   "claim_text": "Cambridge found EU transparency-deliberation tension; IMF called government a friction-forcing fortress.",
   "claim_type": "name_or_entity",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "A Cambridge study ... found tension between transparent deliberation and efficient decision-making. An IMF analysis ... \"is not a sports car - it's a fortress\"",
   "reasoning": "Both attributions and characterizations match the source."
  },
  {
   "claim_id": "C089",
   "loglog_ids": [
    "7.2.2"
   ],
   "claim_text": "IMF: friction forces accountability and catches errors before harm.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "\"friction forces accountability\" and \"catches errors before they cause harm.\"",
   "reasoning": "Both quoted phrases reproduce the source verbatim."
  },
  {
   "claim_id": "C090",
   "loglog_ids": [
    "7.2.3"
   ],
   "claim_text": "Robodebt: 470,000 incorrect notices and a $1.8 billion settlement.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "470,000 incorrect debt notices and a $1.8 billion settlement.",
   "reasoning": "Numbers and entity match; dropping the word debt is harmless compression."
  },
  {
   "claim_id": "C091",
   "loglog_ids": [
    "7.2.4"
   ],
   "claim_text": "This confuses decision speed with decision documentation.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "this concern confuses two things: the speed of decision-making and the documentation of decision-making.",
   "reasoning": "Identical meaning to the source's distinction."
  },
  {
   "claim_id": "C092",
   "loglog_ids": [
    "7.2.5"
   ],
   "claim_text": "Document at current speed; fix burdensome systems, keep accountability.",
   "claim_type": "recommendation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "documenting what happens at the current speed ... If documentation is burdensome, you improve the documentation systems - you don't abandon accountability.",
   "reasoning": "Preserves both the documentation-at-current-speed point and the fix-systems recommendation."
  },
  {
   "claim_id": "C093",
   "loglog_ids": [
    "7.2.6"
   ],
   "claim_text": "CEOs demand documented work, not slower work.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "The CEO doesn't demand employees work slower. The CEO demands employees document their work.",
   "reasoning": "Direct restatement preserving the negation about speed."
  },
  {
   "claim_id": "C094",
   "loglog_ids": [
    "7.2.7"
   ],
   "claim_text": "New Zealand's 30-day cabinet papers halted nothing; reasoning stands verifiable.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "New Zealand publishes cabinet papers within 30 days. Their government hasn't ground to a halt ... citizens can verify whether the reasoning was sound.",
   "reasoning": "30-day figure and both consequences match this source passage."
  },
  {
   "claim_id": "C095",
   "loglog_ids": [
    "7.2.8"
   ],
   "claim_text": "Opacity makes decisions unaccountable random walks, not better ones.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "opacity doesn't make decisions *better* - it just makes them *unaccountable* ... Nobody notices the random walk",
   "reasoning": "Restates the source's contrast and random-walk image with the negation intact."
  },
  {
   "claim_id": "C096",
   "loglog_ids": [
    "7.2.9"
   ],
   "claim_text": "Documented consistency pressure prevents reversals and speeds decisions long-term.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Transparency creates pressure for logical consistency, which in the long run actually improves decision-making speed by preventing costly reversals",
   "reasoning": "Preserves the causal claim linking consistency pressure to fewer reversals and speed."
  },
  {
   "claim_id": "C097",
   "loglog_ids": [
    "7.3"
   ],
   "claim_text": "Objection: diplomacy requires secrecy.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "### \"Diplomacy Requires Secrecy\"",
   "reasoning": "Matches the source heading naming the diplomacy objection."
  },
  {
   "claim_id": "C098",
   "loglog_ids": [
    "7.3.1"
   ],
   "claim_text": "Conceded: the most legitimate concern, deserving nuance.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "This is the most legitimate concern, and it deserves nuance.",
   "reasoning": "Direct restatement of the concession."
  },
  {
   "claim_id": "C099",
   "loglog_ids": [
    "7.3.2"
   ],
   "claim_text": "JCPOA began in 2012 via Sullivan's secret Oman backchannel.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "negotiations began in 2012 with a secret backchannel. Jake Sullivan secretly traveled to Oman",
   "reasoning": "Year, name Jake Sullivan, and Oman backchannel all match."
  },
  {
   "claim_id": "C100",
   "loglog_ids": [
    "7.3.3"
   ],
   "claim_text": "Camp David 1978 and Cold War backchannels likewise needed private space.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "The Camp David Accords (1978) similarly required private space for compromise. Cold War backchannels",
   "reasoning": "1978 attribution and the private-space point match."
  },
  {
   "claim_id": "C101",
   "loglog_ids": [
    "7.3.4"
   ],
   "claim_text": "Democratic dilemma: secrecy enables flexibility, but barren without consent.",
   "claim_type": "definition",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "\"negotiations can be flexible and successful only if they are kept secret, but they will be barren without popular consent.\"",
   "reasoning": "Faithful compression of the quoted democratic dilemma."
  },
  {
   "claim_id": "C102",
   "loglog_ids": [
    "7.3.5"
   ],
   "claim_text": "CEOs allow confidential negotiation, then demand full disclosure afterward.",
   "claim_type": "recommendation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "A CEO may authorize a negotiation team to keep details confidential *during* the negotiation. But the CEO expects full disclosure once it concludes.",
   "reasoning": "Preserves both the during-negotiation confidentiality and post-conclusion disclosure."
  },
  {
   "claim_id": "C103",
   "loglog_ids": [
    "7.3.6"
   ],
   "claim_text": "Disclose afterward what was offered, conceded, why, and alternatives.",
   "claim_type": "recommendation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "what was offered, what was conceded, why, what alternatives were considered.",
   "reasoning": "Lists exactly the source's disclosure items."
  },
  {
   "claim_id": "C104",
   "loglog_ids": [
    "7.3.7"
   ],
   "claim_text": "Temporary secrecy during talks is acceptable; permanent secrecy is not.",
   "claim_type": "recommendation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "*Temporary operational secrecy during active negotiations* may be acceptable. *Permanent secrecy about what was decided and why* is not.",
   "reasoning": "Reproduces the source's acceptability distinction and negation."
  },
  {
   "claim_id": "C105",
   "loglog_ids": [
    "7.3.8"
   ],
   "claim_text": "Release full documentation 30-90 days after conclusion for evaluation.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Full documentation released after conclusion (e.g., 30-90 days) ... Citizens can evaluate whether negotiators served their interests",
   "reasoning": "30-90 day window and evaluation purpose match."
  },
  {
   "claim_id": "C106",
   "loglog_ids": [
    "7.3.9"
   ],
   "claim_text": "Foreign-refusal arguments let non-principals veto citizens' oversight.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "It makes citizens' oversight contingent on foreign governments' preferences. But foreign governments are not the principals here.",
   "reasoning": "Captures the source's point that foreign preferences would condition citizens' oversight."
  },
  {
   "claim_id": "C107",
   "loglog_ids": [
    "7.3.10"
   ],
   "claim_text": "Foreign governments are not the principals; citizens are.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "foreign governments are not the principals here. You are.",
   "reasoning": "Direct restatement preserving the negation."
  },
  {
   "claim_id": "C108",
   "loglog_ids": [
    "7.4"
   ],
   "claim_text": "Objection: special interests benefit more than ordinary citizens.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "### \"Special Interests Will Benefit More Than Ordinary Citizens\"",
   "reasoning": "Matches the source heading naming the special-interest objection."
  },
  {
   "claim_id": "C109",
   "loglog_ids": [
    "7.4.1"
   ],
   "claim_text": "Conceded: empirically grounded and worth taking seriously.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "This is an empirically grounded concern that you should take seriously.",
   "reasoning": "Direct restatement of the concession."
  },
  {
   "claim_id": "C110",
   "loglog_ids": [
    "7.4.2"
   ],
   "claim_text": "Harden and Kirkland studied all 50 legislatures over multiple decades.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "studied all 50 US state legislatures over multiple decades.",
   "reasoning": "Count and scope match exactly."
  },
  {
   "claim_id": "C111",
   "loglog_ids": [
    "7.4.3"
   ],
   "claim_text": "Notre Dame-Virginia scholars' Illusion of Accountability compares open versus closed meetings using surveys versus outcomes.",
   "claim_type": "name_or_entity",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Jeff Harden (University of Notre Dame) and Justin Kirkland (University of Virginia) ... *The Illusion of Accountability* ... compared states with open versus closed legislative meetings, using survey data on policy preferences versus actual policy outcomes.",
   "reasoning": "Affiliations, book title, and method all match the source."
  },
  {
   "claim_id": "C112",
   "loglog_ids": [
    "7.4.4"
   ],
   "claim_text": "More lobbyists register and donate, yet policy-opinion correlation stays same open or closed.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "more lobbying groups register ... Lobbyists donate more to incumbents. And public policy's correlation with public opinion is *the same* whether meetings are open or closed.",
   "reasoning": "All three findings match the source."
  },
  {
   "claim_id": "C113",
   "loglog_ids": [
    "7.4.5"
   ],
   "claim_text": "Harden: the laws improve representation for unrepresentative interest groups, not citizens.",
   "claim_type": "name_or_entity",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "\"The laws don't make citizen representation better, they make it better for interest groups, which aren't representative of the general public.\"",
   "reasoning": "Faithful to the quoted Harden statement and its negation."
  },
  {
   "claim_id": "C114",
   "loglog_ids": [
    "7.4.6"
   ],
   "claim_text": "Arnold (1990): open markups advantage organized interests over inattentive citizens.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Princeton's Douglas Arnold (1990) observed ... \"Open markup sessions often give organized interests a powerful advantage over inattentive citizens.\"",
   "reasoning": "Year, name, and quoted claim all match."
  },
  {
   "claim_id": "C115",
   "loglog_ids": [
    "7.4.7"
   ],
   "claim_text": "Ireland 2024: 569 participants; lobbying transparency did not raise trust.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "2024 survey experiment in Ireland ... with 569 participants found that citizens exposed to lobbying information don't develop more positive evaluations of trust",
   "reasoning": "Year, count, and the negative finding match."
  },
  {
   "claim_id": "C116",
   "loglog_ids": [
    "7.4.8"
   ],
   "claim_text": "Asymmetry is the problem: paid monitors versus busy citizens.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "the *asymmetry* is the problem. Lobbyists are paid to monitor government.",
   "reasoning": "Direct restatement of the source's asymmetry point."
  },
  {
   "claim_id": "C117",
   "loglog_ids": [
    "7.4.9"
   ],
   "claim_text": "Lobbyists wield staff, expertise, and capacity; citizens have jobs and families.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "They have professional staff, legal expertise, and organizational capacity. Citizens have jobs, families, and finite attention.",
   "reasoning": "Faithful list of the source's stated asymmetries."
  },
  {
   "claim_id": "C118",
   "loglog_ids": [
    "7.4.10"
   ],
   "claim_text": "Build citizen capacity: auditors, watchdogs, journalism, civic tech.",
   "claim_type": "recommendation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "hire auditors, create oversight committees ... fund watchdog organizations, support investigative journalism, build civic technology.",
   "reasoning": "Matches the source's capacity-building recommendations."
  },
  {
   "claim_id": "C119",
   "loglog_ids": [
    "7.4.11"
   ],
   "claim_text": "Brazil's Fiquem Sabendo files 2,000-3,000 FOI requests yearly for citizens.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Brazil's Fiquem Sabendo files 2,000-3,000 FOI requests per year on behalf of citizens.",
   "reasoning": "Name and request count match exactly."
  },
  {
   "claim_id": "C120",
   "loglog_ids": [
    "7.4.12"
   ],
   "claim_text": "A robust and competitive electoral environment is the real key.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "\"the real key to quality representation is a robust and competitive electoral environment.\"",
   "reasoning": "Direct quotation with correct attribution to Harden and Kirkland."
  },
  {
   "claim_id": "C121",
   "loglog_ids": [
    "7.4.13"
   ],
   "claim_text": "Opacity guarantees no accountability; transparency makes it possible.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Opacity *guarantees* no accountability. Transparency at least makes accountability *possible*.",
   "reasoning": "Reproduces the source's contrast and negation."
  },
  {
   "claim_id": "C122",
   "loglog_ids": [
    "7.4.14"
   ],
   "claim_text": "Build usage capacity rather than reducing information.",
   "claim_type": "recommendation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "The answer is to build capacity, not reduce information.",
   "reasoning": "Direct restatement preserving the not-reduce-information negation."
  },
  {
   "claim_id": "C123",
   "loglog_ids": [
    "7.5"
   ],
   "claim_text": "Objection: public officials will face harassment.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "### \"Public Officials Will Be Harassed\"",
   "reasoning": "Matches the source heading naming the harassment objection."
  },
  {
   "claim_id": "C124",
   "loglog_ids": [
    "7.5.1"
   ],
   "claim_text": "Conceded: real, documented, and growing.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "This concern is real, documented, and growing.",
   "reasoning": "Direct restatement of the concession."
  },
  {
   "claim_id": "C125",
   "loglog_ids": [
    "7.5.2"
   ],
   "claim_text": "Brennan surveyed 735 local election officials, February-March 2024, weighted by region and jurisdiction size, margin ±3%.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "surveyed 735 local election officials between February and March 2024 (weighted by region and jurisdiction size, margin of error ±3%)",
   "reasoning": "All figures and methodology details match the source."
  },
  {
   "claim_id": "C126",
   "loglog_ids": [
    "7.5.3"
   ],
   "claim_text": "38% threatened; over half fear for colleagues; over 1 in 4 fear assault.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "38% experienced threats ... More than half are concerned about the safety of colleagues ... More than 1 in 4 worry about being assaulted",
   "reasoning": "All three statistics match the source's survey list."
  },
  {
   "claim_id": "C127",
   "loglog_ids": [
    "7.5.4"
   ],
   "claim_text": "34% know someone who resigned, up from 22% in 2023.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "34% know someone who resigned due to safety concerns (up from 22% in 2023)",
   "reasoning": "Both percentages and the 2023 comparison match."
  },
  {
   "claim_id": "C128",
   "loglog_ids": [
    "7.5.5"
   ],
   "claim_text": "61% of the threatened were threatened in person or by phone.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "61% of those threatened received threats in person or by phone",
   "reasoning": "Percentage and channel detail match the source."
  },
  {
   "claim_id": "C129",
   "loglog_ids": [
    "7.5.6"
   ],
   "claim_text": "2024: doxxing and swatting evolved into sophisticated technology-enabled harassment tools.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "reported in 2024 that doxxing and swatting have \"evolved into sophisticated, technology-enabled tools of harassment,\"",
   "reasoning": "Year and quoted characterization match the NAAG report."
  },
  {
   "claim_id": "C130",
   "loglog_ids": [
    "7.5.7"
   ],
   "claim_text": "AI and automated scraping intensify scale, precision, and anonymity.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "AI and automated data scraping intensifying \"the scale, precision, and anonymity\" of attacks.",
   "reasoning": "Matches the source's quoted list and agents."
  },
  {
   "claim_id": "C131",
   "loglog_ids": [
    "7.5.8"
   ],
   "claim_text": "Since 2022, 22 states passed protections for election officials.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Since 2022, 22 states have passed protections for election officials.",
   "reasoning": "Year and state count match exactly."
  },
  {
   "claim_id": "C132",
   "loglog_ids": [
    "7.5.9"
   ],
   "claim_text": "Publish who decided what and why; protect addresses, families, schedules.",
   "claim_type": "recommendation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Transparency of decisions (who decided what, based on what reasoning) should be public. Personal information of officials (home addresses, family members, daily schedules) should be protected.",
   "reasoning": "Preserves both the public-decisions and protected-details distinction."
  },
  {
   "claim_id": "C133",
   "loglog_ids": [
    "7.5.10"
   ],
   "claim_text": "CEOs review work product, not employees' home addresses.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "The CEO does not publish employees' home addresses to angry customers. Accountability for work product is not the same as personal vulnerability.",
   "reasoning": "Faithful to the source's distinction and negation."
  },
  {
   "claim_id": "C134",
   "loglog_ids": [
    "7.5.11"
   ],
   "claim_text": "Current harassment feeds on opacity-bred fraud conspiracies.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "much of the *current* harassment stems from *lack* of transparency. Election officials are harassed because of conspiracy theories about fraud.",
   "reasoning": "Preserves the source's causal link between opacity and harassment."
  },
  {
   "claim_id": "C135",
   "loglog_ids": [
    "7.5.12"
   ],
   "claim_text": "Documented audits, custody chains, and counts would starve conspiracies.",
   "claim_type": "causal_link",
   "verdict": "Partially supported",
   "severity": "Minor",
   "evidence_quote": "the conspiracy theories would have less room to grow",
   "reasoning": "Source says conspiracies would have less room to grow; node strengthens to starve, an absolute elimination claim."
  },
  {
   "claim_id": "C136",
   "loglog_ids": [
    "7.5.13"
   ],
   "claim_text": "Protect individuals more while making processes more transparent.",
   "claim_type": "recommendation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "better protection for individuals, combined with *more* transparency about processes.",
   "reasoning": "Direct restatement of the source's dual recommendation."
  },
  {
   "claim_id": "C137",
   "loglog_ids": [
    "7.6"
   ],
   "claim_text": "Objection: national security forbids transparency.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "### \"National Security!\"",
   "reasoning": "Matches the source heading for the national security objection."
  },
  {
   "claim_id": "C138",
   "loglog_ids": [
    "7.6.1"
   ],
   "claim_text": "This objection is used most and scrutinized least.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "This is the objection that gets used most often and scrutinized least.",
   "reasoning": "Direct restatement of the source."
  },
  {
   "claim_id": "C139",
   "loglog_ids": [
    "7.6.2"
   ],
   "claim_text": "Chicago 2020-2022: roughly 60% call intelligence vital.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "surveyed Americans in 2020 and 2022 and found that roughly 60% agree the intelligence community \"plays a vital role\"",
   "reasoning": "Years, percentage, and attribution match."
  },
  {
   "claim_id": "C140",
   "loglog_ids": [
    "7.6.3"
   ],
   "claim_text": "A majority say it could share more without harming effectiveness.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "a majority also agreed the IC \"could share more information with the American people without compromising effectiveness.\"",
   "reasoning": "Faithful to the quoted survey result."
  },
  {
   "claim_id": "C141",
   "loglog_ids": [
    "7.6.4"
   ],
   "claim_text": "Civil-liberties threat perception rose from 12% in 2021 to 17% in 2022.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "rising (from 12% in 2021 to 17% in 2022)",
   "reasoning": "Both percentages and years match exactly."
  },
  {
   "claim_id": "C142",
   "loglog_ids": [
    "7.6.5"
   ],
   "claim_text": "Brennan: far too much is classified; secrecy undermines democratic self-government.",
   "claim_type": "name_or_entity",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "\"federal officials and outside experts agree that far too much information is classified.\" And: \"excessive secrecy ... undermines the basic functions of democratic self-government.\"",
   "reasoning": "Both quoted Brennan Center statements match."
  },
  {
   "claim_id": "C143",
   "loglog_ids": [
    "7.6.6"
   ],
   "claim_text": "SIPRI: military transparency builds inter-state trust and prevents waste.",
   "claim_type": "name_or_entity",
   "verdict": "Partially supported",
   "severity": "Minor",
   "evidence_quote": "\"transparency in military matters is generally considered essential for building trust between states\" and \"can help prevent wasteful spending.\"",
   "reasoning": "Node states absolutes; source hedges with generally considered, essential, and can help prevent."
  },
  {
   "claim_id": "C144",
   "loglog_ids": [
    "7.6.7"
   ],
   "claim_text": "Snowden proved catastrophe predictions wrong and programs illegal.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "The government predicted catastrophe. Independent research found minimal impact. The court found the programs *illegal*.",
   "reasoning": "Node summarizes the source's claim that predicted catastrophe did not materialize and programs were illegal."
  },
  {
   "claim_id": "C145",
   "loglog_ids": [
    "7.6.8"
   ],
   "claim_text": "Independent research found minimal impact; reforms improved civil liberties.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Independent research found minimal impact. ... The reforms improved civil liberties.",
   "reasoning": "Direct restatement of both source statements."
  },
  {
   "claim_id": "C146",
   "loglog_ids": [
    "7.6.9"
   ],
   "claim_text": "Flip the burden: transparent by default, secrecy needs proof.",
   "claim_type": "recommendation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "almost everything is transparent by default, and officials must prove their need for secrecy.",
   "reasoning": "Faithful to the source's proposed burden reversal."
  },
  {
   "claim_id": "C147",
   "loglog_ids": [
    "7.6.10"
   ],
   "claim_text": "Temporary classification fits active operations; strategy, doctrine, budgets, procurement, and rules stay open.",
   "claim_type": "recommendation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "The CEO may authorize temporary classification during an operation. ... Strategy, doctrine, budget, procurement, rules of engagement should always be transparent.",
   "reasoning": "Matches the temporary-classification exception and open-by-default list."
  },
  {
   "claim_id": "C148",
   "loglog_ids": [
    "7.6.11"
   ],
   "claim_text": "The label hides embarrassment, illegality, incompetence, and corruption.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "The \"national security\" label is overused to hide embarrassing decisions, illegal activities (as Snowden revealed), bureaucratic incompetence, and corruption.",
   "reasoning": "Faithful compression of the source's list."
  },
  {
   "claim_id": "C149",
   "loglog_ids": [
    "7.6.12"
   ],
   "claim_text": "Officials under scrutiny set secrecy criteria: a conflict of interest.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Currently, the officials whose decisions might be scrutinized. That's a conflict of interest.",
   "reasoning": "Direct restatement of the source's conflict-of-interest point."
  },
  {
   "claim_id": "C150",
   "loglog_ids": [
    "7.7"
   ],
   "claim_text": "Objection: populists will weaponize transparency.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "### \"Populists Will Weaponize Transparency\"",
   "reasoning": "Matches the source heading naming the populism objection."
  },
  {
   "claim_id": "C151",
   "loglog_ids": [
    "7.7.1"
   ],
   "claim_text": "Conceded: sophisticated and research-backed.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "This is a sophisticated concern backed by real research.",
   "reasoning": "Direct restatement of the concession."
  },
  {
   "claim_id": "C152",
   "loglog_ids": [
    "7.7.2"
   ],
   "claim_text": "Kyle-Gultchin studied 43 democracies, 1990-2018, Polity IV at least 6, leaders journal-screened.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "studying populist governments in 43 democratic countries between 1990 and 2018 (leaders classified through academic journal screening, countries coded as democratic using Polity IV score ≥6)",
   "reasoning": "All figures and methodological details match."
  },
  {
   "claim_id": "C153",
   "loglog_ids": [
    "7.7.3"
   ],
   "claim_text": "Populists are 4x likelier to damage institutions: 23% versus 6%.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Populist governments are 4x more likely to damage democratic institutions (23% vs 6% of non-populists)",
   "reasoning": "Multiplier and both percentages match."
  },
  {
   "claim_id": "C154",
   "loglog_ids": [
    "7.7.4"
   ],
   "claim_text": "Countries fall 5 places on corruption perceptions; top-half starters fall 11.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Countries fall an average of 5 places ... Countries starting in the top half fall an average of 11 places",
   "reasoning": "Both figures match the source."
  },
  {
   "claim_id": "C155",
   "loglog_ids": [
    "7.7.5"
   ],
   "claim_text": "Venezuela dropped 83 places under Chávez.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "(Venezuela dropped 83 under Chávez)",
   "reasoning": "Country, figure, and leader match exactly."
  },
  {
   "claim_id": "C156",
   "loglog_ids": [
    "7.7.6"
   ],
   "claim_text": "Over 50% amended or rewrote constitutions; populists rule 6.5 versus 3 years.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Over 50% of populist leaders amended or rewrote constitutions ... Populists hold office twice as long ... (6.5 vs 3 years)",
   "reasoning": "Both the 50% figure and the 6.5 vs 3 years match."
  },
  {
   "claim_id": "C157",
   "loglog_ids": [
    "7.7.7"
   ],
   "claim_text": "Stanford: visibility-driven re-election tempts short-term populist policies.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "\"when re-election hinges on immediate visibility rather than long-term strategy, leaders may opt for populist policies\"",
   "reasoning": "Faithful compression of the quoted Stanford argument."
  },
  {
   "claim_id": "C158",
   "loglog_ids": [
    "7.7.8"
   ],
   "claim_text": "Sweden Democrats repurposed FOI and alternative media against elites.",
   "claim_type": "name_or_entity",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "the Sweden Democrats ... have \"strategically repurposed\" transparency mechanisms, using freedom of information ... while leveraging alternative media",
   "reasoning": "Party, mechanism, and media all match."
  },
  {
   "claim_id": "C159",
   "loglog_ids": [
    "7.7.9"
   ],
   "claim_text": "They expose scandals to erode trust in traditional elites.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "using freedom of information to expose scandals and erode trust in traditional elites",
   "reasoning": "Direct restatement of the source phrase."
  },
  {
   "claim_id": "C160",
   "loglog_ids": [
    "7.7.10"
   ],
   "claim_text": "Causality is backwards: populists damage democracy by reducing transparency.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "the causal story is backwards. The research shows populists *damage* democracy - and they do so by *reducing* transparency, not increasing it.",
   "reasoning": "Preserves the causal reversal and the not-increasing negation."
  },
  {
   "claim_id": "C161",
   "loglog_ids": [
    "7.7.11"
   ],
   "claim_text": "Cherry-picking works only while the full record stays hidden.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "This works precisely because *not everything* is visible. In a fully transparent system, selective leaking loses its power.",
   "reasoning": "Faithful to the source's visibility-dependent explanation."
  },
  {
   "claim_id": "C162",
   "loglog_ids": [
    "7.7.12"
   ],
   "claim_text": "Electoral cycles cause short-termism with or without transparency.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "the \"short-term thinking\" problem exists with or without transparency. Electoral cycles create short-term incentives regardless.",
   "reasoning": "Direct restatement of the source."
  },
  {
   "claim_id": "C163",
   "loglog_ids": [
    "7.7.13"
   ],
   "claim_text": "Documented long-term rationale makes unpopular-but-wise decisions defensible.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "An unpopular decision with documented reasoning is defensible.",
   "reasoning": "Direct restatement of the source."
  },
  {
   "claim_id": "C164",
   "loglog_ids": [
    "7.7.14"
   ],
   "claim_text": "Evaluating reasoning, not just outcomes, is populism's antidote.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Transparency enables evaluation of *reasoning*, not just outcomes. And that's the antidote to populism, not its enabler.",
   "reasoning": "Both negations and the antidote claim match."
  },
  {
   "claim_id": "C165",
   "loglog_ids": [
    "7.7.15"
   ],
   "claim_text": "CEOs want documented reasoning, not merely popular decisions.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "The CEO doesn't want employees to make only *popular* decisions. The CEO wants employees to make *documented* decisions with clear reasoning.",
   "reasoning": "Faithful restatement with the only-popular contrast preserved."
  },
  {
   "claim_id": "C166",
   "loglog_ids": [
    "7.8"
   ],
   "claim_text": "Objection: misinformation makes transparency pointless.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "### \"Misinformation Makes Transparency Pointless\"",
   "reasoning": "Matches the source heading naming the misinformation objection."
  },
  {
   "claim_id": "C167",
   "loglog_ids": [
    "7.8.1"
   ],
   "claim_text": "Harvard 2023: Canadian panel; COVID-19 false beliefs lower perceived transparency.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "study published in the Harvard Kennedy School Misinformation Review (2023, based on a Canadian panel survey) found that people who endorse false beliefs (specifically COVID-19 related) perceive government as *less* transparent",
   "reasoning": "Year, venue, sample, and finding all match."
  },
  {
   "claim_id": "C168",
   "loglog_ids": [
    "7.8.2"
   ],
   "claim_text": "This holds controlling for real transparency levels.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "This holds even when controlling for real transparency.",
   "reasoning": "Direct restatement."
  },
  {
   "claim_id": "C169",
   "loglog_ids": [
    "7.8.3"
   ],
   "claim_text": "Negative transparency perceptions cut voting, trust, and democratic satisfaction.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "negative transparency perceptions are associated with decline in voting intentions, trust, and satisfaction with democracy.",
   "reasoning": "Close paraphrase preserving the three associated declines."
  },
  {
   "claim_id": "C170",
   "loglog_ids": [
    "7.8.4"
   ],
   "claim_text": "Citizens prize transparency's idea but dislike disclosures' messy content.",
   "claim_type": "interpretation",
   "verdict": "Partially supported",
   "severity": "Minor",
   "evidence_quote": "citizens value the *idea* of transparency but may react negatively to the *content* of actual disclosures",
   "reasoning": "Source hedges with may react negatively; node states the dislike as settled fact."
  },
  {
   "claim_id": "C171",
   "loglog_ids": [
    "7.8.5"
   ],
   "claim_text": "So-why-bother does not follow from these findings.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "the conclusion drawn from them - \"so why bother?\" - doesn't follow.",
   "reasoning": "Direct restatement preserving the negation."
  },
  {
   "claim_id": "C172",
   "loglog_ids": [
    "7.8.6"
   ],
   "claim_text": "False beliefs drive perceived opacity, not the reverse.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "false beliefs lead to perceived non-transparency. It does *not* show: actual transparency leads to more false beliefs.",
   "reasoning": "Preserves both the causal direction and the negation."
  },
  {
   "claim_id": "C173",
   "loglog_ids": [
    "7.8.7"
   ],
   "claim_text": "Opacity enables false beliefs; secrecy vacuums breed speculation.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "opacity *enables* false beliefs ... Speculation flourishes where documentation doesn't exist.",
   "reasoning": "Faithful to both source claims."
  },
  {
   "claim_id": "C174",
   "loglog_ids": [
    "7.8.8"
   ],
   "claim_text": "Election conspiracies grow where processes stay opaque.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Election conspiracy theories grow precisely because *some* processes remain opaque.",
   "reasoning": "Direct restatement preserving the some qualifier's sense."
  },
  {
   "claim_id": "C175",
   "loglog_ids": [
    "7.8.9"
   ],
   "claim_text": "Full documentation gives checkable ground truth for false claims.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Transparency provides ground truth. If full documentation exists, false claims can be checked against reality.",
   "reasoning": "Direct restatement of the source."
  },
  {
   "claim_id": "C176",
   "loglog_ids": [
    "7.8.10"
   ],
   "claim_text": "Latent availability deters misconduct even without consumption.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Availability changes behavior even without consumption. The knowledge that the record exists deters misconduct.",
   "reasoning": "Matches the source's availability-deters-misconduct claim."
  },
  {
   "claim_id": "C177",
   "loglog_ids": [
    "7.8.11"
   ],
   "claim_text": "CEOs need not read every email to benefit from access.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "The CEO doesn't read every email but values that they *could*.",
   "reasoning": "Faithful restatement preserving the negation."
  },
  {
   "claim_id": "C178",
   "loglog_ids": [
    "7.8.12"
   ],
   "claim_text": "Persistent transparency builds trust through consistently matching reality.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Persistent, comprehensive transparency creates a verifiable track record. Trust emerges when the disclosed information consistently matches reality.",
   "reasoning": "Direct restatement of the trust-building mechanism."
  },
  {
   "claim_id": "C179",
   "loglog_ids": [
    "7.8.13"
   ],
   "claim_text": "Pair transparency with accessibility, explanation, and intermediary translators.",
   "claim_type": "recommendation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "accompanied by accessibility, explanation, and intermediaries (journalists, civic tech, educators) who translate raw data",
   "reasoning": "Matches the source's recommended accompaniments."
  },
  {
   "claim_id": "C180",
   "loglog_ids": [
    "7.9"
   ],
   "claim_text": "Objection: markets will be manipulated by early disclosures.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "### \"Markets Will Be Manipulated\"",
   "reasoning": "Matches the source heading naming the markets objection."
  },
  {
   "claim_id": "C181",
   "loglog_ids": [
    "7.9.1"
   ],
   "claim_text": "Trade positions and monetary deliberations invite trader exploitation.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "doesn't publishing its positions undermine the negotiation? ... couldn't traders exploit advance knowledge?",
   "reasoning": "Faithful restatement of the source's two rhetorical concerns."
  },
  {
   "claim_id": "C182",
   "loglog_ids": [
    "7.9.2"
   ],
   "claim_text": "Conceded: valid but narrow; answer is delayed, not permanent, secrecy.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "This concern is valid but narrow. The solution isn't permanent secrecy. It's time-delayed transparency.",
   "reasoning": "Preserves the concession and the not-permanent negation."
  },
  {
   "claim_id": "C183",
   "loglog_ids": [
    "7.9.3"
   ],
   "claim_text": "The Fed releases minutes in three weeks, transcripts in five years.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "The US Federal Reserve releases FOMC minutes with a three-week delay and full transcripts with a five-year delay.",
   "reasoning": "Delays and entity match."
  },
  {
   "claim_id": "C184",
   "loglog_ids": [
    "7.9.4"
   ],
   "claim_text": "TTIP failed amid backlash from citizens feeling excluded by secrecy.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "The EU's failed TTIP trade negotiations actually suffered from *too much* secrecy - public backlash grew partly because citizens felt excluded",
   "reasoning": "Faithful to the source, including the partly qualifier's sense."
  },
  {
   "claim_id": "C185",
   "loglog_ids": [
    "7.9.5"
   ],
   "claim_text": "All information goes public eventually; only timing is managed.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "all information eventually becomes public. Timing may be managed for specific categories",
   "reasoning": "Direct restatement of the source."
  },
  {
   "claim_id": "C186",
   "loglog_ids": [
    "7.9.6"
   ],
   "claim_text": "Monetary waits for implementation, trade for conclusion, procurement for award.",
   "claim_type": "recommendation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "monetary policy (delay until implementation), trade negotiations (delay until conclusion), procurement (delay until contract award)",
   "reasoning": "All three category delays match."
  },
  {
   "claim_id": "C187",
   "loglog_ids": [
    "7.9.7"
   ],
   "claim_text": "Procurement secrecy lets officials favor connected contractors.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "If bidding processes are opaque, officials can favor connected contractors with impunity.",
   "reasoning": "Faithful restatement of the source."
  },
  {
   "claim_id": "C188",
   "loglog_ids": [
    "7.9.8"
   ],
   "claim_text": "Brazil's contract sunlight specifically prevents procurement fraud.",
   "claim_type": "name_or_entity",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Brazil's Transparency Portal includes contract information specifically because sunlight in procurement prevents fraud.",
   "reasoning": "Direct restatement with correct entity."
  },
  {
   "claim_id": "C189",
   "loglog_ids": [
    "7.10"
   ],
   "claim_text": "Objection: those in power will never allow this.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "### \"Those in Power Will Never Allow This\"",
   "reasoning": "Matches the source heading naming the power objection."
  },
  {
   "claim_id": "C190",
   "loglog_ids": [
    "7.10.1"
   ],
   "claim_text": "That describes the political challenge, not a principled objection.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "This is the concern that isn't really an objection. It's a description of the political challenge.",
   "reasoning": "Direct restatement preserving both negations."
  },
  {
   "claim_id": "C191",
   "loglog_ids": [
    "7.10.2"
   ],
   "claim_text": "Iceland 2008: 950 citizens set values; 25-member politician-free council drafted.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "After the 2008 financial crisis, 950 randomly selected citizens identified constitutional values. A 25-person council (explicitly excluding politicians) drafted a new constitution",
   "reasoning": "Year, both counts, and the politician exclusion match."
  },
  {
   "claim_id": "C192",
   "loglog_ids": [
    "7.10.3"
   ],
   "claim_text": "3,600 social-media comments; unanimous council; two-thirds referendum approval.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "3,600 public comments via social media. The draft was approved unanimously by the council and by a two-thirds majority in a national referendum.",
   "reasoning": "All three details match."
  },
  {
   "claim_id": "C193",
   "loglog_ids": [
    "7.10.4"
   ],
   "claim_text": "Parliament refused to ratify the draft.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "And then the existing parliament refused to ratify it.",
   "reasoning": "Direct restatement."
  },
  {
   "claim_id": "C194",
   "loglog_ids": [
    "7.10.5"
   ],
   "claim_text": "OGP: 75 countries, 4,500+ commitments since 2011; one-third delayed for funding.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Open Government Partnership (75 countries, 4,500+ commitments since 2011) found that one-third of delayed commitments fail due to \"lack of funding and technical capacity.\"",
   "reasoning": "All figures and the funding cause match."
  },
  {
   "claim_id": "C195",
   "loglog_ids": [
    "7.10.6"
   ],
   "claim_text": "Coordination failures, weak support, and transitions kill the rest.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "\"poor institutional coordination, lack of political support, and discontinuity from one administration to another during political transitions.\"",
   "reasoning": "Faithful compression of the source's listed remaining causes."
  },
  {
   "claim_id": "C196",
   "loglog_ids": [
    "7.10.7"
   ],
   "claim_text": "Successor governments abandon predecessors' transparency promises.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "new governments abandon their predecessors' transparency promises.",
   "reasoning": "Direct restatement."
  },
  {
   "claim_id": "C197",
   "loglog_ids": [
    "7.10.8"
   ],
   "claim_text": "Conceded: opacity's beneficiaries will always resist.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Those who benefit from opacity ... will resist transparency. They will always resist.",
   "reasoning": "Direct restatement of the concession."
  },
  {
   "claim_id": "C198",
   "loglog_ids": [
    "7.10.9"
   ],
   "claim_text": "Threatening the powerful is the point, not a flaw.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "It's a statement that transparency threatens the powerful. Which is exactly the point.",
   "reasoning": "Direct restatement preserving the negation."
  },
  {
   "claim_id": "C199",
   "loglog_ids": [
    "7.10.10"
   ],
   "claim_text": "Sweden 1766, post-Watergate, and post-2008 Iceland opened reform windows.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Sweden 1766 ... Post-Watergate US: scandal created a window for reform. Post-2008 Iceland: financial crisis created demand",
   "reasoning": "All three precedents match the source list."
  },
  {
   "claim_id": "C200",
   "loglog_ids": [
    "7.10.11"
   ],
   "claim_text": "Iceland's parliament ultimately blocked implementation despite the crisis.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "even though the existing parliament ultimately blocked implementation",
   "reasoning": "Direct restatement."
  },
  {
   "claim_id": "C201",
   "loglog_ids": [
    "7.10.12"
   ],
   "claim_text": "Ask who works for whom, not whether politicians permit oversight.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "The current framing asks: \"Will politicians allow this?\" That's the wrong question. The CEO framing asks: \"Who works for whom?\"",
   "reasoning": "Faithful restatement of the source's reframing."
  },
  {
   "claim_id": "C202",
   "loglog_ids": [
    "7.10.13"
   ],
   "claim_text": "This is a governance-design problem, not permission-seeking.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "This is a governance design problem, not a permission-seeking problem.",
   "reasoning": "Direct restatement preserving the negation."
  },
  {
   "claim_id": "C203",
   "loglog_ids": [
    "8"
   ],
   "claim_text": "Transparency is the measuring stick, not one value among many.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Transparency is not a value to be balanced. It's the measuring stick.",
   "reasoning": "Source rejects treating transparency as one value among many and names it the measuring stick."
  },
  {
   "claim_id": "C204",
   "loglog_ids": [
    "8.1"
   ],
   "claim_text": "Reject balancing transparency against efficiency, security, privacy, or speed.",
   "claim_type": "recommendation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "to \"balance\" it against efficiency, security, privacy, and speed ... Reject this framing.",
   "reasoning": "Source lists the same four values and explicitly rejects the balancing framing."
  },
  {
   "claim_id": "C205",
   "loglog_ids": [
    "8.2"
   ],
   "claim_text": "Speed and accountability are byproducts; document everything, then improve.",
   "claim_type": "recommendation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Speed and accountability are *byproducts*. Whatever speed your government operates at, document everything ... iteratively improve the processes",
   "reasoning": "Source states byproducts and instructs documenting everything then improving revealed processes."
  },
  {
   "claim_id": "C206",
   "loglog_ids": [
    "8.3"
   ],
   "claim_text": "The record pressures consistency, reasoning, accountability, and prosecution.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "pressure for consistency, pressure for sound reasoning, pressure for accountability ... easier to prosecute.",
   "reasoning": "Source lists exactly these pressures plus easier prosecution of corruption."
  },
  {
   "claim_id": "C207",
   "loglog_ids": [
    "8.4"
   ],
   "claim_text": "Reviewable officials reason better; documented decisions grow careful.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Officials who know their reasoning will be reviewed will produce better reasoning. Decisions that must be documented will be more carefully considered.",
   "reasoning": "Direct paraphrase of the two source sentences with identical meaning."
  },
  {
   "claim_id": "C208",
   "loglog_ids": [
    "8.5"
   ],
   "claim_text": "Reaching 100% transparency solves speed and accountability as consequences.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "In order to reach 100% transparency, you'll have to solve speed and accountability along the way ... they're consequences of it.",
   "reasoning": "Source says solving speed and accountability is required and labels them consequences, matching the claim."
  },
  {
   "claim_id": "C209",
   "loglog_ids": [
    "8.6"
   ],
   "claim_text": "Linux: thousands worldwide, every commit, issue, and pull request visible.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Linux ... built by thousands of people across the world ... Every commit is visible. Every issue is tracked. Every pull request is discussed.",
   "reasoning": "Source attributes these exact features to Linux and its worldwide contributors."
  },
  {
   "claim_id": "C210",
   "loglog_ids": [
    "8.7"
   ],
   "claim_text": "Disagreeing users can fork the project.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "If you disagree with a decision, you can fork the project.",
   "reasoning": "Near-verbatim restatement of the source sentence about forking."
  },
  {
   "claim_id": "C211",
   "loglog_ids": [
    "8.8"
   ],
   "claim_text": "Complex collaborative systems can be built and maintained publicly.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "complex systems can be built and maintained in public",
   "reasoning": "Source asserts this general principle about complex systems built in public."
  },
  {
   "claim_id": "C212",
   "loglog_ids": [
    "8.9"
   ],
   "claim_text": "Government is involuntary: you cannot fork your country.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "In government, you're subject to decisions whether you participated or not. You can't fork your country.",
   "reasoning": "Source states both the involuntary subjection and the inability to fork one's country."
  },
  {
   "claim_id": "C213",
   "loglog_ids": [
    "8.10"
   ],
   "claim_text": "Open source is voluntary exit; government binds non-participants.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "in open source, participation is voluntary. You can leave. In government, you're subject to decisions whether you participated or not.",
   "reasoning": "Claim matches the source contrast between voluntary exit and binding government decisions."
  },
  {
   "claim_id": "C214",
   "loglog_ids": [
    "8.11"
   ],
   "claim_text": "Less choice about affectedness means more right to see.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "The less choice you have about being affected by decisions, the more right you have to see how those decisions are made.",
   "reasoning": "Direct rephrasing of the source's proportional statement with same meaning."
  },
  {
   "claim_id": "C215",
   "loglog_ids": [
    "8.12"
   ],
   "claim_text": "You pay, live with consequences, and are CEO: act like it.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "You pay for this government. You live with its consequences. You are the CEO. Act like it.",
   "reasoning": "Compression of the four source sentences into one, preserving all propositions."
  },
  {
   "claim_id": "C216",
   "loglog_ids": [
    "9"
   ],
   "claim_text": "Appendix registers 49 sources backing the case.",
   "claim_type": "meta",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Appendix: Sources with Summaries ... 49. [Finnish Ministry of Justice - Act on Openness of Government Activities]",
   "reasoning": "Source appendix lists numbered sources 1 through 49."
  },
  {
   "claim_id": "C217",
   "loglog_ids": [
    "9.1"
   ],
   "claim_text": "UNESCO lists the 1766 ordinance as first free-communication legislation.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "UNESCO recognition of the 1766 act as world's first legislation guaranteeing free communication of information",
   "reasoning": "Source states UNESCO recognizes it as first such legislation."
  },
  {
   "claim_id": "C218",
   "loglog_ids": [
    "9.2"
   ],
   "claim_text": "GWU archive marks the FOI act's 250th anniversary; Britannica covers the 1766 act's Hats-Caps-Chydenius origins.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "George Washington University archive documenting the 250th anniversary of the world's first FOI act ... origins in the political conflict between Hats and Caps parties; role of Anders Chydenius",
   "reasoning": "Source describes both the 250th anniversary archive and the Hats-Caps-Chydenius origins."
  },
  {
   "claim_id": "C219",
   "loglog_ids": [
    "9.3"
   ],
   "claim_text": "X-Road official specs plus wiki history: 1998 start, 2001 launch, 1996 leak.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "history (started 1998, launched 2001), architecture decisions, 1996 data leak",
   "reasoning": "All three dates match source exactly."
  },
  {
   "claim_id": "C220",
   "loglog_ids": [
    "9.4"
   ],
   "claim_text": "Estonia's 30-year journey rose 16th to 2nd, hitting 100% digitalization in 2024; Brazil's 2004 CGU portal holds five categories.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "rise from 16th to 2nd ... 100% digitalization milestone in 2024 ... portal in 2004 by CGU; details five data categories",
   "reasoning": "Source matches all figures: 30-year, 16th to 2nd, 2024, 2004, five categories."
  },
  {
   "claim_id": "C221",
   "loglog_ids": [
    "9.5"
   ],
   "claim_text": "OECD logs 20+ million yearly portal visits and 17-source 2018 integration.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "portal accessed 20+ million times yearly; describes 2018 data warehouse integration of 17 sources",
   "reasoning": "Numbers and year match source."
  },
  {
   "claim_id": "C222",
   "loglog_ids": [
    "9.6"
   ],
   "claim_text": "Fiquem Sabendo's LAI probe surfaced 60GB over 27 years of former presidents.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Fiquem Sabendo used LAI to uncover 60GB of hidden pension payment data spanning 27 years of former presidents",
   "reasoning": "Actor, volume, and span match source."
  },
  {
   "claim_id": "C223",
   "loglog_ids": [
    "9.7"
   ],
   "claim_text": "OPEN launched April 1999 under Mayor Goh, covering 70 tasks.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "OPEN system launched April 1999 under Mayor Goh's anti-corruption campaign; covers 70 municipal tasks",
   "reasoning": "Date, actor, and count match source."
  },
  {
   "claim_id": "C224",
   "loglog_ids": [
    "9.8"
   ],
   "claim_text": "Peer-reviewed OPEN study confirms corruption falls as e-participation rises.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Peer-reviewed study ... confirms corruption decreases with e-participation",
   "reasoning": "Source states the same inverse relationship."
  },
  {
   "claim_id": "C225",
   "loglog_ids": [
    "9.9"
   ],
   "claim_text": "NZ guidance plus DPMC: 30-business-day cabinet releases from January 2019.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "details 30 business day requirement from January 2019",
   "reasoning": "Requirement and start date match source."
  },
  {
   "claim_id": "C226",
   "loglog_ids": [
    "9.10"
   ],
   "claim_text": "Taiwan's Pol.is crowdsourced Uber rules; paper traces Sunflower 2014, Tang, g0v.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "details Uber regulation as first test case ... traces origins to 2014 Sunflower Movement; analyzes Audrey Tang's role and g0v community",
   "reasoning": "Uber case, 2014, Tang, and g0v all appear in source."
  },
  {
   "claim_id": "C227",
   "loglog_ids": [
    "9.11"
   ],
   "claim_text": "Iceland analyses cover rejected crowdsourced draft and deliberative quality.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "why parliament rejected the crowdsourced draft despite referendum approval ... assessment of the deliberative quality",
   "reasoning": "Both analyses described match source."
  },
  {
   "claim_id": "C228",
   "loglog_ids": [
    "9.12"
   ],
   "claim_text": "EFF's 10-year Snowden review details FREEDOM Act gains and limits.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "10-year retrospective ... details USA FREEDOM Act passage and limitations",
   "reasoning": "Source matches on both gains and limitations."
  },
  {
   "claim_id": "C229",
   "loglog_ids": [
    "9.13"
   ],
   "claim_text": "IAPP review links disclosures to legal change and GDPR acceleration.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "legal and policy changes triggered by disclosures; notes GDPR acceleration",
   "reasoning": "Source states the same linkage."
  },
  {
   "claim_id": "C230",
   "loglog_ids": [
    "9.14"
   ],
   "claim_text": "TechCrunch and ACLU cover 2020 illegality rulings and privacy victory.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "2020 court ruling that NSA program was illegal ... ACLU attorney calls ruling \"a victory for privacy rights\"",
   "reasoning": "Both outlets and characterizations match source."
  },
  {
   "claim_id": "C231",
   "loglog_ids": [
    "9.15"
   ],
   "claim_text": "Pew 2019: 66% concerned; Roper tracks 1950s-present transparency opinion.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "66% concerned about government data collection ... from 1950s to present",
   "reasoning": "Percentage and period match source."
  },
  {
   "claim_id": "C232",
   "loglog_ids": [
    "9.16"
   ],
   "claim_text": "Roper adds ABC and Freedom Forum poll history on openness.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "includes ABC News and Freedom Forum poll data",
   "reasoning": "Both poll sources named in source."
  },
  {
   "claim_id": "C233",
   "loglog_ids": [
    "9.17"
   ],
   "claim_text": "IMF defends friction as accountability; Cambridge studies EU legitimacy perceptions.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "intentional accountability design ... transparency affects how public perceives decision-making legitimacy",
   "reasoning": "Both the IMF argument and Cambridge finding match source."
  },
  {
   "claim_id": "C234",
   "loglog_ids": [
    "9.18"
   ],
   "claim_text": "World Bank reviews mixed transparency impacts incumbents can undo.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "mixed findings on effectiveness; notes incumbents can undo positive effects of information",
   "reasoning": "Source states both mixed findings and incumbent reversal."
  },
  {
   "claim_id": "C235",
   "loglog_ids": [
    "9.19"
   ],
   "claim_text": "Harvard details Oman's Iran backchannel; Oxford frames the democratic dilemma.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "secret backchannel in Oman in achieving framework before public talks ... frames the \"democratic dilemma\"",
   "reasoning": "Both Harvard Oman detail and Oxford dilemma appear in source."
  },
  {
   "claim_id": "C236",
   "loglog_ids": [
    "9.20"
   ],
   "claim_text": "Notre Dame release: transparency aids lobbyists across 50 states, decades studied.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "transparency benefits lobbyists more than citizens in US state legislatures; ... multi-decade study of 50 states",
   "reasoning": "Source supports lobbyist benefit and 50-state multi-decade scope."
  },
  {
   "claim_id": "C237",
   "loglog_ids": [
    "9.21"
   ],
   "claim_text": "Oxford surveys diplomacy's secrecy evolution from antiquity to modernity.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "traces historical evolution from ancient diplomacy to modern era",
   "reasoning": "Source matches the ancient-to-modern scope."
  },
  {
   "claim_id": "C238",
   "loglog_ids": [
    "9.22"
   ],
   "claim_text": "Harden-Kirkland book blames electoral competition gaps; Irish 2024 trial had 569 subjects.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "proposes electoral competition as the key variable ... 2024 experimental study with 569 participants in Ireland",
   "reasoning": "Key variable and 569 participants match source."
  },
  {
   "claim_id": "C239",
   "loglog_ids": [
    "9.23"
   ],
   "claim_text": "Brennan 2024: 735 officials, threats rising since 2020, 38% threatened, ±3% margin.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "survey of 735 officials ... since 2020; 38% report threats; margin of error ±3%",
   "reasoning": "Sample size, trend, percentage, and margin match source."
  },
  {
   "claim_id": "C240",
   "loglog_ids": [
    "9.24"
   ],
   "claim_text": "NAAG tracks doxxing-swatting systematization and AI intensification.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "evolution from fringe behavior to systematic harassment; notes AI intensification",
   "reasoning": "Source states systematization and AI intensification."
  },
  {
   "claim_id": "C241",
   "loglog_ids": [
    "9.25"
   ],
   "claim_text": "Issue One counts 22 protective states since 2022; Chicago finds ~60% support, 12% to 17% wariness in 2021-2022.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "across 22 states since 2022 ... general support (~60%) but increasing civil liberties concerns (12% to 17% 2021-2022)",
   "reasoning": "State count, support level, and concern range match source."
  },
  {
   "claim_id": "C242",
   "loglog_ids": [
    "9.26"
   ],
   "claim_text": "Brennan decries overclassification; SIPRI links military openness to trust.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "classification levels far exceed genuine security needs ... military budget transparency ... builds inter-state trust",
   "reasoning": "Source supports overclassification critique and transparency-trust link."
  },
  {
   "claim_id": "C243",
   "loglog_ids": [
    "9.27"
   ],
   "claim_text": "Blair Institute: 43 states 1990-2018, populists 4x damaging, 5-place corruption slide.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "43 countries (1990-2018) ... 4x more likely to damage democratic institutions; countries fall average 5 places",
   "reasoning": "Country count, period, multiplier, and places match source."
  },
  {
   "claim_id": "C244",
   "loglog_ids": [
    "9.28"
   ],
   "claim_text": "Stanford warns visibility-driven re-election tempts short-term populism.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "transparency can create perverse incentives for short-term populist policies when re-election depends on immediate visibility",
   "reasoning": "Source states the same causal warning."
  },
  {
   "claim_id": "C245",
   "loglog_ids": [
    "9.29"
   ],
   "claim_text": "Sweden-Democrats study plus Harvard misinformation panel on perceived transparency.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Swedish populist party exploits transparency norms ... false beliefs causally reduce perceived transparency regardless of actual transparency levels",
   "reasoning": "Both studies described match source."
  },
  {
   "claim_id": "C246",
   "loglog_ids": [
    "9.30"
   ],
   "claim_text": "Latent-transparency experiments plus OGP's 75-country commitment autopsy.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "identifies \"latent transparency\" concept ... failed commitments across 75 member countries",
   "reasoning": "Latent transparency concept and 75 countries match source."
  },
  {
   "claim_id": "C247",
   "loglog_ids": [
    "9.31"
   ],
   "claim_text": "Hong 2024 ties competition-data quality to capacity; Ruijer (2020) maps conformity-to-resistance.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Hong (2024) ... only when administrative capacity is also high ... Ruijer et al. (2020) ... ranging from conformity to active resistance",
   "reasoning": "Both authors, years, and findings match source."
  },
  {
   "claim_id": "C248",
   "loglog_ids": [
    "9.32"
   ],
   "claim_text": "Workaround-resistance study plus Nordics' 250+ year openness overview.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "resist open government data policy through workarounds ... traces 250+ years of FOI practice",
   "reasoning": "Workaround study and 250+ year span match source."
  },
  {
   "claim_id": "C249",
   "loglog_ids": [
    "9.33"
   ],
   "claim_text": "Nordicom compares five Nordic regimes with inconsistent openness patterns.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "comparing right-of-access rules across five Nordic countries; notes inconsistent patterns",
   "reasoning": "Five-country comparison and inconsistency match source."
  },
  {
   "claim_id": "C250",
   "loglog_ids": [
    "9.34"
   ],
   "claim_text": "Finland's 1999 law deems documents public unless specifically exempted.",
   "claim_type": "definition",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "transparency law (1999 amendment); establishes principle that all government documents are public unless specifically exempted",
   "reasoning": "Year, default-public rule, and exemption match source."
  }
 ],
 "metrics": {
  "total_claims": 250,
  "supported": 245,
  "partially_supported": 5,
  "unverifiable": 0,
  "contradicted": 0,
  "critical_errors": 0,
  "faithfulness_precision": 0.98
 },
 "fail_list": [
  "C032",
  "C068",
  "C135",
  "C143",
  "C170"
 ]
}
```

## Judge Cov (coverage), opencode-go/deepseek-v4.1-flash

```json
{
 "judge": "coverage",
 "judge_version": "1.0.0",
 "model": "opencode-go/deepseek-v4.1-flash (opencode) scripted pipeline 2026-09-15",
 "source_id": "02_case_for_transparent_government",
 "key_points": [
  {
   "point_id": "K01",
   "point_text": "Central thesis: every government decision should be fully documented and publicly available, not just the final policy but the whole chain (data used, considerations, who was involved, alternatives, arguments for and against, implementation, evaluation, course-correction, and when/how it will be reconsidered). This is framed as basic accountability, not radicalism; only its novelty makes it sound radical.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L002",
    "L007",
    "L008",
    "L009",
    "L010",
    "L011",
    "L012"
   ],
   "evidence_quote": "Every government decision should be fully documented and publicly available. ... Document data used, considerations made, and who was involved. ... Document alternatives considered, arguments for and against, implementation steps. ... Document evaluation, course-correction plans, and reconsideration terms. ... It sounds radical only because the opposite was normalized.",
   "reasoning": "L007 states the thesis and L008-L010 enumerate the full chain (data, who, alternatives, arguments, implementation, evaluation, reconsideration), matching the source. L011-L012 add the basic-accountability and radical-only-because-novel framing."
  },
  {
   "point_id": "K02",
   "point_text": "Citizen-as-CEO framing: in a democracy citizens are the principals/CEOs and public servants are agents/employees who spend the citizens' money; information flows upward and accountability exists because a reviewable trail exists, whereas the current government lets agents classify and refuse to explain.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L013",
    "L014",
    "L015",
    "L016"
   ],
   "evidence_quote": "In democracy citizens are principals; officials are their employee-agents. ... Every servant from licensing clerk to president works for you. ... A company letting managers classify emails would go bankrupt within a year.",
   "reasoning": "L013-L016 capture the principal/agent CEO framing, the servant range from clerk to president, and the classify-and-refuse analogy to the current government."
  },
  {
   "point_id": "K03",
   "point_text": "Availability versus consumption distinction: the citizen-CEO need not read every email or attend every meeting, but must be able to trace any decision that matters; mere availability changes behavior even without consumption.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L015",
    "L017",
    "L177",
    "L178"
   ],
   "evidence_quote": "CEOs need not read everything, but reviewability shapes behavior. ... Nuance: Availability matters, not consumption: trace decisions affecting your life. ... Latent availability deters misconduct even without consumption. ... CEOs need not read every email to benefit from access.",
   "reasoning": "L015 and L017 state the distinction directly; L177-L178 reinforce that latent availability deters misconduct without consumption, matching the source."
  },
  {
   "point_id": "K04",
   "point_text": "Scope clarification: transparency is about government decisions, processes, and officials flowing to citizens, NOT about citizens surveilling each other or exposing personal records (tax returns, medical records). Privacy-preserving approaches (aggregation, anonymization, differential privacy) make separating government decision data from citizen personal data technically straightforward.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L018",
    "L019",
    "L020",
    "L021",
    "L022",
    "L023"
   ],
   "evidence_quote": "Transparency flows from government to citizens, never the reverse. ... Not tax returns, medical records, or citizens surveilling each other. ... Publish $X/$Y/$Z/$W spending, not John Smith's $47,000 taxes. ... Aggregation, anonymization, and differential privacy make separation technically straightforward.",
   "reasoning": "L018-L020 state the direction and exclusions (tax returns, medical records, mutual surveillance). L023 names all three privacy-preserving techniques, so the quantifier and mechanism are intact."
  },
  {
   "point_id": "K05",
   "point_text": "Sweden 1766: the Freedom of the Press Act was the world's first freedom of information law, now part of the constitution; born from Hats vs Caps political conflict, driven by Anders Chydenius with an explicitly anti-corruption motive. Two hundred sixty years later the offentlighetsprincipen makes documents public by default and the country has not collapsed, with Nordic countries ranking among the least corrupt and most effective democracies.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L026",
    "L027",
    "L028",
    "L029",
    "L030",
    "L031"
   ],
   "evidence_quote": "Sweden's 260-year openness shows transparency endures without collapse. ... In 1766 Sweden passed the world's first freedom-of-information law. ... Chydenius drove Hats-versus-Caps explicitly anti-corruption law. ... Offentlighetsprincipen keeps documents public by default 260 years on. ... Nordics consistently rank among least corrupt, most effective democracies.",
   "reasoning": "All elements present: 1766, first FOI law, constitutional, Hats vs Caps, Chydenius, anti-corruption motive, offentlighetsprincipen by default, no collapse, Nordic rankings."
  },
  {
   "point_id": "K06",
   "point_text": "Seoul/South Korea 1999: the OPEN system tracks 70 corruption-prone municipal tasks (construction permits, environmental regulation, urban planning) and shows citizens who decided what, at which point, in real time; this visibility removed the leverage that enabled bribery, and research confirmed corruption decreases as e-participation increases.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L032",
    "L033",
    "L034",
    "L035",
    "L036",
    "L037"
   ],
   "evidence_quote": "Seoul's 1999 OPEN system made bribery-prone permitting visible. ... OPEN tracks 70 corruption-prone tasks, including construction, environmental, and urban planning permits, in real time. ... Visibility eliminated that bribery leverage entirely. ... Corruption decreases as e-participation increases.",
   "reasoning": "Year, task count, three task categories, real-time visibility, elimination of bribery leverage, and the e-participation research finding are all captured."
  },
  {
   "point_id": "K07",
   "point_text": "Estonia 2001: X-Road is a distributed data exchange layer connecting 929+ institutions, 1,887 information systems, and 3,000+ digital services, with every transaction timestamped and cryptographically signed and all access logged; Estonia ranks 2nd in the UN E-Government Development Index with no major breaches in over 20 years, proving the infrastructure is technically feasible and that the will, not the technology, is the bottleneck.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L038",
    "L039",
    "L040",
    "L041",
    "L042",
    "L043",
    "L044",
    "L045"
   ],
   "evidence_quote": "Estonia's 2001 X-Road proves transparency infrastructure scales. ... X-Road links 929+ institutions, 1,887 systems, 3,000+ services, timestamped, signed, logged. ... Estonia ranks 2nd on the UN E-Government Development Index. ... No major breaches in over 20 years ... The technology is feasible; the bottleneck is will.",
   "reasoning": "All numbers (929+, 1,887, 3,000+), the signing/timestamping/logging, 2nd rank, no-major-breaches, and the will-not-technology conclusion are present."
  },
  {
   "point_id": "K08",
   "point_text": "Brazil 2004: the Transparency Portal publishes all federal spending (contracts, transfers, salaries, travel, credit card transactions) with 20+ million accesses per year; the Transparency Card sends real-time notifications about political spending (430,000+ active cards, 20+ million notifications), and journalists using the Access to Information Law uncovered 60GB of hidden pension payment data going back 27 years.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L046",
    "L047",
    "L048",
    "L049",
    "L050"
   ],
   "evidence_quote": "Brazil's 2004 Transparency Portal follows all federal money. ... It publishes contracts, transfers, salaries, travel, and credit-card transactions. ... over 20 million accesses per year. ... Transparency Card sent 20+ million notifications via 430,000+ active cards. ... Journalists uncovered 60GB of hidden pension payments spanning 27 years.",
   "reasoning": "Year, five published categories, 20+ million accesses, Transparency Card with 430,000+ cards and 20+ million notifications, and the 60GB/27-year pension find are all present."
  },
  {
   "point_id": "K09",
   "point_text": "New Zealand 2019: the government proactively publishes all Cabinet papers and minutes online within 30 business days of decisions, even though cabinet deliberations are typically the most protected category of government information; government has not ground to a halt and citizens can now see why decisions were made.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L052",
    "L053",
    "L054",
    "L055"
   ],
   "evidence_quote": "New Zealand publishes cabinet papers by default since 2019. ... All papers and minutes appear online within 30 business days. ... Cabinet deliberations are typically the world's most protected government information. ... Government has not halted ... citizens see why.",
   "reasoning": "Year, 30-business-day window, most-protected-category framing, and the not-halted/see-why outcome all match."
  },
  {
   "point_id": "K10",
   "point_text": "Recurring pattern: secret government programs are later revealed to be illegal or built on lies, and internal oversight failed because it operated inside the same secrecy bubble. Examples: Pentagon Papers 1971 (Vietnam unwinnable while publicly claiming progress), COINTELPRO exposed 1971 (illegal surveillance of civil rights leaders), Snowden 2013 (NSA bulk metadata collection, PRISM, surveilling foreign leaders). In each case the government predicted catastrophe and the programs proved illegal, unconstitutional, or deceptive.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L060",
    "L061",
    "L062",
    "L063",
    "L064",
    "L065",
    "L070",
    "L071"
   ],
   "evidence_quote": "Secret programs recur as illegal; secret oversight reliably fails to catch them. ... 1971 Pentagon Papers showed government knew Vietnam was unwinnable while publicly claiming progress. ... Media, Pennsylvania break-in exposed COINTELPRO's illegal surveillance ... In 2013 Snowden revealed bulk metadata collection ... PRISM, and leader surveillance. ... FISA courts, committees, and inspectors general failed inside the secrecy structure.",
   "reasoning": "The pattern, all three examples with years and content, the failed cataclysm predictions, and the oversight-inside-secrecy explanation (L070-L071) are all captured."
  },
  {
   "point_id": "K11",
   "point_text": "Snowden aftermath: in September 2020 the US Ninth Circuit ruled the NSA bulk phone record collection illegal and possibly unconstitutional, failing FISA's relevance requirement; Geoffrey R. Stone found no evidence it stopped terror attacks, and the NSA abandoned the program in 2018. The USA FREEDOM Act (2015) was the first legislation in over 30 years to rein in NSA spying, ending bulk metadata collection; tech transparency reporting, default HTTPS, and accelerated EU GDPR followed. Whether disclosure caused operational harm remains genuinely uncertain, but the legality and oversight failures are not.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L066",
    "L067",
    "L068",
    "L069",
    "L072",
    "L073",
    "L074",
    "L075",
    "L076",
    "L077"
   ],
   "evidence_quote": "In September 2020 the Ninth Circuit ruled bulk collection illegal, possibly unconstitutional. ... The court required FISA relevance to a particular authorized investigation. ... Stone found no evidence bulk collection stopped any terror attacks. ... The NSA abandoned the program in 2018 ... The 2015 USA FREEDOM Act first reined in NSA spying in over 30 years. ... HTTPS became default ... GDPR was accelerated ... Operational harm is genuinely uncertain; illegality is not.",
   "reasoning": "All specifics present: Sept 2020 Ninth Circuit, possibly unconstitutional, FISA relevance, Stone, 2018 abandonment, 2015 Act/first-in-30-years, transparency reporting, HTTPS, GDPR, and the harm-uncertain/illegality-certain caveat."
  },
  {
   "point_id": "K12",
   "point_text": "Privacy and harassment objections: privacy fears (e.g., 66% concerned about government data collection; 86% opposed to online public records) are about citizen data held by government, not about government decisions being visible, so they rest on a direction confusion; likewise threats to officials are real (Brennan Center 2024 survey of 735 officials: 38% threatened, 34% know someone who resigned, up from 22% in 2023), so decisions should be public while officials' personal information is protected. Much current harassment stems from lack of transparency about processes.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L082",
    "L083",
    "L084",
    "L126",
    "L127",
    "L128",
    "L133",
    "L135",
    "L136"
   ],
   "evidence_quote": "2019 Pew: 66% fear collection ... A 2000 ABC poll: 86% said agencies should not publish such records online. ... Polls fear citizen data held by government, not visible government decisions. ... Brennan surveyed 735 local election officials ... 38% threatened ... 34% know someone who resigned, up from 22% in 2023. ... Publish who decided what and why; protect addresses, families, schedules. ... Current harassment feeds on opacity-bred fraud conspiracies.",
   "reasoning": "All numbers and caveats present: 66%, 86%, direction-confusion rebuttal, Brennan 735/38%/34% up from 22%, protect personal info while publishing decisions, and harassment-fed-by-opacity."
  },
  {
   "point_id": "K13",
   "point_text": "Secrecy-based objections and answers: the gridlock argument confuses speed with documentation (transparency documents decisions at the current speed, as NZ shows, and opacity makes decisions unaccountable rather than better); diplomacy (JCPOA secret Oman backchannel, Camp David, Cold War) and markets (Fed FOMC minutes delayed three weeks, transcripts five years; TTIP harmed by too much secrecy) justify only temporary operational secrecy with time-delayed release (e.g., 30-90 days), never permanent secrecy about what was decided and why; national security is overused to hide embarrassment, illegality, incompetence, and corruption, and the burden of proof should be reversed so officials must justify secrecy.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L092",
    "L094",
    "L095",
    "L096",
    "L100",
    "L101",
    "L105",
    "L106",
    "L147",
    "L148",
    "L149",
    "L150",
    "L184",
    "L185",
    "L186"
   ],
   "evidence_quote": "This confuses decision speed with decision documentation. ... New Zealand's 30-day cabinet papers halted nothing ... Opacity makes decisions unaccountable random walks, not better ones. ... JCPOA began in 2012 via Sullivan's secret Oman backchannel. ... Camp David 1978 and Cold War backchannels ... Temporary secrecy during talks is acceptable; permanent secrecy is not. ... Release full documentation 30-90 days after conclusion ... The Fed releases minutes in three weeks, transcripts in five years. ... TTIP failed amid backlash ... Flip the burden: transparent by default, secrecy needs proof. ... The label hides embarrassment, illegality, incompetence, and corruption. ... Officials under scrutiny set secrecy criteria: a conflict of interest.",
   "reasoning": "Every element is present: speed/documentation confusion, NZ example, unaccountability of opacity, JCPOA Oman, Camp David, Cold War, Fed 3-week/5-year timing, TTIP, 30-90 day delayed release, national-security overuse/label, and reversing the burden of proof."
  },
  {
   "point_id": "K14",
   "point_text": "Empirical misuse concerns acknowledged but rebutted: Harden and Kirkland found open legislative meetings bring more lobbying, more lobbyist donations, and no improved policy-opinion correlation, and 2024 Irish experiment found lobbying transparency does not raise trust; populism research (Kyle and Gultchin, 43 countries 1990-2018) finds populists 4x more likely to damage democracy and countries falling ~5 places on the Corruption Perceptions Index; misinformation research finds false beliefs reduce perceived transparency. The answer is not less transparency but building citizen capacity (watchdogs, investigative journalism, civic tech, professional monitoring) and better transparency, since populists reduce rather than increase transparency, opacity enables false beliefs, and selective exploitation works only because not everything is visible.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L111",
    "L113",
    "L114",
    "L116",
    "L117",
    "L119",
    "L153",
    "L154",
    "L155",
    "L161",
    "L162",
    "L168",
    "L173",
    "L174"
   ],
   "evidence_quote": "Harden and Kirkland studied all 50 legislatures over multiple decades. ... More lobbyists register and donate, yet policy-opinion correlation stays same open or closed. ... Ireland 2024: 569 participants; lobbying transparency did not raise trust. ... Build citizen capacity: auditors, watchdogs, journalism, civic tech. ... Kyle-Gultchin studied 43 democracies, 1990-2018 ... Populists are 4x likelier to damage institutions ... Countries fall 5 places on corruption perceptions ... Causality is backwards: populists damage democracy by reducing transparency. ... Cherry-picking works only while the full record stays hidden. ... Harvard 2023 ... COVID-19 false beliefs lower perceived transparency. ... False beliefs drive perceived opacity, not the reverse. ... Opacity enables false beliefs.",
   "reasoning": "All empirical results and numbers present: Harden/Kirkland lobbying and donation finding with no correlation improvement, Irish 2024 experiment, Kyle-Gultchin 43 countries/1990-2018/4x/5 places, misinformation false-beliefs finding, and the citizen-capacity plus causal-reversal rebuttals."
  },
  {
   "point_id": "K15",
   "point_text": "Resistance and the closing vision: 'those in power will never allow this' is a description of the political challenge, not a principled objection (Iceland's 2008 crowdsourced constitution was blocked by parliament despite referendum approval; OGP commitments fail on funding, coordination, and political transitions), and the CEO framing reframes it as a governance design problem of who works for whom. Transparency is not a value to be balanced but the measuring stick; speed and accountability are byproducts, and open source shows complex collaborative work can be done in public, with the case for transparency stronger because citizens cannot fork their country.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L191",
    "L193",
    "L194",
    "L195",
    "L196",
    "L197",
    "L202",
    "L203",
    "L204",
    "L205",
    "L206",
    "L209",
    "L210",
    "L211",
    "L212",
    "L213"
   ],
   "evidence_quote": "That describes the political challenge, not a principled objection. ... two-thirds referendum approval. ... Parliament refused to ratify the draft. ... OGP: 75 countries, 4,500+ commitments since 2011; one-third delayed for funding. ... Ask who works for whom ... This is a governance-design problem, not permission-seeking. ... Transparency is the measuring stick, not one value among many. ... Speed and accountability are byproducts ... Linux ... Disagreeing users can fork the project. ... Government is involuntary: you cannot fork your country.",
   "reasoning": "All elements present: description-not-objection reframe, Iceland 2008 blocked constitution, OGP funding/coordination/transition failures, who-works-for-whom governance-design framing, transparency-as-measuring-stick, speed/accountability as byproducts, open-source example, and cannot-fork-your-country."
  }
 ],
 "metrics": {
  "total_points": 15,
  "must_have_total": 15,
  "must_have_present": 15,
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
 "source_id": "02_case_for_transparent_government",
 "claims": [
  {
   "claim_id": "C001",
   "loglog_ids": [
    "0"
   ],
   "claim_text": "Citizens are governments' CEO-principals, so every decision should be fully documented and traceable, with objections answered and precedents proving feasibility.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "None",
   "evidence_quote": "every government decision should be fully documented and publicly available ... You are the principal ... Pieces of this system already exist",
   "reasoning": "Summary tracks the thesis, principal-agent framing, and the objections and precedents sections of the source."
  },
  {
   "claim_id": "C002",
   "loglog_ids": [
    "1"
   ],
   "claim_text": "A manager hiding a million-dollar decision would be fired, yet governments do the same.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "None",
   "evidence_quote": "You'd fire them. ... That's how your government operates.",
   "reasoning": "Source states the owner would fire the manager and later says government operates the same way."
  },
  {
   "claim_id": "C003",
   "loglog_ids": [
    "1.1"
   ],
   "claim_text": "Manager refused to explain a million-dollar decision, citing lost leverage.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "None",
   "evidence_quote": "If you know how I make these decisions, I lose my leverage.",
   "reasoning": "Direct paraphrase of the manager's quoted refusal about the million-dollar budget decision."
  },
  {
   "claim_id": "C004",
   "loglog_ids": [
    "1.2"
   ],
   "claim_text": "An owner would sue, force disclosure, and fire that manager.",
   "claim_type": "claim",
   "verdict": "Supported",
   "severity": "None",
   "evidence_quote": "You'd take them to court. You'd force disclosure. You'd fire them.",
   "reasoning": "Matches the source's three listed responses exactly."
  },
  {
   "claim_id": "C005",
   "loglog_ids": [
    "1.3"
   ],
   "claim_text": "Governments refuse with classified, security, operations, and speed excuses.",
   "claim_type": "claim",
   "verdict": "Supported",
   "severity": "None",
   "evidence_quote": "you're told it's classified. It's a matter of national security. It would compromise ongoing operations. It would slow things down.",
   "reasoning": "All four cited excuses map directly to the source's listed justifications."
  },
  {
   "claim_id": "C006",
   "loglog_ids": [
    "2"
   ],
   "claim_text": "Every government decision should be fully documented and publicly available.",
   "claim_type": "recommendation",
   "verdict": "Supported",
   "severity": "None",
   "evidence_quote": "every government decision should be fully documented and publicly available",
   "reasoning": "Verbatim restatement of the source's central proposition."
  },
  {
   "claim_id": "C007",
   "loglog_ids": [
    "2.1"
   ],
   "claim_text": "Document data used, considerations made, and who was involved.",
   "claim_type": "recommendation",
   "verdict": "Supported",
   "severity": "None",
   "evidence_quote": "What data was used ... What considerations were made ... Who was involved",
   "reasoning": "First three items of the source's chain list, preserved."
  },
  {
   "claim_id": "C008",
   "loglog_ids": [
    "2.2"
   ],
   "claim_text": "Document alternatives considered, arguments for and against, implementation steps.",
   "claim_type": "recommendation",
   "verdict": "Supported",
   "severity": "None",
   "evidence_quote": "What alternatives were considered ... arguments for and against ... How it will be implemented",
   "reasoning": "Maps to the middle items of the source's documentation chain list."
  },
  {
   "claim_id": "C009",
   "loglog_ids": [
    "2.3"
   ],
   "claim_text": "Document evaluation, course-correction plans, and reconsideration terms.",
   "claim_type": "recommendation",
   "verdict": "Supported",
   "severity": "None",
   "evidence_quote": "How it will be evaluated ... course-correction plans ... When and how it will be reconsidered, and what it takes to change it",
   "reasoning": "Covers the final items of the source's documentation chain list."
  },
  {
   "claim_id": "C010",
   "loglog_ids": [
    "2.4"
   ],
   "claim_text": "Competent boards and CEOs already demand this basic accountability.",
   "claim_type": "claim",
   "verdict": "Supported",
   "severity": "None",
   "evidence_quote": "This is what any competent board of directors expects ... It's what any CEO expects ... It's basic accountability.",
   "reasoning": "Aligns with the source's board, CEO, and basic accountability statements."
  },
  {
   "claim_id": "C011",
   "loglog_ids": [
    "2.5"
   ],
   "claim_text": "It sounds radical only because the opposite was normalized.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "None",
   "evidence_quote": "The only thing that makes it sound radical is that we've normalized the opposite.",
   "reasoning": "Near-verbatim, with the restrictive 'only' preserved as in the source."
  },
  {
   "claim_id": "C012",
   "loglog_ids": [
    "3"
   ],
   "claim_text": "In democracy citizens are principals; officials are their employee-agents.",
   "claim_type": "claim",
   "verdict": "Supported",
   "severity": "None",
   "evidence_quote": "You are the principal in a principal-agent relationship ... is an agent working on your behalf ... They are your employees.",
   "reasoning": "Faithfully captures the source's principal-agent and employees framing."
  },
  {
   "claim_id": "C013",
   "loglog_ids": [
    "3.1"
   ],
   "claim_text": "Every servant from licensing clerk to president works for you.",
   "claim_type": "claim",
   "verdict": "Supported",
   "severity": "None",
   "evidence_quote": "Every public servant, from the clerk at your local licensing office to the president, is an agent working on your behalf.",
   "reasoning": "Same endpoints and scope as the source span."
  },
  {
   "claim_id": "C014",
   "loglog_ids": [
    "3.2"
   ],
   "claim_text": "CEOs need not read everything, but reviewability shapes behavior.",
   "claim_type": "claim",
   "verdict": "Supported",
   "severity": "None",
   "evidence_quote": "The CEO doesn't read every email. But they *could*. And that knowledge - that anything could be reviewed at any time - shapes behavior.",
   "reasoning": "Preserves both the non-consumption point and the behavioral effect of reviewability."
  },
  {
   "claim_id": "C015",
   "loglog_ids": [
    "3.3"
   ],
   "claim_text": "A company letting managers classify emails would go bankrupt within a year.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "None",
   "evidence_quote": "That company would be bankrupt within a year, eaten alive by internal corruption and incompetence",
   "reasoning": "Timeline and outcome match the source's hypothetical exactly."
  },
  {
   "claim_id": "C016",
   "loglog_ids": [
    "3.4"
   ],
   "claim_text": "Availability matters, not consumption: trace decisions affecting your life.",
   "claim_type": "nuance",
   "verdict": "Supported",
   "severity": "None",
   "evidence_quote": "The distinction between \"availability\" and \"consumption\" is crucial ... if a decision affects your community, your livelihood, your children's future - you *can* trace it back.",
   "reasoning": "Reflects the source's availability-versus-consumption distinction and traceability point."
  },
  {
   "claim_id": "C017",
   "loglog_ids": [
    "4"
   ],
   "claim_text": "Transparency flows from government to citizens, never the reverse.",
   "claim_type": "definition",
   "verdict": "Supported",
   "severity": "None",
   "evidence_quote": "the government's decisions, data, and processes flow *to* citizens. Not the other way around.",
   "reasoning": "One-directional claim matches the source's directional definition and negation."
  },
  {
   "claim_id": "C018",
   "loglog_ids": [
    "4.1"
   ],
   "claim_text": "Decisions visible, processes traceable, officials accountable to citizens.",
   "claim_type": "definition",
   "verdict": "Supported",
   "severity": "None",
   "evidence_quote": "Government decisions being visible to citizens. Government processes being traceable by citizens. Government officials being accountable to citizens.",
   "reasoning": "Direct restatement of the source's 'This is about' list."
  },
  {
   "claim_id": "C019",
   "loglog_ids": [
    "4.2"
   ],
   "claim_text": "Not tax returns, medical records, or citizens surveilling each other.",
   "claim_type": "definition",
   "verdict": "Supported",
   "severity": "None",
   "evidence_quote": "This is NOT about: Your tax returns ... Your medical records being public. Citizens surveilling each other.",
   "reasoning": "Negated exclusions preserved exactly from the source's 'This is NOT about' list."
  },
  {
   "claim_id": "C020",
   "loglog_ids": [
    "4.3"
   ],
   "claim_text": "CEOs see work product, not employees' medical records.",
   "claim_type": "definition",
   "verdict": "Supported",
   "severity": "None",
   "evidence_quote": "The CEO sees employee work product. The CEO does not publish employees' medical records to angry customers.",
   "reasoning": "Preserves the work-product versus medical-records contrast and the negation."
  },
  {
   "claim_id": "C021",
   "loglog_ids": [
    "4.4"
   ],
   "claim_text": "Publish $X/$Y/$Z/$W spending, not John Smith's $47,000 taxes.",
   "claim_type": "example",
   "verdict": "Supported",
   "severity": "None",
   "evidence_quote": "spent it as follows: $Y on healthcare, $Z on defense, $W on infrastructure ... It does *not* mean: \"John Smith paid $47,000 in taxes last year.\"",
   "reasoning": "Example structure and the $47,000 figure match the source exactly."
  },
  {
   "claim_id": "C022",
   "loglog_ids": [
    "4.5"
   ],
   "claim_text": "Aggregation, anonymization, and differential privacy make separation technically straightforward.",
   "claim_type": "claim",
   "verdict": "Supported",
   "severity": "None",
   "evidence_quote": "Privacy-preserving approaches - aggregate data, anonymization, differential privacy - make this technically straightforward.",
   "reasoning": "All three named techniques and the 'straightforward' qualifier match the source."
  },
  {
   "claim_id": "C023",
   "loglog_ids": [
    "5"
   ],
   "claim_text": "Pieces of this system already exist and prove it works.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Pieces of this system already exist around the world... several have gone far enough to prove it works.",
   "reasoning": "SOURCE asserts existing pieces and that several cases prove it works; identical meaning."
  },
  {
   "claim_id": "C024",
   "loglog_ids": [
    "5.1"
   ],
   "claim_text": "No country nears complete transparency, but several prove feasibility.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "No country has achieved anything close to complete transparency, but several have gone far enough to prove it works.",
   "reasoning": "Direct paraphrase preserving the concession and the feasibility claim."
  },
  {
   "claim_id": "C025",
   "loglog_ids": [
    "5.2"
   ],
   "claim_text": "Sweden's 260-year openness shows transparency endures without collapse.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Two hundred and sixty years later, Sweden still operates under this principle... The country has not collapsed.",
   "reasoning": "260 years, endurance, and non-collapse are all stated in SOURCE."
  },
  {
   "claim_id": "C026",
   "loglog_ids": [
    "5.2.1"
   ],
   "claim_text": "In 1766 Sweden passed the world's first freedom-of-information law.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "In 1766, Sweden passed the Freedom of the Press Act - the world's first freedom of information law.",
   "reasoning": "Date and superlative match SOURCE exactly."
  },
  {
   "claim_id": "C027",
   "loglog_ids": [
    "5.2.2"
   ],
   "claim_text": "It abolished censorship and is now constitutional.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "It abolished censorship... It's now part of the Swedish constitution.",
   "reasoning": "Both facts appear verbatim in SOURCE."
  },
  {
   "claim_id": "C028",
   "loglog_ids": [
    "5.2.3"
   ],
   "claim_text": "Finnish-Swedish priest-politician Chydenius drove Hats-versus-Caps explicitly anti-corruption law.",
   "claim_type": "name_or_entity",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Anders Chydenius, a Finnish-Swedish priest and politician, drove the legislation through parliament. The motivation was explicitly anti-corruption.",
   "reasoning": "Name, roles, driving role, and anti-corruption motive all match; Hats/Caps context is adjacent."
  },
  {
   "claim_id": "C029",
   "loglog_ids": [
    "5.2.4"
   ],
   "claim_text": "Offentlighetsprincipen keeps documents public by default 260 years on.",
   "claim_type": "definition",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Two hundred and sixty years later, Sweden still operates under this principle. It's called offentlighetsprincipen... Government documents are public by default.",
   "reasoning": "Term, default-public rule, and 260-year persistence all stated."
  },
  {
   "claim_id": "C030",
   "loglog_ids": [
    "5.2.5"
   ],
   "claim_text": "Nordics consistently rank among least corrupt, most effective democracies.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Nordic countries consistently rank among the least corrupt and most effective democracies in the world.",
   "reasoning": "Near-verbatim restatement."
  },
  {
   "claim_id": "C031",
   "loglog_ids": [
    "5.3"
   ],
   "claim_text": "Seoul's 1999 OPEN system made bribery-prone permitting visible.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "In 1999, Seoul launched the OPEN system... shows citizens exactly who made what decision.",
   "reasoning": "Year and the visibility of corruption-prone tasks match."
  },
  {
   "claim_id": "C032",
   "loglog_ids": [
    "5.3.1"
   ],
   "claim_text": "OPEN tracks 70 corruption-prone tasks, including construction, environmental, and urban planning permits, in real time.",
   "claim_type": "number_or_date",
   "verdict": "Partially supported",
   "severity": "Minor",
   "evidence_quote": "tracks 70 municipal tasks most prone to corruption - construction permits, environmental regulation, urban planning - and shows citizens... in real time.",
   "reasoning": "Number 70 is correct, but SOURCE lists environmental regulation and urban planning, not permits, and ties real time to showing citizens."
  },
  {
   "claim_id": "C033",
   "loglog_ids": [
    "5.3.2"
   ],
   "claim_text": "Citizens see exactly who decided what at each process point.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "shows citizens exactly who made what decision, at which point in the process, in real time.",
   "reasoning": "Direct restatement of SOURCE."
  },
  {
   "claim_id": "C034",
   "loglog_ids": [
    "5.3.3"
   ],
   "claim_text": "Previously invisible processing let officials demand speed-up bribes unprovably.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "This opacity enabled bribery: officials could demand payments to \"move things along\" and nobody could prove it.",
   "reasoning": "Opacity-to-bribery causal link and unprovability all stated."
  },
  {
   "claim_id": "C035",
   "loglog_ids": [
    "5.3.4"
   ],
   "claim_text": "Visibility eliminated that bribery leverage entirely.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Making the process visible eliminated that leverage entirely.",
   "reasoning": "Verbatim in meaning."
  },
  {
   "claim_id": "C036",
   "loglog_ids": [
    "5.3.5"
   ],
   "claim_text": "Corruption decreases as e-participation increases; UN, OECD, World Bank recognized it.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "\"corruption decreases as e-participation increases.\" The system was recognized by the UN, OECD, and World Bank.",
   "reasoning": "Quote and the three recognizing bodies match SOURCE."
  },
  {
   "claim_id": "C037",
   "loglog_ids": [
    "5.4"
   ],
   "claim_text": "Estonia's 2001 X-Road proves transparency infrastructure scales.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "### Estonia: The Infrastructure Proof (2001)... If your objection is \"this can't scale,\" look at Estonia's X-Road.",
   "reasoning": "Year and scale-proof framing both supported."
  },
  {
   "claim_id": "C038",
   "loglog_ids": [
    "5.4.1"
   ],
   "claim_text": "X-Road links 929+ institutions, 1,887 systems, 3,000+ services, timestamped, signed, logged.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "connecting 929+ institutions, 1,887 information systems, and 3,000+ digital services. Every transaction is timestamped and cryptographically signed. All data access is logged.",
   "reasoning": "All three figures and the three properties match SOURCE."
  },
  {
   "claim_id": "C039",
   "loglog_ids": [
    "5.4.2"
   ],
   "claim_text": "Citizens can see who accessed their data and why.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Citizens can see who accessed their data and why.",
   "reasoning": "Verbatim."
  },
  {
   "claim_id": "C040",
   "loglog_ids": [
    "5.4.3"
   ],
   "claim_text": "Estonia ranks 2nd on the UN E-Government Development Index.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Estonia now ranks 2nd in the UN E-Government Development Index.",
   "reasoning": "Rank and index match."
  },
  {
   "claim_id": "C041",
   "loglog_ids": [
    "5.4.4"
   ],
   "claim_text": "No major breaches in over 20 years despite constant cyber attacks.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "The system has had no major security breaches in over 20 years, despite constant cyber attacks.",
   "reasoning": "Negation, duration, and qualifier preserved."
  },
  {
   "claim_id": "C042",
   "loglog_ids": [
    "5.4.5"
   ],
   "claim_text": "X-Road is MIT-licensed open source, deployed in 20+ countries.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "It's open source (MIT license) and deployed in 20+ countries.",
   "reasoning": "License and deployment count match."
  },
  {
   "claim_id": "C043",
   "loglog_ids": [
    "5.4.6"
   ],
   "claim_text": "X-Road proves every-email-available infrastructure is technically feasible.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "X-Road proves the \"every email available up the chain\" infrastructure is technically feasible.",
   "reasoning": "Identical claim in SOURCE."
  },
  {
   "claim_id": "C044",
   "loglog_ids": [
    "5.4.7"
   ],
   "claim_text": "The technology is feasible; the bottleneck is will.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "The technology is not the bottleneck. The will is.",
   "reasoning": "Meaning preserved."
  },
  {
   "claim_id": "C045",
   "loglog_ids": [
    "5.5"
   ],
   "claim_text": "Brazil's 2004 Transparency Portal follows all federal money.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "### Brazil: Following the Money (2004)... publishes all federal spending.",
   "reasoning": "Year heading and all-federal-spending scope match."
  },
  {
   "claim_id": "C046",
   "loglog_ids": [
    "5.5.1"
   ],
   "claim_text": "It publishes contracts, transfers, salaries, travel, and credit-card transactions.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "contracts, transfers, salaries, travel expenses, and government credit card transactions.",
   "reasoning": "All five categories match SOURCE."
  },
  {
   "claim_id": "C047",
   "loglog_ids": [
    "5.5.2"
   ],
   "claim_text": "The portal receives over 20 million accesses per year.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "It receives over 20 million accesses per year.",
   "reasoning": "Verbatim figure."
  },
  {
   "claim_id": "C048",
   "loglog_ids": [
    "5.5.3"
   ],
   "claim_text": "Transparency Card sent 20+ million notifications via 430,000+ active cards.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "over 430,000 active cards, 20+ million notifications sent.",
   "reasoning": "Both counts match."
  },
  {
   "claim_id": "C049",
   "loglog_ids": [
    "5.5.4"
   ],
   "claim_text": "Journalists uncovered 60GB of hidden pension payments spanning 27 years.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "they uncovered 60GB of hidden pension payment data going back 27 years.",
   "reasoning": "Amount and span match."
  },
  {
   "claim_id": "C050",
   "loglog_ids": [
    "5.5.5"
   ],
   "claim_text": "Give citizens CEO tools and they find the fraud.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "This is what happens when you give citizens the tools to be CEOs: they find the fraud.",
   "reasoning": "Restatement preserving meaning."
  },
  {
   "claim_id": "C051",
   "loglog_ids": [
    "5.6"
   ],
   "claim_text": "New Zealand publishes cabinet papers by default since 2019.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Since 2019, New Zealand has proactively published all Cabinet papers and minutes online.",
   "reasoning": "Year, actor, and default publishing match."
  },
  {
   "claim_id": "C052",
   "loglog_ids": [
    "5.6.1"
   ],
   "claim_text": "All papers and minutes appear online within 30 business days.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "all Cabinet papers and minutes online within 30 business days of decisions being made.",
   "reasoning": "Window and scope match."
  },
  {
   "claim_id": "C053",
   "loglog_ids": [
    "5.6.2"
   ],
   "claim_text": "Cabinet deliberations are typically the world's most protected government information.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "cabinet deliberations are typically the most protected category of government information anywhere in the world.",
   "reasoning": "Hedge 'typically' and superlative preserved."
  },
  {
   "claim_id": "C054",
   "loglog_ids": [
    "5.6.3"
   ],
   "claim_text": "Government has not halted; ministers still deliberate; citizens see why.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "The government has not ground to a halt. Ministers have not stopped deliberating. What has changed is that citizens can see why.",
   "reasoning": "All three negations and the affirmative claim preserved."
  },
  {
   "claim_id": "C055",
   "loglog_ids": [
    "5.7"
   ],
   "claim_text": "Taiwan's vTaiwan crowdsources laws through consensus-finding deliberation.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Taiwan's vTaiwan platform uses Pol.is to let citizens participate in policy deliberation... surfaces statements that find cross-group consensus.",
   "reasoning": "Actor, method, and consensus mechanism match."
  },
  {
   "claim_id": "C056",
   "loglog_ids": [
    "5.7.1"
   ],
   "claim_text": "Pol.is takes agree-disagree votes with no replies, surfacing cross-group consensus.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "vote agree or disagree (no replies allowed - this prevents flame wars), and an algorithm surfaces statements that find cross-group consensus.",
   "reasoning": "Voting mode, no-replies rule, and consensus surfacing all present."
  },
  {
   "claim_id": "C057",
   "loglog_ids": [
    "5.7.2"
   ],
   "claim_text": "By 2018, 26 issues processed; 80% led to government action.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "By 2018, 26 issues had been processed, and 80% led to government action.",
   "reasoning": "Year, count, and percentage match exactly."
  },
  {
   "claim_id": "C058",
   "loglog_ids": [
    "5.7.3"
   ],
   "claim_text": "Participation is downstream of transparency, not core transparency itself.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "This isn't core transparency - it's what becomes possible downstream of transparency.",
   "reasoning": "Negation and downstream framing preserved."
  },
  {
   "claim_id": "C059",
   "loglog_ids": [
    "6"
   ],
   "claim_text": "Secret programs recur as illegal; secret oversight reliably fails to catch them.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "a recurring pattern in which government programs, shielded by secrecy, are later revealed to be illegal or built on lies... secret oversight reliably fails to prevent illegal secret programs",
   "reasoning": "Source asserts the recurring illegality pattern and reliable oversight failure. Dropped 'or built on lies' is harmless compression."
  },
  {
   "claim_id": "C060",
   "loglog_ids": [
    "6.1"
   ],
   "claim_text": "In 1971 Pentagon Papers showed government knew Vietnam was unwinnable while publicly claiming progress.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "In 1971, the Pentagon Papers revealed that the US government knew the Vietnam War was unwinnable while publicly claiming progress.",
   "reasoning": "Loglog restates the source sentence with year, actor, and claim intact."
  },
  {
   "claim_id": "C061",
   "loglog_ids": [
    "6.2"
   ],
   "claim_text": "Media, Pennsylvania break-in exposed COINTELPRO's illegal surveillance and disruption.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "activists broke into an FBI office in Media, Pennsylvania, and exposed COINTELPRO - a program of illegal surveillance, infiltration, and disruption",
   "reasoning": "Location, target, and program attributes match the source exactly."
  },
  {
   "claim_id": "C062",
   "loglog_ids": [
    "6.3"
   ],
   "claim_text": "COINTELPRO targeted civil rights leaders and political dissidents.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "targeting civil rights leaders and political dissidents",
   "reasoning": "Direct restatement of the source's target list."
  },
  {
   "claim_id": "C063",
   "loglog_ids": [
    "6.4"
   ],
   "claim_text": "In 2013 Snowden revealed bulk metadata collection from millions of Americans, PRISM, and leader surveillance.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "In 2013, Edward Snowden leaked classified documents revealing the NSA was bulk-collecting phone metadata from millions of Americans... through PRISM, and surveilling foreign leaders",
   "reasoning": "Year, actor, bulk collection, PRISM, and foreign-leader surveillance match the source."
  },
  {
   "claim_id": "C064",
   "loglog_ids": [
    "6.5"
   ],
   "claim_text": "Each disclosure was predicted catastrophic yet revealed illegality, unconstitutionality, or deliberate deception.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "In each case, the government predicted catastrophe from disclosure. In each case, the programs turned out to be illegal, unconstitutional, or based on deliberate deception",
   "reasoning": "The paired source sentences directly assert both the catastrophe prediction and the revealed outcomes."
  },
  {
   "claim_id": "C065",
   "loglog_ids": [
    "6.6"
   ],
   "claim_text": "In September 2020 the Ninth Circuit ruled bulk collection illegal, possibly unconstitutional.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "In September 2020, the US Ninth Circuit Court of Appeals ruled that the NSA's bulk phone record collection was illegal and possibly unconstitutional.",
   "reasoning": "Court, date, and both qualifiers match the source."
  },
  {
   "claim_id": "C066",
   "loglog_ids": [
    "6.7"
   ],
   "claim_text": "The court required FISA relevance to a particular authorized investigation.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "the government failed to satisfy FISA's requirement to show \"relevance to a particular authorized investigation.\"",
   "reasoning": "Quoted FISA requirement is reproduced accurately."
  },
  {
   "claim_id": "C067",
   "loglog_ids": [
    "6.8"
   ],
   "claim_text": "Stone found no evidence bulk collection stopped any terror attacks.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Geoffrey R. Stone, found \"no evidence that the bulk collection of phone data had stopped any terror attacks.\"",
   "reasoning": "The finding and attribution to Stone match the source quote."
  },
  {
   "claim_id": "C068",
   "loglog_ids": [
    "6.9"
   ],
   "claim_text": "The NSA abandoned the program in 2018: it no longer made sense.",
   "claim_type": "number_or_date",
   "verdict": "Partially supported",
   "severity": "Minor",
   "evidence_quote": "The NSA itself reportedly abandoned the program in 2018, telling the White House it \"no longer made sense.\"",
   "reasoning": "Node states as flat fact what source hedges with 'reportedly', dropping the attribution qualifier."
  },
  {
   "claim_id": "C069",
   "loglog_ids": [
    "6.10"
   ],
   "claim_text": "FISA courts, committees, and inspectors general failed inside the secrecy structure.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "The FISA court, congressional intelligence committees, and inspectors general all existed. They failed because they operated inside the secrecy structure",
   "reasoning": "All three oversight bodies and the failure cause match the source."
  },
  {
   "claim_id": "C070",
   "loglog_ids": [
    "6.11"
   ],
   "claim_text": "Secret oversight can be captured, co-opted, or worn down institutionally.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Oversight that is itself secret is oversight that can be captured, co-opted, or simply worn down by institutional pressure.",
   "reasoning": "Node reproduces the source's three mechanisms and the 'can' hedge."
  },
  {
   "claim_id": "C071",
   "loglog_ids": [
    "6.12"
   ],
   "claim_text": "The 2015 USA FREEDOM Act first reined in NSA spying in over 30 years.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "The USA FREEDOM Act (2015) became the first legislation to rein in NSA spying in over 30 years.",
   "reasoning": "Year, statute, and the 30-year first characterize the source verbatim."
  },
  {
   "claim_id": "C072",
   "loglog_ids": [
    "6.13"
   ],
   "claim_text": "It ended bulk metadata collection and required releasing significant FISC opinions.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "It ended bulk collection of phone metadata and required the Foreign Intelligence Surveillance Court to release significant opinions.",
   "reasoning": "Both effects match the source; FISC is the source's named court."
  },
  {
   "claim_id": "C073",
   "loglog_ids": [
    "6.14"
   ],
   "claim_text": "The tech sector adopted transparency reporting on data requests.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "The tech sector adopted transparency reporting on government data requests.",
   "reasoning": "Direct restatement of the source claim."
  },
  {
   "claim_id": "C074",
   "loglog_ids": [
    "6.15"
   ],
   "claim_text": "HTTPS became default on most websites.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "HTTPS encryption became the default on most websites.",
   "reasoning": "Verbatim match including the 'most websites' scope."
  },
  {
   "claim_id": "C075",
   "loglog_ids": [
    "6.16"
   ],
   "claim_text": "The EU's GDPR was accelerated by the revelations.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "The EU's GDPR was accelerated by the revelations.",
   "reasoning": "Direct restatement of the causal claim."
  },
  {
   "claim_id": "C076",
   "loglog_ids": [
    "6.17"
   ],
   "claim_text": "Operational harm is genuinely uncertain; illegality is not.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Whether these disclosures caused operational harm is genuinely uncertain... But the legality question is not uncertain. The programs were illegal.",
   "reasoning": "Node preserves both the uncertainty and its contrast with settled illegality."
  },
  {
   "claim_id": "C077",
   "loglog_ids": [
    "6.18"
   ],
   "claim_text": "Snowden is the symptom of absent designed-in transparency, not the solution.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Snowden is not the solution. Snowden is the symptom of a system where the only alternative to permanent secrecy is uncontrolled disclosure.",
   "reasoning": "Node keeps both negations and maps 'absence of a model' to designed-in transparency."
  },
  {
   "claim_id": "C078",
   "loglog_ids": [
    "6.19"
   ],
   "claim_text": "Designed-in traceability would surface illegality early without bulk-leak damage.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Designed-in transparency - where citizens can trace decisions by default - would have made the illegal programs visible before they scaled, without the collateral damage of a bulk leak.",
   "reasoning": "Early visibility and avoided bulk-leak damage match the source claim closely."
  },
  {
   "claim_id": "C079",
   "loglog_ids": [
    "7"
   ],
   "claim_text": "Ten objections follow, some power-protecting, some genuinely concerned; each gets honest engagement.",
   "claim_type": "meta",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Some come from officials protecting their power. But some come from citizens with genuine concerns. These deserve honest engagement.",
   "reasoning": "Source names both objection sources and promises honest engagement; ten subsequent headings enumerate ten objections."
  },
  {
   "claim_id": "C080",
   "loglog_ids": [
    "7.1"
   ],
   "claim_text": "Privacy objection: transparency will violate my privacy.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "### \"My Privacy Will Be Violated\"",
   "reasoning": "Matches the source heading naming the privacy objection."
  },
  {
   "claim_id": "C081",
   "loglog_ids": [
    "7.1.1"
   ],
   "claim_text": "2019 Pew: 66% fear collection, 64% fear use, 6% very confident.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "66% of Americans are concerned about government data collection, and 64% are concerned about how the government uses their data. Only 6% are \"very confident\"",
   "reasoning": "All three percentages and the 2019 Pew attribution match the source exactly."
  },
  {
   "claim_id": "C082",
   "loglog_ids": [
    "7.1.2"
   ],
   "claim_text": "A 2000 ABC poll: 86% said agencies should not publish such records online.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "2000 ABC News poll ... 86% said government agencies should *not* make public records ... available online.",
   "reasoning": "Date, percentage, and the negation about publishing records online all match."
  },
  {
   "claim_id": "C083",
   "loglog_ids": [
    "7.1.3"
   ],
   "claim_text": "Polls fear citizen data held by government, not visible government decisions.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "fear about *citizen data* held by government. Not fear about *government decisions* being visible to citizens.",
   "reasoning": "Direct restatement of the source's distinction, including the negation."
  },
  {
   "claim_id": "C084",
   "loglog_ids": [
    "7.1.4"
   ],
   "claim_text": "Quarterly-report review differs from publishing employee health records.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "The CEO reviewing quarterly reports is not the same as the CEO publishing employee health records.",
   "reasoning": "Paraphrase preserves the source's comparison and negation."
  },
  {
   "claim_id": "C085",
   "loglog_ids": [
    "7.1.5"
   ],
   "claim_text": "$50 million infrastructure-allocation transparency needs no neighbor's personal data.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "allocate $50 million in infrastructure spending. It does not mean: \"Here is the personal information of every citizen...\"",
   "reasoning": "Amount and the contrast with personal data match the source."
  },
  {
   "claim_id": "C086",
   "loglog_ids": [
    "7.1.6"
   ],
   "claim_text": "Bundled record systems should be separated, not kept wholly secret.",
   "claim_type": "recommendation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "the solution is to separate them, not to keep everything secret.",
   "reasoning": "Direct restatement preserving the separation recommendation and negation."
  },
  {
   "claim_id": "C087",
   "loglog_ids": [
    "7.2"
   ],
   "claim_text": "Objection: if every action is public, deliberation dies and processes paralyze.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "if every action is public, deliberation becomes impossible. Officials will be afraid to propose ideas. Processes will be paralyzed.",
   "reasoning": "Tracks the source's stated fear about deliberation and paralysis."
  },
  {
   "claim_id": "C088",
   "loglog_ids": [
    "7.2.1"
   ],
   "claim_text": "Cambridge found EU transparency-deliberation tension; IMF called government a friction-forcing fortress.",
   "claim_type": "name_or_entity",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "A Cambridge study ... found tension between transparent deliberation and efficient decision-making. An IMF analysis ... \"is not a sports car - it's a fortress\"",
   "reasoning": "Both attributions and characterizations match the source."
  },
  {
   "claim_id": "C089",
   "loglog_ids": [
    "7.2.2"
   ],
   "claim_text": "IMF: friction forces accountability and catches errors before harm.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "\"friction forces accountability\" and \"catches errors before they cause harm.\"",
   "reasoning": "Both quoted phrases reproduce the source verbatim."
  },
  {
   "claim_id": "C090",
   "loglog_ids": [
    "7.2.3"
   ],
   "claim_text": "Robodebt: 470,000 incorrect notices and a $1.8 billion settlement.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "470,000 incorrect debt notices and a $1.8 billion settlement.",
   "reasoning": "Numbers and entity match; dropping the word debt is harmless compression."
  },
  {
   "claim_id": "C091",
   "loglog_ids": [
    "7.2.4"
   ],
   "claim_text": "This confuses decision speed with decision documentation.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "this concern confuses two things: the speed of decision-making and the documentation of decision-making.",
   "reasoning": "Identical meaning to the source's distinction."
  },
  {
   "claim_id": "C092",
   "loglog_ids": [
    "7.2.5"
   ],
   "claim_text": "Document at current speed; fix burdensome systems, keep accountability.",
   "claim_type": "recommendation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "documenting what happens at the current speed ... If documentation is burdensome, you improve the documentation systems - you don't abandon accountability.",
   "reasoning": "Preserves both the documentation-at-current-speed point and the fix-systems recommendation."
  },
  {
   "claim_id": "C093",
   "loglog_ids": [
    "7.2.6"
   ],
   "claim_text": "CEOs demand documented work, not slower work.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "The CEO doesn't demand employees work slower. The CEO demands employees document their work.",
   "reasoning": "Direct restatement preserving the negation about speed."
  },
  {
   "claim_id": "C094",
   "loglog_ids": [
    "7.2.7"
   ],
   "claim_text": "New Zealand's 30-day cabinet papers halted nothing; reasoning stands verifiable.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "New Zealand publishes cabinet papers within 30 days. Their government hasn't ground to a halt ... citizens can verify whether the reasoning was sound.",
   "reasoning": "30-day figure and both consequences match this source passage."
  },
  {
   "claim_id": "C095",
   "loglog_ids": [
    "7.2.8"
   ],
   "claim_text": "Opacity makes decisions unaccountable random walks, not better ones.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "opacity doesn't make decisions *better* - it just makes them *unaccountable* ... Nobody notices the random walk",
   "reasoning": "Restates the source's contrast and random-walk image with the negation intact."
  },
  {
   "claim_id": "C096",
   "loglog_ids": [
    "7.2.9"
   ],
   "claim_text": "Documented consistency pressure prevents reversals and speeds decisions long-term.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Transparency creates pressure for logical consistency, which in the long run actually improves decision-making speed by preventing costly reversals",
   "reasoning": "Preserves the causal claim linking consistency pressure to fewer reversals and speed."
  },
  {
   "claim_id": "C097",
   "loglog_ids": [
    "7.3"
   ],
   "claim_text": "Objection: diplomacy requires secrecy.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "### \"Diplomacy Requires Secrecy\"",
   "reasoning": "Matches the source heading naming the diplomacy objection."
  },
  {
   "claim_id": "C098",
   "loglog_ids": [
    "7.3.1"
   ],
   "claim_text": "Conceded: the most legitimate concern, deserving nuance.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "This is the most legitimate concern, and it deserves nuance.",
   "reasoning": "Direct restatement of the concession."
  },
  {
   "claim_id": "C099",
   "loglog_ids": [
    "7.3.2"
   ],
   "claim_text": "JCPOA began in 2012 via Sullivan's secret Oman backchannel.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "negotiations began in 2012 with a secret backchannel. Jake Sullivan secretly traveled to Oman",
   "reasoning": "Year, name Jake Sullivan, and Oman backchannel all match."
  },
  {
   "claim_id": "C100",
   "loglog_ids": [
    "7.3.3"
   ],
   "claim_text": "Camp David 1978 and Cold War backchannels likewise needed private space.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "The Camp David Accords (1978) similarly required private space for compromise. Cold War backchannels",
   "reasoning": "1978 attribution and the private-space point match."
  },
  {
   "claim_id": "C101",
   "loglog_ids": [
    "7.3.4"
   ],
   "claim_text": "Democratic dilemma: secrecy enables flexibility, but barren without consent.",
   "claim_type": "definition",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "\"negotiations can be flexible and successful only if they are kept secret, but they will be barren without popular consent.\"",
   "reasoning": "Faithful compression of the quoted democratic dilemma."
  },
  {
   "claim_id": "C102",
   "loglog_ids": [
    "7.3.5"
   ],
   "claim_text": "CEOs allow confidential negotiation, then demand full disclosure afterward.",
   "claim_type": "recommendation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "A CEO may authorize a negotiation team to keep details confidential *during* the negotiation. But the CEO expects full disclosure once it concludes.",
   "reasoning": "Preserves both the during-negotiation confidentiality and post-conclusion disclosure."
  },
  {
   "claim_id": "C103",
   "loglog_ids": [
    "7.3.6"
   ],
   "claim_text": "Disclose afterward what was offered, conceded, why, and alternatives.",
   "claim_type": "recommendation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "what was offered, what was conceded, why, what alternatives were considered.",
   "reasoning": "Lists exactly the source's disclosure items."
  },
  {
   "claim_id": "C104",
   "loglog_ids": [
    "7.3.7"
   ],
   "claim_text": "Temporary secrecy during talks is acceptable; permanent secrecy is not.",
   "claim_type": "recommendation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "*Temporary operational secrecy during active negotiations* may be acceptable. *Permanent secrecy about what was decided and why* is not.",
   "reasoning": "Reproduces the source's acceptability distinction and negation."
  },
  {
   "claim_id": "C105",
   "loglog_ids": [
    "7.3.8"
   ],
   "claim_text": "Release full documentation 30-90 days after conclusion for evaluation.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Full documentation released after conclusion (e.g., 30-90 days) ... Citizens can evaluate whether negotiators served their interests",
   "reasoning": "30-90 day window and evaluation purpose match."
  },
  {
   "claim_id": "C106",
   "loglog_ids": [
    "7.3.9"
   ],
   "claim_text": "Foreign-refusal arguments let non-principals veto citizens' oversight.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "It makes citizens' oversight contingent on foreign governments' preferences. But foreign governments are not the principals here.",
   "reasoning": "Captures the source's point that foreign preferences would condition citizens' oversight."
  },
  {
   "claim_id": "C107",
   "loglog_ids": [
    "7.3.10"
   ],
   "claim_text": "Foreign governments are not the principals; citizens are.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "foreign governments are not the principals here. You are.",
   "reasoning": "Direct restatement preserving the negation."
  },
  {
   "claim_id": "C108",
   "loglog_ids": [
    "7.4"
   ],
   "claim_text": "Objection: special interests benefit more than ordinary citizens.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "### \"Special Interests Will Benefit More Than Ordinary Citizens\"",
   "reasoning": "Matches the source heading naming the special-interest objection."
  },
  {
   "claim_id": "C109",
   "loglog_ids": [
    "7.4.1"
   ],
   "claim_text": "Conceded: empirically grounded and worth taking seriously.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "This is an empirically grounded concern that you should take seriously.",
   "reasoning": "Direct restatement of the concession."
  },
  {
   "claim_id": "C110",
   "loglog_ids": [
    "7.4.2"
   ],
   "claim_text": "Harden and Kirkland studied all 50 legislatures over multiple decades.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "studied all 50 US state legislatures over multiple decades.",
   "reasoning": "Count and scope match exactly."
  },
  {
   "claim_id": "C111",
   "loglog_ids": [
    "7.4.3"
   ],
   "claim_text": "Notre Dame-Virginia scholars' Illusion of Accountability compares open versus closed meetings using surveys versus outcomes.",
   "claim_type": "name_or_entity",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Jeff Harden (University of Notre Dame) and Justin Kirkland (University of Virginia) ... *The Illusion of Accountability* ... compared states with open versus closed legislative meetings, using survey data on policy preferences versus actual policy outcomes.",
   "reasoning": "Affiliations, book title, and method all match the source."
  },
  {
   "claim_id": "C112",
   "loglog_ids": [
    "7.4.4"
   ],
   "claim_text": "More lobbyists register and donate, yet policy-opinion correlation stays same open or closed.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "more lobbying groups register ... Lobbyists donate more to incumbents. And public policy's correlation with public opinion is *the same* whether meetings are open or closed.",
   "reasoning": "All three findings match the source."
  },
  {
   "claim_id": "C113",
   "loglog_ids": [
    "7.4.5"
   ],
   "claim_text": "Harden: the laws improve representation for unrepresentative interest groups, not citizens.",
   "claim_type": "name_or_entity",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "\"The laws don't make citizen representation better, they make it better for interest groups, which aren't representative of the general public.\"",
   "reasoning": "Faithful to the quoted Harden statement and its negation."
  },
  {
   "claim_id": "C114",
   "loglog_ids": [
    "7.4.6"
   ],
   "claim_text": "Arnold (1990): open markups advantage organized interests over inattentive citizens.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Princeton's Douglas Arnold (1990) observed ... \"Open markup sessions often give organized interests a powerful advantage over inattentive citizens.\"",
   "reasoning": "Year, name, and quoted claim all match."
  },
  {
   "claim_id": "C115",
   "loglog_ids": [
    "7.4.7"
   ],
   "claim_text": "Ireland 2024: 569 participants; lobbying transparency did not raise trust.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "2024 survey experiment in Ireland ... with 569 participants found that citizens exposed to lobbying information don't develop more positive evaluations of trust",
   "reasoning": "Year, count, and the negative finding match."
  },
  {
   "claim_id": "C116",
   "loglog_ids": [
    "7.4.8"
   ],
   "claim_text": "Asymmetry is the problem: paid monitors versus busy citizens.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "the *asymmetry* is the problem. Lobbyists are paid to monitor government.",
   "reasoning": "Direct restatement of the source's asymmetry point."
  },
  {
   "claim_id": "C117",
   "loglog_ids": [
    "7.4.9"
   ],
   "claim_text": "Lobbyists wield staff, expertise, and capacity; citizens have jobs and families.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "They have professional staff, legal expertise, and organizational capacity. Citizens have jobs, families, and finite attention.",
   "reasoning": "Faithful list of the source's stated asymmetries."
  },
  {
   "claim_id": "C118",
   "loglog_ids": [
    "7.4.10"
   ],
   "claim_text": "Build citizen capacity: auditors, watchdogs, journalism, civic tech.",
   "claim_type": "recommendation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "hire auditors, create oversight committees ... fund watchdog organizations, support investigative journalism, build civic technology.",
   "reasoning": "Matches the source's capacity-building recommendations."
  },
  {
   "claim_id": "C119",
   "loglog_ids": [
    "7.4.11"
   ],
   "claim_text": "Brazil's Fiquem Sabendo files 2,000-3,000 FOI requests yearly for citizens.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Brazil's Fiquem Sabendo files 2,000-3,000 FOI requests per year on behalf of citizens.",
   "reasoning": "Name and request count match exactly."
  },
  {
   "claim_id": "C120",
   "loglog_ids": [
    "7.4.12"
   ],
   "claim_text": "A robust and competitive electoral environment is the real key.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "\"the real key to quality representation is a robust and competitive electoral environment.\"",
   "reasoning": "Direct quotation with correct attribution to Harden and Kirkland."
  },
  {
   "claim_id": "C121",
   "loglog_ids": [
    "7.4.13"
   ],
   "claim_text": "Opacity guarantees no accountability; transparency makes it possible.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Opacity *guarantees* no accountability. Transparency at least makes accountability *possible*.",
   "reasoning": "Reproduces the source's contrast and negation."
  },
  {
   "claim_id": "C122",
   "loglog_ids": [
    "7.4.14"
   ],
   "claim_text": "Build usage capacity rather than reducing information.",
   "claim_type": "recommendation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "The answer is to build capacity, not reduce information.",
   "reasoning": "Direct restatement preserving the not-reduce-information negation."
  },
  {
   "claim_id": "C123",
   "loglog_ids": [
    "7.5"
   ],
   "claim_text": "Objection: public officials will face harassment.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "### \"Public Officials Will Be Harassed\"",
   "reasoning": "Matches the source heading naming the harassment objection."
  },
  {
   "claim_id": "C124",
   "loglog_ids": [
    "7.5.1"
   ],
   "claim_text": "Conceded: real, documented, and growing.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "This concern is real, documented, and growing.",
   "reasoning": "Direct restatement of the concession."
  },
  {
   "claim_id": "C125",
   "loglog_ids": [
    "7.5.2"
   ],
   "claim_text": "Brennan surveyed 735 local election officials, February-March 2024, weighted by region and jurisdiction size, margin ±3%.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "surveyed 735 local election officials between February and March 2024 (weighted by region and jurisdiction size, margin of error ±3%)",
   "reasoning": "All figures and methodology details match the source."
  },
  {
   "claim_id": "C126",
   "loglog_ids": [
    "7.5.3"
   ],
   "claim_text": "38% threatened; over half fear for colleagues; over 1 in 4 fear assault.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "38% experienced threats ... More than half are concerned about the safety of colleagues ... More than 1 in 4 worry about being assaulted",
   "reasoning": "All three statistics match the source's survey list."
  },
  {
   "claim_id": "C127",
   "loglog_ids": [
    "7.5.4"
   ],
   "claim_text": "34% know someone who resigned, up from 22% in 2023.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "34% know someone who resigned due to safety concerns (up from 22% in 2023)",
   "reasoning": "Both percentages and the 2023 comparison match."
  },
  {
   "claim_id": "C128",
   "loglog_ids": [
    "7.5.5"
   ],
   "claim_text": "61% of the threatened were threatened in person or by phone.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "61% of those threatened received threats in person or by phone",
   "reasoning": "Percentage and channel detail match the source."
  },
  {
   "claim_id": "C129",
   "loglog_ids": [
    "7.5.6"
   ],
   "claim_text": "2024: doxxing and swatting evolved into sophisticated technology-enabled harassment tools.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "reported in 2024 that doxxing and swatting have \"evolved into sophisticated, technology-enabled tools of harassment,\"",
   "reasoning": "Year and quoted characterization match the NAAG report."
  },
  {
   "claim_id": "C130",
   "loglog_ids": [
    "7.5.7"
   ],
   "claim_text": "AI and automated scraping intensify scale, precision, and anonymity.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "AI and automated data scraping intensifying \"the scale, precision, and anonymity\" of attacks.",
   "reasoning": "Matches the source's quoted list and agents."
  },
  {
   "claim_id": "C131",
   "loglog_ids": [
    "7.5.8"
   ],
   "claim_text": "Since 2022, 22 states passed protections for election officials.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Since 2022, 22 states have passed protections for election officials.",
   "reasoning": "Year and state count match exactly."
  },
  {
   "claim_id": "C132",
   "loglog_ids": [
    "7.5.9"
   ],
   "claim_text": "Publish who decided what and why; protect addresses, families, schedules.",
   "claim_type": "recommendation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Transparency of decisions (who decided what, based on what reasoning) should be public. Personal information of officials (home addresses, family members, daily schedules) should be protected.",
   "reasoning": "Preserves both the public-decisions and protected-details distinction."
  },
  {
   "claim_id": "C133",
   "loglog_ids": [
    "7.5.10"
   ],
   "claim_text": "CEOs review work product, not employees' home addresses.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "The CEO does not publish employees' home addresses to angry customers. Accountability for work product is not the same as personal vulnerability.",
   "reasoning": "Faithful to the source's distinction and negation."
  },
  {
   "claim_id": "C134",
   "loglog_ids": [
    "7.5.11"
   ],
   "claim_text": "Current harassment feeds on opacity-bred fraud conspiracies.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "much of the *current* harassment stems from *lack* of transparency. Election officials are harassed because of conspiracy theories about fraud.",
   "reasoning": "Preserves the source's causal link between opacity and harassment."
  },
  {
   "claim_id": "C135",
   "loglog_ids": [
    "7.5.12"
   ],
   "claim_text": "Documented audits, custody chains, and counts would starve conspiracies.",
   "claim_type": "causal_link",
   "verdict": "Partially supported",
   "severity": "Minor",
   "evidence_quote": "the conspiracy theories would have less room to grow",
   "reasoning": "Source says conspiracies would have less room to grow; node strengthens to starve, an absolute elimination claim."
  },
  {
   "claim_id": "C136",
   "loglog_ids": [
    "7.5.13"
   ],
   "claim_text": "Protect individuals more while making processes more transparent.",
   "claim_type": "recommendation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "better protection for individuals, combined with *more* transparency about processes.",
   "reasoning": "Direct restatement of the source's dual recommendation."
  },
  {
   "claim_id": "C137",
   "loglog_ids": [
    "7.6"
   ],
   "claim_text": "Objection: national security forbids transparency.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "### \"National Security!\"",
   "reasoning": "Matches the source heading for the national security objection."
  },
  {
   "claim_id": "C138",
   "loglog_ids": [
    "7.6.1"
   ],
   "claim_text": "This objection is used most and scrutinized least.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "This is the objection that gets used most often and scrutinized least.",
   "reasoning": "Direct restatement of the source."
  },
  {
   "claim_id": "C139",
   "loglog_ids": [
    "7.6.2"
   ],
   "claim_text": "Chicago 2020-2022: roughly 60% call intelligence vital.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "surveyed Americans in 2020 and 2022 and found that roughly 60% agree the intelligence community \"plays a vital role\"",
   "reasoning": "Years, percentage, and attribution match."
  },
  {
   "claim_id": "C140",
   "loglog_ids": [
    "7.6.3"
   ],
   "claim_text": "A majority say it could share more without harming effectiveness.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "a majority also agreed the IC \"could share more information with the American people without compromising effectiveness.\"",
   "reasoning": "Faithful to the quoted survey result."
  },
  {
   "claim_id": "C141",
   "loglog_ids": [
    "7.6.4"
   ],
   "claim_text": "Civil-liberties threat perception rose from 12% in 2021 to 17% in 2022.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "rising (from 12% in 2021 to 17% in 2022)",
   "reasoning": "Both percentages and years match exactly."
  },
  {
   "claim_id": "C142",
   "loglog_ids": [
    "7.6.5"
   ],
   "claim_text": "Brennan: far too much is classified; secrecy undermines democratic self-government.",
   "claim_type": "name_or_entity",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "\"federal officials and outside experts agree that far too much information is classified.\" And: \"excessive secrecy ... undermines the basic functions of democratic self-government.\"",
   "reasoning": "Both quoted Brennan Center statements match."
  },
  {
   "claim_id": "C143",
   "loglog_ids": [
    "7.6.6"
   ],
   "claim_text": "SIPRI: military transparency builds inter-state trust and prevents waste.",
   "claim_type": "name_or_entity",
   "verdict": "Partially supported",
   "severity": "Minor",
   "evidence_quote": "\"transparency in military matters is generally considered essential for building trust between states\" and \"can help prevent wasteful spending.\"",
   "reasoning": "Node states absolutes; source hedges with generally considered, essential, and can help prevent."
  },
  {
   "claim_id": "C144",
   "loglog_ids": [
    "7.6.7"
   ],
   "claim_text": "Snowden proved catastrophe predictions wrong and programs illegal.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "The government predicted catastrophe. Independent research found minimal impact. The court found the programs *illegal*.",
   "reasoning": "Node summarizes the source's claim that predicted catastrophe did not materialize and programs were illegal."
  },
  {
   "claim_id": "C145",
   "loglog_ids": [
    "7.6.8"
   ],
   "claim_text": "Independent research found minimal impact; reforms improved civil liberties.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Independent research found minimal impact. ... The reforms improved civil liberties.",
   "reasoning": "Direct restatement of both source statements."
  },
  {
   "claim_id": "C146",
   "loglog_ids": [
    "7.6.9"
   ],
   "claim_text": "Flip the burden: transparent by default, secrecy needs proof.",
   "claim_type": "recommendation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "almost everything is transparent by default, and officials must prove their need for secrecy.",
   "reasoning": "Faithful to the source's proposed burden reversal."
  },
  {
   "claim_id": "C147",
   "loglog_ids": [
    "7.6.10"
   ],
   "claim_text": "Temporary classification fits active operations; strategy, doctrine, budgets, procurement, and rules stay open.",
   "claim_type": "recommendation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "The CEO may authorize temporary classification during an operation. ... Strategy, doctrine, budget, procurement, rules of engagement should always be transparent.",
   "reasoning": "Matches the temporary-classification exception and open-by-default list."
  },
  {
   "claim_id": "C148",
   "loglog_ids": [
    "7.6.11"
   ],
   "claim_text": "The label hides embarrassment, illegality, incompetence, and corruption.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "The \"national security\" label is overused to hide embarrassing decisions, illegal activities (as Snowden revealed), bureaucratic incompetence, and corruption.",
   "reasoning": "Faithful compression of the source's list."
  },
  {
   "claim_id": "C149",
   "loglog_ids": [
    "7.6.12"
   ],
   "claim_text": "Officials under scrutiny set secrecy criteria: a conflict of interest.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Currently, the officials whose decisions might be scrutinized. That's a conflict of interest.",
   "reasoning": "Direct restatement of the source's conflict-of-interest point."
  },
  {
   "claim_id": "C150",
   "loglog_ids": [
    "7.7"
   ],
   "claim_text": "Objection: populists will weaponize transparency.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "### \"Populists Will Weaponize Transparency\"",
   "reasoning": "Matches the source heading naming the populism objection."
  },
  {
   "claim_id": "C151",
   "loglog_ids": [
    "7.7.1"
   ],
   "claim_text": "Conceded: sophisticated and research-backed.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "This is a sophisticated concern backed by real research.",
   "reasoning": "Direct restatement of the concession."
  },
  {
   "claim_id": "C152",
   "loglog_ids": [
    "7.7.2"
   ],
   "claim_text": "Kyle-Gultchin studied 43 democracies, 1990-2018, Polity IV at least 6, leaders journal-screened.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "studying populist governments in 43 democratic countries between 1990 and 2018 (leaders classified through academic journal screening, countries coded as democratic using Polity IV score ≥6)",
   "reasoning": "All figures and methodological details match."
  },
  {
   "claim_id": "C153",
   "loglog_ids": [
    "7.7.3"
   ],
   "claim_text": "Populists are 4x likelier to damage institutions: 23% versus 6%.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Populist governments are 4x more likely to damage democratic institutions (23% vs 6% of non-populists)",
   "reasoning": "Multiplier and both percentages match."
  },
  {
   "claim_id": "C154",
   "loglog_ids": [
    "7.7.4"
   ],
   "claim_text": "Countries fall 5 places on corruption perceptions; top-half starters fall 11.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Countries fall an average of 5 places ... Countries starting in the top half fall an average of 11 places",
   "reasoning": "Both figures match the source."
  },
  {
   "claim_id": "C155",
   "loglog_ids": [
    "7.7.5"
   ],
   "claim_text": "Venezuela dropped 83 places under Chávez.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "(Venezuela dropped 83 under Chávez)",
   "reasoning": "Country, figure, and leader match exactly."
  },
  {
   "claim_id": "C156",
   "loglog_ids": [
    "7.7.6"
   ],
   "claim_text": "Over 50% amended or rewrote constitutions; populists rule 6.5 versus 3 years.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Over 50% of populist leaders amended or rewrote constitutions ... Populists hold office twice as long ... (6.5 vs 3 years)",
   "reasoning": "Both the 50% figure and the 6.5 vs 3 years match."
  },
  {
   "claim_id": "C157",
   "loglog_ids": [
    "7.7.7"
   ],
   "claim_text": "Stanford: visibility-driven re-election tempts short-term populist policies.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "\"when re-election hinges on immediate visibility rather than long-term strategy, leaders may opt for populist policies\"",
   "reasoning": "Faithful compression of the quoted Stanford argument."
  },
  {
   "claim_id": "C158",
   "loglog_ids": [
    "7.7.8"
   ],
   "claim_text": "Sweden Democrats repurposed FOI and alternative media against elites.",
   "claim_type": "name_or_entity",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "the Sweden Democrats ... have \"strategically repurposed\" transparency mechanisms, using freedom of information ... while leveraging alternative media",
   "reasoning": "Party, mechanism, and media all match."
  },
  {
   "claim_id": "C159",
   "loglog_ids": [
    "7.7.9"
   ],
   "claim_text": "They expose scandals to erode trust in traditional elites.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "using freedom of information to expose scandals and erode trust in traditional elites",
   "reasoning": "Direct restatement of the source phrase."
  },
  {
   "claim_id": "C160",
   "loglog_ids": [
    "7.7.10"
   ],
   "claim_text": "Causality is backwards: populists damage democracy by reducing transparency.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "the causal story is backwards. The research shows populists *damage* democracy - and they do so by *reducing* transparency, not increasing it.",
   "reasoning": "Preserves the causal reversal and the not-increasing negation."
  },
  {
   "claim_id": "C161",
   "loglog_ids": [
    "7.7.11"
   ],
   "claim_text": "Cherry-picking works only while the full record stays hidden.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "This works precisely because *not everything* is visible. In a fully transparent system, selective leaking loses its power.",
   "reasoning": "Faithful to the source's visibility-dependent explanation."
  },
  {
   "claim_id": "C162",
   "loglog_ids": [
    "7.7.12"
   ],
   "claim_text": "Electoral cycles cause short-termism with or without transparency.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "the \"short-term thinking\" problem exists with or without transparency. Electoral cycles create short-term incentives regardless.",
   "reasoning": "Direct restatement of the source."
  },
  {
   "claim_id": "C163",
   "loglog_ids": [
    "7.7.13"
   ],
   "claim_text": "Documented long-term rationale makes unpopular-but-wise decisions defensible.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "An unpopular decision with documented reasoning is defensible.",
   "reasoning": "Direct restatement of the source."
  },
  {
   "claim_id": "C164",
   "loglog_ids": [
    "7.7.14"
   ],
   "claim_text": "Evaluating reasoning, not just outcomes, is populism's antidote.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Transparency enables evaluation of *reasoning*, not just outcomes. And that's the antidote to populism, not its enabler.",
   "reasoning": "Both negations and the antidote claim match."
  },
  {
   "claim_id": "C165",
   "loglog_ids": [
    "7.7.15"
   ],
   "claim_text": "CEOs want documented reasoning, not merely popular decisions.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "The CEO doesn't want employees to make only *popular* decisions. The CEO wants employees to make *documented* decisions with clear reasoning.",
   "reasoning": "Faithful restatement with the only-popular contrast preserved."
  },
  {
   "claim_id": "C166",
   "loglog_ids": [
    "7.8"
   ],
   "claim_text": "Objection: misinformation makes transparency pointless.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "### \"Misinformation Makes Transparency Pointless\"",
   "reasoning": "Matches the source heading naming the misinformation objection."
  },
  {
   "claim_id": "C167",
   "loglog_ids": [
    "7.8.1"
   ],
   "claim_text": "Harvard 2023: Canadian panel; COVID-19 false beliefs lower perceived transparency.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "study published in the Harvard Kennedy School Misinformation Review (2023, based on a Canadian panel survey) found that people who endorse false beliefs (specifically COVID-19 related) perceive government as *less* transparent",
   "reasoning": "Year, venue, sample, and finding all match."
  },
  {
   "claim_id": "C168",
   "loglog_ids": [
    "7.8.2"
   ],
   "claim_text": "This holds controlling for real transparency levels.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "This holds even when controlling for real transparency.",
   "reasoning": "Direct restatement."
  },
  {
   "claim_id": "C169",
   "loglog_ids": [
    "7.8.3"
   ],
   "claim_text": "Negative transparency perceptions cut voting, trust, and democratic satisfaction.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "negative transparency perceptions are associated with decline in voting intentions, trust, and satisfaction with democracy.",
   "reasoning": "Close paraphrase preserving the three associated declines."
  },
  {
   "claim_id": "C170",
   "loglog_ids": [
    "7.8.4"
   ],
   "claim_text": "Citizens prize transparency's idea but dislike disclosures' messy content.",
   "claim_type": "interpretation",
   "verdict": "Partially supported",
   "severity": "Minor",
   "evidence_quote": "citizens value the *idea* of transparency but may react negatively to the *content* of actual disclosures",
   "reasoning": "Source hedges with may react negatively; node states the dislike as settled fact."
  },
  {
   "claim_id": "C171",
   "loglog_ids": [
    "7.8.5"
   ],
   "claim_text": "So-why-bother does not follow from these findings.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "the conclusion drawn from them - \"so why bother?\" - doesn't follow.",
   "reasoning": "Direct restatement preserving the negation."
  },
  {
   "claim_id": "C172",
   "loglog_ids": [
    "7.8.6"
   ],
   "claim_text": "False beliefs drive perceived opacity, not the reverse.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "false beliefs lead to perceived non-transparency. It does *not* show: actual transparency leads to more false beliefs.",
   "reasoning": "Preserves both the causal direction and the negation."
  },
  {
   "claim_id": "C173",
   "loglog_ids": [
    "7.8.7"
   ],
   "claim_text": "Opacity enables false beliefs; secrecy vacuums breed speculation.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "opacity *enables* false beliefs ... Speculation flourishes where documentation doesn't exist.",
   "reasoning": "Faithful to both source claims."
  },
  {
   "claim_id": "C174",
   "loglog_ids": [
    "7.8.8"
   ],
   "claim_text": "Election conspiracies grow where processes stay opaque.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Election conspiracy theories grow precisely because *some* processes remain opaque.",
   "reasoning": "Direct restatement preserving the some qualifier's sense."
  },
  {
   "claim_id": "C175",
   "loglog_ids": [
    "7.8.9"
   ],
   "claim_text": "Full documentation gives checkable ground truth for false claims.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Transparency provides ground truth. If full documentation exists, false claims can be checked against reality.",
   "reasoning": "Direct restatement of the source."
  },
  {
   "claim_id": "C176",
   "loglog_ids": [
    "7.8.10"
   ],
   "claim_text": "Latent availability deters misconduct even without consumption.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Availability changes behavior even without consumption. The knowledge that the record exists deters misconduct.",
   "reasoning": "Matches the source's availability-deters-misconduct claim."
  },
  {
   "claim_id": "C177",
   "loglog_ids": [
    "7.8.11"
   ],
   "claim_text": "CEOs need not read every email to benefit from access.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "The CEO doesn't read every email but values that they *could*.",
   "reasoning": "Faithful restatement preserving the negation."
  },
  {
   "claim_id": "C178",
   "loglog_ids": [
    "7.8.12"
   ],
   "claim_text": "Persistent transparency builds trust through consistently matching reality.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Persistent, comprehensive transparency creates a verifiable track record. Trust emerges when the disclosed information consistently matches reality.",
   "reasoning": "Direct restatement of the trust-building mechanism."
  },
  {
   "claim_id": "C179",
   "loglog_ids": [
    "7.8.13"
   ],
   "claim_text": "Pair transparency with accessibility, explanation, and intermediary translators.",
   "claim_type": "recommendation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "accompanied by accessibility, explanation, and intermediaries (journalists, civic tech, educators) who translate raw data",
   "reasoning": "Matches the source's recommended accompaniments."
  },
  {
   "claim_id": "C180",
   "loglog_ids": [
    "7.9"
   ],
   "claim_text": "Objection: markets will be manipulated by early disclosures.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "### \"Markets Will Be Manipulated\"",
   "reasoning": "Matches the source heading naming the markets objection."
  },
  {
   "claim_id": "C181",
   "loglog_ids": [
    "7.9.1"
   ],
   "claim_text": "Trade positions and monetary deliberations invite trader exploitation.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "doesn't publishing its positions undermine the negotiation? ... couldn't traders exploit advance knowledge?",
   "reasoning": "Faithful restatement of the source's two rhetorical concerns."
  },
  {
   "claim_id": "C182",
   "loglog_ids": [
    "7.9.2"
   ],
   "claim_text": "Conceded: valid but narrow; answer is delayed, not permanent, secrecy.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "This concern is valid but narrow. The solution isn't permanent secrecy. It's time-delayed transparency.",
   "reasoning": "Preserves the concession and the not-permanent negation."
  },
  {
   "claim_id": "C183",
   "loglog_ids": [
    "7.9.3"
   ],
   "claim_text": "The Fed releases minutes in three weeks, transcripts in five years.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "The US Federal Reserve releases FOMC minutes with a three-week delay and full transcripts with a five-year delay.",
   "reasoning": "Delays and entity match."
  },
  {
   "claim_id": "C184",
   "loglog_ids": [
    "7.9.4"
   ],
   "claim_text": "TTIP failed amid backlash from citizens feeling excluded by secrecy.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "The EU's failed TTIP trade negotiations actually suffered from *too much* secrecy - public backlash grew partly because citizens felt excluded",
   "reasoning": "Faithful to the source, including the partly qualifier's sense."
  },
  {
   "claim_id": "C185",
   "loglog_ids": [
    "7.9.5"
   ],
   "claim_text": "All information goes public eventually; only timing is managed.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "all information eventually becomes public. Timing may be managed for specific categories",
   "reasoning": "Direct restatement of the source."
  },
  {
   "claim_id": "C186",
   "loglog_ids": [
    "7.9.6"
   ],
   "claim_text": "Monetary waits for implementation, trade for conclusion, procurement for award.",
   "claim_type": "recommendation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "monetary policy (delay until implementation), trade negotiations (delay until conclusion), procurement (delay until contract award)",
   "reasoning": "All three category delays match."
  },
  {
   "claim_id": "C187",
   "loglog_ids": [
    "7.9.7"
   ],
   "claim_text": "Procurement secrecy lets officials favor connected contractors.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "If bidding processes are opaque, officials can favor connected contractors with impunity.",
   "reasoning": "Faithful restatement of the source."
  },
  {
   "claim_id": "C188",
   "loglog_ids": [
    "7.9.8"
   ],
   "claim_text": "Brazil's contract sunlight specifically prevents procurement fraud.",
   "claim_type": "name_or_entity",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Brazil's Transparency Portal includes contract information specifically because sunlight in procurement prevents fraud.",
   "reasoning": "Direct restatement with correct entity."
  },
  {
   "claim_id": "C189",
   "loglog_ids": [
    "7.10"
   ],
   "claim_text": "Objection: those in power will never allow this.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "### \"Those in Power Will Never Allow This\"",
   "reasoning": "Matches the source heading naming the power objection."
  },
  {
   "claim_id": "C190",
   "loglog_ids": [
    "7.10.1"
   ],
   "claim_text": "That describes the political challenge, not a principled objection.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "This is the concern that isn't really an objection. It's a description of the political challenge.",
   "reasoning": "Direct restatement preserving both negations."
  },
  {
   "claim_id": "C191",
   "loglog_ids": [
    "7.10.2"
   ],
   "claim_text": "Iceland 2008: 950 citizens set values; 25-member politician-free council drafted.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "After the 2008 financial crisis, 950 randomly selected citizens identified constitutional values. A 25-person council (explicitly excluding politicians) drafted a new constitution",
   "reasoning": "Year, both counts, and the politician exclusion match."
  },
  {
   "claim_id": "C192",
   "loglog_ids": [
    "7.10.3"
   ],
   "claim_text": "3,600 social-media comments; unanimous council; two-thirds referendum approval.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "3,600 public comments via social media. The draft was approved unanimously by the council and by a two-thirds majority in a national referendum.",
   "reasoning": "All three details match."
  },
  {
   "claim_id": "C193",
   "loglog_ids": [
    "7.10.4"
   ],
   "claim_text": "Parliament refused to ratify the draft.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "And then the existing parliament refused to ratify it.",
   "reasoning": "Direct restatement."
  },
  {
   "claim_id": "C194",
   "loglog_ids": [
    "7.10.5"
   ],
   "claim_text": "OGP: 75 countries, 4,500+ commitments since 2011; one-third delayed for funding.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Open Government Partnership (75 countries, 4,500+ commitments since 2011) found that one-third of delayed commitments fail due to \"lack of funding and technical capacity.\"",
   "reasoning": "All figures and the funding cause match."
  },
  {
   "claim_id": "C195",
   "loglog_ids": [
    "7.10.6"
   ],
   "claim_text": "Coordination failures, weak support, and transitions kill the rest.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "\"poor institutional coordination, lack of political support, and discontinuity from one administration to another during political transitions.\"",
   "reasoning": "Faithful compression of the source's listed remaining causes."
  },
  {
   "claim_id": "C196",
   "loglog_ids": [
    "7.10.7"
   ],
   "claim_text": "Successor governments abandon predecessors' transparency promises.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "new governments abandon their predecessors' transparency promises.",
   "reasoning": "Direct restatement."
  },
  {
   "claim_id": "C197",
   "loglog_ids": [
    "7.10.8"
   ],
   "claim_text": "Conceded: opacity's beneficiaries will always resist.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Those who benefit from opacity ... will resist transparency. They will always resist.",
   "reasoning": "Direct restatement of the concession."
  },
  {
   "claim_id": "C198",
   "loglog_ids": [
    "7.10.9"
   ],
   "claim_text": "Threatening the powerful is the point, not a flaw.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "It's a statement that transparency threatens the powerful. Which is exactly the point.",
   "reasoning": "Direct restatement preserving the negation."
  },
  {
   "claim_id": "C199",
   "loglog_ids": [
    "7.10.10"
   ],
   "claim_text": "Sweden 1766, post-Watergate, and post-2008 Iceland opened reform windows.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Sweden 1766 ... Post-Watergate US: scandal created a window for reform. Post-2008 Iceland: financial crisis created demand",
   "reasoning": "All three precedents match the source list."
  },
  {
   "claim_id": "C200",
   "loglog_ids": [
    "7.10.11"
   ],
   "claim_text": "Iceland's parliament ultimately blocked implementation despite the crisis.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "even though the existing parliament ultimately blocked implementation",
   "reasoning": "Direct restatement."
  },
  {
   "claim_id": "C201",
   "loglog_ids": [
    "7.10.12"
   ],
   "claim_text": "Ask who works for whom, not whether politicians permit oversight.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "The current framing asks: \"Will politicians allow this?\" That's the wrong question. The CEO framing asks: \"Who works for whom?\"",
   "reasoning": "Faithful restatement of the source's reframing."
  },
  {
   "claim_id": "C202",
   "loglog_ids": [
    "7.10.13"
   ],
   "claim_text": "This is a governance-design problem, not permission-seeking.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "This is a governance design problem, not a permission-seeking problem.",
   "reasoning": "Direct restatement preserving the negation."
  },
  {
   "claim_id": "C203",
   "loglog_ids": [
    "8"
   ],
   "claim_text": "Transparency is the measuring stick, not one value among many.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Transparency is not a value to be balanced. It's the measuring stick.",
   "reasoning": "Source rejects treating transparency as one value among many and names it the measuring stick."
  },
  {
   "claim_id": "C204",
   "loglog_ids": [
    "8.1"
   ],
   "claim_text": "Reject balancing transparency against efficiency, security, privacy, or speed.",
   "claim_type": "recommendation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "to \"balance\" it against efficiency, security, privacy, and speed ... Reject this framing.",
   "reasoning": "Source lists the same four values and explicitly rejects the balancing framing."
  },
  {
   "claim_id": "C205",
   "loglog_ids": [
    "8.2"
   ],
   "claim_text": "Speed and accountability are byproducts; document everything, then improve.",
   "claim_type": "recommendation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Speed and accountability are *byproducts*. Whatever speed your government operates at, document everything ... iteratively improve the processes",
   "reasoning": "Source states byproducts and instructs documenting everything then improving revealed processes."
  },
  {
   "claim_id": "C206",
   "loglog_ids": [
    "8.3"
   ],
   "claim_text": "The record pressures consistency, reasoning, accountability, and prosecution.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "pressure for consistency, pressure for sound reasoning, pressure for accountability ... easier to prosecute.",
   "reasoning": "Source lists exactly these pressures plus easier prosecution of corruption."
  },
  {
   "claim_id": "C207",
   "loglog_ids": [
    "8.4"
   ],
   "claim_text": "Reviewable officials reason better; documented decisions grow careful.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Officials who know their reasoning will be reviewed will produce better reasoning. Decisions that must be documented will be more carefully considered.",
   "reasoning": "Direct paraphrase of the two source sentences with identical meaning."
  },
  {
   "claim_id": "C208",
   "loglog_ids": [
    "8.5"
   ],
   "claim_text": "Reaching 100% transparency solves speed and accountability as consequences.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "In order to reach 100% transparency, you'll have to solve speed and accountability along the way ... they're consequences of it.",
   "reasoning": "Source says solving speed and accountability is required and labels them consequences, matching the claim."
  },
  {
   "claim_id": "C209",
   "loglog_ids": [
    "8.6"
   ],
   "claim_text": "Linux: thousands worldwide, every commit, issue, and pull request visible.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Linux ... built by thousands of people across the world ... Every commit is visible. Every issue is tracked. Every pull request is discussed.",
   "reasoning": "Source attributes these exact features to Linux and its worldwide contributors."
  },
  {
   "claim_id": "C210",
   "loglog_ids": [
    "8.7"
   ],
   "claim_text": "Disagreeing users can fork the project.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "If you disagree with a decision, you can fork the project.",
   "reasoning": "Near-verbatim restatement of the source sentence about forking."
  },
  {
   "claim_id": "C211",
   "loglog_ids": [
    "8.8"
   ],
   "claim_text": "Complex collaborative systems can be built and maintained publicly.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "complex systems can be built and maintained in public",
   "reasoning": "Source asserts this general principle about complex systems built in public."
  },
  {
   "claim_id": "C212",
   "loglog_ids": [
    "8.9"
   ],
   "claim_text": "Government is involuntary: you cannot fork your country.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "In government, you're subject to decisions whether you participated or not. You can't fork your country.",
   "reasoning": "Source states both the involuntary subjection and the inability to fork one's country."
  },
  {
   "claim_id": "C213",
   "loglog_ids": [
    "8.10"
   ],
   "claim_text": "Open source is voluntary exit; government binds non-participants.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "in open source, participation is voluntary. You can leave. In government, you're subject to decisions whether you participated or not.",
   "reasoning": "Claim matches the source contrast between voluntary exit and binding government decisions."
  },
  {
   "claim_id": "C214",
   "loglog_ids": [
    "8.11"
   ],
   "claim_text": "Less choice about affectedness means more right to see.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "The less choice you have about being affected by decisions, the more right you have to see how those decisions are made.",
   "reasoning": "Direct rephrasing of the source's proportional statement with same meaning."
  },
  {
   "claim_id": "C215",
   "loglog_ids": [
    "8.12"
   ],
   "claim_text": "You pay, live with consequences, and are CEO: act like it.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "You pay for this government. You live with its consequences. You are the CEO. Act like it.",
   "reasoning": "Compression of the four source sentences into one, preserving all propositions."
  },
  {
   "claim_id": "C216",
   "loglog_ids": [
    "9"
   ],
   "claim_text": "Appendix registers 49 sources backing the case.",
   "claim_type": "meta",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Appendix: Sources with Summaries ... 49. [Finnish Ministry of Justice - Act on Openness of Government Activities]",
   "reasoning": "Source appendix lists numbered sources 1 through 49."
  },
  {
   "claim_id": "C217",
   "loglog_ids": [
    "9.1"
   ],
   "claim_text": "UNESCO lists the 1766 ordinance as first free-communication legislation.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "UNESCO recognition of the 1766 act as world's first legislation guaranteeing free communication of information",
   "reasoning": "Source states UNESCO recognizes it as first such legislation."
  },
  {
   "claim_id": "C218",
   "loglog_ids": [
    "9.2"
   ],
   "claim_text": "GWU archive marks the FOI act's 250th anniversary; Britannica covers the 1766 act's Hats-Caps-Chydenius origins.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "George Washington University archive documenting the 250th anniversary of the world's first FOI act ... origins in the political conflict between Hats and Caps parties; role of Anders Chydenius",
   "reasoning": "Source describes both the 250th anniversary archive and the Hats-Caps-Chydenius origins."
  },
  {
   "claim_id": "C219",
   "loglog_ids": [
    "9.3"
   ],
   "claim_text": "X-Road official specs plus wiki history: 1998 start, 2001 launch, 1996 leak.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "history (started 1998, launched 2001), architecture decisions, 1996 data leak",
   "reasoning": "All three dates match source exactly."
  },
  {
   "claim_id": "C220",
   "loglog_ids": [
    "9.4"
   ],
   "claim_text": "Estonia's 30-year journey rose 16th to 2nd, hitting 100% digitalization in 2024; Brazil's 2004 CGU portal holds five categories.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "rise from 16th to 2nd ... 100% digitalization milestone in 2024 ... portal in 2004 by CGU; details five data categories",
   "reasoning": "Source matches all figures: 30-year, 16th to 2nd, 2024, 2004, five categories."
  },
  {
   "claim_id": "C221",
   "loglog_ids": [
    "9.5"
   ],
   "claim_text": "OECD logs 20+ million yearly portal visits and 17-source 2018 integration.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "portal accessed 20+ million times yearly; describes 2018 data warehouse integration of 17 sources",
   "reasoning": "Numbers and year match source."
  },
  {
   "claim_id": "C222",
   "loglog_ids": [
    "9.6"
   ],
   "claim_text": "Fiquem Sabendo's LAI probe surfaced 60GB over 27 years of former presidents.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Fiquem Sabendo used LAI to uncover 60GB of hidden pension payment data spanning 27 years of former presidents",
   "reasoning": "Actor, volume, and span match source."
  },
  {
   "claim_id": "C223",
   "loglog_ids": [
    "9.7"
   ],
   "claim_text": "OPEN launched April 1999 under Mayor Goh, covering 70 tasks.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "OPEN system launched April 1999 under Mayor Goh's anti-corruption campaign; covers 70 municipal tasks",
   "reasoning": "Date, actor, and count match source."
  },
  {
   "claim_id": "C224",
   "loglog_ids": [
    "9.8"
   ],
   "claim_text": "Peer-reviewed OPEN study confirms corruption falls as e-participation rises.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Peer-reviewed study ... confirms corruption decreases with e-participation",
   "reasoning": "Source states the same inverse relationship."
  },
  {
   "claim_id": "C225",
   "loglog_ids": [
    "9.9"
   ],
   "claim_text": "NZ guidance plus DPMC: 30-business-day cabinet releases from January 2019.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "details 30 business day requirement from January 2019",
   "reasoning": "Requirement and start date match source."
  },
  {
   "claim_id": "C226",
   "loglog_ids": [
    "9.10"
   ],
   "claim_text": "Taiwan's Pol.is crowdsourced Uber rules; paper traces Sunflower 2014, Tang, g0v.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "details Uber regulation as first test case ... traces origins to 2014 Sunflower Movement; analyzes Audrey Tang's role and g0v community",
   "reasoning": "Uber case, 2014, Tang, and g0v all appear in source."
  },
  {
   "claim_id": "C227",
   "loglog_ids": [
    "9.11"
   ],
   "claim_text": "Iceland analyses cover rejected crowdsourced draft and deliberative quality.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "why parliament rejected the crowdsourced draft despite referendum approval ... assessment of the deliberative quality",
   "reasoning": "Both analyses described match source."
  },
  {
   "claim_id": "C228",
   "loglog_ids": [
    "9.12"
   ],
   "claim_text": "EFF's 10-year Snowden review details FREEDOM Act gains and limits.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "10-year retrospective ... details USA FREEDOM Act passage and limitations",
   "reasoning": "Source matches on both gains and limitations."
  },
  {
   "claim_id": "C229",
   "loglog_ids": [
    "9.13"
   ],
   "claim_text": "IAPP review links disclosures to legal change and GDPR acceleration.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "legal and policy changes triggered by disclosures; notes GDPR acceleration",
   "reasoning": "Source states the same linkage."
  },
  {
   "claim_id": "C230",
   "loglog_ids": [
    "9.14"
   ],
   "claim_text": "TechCrunch and ACLU cover 2020 illegality rulings and privacy victory.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "2020 court ruling that NSA program was illegal ... ACLU attorney calls ruling \"a victory for privacy rights\"",
   "reasoning": "Both outlets and characterizations match source."
  },
  {
   "claim_id": "C231",
   "loglog_ids": [
    "9.15"
   ],
   "claim_text": "Pew 2019: 66% concerned; Roper tracks 1950s-present transparency opinion.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "66% concerned about government data collection ... from 1950s to present",
   "reasoning": "Percentage and period match source."
  },
  {
   "claim_id": "C232",
   "loglog_ids": [
    "9.16"
   ],
   "claim_text": "Roper adds ABC and Freedom Forum poll history on openness.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "includes ABC News and Freedom Forum poll data",
   "reasoning": "Both poll sources named in source."
  },
  {
   "claim_id": "C233",
   "loglog_ids": [
    "9.17"
   ],
   "claim_text": "IMF defends friction as accountability; Cambridge studies EU legitimacy perceptions.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "intentional accountability design ... transparency affects how public perceives decision-making legitimacy",
   "reasoning": "Both the IMF argument and Cambridge finding match source."
  },
  {
   "claim_id": "C234",
   "loglog_ids": [
    "9.18"
   ],
   "claim_text": "World Bank reviews mixed transparency impacts incumbents can undo.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "mixed findings on effectiveness; notes incumbents can undo positive effects of information",
   "reasoning": "Source states both mixed findings and incumbent reversal."
  },
  {
   "claim_id": "C235",
   "loglog_ids": [
    "9.19"
   ],
   "claim_text": "Harvard details Oman's Iran backchannel; Oxford frames the democratic dilemma.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "secret backchannel in Oman in achieving framework before public talks ... frames the \"democratic dilemma\"",
   "reasoning": "Both Harvard Oman detail and Oxford dilemma appear in source."
  },
  {
   "claim_id": "C236",
   "loglog_ids": [
    "9.20"
   ],
   "claim_text": "Notre Dame release: transparency aids lobbyists across 50 states, decades studied.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "transparency benefits lobbyists more than citizens in US state legislatures; ... multi-decade study of 50 states",
   "reasoning": "Source supports lobbyist benefit and 50-state multi-decade scope."
  },
  {
   "claim_id": "C237",
   "loglog_ids": [
    "9.21"
   ],
   "claim_text": "Oxford surveys diplomacy's secrecy evolution from antiquity to modernity.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "traces historical evolution from ancient diplomacy to modern era",
   "reasoning": "Source matches the ancient-to-modern scope."
  },
  {
   "claim_id": "C238",
   "loglog_ids": [
    "9.22"
   ],
   "claim_text": "Harden-Kirkland book blames electoral competition gaps; Irish 2024 trial had 569 subjects.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "proposes electoral competition as the key variable ... 2024 experimental study with 569 participants in Ireland",
   "reasoning": "Key variable and 569 participants match source."
  },
  {
   "claim_id": "C239",
   "loglog_ids": [
    "9.23"
   ],
   "claim_text": "Brennan 2024: 735 officials, threats rising since 2020, 38% threatened, ±3% margin.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "survey of 735 officials ... since 2020; 38% report threats; margin of error ±3%",
   "reasoning": "Sample size, trend, percentage, and margin match source."
  },
  {
   "claim_id": "C240",
   "loglog_ids": [
    "9.24"
   ],
   "claim_text": "NAAG tracks doxxing-swatting systematization and AI intensification.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "evolution from fringe behavior to systematic harassment; notes AI intensification",
   "reasoning": "Source states systematization and AI intensification."
  },
  {
   "claim_id": "C241",
   "loglog_ids": [
    "9.25"
   ],
   "claim_text": "Issue One counts 22 protective states since 2022; Chicago finds ~60% support, 12% to 17% wariness in 2021-2022.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "across 22 states since 2022 ... general support (~60%) but increasing civil liberties concerns (12% to 17% 2021-2022)",
   "reasoning": "State count, support level, and concern range match source."
  },
  {
   "claim_id": "C242",
   "loglog_ids": [
    "9.26"
   ],
   "claim_text": "Brennan decries overclassification; SIPRI links military openness to trust.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "classification levels far exceed genuine security needs ... military budget transparency ... builds inter-state trust",
   "reasoning": "Source supports overclassification critique and transparency-trust link."
  },
  {
   "claim_id": "C243",
   "loglog_ids": [
    "9.27"
   ],
   "claim_text": "Blair Institute: 43 states 1990-2018, populists 4x damaging, 5-place corruption slide.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "43 countries (1990-2018) ... 4x more likely to damage democratic institutions; countries fall average 5 places",
   "reasoning": "Country count, period, multiplier, and places match source."
  },
  {
   "claim_id": "C244",
   "loglog_ids": [
    "9.28"
   ],
   "claim_text": "Stanford warns visibility-driven re-election tempts short-term populism.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "transparency can create perverse incentives for short-term populist policies when re-election depends on immediate visibility",
   "reasoning": "Source states the same causal warning."
  },
  {
   "claim_id": "C245",
   "loglog_ids": [
    "9.29"
   ],
   "claim_text": "Sweden-Democrats study plus Harvard misinformation panel on perceived transparency.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Swedish populist party exploits transparency norms ... false beliefs causally reduce perceived transparency regardless of actual transparency levels",
   "reasoning": "Both studies described match source."
  },
  {
   "claim_id": "C246",
   "loglog_ids": [
    "9.30"
   ],
   "claim_text": "Latent-transparency experiments plus OGP's 75-country commitment autopsy.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "identifies \"latent transparency\" concept ... failed commitments across 75 member countries",
   "reasoning": "Latent transparency concept and 75 countries match source."
  },
  {
   "claim_id": "C247",
   "loglog_ids": [
    "9.31"
   ],
   "claim_text": "Hong 2024 ties competition-data quality to capacity; Ruijer (2020) maps conformity-to-resistance.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Hong (2024) ... only when administrative capacity is also high ... Ruijer et al. (2020) ... ranging from conformity to active resistance",
   "reasoning": "Both authors, years, and findings match source."
  },
  {
   "claim_id": "C248",
   "loglog_ids": [
    "9.32"
   ],
   "claim_text": "Workaround-resistance study plus Nordics' 250+ year openness overview.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "resist open government data policy through workarounds ... traces 250+ years of FOI practice",
   "reasoning": "Workaround study and 250+ year span match source."
  },
  {
   "claim_id": "C249",
   "loglog_ids": [
    "9.33"
   ],
   "claim_text": "Nordicom compares five Nordic regimes with inconsistent openness patterns.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "comparing right-of-access rules across five Nordic countries; notes inconsistent patterns",
   "reasoning": "Five-country comparison and inconsistency match source."
  },
  {
   "claim_id": "C250",
   "loglog_ids": [
    "9.34"
   ],
   "claim_text": "Finland's 1999 law deems documents public unless specifically exempted.",
   "claim_type": "definition",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "transparency law (1999 amendment); establishes principle that all government documents are public unless specifically exempted",
   "reasoning": "Year, default-public rule, and exemption match source."
  }
 ],
 "metrics": {
  "total_claims": 250,
  "supported": 245,
  "partially_supported": 5,
  "unverifiable": 0,
  "contradicted": 0,
  "critical_errors": 0,
  "faithfulness_precision": 0.98
 },
 "fail_list": [
  "C032",
  "C068",
  "C135",
  "C143",
  "C170"
 ]
}
```

## Judge Cov (coverage), opencode-go/deepseek-v4.1-flash

```json
{
 "judge": "coverage",
 "judge_version": "1.0.0",
 "model": "opencode-go/deepseek-v4.1-flash (opencode) scripted pipeline 2026-09-15",
 "source_id": "02_case_for_transparent_government",
 "key_points": [
  {
   "point_id": "K01",
   "point_text": "Central thesis: every government decision should be fully documented and publicly available, not just the final policy but the whole chain (data used, considerations, who was involved, alternatives, arguments for and against, implementation, evaluation, course-correction, and when/how it will be reconsidered). This is framed as basic accountability, not radicalism; only its novelty makes it sound radical.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L002",
    "L007",
    "L008",
    "L009",
    "L010",
    "L011",
    "L012"
   ],
   "evidence_quote": "Every government decision should be fully documented and publicly available. ... Document data used, considerations made, and who was involved. ... Document alternatives considered, arguments for and against, implementation steps. ... Document evaluation, course-correction plans, and reconsideration terms. ... It sounds radical only because the opposite was normalized.",
   "reasoning": "L007 states the thesis and L008-L010 enumerate the full chain (data, who, alternatives, arguments, implementation, evaluation, reconsideration), matching the source. L011-L012 add the basic-accountability and radical-only-because-novel framing."
  },
  {
   "point_id": "K02",
   "point_text": "Citizen-as-CEO framing: in a democracy citizens are the principals/CEOs and public servants are agents/employees who spend the citizens' money; information flows upward and accountability exists because a reviewable trail exists, whereas the current government lets agents classify and refuse to explain.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L013",
    "L014",
    "L015",
    "L016"
   ],
   "evidence_quote": "In democracy citizens are principals; officials are their employee-agents. ... Every servant from licensing clerk to president works for you. ... A company letting managers classify emails would go bankrupt within a year.",
   "reasoning": "L013-L016 capture the principal/agent CEO framing, the servant range from clerk to president, and the classify-and-refuse analogy to the current government."
  },
  {
   "point_id": "K03",
   "point_text": "Availability versus consumption distinction: the citizen-CEO need not read every email or attend every meeting, but must be able to trace any decision that matters; mere availability changes behavior even without consumption.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L015",
    "L017",
    "L177",
    "L178"
   ],
   "evidence_quote": "CEOs need not read everything, but reviewability shapes behavior. ... Nuance: Availability matters, not consumption: trace decisions affecting your life. ... Latent availability deters misconduct even without consumption. ... CEOs need not read every email to benefit from access.",
   "reasoning": "L015 and L017 state the distinction directly; L177-L178 reinforce that latent availability deters misconduct without consumption, matching the source."
  },
  {
   "point_id": "K04",
   "point_text": "Scope clarification: transparency is about government decisions, processes, and officials flowing to citizens, NOT about citizens surveilling each other or exposing personal records (tax returns, medical records). Privacy-preserving approaches (aggregation, anonymization, differential privacy) make separating government decision data from citizen personal data technically straightforward.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L018",
    "L019",
    "L020",
    "L021",
    "L022",
    "L023"
   ],
   "evidence_quote": "Transparency flows from government to citizens, never the reverse. ... Not tax returns, medical records, or citizens surveilling each other. ... Publish $X/$Y/$Z/$W spending, not John Smith's $47,000 taxes. ... Aggregation, anonymization, and differential privacy make separation technically straightforward.",
   "reasoning": "L018-L020 state the direction and exclusions (tax returns, medical records, mutual surveillance). L023 names all three privacy-preserving techniques, so the quantifier and mechanism are intact."
  },
  {
   "point_id": "K05",
   "point_text": "Sweden 1766: the Freedom of the Press Act was the world's first freedom of information law, now part of the constitution; born from Hats vs Caps political conflict, driven by Anders Chydenius with an explicitly anti-corruption motive. Two hundred sixty years later the offentlighetsprincipen makes documents public by default and the country has not collapsed, with Nordic countries ranking among the least corrupt and most effective democracies.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L026",
    "L027",
    "L028",
    "L029",
    "L030",
    "L031"
   ],
   "evidence_quote": "Sweden's 260-year openness shows transparency endures without collapse. ... In 1766 Sweden passed the world's first freedom-of-information law. ... Chydenius drove Hats-versus-Caps explicitly anti-corruption law. ... Offentlighetsprincipen keeps documents public by default 260 years on. ... Nordics consistently rank among least corrupt, most effective democracies.",
   "reasoning": "All elements present: 1766, first FOI law, constitutional, Hats vs Caps, Chydenius, anti-corruption motive, offentlighetsprincipen by default, no collapse, Nordic rankings."
  },
  {
   "point_id": "K06",
   "point_text": "Seoul/South Korea 1999: the OPEN system tracks 70 corruption-prone municipal tasks (construction permits, environmental regulation, urban planning) and shows citizens who decided what, at which point, in real time; this visibility removed the leverage that enabled bribery, and research confirmed corruption decreases as e-participation increases.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L032",
    "L033",
    "L034",
    "L035",
    "L036",
    "L037"
   ],
   "evidence_quote": "Seoul's 1999 OPEN system made bribery-prone permitting visible. ... OPEN tracks 70 corruption-prone tasks, including construction, environmental, and urban planning permits, in real time. ... Visibility eliminated that bribery leverage entirely. ... Corruption decreases as e-participation increases.",
   "reasoning": "Year, task count, three task categories, real-time visibility, elimination of bribery leverage, and the e-participation research finding are all captured."
  },
  {
   "point_id": "K07",
   "point_text": "Estonia 2001: X-Road is a distributed data exchange layer connecting 929+ institutions, 1,887 information systems, and 3,000+ digital services, with every transaction timestamped and cryptographically signed and all access logged; Estonia ranks 2nd in the UN E-Government Development Index with no major breaches in over 20 years, proving the infrastructure is technically feasible and that the will, not the technology, is the bottleneck.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L038",
    "L039",
    "L040",
    "L041",
    "L042",
    "L043",
    "L044",
    "L045"
   ],
   "evidence_quote": "Estonia's 2001 X-Road proves transparency infrastructure scales. ... X-Road links 929+ institutions, 1,887 systems, 3,000+ services, timestamped, signed, logged. ... Estonia ranks 2nd on the UN E-Government Development Index. ... No major breaches in over 20 years ... The technology is feasible; the bottleneck is will.",
   "reasoning": "All numbers (929+, 1,887, 3,000+), the signing/timestamping/logging, 2nd rank, no-major-breaches, and the will-not-technology conclusion are present."
  },
  {
   "point_id": "K08",
   "point_text": "Brazil 2004: the Transparency Portal publishes all federal spending (contracts, transfers, salaries, travel, credit card transactions) with 20+ million accesses per year; the Transparency Card sends real-time notifications about political spending (430,000+ active cards, 20+ million notifications), and journalists using the Access to Information Law uncovered 60GB of hidden pension payment data going back 27 years.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L046",
    "L047",
    "L048",
    "L049",
    "L050"
   ],
   "evidence_quote": "Brazil's 2004 Transparency Portal follows all federal money. ... It publishes contracts, transfers, salaries, travel, and credit-card transactions. ... over 20 million accesses per year. ... Transparency Card sent 20+ million notifications via 430,000+ active cards. ... Journalists uncovered 60GB of hidden pension payments spanning 27 years.",
   "reasoning": "Year, five published categories, 20+ million accesses, Transparency Card with 430,000+ cards and 20+ million notifications, and the 60GB/27-year pension find are all present."
  },
  {
   "point_id": "K09",
   "point_text": "New Zealand 2019: the government proactively publishes all Cabinet papers and minutes online within 30 business days of decisions, even though cabinet deliberations are typically the most protected category of government information; government has not ground to a halt and citizens can now see why decisions were made.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L052",
    "L053",
    "L054",
    "L055"
   ],
   "evidence_quote": "New Zealand publishes cabinet papers by default since 2019. ... All papers and minutes appear online within 30 business days. ... Cabinet deliberations are typically the world's most protected government information. ... Government has not halted ... citizens see why.",
   "reasoning": "Year, 30-business-day window, most-protected-category framing, and the not-halted/see-why outcome all match."
  },
  {
   "point_id": "K10",
   "point_text": "Recurring pattern: secret government programs are later revealed to be illegal or built on lies, and internal oversight failed because it operated inside the same secrecy bubble. Examples: Pentagon Papers 1971 (Vietnam unwinnable while publicly claiming progress), COINTELPRO exposed 1971 (illegal surveillance of civil rights leaders), Snowden 2013 (NSA bulk metadata collection, PRISM, surveilling foreign leaders). In each case the government predicted catastrophe and the programs proved illegal, unconstitutional, or deceptive.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L060",
    "L061",
    "L062",
    "L063",
    "L064",
    "L065",
    "L070",
    "L071"
   ],
   "evidence_quote": "Secret programs recur as illegal; secret oversight reliably fails to catch them. ... 1971 Pentagon Papers showed government knew Vietnam was unwinnable while publicly claiming progress. ... Media, Pennsylvania break-in exposed COINTELPRO's illegal surveillance ... In 2013 Snowden revealed bulk metadata collection ... PRISM, and leader surveillance. ... FISA courts, committees, and inspectors general failed inside the secrecy structure.",
   "reasoning": "The pattern, all three examples with years and content, the failed cataclysm predictions, and the oversight-inside-secrecy explanation (L070-L071) are all captured."
  },
  {
   "point_id": "K11",
   "point_text": "Snowden aftermath: in September 2020 the US Ninth Circuit ruled the NSA bulk phone record collection illegal and possibly unconstitutional, failing FISA's relevance requirement; Geoffrey R. Stone found no evidence it stopped terror attacks, and the NSA abandoned the program in 2018. The USA FREEDOM Act (2015) was the first legislation in over 30 years to rein in NSA spying, ending bulk metadata collection; tech transparency reporting, default HTTPS, and accelerated EU GDPR followed. Whether disclosure caused operational harm remains genuinely uncertain, but the legality and oversight failures are not.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L066",
    "L067",
    "L068",
    "L069",
    "L072",
    "L073",
    "L074",
    "L075",
    "L076",
    "L077"
   ],
   "evidence_quote": "In September 2020 the Ninth Circuit ruled bulk collection illegal, possibly unconstitutional. ... The court required FISA relevance to a particular authorized investigation. ... Stone found no evidence bulk collection stopped any terror attacks. ... The NSA abandoned the program in 2018 ... The 2015 USA FREEDOM Act first reined in NSA spying in over 30 years. ... HTTPS became default ... GDPR was accelerated ... Operational harm is genuinely uncertain; illegality is not.",
   "reasoning": "All specifics present: Sept 2020 Ninth Circuit, possibly unconstitutional, FISA relevance, Stone, 2018 abandonment, 2015 Act/first-in-30-years, transparency reporting, HTTPS, GDPR, and the harm-uncertain/illegality-certain caveat."
  },
  {
   "point_id": "K12",
   "point_text": "Privacy and harassment objections: privacy fears (e.g., 66% concerned about government data collection; 86% opposed to online public records) are about citizen data held by government, not about government decisions being visible, so they rest on a direction confusion; likewise threats to officials are real (Brennan Center 2024 survey of 735 officials: 38% threatened, 34% know someone who resigned, up from 22% in 2023), so decisions should be public while officials' personal information is protected. Much current harassment stems from lack of transparency about processes.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L082",
    "L083",
    "L084",
    "L126",
    "L127",
    "L128",
    "L133",
    "L135",
    "L136"
   ],
   "evidence_quote": "2019 Pew: 66% fear collection ... A 2000 ABC poll: 86% said agencies should not publish such records online. ... Polls fear citizen data held by government, not visible government decisions. ... Brennan surveyed 735 local election officials ... 38% threatened ... 34% know someone who resigned, up from 22% in 2023. ... Publish who decided what and why; protect addresses, families, schedules. ... Current harassment feeds on opacity-bred fraud conspiracies.",
   "reasoning": "All numbers and caveats present: 66%, 86%, direction-confusion rebuttal, Brennan 735/38%/34% up from 22%, protect personal info while publishing decisions, and harassment-fed-by-opacity."
  },
  {
   "point_id": "K13",
   "point_text": "Secrecy-based objections and answers: the gridlock argument confuses speed with documentation (transparency documents decisions at the current speed, as NZ shows, and opacity makes decisions unaccountable rather than better); diplomacy (JCPOA secret Oman backchannel, Camp David, Cold War) and markets (Fed FOMC minutes delayed three weeks, transcripts five years; TTIP harmed by too much secrecy) justify only temporary operational secrecy with time-delayed release (e.g., 30-90 days), never permanent secrecy about what was decided and why; national security is overused to hide embarrassment, illegality, incompetence, and corruption, and the burden of proof should be reversed so officials must justify secrecy.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L092",
    "L094",
    "L095",
    "L096",
    "L100",
    "L101",
    "L105",
    "L106",
    "L147",
    "L148",
    "L149",
    "L150",
    "L184",
    "L185",
    "L186"
   ],
   "evidence_quote": "This confuses decision speed with decision documentation. ... New Zealand's 30-day cabinet papers halted nothing ... Opacity makes decisions unaccountable random walks, not better ones. ... JCPOA began in 2012 via Sullivan's secret Oman backchannel. ... Camp David 1978 and Cold War backchannels ... Temporary secrecy during talks is acceptable; permanent secrecy is not. ... Release full documentation 30-90 days after conclusion ... The Fed releases minutes in three weeks, transcripts in five years. ... TTIP failed amid backlash ... Flip the burden: transparent by default, secrecy needs proof. ... The label hides embarrassment, illegality, incompetence, and corruption. ... Officials under scrutiny set secrecy criteria: a conflict of interest.",
   "reasoning": "Every element is present: speed/documentation confusion, NZ example, unaccountability of opacity, JCPOA Oman, Camp David, Cold War, Fed 3-week/5-year timing, TTIP, 30-90 day delayed release, national-security overuse/label, and reversing the burden of proof."
  },
  {
   "point_id": "K14",
   "point_text": "Empirical misuse concerns acknowledged but rebutted: Harden and Kirkland found open legislative meetings bring more lobbying, more lobbyist donations, and no improved policy-opinion correlation, and 2024 Irish experiment found lobbying transparency does not raise trust; populism research (Kyle and Gultchin, 43 countries 1990-2018) finds populists 4x more likely to damage democracy and countries falling ~5 places on the Corruption Perceptions Index; misinformation research finds false beliefs reduce perceived transparency. The answer is not less transparency but building citizen capacity (watchdogs, investigative journalism, civic tech, professional monitoring) and better transparency, since populists reduce rather than increase transparency, opacity enables false beliefs, and selective exploitation works only because not everything is visible.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L111",
    "L113",
    "L114",
    "L116",
    "L117",
    "L119",
    "L153",
    "L154",
    "L155",
    "L161",
    "L162",
    "L168",
    "L173",
    "L174"
   ],
   "evidence_quote": "Harden and Kirkland studied all 50 legislatures over multiple decades. ... More lobbyists register and donate, yet policy-opinion correlation stays same open or closed. ... Ireland 2024: 569 participants; lobbying transparency did not raise trust. ... Build citizen capacity: auditors, watchdogs, journalism, civic tech. ... Kyle-Gultchin studied 43 democracies, 1990-2018 ... Populists are 4x likelier to damage institutions ... Countries fall 5 places on corruption perceptions ... Causality is backwards: populists damage democracy by reducing transparency. ... Cherry-picking works only while the full record stays hidden. ... Harvard 2023 ... COVID-19 false beliefs lower perceived transparency. ... False beliefs drive perceived opacity, not the reverse. ... Opacity enables false beliefs.",
   "reasoning": "All empirical results and numbers present: Harden/Kirkland lobbying and donation finding with no correlation improvement, Irish 2024 experiment, Kyle-Gultchin 43 countries/1990-2018/4x/5 places, misinformation false-beliefs finding, and the citizen-capacity plus causal-reversal rebuttals."
  },
  {
   "point_id": "K15",
   "point_text": "Resistance and the closing vision: 'those in power will never allow this' is a description of the political challenge, not a principled objection (Iceland's 2008 crowdsourced constitution was blocked by parliament despite referendum approval; OGP commitments fail on funding, coordination, and political transitions), and the CEO framing reframes it as a governance design problem of who works for whom. Transparency is not a value to be balanced but the measuring stick; speed and accountability are byproducts, and open source shows complex collaborative work can be done in public, with the case for transparency stronger because citizens cannot fork their country.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L191",
    "L193",
    "L194",
    "L195",
    "L196",
    "L197",
    "L202",
    "L203",
    "L204",
    "L205",
    "L206",
    "L209",
    "L210",
    "L211",
    "L212",
    "L213"
   ],
   "evidence_quote": "That describes the political challenge, not a principled objection. ... two-thirds referendum approval. ... Parliament refused to ratify the draft. ... OGP: 75 countries, 4,500+ commitments since 2011; one-third delayed for funding. ... Ask who works for whom ... This is a governance-design problem, not permission-seeking. ... Transparency is the measuring stick, not one value among many. ... Speed and accountability are byproducts ... Linux ... Disagreeing users can fork the project. ... Government is involuntary: you cannot fork your country.",
   "reasoning": "All elements present: description-not-objection reframe, Iceland 2008 blocked constitution, OGP funding/coordination/transition failures, who-works-for-whom governance-design framing, transparency-as-measuring-stick, speed/accountability as byproducts, open-source example, and cannot-fork-your-country."
  }
 ],
 "metrics": {
  "total_points": 15,
  "must_have_total": 15,
  "must_have_present": 15,
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
 "source_id": "02_case_for_transparent_government",
 "labels": [
  {
   "claim_id": "C001",
   "loglog_ids": [
    "0"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Section 0 summary states thesis; first occurrence, body still adds detail."
  },
  {
   "claim_id": "C002",
   "loglog_ids": [
    "1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Manager analogy introduces the governing case, new here."
  },
  {
   "claim_id": "C003",
   "loglog_ids": [
    "1.1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Concrete example instance, not stated earlier."
  },
  {
   "claim_id": "C004",
   "loglog_ids": [
    "1.2"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Owner-response detail extends the analogy."
  },
  {
   "claim_id": "C005",
   "loglog_ids": [
    "1.3"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Government excuse list new and enumerates objections."
  },
  {
   "claim_id": "C006",
   "loglog_ids": [
    "2"
   ],
   "label": "Duplicate",
   "canonical_id": "C001",
   "reasoning": "Section 2 heading restates summary mandate; adds only publicly available."
  },
  {
   "claim_id": "C007",
   "loglog_ids": [
    "2.1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Specific documentation fields, new information."
  },
  {
   "claim_id": "C008",
   "loglog_ids": [
    "2.2"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Additional documentation fields, new."
  },
  {
   "claim_id": "C009",
   "loglog_ids": [
    "2.3"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Evaluation and course-correction fields, new."
  },
  {
   "claim_id": "C010",
   "loglog_ids": [
    "2.4"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Corporate comparability claim, supports mandate."
  },
  {
   "claim_id": "C011",
   "loglog_ids": [
    "2.5"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Normalization explanation, new framing."
  },
  {
   "claim_id": "C012",
   "loglog_ids": [
    "3"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Principal-agent definition, distinct from summary."
  },
  {
   "claim_id": "C013",
   "loglog_ids": [
    "3.1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Scope enumeration from clerk to president, new."
  },
  {
   "claim_id": "C014",
   "loglog_ids": [
    "3.2"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Reviewability-behavior link, first occurrence."
  },
  {
   "claim_id": "C015",
   "loglog_ids": [
    "3.3"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Bankruptcy reductio, new argument."
  },
  {
   "claim_id": "C016",
   "loglog_ids": [
    "3.4"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Availability-versus-consumption nuance, first occurrence."
  },
  {
   "claim_id": "C017",
   "loglog_ids": [
    "4"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Direction definition, new scope claim."
  },
  {
   "claim_id": "C018",
   "loglog_ids": [
    "4.1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Positive definition components, new."
  },
  {
   "claim_id": "C019",
   "loglog_ids": [
    "4.2"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Negative exclusions, new and load-bearing."
  },
  {
   "claim_id": "C020",
   "loglog_ids": [
    "4.3"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "CEO work-product analogy, first occurrence."
  },
  {
   "claim_id": "C021",
   "loglog_ids": [
    "4.4"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Fiscal example with figures, new."
  },
  {
   "claim_id": "C022",
   "loglog_ids": [
    "4.5"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Privacy-technique feasibility claim, new."
  },
  {
   "claim_id": "C023",
   "loglog_ids": [
    "5"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Feasibility thesis, new section claim."
  },
  {
   "claim_id": "C024",
   "loglog_ids": [
    "5.1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Existence nuance, new."
  },
  {
   "claim_id": "C025",
   "loglog_ids": [
    "5.2"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Sweden example headline, new."
  },
  {
   "claim_id": "C026",
   "loglog_ids": [
    "5.2.1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "1766 law date, canonical body occurrence."
  },
  {
   "claim_id": "C027",
   "loglog_ids": [
    "5.2.2"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Censorship abolition detail, new."
  },
  {
   "claim_id": "C028",
   "loglog_ids": [
    "5.2.3"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Chydenius origin detail, canonical body occurrence."
  },
  {
   "claim_id": "C029",
   "loglog_ids": [
    "5.2.4"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Offentlighetsprincipen term, new."
  },
  {
   "claim_id": "C030",
   "loglog_ids": [
    "5.2.5"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Nordic ranking fact, new."
  },
  {
   "claim_id": "C031",
   "loglog_ids": [
    "5.3"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Seoul OPEN case headline, new."
  },
  {
   "claim_id": "C032",
   "loglog_ids": [
    "5.3.1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "70-task scope, canonical body occurrence."
  },
  {
   "claim_id": "C033",
   "loglog_ids": [
    "5.3.2"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Process-point attribution, new."
  },
  {
   "claim_id": "C034",
   "loglog_ids": [
    "5.3.3"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Bribe mechanism, new causal detail."
  },
  {
   "claim_id": "C035",
   "loglog_ids": [
    "5.3.4"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Elimination outcome, new."
  },
  {
   "claim_id": "C036",
   "loglog_ids": [
    "5.3.5"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Corruption-participation link, canonical occurrence."
  },
  {
   "claim_id": "C037",
   "loglog_ids": [
    "5.4"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Estonia X-Road headline, new."
  },
  {
   "claim_id": "C038",
   "loglog_ids": [
    "5.4.1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "System statistics, canonical body occurrence."
  },
  {
   "claim_id": "C039",
   "loglog_ids": [
    "5.4.2"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Data-access visibility fact, new."
  },
  {
   "claim_id": "C040",
   "loglog_ids": [
    "5.4.3"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Estonia index rank, canonical occurrence."
  },
  {
   "claim_id": "C041",
   "loglog_ids": [
    "5.4.4"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Breach record, new evidence."
  },
  {
   "claim_id": "C042",
   "loglog_ids": [
    "5.4.5"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "License and deployment fact, new."
  },
  {
   "claim_id": "C043",
   "loglog_ids": [
    "5.4.6"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Feasibility interpretation, new."
  },
  {
   "claim_id": "C044",
   "loglog_ids": [
    "5.4.7"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Will-versus-technology conclusion, new."
  },
  {
   "claim_id": "C045",
   "loglog_ids": [
    "5.5"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Brazil portal headline, new."
  },
  {
   "claim_id": "C046",
   "loglog_ids": [
    "5.5.1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Publication categories, new."
  },
  {
   "claim_id": "C047",
   "loglog_ids": [
    "5.5.2"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Access-count figure, canonical occurrence."
  },
  {
   "claim_id": "C048",
   "loglog_ids": [
    "5.5.3"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Transparency Card figures, new."
  },
  {
   "claim_id": "C049",
   "loglog_ids": [
    "5.5.4"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "60GB pension find, canonical occurrence."
  },
  {
   "claim_id": "C050",
   "loglog_ids": [
    "5.5.5"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Fraud-finding interpretation, new."
  },
  {
   "claim_id": "C051",
   "loglog_ids": [
    "5.6"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "New Zealand case headline, new."
  },
  {
   "claim_id": "C052",
   "loglog_ids": [
    "5.6.1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "30-day window, canonical occurrence."
  },
  {
   "claim_id": "C053",
   "loglog_ids": [
    "5.6.2"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Cabinet-protection baseline, new."
  },
  {
   "claim_id": "C054",
   "loglog_ids": [
    "5.6.3"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Government-continued fact, new."
  },
  {
   "claim_id": "C055",
   "loglog_ids": [
    "5.7"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Taiwan vTaiwan headline, new."
  },
  {
   "claim_id": "C056",
   "loglog_ids": [
    "5.7.1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Pol.is mechanism, canonical occurrence."
  },
  {
   "claim_id": "C057",
   "loglog_ids": [
    "5.7.2"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "2018 throughput figures, new."
  },
  {
   "claim_id": "C058",
   "loglog_ids": [
    "5.7.3"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Participation-versus-transparency scope, new."
  },
  {
   "claim_id": "C059",
   "loglog_ids": [
    "6"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Secret-program failure thesis, new."
  },
  {
   "claim_id": "C060",
   "loglog_ids": [
    "6.1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Pentagon Papers evidence, new."
  },
  {
   "claim_id": "C061",
   "loglog_ids": [
    "6.2"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "COINTELPRO exposure, new."
  },
  {
   "claim_id": "C062",
   "loglog_ids": [
    "6.3"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "COINTELPRO targets, new."
  },
  {
   "claim_id": "C063",
   "loglog_ids": [
    "6.4"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Snowden revelations detail, new."
  },
  {
   "claim_id": "C064",
   "loglog_ids": [
    "6.5"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Predicted-catastrophe pattern, canonical occurrence."
  },
  {
   "claim_id": "C065",
   "loglog_ids": [
    "6.6"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Ninth Circuit ruling, canonical occurrence."
  },
  {
   "claim_id": "C066",
   "loglog_ids": [
    "6.7"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "FISA-relevance requirement, new."
  },
  {
   "claim_id": "C067",
   "loglog_ids": [
    "6.8"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Stone finding, new evidence."
  },
  {
   "claim_id": "C068",
   "loglog_ids": [
    "6.9"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "2018 abandonment date, new; partially supported but scored."
  },
  {
   "claim_id": "C069",
   "loglog_ids": [
    "6.10"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Oversight-failure claim, new."
  },
  {
   "claim_id": "C070",
   "loglog_ids": [
    "6.11"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Capture interpretation, new."
  },
  {
   "claim_id": "C071",
   "loglog_ids": [
    "6.12"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "USA FREEDOM Act, new."
  },
  {
   "claim_id": "C072",
   "loglog_ids": [
    "6.13"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Act contents, canonical occurrence."
  },
  {
   "claim_id": "C073",
   "loglog_ids": [
    "6.14"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Tech transparency reporting, new."
  },
  {
   "claim_id": "C074",
   "loglog_ids": [
    "6.15"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "HTTPS default, new."
  },
  {
   "claim_id": "C075",
   "loglog_ids": [
    "6.16"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "GDPR acceleration, canonical occurrence."
  },
  {
   "claim_id": "C076",
   "loglog_ids": [
    "6.17"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Harm-versus-illegality nuance, new."
  },
  {
   "claim_id": "C077",
   "loglog_ids": [
    "6.18"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Snowden-symptom framing, new."
  },
  {
   "claim_id": "C078",
   "loglog_ids": [
    "6.19"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Designed-in traceability proposal, new."
  },
  {
   "claim_id": "C079",
   "loglog_ids": [
    "7"
   ],
   "label": "Trivia",
   "canonical_id": null,
   "reasoning": "Roadmap transition announcing ten objections; filler with no substantive content."
  },
  {
   "claim_id": "C080",
   "loglog_ids": [
    "7.1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Privacy objection, new."
  },
  {
   "claim_id": "C081",
   "loglog_ids": [
    "7.1.1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Pew figures, canonical occurrence."
  },
  {
   "claim_id": "C082",
   "loglog_ids": [
    "7.1.2"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "ABC poll, canonical occurrence."
  },
  {
   "claim_id": "C083",
   "loglog_ids": [
    "7.1.3"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Poll reinterpretation, new."
  },
  {
   "claim_id": "C084",
   "loglog_ids": [
    "7.1.4"
   ],
   "label": "Duplicate",
   "canonical_id": "C020",
   "reasoning": "Repeats work-product-versus-health-records distinction from 4.3."
  },
  {
   "claim_id": "C085",
   "loglog_ids": [
    "7.1.5"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Specific rebuttal figure, distinct from 4.4."
  },
  {
   "claim_id": "C086",
   "loglog_ids": [
    "7.1.6"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Bundled-systems split recommendation, new."
  },
  {
   "claim_id": "C087",
   "loglog_ids": [
    "7.2"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Deliberation-paralysis objection, new."
  },
  {
   "claim_id": "C088",
   "loglog_ids": [
    "7.2.1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Cambridge and IMF evidence, canonical occurrence."
  },
  {
   "claim_id": "C089",
   "loglog_ids": [
    "7.2.2"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "IMF friction defense, new."
  },
  {
   "claim_id": "C090",
   "loglog_ids": [
    "7.2.3"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Robodebt figures, canonical occurrence."
  },
  {
   "claim_id": "C091",
   "loglog_ids": [
    "7.2.4"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Speed-versus-documentation confusion, new."
  },
  {
   "claim_id": "C092",
   "loglog_ids": [
    "7.2.5"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Document-at-speed recommendation, new."
  },
  {
   "claim_id": "C093",
   "loglog_ids": [
    "7.2.6"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "CEO documentation analogy, new here."
  },
  {
   "claim_id": "C094",
   "loglog_ids": [
    "7.2.7"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "New Zealand restated as rebuttal, new context."
  },
  {
   "claim_id": "C095",
   "loglog_ids": [
    "7.2.8"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Opacity-as-random-walk claim, new."
  },
  {
   "claim_id": "C096",
   "loglog_ids": [
    "7.2.9"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Consistency-speed causal claim, new."
  },
  {
   "claim_id": "C097",
   "loglog_ids": [
    "7.3"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Diplomacy-secrecy objection, new."
  },
  {
   "claim_id": "C098",
   "loglog_ids": [
    "7.3.1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Concession stance, new."
  },
  {
   "claim_id": "C099",
   "loglog_ids": [
    "7.3.2"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "JCPOA backchannel, canonical occurrence."
  },
  {
   "claim_id": "C100",
   "loglog_ids": [
    "7.3.3"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Camp David and Cold War examples, new."
  },
  {
   "claim_id": "C101",
   "loglog_ids": [
    "7.3.4"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Democratic dilemma definition, new."
  },
  {
   "claim_id": "C102",
   "loglog_ids": [
    "7.3.5"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "CEO negotiation analogy, new."
  },
  {
   "claim_id": "C103",
   "loglog_ids": [
    "7.3.6"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Post-hoc disclosure recommendation, new."
  },
  {
   "claim_id": "C104",
   "loglog_ids": [
    "7.3.7"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Temporary-versus-permanent secrecy line, new."
  },
  {
   "claim_id": "C105",
   "loglog_ids": [
    "7.3.8"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "30-90 day release window, new."
  },
  {
   "claim_id": "C106",
   "loglog_ids": [
    "7.3.9"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Non-principal veto claim, new."
  },
  {
   "claim_id": "C107",
   "loglog_ids": [
    "7.3.10"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Principals restatement in foreign context, new angle."
  },
  {
   "claim_id": "C108",
   "loglog_ids": [
    "7.4"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Special-interest objection, new."
  },
  {
   "claim_id": "C109",
   "loglog_ids": [
    "7.4.1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Concession stance, new."
  },
  {
   "claim_id": "C110",
   "loglog_ids": [
    "7.4.2"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Harden-Kirkland study, canonical occurrence."
  },
  {
   "claim_id": "C111",
   "loglog_ids": [
    "7.4.3"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Illusion of Accountability study, new."
  },
  {
   "claim_id": "C112",
   "loglog_ids": [
    "7.4.4"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Lobbyist-versus-correlation finding, new."
  },
  {
   "claim_id": "C113",
   "loglog_ids": [
    "7.4.5"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Harden representation finding, new."
  },
  {
   "claim_id": "C114",
   "loglog_ids": [
    "7.4.6"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Arnold 1990 finding, new."
  },
  {
   "claim_id": "C115",
   "loglog_ids": [
    "7.4.7"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Ireland 2024 trial, new."
  },
  {
   "claim_id": "C116",
   "loglog_ids": [
    "7.4.8"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Asymmetry framing, new."
  },
  {
   "claim_id": "C117",
   "loglog_ids": [
    "7.4.9"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Resource imbalance detail, new."
  },
  {
   "claim_id": "C118",
   "loglog_ids": [
    "7.4.10"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Build-capacity recommendation, canonical occurrence."
  },
  {
   "claim_id": "C119",
   "loglog_ids": [
    "7.4.11"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Fiquem Sabendo evidence, new."
  },
  {
   "claim_id": "C120",
   "loglog_ids": [
    "7.4.12"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Electoral-competition key claim, new."
  },
  {
   "claim_id": "C121",
   "loglog_ids": [
    "7.4.13"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Opacity-transparency contrast, new."
  },
  {
   "claim_id": "C122",
   "loglog_ids": [
    "7.4.14"
   ],
   "label": "Duplicate",
   "canonical_id": "C118",
   "reasoning": "Restates build-capacity-not-reduce-information recommendation from 7.4.10."
  },
  {
   "claim_id": "C123",
   "loglog_ids": [
    "7.5"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Harassment objection, new."
  },
  {
   "claim_id": "C124",
   "loglog_ids": [
    "7.5.1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Concession stance, new."
  },
  {
   "claim_id": "C125",
   "loglog_ids": [
    "7.5.2"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Brennan survey method, canonical occurrence."
  },
  {
   "claim_id": "C126",
   "loglog_ids": [
    "7.5.3"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Threat percentages, new."
  },
  {
   "claim_id": "C127",
   "loglog_ids": [
    "7.5.4"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Resignation-awareness figures, new."
  },
  {
   "claim_id": "C128",
   "loglog_ids": [
    "7.5.5"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "In-person threat figure, new."
  },
  {
   "claim_id": "C129",
   "loglog_ids": [
    "7.5.6"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Doxxing-swatting evolution, canonical occurrence."
  },
  {
   "claim_id": "C130",
   "loglog_ids": [
    "7.5.7"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "AI intensification claim, new."
  },
  {
   "claim_id": "C131",
   "loglog_ids": [
    "7.5.8"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "22-state protection count, new."
  },
  {
   "claim_id": "C132",
   "loglog_ids": [
    "7.5.9"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Publish-why-protect-personal recommendation, new."
  },
  {
   "claim_id": "C133",
   "loglog_ids": [
    "7.5.10"
   ],
   "label": "Duplicate",
   "canonical_id": "C020",
   "reasoning": "Work-product-versus-personal-records analogy repeats 4.3."
  },
  {
   "claim_id": "C134",
   "loglog_ids": [
    "7.5.11"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Opacity-conspiracy causal claim, canonical occurrence."
  },
  {
   "claim_id": "C135",
   "loglog_ids": [
    "7.5.12"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Audit-transparency antidote, new; partially supported but scored."
  },
  {
   "claim_id": "C136",
   "loglog_ids": [
    "7.5.13"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Protect-more-while-transparent recommendation, new."
  },
  {
   "claim_id": "C137",
   "loglog_ids": [
    "7.6"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "National-security objection, new."
  },
  {
   "claim_id": "C138",
   "loglog_ids": [
    "7.6.1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Use-versus-scrutiny observation, new."
  },
  {
   "claim_id": "C139",
   "loglog_ids": [
    "7.6.2"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Chicago poll figure, canonical occurrence."
  },
  {
   "claim_id": "C140",
   "loglog_ids": [
    "7.6.3"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Share-more majority, canonical occurrence."
  },
  {
   "claim_id": "C141",
   "loglog_ids": [
    "7.6.4"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Wariness trend figures, new."
  },
  {
   "claim_id": "C142",
   "loglog_ids": [
    "7.6.5"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Brennan overclassification claim, new."
  },
  {
   "claim_id": "C143",
   "loglog_ids": [
    "7.6.6"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "SIPRI trust claim, canonical occurrence; partially supported but scored."
  },
  {
   "claim_id": "C144",
   "loglog_ids": [
    "7.6.7"
   ],
   "label": "Duplicate",
   "canonical_id": "C064",
   "reasoning": "Snowden catastrophe-prediction failure restates 6.5 pattern."
  },
  {
   "claim_id": "C145",
   "loglog_ids": [
    "7.6.8"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Independent-research minimal impact, new."
  },
  {
   "claim_id": "C146",
   "loglog_ids": [
    "7.6.9"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Flip-the-burden recommendation, new."
  },
  {
   "claim_id": "C147",
   "loglog_ids": [
    "7.6.10"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Temporary classification scope, new."
  },
  {
   "claim_id": "C148",
   "loglog_ids": [
    "7.6.11"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Label-hides-misconduct claim, new."
  },
  {
   "claim_id": "C149",
   "loglog_ids": [
    "7.6.12"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Conflict-of-interest claim, new."
  },
  {
   "claim_id": "C150",
   "loglog_ids": [
    "7.7"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Populist-weaponization objection, new."
  },
  {
   "claim_id": "C151",
   "loglog_ids": [
    "7.7.1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Concession stance, new."
  },
  {
   "claim_id": "C152",
   "loglog_ids": [
    "7.7.2"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Kyle-Gultchin dataset, canonical occurrence."
  },
  {
   "claim_id": "C153",
   "loglog_ids": [
    "7.7.3"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "4x institution-damage figure, new."
  },
  {
   "claim_id": "C154",
   "loglog_ids": [
    "7.7.4"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Corruption-rank slides, new."
  },
  {
   "claim_id": "C155",
   "loglog_ids": [
    "7.7.5"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Venezuela example, new."
  },
  {
   "claim_id": "C156",
   "loglog_ids": [
    "7.7.6"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Constitution-rewrite and tenure figures, new."
  },
  {
   "claim_id": "C157",
   "loglog_ids": [
    "7.7.7"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Stanford short-termism claim, canonical occurrence."
  },
  {
   "claim_id": "C158",
   "loglog_ids": [
    "7.7.8"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Sweden Democrats case, new."
  },
  {
   "claim_id": "C159",
   "loglog_ids": [
    "7.7.9"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Scandal-erosion mechanism, new."
  },
  {
   "claim_id": "C160",
   "loglog_ids": [
    "7.7.10"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Reversed-causality claim, new."
  },
  {
   "claim_id": "C161",
   "loglog_ids": [
    "7.7.11"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Cherry-picking-hidden-record claim, new."
  },
  {
   "claim_id": "C162",
   "loglog_ids": [
    "7.7.12"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Electoral-cycle short-termism, new."
  },
  {
   "claim_id": "C163",
   "loglog_ids": [
    "7.7.13"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Documented-rationale defensibility, new."
  },
  {
   "claim_id": "C164",
   "loglog_ids": [
    "7.7.14"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Reasoning-evaluation antidote, new."
  },
  {
   "claim_id": "C165",
   "loglog_ids": [
    "7.7.15"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "CEO documented-reasoning analogy, distinct from 7.2.6."
  },
  {
   "claim_id": "C166",
   "loglog_ids": [
    "7.8"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Misinformation objection, new."
  },
  {
   "claim_id": "C167",
   "loglog_ids": [
    "7.8.1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Harvard panel finding, canonical occurrence."
  },
  {
   "claim_id": "C168",
   "loglog_ids": [
    "7.8.2"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Control variable detail, new."
  },
  {
   "claim_id": "C169",
   "loglog_ids": [
    "7.8.3"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Perception-effects causal claim, new."
  },
  {
   "claim_id": "C170",
   "loglog_ids": [
    "7.8.4"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Prize-idea-dislike-content finding, new; partially supported but scored."
  },
  {
   "claim_id": "C171",
   "loglog_ids": [
    "7.8.5"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Non-sequitur rebuttal, new."
  },
  {
   "claim_id": "C172",
   "loglog_ids": [
    "7.8.6"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Direction-of-causality claim, new."
  },
  {
   "claim_id": "C173",
   "loglog_ids": [
    "7.8.7"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Secrecy-vacuum speculation claim, new."
  },
  {
   "claim_id": "C174",
   "loglog_ids": [
    "7.8.8"
   ],
   "label": "Duplicate",
   "canonical_id": "C134",
   "reasoning": "Election-conspiracy-from-opacity restates opacity-conspiracy link in 7.5.11."
  },
  {
   "claim_id": "C175",
   "loglog_ids": [
    "7.8.9"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Checkable-ground-truth claim, new."
  },
  {
   "claim_id": "C176",
   "loglog_ids": [
    "7.8.10"
   ],
   "label": "Duplicate",
   "canonical_id": "C016",
   "reasoning": "Latent-availability-deters-misconduct restates availability-over-consumption in 3.4."
  },
  {
   "claim_id": "C177",
   "loglog_ids": [
    "7.8.11"
   ],
   "label": "Duplicate",
   "canonical_id": "C014",
   "reasoning": "CEOs-need-not-read-every-email restates reviewability claim in 3.2."
  },
  {
   "claim_id": "C178",
   "loglog_ids": [
    "7.8.12"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Persistent-transparency trust claim, new."
  },
  {
   "claim_id": "C179",
   "loglog_ids": [
    "7.8.13"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Accessibility-intermediary recommendation, new."
  },
  {
   "claim_id": "C180",
   "loglog_ids": [
    "7.9"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Market-manipulation objection, new."
  },
  {
   "claim_id": "C181",
   "loglog_ids": [
    "7.9.1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Trader-exploitation detail, new."
  },
  {
   "claim_id": "C182",
   "loglog_ids": [
    "7.9.2"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Delayed-secrecy concession, new."
  },
  {
   "claim_id": "C183",
   "loglog_ids": [
    "7.9.3"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Fed release windows, new."
  },
  {
   "claim_id": "C184",
   "loglog_ids": [
    "7.9.4"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "TTIP failure evidence, new."
  },
  {
   "claim_id": "C185",
   "loglog_ids": [
    "7.9.5"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Eventual-publication framing, new."
  },
  {
   "claim_id": "C186",
   "loglog_ids": [
    "7.9.6"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Domain-specific timing recommendation, new."
  },
  {
   "claim_id": "C187",
   "loglog_ids": [
    "7.9.7"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Procurement-favoritism claim, new."
  },
  {
   "claim_id": "C188",
   "loglog_ids": [
    "7.9.8"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Brazil contract-sunlight claim, new."
  },
  {
   "claim_id": "C189",
   "loglog_ids": [
    "7.10"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Power-will-refuse objection, new."
  },
  {
   "claim_id": "C190",
   "loglog_ids": [
    "7.10.1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Political-challenge rebuttal, new."
  },
  {
   "claim_id": "C191",
   "loglog_ids": [
    "7.10.2"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Iceland 2008 process, new."
  },
  {
   "claim_id": "C192",
   "loglog_ids": [
    "7.10.3"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Comment and approval figures, new."
  },
  {
   "claim_id": "C193",
   "loglog_ids": [
    "7.10.4"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Parliament refusal, canonical occurrence."
  },
  {
   "claim_id": "C194",
   "loglog_ids": [
    "7.10.5"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "OGP commitment figures, canonical occurrence."
  },
  {
   "claim_id": "C195",
   "loglog_ids": [
    "7.10.6"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Failure causes, new."
  },
  {
   "claim_id": "C196",
   "loglog_ids": [
    "7.10.7"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Successor-abandonment claim, new."
  },
  {
   "claim_id": "C197",
   "loglog_ids": [
    "7.10.8"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Beneficiary-resistance concession, new."
  },
  {
   "claim_id": "C198",
   "loglog_ids": [
    "7.10.9"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Threatening-power-is-point claim, new."
  },
  {
   "claim_id": "C199",
   "loglog_ids": [
    "7.10.10"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Reform-window examples, new."
  },
  {
   "claim_id": "C200",
   "loglog_ids": [
    "7.10.11"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Iceland blockage interpretation, new."
  },
  {
   "claim_id": "C201",
   "loglog_ids": [
    "7.10.12"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Who-works-for-whom reframe, new."
  },
  {
   "claim_id": "C202",
   "loglog_ids": [
    "7.10.13"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Governance-design framing, new."
  },
  {
   "claim_id": "C203",
   "loglog_ids": [
    "8"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Measuring-stick thesis, new."
  },
  {
   "claim_id": "C204",
   "loglog_ids": [
    "8.1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Reject-balancing recommendation, new."
  },
  {
   "claim_id": "C205",
   "loglog_ids": [
    "8.2"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Byproducts recommendation, canonical occurrence."
  },
  {
   "claim_id": "C206",
   "loglog_ids": [
    "8.3"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Record-pressure causal claim, new."
  },
  {
   "claim_id": "C207",
   "loglog_ids": [
    "8.4"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Reviewable-officials-better claim, new."
  },
  {
   "claim_id": "C208",
   "loglog_ids": [
    "8.5"
   ],
   "label": "Duplicate",
   "canonical_id": "C205",
   "reasoning": "Speed-accountability-as-consequences restates 8.2 with 100% emphasis."
  },
  {
   "claim_id": "C209",
   "loglog_ids": [
    "8.6"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Linux open-work example, new."
  },
  {
   "claim_id": "C210",
   "loglog_ids": [
    "8.7"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Forking fact, new."
  },
  {
   "claim_id": "C211",
   "loglog_ids": [
    "8.8"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Public-complex-systems claim, new."
  },
  {
   "claim_id": "C212",
   "loglog_ids": [
    "8.9"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Cannot-fork-country fact, new."
  },
  {
   "claim_id": "C213",
   "loglog_ids": [
    "8.10"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Voluntary-exit contrast, new."
  },
  {
   "claim_id": "C214",
   "loglog_ids": [
    "8.11"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Affectedness-right-to-see link, new."
  },
  {
   "claim_id": "C215",
   "loglog_ids": [
    "8.12"
   ],
   "label": "Duplicate",
   "canonical_id": "C012",
   "reasoning": "You-are-CEO closing restates citizen-principal claim in 3."
  },
  {
   "claim_id": "C216",
   "loglog_ids": [
    "9"
   ],
   "label": "Trivia",
   "canonical_id": null,
   "reasoning": "Appendix header counting sources; restated header with no substantive content."
  },
  {
   "claim_id": "C217",
   "loglog_ids": [
    "9.1"
   ],
   "label": "Duplicate",
   "canonical_id": "C026",
   "reasoning": "Register restates 1766 first-FOI-law claim from 5.2.1."
  },
  {
   "claim_id": "C218",
   "loglog_ids": [
    "9.2"
   ],
   "label": "Duplicate",
   "canonical_id": "C028",
   "reasoning": "Register restates Chydenius Hats-Caps origin from 5.2.3."
  },
  {
   "claim_id": "C219",
   "loglog_ids": [
    "9.3"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Adds 1998 start and 1996 leak dates absent from body."
  },
  {
   "claim_id": "C220",
   "loglog_ids": [
    "9.4"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Adds 16th-to-2nd rise and 2024 digitalization figure."
  },
  {
   "claim_id": "C221",
   "loglog_ids": [
    "9.5"
   ],
   "label": "Duplicate",
   "canonical_id": "C047",
   "reasoning": "Register restates 20M portal-visit figure from 5.5.2."
  },
  {
   "claim_id": "C222",
   "loglog_ids": [
    "9.6"
   ],
   "label": "Duplicate",
   "canonical_id": "C049",
   "reasoning": "Register restates 60GB/27-year pension find from 5.5.4."
  },
  {
   "claim_id": "C223",
   "loglog_ids": [
    "9.7"
   ],
   "label": "Duplicate",
   "canonical_id": "C032",
   "reasoning": "Register restates OPEN 70-task scope from 5.3.1."
  },
  {
   "claim_id": "C224",
   "loglog_ids": [
    "9.8"
   ],
   "label": "Duplicate",
   "canonical_id": "C036",
   "reasoning": "Register restates corruption-participation link from 5.3.5."
  },
  {
   "claim_id": "C225",
   "loglog_ids": [
    "9.9"
   ],
   "label": "Duplicate",
   "canonical_id": "C052",
   "reasoning": "Register restates 30-business-day cabinet window from 5.6.1."
  },
  {
   "claim_id": "C226",
   "loglog_ids": [
    "9.10"
   ],
   "label": "Duplicate",
   "canonical_id": "C056",
   "reasoning": "Register restates Pol.is mechanism from 5.7.1."
  },
  {
   "claim_id": "C227",
   "loglog_ids": [
    "9.11"
   ],
   "label": "Duplicate",
   "canonical_id": "C193",
   "reasoning": "Register restates Iceland rejected draft from 7.10.4."
  },
  {
   "claim_id": "C228",
   "loglog_ids": [
    "9.12"
   ],
   "label": "Duplicate",
   "canonical_id": "C072",
   "reasoning": "Register restates FREEDOM Act gains and limits from 6.13."
  },
  {
   "claim_id": "C229",
   "loglog_ids": [
    "9.13"
   ],
   "label": "Duplicate",
   "canonical_id": "C075",
   "reasoning": "Register restates GDPR acceleration from 6.16."
  },
  {
   "claim_id": "C230",
   "loglog_ids": [
    "9.14"
   ],
   "label": "Duplicate",
   "canonical_id": "C065",
   "reasoning": "Register restates 2020 illegality rulings from 6.6."
  },
  {
   "claim_id": "C231",
   "loglog_ids": [
    "9.15"
   ],
   "label": "Duplicate",
   "canonical_id": "C081",
   "reasoning": "Register restates Pew 66% figure from 7.1.1."
  },
  {
   "claim_id": "C232",
   "loglog_ids": [
    "9.16"
   ],
   "label": "Duplicate",
   "canonical_id": "C082",
   "reasoning": "Register restates ABC poll history from 7.1.2."
  },
  {
   "claim_id": "C233",
   "loglog_ids": [
    "9.17"
   ],
   "label": "Duplicate",
   "canonical_id": "C088",
   "reasoning": "Register restates IMF-Cambridge friction evidence from 7.2.1."
  },
  {
   "claim_id": "C234",
   "loglog_ids": [
    "9.18"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "World Bank mixed-impact and reversibility point absent from body."
  },
  {
   "claim_id": "C235",
   "loglog_ids": [
    "9.19"
   ],
   "label": "Duplicate",
   "canonical_id": "C099",
   "reasoning": "Register restates Oman backchannel from 7.3.2."
  },
  {
   "claim_id": "C236",
   "loglog_ids": [
    "9.20"
   ],
   "label": "Duplicate",
   "canonical_id": "C110",
   "reasoning": "Register restates 50-state lobbyist study from 7.4.2."
  },
  {
   "claim_id": "C237",
   "loglog_ids": [
    "9.21"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Oxford diplomacy-history survey absent from body."
  },
  {
   "claim_id": "C238",
   "loglog_ids": [
    "9.22"
   ],
   "label": "Duplicate",
   "canonical_id": "C110",
   "reasoning": "Register restates Harden-Kirkland study plus Irish trial figures."
  },
  {
   "claim_id": "C239",
   "loglog_ids": [
    "9.23"
   ],
   "label": "Duplicate",
   "canonical_id": "C125",
   "reasoning": "Register restates Brennan 735-official survey from 7.5.2."
  },
  {
   "claim_id": "C240",
   "loglog_ids": [
    "9.24"
   ],
   "label": "Duplicate",
   "canonical_id": "C129",
   "reasoning": "Register restates doxxing-swatting and AI harassment from 7.5.6."
  },
  {
   "claim_id": "C241",
   "loglog_ids": [
    "9.25"
   ],
   "label": "Duplicate",
   "canonical_id": "C140",
   "reasoning": "Register restates 22-state and Chicago poll figures from 7.6.2-7.6.4."
  },
  {
   "claim_id": "C242",
   "loglog_ids": [
    "9.26"
   ],
   "label": "Duplicate",
   "canonical_id": "C143",
   "reasoning": "Register restates Brennan overclassification and SIPRI trust from 7.6.5-7.6.6."
  },
  {
   "claim_id": "C243",
   "loglog_ids": [
    "9.27"
   ],
   "label": "Duplicate",
   "canonical_id": "C152",
   "reasoning": "Register restates 43-state populism dataset from 7.7.2."
  },
  {
   "claim_id": "C244",
   "loglog_ids": [
    "9.28"
   ],
   "label": "Duplicate",
   "canonical_id": "C157",
   "reasoning": "Register restates Stanford short-termism warning from 7.7.7."
  },
  {
   "claim_id": "C245",
   "loglog_ids": [
    "9.29"
   ],
   "label": "Duplicate",
   "canonical_id": "C167",
   "reasoning": "Register restates Harvard misinformation panel from 7.8.1."
  },
  {
   "claim_id": "C246",
   "loglog_ids": [
    "9.30"
   ],
   "label": "Duplicate",
   "canonical_id": "C194",
   "reasoning": "Register restates OGP 75-country autopsy from 7.10.5."
  },
  {
   "claim_id": "C247",
   "loglog_ids": [
    "9.31"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Hong 2024 and Ruijer 2020 sources absent from body."
  },
  {
   "claim_id": "C248",
   "loglog_ids": [
    "9.32"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Workaround-resistance study absent from body."
  },
  {
   "claim_id": "C249",
   "loglog_ids": [
    "9.33"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Nordicom five-regime comparison absent from body."
  },
  {
   "claim_id": "C250",
   "loglog_ids": [
    "9.34"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Finland 1999 public-by-default law absent from body."
  }
 ],
 "metrics": {
  "scored_claims": 250,
  "unique": 212,
  "duplicates": 36,
  "trivia": 2,
  "redundancy_rate": 0.144,
  "trivia_rate": 0.008,
  "structured_tokens": 296,
  "tokens_per_unique_claim": 1.396
 },
 "prune_list": [
  "C006 duplicates C001, safe to merge",
  "C084 duplicates C020, safe to merge",
  "C122 duplicates C118, safe to merge",
  "C133 duplicates C020, safe to merge",
  "C144 duplicates C064, safe to merge",
  "C174 duplicates C134, safe to merge",
  "C176 duplicates C016, safe to merge",
  "C177 duplicates C014, safe to merge",
  "C208 duplicates C205, safe to merge",
  "C215 duplicates C012, safe to merge",
  "C217 duplicates C026, register recap, safe to merge",
  "C218 duplicates C028, register recap, safe to merge",
  "C221 duplicates C047, register recap, safe to merge",
  "C222 duplicates C049, register recap, safe to merge",
  "C223 duplicates C032, register recap, safe to merge",
  "C224 duplicates C036, register recap, safe to merge",
  "C225 duplicates C052, register recap, safe to merge",
  "C226 duplicates C056, register recap, safe to merge",
  "C227 duplicates C193, register recap, safe to merge",
  "C228 duplicates C072, register recap, safe to merge",
  "C229 duplicates C075, register recap, safe to merge",
  "C230 duplicates C065, register recap, safe to merge",
  "C231 duplicates C081, register recap, safe to merge",
  "C232 duplicates C082, register recap, safe to merge",
  "C233 duplicates C088, register recap, safe to merge",
  "C235 duplicates C099, register recap, safe to merge",
  "C236 duplicates C110, register recap, safe to merge",
  "C238 duplicates C110, register recap, safe to merge",
  "C239 duplicates C125, register recap, safe to merge",
  "C240 duplicates C129, register recap, safe to merge",
  "C241 duplicates C140, register recap, safe to merge",
  "C242 duplicates C143, register recap, safe to merge",
  "C243 duplicates C152, register recap, safe to merge",
  "C244 duplicates C157, register recap, safe to merge",
  "C245 duplicates C167, register recap, safe to merge",
  "C246 duplicates C194, register recap, safe to merge",
  "C079 roadmap transition, trivia, safe to cut",
  "C216 appendix header count, trivia, safe to cut"
 ]
}
```

## Judge F (faithfulness), opencode-go/deepseek-v4.1-flash

```json
{
 "judge": "faithfulness",
 "judge_version": "1.0.0",
 "model": "opencode-go/deepseek-v4.1-flash (opencode) scripted pipeline 2026-09-15",
 "source_id": "02_case_for_transparent_government",
 "claims": [
  {
   "claim_id": "C001",
   "loglog_ids": [
    "0"
   ],
   "claim_text": "Citizens are governments' CEO-principals, so every decision should be fully documented and traceable, with objections answered and precedents proving feasibility.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "None",
   "evidence_quote": "every government decision should be fully documented and publicly available ... You are the principal ... Pieces of this system already exist",
   "reasoning": "Summary tracks the thesis, principal-agent framing, and the objections and precedents sections of the source."
  },
  {
   "claim_id": "C002",
   "loglog_ids": [
    "1"
   ],
   "claim_text": "A manager hiding a million-dollar decision would be fired, yet governments do the same.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "None",
   "evidence_quote": "You'd fire them. ... That's how your government operates.",
   "reasoning": "Source states the owner would fire the manager and later says government operates the same way."
  },
  {
   "claim_id": "C003",
   "loglog_ids": [
    "1.1"
   ],
   "claim_text": "Manager refused to explain a million-dollar decision, citing lost leverage.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "None",
   "evidence_quote": "If you know how I make these decisions, I lose my leverage.",
   "reasoning": "Direct paraphrase of the manager's quoted refusal about the million-dollar budget decision."
  },
  {
   "claim_id": "C004",
   "loglog_ids": [
    "1.2"
   ],
   "claim_text": "An owner would sue, force disclosure, and fire that manager.",
   "claim_type": "claim",
   "verdict": "Supported",
   "severity": "None",
   "evidence_quote": "You'd take them to court. You'd force disclosure. You'd fire them.",
   "reasoning": "Matches the source's three listed responses exactly."
  },
  {
   "claim_id": "C005",
   "loglog_ids": [
    "1.3"
   ],
   "claim_text": "Governments refuse with classified, security, operations, and speed excuses.",
   "claim_type": "claim",
   "verdict": "Supported",
   "severity": "None",
   "evidence_quote": "you're told it's classified. It's a matter of national security. It would compromise ongoing operations. It would slow things down.",
   "reasoning": "All four cited excuses map directly to the source's listed justifications."
  },
  {
   "claim_id": "C006",
   "loglog_ids": [
    "2"
   ],
   "claim_text": "Every government decision should be fully documented and publicly available.",
   "claim_type": "recommendation",
   "verdict": "Supported",
   "severity": "None",
   "evidence_quote": "every government decision should be fully documented and publicly available",
   "reasoning": "Verbatim restatement of the source's central proposition."
  },
  {
   "claim_id": "C007",
   "loglog_ids": [
    "2.1"
   ],
   "claim_text": "Document data used, considerations made, and who was involved.",
   "claim_type": "recommendation",
   "verdict": "Supported",
   "severity": "None",
   "evidence_quote": "What data was used ... What considerations were made ... Who was involved",
   "reasoning": "First three items of the source's chain list, preserved."
  },
  {
   "claim_id": "C008",
   "loglog_ids": [
    "2.2"
   ],
   "claim_text": "Document alternatives considered, arguments for and against, implementation steps.",
   "claim_type": "recommendation",
   "verdict": "Supported",
   "severity": "None",
   "evidence_quote": "What alternatives were considered ... arguments for and against ... How it will be implemented",
   "reasoning": "Maps to the middle items of the source's documentation chain list."
  },
  {
   "claim_id": "C009",
   "loglog_ids": [
    "2.3"
   ],
   "claim_text": "Document evaluation, course-correction plans, and reconsideration terms.",
   "claim_type": "recommendation",
   "verdict": "Supported",
   "severity": "None",
   "evidence_quote": "How it will be evaluated ... course-correction plans ... When and how it will be reconsidered, and what it takes to change it",
   "reasoning": "Covers the final items of the source's documentation chain list."
  },
  {
   "claim_id": "C010",
   "loglog_ids": [
    "2.4"
   ],
   "claim_text": "Competent boards and CEOs already demand this basic accountability.",
   "claim_type": "claim",
   "verdict": "Supported",
   "severity": "None",
   "evidence_quote": "This is what any competent board of directors expects ... It's what any CEO expects ... It's basic accountability.",
   "reasoning": "Aligns with the source's board, CEO, and basic accountability statements."
  },
  {
   "claim_id": "C011",
   "loglog_ids": [
    "2.5"
   ],
   "claim_text": "It sounds radical only because the opposite was normalized.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "None",
   "evidence_quote": "The only thing that makes it sound radical is that we've normalized the opposite.",
   "reasoning": "Near-verbatim, with the restrictive 'only' preserved as in the source."
  },
  {
   "claim_id": "C012",
   "loglog_ids": [
    "3"
   ],
   "claim_text": "In democracy citizens are principals; officials are their employee-agents.",
   "claim_type": "claim",
   "verdict": "Supported",
   "severity": "None",
   "evidence_quote": "You are the principal in a principal-agent relationship ... is an agent working on your behalf ... They are your employees.",
   "reasoning": "Faithfully captures the source's principal-agent and employees framing."
  },
  {
   "claim_id": "C013",
   "loglog_ids": [
    "3.1"
   ],
   "claim_text": "Every servant from licensing clerk to president works for you.",
   "claim_type": "claim",
   "verdict": "Supported",
   "severity": "None",
   "evidence_quote": "Every public servant, from the clerk at your local licensing office to the president, is an agent working on your behalf.",
   "reasoning": "Same endpoints and scope as the source span."
  },
  {
   "claim_id": "C014",
   "loglog_ids": [
    "3.2"
   ],
   "claim_text": "CEOs need not read everything, but reviewability shapes behavior.",
   "claim_type": "claim",
   "verdict": "Supported",
   "severity": "None",
   "evidence_quote": "The CEO doesn't read every email. But they *could*. And that knowledge - that anything could be reviewed at any time - shapes behavior.",
   "reasoning": "Preserves both the non-consumption point and the behavioral effect of reviewability."
  },
  {
   "claim_id": "C015",
   "loglog_ids": [
    "3.3"
   ],
   "claim_text": "A company letting managers classify emails would go bankrupt within a year.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "None",
   "evidence_quote": "That company would be bankrupt within a year, eaten alive by internal corruption and incompetence",
   "reasoning": "Timeline and outcome match the source's hypothetical exactly."
  },
  {
   "claim_id": "C016",
   "loglog_ids": [
    "3.4"
   ],
   "claim_text": "Availability matters, not consumption: trace decisions affecting your life.",
   "claim_type": "nuance",
   "verdict": "Supported",
   "severity": "None",
   "evidence_quote": "The distinction between \"availability\" and \"consumption\" is crucial ... if a decision affects your community, your livelihood, your children's future - you *can* trace it back.",
   "reasoning": "Reflects the source's availability-versus-consumption distinction and traceability point."
  },
  {
   "claim_id": "C017",
   "loglog_ids": [
    "4"
   ],
   "claim_text": "Transparency flows from government to citizens, never the reverse.",
   "claim_type": "definition",
   "verdict": "Supported",
   "severity": "None",
   "evidence_quote": "the government's decisions, data, and processes flow *to* citizens. Not the other way around.",
   "reasoning": "One-directional claim matches the source's directional definition and negation."
  },
  {
   "claim_id": "C018",
   "loglog_ids": [
    "4.1"
   ],
   "claim_text": "Decisions visible, processes traceable, officials accountable to citizens.",
   "claim_type": "definition",
   "verdict": "Supported",
   "severity": "None",
   "evidence_quote": "Government decisions being visible to citizens. Government processes being traceable by citizens. Government officials being accountable to citizens.",
   "reasoning": "Direct restatement of the source's 'This is about' list."
  },
  {
   "claim_id": "C019",
   "loglog_ids": [
    "4.2"
   ],
   "claim_text": "Not tax returns, medical records, or citizens surveilling each other.",
   "claim_type": "definition",
   "verdict": "Supported",
   "severity": "None",
   "evidence_quote": "This is NOT about: Your tax returns ... Your medical records being public. Citizens surveilling each other.",
   "reasoning": "Negated exclusions preserved exactly from the source's 'This is NOT about' list."
  },
  {
   "claim_id": "C020",
   "loglog_ids": [
    "4.3"
   ],
   "claim_text": "CEOs see work product, not employees' medical records.",
   "claim_type": "definition",
   "verdict": "Supported",
   "severity": "None",
   "evidence_quote": "The CEO sees employee work product. The CEO does not publish employees' medical records to angry customers.",
   "reasoning": "Preserves the work-product versus medical-records contrast and the negation."
  },
  {
   "claim_id": "C021",
   "loglog_ids": [
    "4.4"
   ],
   "claim_text": "Publish $X/$Y/$Z/$W spending, not John Smith's $47,000 taxes.",
   "claim_type": "example",
   "verdict": "Supported",
   "severity": "None",
   "evidence_quote": "spent it as follows: $Y on healthcare, $Z on defense, $W on infrastructure ... It does *not* mean: \"John Smith paid $47,000 in taxes last year.\"",
   "reasoning": "Example structure and the $47,000 figure match the source exactly."
  },
  {
   "claim_id": "C022",
   "loglog_ids": [
    "4.5"
   ],
   "claim_text": "Aggregation, anonymization, and differential privacy make separation technically straightforward.",
   "claim_type": "claim",
   "verdict": "Supported",
   "severity": "None",
   "evidence_quote": "Privacy-preserving approaches - aggregate data, anonymization, differential privacy - make this technically straightforward.",
   "reasoning": "All three named techniques and the 'straightforward' qualifier match the source."
  },
  {
   "claim_id": "C023",
   "loglog_ids": [
    "5"
   ],
   "claim_text": "Pieces of this system already exist and prove it works.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Pieces of this system already exist around the world... several have gone far enough to prove it works.",
   "reasoning": "SOURCE asserts existing pieces and that several cases prove it works; identical meaning."
  },
  {
   "claim_id": "C024",
   "loglog_ids": [
    "5.1"
   ],
   "claim_text": "No country nears complete transparency, but several prove feasibility.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "No country has achieved anything close to complete transparency, but several have gone far enough to prove it works.",
   "reasoning": "Direct paraphrase preserving the concession and the feasibility claim."
  },
  {
   "claim_id": "C025",
   "loglog_ids": [
    "5.2"
   ],
   "claim_text": "Sweden's 260-year openness shows transparency endures without collapse.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Two hundred and sixty years later, Sweden still operates under this principle... The country has not collapsed.",
   "reasoning": "260 years, endurance, and non-collapse are all stated in SOURCE."
  },
  {
   "claim_id": "C026",
   "loglog_ids": [
    "5.2.1"
   ],
   "claim_text": "In 1766 Sweden passed the world's first freedom-of-information law.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "In 1766, Sweden passed the Freedom of the Press Act - the world's first freedom of information law.",
   "reasoning": "Date and superlative match SOURCE exactly."
  },
  {
   "claim_id": "C027",
   "loglog_ids": [
    "5.2.2"
   ],
   "claim_text": "It abolished censorship and is now constitutional.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "It abolished censorship... It's now part of the Swedish constitution.",
   "reasoning": "Both facts appear verbatim in SOURCE."
  },
  {
   "claim_id": "C028",
   "loglog_ids": [
    "5.2.3"
   ],
   "claim_text": "Finnish-Swedish priest-politician Chydenius drove Hats-versus-Caps explicitly anti-corruption law.",
   "claim_type": "name_or_entity",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Anders Chydenius, a Finnish-Swedish priest and politician, drove the legislation through parliament. The motivation was explicitly anti-corruption.",
   "reasoning": "Name, roles, driving role, and anti-corruption motive all match; Hats/Caps context is adjacent."
  },
  {
   "claim_id": "C029",
   "loglog_ids": [
    "5.2.4"
   ],
   "claim_text": "Offentlighetsprincipen keeps documents public by default 260 years on.",
   "claim_type": "definition",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Two hundred and sixty years later, Sweden still operates under this principle. It's called offentlighetsprincipen... Government documents are public by default.",
   "reasoning": "Term, default-public rule, and 260-year persistence all stated."
  },
  {
   "claim_id": "C030",
   "loglog_ids": [
    "5.2.5"
   ],
   "claim_text": "Nordics consistently rank among least corrupt, most effective democracies.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Nordic countries consistently rank among the least corrupt and most effective democracies in the world.",
   "reasoning": "Near-verbatim restatement."
  },
  {
   "claim_id": "C031",
   "loglog_ids": [
    "5.3"
   ],
   "claim_text": "Seoul's 1999 OPEN system made bribery-prone permitting visible.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "In 1999, Seoul launched the OPEN system... shows citizens exactly who made what decision.",
   "reasoning": "Year and the visibility of corruption-prone tasks match."
  },
  {
   "claim_id": "C032",
   "loglog_ids": [
    "5.3.1"
   ],
   "claim_text": "OPEN tracks 70 corruption-prone tasks, including construction, environmental, and urban planning permits, in real time.",
   "claim_type": "number_or_date",
   "verdict": "Partially supported",
   "severity": "Minor",
   "evidence_quote": "tracks 70 municipal tasks most prone to corruption - construction permits, environmental regulation, urban planning - and shows citizens... in real time.",
   "reasoning": "Number 70 is correct, but SOURCE lists environmental regulation and urban planning, not permits, and ties real time to showing citizens."
  },
  {
   "claim_id": "C033",
   "loglog_ids": [
    "5.3.2"
   ],
   "claim_text": "Citizens see exactly who decided what at each process point.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "shows citizens exactly who made what decision, at which point in the process, in real time.",
   "reasoning": "Direct restatement of SOURCE."
  },
  {
   "claim_id": "C034",
   "loglog_ids": [
    "5.3.3"
   ],
   "claim_text": "Previously invisible processing let officials demand speed-up bribes unprovably.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "This opacity enabled bribery: officials could demand payments to \"move things along\" and nobody could prove it.",
   "reasoning": "Opacity-to-bribery causal link and unprovability all stated."
  },
  {
   "claim_id": "C035",
   "loglog_ids": [
    "5.3.4"
   ],
   "claim_text": "Visibility eliminated that bribery leverage entirely.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Making the process visible eliminated that leverage entirely.",
   "reasoning": "Verbatim in meaning."
  },
  {
   "claim_id": "C036",
   "loglog_ids": [
    "5.3.5"
   ],
   "claim_text": "Corruption decreases as e-participation increases; UN, OECD, World Bank recognized it.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "\"corruption decreases as e-participation increases.\" The system was recognized by the UN, OECD, and World Bank.",
   "reasoning": "Quote and the three recognizing bodies match SOURCE."
  },
  {
   "claim_id": "C037",
   "loglog_ids": [
    "5.4"
   ],
   "claim_text": "Estonia's 2001 X-Road proves transparency infrastructure scales.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "### Estonia: The Infrastructure Proof (2001)... If your objection is \"this can't scale,\" look at Estonia's X-Road.",
   "reasoning": "Year and scale-proof framing both supported."
  },
  {
   "claim_id": "C038",
   "loglog_ids": [
    "5.4.1"
   ],
   "claim_text": "X-Road links 929+ institutions, 1,887 systems, 3,000+ services, timestamped, signed, logged.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "connecting 929+ institutions, 1,887 information systems, and 3,000+ digital services. Every transaction is timestamped and cryptographically signed. All data access is logged.",
   "reasoning": "All three figures and the three properties match SOURCE."
  },
  {
   "claim_id": "C039",
   "loglog_ids": [
    "5.4.2"
   ],
   "claim_text": "Citizens can see who accessed their data and why.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Citizens can see who accessed their data and why.",
   "reasoning": "Verbatim."
  },
  {
   "claim_id": "C040",
   "loglog_ids": [
    "5.4.3"
   ],
   "claim_text": "Estonia ranks 2nd on the UN E-Government Development Index.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Estonia now ranks 2nd in the UN E-Government Development Index.",
   "reasoning": "Rank and index match."
  },
  {
   "claim_id": "C041",
   "loglog_ids": [
    "5.4.4"
   ],
   "claim_text": "No major breaches in over 20 years despite constant cyber attacks.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "The system has had no major security breaches in over 20 years, despite constant cyber attacks.",
   "reasoning": "Negation, duration, and qualifier preserved."
  },
  {
   "claim_id": "C042",
   "loglog_ids": [
    "5.4.5"
   ],
   "claim_text": "X-Road is MIT-licensed open source, deployed in 20+ countries.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "It's open source (MIT license) and deployed in 20+ countries.",
   "reasoning": "License and deployment count match."
  },
  {
   "claim_id": "C043",
   "loglog_ids": [
    "5.4.6"
   ],
   "claim_text": "X-Road proves every-email-available infrastructure is technically feasible.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "X-Road proves the \"every email available up the chain\" infrastructure is technically feasible.",
   "reasoning": "Identical claim in SOURCE."
  },
  {
   "claim_id": "C044",
   "loglog_ids": [
    "5.4.7"
   ],
   "claim_text": "The technology is feasible; the bottleneck is will.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "The technology is not the bottleneck. The will is.",
   "reasoning": "Meaning preserved."
  },
  {
   "claim_id": "C045",
   "loglog_ids": [
    "5.5"
   ],
   "claim_text": "Brazil's 2004 Transparency Portal follows all federal money.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "### Brazil: Following the Money (2004)... publishes all federal spending.",
   "reasoning": "Year heading and all-federal-spending scope match."
  },
  {
   "claim_id": "C046",
   "loglog_ids": [
    "5.5.1"
   ],
   "claim_text": "It publishes contracts, transfers, salaries, travel, and credit-card transactions.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "contracts, transfers, salaries, travel expenses, and government credit card transactions.",
   "reasoning": "All five categories match SOURCE."
  },
  {
   "claim_id": "C047",
   "loglog_ids": [
    "5.5.2"
   ],
   "claim_text": "The portal receives over 20 million accesses per year.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "It receives over 20 million accesses per year.",
   "reasoning": "Verbatim figure."
  },
  {
   "claim_id": "C048",
   "loglog_ids": [
    "5.5.3"
   ],
   "claim_text": "Transparency Card sent 20+ million notifications via 430,000+ active cards.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "over 430,000 active cards, 20+ million notifications sent.",
   "reasoning": "Both counts match."
  },
  {
   "claim_id": "C049",
   "loglog_ids": [
    "5.5.4"
   ],
   "claim_text": "Journalists uncovered 60GB of hidden pension payments spanning 27 years.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "they uncovered 60GB of hidden pension payment data going back 27 years.",
   "reasoning": "Amount and span match."
  },
  {
   "claim_id": "C050",
   "loglog_ids": [
    "5.5.5"
   ],
   "claim_text": "Give citizens CEO tools and they find the fraud.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "This is what happens when you give citizens the tools to be CEOs: they find the fraud.",
   "reasoning": "Restatement preserving meaning."
  },
  {
   "claim_id": "C051",
   "loglog_ids": [
    "5.6"
   ],
   "claim_text": "New Zealand publishes cabinet papers by default since 2019.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Since 2019, New Zealand has proactively published all Cabinet papers and minutes online.",
   "reasoning": "Year, actor, and default publishing match."
  },
  {
   "claim_id": "C052",
   "loglog_ids": [
    "5.6.1"
   ],
   "claim_text": "All papers and minutes appear online within 30 business days.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "all Cabinet papers and minutes online within 30 business days of decisions being made.",
   "reasoning": "Window and scope match."
  },
  {
   "claim_id": "C053",
   "loglog_ids": [
    "5.6.2"
   ],
   "claim_text": "Cabinet deliberations are typically the world's most protected government information.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "cabinet deliberations are typically the most protected category of government information anywhere in the world.",
   "reasoning": "Hedge 'typically' and superlative preserved."
  },
  {
   "claim_id": "C054",
   "loglog_ids": [
    "5.6.3"
   ],
   "claim_text": "Government has not halted; ministers still deliberate; citizens see why.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "The government has not ground to a halt. Ministers have not stopped deliberating. What has changed is that citizens can see why.",
   "reasoning": "All three negations and the affirmative claim preserved."
  },
  {
   "claim_id": "C055",
   "loglog_ids": [
    "5.7"
   ],
   "claim_text": "Taiwan's vTaiwan crowdsources laws through consensus-finding deliberation.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Taiwan's vTaiwan platform uses Pol.is to let citizens participate in policy deliberation... surfaces statements that find cross-group consensus.",
   "reasoning": "Actor, method, and consensus mechanism match."
  },
  {
   "claim_id": "C056",
   "loglog_ids": [
    "5.7.1"
   ],
   "claim_text": "Pol.is takes agree-disagree votes with no replies, surfacing cross-group consensus.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "vote agree or disagree (no replies allowed - this prevents flame wars), and an algorithm surfaces statements that find cross-group consensus.",
   "reasoning": "Voting mode, no-replies rule, and consensus surfacing all present."
  },
  {
   "claim_id": "C057",
   "loglog_ids": [
    "5.7.2"
   ],
   "claim_text": "By 2018, 26 issues processed; 80% led to government action.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "By 2018, 26 issues had been processed, and 80% led to government action.",
   "reasoning": "Year, count, and percentage match exactly."
  },
  {
   "claim_id": "C058",
   "loglog_ids": [
    "5.7.3"
   ],
   "claim_text": "Participation is downstream of transparency, not core transparency itself.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "This isn't core transparency - it's what becomes possible downstream of transparency.",
   "reasoning": "Negation and downstream framing preserved."
  },
  {
   "claim_id": "C059",
   "loglog_ids": [
    "6"
   ],
   "claim_text": "Secret programs recur as illegal; secret oversight reliably fails to catch them.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "a recurring pattern in which government programs, shielded by secrecy, are later revealed to be illegal or built on lies... secret oversight reliably fails to prevent illegal secret programs",
   "reasoning": "Source asserts the recurring illegality pattern and reliable oversight failure. Dropped 'or built on lies' is harmless compression."
  },
  {
   "claim_id": "C060",
   "loglog_ids": [
    "6.1"
   ],
   "claim_text": "In 1971 Pentagon Papers showed government knew Vietnam was unwinnable while publicly claiming progress.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "In 1971, the Pentagon Papers revealed that the US government knew the Vietnam War was unwinnable while publicly claiming progress.",
   "reasoning": "Loglog restates the source sentence with year, actor, and claim intact."
  },
  {
   "claim_id": "C061",
   "loglog_ids": [
    "6.2"
   ],
   "claim_text": "Media, Pennsylvania break-in exposed COINTELPRO's illegal surveillance and disruption.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "activists broke into an FBI office in Media, Pennsylvania, and exposed COINTELPRO - a program of illegal surveillance, infiltration, and disruption",
   "reasoning": "Location, target, and program attributes match the source exactly."
  },
  {
   "claim_id": "C062",
   "loglog_ids": [
    "6.3"
   ],
   "claim_text": "COINTELPRO targeted civil rights leaders and political dissidents.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "targeting civil rights leaders and political dissidents",
   "reasoning": "Direct restatement of the source's target list."
  },
  {
   "claim_id": "C063",
   "loglog_ids": [
    "6.4"
   ],
   "claim_text": "In 2013 Snowden revealed bulk metadata collection from millions of Americans, PRISM, and leader surveillance.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "In 2013, Edward Snowden leaked classified documents revealing the NSA was bulk-collecting phone metadata from millions of Americans... through PRISM, and surveilling foreign leaders",
   "reasoning": "Year, actor, bulk collection, PRISM, and foreign-leader surveillance match the source."
  },
  {
   "claim_id": "C064",
   "loglog_ids": [
    "6.5"
   ],
   "claim_text": "Each disclosure was predicted catastrophic yet revealed illegality, unconstitutionality, or deliberate deception.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "In each case, the government predicted catastrophe from disclosure. In each case, the programs turned out to be illegal, unconstitutional, or based on deliberate deception",
   "reasoning": "The paired source sentences directly assert both the catastrophe prediction and the revealed outcomes."
  },
  {
   "claim_id": "C065",
   "loglog_ids": [
    "6.6"
   ],
   "claim_text": "In September 2020 the Ninth Circuit ruled bulk collection illegal, possibly unconstitutional.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "In September 2020, the US Ninth Circuit Court of Appeals ruled that the NSA's bulk phone record collection was illegal and possibly unconstitutional.",
   "reasoning": "Court, date, and both qualifiers match the source."
  },
  {
   "claim_id": "C066",
   "loglog_ids": [
    "6.7"
   ],
   "claim_text": "The court required FISA relevance to a particular authorized investigation.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "the government failed to satisfy FISA's requirement to show \"relevance to a particular authorized investigation.\"",
   "reasoning": "Quoted FISA requirement is reproduced accurately."
  },
  {
   "claim_id": "C067",
   "loglog_ids": [
    "6.8"
   ],
   "claim_text": "Stone found no evidence bulk collection stopped any terror attacks.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Geoffrey R. Stone, found \"no evidence that the bulk collection of phone data had stopped any terror attacks.\"",
   "reasoning": "The finding and attribution to Stone match the source quote."
  },
  {
   "claim_id": "C068",
   "loglog_ids": [
    "6.9"
   ],
   "claim_text": "The NSA abandoned the program in 2018: it no longer made sense.",
   "claim_type": "number_or_date",
   "verdict": "Partially supported",
   "severity": "Minor",
   "evidence_quote": "The NSA itself reportedly abandoned the program in 2018, telling the White House it \"no longer made sense.\"",
   "reasoning": "Node states as flat fact what source hedges with 'reportedly', dropping the attribution qualifier."
  },
  {
   "claim_id": "C069",
   "loglog_ids": [
    "6.10"
   ],
   "claim_text": "FISA courts, committees, and inspectors general failed inside the secrecy structure.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "The FISA court, congressional intelligence committees, and inspectors general all existed. They failed because they operated inside the secrecy structure",
   "reasoning": "All three oversight bodies and the failure cause match the source."
  },
  {
   "claim_id": "C070",
   "loglog_ids": [
    "6.11"
   ],
   "claim_text": "Secret oversight can be captured, co-opted, or worn down institutionally.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Oversight that is itself secret is oversight that can be captured, co-opted, or simply worn down by institutional pressure.",
   "reasoning": "Node reproduces the source's three mechanisms and the 'can' hedge."
  },
  {
   "claim_id": "C071",
   "loglog_ids": [
    "6.12"
   ],
   "claim_text": "The 2015 USA FREEDOM Act first reined in NSA spying in over 30 years.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "The USA FREEDOM Act (2015) became the first legislation to rein in NSA spying in over 30 years.",
   "reasoning": "Year, statute, and the 30-year first characterize the source verbatim."
  },
  {
   "claim_id": "C072",
   "loglog_ids": [
    "6.13"
   ],
   "claim_text": "It ended bulk metadata collection and required releasing significant FISC opinions.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "It ended bulk collection of phone metadata and required the Foreign Intelligence Surveillance Court to release significant opinions.",
   "reasoning": "Both effects match the source; FISC is the source's named court."
  },
  {
   "claim_id": "C073",
   "loglog_ids": [
    "6.14"
   ],
   "claim_text": "The tech sector adopted transparency reporting on data requests.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "The tech sector adopted transparency reporting on government data requests.",
   "reasoning": "Direct restatement of the source claim."
  },
  {
   "claim_id": "C074",
   "loglog_ids": [
    "6.15"
   ],
   "claim_text": "HTTPS became default on most websites.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "HTTPS encryption became the default on most websites.",
   "reasoning": "Verbatim match including the 'most websites' scope."
  },
  {
   "claim_id": "C075",
   "loglog_ids": [
    "6.16"
   ],
   "claim_text": "The EU's GDPR was accelerated by the revelations.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "The EU's GDPR was accelerated by the revelations.",
   "reasoning": "Direct restatement of the causal claim."
  },
  {
   "claim_id": "C076",
   "loglog_ids": [
    "6.17"
   ],
   "claim_text": "Operational harm is genuinely uncertain; illegality is not.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Whether these disclosures caused operational harm is genuinely uncertain... But the legality question is not uncertain. The programs were illegal.",
   "reasoning": "Node preserves both the uncertainty and its contrast with settled illegality."
  },
  {
   "claim_id": "C077",
   "loglog_ids": [
    "6.18"
   ],
   "claim_text": "Snowden is the symptom of absent designed-in transparency, not the solution.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Snowden is not the solution. Snowden is the symptom of a system where the only alternative to permanent secrecy is uncontrolled disclosure.",
   "reasoning": "Node keeps both negations and maps 'absence of a model' to designed-in transparency."
  },
  {
   "claim_id": "C078",
   "loglog_ids": [
    "6.19"
   ],
   "claim_text": "Designed-in traceability would surface illegality early without bulk-leak damage.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Designed-in transparency - where citizens can trace decisions by default - would have made the illegal programs visible before they scaled, without the collateral damage of a bulk leak.",
   "reasoning": "Early visibility and avoided bulk-leak damage match the source claim closely."
  },
  {
   "claim_id": "C079",
   "loglog_ids": [
    "7"
   ],
   "claim_text": "Ten objections follow, some power-protecting, some genuinely concerned; each gets honest engagement.",
   "claim_type": "meta",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Some come from officials protecting their power. But some come from citizens with genuine concerns. These deserve honest engagement.",
   "reasoning": "Source names both objection sources and promises honest engagement; ten subsequent headings enumerate ten objections."
  },
  {
   "claim_id": "C080",
   "loglog_ids": [
    "7.1"
   ],
   "claim_text": "Privacy objection: transparency will violate my privacy.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "### \"My Privacy Will Be Violated\"",
   "reasoning": "Matches the source heading naming the privacy objection."
  },
  {
   "claim_id": "C081",
   "loglog_ids": [
    "7.1.1"
   ],
   "claim_text": "2019 Pew: 66% fear collection, 64% fear use, 6% very confident.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "66% of Americans are concerned about government data collection, and 64% are concerned about how the government uses their data. Only 6% are \"very confident\"",
   "reasoning": "All three percentages and the 2019 Pew attribution match the source exactly."
  },
  {
   "claim_id": "C082",
   "loglog_ids": [
    "7.1.2"
   ],
   "claim_text": "A 2000 ABC poll: 86% said agencies should not publish such records online.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "2000 ABC News poll ... 86% said government agencies should *not* make public records ... available online.",
   "reasoning": "Date, percentage, and the negation about publishing records online all match."
  },
  {
   "claim_id": "C083",
   "loglog_ids": [
    "7.1.3"
   ],
   "claim_text": "Polls fear citizen data held by government, not visible government decisions.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "fear about *citizen data* held by government. Not fear about *government decisions* being visible to citizens.",
   "reasoning": "Direct restatement of the source's distinction, including the negation."
  },
  {
   "claim_id": "C084",
   "loglog_ids": [
    "7.1.4"
   ],
   "claim_text": "Quarterly-report review differs from publishing employee health records.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "The CEO reviewing quarterly reports is not the same as the CEO publishing employee health records.",
   "reasoning": "Paraphrase preserves the source's comparison and negation."
  },
  {
   "claim_id": "C085",
   "loglog_ids": [
    "7.1.5"
   ],
   "claim_text": "$50 million infrastructure-allocation transparency needs no neighbor's personal data.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "allocate $50 million in infrastructure spending. It does not mean: \"Here is the personal information of every citizen...\"",
   "reasoning": "Amount and the contrast with personal data match the source."
  },
  {
   "claim_id": "C086",
   "loglog_ids": [
    "7.1.6"
   ],
   "claim_text": "Bundled record systems should be separated, not kept wholly secret.",
   "claim_type": "recommendation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "the solution is to separate them, not to keep everything secret.",
   "reasoning": "Direct restatement preserving the separation recommendation and negation."
  },
  {
   "claim_id": "C087",
   "loglog_ids": [
    "7.2"
   ],
   "claim_text": "Objection: if every action is public, deliberation dies and processes paralyze.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "if every action is public, deliberation becomes impossible. Officials will be afraid to propose ideas. Processes will be paralyzed.",
   "reasoning": "Tracks the source's stated fear about deliberation and paralysis."
  },
  {
   "claim_id": "C088",
   "loglog_ids": [
    "7.2.1"
   ],
   "claim_text": "Cambridge found EU transparency-deliberation tension; IMF called government a friction-forcing fortress.",
   "claim_type": "name_or_entity",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "A Cambridge study ... found tension between transparent deliberation and efficient decision-making. An IMF analysis ... \"is not a sports car - it's a fortress\"",
   "reasoning": "Both attributions and characterizations match the source."
  },
  {
   "claim_id": "C089",
   "loglog_ids": [
    "7.2.2"
   ],
   "claim_text": "IMF: friction forces accountability and catches errors before harm.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "\"friction forces accountability\" and \"catches errors before they cause harm.\"",
   "reasoning": "Both quoted phrases reproduce the source verbatim."
  },
  {
   "claim_id": "C090",
   "loglog_ids": [
    "7.2.3"
   ],
   "claim_text": "Robodebt: 470,000 incorrect notices and a $1.8 billion settlement.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "470,000 incorrect debt notices and a $1.8 billion settlement.",
   "reasoning": "Numbers and entity match; dropping the word debt is harmless compression."
  },
  {
   "claim_id": "C091",
   "loglog_ids": [
    "7.2.4"
   ],
   "claim_text": "This confuses decision speed with decision documentation.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "this concern confuses two things: the speed of decision-making and the documentation of decision-making.",
   "reasoning": "Identical meaning to the source's distinction."
  },
  {
   "claim_id": "C092",
   "loglog_ids": [
    "7.2.5"
   ],
   "claim_text": "Document at current speed; fix burdensome systems, keep accountability.",
   "claim_type": "recommendation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "documenting what happens at the current speed ... If documentation is burdensome, you improve the documentation systems - you don't abandon accountability.",
   "reasoning": "Preserves both the documentation-at-current-speed point and the fix-systems recommendation."
  },
  {
   "claim_id": "C093",
   "loglog_ids": [
    "7.2.6"
   ],
   "claim_text": "CEOs demand documented work, not slower work.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "The CEO doesn't demand employees work slower. The CEO demands employees document their work.",
   "reasoning": "Direct restatement preserving the negation about speed."
  },
  {
   "claim_id": "C094",
   "loglog_ids": [
    "7.2.7"
   ],
   "claim_text": "New Zealand's 30-day cabinet papers halted nothing; reasoning stands verifiable.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "New Zealand publishes cabinet papers within 30 days. Their government hasn't ground to a halt ... citizens can verify whether the reasoning was sound.",
   "reasoning": "30-day figure and both consequences match this source passage."
  },
  {
   "claim_id": "C095",
   "loglog_ids": [
    "7.2.8"
   ],
   "claim_text": "Opacity makes decisions unaccountable random walks, not better ones.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "opacity doesn't make decisions *better* - it just makes them *unaccountable* ... Nobody notices the random walk",
   "reasoning": "Restates the source's contrast and random-walk image with the negation intact."
  },
  {
   "claim_id": "C096",
   "loglog_ids": [
    "7.2.9"
   ],
   "claim_text": "Documented consistency pressure prevents reversals and speeds decisions long-term.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Transparency creates pressure for logical consistency, which in the long run actually improves decision-making speed by preventing costly reversals",
   "reasoning": "Preserves the causal claim linking consistency pressure to fewer reversals and speed."
  },
  {
   "claim_id": "C097",
   "loglog_ids": [
    "7.3"
   ],
   "claim_text": "Objection: diplomacy requires secrecy.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "### \"Diplomacy Requires Secrecy\"",
   "reasoning": "Matches the source heading naming the diplomacy objection."
  },
  {
   "claim_id": "C098",
   "loglog_ids": [
    "7.3.1"
   ],
   "claim_text": "Conceded: the most legitimate concern, deserving nuance.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "This is the most legitimate concern, and it deserves nuance.",
   "reasoning": "Direct restatement of the concession."
  },
  {
   "claim_id": "C099",
   "loglog_ids": [
    "7.3.2"
   ],
   "claim_text": "JCPOA began in 2012 via Sullivan's secret Oman backchannel.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "negotiations began in 2012 with a secret backchannel. Jake Sullivan secretly traveled to Oman",
   "reasoning": "Year, name Jake Sullivan, and Oman backchannel all match."
  },
  {
   "claim_id": "C100",
   "loglog_ids": [
    "7.3.3"
   ],
   "claim_text": "Camp David 1978 and Cold War backchannels likewise needed private space.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "The Camp David Accords (1978) similarly required private space for compromise. Cold War backchannels",
   "reasoning": "1978 attribution and the private-space point match."
  },
  {
   "claim_id": "C101",
   "loglog_ids": [
    "7.3.4"
   ],
   "claim_text": "Democratic dilemma: secrecy enables flexibility, but barren without consent.",
   "claim_type": "definition",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "\"negotiations can be flexible and successful only if they are kept secret, but they will be barren without popular consent.\"",
   "reasoning": "Faithful compression of the quoted democratic dilemma."
  },
  {
   "claim_id": "C102",
   "loglog_ids": [
    "7.3.5"
   ],
   "claim_text": "CEOs allow confidential negotiation, then demand full disclosure afterward.",
   "claim_type": "recommendation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "A CEO may authorize a negotiation team to keep details confidential *during* the negotiation. But the CEO expects full disclosure once it concludes.",
   "reasoning": "Preserves both the during-negotiation confidentiality and post-conclusion disclosure."
  },
  {
   "claim_id": "C103",
   "loglog_ids": [
    "7.3.6"
   ],
   "claim_text": "Disclose afterward what was offered, conceded, why, and alternatives.",
   "claim_type": "recommendation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "what was offered, what was conceded, why, what alternatives were considered.",
   "reasoning": "Lists exactly the source's disclosure items."
  },
  {
   "claim_id": "C104",
   "loglog_ids": [
    "7.3.7"
   ],
   "claim_text": "Temporary secrecy during talks is acceptable; permanent secrecy is not.",
   "claim_type": "recommendation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "*Temporary operational secrecy during active negotiations* may be acceptable. *Permanent secrecy about what was decided and why* is not.",
   "reasoning": "Reproduces the source's acceptability distinction and negation."
  },
  {
   "claim_id": "C105",
   "loglog_ids": [
    "7.3.8"
   ],
   "claim_text": "Release full documentation 30-90 days after conclusion for evaluation.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Full documentation released after conclusion (e.g., 30-90 days) ... Citizens can evaluate whether negotiators served their interests",
   "reasoning": "30-90 day window and evaluation purpose match."
  },
  {
   "claim_id": "C106",
   "loglog_ids": [
    "7.3.9"
   ],
   "claim_text": "Foreign-refusal arguments let non-principals veto citizens' oversight.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "It makes citizens' oversight contingent on foreign governments' preferences. But foreign governments are not the principals here.",
   "reasoning": "Captures the source's point that foreign preferences would condition citizens' oversight."
  },
  {
   "claim_id": "C107",
   "loglog_ids": [
    "7.3.10"
   ],
   "claim_text": "Foreign governments are not the principals; citizens are.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "foreign governments are not the principals here. You are.",
   "reasoning": "Direct restatement preserving the negation."
  },
  {
   "claim_id": "C108",
   "loglog_ids": [
    "7.4"
   ],
   "claim_text": "Objection: special interests benefit more than ordinary citizens.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "### \"Special Interests Will Benefit More Than Ordinary Citizens\"",
   "reasoning": "Matches the source heading naming the special-interest objection."
  },
  {
   "claim_id": "C109",
   "loglog_ids": [
    "7.4.1"
   ],
   "claim_text": "Conceded: empirically grounded and worth taking seriously.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "This is an empirically grounded concern that you should take seriously.",
   "reasoning": "Direct restatement of the concession."
  },
  {
   "claim_id": "C110",
   "loglog_ids": [
    "7.4.2"
   ],
   "claim_text": "Harden and Kirkland studied all 50 legislatures over multiple decades.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "studied all 50 US state legislatures over multiple decades.",
   "reasoning": "Count and scope match exactly."
  },
  {
   "claim_id": "C111",
   "loglog_ids": [
    "7.4.3"
   ],
   "claim_text": "Notre Dame-Virginia scholars' Illusion of Accountability compares open versus closed meetings using surveys versus outcomes.",
   "claim_type": "name_or_entity",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Jeff Harden (University of Notre Dame) and Justin Kirkland (University of Virginia) ... *The Illusion of Accountability* ... compared states with open versus closed legislative meetings, using survey data on policy preferences versus actual policy outcomes.",
   "reasoning": "Affiliations, book title, and method all match the source."
  },
  {
   "claim_id": "C112",
   "loglog_ids": [
    "7.4.4"
   ],
   "claim_text": "More lobbyists register and donate, yet policy-opinion correlation stays same open or closed.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "more lobbying groups register ... Lobbyists donate more to incumbents. And public policy's correlation with public opinion is *the same* whether meetings are open or closed.",
   "reasoning": "All three findings match the source."
  },
  {
   "claim_id": "C113",
   "loglog_ids": [
    "7.4.5"
   ],
   "claim_text": "Harden: the laws improve representation for unrepresentative interest groups, not citizens.",
   "claim_type": "name_or_entity",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "\"The laws don't make citizen representation better, they make it better for interest groups, which aren't representative of the general public.\"",
   "reasoning": "Faithful to the quoted Harden statement and its negation."
  },
  {
   "claim_id": "C114",
   "loglog_ids": [
    "7.4.6"
   ],
   "claim_text": "Arnold (1990): open markups advantage organized interests over inattentive citizens.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Princeton's Douglas Arnold (1990) observed ... \"Open markup sessions often give organized interests a powerful advantage over inattentive citizens.\"",
   "reasoning": "Year, name, and quoted claim all match."
  },
  {
   "claim_id": "C115",
   "loglog_ids": [
    "7.4.7"
   ],
   "claim_text": "Ireland 2024: 569 participants; lobbying transparency did not raise trust.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "2024 survey experiment in Ireland ... with 569 participants found that citizens exposed to lobbying information don't develop more positive evaluations of trust",
   "reasoning": "Year, count, and the negative finding match."
  },
  {
   "claim_id": "C116",
   "loglog_ids": [
    "7.4.8"
   ],
   "claim_text": "Asymmetry is the problem: paid monitors versus busy citizens.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "the *asymmetry* is the problem. Lobbyists are paid to monitor government.",
   "reasoning": "Direct restatement of the source's asymmetry point."
  },
  {
   "claim_id": "C117",
   "loglog_ids": [
    "7.4.9"
   ],
   "claim_text": "Lobbyists wield staff, expertise, and capacity; citizens have jobs and families.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "They have professional staff, legal expertise, and organizational capacity. Citizens have jobs, families, and finite attention.",
   "reasoning": "Faithful list of the source's stated asymmetries."
  },
  {
   "claim_id": "C118",
   "loglog_ids": [
    "7.4.10"
   ],
   "claim_text": "Build citizen capacity: auditors, watchdogs, journalism, civic tech.",
   "claim_type": "recommendation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "hire auditors, create oversight committees ... fund watchdog organizations, support investigative journalism, build civic technology.",
   "reasoning": "Matches the source's capacity-building recommendations."
  },
  {
   "claim_id": "C119",
   "loglog_ids": [
    "7.4.11"
   ],
   "claim_text": "Brazil's Fiquem Sabendo files 2,000-3,000 FOI requests yearly for citizens.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Brazil's Fiquem Sabendo files 2,000-3,000 FOI requests per year on behalf of citizens.",
   "reasoning": "Name and request count match exactly."
  },
  {
   "claim_id": "C120",
   "loglog_ids": [
    "7.4.12"
   ],
   "claim_text": "A robust and competitive electoral environment is the real key.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "\"the real key to quality representation is a robust and competitive electoral environment.\"",
   "reasoning": "Direct quotation with correct attribution to Harden and Kirkland."
  },
  {
   "claim_id": "C121",
   "loglog_ids": [
    "7.4.13"
   ],
   "claim_text": "Opacity guarantees no accountability; transparency makes it possible.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Opacity *guarantees* no accountability. Transparency at least makes accountability *possible*.",
   "reasoning": "Reproduces the source's contrast and negation."
  },
  {
   "claim_id": "C122",
   "loglog_ids": [
    "7.4.14"
   ],
   "claim_text": "Build usage capacity rather than reducing information.",
   "claim_type": "recommendation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "The answer is to build capacity, not reduce information.",
   "reasoning": "Direct restatement preserving the not-reduce-information negation."
  },
  {
   "claim_id": "C123",
   "loglog_ids": [
    "7.5"
   ],
   "claim_text": "Objection: public officials will face harassment.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "### \"Public Officials Will Be Harassed\"",
   "reasoning": "Matches the source heading naming the harassment objection."
  },
  {
   "claim_id": "C124",
   "loglog_ids": [
    "7.5.1"
   ],
   "claim_text": "Conceded: real, documented, and growing.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "This concern is real, documented, and growing.",
   "reasoning": "Direct restatement of the concession."
  },
  {
   "claim_id": "C125",
   "loglog_ids": [
    "7.5.2"
   ],
   "claim_text": "Brennan surveyed 735 local election officials, February-March 2024, weighted by region and jurisdiction size, margin ±3%.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "surveyed 735 local election officials between February and March 2024 (weighted by region and jurisdiction size, margin of error ±3%)",
   "reasoning": "All figures and methodology details match the source."
  },
  {
   "claim_id": "C126",
   "loglog_ids": [
    "7.5.3"
   ],
   "claim_text": "38% threatened; over half fear for colleagues; over 1 in 4 fear assault.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "38% experienced threats ... More than half are concerned about the safety of colleagues ... More than 1 in 4 worry about being assaulted",
   "reasoning": "All three statistics match the source's survey list."
  },
  {
   "claim_id": "C127",
   "loglog_ids": [
    "7.5.4"
   ],
   "claim_text": "34% know someone who resigned, up from 22% in 2023.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "34% know someone who resigned due to safety concerns (up from 22% in 2023)",
   "reasoning": "Both percentages and the 2023 comparison match."
  },
  {
   "claim_id": "C128",
   "loglog_ids": [
    "7.5.5"
   ],
   "claim_text": "61% of the threatened were threatened in person or by phone.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "61% of those threatened received threats in person or by phone",
   "reasoning": "Percentage and channel detail match the source."
  },
  {
   "claim_id": "C129",
   "loglog_ids": [
    "7.5.6"
   ],
   "claim_text": "2024: doxxing and swatting evolved into sophisticated technology-enabled harassment tools.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "reported in 2024 that doxxing and swatting have \"evolved into sophisticated, technology-enabled tools of harassment,\"",
   "reasoning": "Year and quoted characterization match the NAAG report."
  },
  {
   "claim_id": "C130",
   "loglog_ids": [
    "7.5.7"
   ],
   "claim_text": "AI and automated scraping intensify scale, precision, and anonymity.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "AI and automated data scraping intensifying \"the scale, precision, and anonymity\" of attacks.",
   "reasoning": "Matches the source's quoted list and agents."
  },
  {
   "claim_id": "C131",
   "loglog_ids": [
    "7.5.8"
   ],
   "claim_text": "Since 2022, 22 states passed protections for election officials.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Since 2022, 22 states have passed protections for election officials.",
   "reasoning": "Year and state count match exactly."
  },
  {
   "claim_id": "C132",
   "loglog_ids": [
    "7.5.9"
   ],
   "claim_text": "Publish who decided what and why; protect addresses, families, schedules.",
   "claim_type": "recommendation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Transparency of decisions (who decided what, based on what reasoning) should be public. Personal information of officials (home addresses, family members, daily schedules) should be protected.",
   "reasoning": "Preserves both the public-decisions and protected-details distinction."
  },
  {
   "claim_id": "C133",
   "loglog_ids": [
    "7.5.10"
   ],
   "claim_text": "CEOs review work product, not employees' home addresses.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "The CEO does not publish employees' home addresses to angry customers. Accountability for work product is not the same as personal vulnerability.",
   "reasoning": "Faithful to the source's distinction and negation."
  },
  {
   "claim_id": "C134",
   "loglog_ids": [
    "7.5.11"
   ],
   "claim_text": "Current harassment feeds on opacity-bred fraud conspiracies.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "much of the *current* harassment stems from *lack* of transparency. Election officials are harassed because of conspiracy theories about fraud.",
   "reasoning": "Preserves the source's causal link between opacity and harassment."
  },
  {
   "claim_id": "C135",
   "loglog_ids": [
    "7.5.12"
   ],
   "claim_text": "Documented audits, custody chains, and counts would starve conspiracies.",
   "claim_type": "causal_link",
   "verdict": "Partially supported",
   "severity": "Minor",
   "evidence_quote": "the conspiracy theories would have less room to grow",
   "reasoning": "Source says conspiracies would have less room to grow; node strengthens to starve, an absolute elimination claim."
  },
  {
   "claim_id": "C136",
   "loglog_ids": [
    "7.5.13"
   ],
   "claim_text": "Protect individuals more while making processes more transparent.",
   "claim_type": "recommendation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "better protection for individuals, combined with *more* transparency about processes.",
   "reasoning": "Direct restatement of the source's dual recommendation."
  },
  {
   "claim_id": "C137",
   "loglog_ids": [
    "7.6"
   ],
   "claim_text": "Objection: national security forbids transparency.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "### \"National Security!\"",
   "reasoning": "Matches the source heading for the national security objection."
  },
  {
   "claim_id": "C138",
   "loglog_ids": [
    "7.6.1"
   ],
   "claim_text": "This objection is used most and scrutinized least.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "This is the objection that gets used most often and scrutinized least.",
   "reasoning": "Direct restatement of the source."
  },
  {
   "claim_id": "C139",
   "loglog_ids": [
    "7.6.2"
   ],
   "claim_text": "Chicago 2020-2022: roughly 60% call intelligence vital.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "surveyed Americans in 2020 and 2022 and found that roughly 60% agree the intelligence community \"plays a vital role\"",
   "reasoning": "Years, percentage, and attribution match."
  },
  {
   "claim_id": "C140",
   "loglog_ids": [
    "7.6.3"
   ],
   "claim_text": "A majority say it could share more without harming effectiveness.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "a majority also agreed the IC \"could share more information with the American people without compromising effectiveness.\"",
   "reasoning": "Faithful to the quoted survey result."
  },
  {
   "claim_id": "C141",
   "loglog_ids": [
    "7.6.4"
   ],
   "claim_text": "Civil-liberties threat perception rose from 12% in 2021 to 17% in 2022.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "rising (from 12% in 2021 to 17% in 2022)",
   "reasoning": "Both percentages and years match exactly."
  },
  {
   "claim_id": "C142",
   "loglog_ids": [
    "7.6.5"
   ],
   "claim_text": "Brennan: far too much is classified; secrecy undermines democratic self-government.",
   "claim_type": "name_or_entity",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "\"federal officials and outside experts agree that far too much information is classified.\" And: \"excessive secrecy ... undermines the basic functions of democratic self-government.\"",
   "reasoning": "Both quoted Brennan Center statements match."
  },
  {
   "claim_id": "C143",
   "loglog_ids": [
    "7.6.6"
   ],
   "claim_text": "SIPRI: military transparency builds inter-state trust and prevents waste.",
   "claim_type": "name_or_entity",
   "verdict": "Partially supported",
   "severity": "Minor",
   "evidence_quote": "\"transparency in military matters is generally considered essential for building trust between states\" and \"can help prevent wasteful spending.\"",
   "reasoning": "Node states absolutes; source hedges with generally considered, essential, and can help prevent."
  },
  {
   "claim_id": "C144",
   "loglog_ids": [
    "7.6.7"
   ],
   "claim_text": "Snowden proved catastrophe predictions wrong and programs illegal.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "The government predicted catastrophe. Independent research found minimal impact. The court found the programs *illegal*.",
   "reasoning": "Node summarizes the source's claim that predicted catastrophe did not materialize and programs were illegal."
  },
  {
   "claim_id": "C145",
   "loglog_ids": [
    "7.6.8"
   ],
   "claim_text": "Independent research found minimal impact; reforms improved civil liberties.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Independent research found minimal impact. ... The reforms improved civil liberties.",
   "reasoning": "Direct restatement of both source statements."
  },
  {
   "claim_id": "C146",
   "loglog_ids": [
    "7.6.9"
   ],
   "claim_text": "Flip the burden: transparent by default, secrecy needs proof.",
   "claim_type": "recommendation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "almost everything is transparent by default, and officials must prove their need for secrecy.",
   "reasoning": "Faithful to the source's proposed burden reversal."
  },
  {
   "claim_id": "C147",
   "loglog_ids": [
    "7.6.10"
   ],
   "claim_text": "Temporary classification fits active operations; strategy, doctrine, budgets, procurement, and rules stay open.",
   "claim_type": "recommendation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "The CEO may authorize temporary classification during an operation. ... Strategy, doctrine, budget, procurement, rules of engagement should always be transparent.",
   "reasoning": "Matches the temporary-classification exception and open-by-default list."
  },
  {
   "claim_id": "C148",
   "loglog_ids": [
    "7.6.11"
   ],
   "claim_text": "The label hides embarrassment, illegality, incompetence, and corruption.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "The \"national security\" label is overused to hide embarrassing decisions, illegal activities (as Snowden revealed), bureaucratic incompetence, and corruption.",
   "reasoning": "Faithful compression of the source's list."
  },
  {
   "claim_id": "C149",
   "loglog_ids": [
    "7.6.12"
   ],
   "claim_text": "Officials under scrutiny set secrecy criteria: a conflict of interest.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Currently, the officials whose decisions might be scrutinized. That's a conflict of interest.",
   "reasoning": "Direct restatement of the source's conflict-of-interest point."
  },
  {
   "claim_id": "C150",
   "loglog_ids": [
    "7.7"
   ],
   "claim_text": "Objection: populists will weaponize transparency.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "### \"Populists Will Weaponize Transparency\"",
   "reasoning": "Matches the source heading naming the populism objection."
  },
  {
   "claim_id": "C151",
   "loglog_ids": [
    "7.7.1"
   ],
   "claim_text": "Conceded: sophisticated and research-backed.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "This is a sophisticated concern backed by real research.",
   "reasoning": "Direct restatement of the concession."
  },
  {
   "claim_id": "C152",
   "loglog_ids": [
    "7.7.2"
   ],
   "claim_text": "Kyle-Gultchin studied 43 democracies, 1990-2018, Polity IV at least 6, leaders journal-screened.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "studying populist governments in 43 democratic countries between 1990 and 2018 (leaders classified through academic journal screening, countries coded as democratic using Polity IV score ≥6)",
   "reasoning": "All figures and methodological details match."
  },
  {
   "claim_id": "C153",
   "loglog_ids": [
    "7.7.3"
   ],
   "claim_text": "Populists are 4x likelier to damage institutions: 23% versus 6%.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Populist governments are 4x more likely to damage democratic institutions (23% vs 6% of non-populists)",
   "reasoning": "Multiplier and both percentages match."
  },
  {
   "claim_id": "C154",
   "loglog_ids": [
    "7.7.4"
   ],
   "claim_text": "Countries fall 5 places on corruption perceptions; top-half starters fall 11.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Countries fall an average of 5 places ... Countries starting in the top half fall an average of 11 places",
   "reasoning": "Both figures match the source."
  },
  {
   "claim_id": "C155",
   "loglog_ids": [
    "7.7.5"
   ],
   "claim_text": "Venezuela dropped 83 places under Chávez.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "(Venezuela dropped 83 under Chávez)",
   "reasoning": "Country, figure, and leader match exactly."
  },
  {
   "claim_id": "C156",
   "loglog_ids": [
    "7.7.6"
   ],
   "claim_text": "Over 50% amended or rewrote constitutions; populists rule 6.5 versus 3 years.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Over 50% of populist leaders amended or rewrote constitutions ... Populists hold office twice as long ... (6.5 vs 3 years)",
   "reasoning": "Both the 50% figure and the 6.5 vs 3 years match."
  },
  {
   "claim_id": "C157",
   "loglog_ids": [
    "7.7.7"
   ],
   "claim_text": "Stanford: visibility-driven re-election tempts short-term populist policies.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "\"when re-election hinges on immediate visibility rather than long-term strategy, leaders may opt for populist policies\"",
   "reasoning": "Faithful compression of the quoted Stanford argument."
  },
  {
   "claim_id": "C158",
   "loglog_ids": [
    "7.7.8"
   ],
   "claim_text": "Sweden Democrats repurposed FOI and alternative media against elites.",
   "claim_type": "name_or_entity",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "the Sweden Democrats ... have \"strategically repurposed\" transparency mechanisms, using freedom of information ... while leveraging alternative media",
   "reasoning": "Party, mechanism, and media all match."
  },
  {
   "claim_id": "C159",
   "loglog_ids": [
    "7.7.9"
   ],
   "claim_text": "They expose scandals to erode trust in traditional elites.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "using freedom of information to expose scandals and erode trust in traditional elites",
   "reasoning": "Direct restatement of the source phrase."
  },
  {
   "claim_id": "C160",
   "loglog_ids": [
    "7.7.10"
   ],
   "claim_text": "Causality is backwards: populists damage democracy by reducing transparency.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "the causal story is backwards. The research shows populists *damage* democracy - and they do so by *reducing* transparency, not increasing it.",
   "reasoning": "Preserves the causal reversal and the not-increasing negation."
  },
  {
   "claim_id": "C161",
   "loglog_ids": [
    "7.7.11"
   ],
   "claim_text": "Cherry-picking works only while the full record stays hidden.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "This works precisely because *not everything* is visible. In a fully transparent system, selective leaking loses its power.",
   "reasoning": "Faithful to the source's visibility-dependent explanation."
  },
  {
   "claim_id": "C162",
   "loglog_ids": [
    "7.7.12"
   ],
   "claim_text": "Electoral cycles cause short-termism with or without transparency.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "the \"short-term thinking\" problem exists with or without transparency. Electoral cycles create short-term incentives regardless.",
   "reasoning": "Direct restatement of the source."
  },
  {
   "claim_id": "C163",
   "loglog_ids": [
    "7.7.13"
   ],
   "claim_text": "Documented long-term rationale makes unpopular-but-wise decisions defensible.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "An unpopular decision with documented reasoning is defensible.",
   "reasoning": "Direct restatement of the source."
  },
  {
   "claim_id": "C164",
   "loglog_ids": [
    "7.7.14"
   ],
   "claim_text": "Evaluating reasoning, not just outcomes, is populism's antidote.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Transparency enables evaluation of *reasoning*, not just outcomes. And that's the antidote to populism, not its enabler.",
   "reasoning": "Both negations and the antidote claim match."
  },
  {
   "claim_id": "C165",
   "loglog_ids": [
    "7.7.15"
   ],
   "claim_text": "CEOs want documented reasoning, not merely popular decisions.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "The CEO doesn't want employees to make only *popular* decisions. The CEO wants employees to make *documented* decisions with clear reasoning.",
   "reasoning": "Faithful restatement with the only-popular contrast preserved."
  },
  {
   "claim_id": "C166",
   "loglog_ids": [
    "7.8"
   ],
   "claim_text": "Objection: misinformation makes transparency pointless.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "### \"Misinformation Makes Transparency Pointless\"",
   "reasoning": "Matches the source heading naming the misinformation objection."
  },
  {
   "claim_id": "C167",
   "loglog_ids": [
    "7.8.1"
   ],
   "claim_text": "Harvard 2023: Canadian panel; COVID-19 false beliefs lower perceived transparency.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "study published in the Harvard Kennedy School Misinformation Review (2023, based on a Canadian panel survey) found that people who endorse false beliefs (specifically COVID-19 related) perceive government as *less* transparent",
   "reasoning": "Year, venue, sample, and finding all match."
  },
  {
   "claim_id": "C168",
   "loglog_ids": [
    "7.8.2"
   ],
   "claim_text": "This holds controlling for real transparency levels.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "This holds even when controlling for real transparency.",
   "reasoning": "Direct restatement."
  },
  {
   "claim_id": "C169",
   "loglog_ids": [
    "7.8.3"
   ],
   "claim_text": "Negative transparency perceptions cut voting, trust, and democratic satisfaction.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "negative transparency perceptions are associated with decline in voting intentions, trust, and satisfaction with democracy.",
   "reasoning": "Close paraphrase preserving the three associated declines."
  },
  {
   "claim_id": "C170",
   "loglog_ids": [
    "7.8.4"
   ],
   "claim_text": "Citizens prize transparency's idea but dislike disclosures' messy content.",
   "claim_type": "interpretation",
   "verdict": "Partially supported",
   "severity": "Minor",
   "evidence_quote": "citizens value the *idea* of transparency but may react negatively to the *content* of actual disclosures",
   "reasoning": "Source hedges with may react negatively; node states the dislike as settled fact."
  },
  {
   "claim_id": "C171",
   "loglog_ids": [
    "7.8.5"
   ],
   "claim_text": "So-why-bother does not follow from these findings.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "the conclusion drawn from them - \"so why bother?\" - doesn't follow.",
   "reasoning": "Direct restatement preserving the negation."
  },
  {
   "claim_id": "C172",
   "loglog_ids": [
    "7.8.6"
   ],
   "claim_text": "False beliefs drive perceived opacity, not the reverse.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "false beliefs lead to perceived non-transparency. It does *not* show: actual transparency leads to more false beliefs.",
   "reasoning": "Preserves both the causal direction and the negation."
  },
  {
   "claim_id": "C173",
   "loglog_ids": [
    "7.8.7"
   ],
   "claim_text": "Opacity enables false beliefs; secrecy vacuums breed speculation.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "opacity *enables* false beliefs ... Speculation flourishes where documentation doesn't exist.",
   "reasoning": "Faithful to both source claims."
  },
  {
   "claim_id": "C174",
   "loglog_ids": [
    "7.8.8"
   ],
   "claim_text": "Election conspiracies grow where processes stay opaque.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Election conspiracy theories grow precisely because *some* processes remain opaque.",
   "reasoning": "Direct restatement preserving the some qualifier's sense."
  },
  {
   "claim_id": "C175",
   "loglog_ids": [
    "7.8.9"
   ],
   "claim_text": "Full documentation gives checkable ground truth for false claims.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Transparency provides ground truth. If full documentation exists, false claims can be checked against reality.",
   "reasoning": "Direct restatement of the source."
  },
  {
   "claim_id": "C176",
   "loglog_ids": [
    "7.8.10"
   ],
   "claim_text": "Latent availability deters misconduct even without consumption.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Availability changes behavior even without consumption. The knowledge that the record exists deters misconduct.",
   "reasoning": "Matches the source's availability-deters-misconduct claim."
  },
  {
   "claim_id": "C177",
   "loglog_ids": [
    "7.8.11"
   ],
   "claim_text": "CEOs need not read every email to benefit from access.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "The CEO doesn't read every email but values that they *could*.",
   "reasoning": "Faithful restatement preserving the negation."
  },
  {
   "claim_id": "C178",
   "loglog_ids": [
    "7.8.12"
   ],
   "claim_text": "Persistent transparency builds trust through consistently matching reality.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Persistent, comprehensive transparency creates a verifiable track record. Trust emerges when the disclosed information consistently matches reality.",
   "reasoning": "Direct restatement of the trust-building mechanism."
  },
  {
   "claim_id": "C179",
   "loglog_ids": [
    "7.8.13"
   ],
   "claim_text": "Pair transparency with accessibility, explanation, and intermediary translators.",
   "claim_type": "recommendation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "accompanied by accessibility, explanation, and intermediaries (journalists, civic tech, educators) who translate raw data",
   "reasoning": "Matches the source's recommended accompaniments."
  },
  {
   "claim_id": "C180",
   "loglog_ids": [
    "7.9"
   ],
   "claim_text": "Objection: markets will be manipulated by early disclosures.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "### \"Markets Will Be Manipulated\"",
   "reasoning": "Matches the source heading naming the markets objection."
  },
  {
   "claim_id": "C181",
   "loglog_ids": [
    "7.9.1"
   ],
   "claim_text": "Trade positions and monetary deliberations invite trader exploitation.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "doesn't publishing its positions undermine the negotiation? ... couldn't traders exploit advance knowledge?",
   "reasoning": "Faithful restatement of the source's two rhetorical concerns."
  },
  {
   "claim_id": "C182",
   "loglog_ids": [
    "7.9.2"
   ],
   "claim_text": "Conceded: valid but narrow; answer is delayed, not permanent, secrecy.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "This concern is valid but narrow. The solution isn't permanent secrecy. It's time-delayed transparency.",
   "reasoning": "Preserves the concession and the not-permanent negation."
  },
  {
   "claim_id": "C183",
   "loglog_ids": [
    "7.9.3"
   ],
   "claim_text": "The Fed releases minutes in three weeks, transcripts in five years.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "The US Federal Reserve releases FOMC minutes with a three-week delay and full transcripts with a five-year delay.",
   "reasoning": "Delays and entity match."
  },
  {
   "claim_id": "C184",
   "loglog_ids": [
    "7.9.4"
   ],
   "claim_text": "TTIP failed amid backlash from citizens feeling excluded by secrecy.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "The EU's failed TTIP trade negotiations actually suffered from *too much* secrecy - public backlash grew partly because citizens felt excluded",
   "reasoning": "Faithful to the source, including the partly qualifier's sense."
  },
  {
   "claim_id": "C185",
   "loglog_ids": [
    "7.9.5"
   ],
   "claim_text": "All information goes public eventually; only timing is managed.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "all information eventually becomes public. Timing may be managed for specific categories",
   "reasoning": "Direct restatement of the source."
  },
  {
   "claim_id": "C186",
   "loglog_ids": [
    "7.9.6"
   ],
   "claim_text": "Monetary waits for implementation, trade for conclusion, procurement for award.",
   "claim_type": "recommendation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "monetary policy (delay until implementation), trade negotiations (delay until conclusion), procurement (delay until contract award)",
   "reasoning": "All three category delays match."
  },
  {
   "claim_id": "C187",
   "loglog_ids": [
    "7.9.7"
   ],
   "claim_text": "Procurement secrecy lets officials favor connected contractors.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "If bidding processes are opaque, officials can favor connected contractors with impunity.",
   "reasoning": "Faithful restatement of the source."
  },
  {
   "claim_id": "C188",
   "loglog_ids": [
    "7.9.8"
   ],
   "claim_text": "Brazil's contract sunlight specifically prevents procurement fraud.",
   "claim_type": "name_or_entity",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Brazil's Transparency Portal includes contract information specifically because sunlight in procurement prevents fraud.",
   "reasoning": "Direct restatement with correct entity."
  },
  {
   "claim_id": "C189",
   "loglog_ids": [
    "7.10"
   ],
   "claim_text": "Objection: those in power will never allow this.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "### \"Those in Power Will Never Allow This\"",
   "reasoning": "Matches the source heading naming the power objection."
  },
  {
   "claim_id": "C190",
   "loglog_ids": [
    "7.10.1"
   ],
   "claim_text": "That describes the political challenge, not a principled objection.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "This is the concern that isn't really an objection. It's a description of the political challenge.",
   "reasoning": "Direct restatement preserving both negations."
  },
  {
   "claim_id": "C191",
   "loglog_ids": [
    "7.10.2"
   ],
   "claim_text": "Iceland 2008: 950 citizens set values; 25-member politician-free council drafted.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "After the 2008 financial crisis, 950 randomly selected citizens identified constitutional values. A 25-person council (explicitly excluding politicians) drafted a new constitution",
   "reasoning": "Year, both counts, and the politician exclusion match."
  },
  {
   "claim_id": "C192",
   "loglog_ids": [
    "7.10.3"
   ],
   "claim_text": "3,600 social-media comments; unanimous council; two-thirds referendum approval.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "3,600 public comments via social media. The draft was approved unanimously by the council and by a two-thirds majority in a national referendum.",
   "reasoning": "All three details match."
  },
  {
   "claim_id": "C193",
   "loglog_ids": [
    "7.10.4"
   ],
   "claim_text": "Parliament refused to ratify the draft.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "And then the existing parliament refused to ratify it.",
   "reasoning": "Direct restatement."
  },
  {
   "claim_id": "C194",
   "loglog_ids": [
    "7.10.5"
   ],
   "claim_text": "OGP: 75 countries, 4,500+ commitments since 2011; one-third delayed for funding.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Open Government Partnership (75 countries, 4,500+ commitments since 2011) found that one-third of delayed commitments fail due to \"lack of funding and technical capacity.\"",
   "reasoning": "All figures and the funding cause match."
  },
  {
   "claim_id": "C195",
   "loglog_ids": [
    "7.10.6"
   ],
   "claim_text": "Coordination failures, weak support, and transitions kill the rest.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "\"poor institutional coordination, lack of political support, and discontinuity from one administration to another during political transitions.\"",
   "reasoning": "Faithful compression of the source's listed remaining causes."
  },
  {
   "claim_id": "C196",
   "loglog_ids": [
    "7.10.7"
   ],
   "claim_text": "Successor governments abandon predecessors' transparency promises.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "new governments abandon their predecessors' transparency promises.",
   "reasoning": "Direct restatement."
  },
  {
   "claim_id": "C197",
   "loglog_ids": [
    "7.10.8"
   ],
   "claim_text": "Conceded: opacity's beneficiaries will always resist.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Those who benefit from opacity ... will resist transparency. They will always resist.",
   "reasoning": "Direct restatement of the concession."
  },
  {
   "claim_id": "C198",
   "loglog_ids": [
    "7.10.9"
   ],
   "claim_text": "Threatening the powerful is the point, not a flaw.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "It's a statement that transparency threatens the powerful. Which is exactly the point.",
   "reasoning": "Direct restatement preserving the negation."
  },
  {
   "claim_id": "C199",
   "loglog_ids": [
    "7.10.10"
   ],
   "claim_text": "Sweden 1766, post-Watergate, and post-2008 Iceland opened reform windows.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Sweden 1766 ... Post-Watergate US: scandal created a window for reform. Post-2008 Iceland: financial crisis created demand",
   "reasoning": "All three precedents match the source list."
  },
  {
   "claim_id": "C200",
   "loglog_ids": [
    "7.10.11"
   ],
   "claim_text": "Iceland's parliament ultimately blocked implementation despite the crisis.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "even though the existing parliament ultimately blocked implementation",
   "reasoning": "Direct restatement."
  },
  {
   "claim_id": "C201",
   "loglog_ids": [
    "7.10.12"
   ],
   "claim_text": "Ask who works for whom, not whether politicians permit oversight.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "The current framing asks: \"Will politicians allow this?\" That's the wrong question. The CEO framing asks: \"Who works for whom?\"",
   "reasoning": "Faithful restatement of the source's reframing."
  },
  {
   "claim_id": "C202",
   "loglog_ids": [
    "7.10.13"
   ],
   "claim_text": "This is a governance-design problem, not permission-seeking.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "This is a governance design problem, not a permission-seeking problem.",
   "reasoning": "Direct restatement preserving the negation."
  },
  {
   "claim_id": "C203",
   "loglog_ids": [
    "8"
   ],
   "claim_text": "Transparency is the measuring stick, not one value among many.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Transparency is not a value to be balanced. It's the measuring stick.",
   "reasoning": "Source rejects treating transparency as one value among many and names it the measuring stick."
  },
  {
   "claim_id": "C204",
   "loglog_ids": [
    "8.1"
   ],
   "claim_text": "Reject balancing transparency against efficiency, security, privacy, or speed.",
   "claim_type": "recommendation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "to \"balance\" it against efficiency, security, privacy, and speed ... Reject this framing.",
   "reasoning": "Source lists the same four values and explicitly rejects the balancing framing."
  },
  {
   "claim_id": "C205",
   "loglog_ids": [
    "8.2"
   ],
   "claim_text": "Speed and accountability are byproducts; document everything, then improve.",
   "claim_type": "recommendation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Speed and accountability are *byproducts*. Whatever speed your government operates at, document everything ... iteratively improve the processes",
   "reasoning": "Source states byproducts and instructs documenting everything then improving revealed processes."
  },
  {
   "claim_id": "C206",
   "loglog_ids": [
    "8.3"
   ],
   "claim_text": "The record pressures consistency, reasoning, accountability, and prosecution.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "pressure for consistency, pressure for sound reasoning, pressure for accountability ... easier to prosecute.",
   "reasoning": "Source lists exactly these pressures plus easier prosecution of corruption."
  },
  {
   "claim_id": "C207",
   "loglog_ids": [
    "8.4"
   ],
   "claim_text": "Reviewable officials reason better; documented decisions grow careful.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Officials who know their reasoning will be reviewed will produce better reasoning. Decisions that must be documented will be more carefully considered.",
   "reasoning": "Direct paraphrase of the two source sentences with identical meaning."
  },
  {
   "claim_id": "C208",
   "loglog_ids": [
    "8.5"
   ],
   "claim_text": "Reaching 100% transparency solves speed and accountability as consequences.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "In order to reach 100% transparency, you'll have to solve speed and accountability along the way ... they're consequences of it.",
   "reasoning": "Source says solving speed and accountability is required and labels them consequences, matching the claim."
  },
  {
   "claim_id": "C209",
   "loglog_ids": [
    "8.6"
   ],
   "claim_text": "Linux: thousands worldwide, every commit, issue, and pull request visible.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Linux ... built by thousands of people across the world ... Every commit is visible. Every issue is tracked. Every pull request is discussed.",
   "reasoning": "Source attributes these exact features to Linux and its worldwide contributors."
  },
  {
   "claim_id": "C210",
   "loglog_ids": [
    "8.7"
   ],
   "claim_text": "Disagreeing users can fork the project.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "If you disagree with a decision, you can fork the project.",
   "reasoning": "Near-verbatim restatement of the source sentence about forking."
  },
  {
   "claim_id": "C211",
   "loglog_ids": [
    "8.8"
   ],
   "claim_text": "Complex collaborative systems can be built and maintained publicly.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "complex systems can be built and maintained in public",
   "reasoning": "Source asserts this general principle about complex systems built in public."
  },
  {
   "claim_id": "C212",
   "loglog_ids": [
    "8.9"
   ],
   "claim_text": "Government is involuntary: you cannot fork your country.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "In government, you're subject to decisions whether you participated or not. You can't fork your country.",
   "reasoning": "Source states both the involuntary subjection and the inability to fork one's country."
  },
  {
   "claim_id": "C213",
   "loglog_ids": [
    "8.10"
   ],
   "claim_text": "Open source is voluntary exit; government binds non-participants.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "in open source, participation is voluntary. You can leave. In government, you're subject to decisions whether you participated or not.",
   "reasoning": "Claim matches the source contrast between voluntary exit and binding government decisions."
  },
  {
   "claim_id": "C214",
   "loglog_ids": [
    "8.11"
   ],
   "claim_text": "Less choice about affectedness means more right to see.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "The less choice you have about being affected by decisions, the more right you have to see how those decisions are made.",
   "reasoning": "Direct rephrasing of the source's proportional statement with same meaning."
  },
  {
   "claim_id": "C215",
   "loglog_ids": [
    "8.12"
   ],
   "claim_text": "You pay, live with consequences, and are CEO: act like it.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "You pay for this government. You live with its consequences. You are the CEO. Act like it.",
   "reasoning": "Compression of the four source sentences into one, preserving all propositions."
  },
  {
   "claim_id": "C216",
   "loglog_ids": [
    "9"
   ],
   "claim_text": "Appendix registers 49 sources backing the case.",
   "claim_type": "meta",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Appendix: Sources with Summaries ... 49. [Finnish Ministry of Justice - Act on Openness of Government Activities]",
   "reasoning": "Source appendix lists numbered sources 1 through 49."
  },
  {
   "claim_id": "C217",
   "loglog_ids": [
    "9.1"
   ],
   "claim_text": "UNESCO lists the 1766 ordinance as first free-communication legislation.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "UNESCO recognition of the 1766 act as world's first legislation guaranteeing free communication of information",
   "reasoning": "Source states UNESCO recognizes it as first such legislation."
  },
  {
   "claim_id": "C218",
   "loglog_ids": [
    "9.2"
   ],
   "claim_text": "GWU archive marks the FOI act's 250th anniversary; Britannica covers the 1766 act's Hats-Caps-Chydenius origins.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "George Washington University archive documenting the 250th anniversary of the world's first FOI act ... origins in the political conflict between Hats and Caps parties; role of Anders Chydenius",
   "reasoning": "Source describes both the 250th anniversary archive and the Hats-Caps-Chydenius origins."
  },
  {
   "claim_id": "C219",
   "loglog_ids": [
    "9.3"
   ],
   "claim_text": "X-Road official specs plus wiki history: 1998 start, 2001 launch, 1996 leak.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "history (started 1998, launched 2001), architecture decisions, 1996 data leak",
   "reasoning": "All three dates match source exactly."
  },
  {
   "claim_id": "C220",
   "loglog_ids": [
    "9.4"
   ],
   "claim_text": "Estonia's 30-year journey rose 16th to 2nd, hitting 100% digitalization in 2024; Brazil's 2004 CGU portal holds five categories.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "rise from 16th to 2nd ... 100% digitalization milestone in 2024 ... portal in 2004 by CGU; details five data categories",
   "reasoning": "Source matches all figures: 30-year, 16th to 2nd, 2024, 2004, five categories."
  },
  {
   "claim_id": "C221",
   "loglog_ids": [
    "9.5"
   ],
   "claim_text": "OECD logs 20+ million yearly portal visits and 17-source 2018 integration.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "portal accessed 20+ million times yearly; describes 2018 data warehouse integration of 17 sources",
   "reasoning": "Numbers and year match source."
  },
  {
   "claim_id": "C222",
   "loglog_ids": [
    "9.6"
   ],
   "claim_text": "Fiquem Sabendo's LAI probe surfaced 60GB over 27 years of former presidents.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Fiquem Sabendo used LAI to uncover 60GB of hidden pension payment data spanning 27 years of former presidents",
   "reasoning": "Actor, volume, and span match source."
  },
  {
   "claim_id": "C223",
   "loglog_ids": [
    "9.7"
   ],
   "claim_text": "OPEN launched April 1999 under Mayor Goh, covering 70 tasks.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "OPEN system launched April 1999 under Mayor Goh's anti-corruption campaign; covers 70 municipal tasks",
   "reasoning": "Date, actor, and count match source."
  },
  {
   "claim_id": "C224",
   "loglog_ids": [
    "9.8"
   ],
   "claim_text": "Peer-reviewed OPEN study confirms corruption falls as e-participation rises.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Peer-reviewed study ... confirms corruption decreases with e-participation",
   "reasoning": "Source states the same inverse relationship."
  },
  {
   "claim_id": "C225",
   "loglog_ids": [
    "9.9"
   ],
   "claim_text": "NZ guidance plus DPMC: 30-business-day cabinet releases from January 2019.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "details 30 business day requirement from January 2019",
   "reasoning": "Requirement and start date match source."
  },
  {
   "claim_id": "C226",
   "loglog_ids": [
    "9.10"
   ],
   "claim_text": "Taiwan's Pol.is crowdsourced Uber rules; paper traces Sunflower 2014, Tang, g0v.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "details Uber regulation as first test case ... traces origins to 2014 Sunflower Movement; analyzes Audrey Tang's role and g0v community",
   "reasoning": "Uber case, 2014, Tang, and g0v all appear in source."
  },
  {
   "claim_id": "C227",
   "loglog_ids": [
    "9.11"
   ],
   "claim_text": "Iceland analyses cover rejected crowdsourced draft and deliberative quality.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "why parliament rejected the crowdsourced draft despite referendum approval ... assessment of the deliberative quality",
   "reasoning": "Both analyses described match source."
  },
  {
   "claim_id": "C228",
   "loglog_ids": [
    "9.12"
   ],
   "claim_text": "EFF's 10-year Snowden review details FREEDOM Act gains and limits.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "10-year retrospective ... details USA FREEDOM Act passage and limitations",
   "reasoning": "Source matches on both gains and limitations."
  },
  {
   "claim_id": "C229",
   "loglog_ids": [
    "9.13"
   ],
   "claim_text": "IAPP review links disclosures to legal change and GDPR acceleration.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "legal and policy changes triggered by disclosures; notes GDPR acceleration",
   "reasoning": "Source states the same linkage."
  },
  {
   "claim_id": "C230",
   "loglog_ids": [
    "9.14"
   ],
   "claim_text": "TechCrunch and ACLU cover 2020 illegality rulings and privacy victory.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "2020 court ruling that NSA program was illegal ... ACLU attorney calls ruling \"a victory for privacy rights\"",
   "reasoning": "Both outlets and characterizations match source."
  },
  {
   "claim_id": "C231",
   "loglog_ids": [
    "9.15"
   ],
   "claim_text": "Pew 2019: 66% concerned; Roper tracks 1950s-present transparency opinion.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "66% concerned about government data collection ... from 1950s to present",
   "reasoning": "Percentage and period match source."
  },
  {
   "claim_id": "C232",
   "loglog_ids": [
    "9.16"
   ],
   "claim_text": "Roper adds ABC and Freedom Forum poll history on openness.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "includes ABC News and Freedom Forum poll data",
   "reasoning": "Both poll sources named in source."
  },
  {
   "claim_id": "C233",
   "loglog_ids": [
    "9.17"
   ],
   "claim_text": "IMF defends friction as accountability; Cambridge studies EU legitimacy perceptions.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "intentional accountability design ... transparency affects how public perceives decision-making legitimacy",
   "reasoning": "Both the IMF argument and Cambridge finding match source."
  },
  {
   "claim_id": "C234",
   "loglog_ids": [
    "9.18"
   ],
   "claim_text": "World Bank reviews mixed transparency impacts incumbents can undo.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "mixed findings on effectiveness; notes incumbents can undo positive effects of information",
   "reasoning": "Source states both mixed findings and incumbent reversal."
  },
  {
   "claim_id": "C235",
   "loglog_ids": [
    "9.19"
   ],
   "claim_text": "Harvard details Oman's Iran backchannel; Oxford frames the democratic dilemma.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "secret backchannel in Oman in achieving framework before public talks ... frames the \"democratic dilemma\"",
   "reasoning": "Both Harvard Oman detail and Oxford dilemma appear in source."
  },
  {
   "claim_id": "C236",
   "loglog_ids": [
    "9.20"
   ],
   "claim_text": "Notre Dame release: transparency aids lobbyists across 50 states, decades studied.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "transparency benefits lobbyists more than citizens in US state legislatures; ... multi-decade study of 50 states",
   "reasoning": "Source supports lobbyist benefit and 50-state multi-decade scope."
  },
  {
   "claim_id": "C237",
   "loglog_ids": [
    "9.21"
   ],
   "claim_text": "Oxford surveys diplomacy's secrecy evolution from antiquity to modernity.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "traces historical evolution from ancient diplomacy to modern era",
   "reasoning": "Source matches the ancient-to-modern scope."
  },
  {
   "claim_id": "C238",
   "loglog_ids": [
    "9.22"
   ],
   "claim_text": "Harden-Kirkland book blames electoral competition gaps; Irish 2024 trial had 569 subjects.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "proposes electoral competition as the key variable ... 2024 experimental study with 569 participants in Ireland",
   "reasoning": "Key variable and 569 participants match source."
  },
  {
   "claim_id": "C239",
   "loglog_ids": [
    "9.23"
   ],
   "claim_text": "Brennan 2024: 735 officials, threats rising since 2020, 38% threatened, ±3% margin.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "survey of 735 officials ... since 2020; 38% report threats; margin of error ±3%",
   "reasoning": "Sample size, trend, percentage, and margin match source."
  },
  {
   "claim_id": "C240",
   "loglog_ids": [
    "9.24"
   ],
   "claim_text": "NAAG tracks doxxing-swatting systematization and AI intensification.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "evolution from fringe behavior to systematic harassment; notes AI intensification",
   "reasoning": "Source states systematization and AI intensification."
  },
  {
   "claim_id": "C241",
   "loglog_ids": [
    "9.25"
   ],
   "claim_text": "Issue One counts 22 protective states since 2022; Chicago finds ~60% support, 12% to 17% wariness in 2021-2022.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "across 22 states since 2022 ... general support (~60%) but increasing civil liberties concerns (12% to 17% 2021-2022)",
   "reasoning": "State count, support level, and concern range match source."
  },
  {
   "claim_id": "C242",
   "loglog_ids": [
    "9.26"
   ],
   "claim_text": "Brennan decries overclassification; SIPRI links military openness to trust.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "classification levels far exceed genuine security needs ... military budget transparency ... builds inter-state trust",
   "reasoning": "Source supports overclassification critique and transparency-trust link."
  },
  {
   "claim_id": "C243",
   "loglog_ids": [
    "9.27"
   ],
   "claim_text": "Blair Institute: 43 states 1990-2018, populists 4x damaging, 5-place corruption slide.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "43 countries (1990-2018) ... 4x more likely to damage democratic institutions; countries fall average 5 places",
   "reasoning": "Country count, period, multiplier, and places match source."
  },
  {
   "claim_id": "C244",
   "loglog_ids": [
    "9.28"
   ],
   "claim_text": "Stanford warns visibility-driven re-election tempts short-term populism.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "transparency can create perverse incentives for short-term populist policies when re-election depends on immediate visibility",
   "reasoning": "Source states the same causal warning."
  },
  {
   "claim_id": "C245",
   "loglog_ids": [
    "9.29"
   ],
   "claim_text": "Sweden-Democrats study plus Harvard misinformation panel on perceived transparency.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Swedish populist party exploits transparency norms ... false beliefs causally reduce perceived transparency regardless of actual transparency levels",
   "reasoning": "Both studies described match source."
  },
  {
   "claim_id": "C246",
   "loglog_ids": [
    "9.30"
   ],
   "claim_text": "Latent-transparency experiments plus OGP's 75-country commitment autopsy.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "identifies \"latent transparency\" concept ... failed commitments across 75 member countries",
   "reasoning": "Latent transparency concept and 75 countries match source."
  },
  {
   "claim_id": "C247",
   "loglog_ids": [
    "9.31"
   ],
   "claim_text": "Hong 2024 ties competition-data quality to capacity; Ruijer (2020) maps conformity-to-resistance.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Hong (2024) ... only when administrative capacity is also high ... Ruijer et al. (2020) ... ranging from conformity to active resistance",
   "reasoning": "Both authors, years, and findings match source."
  },
  {
   "claim_id": "C248",
   "loglog_ids": [
    "9.32"
   ],
   "claim_text": "Workaround-resistance study plus Nordics' 250+ year openness overview.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "resist open government data policy through workarounds ... traces 250+ years of FOI practice",
   "reasoning": "Workaround study and 250+ year span match source."
  },
  {
   "claim_id": "C249",
   "loglog_ids": [
    "9.33"
   ],
   "claim_text": "Nordicom compares five Nordic regimes with inconsistent openness patterns.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "comparing right-of-access rules across five Nordic countries; notes inconsistent patterns",
   "reasoning": "Five-country comparison and inconsistency match source."
  },
  {
   "claim_id": "C250",
   "loglog_ids": [
    "9.34"
   ],
   "claim_text": "Finland's 1999 law deems documents public unless specifically exempted.",
   "claim_type": "definition",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "transparency law (1999 amendment); establishes principle that all government documents are public unless specifically exempted",
   "reasoning": "Year, default-public rule, and exemption match source."
  }
 ],
 "metrics": {
  "total_claims": 250,
  "supported": 245,
  "partially_supported": 5,
  "unverifiable": 0,
  "contradicted": 0,
  "critical_errors": 0,
  "faithfulness_precision": 0.98
 },
 "fail_list": [
  "C032",
  "C068",
  "C135",
  "C143",
  "C170"
 ]
}
```

## Judge Cov (coverage), opencode-go/deepseek-v4.1-flash

```json
{
 "judge": "coverage",
 "judge_version": "1.0.0",
 "model": "opencode-go/deepseek-v4.1-flash (opencode) scripted pipeline 2026-09-15",
 "source_id": "02_case_for_transparent_government",
 "key_points": [
  {
   "point_id": "K01",
   "point_text": "Central thesis: every government decision should be fully documented and publicly available, not just the final policy but the whole chain (data used, considerations, who was involved, alternatives, arguments for and against, implementation, evaluation, course-correction, and when/how it will be reconsidered). This is framed as basic accountability, not radicalism; only its novelty makes it sound radical.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L002",
    "L007",
    "L008",
    "L009",
    "L010",
    "L011",
    "L012"
   ],
   "evidence_quote": "Every government decision should be fully documented and publicly available. ... Document data used, considerations made, and who was involved. ... Document alternatives considered, arguments for and against, implementation steps. ... Document evaluation, course-correction plans, and reconsideration terms. ... It sounds radical only because the opposite was normalized.",
   "reasoning": "L007 states the thesis and L008-L010 enumerate the full chain (data, who, alternatives, arguments, implementation, evaluation, reconsideration), matching the source. L011-L012 add the basic-accountability and radical-only-because-novel framing."
  },
  {
   "point_id": "K02",
   "point_text": "Citizen-as-CEO framing: in a democracy citizens are the principals/CEOs and public servants are agents/employees who spend the citizens' money; information flows upward and accountability exists because a reviewable trail exists, whereas the current government lets agents classify and refuse to explain.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L013",
    "L014",
    "L015",
    "L016"
   ],
   "evidence_quote": "In democracy citizens are principals; officials are their employee-agents. ... Every servant from licensing clerk to president works for you. ... A company letting managers classify emails would go bankrupt within a year.",
   "reasoning": "L013-L016 capture the principal/agent CEO framing, the servant range from clerk to president, and the classify-and-refuse analogy to the current government."
  },
  {
   "point_id": "K03",
   "point_text": "Availability versus consumption distinction: the citizen-CEO need not read every email or attend every meeting, but must be able to trace any decision that matters; mere availability changes behavior even without consumption.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L015",
    "L017",
    "L177",
    "L178"
   ],
   "evidence_quote": "CEOs need not read everything, but reviewability shapes behavior. ... Nuance: Availability matters, not consumption: trace decisions affecting your life. ... Latent availability deters misconduct even without consumption. ... CEOs need not read every email to benefit from access.",
   "reasoning": "L015 and L017 state the distinction directly; L177-L178 reinforce that latent availability deters misconduct without consumption, matching the source."
  },
  {
   "point_id": "K04",
   "point_text": "Scope clarification: transparency is about government decisions, processes, and officials flowing to citizens, NOT about citizens surveilling each other or exposing personal records (tax returns, medical records). Privacy-preserving approaches (aggregation, anonymization, differential privacy) make separating government decision data from citizen personal data technically straightforward.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L018",
    "L019",
    "L020",
    "L021",
    "L022",
    "L023"
   ],
   "evidence_quote": "Transparency flows from government to citizens, never the reverse. ... Not tax returns, medical records, or citizens surveilling each other. ... Publish $X/$Y/$Z/$W spending, not John Smith's $47,000 taxes. ... Aggregation, anonymization, and differential privacy make separation technically straightforward.",
   "reasoning": "L018-L020 state the direction and exclusions (tax returns, medical records, mutual surveillance). L023 names all three privacy-preserving techniques, so the quantifier and mechanism are intact."
  },
  {
   "point_id": "K05",
   "point_text": "Sweden 1766: the Freedom of the Press Act was the world's first freedom of information law, now part of the constitution; born from Hats vs Caps political conflict, driven by Anders Chydenius with an explicitly anti-corruption motive. Two hundred sixty years later the offentlighetsprincipen makes documents public by default and the country has not collapsed, with Nordic countries ranking among the least corrupt and most effective democracies.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L026",
    "L027",
    "L028",
    "L029",
    "L030",
    "L031"
   ],
   "evidence_quote": "Sweden's 260-year openness shows transparency endures without collapse. ... In 1766 Sweden passed the world's first freedom-of-information law. ... Chydenius drove Hats-versus-Caps explicitly anti-corruption law. ... Offentlighetsprincipen keeps documents public by default 260 years on. ... Nordics consistently rank among least corrupt, most effective democracies.",
   "reasoning": "All elements present: 1766, first FOI law, constitutional, Hats vs Caps, Chydenius, anti-corruption motive, offentlighetsprincipen by default, no collapse, Nordic rankings."
  },
  {
   "point_id": "K06",
   "point_text": "Seoul/South Korea 1999: the OPEN system tracks 70 corruption-prone municipal tasks (construction permits, environmental regulation, urban planning) and shows citizens who decided what, at which point, in real time; this visibility removed the leverage that enabled bribery, and research confirmed corruption decreases as e-participation increases.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L032",
    "L033",
    "L034",
    "L035",
    "L036",
    "L037"
   ],
   "evidence_quote": "Seoul's 1999 OPEN system made bribery-prone permitting visible. ... OPEN tracks 70 corruption-prone tasks, including construction, environmental, and urban planning permits, in real time. ... Visibility eliminated that bribery leverage entirely. ... Corruption decreases as e-participation increases.",
   "reasoning": "Year, task count, three task categories, real-time visibility, elimination of bribery leverage, and the e-participation research finding are all captured."
  },
  {
   "point_id": "K07",
   "point_text": "Estonia 2001: X-Road is a distributed data exchange layer connecting 929+ institutions, 1,887 information systems, and 3,000+ digital services, with every transaction timestamped and cryptographically signed and all access logged; Estonia ranks 2nd in the UN E-Government Development Index with no major breaches in over 20 years, proving the infrastructure is technically feasible and that the will, not the technology, is the bottleneck.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L038",
    "L039",
    "L040",
    "L041",
    "L042",
    "L043",
    "L044",
    "L045"
   ],
   "evidence_quote": "Estonia's 2001 X-Road proves transparency infrastructure scales. ... X-Road links 929+ institutions, 1,887 systems, 3,000+ services, timestamped, signed, logged. ... Estonia ranks 2nd on the UN E-Government Development Index. ... No major breaches in over 20 years ... The technology is feasible; the bottleneck is will.",
   "reasoning": "All numbers (929+, 1,887, 3,000+), the signing/timestamping/logging, 2nd rank, no-major-breaches, and the will-not-technology conclusion are present."
  },
  {
   "point_id": "K08",
   "point_text": "Brazil 2004: the Transparency Portal publishes all federal spending (contracts, transfers, salaries, travel, credit card transactions) with 20+ million accesses per year; the Transparency Card sends real-time notifications about political spending (430,000+ active cards, 20+ million notifications), and journalists using the Access to Information Law uncovered 60GB of hidden pension payment data going back 27 years.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L046",
    "L047",
    "L048",
    "L049",
    "L050"
   ],
   "evidence_quote": "Brazil's 2004 Transparency Portal follows all federal money. ... It publishes contracts, transfers, salaries, travel, and credit-card transactions. ... over 20 million accesses per year. ... Transparency Card sent 20+ million notifications via 430,000+ active cards. ... Journalists uncovered 60GB of hidden pension payments spanning 27 years.",
   "reasoning": "Year, five published categories, 20+ million accesses, Transparency Card with 430,000+ cards and 20+ million notifications, and the 60GB/27-year pension find are all present."
  },
  {
   "point_id": "K09",
   "point_text": "New Zealand 2019: the government proactively publishes all Cabinet papers and minutes online within 30 business days of decisions, even though cabinet deliberations are typically the most protected category of government information; government has not ground to a halt and citizens can now see why decisions were made.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L052",
    "L053",
    "L054",
    "L055"
   ],
   "evidence_quote": "New Zealand publishes cabinet papers by default since 2019. ... All papers and minutes appear online within 30 business days. ... Cabinet deliberations are typically the world's most protected government information. ... Government has not halted ... citizens see why.",
   "reasoning": "Year, 30-business-day window, most-protected-category framing, and the not-halted/see-why outcome all match."
  },
  {
   "point_id": "K10",
   "point_text": "Recurring pattern: secret government programs are later revealed to be illegal or built on lies, and internal oversight failed because it operated inside the same secrecy bubble. Examples: Pentagon Papers 1971 (Vietnam unwinnable while publicly claiming progress), COINTELPRO exposed 1971 (illegal surveillance of civil rights leaders), Snowden 2013 (NSA bulk metadata collection, PRISM, surveilling foreign leaders). In each case the government predicted catastrophe and the programs proved illegal, unconstitutional, or deceptive.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L060",
    "L061",
    "L062",
    "L063",
    "L064",
    "L065",
    "L070",
    "L071"
   ],
   "evidence_quote": "Secret programs recur as illegal; secret oversight reliably fails to catch them. ... 1971 Pentagon Papers showed government knew Vietnam was unwinnable while publicly claiming progress. ... Media, Pennsylvania break-in exposed COINTELPRO's illegal surveillance ... In 2013 Snowden revealed bulk metadata collection ... PRISM, and leader surveillance. ... FISA courts, committees, and inspectors general failed inside the secrecy structure.",
   "reasoning": "The pattern, all three examples with years and content, the failed cataclysm predictions, and the oversight-inside-secrecy explanation (L070-L071) are all captured."
  },
  {
   "point_id": "K11",
   "point_text": "Snowden aftermath: in September 2020 the US Ninth Circuit ruled the NSA bulk phone record collection illegal and possibly unconstitutional, failing FISA's relevance requirement; Geoffrey R. Stone found no evidence it stopped terror attacks, and the NSA abandoned the program in 2018. The USA FREEDOM Act (2015) was the first legislation in over 30 years to rein in NSA spying, ending bulk metadata collection; tech transparency reporting, default HTTPS, and accelerated EU GDPR followed. Whether disclosure caused operational harm remains genuinely uncertain, but the legality and oversight failures are not.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L066",
    "L067",
    "L068",
    "L069",
    "L072",
    "L073",
    "L074",
    "L075",
    "L076",
    "L077"
   ],
   "evidence_quote": "In September 2020 the Ninth Circuit ruled bulk collection illegal, possibly unconstitutional. ... The court required FISA relevance to a particular authorized investigation. ... Stone found no evidence bulk collection stopped any terror attacks. ... The NSA abandoned the program in 2018 ... The 2015 USA FREEDOM Act first reined in NSA spying in over 30 years. ... HTTPS became default ... GDPR was accelerated ... Operational harm is genuinely uncertain; illegality is not.",
   "reasoning": "All specifics present: Sept 2020 Ninth Circuit, possibly unconstitutional, FISA relevance, Stone, 2018 abandonment, 2015 Act/first-in-30-years, transparency reporting, HTTPS, GDPR, and the harm-uncertain/illegality-certain caveat."
  },
  {
   "point_id": "K12",
   "point_text": "Privacy and harassment objections: privacy fears (e.g., 66% concerned about government data collection; 86% opposed to online public records) are about citizen data held by government, not about government decisions being visible, so they rest on a direction confusion; likewise threats to officials are real (Brennan Center 2024 survey of 735 officials: 38% threatened, 34% know someone who resigned, up from 22% in 2023), so decisions should be public while officials' personal information is protected. Much current harassment stems from lack of transparency about processes.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L082",
    "L083",
    "L084",
    "L126",
    "L127",
    "L128",
    "L133",
    "L135",
    "L136"
   ],
   "evidence_quote": "2019 Pew: 66% fear collection ... A 2000 ABC poll: 86% said agencies should not publish such records online. ... Polls fear citizen data held by government, not visible government decisions. ... Brennan surveyed 735 local election officials ... 38% threatened ... 34% know someone who resigned, up from 22% in 2023. ... Publish who decided what and why; protect addresses, families, schedules. ... Current harassment feeds on opacity-bred fraud conspiracies.",
   "reasoning": "All numbers and caveats present: 66%, 86%, direction-confusion rebuttal, Brennan 735/38%/34% up from 22%, protect personal info while publishing decisions, and harassment-fed-by-opacity."
  },
  {
   "point_id": "K13",
   "point_text": "Secrecy-based objections and answers: the gridlock argument confuses speed with documentation (transparency documents decisions at the current speed, as NZ shows, and opacity makes decisions unaccountable rather than better); diplomacy (JCPOA secret Oman backchannel, Camp David, Cold War) and markets (Fed FOMC minutes delayed three weeks, transcripts five years; TTIP harmed by too much secrecy) justify only temporary operational secrecy with time-delayed release (e.g., 30-90 days), never permanent secrecy about what was decided and why; national security is overused to hide embarrassment, illegality, incompetence, and corruption, and the burden of proof should be reversed so officials must justify secrecy.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L092",
    "L094",
    "L095",
    "L096",
    "L100",
    "L101",
    "L105",
    "L106",
    "L147",
    "L148",
    "L149",
    "L150",
    "L184",
    "L185",
    "L186"
   ],
   "evidence_quote": "This confuses decision speed with decision documentation. ... New Zealand's 30-day cabinet papers halted nothing ... Opacity makes decisions unaccountable random walks, not better ones. ... JCPOA began in 2012 via Sullivan's secret Oman backchannel. ... Camp David 1978 and Cold War backchannels ... Temporary secrecy during talks is acceptable; permanent secrecy is not. ... Release full documentation 30-90 days after conclusion ... The Fed releases minutes in three weeks, transcripts in five years. ... TTIP failed amid backlash ... Flip the burden: transparent by default, secrecy needs proof. ... The label hides embarrassment, illegality, incompetence, and corruption. ... Officials under scrutiny set secrecy criteria: a conflict of interest.",
   "reasoning": "Every element is present: speed/documentation confusion, NZ example, unaccountability of opacity, JCPOA Oman, Camp David, Cold War, Fed 3-week/5-year timing, TTIP, 30-90 day delayed release, national-security overuse/label, and reversing the burden of proof."
  },
  {
   "point_id": "K14",
   "point_text": "Empirical misuse concerns acknowledged but rebutted: Harden and Kirkland found open legislative meetings bring more lobbying, more lobbyist donations, and no improved policy-opinion correlation, and 2024 Irish experiment found lobbying transparency does not raise trust; populism research (Kyle and Gultchin, 43 countries 1990-2018) finds populists 4x more likely to damage democracy and countries falling ~5 places on the Corruption Perceptions Index; misinformation research finds false beliefs reduce perceived transparency. The answer is not less transparency but building citizen capacity (watchdogs, investigative journalism, civic tech, professional monitoring) and better transparency, since populists reduce rather than increase transparency, opacity enables false beliefs, and selective exploitation works only because not everything is visible.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L111",
    "L113",
    "L114",
    "L116",
    "L117",
    "L119",
    "L153",
    "L154",
    "L155",
    "L161",
    "L162",
    "L168",
    "L173",
    "L174"
   ],
   "evidence_quote": "Harden and Kirkland studied all 50 legislatures over multiple decades. ... More lobbyists register and donate, yet policy-opinion correlation stays same open or closed. ... Ireland 2024: 569 participants; lobbying transparency did not raise trust. ... Build citizen capacity: auditors, watchdogs, journalism, civic tech. ... Kyle-Gultchin studied 43 democracies, 1990-2018 ... Populists are 4x likelier to damage institutions ... Countries fall 5 places on corruption perceptions ... Causality is backwards: populists damage democracy by reducing transparency. ... Cherry-picking works only while the full record stays hidden. ... Harvard 2023 ... COVID-19 false beliefs lower perceived transparency. ... False beliefs drive perceived opacity, not the reverse. ... Opacity enables false beliefs.",
   "reasoning": "All empirical results and numbers present: Harden/Kirkland lobbying and donation finding with no correlation improvement, Irish 2024 experiment, Kyle-Gultchin 43 countries/1990-2018/4x/5 places, misinformation false-beliefs finding, and the citizen-capacity plus causal-reversal rebuttals."
  },
  {
   "point_id": "K15",
   "point_text": "Resistance and the closing vision: 'those in power will never allow this' is a description of the political challenge, not a principled objection (Iceland's 2008 crowdsourced constitution was blocked by parliament despite referendum approval; OGP commitments fail on funding, coordination, and political transitions), and the CEO framing reframes it as a governance design problem of who works for whom. Transparency is not a value to be balanced but the measuring stick; speed and accountability are byproducts, and open source shows complex collaborative work can be done in public, with the case for transparency stronger because citizens cannot fork their country.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L191",
    "L193",
    "L194",
    "L195",
    "L196",
    "L197",
    "L202",
    "L203",
    "L204",
    "L205",
    "L206",
    "L209",
    "L210",
    "L211",
    "L212",
    "L213"
   ],
   "evidence_quote": "That describes the political challenge, not a principled objection. ... two-thirds referendum approval. ... Parliament refused to ratify the draft. ... OGP: 75 countries, 4,500+ commitments since 2011; one-third delayed for funding. ... Ask who works for whom ... This is a governance-design problem, not permission-seeking. ... Transparency is the measuring stick, not one value among many. ... Speed and accountability are byproducts ... Linux ... Disagreeing users can fork the project. ... Government is involuntary: you cannot fork your country.",
   "reasoning": "All elements present: description-not-objection reframe, Iceland 2008 blocked constitution, OGP funding/coordination/transition failures, who-works-for-whom governance-design framing, transparency-as-measuring-stick, speed/accountability as byproducts, open-source example, and cannot-fork-your-country."
  }
 ],
 "metrics": {
  "total_points": 15,
  "must_have_total": 15,
  "must_have_present": 15,
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
 "source_id": "02_case_for_transparent_government",
 "labels": [
  {
   "claim_id": "C001",
   "loglog_ids": [
    "0"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Section 0 summary states thesis; first occurrence, body still adds detail."
  },
  {
   "claim_id": "C002",
   "loglog_ids": [
    "1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Manager analogy introduces the governing case, new here."
  },
  {
   "claim_id": "C003",
   "loglog_ids": [
    "1.1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Concrete example instance, not stated earlier."
  },
  {
   "claim_id": "C004",
   "loglog_ids": [
    "1.2"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Owner-response detail extends the analogy."
  },
  {
   "claim_id": "C005",
   "loglog_ids": [
    "1.3"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Government excuse list new and enumerates objections."
  },
  {
   "claim_id": "C006",
   "loglog_ids": [
    "2"
   ],
   "label": "Duplicate",
   "canonical_id": "C001",
   "reasoning": "Section 2 heading restates summary mandate; adds only publicly available."
  },
  {
   "claim_id": "C007",
   "loglog_ids": [
    "2.1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Specific documentation fields, new information."
  },
  {
   "claim_id": "C008",
   "loglog_ids": [
    "2.2"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Additional documentation fields, new."
  },
  {
   "claim_id": "C009",
   "loglog_ids": [
    "2.3"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Evaluation and course-correction fields, new."
  },
  {
   "claim_id": "C010",
   "loglog_ids": [
    "2.4"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Corporate comparability claim, supports mandate."
  },
  {
   "claim_id": "C011",
   "loglog_ids": [
    "2.5"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Normalization explanation, new framing."
  },
  {
   "claim_id": "C012",
   "loglog_ids": [
    "3"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Principal-agent definition, distinct from summary."
  },
  {
   "claim_id": "C013",
   "loglog_ids": [
    "3.1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Scope enumeration from clerk to president, new."
  },
  {
   "claim_id": "C014",
   "loglog_ids": [
    "3.2"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Reviewability-behavior link, first occurrence."
  },
  {
   "claim_id": "C015",
   "loglog_ids": [
    "3.3"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Bankruptcy reductio, new argument."
  },
  {
   "claim_id": "C016",
   "loglog_ids": [
    "3.4"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Availability-versus-consumption nuance, first occurrence."
  },
  {
   "claim_id": "C017",
   "loglog_ids": [
    "4"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Direction definition, new scope claim."
  },
  {
   "claim_id": "C018",
   "loglog_ids": [
    "4.1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Positive definition components, new."
  },
  {
   "claim_id": "C019",
   "loglog_ids": [
    "4.2"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Negative exclusions, new and load-bearing."
  },
  {
   "claim_id": "C020",
   "loglog_ids": [
    "4.3"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "CEO work-product analogy, first occurrence."
  },
  {
   "claim_id": "C021",
   "loglog_ids": [
    "4.4"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Fiscal example with figures, new."
  },
  {
   "claim_id": "C022",
   "loglog_ids": [
    "4.5"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Privacy-technique feasibility claim, new."
  },
  {
   "claim_id": "C023",
   "loglog_ids": [
    "5"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Feasibility thesis, new section claim."
  },
  {
   "claim_id": "C024",
   "loglog_ids": [
    "5.1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Existence nuance, new."
  },
  {
   "claim_id": "C025",
   "loglog_ids": [
    "5.2"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Sweden example headline, new."
  },
  {
   "claim_id": "C026",
   "loglog_ids": [
    "5.2.1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "1766 law date, canonical body occurrence."
  },
  {
   "claim_id": "C027",
   "loglog_ids": [
    "5.2.2"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Censorship abolition detail, new."
  },
  {
   "claim_id": "C028",
   "loglog_ids": [
    "5.2.3"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Chydenius origin detail, canonical body occurrence."
  },
  {
   "claim_id": "C029",
   "loglog_ids": [
    "5.2.4"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Offentlighetsprincipen term, new."
  },
  {
   "claim_id": "C030",
   "loglog_ids": [
    "5.2.5"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Nordic ranking fact, new."
  },
  {
   "claim_id": "C031",
   "loglog_ids": [
    "5.3"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Seoul OPEN case headline, new."
  },
  {
   "claim_id": "C032",
   "loglog_ids": [
    "5.3.1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "70-task scope, canonical body occurrence."
  },
  {
   "claim_id": "C033",
   "loglog_ids": [
    "5.3.2"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Process-point attribution, new."
  },
  {
   "claim_id": "C034",
   "loglog_ids": [
    "5.3.3"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Bribe mechanism, new causal detail."
  },
  {
   "claim_id": "C035",
   "loglog_ids": [
    "5.3.4"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Elimination outcome, new."
  },
  {
   "claim_id": "C036",
   "loglog_ids": [
    "5.3.5"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Corruption-participation link, canonical occurrence."
  },
  {
   "claim_id": "C037",
   "loglog_ids": [
    "5.4"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Estonia X-Road headline, new."
  },
  {
   "claim_id": "C038",
   "loglog_ids": [
    "5.4.1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "System statistics, canonical body occurrence."
  },
  {
   "claim_id": "C039",
   "loglog_ids": [
    "5.4.2"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Data-access visibility fact, new."
  },
  {
   "claim_id": "C040",
   "loglog_ids": [
    "5.4.3"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Estonia index rank, canonical occurrence."
  },
  {
   "claim_id": "C041",
   "loglog_ids": [
    "5.4.4"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Breach record, new evidence."
  },
  {
   "claim_id": "C042",
   "loglog_ids": [
    "5.4.5"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "License and deployment fact, new."
  },
  {
   "claim_id": "C043",
   "loglog_ids": [
    "5.4.6"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Feasibility interpretation, new."
  },
  {
   "claim_id": "C044",
   "loglog_ids": [
    "5.4.7"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Will-versus-technology conclusion, new."
  },
  {
   "claim_id": "C045",
   "loglog_ids": [
    "5.5"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Brazil portal headline, new."
  },
  {
   "claim_id": "C046",
   "loglog_ids": [
    "5.5.1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Publication categories, new."
  },
  {
   "claim_id": "C047",
   "loglog_ids": [
    "5.5.2"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Access-count figure, canonical occurrence."
  },
  {
   "claim_id": "C048",
   "loglog_ids": [
    "5.5.3"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Transparency Card figures, new."
  },
  {
   "claim_id": "C049",
   "loglog_ids": [
    "5.5.4"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "60GB pension find, canonical occurrence."
  },
  {
   "claim_id": "C050",
   "loglog_ids": [
    "5.5.5"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Fraud-finding interpretation, new."
  },
  {
   "claim_id": "C051",
   "loglog_ids": [
    "5.6"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "New Zealand case headline, new."
  },
  {
   "claim_id": "C052",
   "loglog_ids": [
    "5.6.1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "30-day window, canonical occurrence."
  },
  {
   "claim_id": "C053",
   "loglog_ids": [
    "5.6.2"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Cabinet-protection baseline, new."
  },
  {
   "claim_id": "C054",
   "loglog_ids": [
    "5.6.3"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Government-continued fact, new."
  },
  {
   "claim_id": "C055",
   "loglog_ids": [
    "5.7"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Taiwan vTaiwan headline, new."
  },
  {
   "claim_id": "C056",
   "loglog_ids": [
    "5.7.1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Pol.is mechanism, canonical occurrence."
  },
  {
   "claim_id": "C057",
   "loglog_ids": [
    "5.7.2"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "2018 throughput figures, new."
  },
  {
   "claim_id": "C058",
   "loglog_ids": [
    "5.7.3"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Participation-versus-transparency scope, new."
  },
  {
   "claim_id": "C059",
   "loglog_ids": [
    "6"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Secret-program failure thesis, new."
  },
  {
   "claim_id": "C060",
   "loglog_ids": [
    "6.1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Pentagon Papers evidence, new."
  },
  {
   "claim_id": "C061",
   "loglog_ids": [
    "6.2"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "COINTELPRO exposure, new."
  },
  {
   "claim_id": "C062",
   "loglog_ids": [
    "6.3"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "COINTELPRO targets, new."
  },
  {
   "claim_id": "C063",
   "loglog_ids": [
    "6.4"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Snowden revelations detail, new."
  },
  {
   "claim_id": "C064",
   "loglog_ids": [
    "6.5"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Predicted-catastrophe pattern, canonical occurrence."
  },
  {
   "claim_id": "C065",
   "loglog_ids": [
    "6.6"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Ninth Circuit ruling, canonical occurrence."
  },
  {
   "claim_id": "C066",
   "loglog_ids": [
    "6.7"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "FISA-relevance requirement, new."
  },
  {
   "claim_id": "C067",
   "loglog_ids": [
    "6.8"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Stone finding, new evidence."
  },
  {
   "claim_id": "C068",
   "loglog_ids": [
    "6.9"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "2018 abandonment date, new; partially supported but scored."
  },
  {
   "claim_id": "C069",
   "loglog_ids": [
    "6.10"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Oversight-failure claim, new."
  },
  {
   "claim_id": "C070",
   "loglog_ids": [
    "6.11"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Capture interpretation, new."
  },
  {
   "claim_id": "C071",
   "loglog_ids": [
    "6.12"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "USA FREEDOM Act, new."
  },
  {
   "claim_id": "C072",
   "loglog_ids": [
    "6.13"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Act contents, canonical occurrence."
  },
  {
   "claim_id": "C073",
   "loglog_ids": [
    "6.14"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Tech transparency reporting, new."
  },
  {
   "claim_id": "C074",
   "loglog_ids": [
    "6.15"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "HTTPS default, new."
  },
  {
   "claim_id": "C075",
   "loglog_ids": [
    "6.16"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "GDPR acceleration, canonical occurrence."
  },
  {
   "claim_id": "C076",
   "loglog_ids": [
    "6.17"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Harm-versus-illegality nuance, new."
  },
  {
   "claim_id": "C077",
   "loglog_ids": [
    "6.18"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Snowden-symptom framing, new."
  },
  {
   "claim_id": "C078",
   "loglog_ids": [
    "6.19"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Designed-in traceability proposal, new."
  },
  {
   "claim_id": "C079",
   "loglog_ids": [
    "7"
   ],
   "label": "Trivia",
   "canonical_id": null,
   "reasoning": "Roadmap transition announcing ten objections; filler with no substantive content."
  },
  {
   "claim_id": "C080",
   "loglog_ids": [
    "7.1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Privacy objection, new."
  },
  {
   "claim_id": "C081",
   "loglog_ids": [
    "7.1.1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Pew figures, canonical occurrence."
  },
  {
   "claim_id": "C082",
   "loglog_ids": [
    "7.1.2"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "ABC poll, canonical occurrence."
  },
  {
   "claim_id": "C083",
   "loglog_ids": [
    "7.1.3"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Poll reinterpretation, new."
  },
  {
   "claim_id": "C084",
   "loglog_ids": [
    "7.1.4"
   ],
   "label": "Duplicate",
   "canonical_id": "C020",
   "reasoning": "Repeats work-product-versus-health-records distinction from 4.3."
  },
  {
   "claim_id": "C085",
   "loglog_ids": [
    "7.1.5"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Specific rebuttal figure, distinct from 4.4."
  },
  {
   "claim_id": "C086",
   "loglog_ids": [
    "7.1.6"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Bundled-systems split recommendation, new."
  },
  {
   "claim_id": "C087",
   "loglog_ids": [
    "7.2"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Deliberation-paralysis objection, new."
  },
  {
   "claim_id": "C088",
   "loglog_ids": [
    "7.2.1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Cambridge and IMF evidence, canonical occurrence."
  },
  {
   "claim_id": "C089",
   "loglog_ids": [
    "7.2.2"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "IMF friction defense, new."
  },
  {
   "claim_id": "C090",
   "loglog_ids": [
    "7.2.3"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Robodebt figures, canonical occurrence."
  },
  {
   "claim_id": "C091",
   "loglog_ids": [
    "7.2.4"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Speed-versus-documentation confusion, new."
  },
  {
   "claim_id": "C092",
   "loglog_ids": [
    "7.2.5"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Document-at-speed recommendation, new."
  },
  {
   "claim_id": "C093",
   "loglog_ids": [
    "7.2.6"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "CEO documentation analogy, new here."
  },
  {
   "claim_id": "C094",
   "loglog_ids": [
    "7.2.7"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "New Zealand restated as rebuttal, new context."
  },
  {
   "claim_id": "C095",
   "loglog_ids": [
    "7.2.8"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Opacity-as-random-walk claim, new."
  },
  {
   "claim_id": "C096",
   "loglog_ids": [
    "7.2.9"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Consistency-speed causal claim, new."
  },
  {
   "claim_id": "C097",
   "loglog_ids": [
    "7.3"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Diplomacy-secrecy objection, new."
  },
  {
   "claim_id": "C098",
   "loglog_ids": [
    "7.3.1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Concession stance, new."
  },
  {
   "claim_id": "C099",
   "loglog_ids": [
    "7.3.2"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "JCPOA backchannel, canonical occurrence."
  },
  {
   "claim_id": "C100",
   "loglog_ids": [
    "7.3.3"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Camp David and Cold War examples, new."
  },
  {
   "claim_id": "C101",
   "loglog_ids": [
    "7.3.4"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Democratic dilemma definition, new."
  },
  {
   "claim_id": "C102",
   "loglog_ids": [
    "7.3.5"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "CEO negotiation analogy, new."
  },
  {
   "claim_id": "C103",
   "loglog_ids": [
    "7.3.6"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Post-hoc disclosure recommendation, new."
  },
  {
   "claim_id": "C104",
   "loglog_ids": [
    "7.3.7"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Temporary-versus-permanent secrecy line, new."
  },
  {
   "claim_id": "C105",
   "loglog_ids": [
    "7.3.8"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "30-90 day release window, new."
  },
  {
   "claim_id": "C106",
   "loglog_ids": [
    "7.3.9"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Non-principal veto claim, new."
  },
  {
   "claim_id": "C107",
   "loglog_ids": [
    "7.3.10"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Principals restatement in foreign context, new angle."
  },
  {
   "claim_id": "C108",
   "loglog_ids": [
    "7.4"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Special-interest objection, new."
  },
  {
   "claim_id": "C109",
   "loglog_ids": [
    "7.4.1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Concession stance, new."
  },
  {
   "claim_id": "C110",
   "loglog_ids": [
    "7.4.2"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Harden-Kirkland study, canonical occurrence."
  },
  {
   "claim_id": "C111",
   "loglog_ids": [
    "7.4.3"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Illusion of Accountability study, new."
  },
  {
   "claim_id": "C112",
   "loglog_ids": [
    "7.4.4"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Lobbyist-versus-correlation finding, new."
  },
  {
   "claim_id": "C113",
   "loglog_ids": [
    "7.4.5"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Harden representation finding, new."
  },
  {
   "claim_id": "C114",
   "loglog_ids": [
    "7.4.6"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Arnold 1990 finding, new."
  },
  {
   "claim_id": "C115",
   "loglog_ids": [
    "7.4.7"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Ireland 2024 trial, new."
  },
  {
   "claim_id": "C116",
   "loglog_ids": [
    "7.4.8"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Asymmetry framing, new."
  },
  {
   "claim_id": "C117",
   "loglog_ids": [
    "7.4.9"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Resource imbalance detail, new."
  },
  {
   "claim_id": "C118",
   "loglog_ids": [
    "7.4.10"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Build-capacity recommendation, canonical occurrence."
  },
  {
   "claim_id": "C119",
   "loglog_ids": [
    "7.4.11"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Fiquem Sabendo evidence, new."
  },
  {
   "claim_id": "C120",
   "loglog_ids": [
    "7.4.12"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Electoral-competition key claim, new."
  },
  {
   "claim_id": "C121",
   "loglog_ids": [
    "7.4.13"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Opacity-transparency contrast, new."
  },
  {
   "claim_id": "C122",
   "loglog_ids": [
    "7.4.14"
   ],
   "label": "Duplicate",
   "canonical_id": "C118",
   "reasoning": "Restates build-capacity-not-reduce-information recommendation from 7.4.10."
  },
  {
   "claim_id": "C123",
   "loglog_ids": [
    "7.5"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Harassment objection, new."
  },
  {
   "claim_id": "C124",
   "loglog_ids": [
    "7.5.1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Concession stance, new."
  },
  {
   "claim_id": "C125",
   "loglog_ids": [
    "7.5.2"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Brennan survey method, canonical occurrence."
  },
  {
   "claim_id": "C126",
   "loglog_ids": [
    "7.5.3"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Threat percentages, new."
  },
  {
   "claim_id": "C127",
   "loglog_ids": [
    "7.5.4"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Resignation-awareness figures, new."
  },
  {
   "claim_id": "C128",
   "loglog_ids": [
    "7.5.5"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "In-person threat figure, new."
  },
  {
   "claim_id": "C129",
   "loglog_ids": [
    "7.5.6"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Doxxing-swatting evolution, canonical occurrence."
  },
  {
   "claim_id": "C130",
   "loglog_ids": [
    "7.5.7"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "AI intensification claim, new."
  },
  {
   "claim_id": "C131",
   "loglog_ids": [
    "7.5.8"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "22-state protection count, new."
  },
  {
   "claim_id": "C132",
   "loglog_ids": [
    "7.5.9"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Publish-why-protect-personal recommendation, new."
  },
  {
   "claim_id": "C133",
   "loglog_ids": [
    "7.5.10"
   ],
   "label": "Duplicate",
   "canonical_id": "C020",
   "reasoning": "Work-product-versus-personal-records analogy repeats 4.3."
  },
  {
   "claim_id": "C134",
   "loglog_ids": [
    "7.5.11"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Opacity-conspiracy causal claim, canonical occurrence."
  },
  {
   "claim_id": "C135",
   "loglog_ids": [
    "7.5.12"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Audit-transparency antidote, new; partially supported but scored."
  },
  {
   "claim_id": "C136",
   "loglog_ids": [
    "7.5.13"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Protect-more-while-transparent recommendation, new."
  },
  {
   "claim_id": "C137",
   "loglog_ids": [
    "7.6"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "National-security objection, new."
  },
  {
   "claim_id": "C138",
   "loglog_ids": [
    "7.6.1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Use-versus-scrutiny observation, new."
  },
  {
   "claim_id": "C139",
   "loglog_ids": [
    "7.6.2"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Chicago poll figure, canonical occurrence."
  },
  {
   "claim_id": "C140",
   "loglog_ids": [
    "7.6.3"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Share-more majority, canonical occurrence."
  },
  {
   "claim_id": "C141",
   "loglog_ids": [
    "7.6.4"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Wariness trend figures, new."
  },
  {
   "claim_id": "C142",
   "loglog_ids": [
    "7.6.5"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Brennan overclassification claim, new."
  },
  {
   "claim_id": "C143",
   "loglog_ids": [
    "7.6.6"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "SIPRI trust claim, canonical occurrence; partially supported but scored."
  },
  {
   "claim_id": "C144",
   "loglog_ids": [
    "7.6.7"
   ],
   "label": "Duplicate",
   "canonical_id": "C064",
   "reasoning": "Snowden catastrophe-prediction failure restates 6.5 pattern."
  },
  {
   "claim_id": "C145",
   "loglog_ids": [
    "7.6.8"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Independent-research minimal impact, new."
  },
  {
   "claim_id": "C146",
   "loglog_ids": [
    "7.6.9"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Flip-the-burden recommendation, new."
  },
  {
   "claim_id": "C147",
   "loglog_ids": [
    "7.6.10"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Temporary classification scope, new."
  },
  {
   "claim_id": "C148",
   "loglog_ids": [
    "7.6.11"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Label-hides-misconduct claim, new."
  },
  {
   "claim_id": "C149",
   "loglog_ids": [
    "7.6.12"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Conflict-of-interest claim, new."
  },
  {
   "claim_id": "C150",
   "loglog_ids": [
    "7.7"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Populist-weaponization objection, new."
  },
  {
   "claim_id": "C151",
   "loglog_ids": [
    "7.7.1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Concession stance, new."
  },
  {
   "claim_id": "C152",
   "loglog_ids": [
    "7.7.2"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Kyle-Gultchin dataset, canonical occurrence."
  },
  {
   "claim_id": "C153",
   "loglog_ids": [
    "7.7.3"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "4x institution-damage figure, new."
  },
  {
   "claim_id": "C154",
   "loglog_ids": [
    "7.7.4"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Corruption-rank slides, new."
  },
  {
   "claim_id": "C155",
   "loglog_ids": [
    "7.7.5"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Venezuela example, new."
  },
  {
   "claim_id": "C156",
   "loglog_ids": [
    "7.7.6"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Constitution-rewrite and tenure figures, new."
  },
  {
   "claim_id": "C157",
   "loglog_ids": [
    "7.7.7"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Stanford short-termism claim, canonical occurrence."
  },
  {
   "claim_id": "C158",
   "loglog_ids": [
    "7.7.8"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Sweden Democrats case, new."
  },
  {
   "claim_id": "C159",
   "loglog_ids": [
    "7.7.9"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Scandal-erosion mechanism, new."
  },
  {
   "claim_id": "C160",
   "loglog_ids": [
    "7.7.10"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Reversed-causality claim, new."
  },
  {
   "claim_id": "C161",
   "loglog_ids": [
    "7.7.11"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Cherry-picking-hidden-record claim, new."
  },
  {
   "claim_id": "C162",
   "loglog_ids": [
    "7.7.12"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Electoral-cycle short-termism, new."
  },
  {
   "claim_id": "C163",
   "loglog_ids": [
    "7.7.13"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Documented-rationale defensibility, new."
  },
  {
   "claim_id": "C164",
   "loglog_ids": [
    "7.7.14"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Reasoning-evaluation antidote, new."
  },
  {
   "claim_id": "C165",
   "loglog_ids": [
    "7.7.15"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "CEO documented-reasoning analogy, distinct from 7.2.6."
  },
  {
   "claim_id": "C166",
   "loglog_ids": [
    "7.8"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Misinformation objection, new."
  },
  {
   "claim_id": "C167",
   "loglog_ids": [
    "7.8.1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Harvard panel finding, canonical occurrence."
  },
  {
   "claim_id": "C168",
   "loglog_ids": [
    "7.8.2"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Control variable detail, new."
  },
  {
   "claim_id": "C169",
   "loglog_ids": [
    "7.8.3"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Perception-effects causal claim, new."
  },
  {
   "claim_id": "C170",
   "loglog_ids": [
    "7.8.4"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Prize-idea-dislike-content finding, new; partially supported but scored."
  },
  {
   "claim_id": "C171",
   "loglog_ids": [
    "7.8.5"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Non-sequitur rebuttal, new."
  },
  {
   "claim_id": "C172",
   "loglog_ids": [
    "7.8.6"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Direction-of-causality claim, new."
  },
  {
   "claim_id": "C173",
   "loglog_ids": [
    "7.8.7"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Secrecy-vacuum speculation claim, new."
  },
  {
   "claim_id": "C174",
   "loglog_ids": [
    "7.8.8"
   ],
   "label": "Duplicate",
   "canonical_id": "C134",
   "reasoning": "Election-conspiracy-from-opacity restates opacity-conspiracy link in 7.5.11."
  },
  {
   "claim_id": "C175",
   "loglog_ids": [
    "7.8.9"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Checkable-ground-truth claim, new."
  },
  {
   "claim_id": "C176",
   "loglog_ids": [
    "7.8.10"
   ],
   "label": "Duplicate",
   "canonical_id": "C016",
   "reasoning": "Latent-availability-deters-misconduct restates availability-over-consumption in 3.4."
  },
  {
   "claim_id": "C177",
   "loglog_ids": [
    "7.8.11"
   ],
   "label": "Duplicate",
   "canonical_id": "C014",
   "reasoning": "CEOs-need-not-read-every-email restates reviewability claim in 3.2."
  },
  {
   "claim_id": "C178",
   "loglog_ids": [
    "7.8.12"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Persistent-transparency trust claim, new."
  },
  {
   "claim_id": "C179",
   "loglog_ids": [
    "7.8.13"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Accessibility-intermediary recommendation, new."
  },
  {
   "claim_id": "C180",
   "loglog_ids": [
    "7.9"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Market-manipulation objection, new."
  },
  {
   "claim_id": "C181",
   "loglog_ids": [
    "7.9.1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Trader-exploitation detail, new."
  },
  {
   "claim_id": "C182",
   "loglog_ids": [
    "7.9.2"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Delayed-secrecy concession, new."
  },
  {
   "claim_id": "C183",
   "loglog_ids": [
    "7.9.3"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Fed release windows, new."
  },
  {
   "claim_id": "C184",
   "loglog_ids": [
    "7.9.4"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "TTIP failure evidence, new."
  },
  {
   "claim_id": "C185",
   "loglog_ids": [
    "7.9.5"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Eventual-publication framing, new."
  },
  {
   "claim_id": "C186",
   "loglog_ids": [
    "7.9.6"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Domain-specific timing recommendation, new."
  },
  {
   "claim_id": "C187",
   "loglog_ids": [
    "7.9.7"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Procurement-favoritism claim, new."
  },
  {
   "claim_id": "C188",
   "loglog_ids": [
    "7.9.8"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Brazil contract-sunlight claim, new."
  },
  {
   "claim_id": "C189",
   "loglog_ids": [
    "7.10"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Power-will-refuse objection, new."
  },
  {
   "claim_id": "C190",
   "loglog_ids": [
    "7.10.1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Political-challenge rebuttal, new."
  },
  {
   "claim_id": "C191",
   "loglog_ids": [
    "7.10.2"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Iceland 2008 process, new."
  },
  {
   "claim_id": "C192",
   "loglog_ids": [
    "7.10.3"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Comment and approval figures, new."
  },
  {
   "claim_id": "C193",
   "loglog_ids": [
    "7.10.4"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Parliament refusal, canonical occurrence."
  },
  {
   "claim_id": "C194",
   "loglog_ids": [
    "7.10.5"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "OGP commitment figures, canonical occurrence."
  },
  {
   "claim_id": "C195",
   "loglog_ids": [
    "7.10.6"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Failure causes, new."
  },
  {
   "claim_id": "C196",
   "loglog_ids": [
    "7.10.7"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Successor-abandonment claim, new."
  },
  {
   "claim_id": "C197",
   "loglog_ids": [
    "7.10.8"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Beneficiary-resistance concession, new."
  },
  {
   "claim_id": "C198",
   "loglog_ids": [
    "7.10.9"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Threatening-power-is-point claim, new."
  },
  {
   "claim_id": "C199",
   "loglog_ids": [
    "7.10.10"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Reform-window examples, new."
  },
  {
   "claim_id": "C200",
   "loglog_ids": [
    "7.10.11"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Iceland blockage interpretation, new."
  },
  {
   "claim_id": "C201",
   "loglog_ids": [
    "7.10.12"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Who-works-for-whom reframe, new."
  },
  {
   "claim_id": "C202",
   "loglog_ids": [
    "7.10.13"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Governance-design framing, new."
  },
  {
   "claim_id": "C203",
   "loglog_ids": [
    "8"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Measuring-stick thesis, new."
  },
  {
   "claim_id": "C204",
   "loglog_ids": [
    "8.1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Reject-balancing recommendation, new."
  },
  {
   "claim_id": "C205",
   "loglog_ids": [
    "8.2"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Byproducts recommendation, canonical occurrence."
  },
  {
   "claim_id": "C206",
   "loglog_ids": [
    "8.3"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Record-pressure causal claim, new."
  },
  {
   "claim_id": "C207",
   "loglog_ids": [
    "8.4"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Reviewable-officials-better claim, new."
  },
  {
   "claim_id": "C208",
   "loglog_ids": [
    "8.5"
   ],
   "label": "Duplicate",
   "canonical_id": "C205",
   "reasoning": "Speed-accountability-as-consequences restates 8.2 with 100% emphasis."
  },
  {
   "claim_id": "C209",
   "loglog_ids": [
    "8.6"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Linux open-work example, new."
  },
  {
   "claim_id": "C210",
   "loglog_ids": [
    "8.7"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Forking fact, new."
  },
  {
   "claim_id": "C211",
   "loglog_ids": [
    "8.8"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Public-complex-systems claim, new."
  },
  {
   "claim_id": "C212",
   "loglog_ids": [
    "8.9"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Cannot-fork-country fact, new."
  },
  {
   "claim_id": "C213",
   "loglog_ids": [
    "8.10"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Voluntary-exit contrast, new."
  },
  {
   "claim_id": "C214",
   "loglog_ids": [
    "8.11"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Affectedness-right-to-see link, new."
  },
  {
   "claim_id": "C215",
   "loglog_ids": [
    "8.12"
   ],
   "label": "Duplicate",
   "canonical_id": "C012",
   "reasoning": "You-are-CEO closing restates citizen-principal claim in 3."
  },
  {
   "claim_id": "C216",
   "loglog_ids": [
    "9"
   ],
   "label": "Trivia",
   "canonical_id": null,
   "reasoning": "Appendix header counting sources; restated header with no substantive content."
  },
  {
   "claim_id": "C217",
   "loglog_ids": [
    "9.1"
   ],
   "label": "Duplicate",
   "canonical_id": "C026",
   "reasoning": "Register restates 1766 first-FOI-law claim from 5.2.1."
  },
  {
   "claim_id": "C218",
   "loglog_ids": [
    "9.2"
   ],
   "label": "Duplicate",
   "canonical_id": "C028",
   "reasoning": "Register restates Chydenius Hats-Caps origin from 5.2.3."
  },
  {
   "claim_id": "C219",
   "loglog_ids": [
    "9.3"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Adds 1998 start and 1996 leak dates absent from body."
  },
  {
   "claim_id": "C220",
   "loglog_ids": [
    "9.4"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Adds 16th-to-2nd rise and 2024 digitalization figure."
  },
  {
   "claim_id": "C221",
   "loglog_ids": [
    "9.5"
   ],
   "label": "Duplicate",
   "canonical_id": "C047",
   "reasoning": "Register restates 20M portal-visit figure from 5.5.2."
  },
  {
   "claim_id": "C222",
   "loglog_ids": [
    "9.6"
   ],
   "label": "Duplicate",
   "canonical_id": "C049",
   "reasoning": "Register restates 60GB/27-year pension find from 5.5.4."
  },
  {
   "claim_id": "C223",
   "loglog_ids": [
    "9.7"
   ],
   "label": "Duplicate",
   "canonical_id": "C032",
   "reasoning": "Register restates OPEN 70-task scope from 5.3.1."
  },
  {
   "claim_id": "C224",
   "loglog_ids": [
    "9.8"
   ],
   "label": "Duplicate",
   "canonical_id": "C036",
   "reasoning": "Register restates corruption-participation link from 5.3.5."
  },
  {
   "claim_id": "C225",
   "loglog_ids": [
    "9.9"
   ],
   "label": "Duplicate",
   "canonical_id": "C052",
   "reasoning": "Register restates 30-business-day cabinet window from 5.6.1."
  },
  {
   "claim_id": "C226",
   "loglog_ids": [
    "9.10"
   ],
   "label": "Duplicate",
   "canonical_id": "C056",
   "reasoning": "Register restates Pol.is mechanism from 5.7.1."
  },
  {
   "claim_id": "C227",
   "loglog_ids": [
    "9.11"
   ],
   "label": "Duplicate",
   "canonical_id": "C193",
   "reasoning": "Register restates Iceland rejected draft from 7.10.4."
  },
  {
   "claim_id": "C228",
   "loglog_ids": [
    "9.12"
   ],
   "label": "Duplicate",
   "canonical_id": "C072",
   "reasoning": "Register restates FREEDOM Act gains and limits from 6.13."
  },
  {
   "claim_id": "C229",
   "loglog_ids": [
    "9.13"
   ],
   "label": "Duplicate",
   "canonical_id": "C075",
   "reasoning": "Register restates GDPR acceleration from 6.16."
  },
  {
   "claim_id": "C230",
   "loglog_ids": [
    "9.14"
   ],
   "label": "Duplicate",
   "canonical_id": "C065",
   "reasoning": "Register restates 2020 illegality rulings from 6.6."
  },
  {
   "claim_id": "C231",
   "loglog_ids": [
    "9.15"
   ],
   "label": "Duplicate",
   "canonical_id": "C081",
   "reasoning": "Register restates Pew 66% figure from 7.1.1."
  },
  {
   "claim_id": "C232",
   "loglog_ids": [
    "9.16"
   ],
   "label": "Duplicate",
   "canonical_id": "C082",
   "reasoning": "Register restates ABC poll history from 7.1.2."
  },
  {
   "claim_id": "C233",
   "loglog_ids": [
    "9.17"
   ],
   "label": "Duplicate",
   "canonical_id": "C088",
   "reasoning": "Register restates IMF-Cambridge friction evidence from 7.2.1."
  },
  {
   "claim_id": "C234",
   "loglog_ids": [
    "9.18"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "World Bank mixed-impact and reversibility point absent from body."
  },
  {
   "claim_id": "C235",
   "loglog_ids": [
    "9.19"
   ],
   "label": "Duplicate",
   "canonical_id": "C099",
   "reasoning": "Register restates Oman backchannel from 7.3.2."
  },
  {
   "claim_id": "C236",
   "loglog_ids": [
    "9.20"
   ],
   "label": "Duplicate",
   "canonical_id": "C110",
   "reasoning": "Register restates 50-state lobbyist study from 7.4.2."
  },
  {
   "claim_id": "C237",
   "loglog_ids": [
    "9.21"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Oxford diplomacy-history survey absent from body."
  },
  {
   "claim_id": "C238",
   "loglog_ids": [
    "9.22"
   ],
   "label": "Duplicate",
   "canonical_id": "C110",
   "reasoning": "Register restates Harden-Kirkland study plus Irish trial figures."
  },
  {
   "claim_id": "C239",
   "loglog_ids": [
    "9.23"
   ],
   "label": "Duplicate",
   "canonical_id": "C125",
   "reasoning": "Register restates Brennan 735-official survey from 7.5.2."
  },
  {
   "claim_id": "C240",
   "loglog_ids": [
    "9.24"
   ],
   "label": "Duplicate",
   "canonical_id": "C129",
   "reasoning": "Register restates doxxing-swatting and AI harassment from 7.5.6."
  },
  {
   "claim_id": "C241",
   "loglog_ids": [
    "9.25"
   ],
   "label": "Duplicate",
   "canonical_id": "C140",
   "reasoning": "Register restates 22-state and Chicago poll figures from 7.6.2-7.6.4."
  },
  {
   "claim_id": "C242",
   "loglog_ids": [
    "9.26"
   ],
   "label": "Duplicate",
   "canonical_id": "C143",
   "reasoning": "Register restates Brennan overclassification and SIPRI trust from 7.6.5-7.6.6."
  },
  {
   "claim_id": "C243",
   "loglog_ids": [
    "9.27"
   ],
   "label": "Duplicate",
   "canonical_id": "C152",
   "reasoning": "Register restates 43-state populism dataset from 7.7.2."
  },
  {
   "claim_id": "C244",
   "loglog_ids": [
    "9.28"
   ],
   "label": "Duplicate",
   "canonical_id": "C157",
   "reasoning": "Register restates Stanford short-termism warning from 7.7.7."
  },
  {
   "claim_id": "C245",
   "loglog_ids": [
    "9.29"
   ],
   "label": "Duplicate",
   "canonical_id": "C167",
   "reasoning": "Register restates Harvard misinformation panel from 7.8.1."
  },
  {
   "claim_id": "C246",
   "loglog_ids": [
    "9.30"
   ],
   "label": "Duplicate",
   "canonical_id": "C194",
   "reasoning": "Register restates OGP 75-country autopsy from 7.10.5."
  },
  {
   "claim_id": "C247",
   "loglog_ids": [
    "9.31"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Hong 2024 and Ruijer 2020 sources absent from body."
  },
  {
   "claim_id": "C248",
   "loglog_ids": [
    "9.32"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Workaround-resistance study absent from body."
  },
  {
   "claim_id": "C249",
   "loglog_ids": [
    "9.33"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Nordicom five-regime comparison absent from body."
  },
  {
   "claim_id": "C250",
   "loglog_ids": [
    "9.34"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Finland 1999 public-by-default law absent from body."
  }
 ],
 "metrics": {
  "scored_claims": 250,
  "unique": 212,
  "duplicates": 36,
  "trivia": 2,
  "redundancy_rate": 0.144,
  "trivia_rate": 0.008,
  "structured_tokens": 296,
  "tokens_per_unique_claim": 1.396
 },
 "prune_list": [
  "C006 duplicates C001, safe to merge",
  "C084 duplicates C020, safe to merge",
  "C122 duplicates C118, safe to merge",
  "C133 duplicates C020, safe to merge",
  "C144 duplicates C064, safe to merge",
  "C174 duplicates C134, safe to merge",
  "C176 duplicates C016, safe to merge",
  "C177 duplicates C014, safe to merge",
  "C208 duplicates C205, safe to merge",
  "C215 duplicates C012, safe to merge",
  "C217 duplicates C026, register recap, safe to merge",
  "C218 duplicates C028, register recap, safe to merge",
  "C221 duplicates C047, register recap, safe to merge",
  "C222 duplicates C049, register recap, safe to merge",
  "C223 duplicates C032, register recap, safe to merge",
  "C224 duplicates C036, register recap, safe to merge",
  "C225 duplicates C052, register recap, safe to merge",
  "C226 duplicates C056, register recap, safe to merge",
  "C227 duplicates C193, register recap, safe to merge",
  "C228 duplicates C072, register recap, safe to merge",
  "C229 duplicates C075, register recap, safe to merge",
  "C230 duplicates C065, register recap, safe to merge",
  "C231 duplicates C081, register recap, safe to merge",
  "C232 duplicates C082, register recap, safe to merge",
  "C233 duplicates C088, register recap, safe to merge",
  "C235 duplicates C099, register recap, safe to merge",
  "C236 duplicates C110, register recap, safe to merge",
  "C238 duplicates C110, register recap, safe to merge",
  "C239 duplicates C125, register recap, safe to merge",
  "C240 duplicates C129, register recap, safe to merge",
  "C241 duplicates C140, register recap, safe to merge",
  "C242 duplicates C143, register recap, safe to merge",
  "C243 duplicates C152, register recap, safe to merge",
  "C244 duplicates C157, register recap, safe to merge",
  "C245 duplicates C167, register recap, safe to merge",
  "C246 duplicates C194, register recap, safe to merge",
  "C079 roadmap transition, trivia, safe to cut",
  "C216 appendix header count, trivia, safe to cut"
 ]
}
```

## Judge Top (overall), opencode-go/deepseek-v4.1-flash

```json
{
 "judge": "overall",
 "judge_version": "1.0.0",
 "model": "deepseek-v4.1-flash (opencode-go/deepseek-v4.1-flash), 2026-09-15",
 "source_id": "unspecified",
 "inputs": {
  "faithfulness_precision": 0.98,
  "critical_errors": 0,
  "must_recall": 1.0,
  "overall_recall": 1.0,
  "redundancy_rate": 0.144,
  "trivia_rate": 0.008
 },
 "weights_used": {
  "faithfulness_precision": 0.4,
  "coverage_must_recall": 0.4,
  "redundancy_penalty": 0.2
 },
 "computation": "weighted = 0.4*0.98 + 0.4*1.0 - 0.2*0.144 = 0.392 + 0.4 - 0.0288 = 0.7632",
 "weighted_score": 0.7632,
 "verdict": "Pass",
 "tradeoff_note": "Coverage is complete (must_recall 1.0) and faithfulness is clean (0.98, zero critical), so the length cost is justified. Redundancy at 0.144 sits just under the 0.15 max, leaving almost no margin, so it is the main risk to watch but does not fail the sample.",
 "fix_list": [
  "Merge the register recap duplicates C217-C246 (30 entries) plus C006/C084/C122/C133/C144/C174/C176/C177/C208/C215 to pull redundancy well below the 0.15 cap.",
  "Fix C032: say environmental regulation and urban planning (not 'permits'), and tie 'real time' to showing citizens, matching 5.3.1.",
  "Fix C068: restore the 'reportedly' hedge for the NSA's 2018 abandonment per 6.9.",
  "Soften absolute framings to match hedged sources: C135 ('starve' vs 'less room to grow', 7.5.12), C143 (SIPRI 'can help prevent'/'generally considered', 7.6.6), C170 (citizens 'may react negatively', 7.8.4)."
 ],
 "reasoning": "Gate checks in order. (1) critical_errors = 0 against critical_contradicted_max = 0: pass. (2) must_recall = 1.0 against must_recall_min = 0.90: pass, all 15 must-have points present with zero partial or missing. (3) faithfulness_precision = 0.98 against faithfulness_precision_min = 0.95: pass, 245/250 supported and 0 contradicted. (4) redundancy_rate = 0.144 against redundancy_max = 0.15: pass, though only by 0.006. No hard gate is missed, so the sample cannot Fail. The remaining non-supported items are five Partially supported claims, all severity Minor: C032 (number correct but 'permits' mislabels environmental/urban items in 5.3.1), C068 (drops source's 'reportedly' from 6.9), C135 ('starve' strengthens 'less room to grow' from 7.5.12), C143 (absolutes where source hedges 'generally considered', 'can help prevent' in 7.6.6), C170 (settled dislike vs 'may react negatively' in 7.8.4). These are hedging/attribution slips rather than factual contradictions, none is Critical, and coverage marks no must-have as partial or missing, so no Partial claim is shown to sit on an unmet Must-have point. That fails to trigger the Borderline condition as specified, so the label is Pass rather than Borderline. Weighted score: 0.4*0.98=0.392, 0.4*1.0=0.4, 0.2*0.144=0.0288, total 0.7632. Concision played no rescue role; its only effect is the -0.0288 penalty, and the coverage gain (1.0 recall) justifies the current length only because redundancy stayed under the cap. Highest-leverage improvement is trimming the 36 duplicates, dominated by the C217-C246 register recap block, since that both lowers redundancy and raises tokens-per-unique-claim efficiency without touching coverage."
}
```
