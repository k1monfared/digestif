# Judge trace (scripted pipeline, opencode-go/deepseek-v4.1-flash)

## Judge F (faithfulness), opencode-go/deepseek-v4.1-flash

```json
{
 "judge": "faithfulness",
 "judge_version": "1.0.0",
 "model": "opencode-go/deepseek-v4.1-flash (opencode) scripted pipeline 2026-09-15",
 "source_id": "03_cant_stop_addicted_to_shindig",
 "claims": [
  {
   "claim_id": "C001",
   "loglog_ids": [
    "0"
   ],
   "claim_text": "Can't Stop analysis shows four-dice odds flatten the distribution, middle columns dominate, probabilistic stopping wins, and forced moves balance design.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "Four-dice probabilities flatten the distribution... Probabilistic strategies dominate... forced-move rule compensates for the mathematical imbalance.",
   "reasoning": "Each summary component matches a conclusion in the source."
  },
  {
   "claim_id": "C002",
   "loglog_ids": [
    "1"
   ],
   "claim_text": "Push-your-luck rules: roll four dice, pair freely, bust loses turn progress.",
   "claim_type": "definition",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "roll four dice, pair them up however you want... if you can't move any of your three active markers, you lose everything you've gained that turn",
   "reasoning": "All three rule elements are stated directly."
  },
  {
   "claim_id": "C003",
   "loglog_ids": [
    "1.1"
   ],
   "claim_text": "Board columns 2 to 12 vary 3 to 13 steps; complete three to win.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "columns numbered 2 through 12... Columns 2 and 12: 3 steps... Column 7: 13 steps. You need to complete three columns to win.",
   "reasoning": "Range and completion condition match source exactly."
  },
  {
   "claim_id": "C004",
   "loglog_ids": [
    "1.2"
   ],
   "claim_text": "Forced-move rule requires taking every legal move from the chosen pairing.",
   "claim_type": "definition",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "you must make ALL legal moves from that pairing, even if you don't want them",
   "reasoning": "Direct restatement of the forced-move rule."
  },
  {
   "claim_id": "C005",
   "loglog_ids": [
    "1.3"
   ],
   "claim_text": "Chasing 7 on {6,7,8} can force an unwanted 2 onto the board.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "you're forced to take BOTH the 2 and the 7, even though column 2 isn't in your plan",
   "reasoning": "Matches the source example precisely."
  },
  {
   "claim_id": "C006",
   "loglog_ids": [
    "2"
   ],
   "claim_text": "Four-dice pairing flattens the probability distribution versus two dice.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "Four-dice probabilities flatten the distribution",
   "reasoning": "Source conclusion states this explicitly."
  },
  {
   "claim_id": "C007",
   "loglog_ids": [
    "2.1"
   ],
   "claim_text": "Two-dice baseline: 7 hits 16.67%, six times more likely than 2.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "sum 7 is the most likely at 16.67%, and it's exactly 6x more likely than sum 2 at 2.78%",
   "reasoning": "Numbers match exactly."
  },
  {
   "claim_id": "C008",
   "loglog_ids": [
    "2.2"
   ],
   "claim_text": "Four dice yield exactly three possible pairings per roll.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "That's it, just three possible pairings.",
   "reasoning": "Count of three pairings is stated in source."
  },
  {
   "claim_id": "C009",
   "loglog_ids": [
    "2.3"
   ],
   "claim_text": "Making a 2 needs two 1s: 171/1296, about 13.2%.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "P(can make a 2) = ... = 171/1296 approx 13.2%",
   "reasoning": "Fraction and percentage match the source."
  },
  {
   "claim_id": "C010",
   "loglog_ids": [
    "2.4"
   ],
   "claim_text": "Making a 7 via inclusion-exclusion: 834/1296, about 64.4%.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "= 834/1296 approx 64.4%",
   "reasoning": "Fraction and percentage match the source."
  },
  {
   "claim_id": "C011",
   "loglog_ids": [
    "2.5"
   ],
   "claim_text": "Probability ratio 4.88 nearly matches length ratio 4.33; designers thought carefully.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "The probability ratio from 2 to 7 is 4.88. The length ratio is 4.33. Pretty close! The game designers were definitely thinking about this.",
   "reasoning": "Both ratios and the inference match the source."
  },
  {
   "claim_id": "C012",
   "loglog_ids": [
    "3"
   ],
   "claim_text": "Column combinations matter more than individual column odds.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "Column combinations matter more than individual columns",
   "reasoning": "Source conclusion states this directly."
  },
  {
   "claim_id": "C013",
   "loglog_ids": [
    "3.1"
   ],
   "claim_text": "Expected rolls cluster near 20; long column 7 completes slightly faster than 2.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "For column 2: 3/0.132 = 22.73 rolls. For column 7: 13/0.644 = 20.18 rolls. Column 7 is slightly faster",
   "reasoning": "Values and comparison match the source."
  },
  {
   "claim_id": "C014",
   "loglog_ids": [
    "3.2"
   ],
   "claim_text": "{6,7,8} succeeds 92% per roll; {2,3,12} only 43.8%.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "{6,7,8}, you have a 92% chance of not busting... {2,3,12}: 568/1296 = 43.8% success rate",
   "reasoning": "Both success rates match the source."
  },
  {
   "claim_id": "C015",
   "loglog_ids": [
    "3.3"
   ],
   "claim_text": "37 combos rate excellent; median succeeds 79.6%, worst collapse to 43.8%.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "37 combinations are 'excellent'... median combination still succeeds 79.6%... worst combinations drop dramatically to just 43.8%",
   "reasoning": "All three numbers match the source."
  },
  {
   "claim_id": "C016",
   "loglog_ids": [
    "4"
   ],
   "claim_text": "Stopping rule weighs expected gain against bust-weighted unsaved progress.",
   "claim_type": "definition",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "Keep rolling if: (P_success x Q) > (P_bust x U)",
   "reasoning": "Describes the source heuristic formula accurately."
  },
  {
   "claim_id": "C017",
   "loglog_ids": [
    "4.1"
   ],
   "claim_text": "Roll on {6,7,8} with five steps banked; stop on {2,3,12} with two.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "On {6,7,8} with 5 unsaved steps... keep rolling. On {2,3,12} with 2 unsaved steps... STOP.",
   "reasoning": "Both step counts and decisions match the source."
  },
  {
   "claim_id": "C018",
   "loglog_ids": [
    "4.2"
   ],
   "claim_text": "Only 39.8% of {6,7,8} rolls are clean; {2,3,12} just 2.3%.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "Only 39.8% of rolls give a clean move on {6,7,8}... For {2,3,12}: Only 2.3% of rolls are clean!",
   "reasoning": "Both percentages match the source."
  },
  {
   "claim_id": "C019",
   "loglog_ids": [
    "4.3"
   ],
   "claim_text": "Continuing current columns usually beats switching, but author hedges: switching unanalyzed quantitatively.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "The mathematics favor continuation in most cases... I haven't fully analyzed this aspect quantitatively.",
   "reasoning": "Hedge is preserved exactly as in source."
  },
  {
   "claim_id": "C020",
   "loglog_ids": [
    "5"
   ],
   "claim_text": "3.6M-game simulations crown probabilistic, consistent strategies over fast ones.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "3.6 million total games... Probabilistic strategies dominate the top rankings... consistency beats raw speed",
   "reasoning": "Combines source findings faithfully."
  },
  {
   "claim_id": "C021",
   "loglog_ids": [
    "5.1"
   ],
   "claim_text": "38 strategy families tested across single-player and head-to-head simulations.",
   "claim_type": "number_or_date",
   "verdict": "Partially supported",
   "severity": "Minor",
   "evidence_quote": "I tested 38 strategies across 14 different strategic families",
   "reasoning": "Number 38 is right for strategies, but source reports 14 families, not 38, mislabeling the count."
  },
  {
   "claim_id": "C022",
   "loglog_ids": [
    "5.2"
   ],
   "claim_text": "GreedyUntil1Col fastest at 10.5 turns but busts 7.5 times per game.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "GreedyUntil1Col is fastest (10.5 turns)... bust rate (7.5 per game)",
   "reasoning": "Both figures match the source."
  },
  {
   "claim_id": "C023",
   "loglog_ids": [
    "5.3"
   ],
   "claim_text": "FiftyPercentSurvival wins 69.84% by stopping below 50% cumulative survival.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "FiftyPercentSurvival dominates with 69.84% overall win rate... Roll until cumulative survival probability drops below 50%",
   "reasoning": "Win rate and rule match the source."
  },
  {
   "claim_id": "C024",
   "loglog_ids": [
    "5.4"
   ],
   "claim_text": "Consistency beats raw speed; pure greedy loses nearly everything.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "Consistency > Speed... The pure Greedy strategy (never stop voluntarily) lost essentially every game.",
   "reasoning": "Both claims are stated in the source."
  },
  {
   "claim_id": "C025",
   "loglog_ids": [
    "5.5"
   ],
   "claim_text": "First player wins 55.59%, an 11.18% edge exceeding chess and Go.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "Player 1 wins 55.59%... First-player advantage: +11.18%... larger than chess (~5%) or Go (~7%)",
   "reasoning": "All figures and comparison match the source."
  },
  {
   "claim_id": "C026",
   "loglog_ids": [
    "6"
   ],
   "claim_text": "Board is nearly balanced singly; forced moves compensate combination imbalance.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "The deviations are +-13.6% at most... forced-move rule compensates for the mathematical imbalance",
   "reasoning": "Both components are stated in the source."
  },
  {
   "claim_id": "C027",
   "loglog_ids": [
    "6.1"
   ],
   "claim_text": "Single-column completion deviates at most 13.6% from 20 rolls.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "The deviations are +-13.6% at most.",
   "reasoning": "Deviation bound matches the source."
  },
  {
   "claim_id": "C028",
   "loglog_ids": [
    "6.2"
   ],
   "claim_text": "Adding one step per middle column would quadruple balance precision.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "Optimal board (+-1 step from current)... 4x more balanced with just +1 step!",
   "reasoning": "The 4x improvement and +1 step match the source."
  },
  {
   "claim_id": "C029",
   "loglog_ids": [
    "6.3"
   ],
   "claim_text": "Forced moves contaminate strong combos, keeping strategy choices interesting.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "add rules that turn that imbalance into interesting strategic choices",
   "reasoning": "Source describes forced moves as contamination and a balancing mechanism."
  },
  {
   "claim_id": "C030",
   "loglog_ids": [
    "7"
   ],
   "claim_text": "Play middle columns consistently; designers should favor playability over perfection.",
   "claim_type": "recommendation",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "Aim for columns 5-9... prioritize consistency over aggressive play. For game designers: Prioritize playability over mathematical perfection",
   "reasoning": "Both recommendations restate the source."
  },
  {
   "claim_id": "C031",
   "loglog_ids": [
    "7.1"
   ],
   "claim_text": "Aim for columns 5-9, avoid edge columns, prioritize consistency over aggression.",
   "claim_type": "recommendation",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "Aim for columns 5-9, avoid forcing activation of columns 2-3 and 11-12, and prioritize consistency over aggressive play",
   "reasoning": "Advice matches the source exactly."
  },
  {
   "claim_id": "C032",
   "loglog_ids": [
    "7.2"
   ],
   "claim_text": "All code, simulations, and datasets are published for reuse.",
   "claim_type": "meta",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "All analysis code and simulation results are available",
   "reasoning": "Source states code and results are available."
  }
 ],
 "metrics": {
  "total_claims": 32,
  "supported": 31,
  "partially_supported": 1,
  "unverifiable": 0,
  "contradicted": 0,
  "critical_errors": 0,
  "faithfulness_precision": 0.9688
 },
 "fail_list": [
  "C021"
 ]
}
```

## Judge Cov (coverage), opencode-go/deepseek-v4.1-flash

```json
{
 "judge": "coverage",
 "judge_version": "1.0.0",
 "model": "opencode-go/deepseek-v4.1-flash (opencode) scripted pipeline 2026-09-15",
 "source_id": "03_cant_stop_addicted_to_shindig",
 "key_points": [
  {
   "point_id": "K01",
   "point_text": "Central thesis: Can't Stop is a masterclass in practical game design, where imperfect mathematical balance is acceptable and rules are used to compensate for it.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L002",
    "L027",
    "L030",
    "L031"
   ],
   "evidence_quote": "forced moves compensate combination imbalance ... designers should favor playability over perfection",
   "reasoning": "L002 summary states forced moves balance design; L030 notes forced moves compensate; L031 frames playability over perfection, matching the thesis."
  },
  {
   "point_id": "K02",
   "point_text": "Game rules: roll four dice, pair them to move markers on columns 2 through 12, need three completed columns to win; column lengths are 3,5,7,9,11,13,11,9,7,5,3.",
   "weight": "Must have",
   "presence": "Partial",
   "loglog_ids": [
    "L003",
    "L004"
   ],
   "evidence_quote": "Board columns 2 to 12 vary 3 to 13 steps; complete three to win",
   "reasoning": "Rules captured but exact column lengths (3,5,7,9,11,13,11,9,7,5,3) are not enumerated, only the 3-to-13 range. Dropped numbers make this Partial."
  },
  {
   "point_id": "K03",
   "point_text": "Forced-move rule: if a chosen pairing creates any valid move you must take all legal moves from that pairing, even onto unwanted columns; you cannot cherry-pick.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L005",
    "L006"
   ],
   "evidence_quote": "Forced-move rule requires taking every legal move from the chosen pairing",
   "reasoning": "L005 states the rule directly; L006 gives the unwanted-move example, preserving meaning."
  },
  {
   "point_id": "K04",
   "point_text": "Two-dice baseline: sum 7 is most likely at 16.67%, exactly 6 times more likely than sum 2 at 2.78%.",
   "weight": "Must have",
   "presence": "Partial",
   "loglog_ids": [
    "L008"
   ],
   "evidence_quote": "Two-dice baseline: 7 hits 16.67%, six times more likely than 2",
   "reasoning": "16.67% and the 6x ratio are present, but the 2.78% baseline probability for sum 2 is dropped. Dropped number caps at Partial."
  },
  {
   "point_id": "K05",
   "point_text": "With four dice the distribution flattens: P(can make 7) = 64.4% and P(can make 2) = 13.2%, only a 4.88x ratio versus 6x with two dice.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L010",
    "L011",
    "L012"
   ],
   "evidence_quote": "Making a 2 ... about 13.2% ... Making a 7 ... about 64.4% ... Probability ratio 4.88",
   "reasoning": "All three figures (13.2%, 64.4%, 4.88) are captured with correct meaning."
  },
  {
   "point_id": "K06",
   "point_text": "Expected rolls to complete a column = length / probability; column 2 needs about 22.73 rolls while column 7 needs about 20.18, so 7 is slightly faster despite being 4x longer.",
   "weight": "Must have",
   "presence": "Partial",
   "loglog_ids": [
    "L014"
   ],
   "evidence_quote": "Expected rolls cluster near 20; long column 7 completes slightly faster than 2",
   "reasoning": "The qualitative finding is retained, but the exact expected values 22.73 and 20.18 are dropped. Dropped numbers make this Partial."
  },
  {
   "point_id": "K07",
   "point_text": "Column combinations matter: {6,7,8} succeeds 92.0% of the time versus 43.8% for {2,3,12}; all 165 three-column combinations were analyzed, with 37 rated excellent (>=85% success) and a median success of 79.6%.",
   "weight": "Must have",
   "presence": "Partial",
   "loglog_ids": [
    "L015",
    "L016"
   ],
   "evidence_quote": "{6,7,8} succeeds 92% per roll; {2,3,12} only 43.8% ... 37 combos rate excellent; median succeeds 79.6%",
   "reasoning": "92%, 43.8%, 37 and 79.6% captured, but the total count of 165 combinations and the >=85% excellent threshold are dropped. Dropped numbers cap at Partial."
  },
  {
   "point_id": "K08",
   "point_text": "\"Clean\" moves are rare: even the best combination {6,7,8} yields only 39.8% clean rolls, and {2,3,12} only 2.3%, so the forced-move rule contaminates good combinations.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L019",
    "L030",
    "L035"
   ],
   "evidence_quote": "Only 39.8% of {6,7,8} rolls are clean; {2,3,12} just 2.3%",
   "reasoning": "Both percentages preserved and the contamination link to forced moves is stated in L030/L035."
  },
  {
   "point_id": "K09",
   "point_text": "Stopping heuristic: keep rolling if (P_success x Q) > (P_bust x U), where Q is expected markers advanced and U is unsaved progress; example on {6,7,8} says roll (1.32 > 0.4) and on {2,3,12} says stop (1.12 > 0.46).",
   "weight": "Must have",
   "presence": "Partial",
   "loglog_ids": [
    "L017",
    "L018"
   ],
   "evidence_quote": "Stopping rule weighs expected gain against bust-weighted unsaved progress ... Roll on {6,7,8} with five steps banked; stop on {2,3,12} with two",
   "reasoning": "The heuristic's conceptual form and the directional decisions survive, but the explicit inequality and the numeric values 1.32/0.4 and 1.12/0.46 are dropped. Partial."
  },
  {
   "point_id": "K10",
   "point_text": "Tournament of 38 strategies across 2,500 head-to-head games each (3.6M total games) found FiftyPercentSurvival the champion at 69.84% win rate, and probabilistic strategies dominate the top rankings.",
   "weight": "Must have",
   "presence": "Partial",
   "loglog_ids": [
    "L021",
    "L022",
    "L024"
   ],
   "evidence_quote": "3.6M-game simulations crown probabilistic, consistent strategies over fast ones ... 38 strategy families ... FiftyPercentSurvival wins 69.84%",
   "reasoning": "38 strategies, 3.6M games and 69.84% all present, but the 2,500 games per head-to-head pairing is dropped. Dropped number makes this Partial."
  },
  {
   "point_id": "K11",
   "point_text": "Consistency beats speed: GreedyUntil1Col is fastest (10.5 turns) but only ranks #11 at 58.90% due to high variance and bust rate, while FiftyPercentSurvival at 11.3 turns wins most.",
   "weight": "Must have",
   "presence": "Partial",
   "loglog_ids": [
    "L023",
    "L024",
    "L025"
   ],
   "evidence_quote": "GreedyUntil1Col fastest at 10.5 turns but busts 7.5 times per game ... Consistency beats raw speed",
   "reasoning": "The core contrast and 10.5-turn speed are present, but the #11 ranking, 58.90% win rate and FiftyPercentSurvival's 11.3 turns are dropped. Partial."
  },
  {
   "point_id": "K12",
   "point_text": "Significant first-player advantage: P1 wins 55.59% of games for a +11.18% edge, larger than chess (~5%) or Go (~7%); GreedyUntil1Col shows extreme bias at +31.24%.",
   "weight": "Must have",
   "presence": "Partial",
   "loglog_ids": [
    "L026"
   ],
   "evidence_quote": "First player wins 55.59%, an 11.18% edge exceeding chess and Go",
   "reasoning": "55.59%, 11.18% and the chess/Go comparison are retained, but the GreedyUntil1Col +31.24% extreme-bias figure is dropped. Partial."
  },
  {
   "point_id": "K13",
   "point_text": "Balance analysis: single-column completion times deviate at most +/-13.6% from 20 rolls, an optimal board one step from current reaches +/-3.09%, and a 20-step board reaches +/-2.17%.",
   "weight": "Must have",
   "presence": "Partial",
   "loglog_ids": [
    "L028",
    "L029"
   ],
   "evidence_quote": "Single-column completion deviates at most 13.6% from 20 rolls ... Adding one step per middle column would quadruple balance precision",
   "reasoning": "The 13.6% deviation and the one-step improvement idea are present, but the explicit +/-3.09% and +/-2.17% figures are dropped. Partial."
  },
  {
   "point_id": "K14",
   "point_text": "Stated caveat: continuation versus switching strategies were not fully analyzed quantitatively and remain an open question for future work.",
   "weight": "Nice to have",
   "presence": "Present",
   "loglog_ids": [
    "L020"
   ],
   "evidence_quote": "Continuing current columns usually beats switching, but author hedges: switching unanalyzed quantitatively",
   "reasoning": "The caveat and its quantitative-unanalyzed status are preserved."
  },
  {
   "point_id": "K15",
   "point_text": "Recommendations: players should use FiftyPercentSurvival and aim for columns 5-9 while avoiding forced activation of 2-3 and 11-12; designers should prioritize playability and use rules to compensate for imbalance, considering handicaps for turn order.",
   "weight": "Must have",
   "presence": "Partial",
   "loglog_ids": [
    "L031",
    "L032"
   ],
   "evidence_quote": "Aim for columns 5-9, avoid edge columns ... designers should favor playability over perfection",
   "reasoning": "The 5-9 target, edge avoidance and playability advice are present, but the explicit FiftyPercentSurvival player recommendation and the turn-order handicap suggestion are not captured. Partial."
  }
 ],
 "metrics": {
  "total_points": 15,
  "must_have_total": 14,
  "must_have_present": 4,
  "must_have_partial": 10,
  "must_have_missing": 0,
  "overall_present": 5,
  "must_recall": 0.6429,
  "overall_recall": 0.6667
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
 "source_id": "03_cant_stop_addicted_to_shindig",
 "claims": [
  {
   "claim_id": "C001",
   "loglog_ids": [
    "0"
   ],
   "claim_text": "Can't Stop analysis shows four-dice odds flatten the distribution, middle columns dominate, probabilistic stopping wins, and forced moves balance design.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "Four-dice probabilities flatten the distribution... Probabilistic strategies dominate... forced-move rule compensates for the mathematical imbalance.",
   "reasoning": "Each summary component matches a conclusion in the source."
  },
  {
   "claim_id": "C002",
   "loglog_ids": [
    "1"
   ],
   "claim_text": "Push-your-luck rules: roll four dice, pair freely, bust loses turn progress.",
   "claim_type": "definition",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "roll four dice, pair them up however you want... if you can't move any of your three active markers, you lose everything you've gained that turn",
   "reasoning": "All three rule elements are stated directly."
  },
  {
   "claim_id": "C003",
   "loglog_ids": [
    "1.1"
   ],
   "claim_text": "Board columns 2 to 12 vary 3 to 13 steps; complete three to win.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "columns numbered 2 through 12... Columns 2 and 12: 3 steps... Column 7: 13 steps. You need to complete three columns to win.",
   "reasoning": "Range and completion condition match source exactly."
  },
  {
   "claim_id": "C004",
   "loglog_ids": [
    "1.2"
   ],
   "claim_text": "Forced-move rule requires taking every legal move from the chosen pairing.",
   "claim_type": "definition",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "you must make ALL legal moves from that pairing, even if you don't want them",
   "reasoning": "Direct restatement of the forced-move rule."
  },
  {
   "claim_id": "C005",
   "loglog_ids": [
    "1.3"
   ],
   "claim_text": "Chasing 7 on {6,7,8} can force an unwanted 2 onto the board.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "you're forced to take BOTH the 2 and the 7, even though column 2 isn't in your plan",
   "reasoning": "Matches the source example precisely."
  },
  {
   "claim_id": "C006",
   "loglog_ids": [
    "2"
   ],
   "claim_text": "Four-dice pairing flattens the probability distribution versus two dice.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "Four-dice probabilities flatten the distribution",
   "reasoning": "Source conclusion states this explicitly."
  },
  {
   "claim_id": "C007",
   "loglog_ids": [
    "2.1"
   ],
   "claim_text": "Two-dice baseline: 7 hits 16.67%, six times more likely than 2.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "sum 7 is the most likely at 16.67%, and it's exactly 6x more likely than sum 2 at 2.78%",
   "reasoning": "Numbers match exactly."
  },
  {
   "claim_id": "C008",
   "loglog_ids": [
    "2.2"
   ],
   "claim_text": "Four dice yield exactly three possible pairings per roll.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "That's it, just three possible pairings.",
   "reasoning": "Count of three pairings is stated in source."
  },
  {
   "claim_id": "C009",
   "loglog_ids": [
    "2.3"
   ],
   "claim_text": "Making a 2 needs two 1s: 171/1296, about 13.2%.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "P(can make a 2) = ... = 171/1296 approx 13.2%",
   "reasoning": "Fraction and percentage match the source."
  },
  {
   "claim_id": "C010",
   "loglog_ids": [
    "2.4"
   ],
   "claim_text": "Making a 7 via inclusion-exclusion: 834/1296, about 64.4%.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "= 834/1296 approx 64.4%",
   "reasoning": "Fraction and percentage match the source."
  },
  {
   "claim_id": "C011",
   "loglog_ids": [
    "2.5"
   ],
   "claim_text": "Probability ratio 4.88 nearly matches length ratio 4.33; designers thought carefully.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "The probability ratio from 2 to 7 is 4.88. The length ratio is 4.33. Pretty close! The game designers were definitely thinking about this.",
   "reasoning": "Both ratios and the inference match the source."
  },
  {
   "claim_id": "C012",
   "loglog_ids": [
    "3"
   ],
   "claim_text": "Column combinations matter more than individual column odds.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "Column combinations matter more than individual columns",
   "reasoning": "Source conclusion states this directly."
  },
  {
   "claim_id": "C013",
   "loglog_ids": [
    "3.1"
   ],
   "claim_text": "Expected rolls cluster near 20; long column 7 completes slightly faster than 2.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "For column 2: 3/0.132 = 22.73 rolls. For column 7: 13/0.644 = 20.18 rolls. Column 7 is slightly faster",
   "reasoning": "Values and comparison match the source."
  },
  {
   "claim_id": "C014",
   "loglog_ids": [
    "3.2"
   ],
   "claim_text": "{6,7,8} succeeds 92% per roll; {2,3,12} only 43.8%.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "{6,7,8}, you have a 92% chance of not busting... {2,3,12}: 568/1296 = 43.8% success rate",
   "reasoning": "Both success rates match the source."
  },
  {
   "claim_id": "C015",
   "loglog_ids": [
    "3.3"
   ],
   "claim_text": "37 combos rate excellent; median succeeds 79.6%, worst collapse to 43.8%.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "37 combinations are 'excellent'... median combination still succeeds 79.6%... worst combinations drop dramatically to just 43.8%",
   "reasoning": "All three numbers match the source."
  },
  {
   "claim_id": "C016",
   "loglog_ids": [
    "4"
   ],
   "claim_text": "Stopping rule weighs expected gain against bust-weighted unsaved progress.",
   "claim_type": "definition",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "Keep rolling if: (P_success x Q) > (P_bust x U)",
   "reasoning": "Describes the source heuristic formula accurately."
  },
  {
   "claim_id": "C017",
   "loglog_ids": [
    "4.1"
   ],
   "claim_text": "Roll on {6,7,8} with five steps banked; stop on {2,3,12} with two.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "On {6,7,8} with 5 unsaved steps... keep rolling. On {2,3,12} with 2 unsaved steps... STOP.",
   "reasoning": "Both step counts and decisions match the source."
  },
  {
   "claim_id": "C018",
   "loglog_ids": [
    "4.2"
   ],
   "claim_text": "Only 39.8% of {6,7,8} rolls are clean; {2,3,12} just 2.3%.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "Only 39.8% of rolls give a clean move on {6,7,8}... For {2,3,12}: Only 2.3% of rolls are clean!",
   "reasoning": "Both percentages match the source."
  },
  {
   "claim_id": "C019",
   "loglog_ids": [
    "4.3"
   ],
   "claim_text": "Continuing current columns usually beats switching, but author hedges: switching unanalyzed quantitatively.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "The mathematics favor continuation in most cases... I haven't fully analyzed this aspect quantitatively.",
   "reasoning": "Hedge is preserved exactly as in source."
  },
  {
   "claim_id": "C020",
   "loglog_ids": [
    "5"
   ],
   "claim_text": "3.6M-game simulations crown probabilistic, consistent strategies over fast ones.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "3.6 million total games... Probabilistic strategies dominate the top rankings... consistency beats raw speed",
   "reasoning": "Combines source findings faithfully."
  },
  {
   "claim_id": "C021",
   "loglog_ids": [
    "5.1"
   ],
   "claim_text": "38 strategy families tested across single-player and head-to-head simulations.",
   "claim_type": "number_or_date",
   "verdict": "Partially supported",
   "severity": "Minor",
   "evidence_quote": "I tested 38 strategies across 14 different strategic families",
   "reasoning": "Number 38 is right for strategies, but source reports 14 families, not 38, mislabeling the count."
  },
  {
   "claim_id": "C022",
   "loglog_ids": [
    "5.2"
   ],
   "claim_text": "GreedyUntil1Col fastest at 10.5 turns but busts 7.5 times per game.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "GreedyUntil1Col is fastest (10.5 turns)... bust rate (7.5 per game)",
   "reasoning": "Both figures match the source."
  },
  {
   "claim_id": "C023",
   "loglog_ids": [
    "5.3"
   ],
   "claim_text": "FiftyPercentSurvival wins 69.84% by stopping below 50% cumulative survival.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "FiftyPercentSurvival dominates with 69.84% overall win rate... Roll until cumulative survival probability drops below 50%",
   "reasoning": "Win rate and rule match the source."
  },
  {
   "claim_id": "C024",
   "loglog_ids": [
    "5.4"
   ],
   "claim_text": "Consistency beats raw speed; pure greedy loses nearly everything.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "Consistency > Speed... The pure Greedy strategy (never stop voluntarily) lost essentially every game.",
   "reasoning": "Both claims are stated in the source."
  },
  {
   "claim_id": "C025",
   "loglog_ids": [
    "5.5"
   ],
   "claim_text": "First player wins 55.59%, an 11.18% edge exceeding chess and Go.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "Player 1 wins 55.59%... First-player advantage: +11.18%... larger than chess (~5%) or Go (~7%)",
   "reasoning": "All figures and comparison match the source."
  },
  {
   "claim_id": "C026",
   "loglog_ids": [
    "6"
   ],
   "claim_text": "Board is nearly balanced singly; forced moves compensate combination imbalance.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "The deviations are +-13.6% at most... forced-move rule compensates for the mathematical imbalance",
   "reasoning": "Both components are stated in the source."
  },
  {
   "claim_id": "C027",
   "loglog_ids": [
    "6.1"
   ],
   "claim_text": "Single-column completion deviates at most 13.6% from 20 rolls.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "The deviations are +-13.6% at most.",
   "reasoning": "Deviation bound matches the source."
  },
  {
   "claim_id": "C028",
   "loglog_ids": [
    "6.2"
   ],
   "claim_text": "Adding one step per middle column would quadruple balance precision.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "Optimal board (+-1 step from current)... 4x more balanced with just +1 step!",
   "reasoning": "The 4x improvement and +1 step match the source."
  },
  {
   "claim_id": "C029",
   "loglog_ids": [
    "6.3"
   ],
   "claim_text": "Forced moves contaminate strong combos, keeping strategy choices interesting.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "add rules that turn that imbalance into interesting strategic choices",
   "reasoning": "Source describes forced moves as contamination and a balancing mechanism."
  },
  {
   "claim_id": "C030",
   "loglog_ids": [
    "7"
   ],
   "claim_text": "Play middle columns consistently; designers should favor playability over perfection.",
   "claim_type": "recommendation",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "Aim for columns 5-9... prioritize consistency over aggressive play. For game designers: Prioritize playability over mathematical perfection",
   "reasoning": "Both recommendations restate the source."
  },
  {
   "claim_id": "C031",
   "loglog_ids": [
    "7.1"
   ],
   "claim_text": "Aim for columns 5-9, avoid edge columns, prioritize consistency over aggression.",
   "claim_type": "recommendation",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "Aim for columns 5-9, avoid forcing activation of columns 2-3 and 11-12, and prioritize consistency over aggressive play",
   "reasoning": "Advice matches the source exactly."
  },
  {
   "claim_id": "C032",
   "loglog_ids": [
    "7.2"
   ],
   "claim_text": "All code, simulations, and datasets are published for reuse.",
   "claim_type": "meta",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "All analysis code and simulation results are available",
   "reasoning": "Source states code and results are available."
  }
 ],
 "metrics": {
  "total_claims": 32,
  "supported": 31,
  "partially_supported": 1,
  "unverifiable": 0,
  "contradicted": 0,
  "critical_errors": 0,
  "faithfulness_precision": 0.9688
 },
 "fail_list": [
  "C021"
 ]
}
```

## Judge Cov (coverage), opencode-go/deepseek-v4.1-flash

```json
{
 "judge": "coverage",
 "judge_version": "1.0.0",
 "model": "opencode-go/deepseek-v4.1-flash (opencode) scripted pipeline 2026-09-15",
 "source_id": "03_cant_stop_addicted_to_shindig",
 "key_points": [
  {
   "point_id": "K01",
   "point_text": "Central thesis: Can't Stop is a masterclass in practical game design, where imperfect mathematical balance is acceptable and rules are used to compensate for it.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L002",
    "L027",
    "L030",
    "L031"
   ],
   "evidence_quote": "forced moves compensate combination imbalance ... designers should favor playability over perfection",
   "reasoning": "L002 summary states forced moves balance design; L030 notes forced moves compensate; L031 frames playability over perfection, matching the thesis."
  },
  {
   "point_id": "K02",
   "point_text": "Game rules: roll four dice, pair them to move markers on columns 2 through 12, need three completed columns to win; column lengths are 3,5,7,9,11,13,11,9,7,5,3.",
   "weight": "Must have",
   "presence": "Partial",
   "loglog_ids": [
    "L003",
    "L004"
   ],
   "evidence_quote": "Board columns 2 to 12 vary 3 to 13 steps; complete three to win",
   "reasoning": "Rules captured but exact column lengths (3,5,7,9,11,13,11,9,7,5,3) are not enumerated, only the 3-to-13 range. Dropped numbers make this Partial."
  },
  {
   "point_id": "K03",
   "point_text": "Forced-move rule: if a chosen pairing creates any valid move you must take all legal moves from that pairing, even onto unwanted columns; you cannot cherry-pick.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L005",
    "L006"
   ],
   "evidence_quote": "Forced-move rule requires taking every legal move from the chosen pairing",
   "reasoning": "L005 states the rule directly; L006 gives the unwanted-move example, preserving meaning."
  },
  {
   "point_id": "K04",
   "point_text": "Two-dice baseline: sum 7 is most likely at 16.67%, exactly 6 times more likely than sum 2 at 2.78%.",
   "weight": "Must have",
   "presence": "Partial",
   "loglog_ids": [
    "L008"
   ],
   "evidence_quote": "Two-dice baseline: 7 hits 16.67%, six times more likely than 2",
   "reasoning": "16.67% and the 6x ratio are present, but the 2.78% baseline probability for sum 2 is dropped. Dropped number caps at Partial."
  },
  {
   "point_id": "K05",
   "point_text": "With four dice the distribution flattens: P(can make 7) = 64.4% and P(can make 2) = 13.2%, only a 4.88x ratio versus 6x with two dice.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L010",
    "L011",
    "L012"
   ],
   "evidence_quote": "Making a 2 ... about 13.2% ... Making a 7 ... about 64.4% ... Probability ratio 4.88",
   "reasoning": "All three figures (13.2%, 64.4%, 4.88) are captured with correct meaning."
  },
  {
   "point_id": "K06",
   "point_text": "Expected rolls to complete a column = length / probability; column 2 needs about 22.73 rolls while column 7 needs about 20.18, so 7 is slightly faster despite being 4x longer.",
   "weight": "Must have",
   "presence": "Partial",
   "loglog_ids": [
    "L014"
   ],
   "evidence_quote": "Expected rolls cluster near 20; long column 7 completes slightly faster than 2",
   "reasoning": "The qualitative finding is retained, but the exact expected values 22.73 and 20.18 are dropped. Dropped numbers make this Partial."
  },
  {
   "point_id": "K07",
   "point_text": "Column combinations matter: {6,7,8} succeeds 92.0% of the time versus 43.8% for {2,3,12}; all 165 three-column combinations were analyzed, with 37 rated excellent (>=85% success) and a median success of 79.6%.",
   "weight": "Must have",
   "presence": "Partial",
   "loglog_ids": [
    "L015",
    "L016"
   ],
   "evidence_quote": "{6,7,8} succeeds 92% per roll; {2,3,12} only 43.8% ... 37 combos rate excellent; median succeeds 79.6%",
   "reasoning": "92%, 43.8%, 37 and 79.6% captured, but the total count of 165 combinations and the >=85% excellent threshold are dropped. Dropped numbers cap at Partial."
  },
  {
   "point_id": "K08",
   "point_text": "\"Clean\" moves are rare: even the best combination {6,7,8} yields only 39.8% clean rolls, and {2,3,12} only 2.3%, so the forced-move rule contaminates good combinations.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L019",
    "L030",
    "L035"
   ],
   "evidence_quote": "Only 39.8% of {6,7,8} rolls are clean; {2,3,12} just 2.3%",
   "reasoning": "Both percentages preserved and the contamination link to forced moves is stated in L030/L035."
  },
  {
   "point_id": "K09",
   "point_text": "Stopping heuristic: keep rolling if (P_success x Q) > (P_bust x U), where Q is expected markers advanced and U is unsaved progress; example on {6,7,8} says roll (1.32 > 0.4) and on {2,3,12} says stop (1.12 > 0.46).",
   "weight": "Must have",
   "presence": "Partial",
   "loglog_ids": [
    "L017",
    "L018"
   ],
   "evidence_quote": "Stopping rule weighs expected gain against bust-weighted unsaved progress ... Roll on {6,7,8} with five steps banked; stop on {2,3,12} with two",
   "reasoning": "The heuristic's conceptual form and the directional decisions survive, but the explicit inequality and the numeric values 1.32/0.4 and 1.12/0.46 are dropped. Partial."
  },
  {
   "point_id": "K10",
   "point_text": "Tournament of 38 strategies across 2,500 head-to-head games each (3.6M total games) found FiftyPercentSurvival the champion at 69.84% win rate, and probabilistic strategies dominate the top rankings.",
   "weight": "Must have",
   "presence": "Partial",
   "loglog_ids": [
    "L021",
    "L022",
    "L024"
   ],
   "evidence_quote": "3.6M-game simulations crown probabilistic, consistent strategies over fast ones ... 38 strategy families ... FiftyPercentSurvival wins 69.84%",
   "reasoning": "38 strategies, 3.6M games and 69.84% all present, but the 2,500 games per head-to-head pairing is dropped. Dropped number makes this Partial."
  },
  {
   "point_id": "K11",
   "point_text": "Consistency beats speed: GreedyUntil1Col is fastest (10.5 turns) but only ranks #11 at 58.90% due to high variance and bust rate, while FiftyPercentSurvival at 11.3 turns wins most.",
   "weight": "Must have",
   "presence": "Partial",
   "loglog_ids": [
    "L023",
    "L024",
    "L025"
   ],
   "evidence_quote": "GreedyUntil1Col fastest at 10.5 turns but busts 7.5 times per game ... Consistency beats raw speed",
   "reasoning": "The core contrast and 10.5-turn speed are present, but the #11 ranking, 58.90% win rate and FiftyPercentSurvival's 11.3 turns are dropped. Partial."
  },
  {
   "point_id": "K12",
   "point_text": "Significant first-player advantage: P1 wins 55.59% of games for a +11.18% edge, larger than chess (~5%) or Go (~7%); GreedyUntil1Col shows extreme bias at +31.24%.",
   "weight": "Must have",
   "presence": "Partial",
   "loglog_ids": [
    "L026"
   ],
   "evidence_quote": "First player wins 55.59%, an 11.18% edge exceeding chess and Go",
   "reasoning": "55.59%, 11.18% and the chess/Go comparison are retained, but the GreedyUntil1Col +31.24% extreme-bias figure is dropped. Partial."
  },
  {
   "point_id": "K13",
   "point_text": "Balance analysis: single-column completion times deviate at most +/-13.6% from 20 rolls, an optimal board one step from current reaches +/-3.09%, and a 20-step board reaches +/-2.17%.",
   "weight": "Must have",
   "presence": "Partial",
   "loglog_ids": [
    "L028",
    "L029"
   ],
   "evidence_quote": "Single-column completion deviates at most 13.6% from 20 rolls ... Adding one step per middle column would quadruple balance precision",
   "reasoning": "The 13.6% deviation and the one-step improvement idea are present, but the explicit +/-3.09% and +/-2.17% figures are dropped. Partial."
  },
  {
   "point_id": "K14",
   "point_text": "Stated caveat: continuation versus switching strategies were not fully analyzed quantitatively and remain an open question for future work.",
   "weight": "Nice to have",
   "presence": "Present",
   "loglog_ids": [
    "L020"
   ],
   "evidence_quote": "Continuing current columns usually beats switching, but author hedges: switching unanalyzed quantitatively",
   "reasoning": "The caveat and its quantitative-unanalyzed status are preserved."
  },
  {
   "point_id": "K15",
   "point_text": "Recommendations: players should use FiftyPercentSurvival and aim for columns 5-9 while avoiding forced activation of 2-3 and 11-12; designers should prioritize playability and use rules to compensate for imbalance, considering handicaps for turn order.",
   "weight": "Must have",
   "presence": "Partial",
   "loglog_ids": [
    "L031",
    "L032"
   ],
   "evidence_quote": "Aim for columns 5-9, avoid edge columns ... designers should favor playability over perfection",
   "reasoning": "The 5-9 target, edge avoidance and playability advice are present, but the explicit FiftyPercentSurvival player recommendation and the turn-order handicap suggestion are not captured. Partial."
  }
 ],
 "metrics": {
  "total_points": 15,
  "must_have_total": 14,
  "must_have_present": 4,
  "must_have_partial": 10,
  "must_have_missing": 0,
  "overall_present": 5,
  "must_recall": 0.6429,
  "overall_recall": 0.6667
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
 "source_id": "03_cant_stop_addicted_to_shindig",
 "labels": [
  {
   "claim_id": "C001",
   "loglog_ids": [
    "L002"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Thesis summary stated first, sets roadmap, repeats no earlier claim ID."
  },
  {
   "claim_id": "C002",
   "loglog_ids": [
    "L003"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Core push-your-luck rules definition, no prior statement."
  },
  {
   "claim_id": "C003",
   "loglog_ids": [
    "L004"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Board geometry setup, new factual content."
  },
  {
   "claim_id": "C004",
   "loglog_ids": [
    "L005"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Forced-move rule definition, new."
  },
  {
   "claim_id": "C005",
   "loglog_ids": [
    "L006"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Concrete forced-move example naming specific columns."
  },
  {
   "claim_id": "C006",
   "loglog_ids": [
    "L007"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Central distribution claim, first full statement."
  },
  {
   "claim_id": "C007",
   "loglog_ids": [
    "L008"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Two-dice baseline percentage, number never trivia."
  },
  {
   "claim_id": "C008",
   "loglog_ids": [
    "L009"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Three-pairings fact, distinct new content."
  },
  {
   "claim_id": "C009",
   "loglog_ids": [
    "L010"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "171/1296 number, never trivia."
  },
  {
   "claim_id": "C010",
   "loglog_ids": [
    "L011"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "834/1296 number with method, never trivia."
  },
  {
   "claim_id": "C011",
   "loglog_ids": [
    "L012"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Ratio interpretation carrying numbers, cannot be trivia."
  },
  {
   "claim_id": "C012",
   "loglog_ids": [
    "L013"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Combination thesis, first statement, new point."
  },
  {
   "claim_id": "C013",
   "loglog_ids": [
    "L014"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Expected-roll figures, numeric, never trivia."
  },
  {
   "claim_id": "C014",
   "loglog_ids": [
    "L015"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Per-roll success percentages, new numbers."
  },
  {
   "claim_id": "C015",
   "loglog_ids": [
    "L016"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Combination stats; only overlaps C014 worst-case 43.8%, adds median and count."
  },
  {
   "claim_id": "C016",
   "loglog_ids": [
    "L017"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Stopping-rule definition, new."
  },
  {
   "claim_id": "C017",
   "loglog_ids": [
    "L018"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Banked-step thresholds, unique numeric content."
  },
  {
   "claim_id": "C018",
   "loglog_ids": [
    "L019"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Clean-roll percentages, distinct metric, never trivia."
  },
  {
   "claim_id": "C019",
   "loglog_ids": [
    "L020"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Hedged switching concession, new content not stated earlier."
  },
  {
   "claim_id": "C020",
   "loglog_ids": [
    "L021"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Simulation headline, first statement of consistency-over-speed."
  },
  {
   "claim_id": "C021",
   "loglog_ids": [
    "L022"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "38 families number, never trivia despite partial support."
  },
  {
   "claim_id": "C022",
   "loglog_ids": [
    "L023"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Greedy speed and bust numbers, unique."
  },
  {
   "claim_id": "C023",
   "loglog_ids": [
    "L024"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "50% survival win rate, unique number."
  },
  {
   "claim_id": "C024",
   "loglog_ids": [
    "L025"
   ],
   "label": "Duplicate",
   "canonical_id": "C020",
   "reasoning": "Restates C020 consistency-over-speed; greedy loss already given in C022."
  },
  {
   "claim_id": "C025",
   "loglog_ids": [
    "L026"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "First-player edge number, unique, never trivia."
  },
  {
   "claim_id": "C026",
   "loglog_ids": [
    "L027"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Balance thesis, first statement of forced-move compensating role."
  },
  {
   "claim_id": "C027",
   "loglog_ids": [
    "L028"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "13.6% deviation bound, new numeric content beyond C013."
  },
  {
   "claim_id": "C028",
   "loglog_ids": [
    "L029"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Counterfactual step adjustment, unique numeric claim."
  },
  {
   "claim_id": "C029",
   "loglog_ids": [
    "L030"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Adds strategy-interest consequence beyond C026 contamination idea."
  },
  {
   "claim_id": "C030",
   "loglog_ids": [
    "L031"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Player and designer advice, first statement of recommendation."
  },
  {
   "claim_id": "C031",
   "loglog_ids": [
    "L032"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Concrete column 5-9 guidance, new specificity beyond C030."
  },
  {
   "claim_id": "C032",
   "loglog_ids": [
    "L033"
   ],
   "label": "Trivia",
   "canonical_id": null,
   "reasoning": "Reproducibility meta-note maps to no analysis point, low value at this length."
  }
 ],
 "metrics": {
  "scored_claims": 32,
  "unique": 30,
  "duplicates": 1,
  "trivia": 1,
  "redundancy_rate": 0.0312,
  "trivia_rate": 0.0312,
  "structured_tokens": 480,
  "tokens_per_unique_claim": 16.0
 },
 "prune_list": [
  "C024 duplicates C020, safe to merge",
  "C032 reproducibility meta-note maps to no scoring point, move to appendix or drop",
  "Cross-links L035-L038 restate C005/C011/C018/C024/C029/C031, safe to trim without claim loss"
 ]
}
```

## Judge F (faithfulness), opencode-go/deepseek-v4.1-flash

```json
{
 "judge": "faithfulness",
 "judge_version": "1.0.0",
 "model": "opencode-go/deepseek-v4.1-flash (opencode) scripted pipeline 2026-09-15",
 "source_id": "03_cant_stop_addicted_to_shindig",
 "claims": [
  {
   "claim_id": "C001",
   "loglog_ids": [
    "0"
   ],
   "claim_text": "Can't Stop analysis shows four-dice odds flatten the distribution, middle columns dominate, probabilistic stopping wins, and forced moves balance design.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "Four-dice probabilities flatten the distribution... Probabilistic strategies dominate... forced-move rule compensates for the mathematical imbalance.",
   "reasoning": "Each summary component matches a conclusion in the source."
  },
  {
   "claim_id": "C002",
   "loglog_ids": [
    "1"
   ],
   "claim_text": "Push-your-luck rules: roll four dice, pair freely, bust loses turn progress.",
   "claim_type": "definition",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "roll four dice, pair them up however you want... if you can't move any of your three active markers, you lose everything you've gained that turn",
   "reasoning": "All three rule elements are stated directly."
  },
  {
   "claim_id": "C003",
   "loglog_ids": [
    "1.1"
   ],
   "claim_text": "Board columns 2 to 12 vary 3 to 13 steps; complete three to win.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "columns numbered 2 through 12... Columns 2 and 12: 3 steps... Column 7: 13 steps. You need to complete three columns to win.",
   "reasoning": "Range and completion condition match source exactly."
  },
  {
   "claim_id": "C004",
   "loglog_ids": [
    "1.2"
   ],
   "claim_text": "Forced-move rule requires taking every legal move from the chosen pairing.",
   "claim_type": "definition",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "you must make ALL legal moves from that pairing, even if you don't want them",
   "reasoning": "Direct restatement of the forced-move rule."
  },
  {
   "claim_id": "C005",
   "loglog_ids": [
    "1.3"
   ],
   "claim_text": "Chasing 7 on {6,7,8} can force an unwanted 2 onto the board.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "you're forced to take BOTH the 2 and the 7, even though column 2 isn't in your plan",
   "reasoning": "Matches the source example precisely."
  },
  {
   "claim_id": "C006",
   "loglog_ids": [
    "2"
   ],
   "claim_text": "Four-dice pairing flattens the probability distribution versus two dice.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "Four-dice probabilities flatten the distribution",
   "reasoning": "Source conclusion states this explicitly."
  },
  {
   "claim_id": "C007",
   "loglog_ids": [
    "2.1"
   ],
   "claim_text": "Two-dice baseline: 7 hits 16.67%, six times more likely than 2.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "sum 7 is the most likely at 16.67%, and it's exactly 6x more likely than sum 2 at 2.78%",
   "reasoning": "Numbers match exactly."
  },
  {
   "claim_id": "C008",
   "loglog_ids": [
    "2.2"
   ],
   "claim_text": "Four dice yield exactly three possible pairings per roll.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "That's it, just three possible pairings.",
   "reasoning": "Count of three pairings is stated in source."
  },
  {
   "claim_id": "C009",
   "loglog_ids": [
    "2.3"
   ],
   "claim_text": "Making a 2 needs two 1s: 171/1296, about 13.2%.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "P(can make a 2) = ... = 171/1296 approx 13.2%",
   "reasoning": "Fraction and percentage match the source."
  },
  {
   "claim_id": "C010",
   "loglog_ids": [
    "2.4"
   ],
   "claim_text": "Making a 7 via inclusion-exclusion: 834/1296, about 64.4%.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "= 834/1296 approx 64.4%",
   "reasoning": "Fraction and percentage match the source."
  },
  {
   "claim_id": "C011",
   "loglog_ids": [
    "2.5"
   ],
   "claim_text": "Probability ratio 4.88 nearly matches length ratio 4.33; designers thought carefully.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "The probability ratio from 2 to 7 is 4.88. The length ratio is 4.33. Pretty close! The game designers were definitely thinking about this.",
   "reasoning": "Both ratios and the inference match the source."
  },
  {
   "claim_id": "C012",
   "loglog_ids": [
    "3"
   ],
   "claim_text": "Column combinations matter more than individual column odds.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "Column combinations matter more than individual columns",
   "reasoning": "Source conclusion states this directly."
  },
  {
   "claim_id": "C013",
   "loglog_ids": [
    "3.1"
   ],
   "claim_text": "Expected rolls cluster near 20; long column 7 completes slightly faster than 2.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "For column 2: 3/0.132 = 22.73 rolls. For column 7: 13/0.644 = 20.18 rolls. Column 7 is slightly faster",
   "reasoning": "Values and comparison match the source."
  },
  {
   "claim_id": "C014",
   "loglog_ids": [
    "3.2"
   ],
   "claim_text": "{6,7,8} succeeds 92% per roll; {2,3,12} only 43.8%.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "{6,7,8}, you have a 92% chance of not busting... {2,3,12}: 568/1296 = 43.8% success rate",
   "reasoning": "Both success rates match the source."
  },
  {
   "claim_id": "C015",
   "loglog_ids": [
    "3.3"
   ],
   "claim_text": "37 combos rate excellent; median succeeds 79.6%, worst collapse to 43.8%.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "37 combinations are 'excellent'... median combination still succeeds 79.6%... worst combinations drop dramatically to just 43.8%",
   "reasoning": "All three numbers match the source."
  },
  {
   "claim_id": "C016",
   "loglog_ids": [
    "4"
   ],
   "claim_text": "Stopping rule weighs expected gain against bust-weighted unsaved progress.",
   "claim_type": "definition",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "Keep rolling if: (P_success x Q) > (P_bust x U)",
   "reasoning": "Describes the source heuristic formula accurately."
  },
  {
   "claim_id": "C017",
   "loglog_ids": [
    "4.1"
   ],
   "claim_text": "Roll on {6,7,8} with five steps banked; stop on {2,3,12} with two.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "On {6,7,8} with 5 unsaved steps... keep rolling. On {2,3,12} with 2 unsaved steps... STOP.",
   "reasoning": "Both step counts and decisions match the source."
  },
  {
   "claim_id": "C018",
   "loglog_ids": [
    "4.2"
   ],
   "claim_text": "Only 39.8% of {6,7,8} rolls are clean; {2,3,12} just 2.3%.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "Only 39.8% of rolls give a clean move on {6,7,8}... For {2,3,12}: Only 2.3% of rolls are clean!",
   "reasoning": "Both percentages match the source."
  },
  {
   "claim_id": "C019",
   "loglog_ids": [
    "4.3"
   ],
   "claim_text": "Continuing current columns usually beats switching, but author hedges: switching unanalyzed quantitatively.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "The mathematics favor continuation in most cases... I haven't fully analyzed this aspect quantitatively.",
   "reasoning": "Hedge is preserved exactly as in source."
  },
  {
   "claim_id": "C020",
   "loglog_ids": [
    "5"
   ],
   "claim_text": "3.6M-game simulations crown probabilistic, consistent strategies over fast ones.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "3.6 million total games... Probabilistic strategies dominate the top rankings... consistency beats raw speed",
   "reasoning": "Combines source findings faithfully."
  },
  {
   "claim_id": "C021",
   "loglog_ids": [
    "5.1"
   ],
   "claim_text": "38 strategy families tested across single-player and head-to-head simulations.",
   "claim_type": "number_or_date",
   "verdict": "Partially supported",
   "severity": "Minor",
   "evidence_quote": "I tested 38 strategies across 14 different strategic families",
   "reasoning": "Number 38 is right for strategies, but source reports 14 families, not 38, mislabeling the count."
  },
  {
   "claim_id": "C022",
   "loglog_ids": [
    "5.2"
   ],
   "claim_text": "GreedyUntil1Col fastest at 10.5 turns but busts 7.5 times per game.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "GreedyUntil1Col is fastest (10.5 turns)... bust rate (7.5 per game)",
   "reasoning": "Both figures match the source."
  },
  {
   "claim_id": "C023",
   "loglog_ids": [
    "5.3"
   ],
   "claim_text": "FiftyPercentSurvival wins 69.84% by stopping below 50% cumulative survival.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "FiftyPercentSurvival dominates with 69.84% overall win rate... Roll until cumulative survival probability drops below 50%",
   "reasoning": "Win rate and rule match the source."
  },
  {
   "claim_id": "C024",
   "loglog_ids": [
    "5.4"
   ],
   "claim_text": "Consistency beats raw speed; pure greedy loses nearly everything.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "Consistency > Speed... The pure Greedy strategy (never stop voluntarily) lost essentially every game.",
   "reasoning": "Both claims are stated in the source."
  },
  {
   "claim_id": "C025",
   "loglog_ids": [
    "5.5"
   ],
   "claim_text": "First player wins 55.59%, an 11.18% edge exceeding chess and Go.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "Player 1 wins 55.59%... First-player advantage: +11.18%... larger than chess (~5%) or Go (~7%)",
   "reasoning": "All figures and comparison match the source."
  },
  {
   "claim_id": "C026",
   "loglog_ids": [
    "6"
   ],
   "claim_text": "Board is nearly balanced singly; forced moves compensate combination imbalance.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "The deviations are +-13.6% at most... forced-move rule compensates for the mathematical imbalance",
   "reasoning": "Both components are stated in the source."
  },
  {
   "claim_id": "C027",
   "loglog_ids": [
    "6.1"
   ],
   "claim_text": "Single-column completion deviates at most 13.6% from 20 rolls.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "The deviations are +-13.6% at most.",
   "reasoning": "Deviation bound matches the source."
  },
  {
   "claim_id": "C028",
   "loglog_ids": [
    "6.2"
   ],
   "claim_text": "Adding one step per middle column would quadruple balance precision.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "Optimal board (+-1 step from current)... 4x more balanced with just +1 step!",
   "reasoning": "The 4x improvement and +1 step match the source."
  },
  {
   "claim_id": "C029",
   "loglog_ids": [
    "6.3"
   ],
   "claim_text": "Forced moves contaminate strong combos, keeping strategy choices interesting.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "add rules that turn that imbalance into interesting strategic choices",
   "reasoning": "Source describes forced moves as contamination and a balancing mechanism."
  },
  {
   "claim_id": "C030",
   "loglog_ids": [
    "7"
   ],
   "claim_text": "Play middle columns consistently; designers should favor playability over perfection.",
   "claim_type": "recommendation",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "Aim for columns 5-9... prioritize consistency over aggressive play. For game designers: Prioritize playability over mathematical perfection",
   "reasoning": "Both recommendations restate the source."
  },
  {
   "claim_id": "C031",
   "loglog_ids": [
    "7.1"
   ],
   "claim_text": "Aim for columns 5-9, avoid edge columns, prioritize consistency over aggression.",
   "claim_type": "recommendation",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "Aim for columns 5-9, avoid forcing activation of columns 2-3 and 11-12, and prioritize consistency over aggressive play",
   "reasoning": "Advice matches the source exactly."
  },
  {
   "claim_id": "C032",
   "loglog_ids": [
    "7.2"
   ],
   "claim_text": "All code, simulations, and datasets are published for reuse.",
   "claim_type": "meta",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "All analysis code and simulation results are available",
   "reasoning": "Source states code and results are available."
  }
 ],
 "metrics": {
  "total_claims": 32,
  "supported": 31,
  "partially_supported": 1,
  "unverifiable": 0,
  "contradicted": 0,
  "critical_errors": 0,
  "faithfulness_precision": 0.9688
 },
 "fail_list": [
  "C021"
 ]
}
```

## Judge Cov (coverage), opencode-go/deepseek-v4.1-flash

```json
{
 "judge": "coverage",
 "judge_version": "1.0.0",
 "model": "opencode-go/deepseek-v4.1-flash (opencode) scripted pipeline 2026-09-15",
 "source_id": "03_cant_stop_addicted_to_shindig",
 "key_points": [
  {
   "point_id": "K01",
   "point_text": "Central thesis: Can't Stop is a masterclass in practical game design, where imperfect mathematical balance is acceptable and rules are used to compensate for it.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L002",
    "L027",
    "L030",
    "L031"
   ],
   "evidence_quote": "forced moves compensate combination imbalance ... designers should favor playability over perfection",
   "reasoning": "L002 summary states forced moves balance design; L030 notes forced moves compensate; L031 frames playability over perfection, matching the thesis."
  },
  {
   "point_id": "K02",
   "point_text": "Game rules: roll four dice, pair them to move markers on columns 2 through 12, need three completed columns to win; column lengths are 3,5,7,9,11,13,11,9,7,5,3.",
   "weight": "Must have",
   "presence": "Partial",
   "loglog_ids": [
    "L003",
    "L004"
   ],
   "evidence_quote": "Board columns 2 to 12 vary 3 to 13 steps; complete three to win",
   "reasoning": "Rules captured but exact column lengths (3,5,7,9,11,13,11,9,7,5,3) are not enumerated, only the 3-to-13 range. Dropped numbers make this Partial."
  },
  {
   "point_id": "K03",
   "point_text": "Forced-move rule: if a chosen pairing creates any valid move you must take all legal moves from that pairing, even onto unwanted columns; you cannot cherry-pick.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L005",
    "L006"
   ],
   "evidence_quote": "Forced-move rule requires taking every legal move from the chosen pairing",
   "reasoning": "L005 states the rule directly; L006 gives the unwanted-move example, preserving meaning."
  },
  {
   "point_id": "K04",
   "point_text": "Two-dice baseline: sum 7 is most likely at 16.67%, exactly 6 times more likely than sum 2 at 2.78%.",
   "weight": "Must have",
   "presence": "Partial",
   "loglog_ids": [
    "L008"
   ],
   "evidence_quote": "Two-dice baseline: 7 hits 16.67%, six times more likely than 2",
   "reasoning": "16.67% and the 6x ratio are present, but the 2.78% baseline probability for sum 2 is dropped. Dropped number caps at Partial."
  },
  {
   "point_id": "K05",
   "point_text": "With four dice the distribution flattens: P(can make 7) = 64.4% and P(can make 2) = 13.2%, only a 4.88x ratio versus 6x with two dice.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L010",
    "L011",
    "L012"
   ],
   "evidence_quote": "Making a 2 ... about 13.2% ... Making a 7 ... about 64.4% ... Probability ratio 4.88",
   "reasoning": "All three figures (13.2%, 64.4%, 4.88) are captured with correct meaning."
  },
  {
   "point_id": "K06",
   "point_text": "Expected rolls to complete a column = length / probability; column 2 needs about 22.73 rolls while column 7 needs about 20.18, so 7 is slightly faster despite being 4x longer.",
   "weight": "Must have",
   "presence": "Partial",
   "loglog_ids": [
    "L014"
   ],
   "evidence_quote": "Expected rolls cluster near 20; long column 7 completes slightly faster than 2",
   "reasoning": "The qualitative finding is retained, but the exact expected values 22.73 and 20.18 are dropped. Dropped numbers make this Partial."
  },
  {
   "point_id": "K07",
   "point_text": "Column combinations matter: {6,7,8} succeeds 92.0% of the time versus 43.8% for {2,3,12}; all 165 three-column combinations were analyzed, with 37 rated excellent (>=85% success) and a median success of 79.6%.",
   "weight": "Must have",
   "presence": "Partial",
   "loglog_ids": [
    "L015",
    "L016"
   ],
   "evidence_quote": "{6,7,8} succeeds 92% per roll; {2,3,12} only 43.8% ... 37 combos rate excellent; median succeeds 79.6%",
   "reasoning": "92%, 43.8%, 37 and 79.6% captured, but the total count of 165 combinations and the >=85% excellent threshold are dropped. Dropped numbers cap at Partial."
  },
  {
   "point_id": "K08",
   "point_text": "\"Clean\" moves are rare: even the best combination {6,7,8} yields only 39.8% clean rolls, and {2,3,12} only 2.3%, so the forced-move rule contaminates good combinations.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L019",
    "L030",
    "L035"
   ],
   "evidence_quote": "Only 39.8% of {6,7,8} rolls are clean; {2,3,12} just 2.3%",
   "reasoning": "Both percentages preserved and the contamination link to forced moves is stated in L030/L035."
  },
  {
   "point_id": "K09",
   "point_text": "Stopping heuristic: keep rolling if (P_success x Q) > (P_bust x U), where Q is expected markers advanced and U is unsaved progress; example on {6,7,8} says roll (1.32 > 0.4) and on {2,3,12} says stop (1.12 > 0.46).",
   "weight": "Must have",
   "presence": "Partial",
   "loglog_ids": [
    "L017",
    "L018"
   ],
   "evidence_quote": "Stopping rule weighs expected gain against bust-weighted unsaved progress ... Roll on {6,7,8} with five steps banked; stop on {2,3,12} with two",
   "reasoning": "The heuristic's conceptual form and the directional decisions survive, but the explicit inequality and the numeric values 1.32/0.4 and 1.12/0.46 are dropped. Partial."
  },
  {
   "point_id": "K10",
   "point_text": "Tournament of 38 strategies across 2,500 head-to-head games each (3.6M total games) found FiftyPercentSurvival the champion at 69.84% win rate, and probabilistic strategies dominate the top rankings.",
   "weight": "Must have",
   "presence": "Partial",
   "loglog_ids": [
    "L021",
    "L022",
    "L024"
   ],
   "evidence_quote": "3.6M-game simulations crown probabilistic, consistent strategies over fast ones ... 38 strategy families ... FiftyPercentSurvival wins 69.84%",
   "reasoning": "38 strategies, 3.6M games and 69.84% all present, but the 2,500 games per head-to-head pairing is dropped. Dropped number makes this Partial."
  },
  {
   "point_id": "K11",
   "point_text": "Consistency beats speed: GreedyUntil1Col is fastest (10.5 turns) but only ranks #11 at 58.90% due to high variance and bust rate, while FiftyPercentSurvival at 11.3 turns wins most.",
   "weight": "Must have",
   "presence": "Partial",
   "loglog_ids": [
    "L023",
    "L024",
    "L025"
   ],
   "evidence_quote": "GreedyUntil1Col fastest at 10.5 turns but busts 7.5 times per game ... Consistency beats raw speed",
   "reasoning": "The core contrast and 10.5-turn speed are present, but the #11 ranking, 58.90% win rate and FiftyPercentSurvival's 11.3 turns are dropped. Partial."
  },
  {
   "point_id": "K12",
   "point_text": "Significant first-player advantage: P1 wins 55.59% of games for a +11.18% edge, larger than chess (~5%) or Go (~7%); GreedyUntil1Col shows extreme bias at +31.24%.",
   "weight": "Must have",
   "presence": "Partial",
   "loglog_ids": [
    "L026"
   ],
   "evidence_quote": "First player wins 55.59%, an 11.18% edge exceeding chess and Go",
   "reasoning": "55.59%, 11.18% and the chess/Go comparison are retained, but the GreedyUntil1Col +31.24% extreme-bias figure is dropped. Partial."
  },
  {
   "point_id": "K13",
   "point_text": "Balance analysis: single-column completion times deviate at most +/-13.6% from 20 rolls, an optimal board one step from current reaches +/-3.09%, and a 20-step board reaches +/-2.17%.",
   "weight": "Must have",
   "presence": "Partial",
   "loglog_ids": [
    "L028",
    "L029"
   ],
   "evidence_quote": "Single-column completion deviates at most 13.6% from 20 rolls ... Adding one step per middle column would quadruple balance precision",
   "reasoning": "The 13.6% deviation and the one-step improvement idea are present, but the explicit +/-3.09% and +/-2.17% figures are dropped. Partial."
  },
  {
   "point_id": "K14",
   "point_text": "Stated caveat: continuation versus switching strategies were not fully analyzed quantitatively and remain an open question for future work.",
   "weight": "Nice to have",
   "presence": "Present",
   "loglog_ids": [
    "L020"
   ],
   "evidence_quote": "Continuing current columns usually beats switching, but author hedges: switching unanalyzed quantitatively",
   "reasoning": "The caveat and its quantitative-unanalyzed status are preserved."
  },
  {
   "point_id": "K15",
   "point_text": "Recommendations: players should use FiftyPercentSurvival and aim for columns 5-9 while avoiding forced activation of 2-3 and 11-12; designers should prioritize playability and use rules to compensate for imbalance, considering handicaps for turn order.",
   "weight": "Must have",
   "presence": "Partial",
   "loglog_ids": [
    "L031",
    "L032"
   ],
   "evidence_quote": "Aim for columns 5-9, avoid edge columns ... designers should favor playability over perfection",
   "reasoning": "The 5-9 target, edge avoidance and playability advice are present, but the explicit FiftyPercentSurvival player recommendation and the turn-order handicap suggestion are not captured. Partial."
  }
 ],
 "metrics": {
  "total_points": 15,
  "must_have_total": 14,
  "must_have_present": 4,
  "must_have_partial": 10,
  "must_have_missing": 0,
  "overall_present": 5,
  "must_recall": 0.6429,
  "overall_recall": 0.6667
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
 "source_id": "03_cant_stop_addicted_to_shindig",
 "labels": [
  {
   "claim_id": "C001",
   "loglog_ids": [
    "L002"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Thesis summary stated first, sets roadmap, repeats no earlier claim ID."
  },
  {
   "claim_id": "C002",
   "loglog_ids": [
    "L003"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Core push-your-luck rules definition, no prior statement."
  },
  {
   "claim_id": "C003",
   "loglog_ids": [
    "L004"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Board geometry setup, new factual content."
  },
  {
   "claim_id": "C004",
   "loglog_ids": [
    "L005"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Forced-move rule definition, new."
  },
  {
   "claim_id": "C005",
   "loglog_ids": [
    "L006"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Concrete forced-move example naming specific columns."
  },
  {
   "claim_id": "C006",
   "loglog_ids": [
    "L007"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Central distribution claim, first full statement."
  },
  {
   "claim_id": "C007",
   "loglog_ids": [
    "L008"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Two-dice baseline percentage, number never trivia."
  },
  {
   "claim_id": "C008",
   "loglog_ids": [
    "L009"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Three-pairings fact, distinct new content."
  },
  {
   "claim_id": "C009",
   "loglog_ids": [
    "L010"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "171/1296 number, never trivia."
  },
  {
   "claim_id": "C010",
   "loglog_ids": [
    "L011"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "834/1296 number with method, never trivia."
  },
  {
   "claim_id": "C011",
   "loglog_ids": [
    "L012"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Ratio interpretation carrying numbers, cannot be trivia."
  },
  {
   "claim_id": "C012",
   "loglog_ids": [
    "L013"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Combination thesis, first statement, new point."
  },
  {
   "claim_id": "C013",
   "loglog_ids": [
    "L014"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Expected-roll figures, numeric, never trivia."
  },
  {
   "claim_id": "C014",
   "loglog_ids": [
    "L015"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Per-roll success percentages, new numbers."
  },
  {
   "claim_id": "C015",
   "loglog_ids": [
    "L016"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Combination stats; only overlaps C014 worst-case 43.8%, adds median and count."
  },
  {
   "claim_id": "C016",
   "loglog_ids": [
    "L017"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Stopping-rule definition, new."
  },
  {
   "claim_id": "C017",
   "loglog_ids": [
    "L018"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Banked-step thresholds, unique numeric content."
  },
  {
   "claim_id": "C018",
   "loglog_ids": [
    "L019"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Clean-roll percentages, distinct metric, never trivia."
  },
  {
   "claim_id": "C019",
   "loglog_ids": [
    "L020"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Hedged switching concession, new content not stated earlier."
  },
  {
   "claim_id": "C020",
   "loglog_ids": [
    "L021"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Simulation headline, first statement of consistency-over-speed."
  },
  {
   "claim_id": "C021",
   "loglog_ids": [
    "L022"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "38 families number, never trivia despite partial support."
  },
  {
   "claim_id": "C022",
   "loglog_ids": [
    "L023"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Greedy speed and bust numbers, unique."
  },
  {
   "claim_id": "C023",
   "loglog_ids": [
    "L024"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "50% survival win rate, unique number."
  },
  {
   "claim_id": "C024",
   "loglog_ids": [
    "L025"
   ],
   "label": "Duplicate",
   "canonical_id": "C020",
   "reasoning": "Restates C020 consistency-over-speed; greedy loss already given in C022."
  },
  {
   "claim_id": "C025",
   "loglog_ids": [
    "L026"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "First-player edge number, unique, never trivia."
  },
  {
   "claim_id": "C026",
   "loglog_ids": [
    "L027"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Balance thesis, first statement of forced-move compensating role."
  },
  {
   "claim_id": "C027",
   "loglog_ids": [
    "L028"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "13.6% deviation bound, new numeric content beyond C013."
  },
  {
   "claim_id": "C028",
   "loglog_ids": [
    "L029"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Counterfactual step adjustment, unique numeric claim."
  },
  {
   "claim_id": "C029",
   "loglog_ids": [
    "L030"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Adds strategy-interest consequence beyond C026 contamination idea."
  },
  {
   "claim_id": "C030",
   "loglog_ids": [
    "L031"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Player and designer advice, first statement of recommendation."
  },
  {
   "claim_id": "C031",
   "loglog_ids": [
    "L032"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Concrete column 5-9 guidance, new specificity beyond C030."
  },
  {
   "claim_id": "C032",
   "loglog_ids": [
    "L033"
   ],
   "label": "Trivia",
   "canonical_id": null,
   "reasoning": "Reproducibility meta-note maps to no analysis point, low value at this length."
  }
 ],
 "metrics": {
  "scored_claims": 32,
  "unique": 30,
  "duplicates": 1,
  "trivia": 1,
  "redundancy_rate": 0.0312,
  "trivia_rate": 0.0312,
  "structured_tokens": 480,
  "tokens_per_unique_claim": 16.0
 },
 "prune_list": [
  "C024 duplicates C020, safe to merge",
  "C032 reproducibility meta-note maps to no scoring point, move to appendix or drop",
  "Cross-links L035-L038 restate C005/C011/C018/C024/C029/C031, safe to trim without claim loss"
 ]
}
```

## Judge Top (overall), opencode-go/deepseek-v4.1-flash

```json
{
 "judge": "overall",
 "judge_version": "1.0.0",
 "model": "opencode-go/deepseek-v4.1-flash, 2026-09-15",
 "source_id": "point-hierarchy",
 "inputs": {
  "faithfulness_precision": 0.9688,
  "critical_errors": 0,
  "must_recall": 0.6429,
  "overall_recall": 0.6667,
  "redundancy_rate": 0.0312,
  "trivia_rate": 0.0312
 },
 "weights_used": {
  "faithfulness_precision": 0.4,
  "coverage_must_recall": 0.4,
  "redundancy_penalty": 0.2
 },
 "computation": "weighted score = 0.4 * faithfulness_precision + 0.4 * must_recall - 0.2 * redundancy_rate = 0.4*0.9688 + 0.4*0.6429 - 0.2*0.0312 = 0.38752 + 0.25716 - 0.00624 = 0.63844",
 "weighted_score": 0.63844,
 "verdict": "Fail",
 "tradeoff_note": "The length budget is not the problem: redundancy is only 0.0312 against a 0.15 max, so concision is comfortably passing. The sample fails because must-have recall is 0.6429, far under the 0.9 gate, and concision cannot rescue a coverage fail.",
 "fix_list": [
  "Recover the 10 Partial must-haves by restoring dropped numbers, not prose: K02 column lengths (3,5,7,9,11,13,11,9,7,5,3), K04 sum-2 baseline 2.78%, K06 expected rolls 22.73 vs 20.18, K07 the 165 total combinations and >=85% excellent threshold, K09 the inequality and values 1.32/0.4 vs 1.12/0.46.",
  "Finish the remaining dropped figures on K10 (2,500 games per head-to-head), K11 (#11 rank, 58.90%, 11.3 turns), K12 (GreedyUntil1Col +31.24%), K13 (+/-3.09% and +/-2.17%), and K15 (explicit FiftyPercentSurvival player pick and turn-order handicap).",
  "Correct C021 to say 14 strategic families tested, not 38 families, to clear the sole Partially supported claim (0.9688 -> 1.0 faithfulness).",
  "Optionally apply the prune list (merge C024 into C020, trim cross-links L035-L038, move C032 to appendix) after coverage numbers are restored."
 ],
 "reasoning": "Gate order per policy. Hard gate 1: critical_errors = 0, equals critical_contradicted_max = 0, pass. Hard gate 2: must_recall = 0.6429 versus must_recall_min = 0.9, FAIL by 0.2571. Hard gate 3: faithfulness_precision = 0.9688 versus min 0.95, pass. Redundancy = 0.0312 versus max 0.15, pass, so the length budget is healthy and not a factor. Because a hard gate is missed, the sample is a Fail and the weighted score is computed only for audit, not to overturn the gate: 0.38752 + 0.25716 - 0.00624 = 0.63844. The coverage judge marked 10 of 14 must-haves (K02, K04, K06, K07, K09, K10, K11, K12, K13, K15) as Partial, and every one of those Partial verdicts traces to a dropped exact number or a dropped explicit recommendation rather than to a missing concept. K02 lost the enumeration 3,5,7,9,11,13,11,9,7,5,3 (only the 3-to-13 range survives); K04 kept 16.67% and the 6x ratio but dropped 2.78%; K06 kept the qualitative finding but dropped 22.73 and 20.18; K07 kept 92%/43.8%/37/79.6% but dropped 165 combinations and the >=85% excellent threshold; K09 kept the directional decisions but dropped the inequality and the 1.32/0.4 and 1.12/0.46 values; K10 dropped 2,500 games per pairing; K11 dropped the #11 rank, 58.90% and 11.3 turns; K12 dropped GreedyUntil1Col +31.24%; K13 dropped +/-3.09% and +/-2.17%; K15 dropped the explicit FiftyPercentSurvival player recommendation and the turn-order handicap. Only 4 must-haves are fully Present, giving 0.6429. Faithfulness is effectively clean: 31 supported, 1 Partial (C021), 0 contradicted, 0 critical, and C021 is a labeling slip (38 strategies justified, 14 families correct) rather than a fabrication. Borderline does not apply because the failure is a hard gate, not a numeric pass with a Partial/Unverifiable claim on a Must-have. Concision is not implicated: redundancy 0.0312 and trivia 0.0312 are well inside budget, and the prune list (C024 duplicate of C020, C032 meta-note, L035-L038 cross-links) would trim tokens without touching the recall deficit. The dominant root cause is summarization that preserves findings while discarding the quantified detail the point hierarchy grades on; restoring those numbers is the single highest-leverage path from 0.6429 back over 0.9."
}
```
