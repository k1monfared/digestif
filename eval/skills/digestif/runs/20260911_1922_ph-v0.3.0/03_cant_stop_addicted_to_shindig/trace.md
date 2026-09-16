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
   "claim_text": "Can't Stop analysis: four dice flatten odds, middle columns dominate, consistent probabilistic strategies win, design favors playability.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Four-dice probabilities flatten the distribution ... Probabilistic strategies dominate ... Perfect balance isn't necessary",
   "reasoning": "All summary strands (flattened odds, middle-column dominance, probabilistic winners, playability) appear in source conclusion."
  },
  {
   "claim_id": "C002",
   "loglog_ids": [
    "1"
   ],
   "claim_text": "Roll four dice, pair freely, advance three active markers; bust loses the turn's progress.",
   "claim_type": "definition",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "roll four dice, pair them up however you want ... if you can't move any of your three active markers, you lose everything you've gained that turn",
   "reasoning": "Source states exactly this rule set."
  },
  {
   "claim_id": "C003",
   "loglog_ids": [
    "1.1"
   ],
   "claim_text": "Columns 2-12 have lengths 3-5-7-9-11-13-11-9-7-5-3; complete three columns to win.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "2 and 12: 3 steps ... 7: 13 steps. You need to complete three columns to win",
   "reasoning": "Sequence matches the source column lengths and win condition."
  },
  {
   "claim_id": "C004",
   "loglog_ids": [
    "1.2"
   ],
   "claim_text": "Forced-move rule: chosen pairing forces ALL its legal moves, even unwanted ones.",
   "claim_type": "definition",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "you must take all available moves ... you must make ALL legal moves from that pairing, even if you don't want them",
   "reasoning": "Direct restatement of the forced-move rule."
  },
  {
   "claim_id": "C005",
   "loglog_ids": [
    "1.3"
   ],
   "claim_text": "(1,1,3,4) as 2+7 on {6,7,8} forces taking both 2 and 7.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "you roll (1,1,3,4) ... pairing (1,1)+(3,4) = 2+7 ... forced to take BOTH the 2 and the 7",
   "reasoning": "Source example matches numbers and forced outcome."
  },
  {
   "claim_id": "C006",
   "loglog_ids": [
    "2"
   ],
   "claim_text": "Two-dice baseline peaks at 7 with 16.67%, exactly 6x likelier than 2 at 2.78%.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Sum 7 is the most likely at 16.67%, and it's exactly 6× more likely than sum 2 at 2.78%",
   "reasoning": "Peak, values, and 6x ratio all match source exactly."
  },
  {
   "claim_id": "C007",
   "loglog_ids": [
    "2.1"
   ],
   "claim_text": "Sums 2-12 have 1-2-3-4-5-6-5-4-3-2-1 ways of 36; 1 way versus 6 ordered ways.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "For sum 2, there's only one way ... sum 7 ... order matters, so that's 6 ways total out of 36",
   "reasoning": "Way counts mirror the source table and proof."
  },
  {
   "claim_id": "C008",
   "loglog_ids": [
    "2.2"
   ],
   "claim_text": "Column 7 is only about 4.3x longer (13/3) than column 2, not 6x.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "it's only 13/3 ≈ 4.3× longer",
   "reasoning": "Source states the 4.3x figure via 13/3."
  },
  {
   "claim_id": "C009",
   "loglog_ids": [
    "3"
   ],
   "claim_text": "Four-dice pairing offers three pairings and sharply flattens the distribution.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "That's it, just three possible pairings ... Did the distribution get flatter?",
   "reasoning": "Source confirms three pairings and a flatter distribution."
  },
  {
   "claim_id": "C010",
   "loglog_ids": [
    "3.1"
   ],
   "claim_text": "P(can make 2) = 171/1296 approx 13.2%, up from two-dice 2.78%.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "P(can make a 2) = 1 - 625/1296 - 500/1296 = 171/1296 ≈ 13.2%",
   "reasoning": "Fraction and percentage match source."
  },
  {
   "claim_id": "C011",
   "loglog_ids": [
    "3.2"
   ],
   "claim_text": "P(can make 7) = 834/1296 approx 64.4% via inclusion-exclusion; overlaps 24/1296, triple 0.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "P(A cap B) = ... 24/1296 ... P(A cap B cap C) = 0 ... P(can make a 7) = 834/1296 ≈ 64.4%",
   "reasoning": "All four numbers match source inclusion-exclusion result."
  },
  {
   "claim_id": "C012",
   "loglog_ids": [
    "3.3"
   ],
   "claim_text": "Full range 13.2% to 64.4%; probability ratio 4.88 nearly matches length ratio 4.33.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "The probability ratio from 2 to 7 is 4.88. The length ratio is 4.33",
   "reasoning": "Both ratios and endpoints match source table."
  },
  {
   "claim_id": "C013",
   "loglog_ids": [
    "4"
   ],
   "claim_text": "Three-column combination choice dominates single-column odds.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "column combination choice dominates individual column balance",
   "reasoning": "Source states combination choice dominates individual columns."
  },
  {
   "claim_id": "C014",
   "loglog_ids": [
    "4.1"
   ],
   "claim_text": "Expected rolls L/P: column 2 needs 22.73, column 7 needs 20.18 rolls.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "For column 2: 3/0.132 = 22.73 rolls. For column 7: 13/0.644 = 20.18 rolls",
   "reasoning": "Expected-roll values match source table."
  },
  {
   "claim_id": "C015",
   "loglog_ids": [
    "4.2"
   ],
   "claim_text": "{6,7,8} succeeds 1193/1296 = 92.0% with Q 1.43 markers per roll.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "1193/1296 = 92.0% success rate ... {6,7,8} | 92.0% ... 1.43",
   "reasoning": "Success fraction and Q value match source."
  },
  {
   "claim_id": "C016",
   "loglog_ids": [
    "4.3"
   ],
   "claim_text": "{2,3,12} succeeds only 568/1296 = 43.8% with Q 1.05; bust likelier.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "568/1296 = 43.8% success rate ... {2,3,12} | 43.8% | 56.2% ... 1.05",
   "reasoning": "Success, bust, and Q figures match source."
  },
  {
   "claim_id": "C017",
   "loglog_ids": [
    "4.4"
   ],
   "claim_text": "All 165 combos ranked; 37 excellent at 85%+, median 79.6%, worst 43.8%.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "37 combinations are \"excellent\" (≥85% success rate) ... median combination still succeeds 79.6% ... worst ... 43.8%",
   "reasoning": "Counts and percentages match source distribution summary."
  },
  {
   "claim_id": "C018",
   "loglog_ids": [
    "4.5"
   ],
   "claim_text": "Clean moves only: 39.8% for {6,7,8} and 2.3% for {2,3,12}.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "{6,7,8} only has 39.8% clean moves ... For {2,3,12}: Only 2.3% of rolls are clean",
   "reasoning": "Both clean-move percentages match source."
  },
  {
   "claim_id": "C019",
   "loglog_ids": [
    "5"
   ],
   "claim_text": "Keep rolling while expected gain exceeds expected loss.",
   "claim_type": "recommendation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Keep rolling if: (P_success × Q) > (P_bust × U)",
   "reasoning": "Source states the same expected-gain heuristic."
  },
  {
   "claim_id": "C020",
   "loglog_ids": [
    "5.1"
   ],
   "claim_text": "Rule: continue if (P_success x Q) > (P_bust x U); {6,7,8} gives 1.32 > 0.4.",
   "claim_type": "recommendation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "0.08 × 5 = 0.4 steps ... 0.92 × 1.43 = 1.32 steps ... 1.32 > 0.4",
   "reasoning": "Formula and worked values match source."
  },
  {
   "claim_id": "C021",
   "loglog_ids": [
    "5.2"
   ],
   "claim_text": "{2,3,12} with 2 steps gives 1.12 > 0.46 loss, so stop.",
   "claim_type": "recommendation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Risk: 0.562 × 2 = 1.12 steps ... Expected gain: 0.438 × 1.05 = 0.46 steps ... you should STOP",
   "reasoning": "Source computes the same figures and conclusion."
  },
  {
   "claim_id": "C022",
   "loglog_ids": [
    "5.3"
   ],
   "claim_text": "Continuation usually beats switching, but full quantitative comparison remains open future work.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "The mathematics favor continuation in most cases ... I haven't fully analyzed this aspect quantitatively ... open question for future work",
   "reasoning": "Mirrors source continuation claim and open-question hedge."
  },
  {
   "claim_id": "C023",
   "loglog_ids": [
    "6"
   ],
   "claim_text": "Tournament of 38 strategies across 14 families over 3.6M games crowns FiftyPercentSurvival.",
   "claim_type": "meta",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "I implemented 38 different strategies ... 14 different strategic families ... 3.6 million total games",
   "reasoning": "Strategy count, family count, and game total match source."
  },
  {
   "claim_id": "C024",
   "loglog_ids": [
    "6.1"
   ],
   "claim_text": "Scale: 1,000 trials per strategy, 2,500 games per matchup, 3.6M games total.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "1,000 single-player trials per strategy, 2,500 head-to-head games per matchup, 3.6 million total games",
   "reasoning": "All three simulation scale figures match source."
  },
  {
   "claim_id": "C025",
   "loglog_ids": [
    "6.2"
   ],
   "claim_text": "Fastest GreedyUntil1Col 10.5 turns (median 9, sd 5.73, 7.50 busts); top 15 span 10.5-12.8.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "GreedyUntil1Col | 10.5 | 9 | 5.73 | 7.50 ... The top 15 all complete games in 10.5-12.8 turns",
   "reasoning": "Means, median, std, busts, and span all match source."
  },
  {
   "claim_id": "C026",
   "loglog_ids": [
    "6.3"
   ],
   "claim_text": "Champion FiftyPercentSurvival 69.84% (132,696/190,000); Heuristic(1.5) 66.46% second.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "FiftyPercentSurvival | 69.84% | 132,696/190,000 ... Heuristic(1.5) | 66.46%",
   "reasoning": "Win share and runner-up value match source table."
  },
  {
   "claim_id": "C027",
   "loglog_ids": [
    "6.4"
   ],
   "claim_text": "Champion stops when cumulative survival drops below 50%: n = log(0.5)/log(P_success).",
   "claim_type": "definition",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Roll until cumulative survival probability drops below 50%, calculated as n = log(0.5) / log(P_success)",
   "reasoning": "Formula and threshold match source exactly."
  },
  {
   "claim_id": "C028",
   "loglog_ids": [
    "6.5"
   ],
   "claim_text": "Paradox: GreedyUntil1Col #1 speed but #11 at 58.90%; consistency beats speed.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "GreedyUntil1Col | #1 | 10.5 | #11 | 58.90% ... consistency beats raw speed",
   "reasoning": "Ranks, win rate, and lesson all match source."
  },
  {
   "claim_id": "C029",
   "loglog_ids": [
    "6.6"
   ],
   "claim_text": "First-player advantage +11.18% overall (P1 wins 55.59%); GreedyUntil1Col bias +31.24%.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "First-player advantage: +11.18% ... Player 1 win rate: 55.59% ... GreedyUntil1Col | +31.24%",
   "reasoning": "All three advantage figures match source."
  },
  {
   "claim_id": "C030",
   "loglog_ids": [
    "6.7"
   ],
   "claim_text": "Opponent-aware tweaks did not help; web game plus full code and data released.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Being \"opponent aware\" didn't help ... I've implemented a fully interactive web version ... All analysis code and simulation results are available",
   "reasoning": "Source confirms opponent-aware failure and public web game, code, and data."
  },
  {
   "claim_id": "C031",
   "loglog_ids": [
    "7"
   ],
   "claim_text": "Board fits 1980 constraints; forced-move rule compensates residual imbalance.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "The current design is excellent for 1980. ... rules and mechanics compensate ... that compensating rule is the forced-move rule",
   "reasoning": "SOURCE states design is excellent for 1980 and forced-move rule compensates the imbalance."
  },
  {
   "claim_id": "C032",
   "loglog_ids": [
    "7.1"
   ],
   "claim_text": "Single-column deviations stay within +/-13.6% given integer lengths.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "The deviations are ±13.6% at most. That's pretty good given that lengths must be integers!",
   "reasoning": "Number and qualifier match SOURCE exactly."
  },
  {
   "claim_id": "C033",
   "loglog_ids": [
    "7.2"
   ],
   "claim_text": "Perfect balance needs 171 vs 834 steps, about an 8-hour game.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Column 2/12: 171 steps ... Column 7: 834 steps. Game duration: ~8 hours.",
   "reasoning": "Step counts and duration match SOURCE."
  },
  {
   "claim_id": "C034",
   "loglog_ids": [
    "7.3"
   ],
   "claim_text": "Optimal +-1-step board [3,5,8,10,12,14,12,10,8,5,3] cuts deviation to +/-3.09%, 4x better.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Max deviation: ±3.09% ... Lengths: [3, 5, 8, 10, 12, 14, 12, 10, 8, 5, 3] ... 4× more balanced with just +1 step!",
   "reasoning": "Lengths, deviation, and 4x improvement all match SOURCE."
  },
  {
   "claim_id": "C035",
   "loglog_ids": [
    "7.4"
   ],
   "claim_text": "Best under-20 board [4,7,11,14,17,20,17,14,11,7,4] hits +/-2.17%; integer linear design +/-3.32%.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Max deviation: ±2.17% ... [4, 7, 11, 14, 17, 20, 17, 14, 11, 7, 4] ... integer step (base=5, step=4): ... Max deviation: ±3.32%",
   "reasoning": "Both boards and deviations match SOURCE numbers."
  },
  {
   "claim_id": "C036",
   "loglog_ids": [
    "7.5"
   ],
   "claim_text": "Advice: play 50% rule on columns 5-9; designers prioritize playability plus handicaps.",
   "claim_type": "recommendation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Use the FiftyPercentSurvival strategy ... Aim for columns 5-9 ... Prioritize playability over mathematical perfection ... consider handicap systems",
   "reasoning": "Both player and designer advice match SOURCE conclusion."
  }
 ],
 "metrics": {
  "total_claims": 36,
  "supported": 36,
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
 "source_id": "03_cant_stop_addicted_to_shindig",
 "key_points": [
  {
   "point_id": "K01",
   "point_text": "Central thesis: Can't Stop is a masterclass in practical game design, where imperfect mathematical balance is acceptable and rules are used to compensate for it.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L002",
    "L032"
   ],
   "evidence_quote": "four dice flatten odds, middle columns dominate, consistent probabilistic strategies win, design favors playability",
   "reasoning": "L002 states the top-level conclusions including design favors playability, and L032 explicitly says design favors playability and the forced-move rule compensates residual imbalance, matching the thesis."
  },
  {
   "point_id": "K02",
   "point_text": "Game rules: roll four dice, pair them to move markers on columns 2 through 12, need three completed columns to win; column lengths are 3,5,7,9,11,13,11,9,7,5,3.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L003",
    "L004"
   ],
   "evidence_quote": "Columns 2-12 have lengths 3-5-7-9-11-13-11-9-7-5-3; complete three columns to win.",
   "reasoning": "L003 gives four dice, pairing, advancing three active markers, and L004 gives exact column lengths and the three-column win condition. All numbers and rules intact."
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
   "evidence_quote": "chosen pairing forces ALL its legal moves, even unwanted ones.",
   "reasoning": "L005 captures the forced-move rule exactly including 'even unwanted ones', and L006 provides the concrete example confirming no cherry-picking."
  },
  {
   "point_id": "K04",
   "point_text": "Two-dice baseline: sum 7 is most likely at 16.67%, exactly 6 times more likely than sum 2 at 2.78%.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L007",
    "L008"
   ],
   "evidence_quote": "Two-dice baseline peaks at 7 with 16.67%, exactly 6x likelier than 2 at 2.78%.",
   "reasoning": "L007 gives 16.67% and the exact 6x ratio versus 2.78%, and L008 supports with the 36-way distribution counts."
  },
  {
   "point_id": "K05",
   "point_text": "With four dice the distribution flattens: P(can make 7) = 64.4% and P(can make 2) = 13.2%, only a 4.88x ratio versus 6x with two dice.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L011",
    "L012",
    "L013"
   ],
   "evidence_quote": "P(can make 7) = 834/1296 approx 64.4% ... P(can make 2) = 171/1296 approx 13.2% ... probability ratio 4.88",
   "reasoning": "L011, L012, and L013 give both endpoints and the 4.88 ratio, explicitly contrasted with the two-dice case. All numbers intact."
  },
  {
   "point_id": "K06",
   "point_text": "Expected rolls to complete a column = length / probability; column 2 needs about 22.73 rolls while column 7 needs about 20.18, so 7 is slightly faster despite being 4x longer.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L015",
    "L013"
   ],
   "evidence_quote": "Expected rolls L/P: column 2 needs 22.73, column 7 needs 20.18 rolls.",
   "reasoning": "L015 states the L/P formula and both roll counts. L013 supplies the 4.33 length ratio that underpins the 'despite being 4x longer' claim."
  },
  {
   "point_id": "K07",
   "point_text": "Column combinations matter: {6,7,8} succeeds 92.0% of the time versus 43.8% for {2,3,12}; all 165 three-column combinations were analyzed, with 37 rated excellent (>=85% success) and a median success of 79.6%.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L016",
    "L017",
    "L018"
   ],
   "evidence_quote": "{6,7,8} succeeds 1193/1296 = 92.0% ... {2,3,12} succeeds only 568/1296 = 43.8% ... All 165 combos ranked; 37 excellent at 85%+, median 79.6%",
   "reasoning": "L016, L017, and L018 capture all four data points: the two combination success rates, the 165-combo universe, the 37 excellent count, and the 79.6% median."
  },
  {
   "point_id": "K08",
   "point_text": "\"Clean\" moves are rare: even the best combination {6,7,8} yields only 39.8% clean rolls, and {2,3,12} only 2.3%, so the forced-move rule contaminates good combinations.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L019",
    "L039"
   ],
   "evidence_quote": "Clean moves only: 39.8% for {6,7,8} and 2.3% for {2,3,12}.",
   "reasoning": "L019 gives both clean-move rates, and L039 explicitly notes forced moves contaminate good combos, matching the causal conclusion."
  },
  {
   "point_id": "K09",
   "point_text": "Stopping heuristic: keep rolling if (P_success x Q) > (P_bust x U), where Q is expected markers advanced and U is unsaved progress; example on {6,7,8} says roll (1.32 > 0.4) and on {2,3,12} says stop (1.12 > 0.46).",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L021",
    "L022"
   ],
   "evidence_quote": "continue if (P_success x Q) > (P_bust x U); {6,7,8} gives 1.32 > 0.4 ... {2,3,12} with 2 steps gives 1.12 > 0.46 loss, so stop.",
   "reasoning": "L021 and L022 give the rule and both worked examples with their numeric comparisons. The meaning of Q and U is implicit via L016/L017's Q values but the decision logic is fully conveyed."
  },
  {
   "point_id": "K10",
   "point_text": "Tournament of 38 strategies across 2,500 head-to-head games each (3.6M total games) found FiftyPercentSurvival the champion at 69.84% win rate, and probabilistic strategies dominate the top rankings.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L024",
    "L025",
    "L027"
   ],
   "evidence_quote": "Tournament of 38 strategies ... 3.6M games ... Champion FiftyPercentSurvival 69.84% (132,696/190,000)",
   "reasoning": "L024, L025, and L027 give the strategy count, the 2,500 games per matchup, 3.6M total, and the 69.84% champion win rate. L027 also shows a probabilistic runner-up, supporting the dominance claim."
  },
  {
   "point_id": "K11",
   "point_text": "Consistency beats speed: GreedyUntil1Col is fastest (10.5 turns) but only ranks #11 at 58.90% due to high variance and bust rate, while FiftyPercentSurvival at 11.3 turns wins most.",
   "weight": "Must have",
   "presence": "Partial",
   "loglog_ids": [
    "L026",
    "L029"
   ],
   "evidence_quote": "GreedyUntil1Col #1 speed but #11 at 58.90%; consistency beats speed.",
   "reasoning": "The core claim and most figures (10.5 turns, #11, 58.90%, variance via sd 5.73 and 7.50 busts, consistency beats speed) are captured by L026 and L029. However the champion FiftyPercentSurvival's 11.3-turn count is not stated anywhere, a dropped number, which per the strict rule caps this Must have at Partial."
  },
  {
   "point_id": "K12",
   "point_text": "Significant first-player advantage: P1 wins 55.59% of games for a +11.18% edge, larger than chess (~5%) or Go (~7%); GreedyUntil1Col shows extreme bias at +31.24%.",
   "weight": "Must have",
   "presence": "Partial",
   "loglog_ids": [
    "L030"
   ],
   "evidence_quote": "First-player advantage +11.18% overall (P1 wins 55.59%); GreedyUntil1Col bias +31.24%.",
   "reasoning": "L030 captures the primary statistics (55.59%, +11.18%, +31.24%). The comparative anchors against chess (~5%) and Go (~7%) are absent, so the 'larger than' framing is lost. Dropped comparative numbers make this Must have Partial."
  },
  {
   "point_id": "K13",
   "point_text": "Balance analysis: single-column completion times deviate at most +/-13.6% from 20 rolls, an optimal board one step from current reaches +/-3.09%, and a 20-step board reaches +/-2.17%.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L033",
    "L035",
    "L036"
   ],
   "evidence_quote": "Single-column deviations stay within +/-13.6% ... Optimal +-1-step board ... cuts deviation to +/-3.09% ... Best under-20 board ... +/-2.17%",
   "reasoning": "L033, L035, and L036 give all three deviation figures. The ~20-roll baseline is corroborated by L015's 20.18/22.73 and L034's balance discussion, so the point survives intact."
  },
  {
   "point_id": "K14",
   "point_text": "Stated caveat: continuation versus switching strategies were not fully analyzed quantitatively and remain an open question for future work.",
   "weight": "Nice to have",
   "presence": "Present",
   "loglog_ids": [
    "L023",
    "L043"
   ],
   "evidence_quote": "Continuation usually beats switching, but full quantitative comparison remains open future work.",
   "reasoning": "L023 states the caveat verbatim and L043 reiterates that the open switching question limits the stopping rule's scope."
  },
  {
   "point_id": "K15",
   "point_text": "Recommendations: players should use FiftyPercentSurvival and aim for columns 5-9 while avoiding forced activation of 2-3 and 11-12; designers should prioritize playability and use rules to compensate for imbalance, considering handicaps for turn order.",
   "weight": "Must have",
   "presence": "Partial",
   "loglog_ids": [
    "L037"
   ],
   "evidence_quote": "Advice: play 50% rule on columns 5-9; designers prioritize playability plus handicaps.",
   "reasoning": "L037 captures the 50% rule, columns 5-9 target, designer playability priority, and handicaps for turn order. The specific condition to avoid forced activation of columns 2-3 and 11-12 is not stated, a dropped actionable condition, capping this Must have at Partial."
  }
 ],
 "metrics": {
  "total_points": 15,
  "must_have_total": 14,
  "must_have_present": 11,
  "must_have_partial": 3,
  "must_have_missing": 0,
  "overall_present": 12,
  "must_recall": 0.8929,
  "overall_recall": 0.9
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
   "claim_text": "Can't Stop analysis: four dice flatten odds, middle columns dominate, consistent probabilistic strategies win, design favors playability.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Four-dice probabilities flatten the distribution ... Probabilistic strategies dominate ... Perfect balance isn't necessary",
   "reasoning": "All summary strands (flattened odds, middle-column dominance, probabilistic winners, playability) appear in source conclusion."
  },
  {
   "claim_id": "C002",
   "loglog_ids": [
    "1"
   ],
   "claim_text": "Roll four dice, pair freely, advance three active markers; bust loses the turn's progress.",
   "claim_type": "definition",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "roll four dice, pair them up however you want ... if you can't move any of your three active markers, you lose everything you've gained that turn",
   "reasoning": "Source states exactly this rule set."
  },
  {
   "claim_id": "C003",
   "loglog_ids": [
    "1.1"
   ],
   "claim_text": "Columns 2-12 have lengths 3-5-7-9-11-13-11-9-7-5-3; complete three columns to win.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "2 and 12: 3 steps ... 7: 13 steps. You need to complete three columns to win",
   "reasoning": "Sequence matches the source column lengths and win condition."
  },
  {
   "claim_id": "C004",
   "loglog_ids": [
    "1.2"
   ],
   "claim_text": "Forced-move rule: chosen pairing forces ALL its legal moves, even unwanted ones.",
   "claim_type": "definition",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "you must take all available moves ... you must make ALL legal moves from that pairing, even if you don't want them",
   "reasoning": "Direct restatement of the forced-move rule."
  },
  {
   "claim_id": "C005",
   "loglog_ids": [
    "1.3"
   ],
   "claim_text": "(1,1,3,4) as 2+7 on {6,7,8} forces taking both 2 and 7.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "you roll (1,1,3,4) ... pairing (1,1)+(3,4) = 2+7 ... forced to take BOTH the 2 and the 7",
   "reasoning": "Source example matches numbers and forced outcome."
  },
  {
   "claim_id": "C006",
   "loglog_ids": [
    "2"
   ],
   "claim_text": "Two-dice baseline peaks at 7 with 16.67%, exactly 6x likelier than 2 at 2.78%.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Sum 7 is the most likely at 16.67%, and it's exactly 6× more likely than sum 2 at 2.78%",
   "reasoning": "Peak, values, and 6x ratio all match source exactly."
  },
  {
   "claim_id": "C007",
   "loglog_ids": [
    "2.1"
   ],
   "claim_text": "Sums 2-12 have 1-2-3-4-5-6-5-4-3-2-1 ways of 36; 1 way versus 6 ordered ways.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "For sum 2, there's only one way ... sum 7 ... order matters, so that's 6 ways total out of 36",
   "reasoning": "Way counts mirror the source table and proof."
  },
  {
   "claim_id": "C008",
   "loglog_ids": [
    "2.2"
   ],
   "claim_text": "Column 7 is only about 4.3x longer (13/3) than column 2, not 6x.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "it's only 13/3 ≈ 4.3× longer",
   "reasoning": "Source states the 4.3x figure via 13/3."
  },
  {
   "claim_id": "C009",
   "loglog_ids": [
    "3"
   ],
   "claim_text": "Four-dice pairing offers three pairings and sharply flattens the distribution.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "That's it, just three possible pairings ... Did the distribution get flatter?",
   "reasoning": "Source confirms three pairings and a flatter distribution."
  },
  {
   "claim_id": "C010",
   "loglog_ids": [
    "3.1"
   ],
   "claim_text": "P(can make 2) = 171/1296 approx 13.2%, up from two-dice 2.78%.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "P(can make a 2) = 1 - 625/1296 - 500/1296 = 171/1296 ≈ 13.2%",
   "reasoning": "Fraction and percentage match source."
  },
  {
   "claim_id": "C011",
   "loglog_ids": [
    "3.2"
   ],
   "claim_text": "P(can make 7) = 834/1296 approx 64.4% via inclusion-exclusion; overlaps 24/1296, triple 0.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "P(A cap B) = ... 24/1296 ... P(A cap B cap C) = 0 ... P(can make a 7) = 834/1296 ≈ 64.4%",
   "reasoning": "All four numbers match source inclusion-exclusion result."
  },
  {
   "claim_id": "C012",
   "loglog_ids": [
    "3.3"
   ],
   "claim_text": "Full range 13.2% to 64.4%; probability ratio 4.88 nearly matches length ratio 4.33.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "The probability ratio from 2 to 7 is 4.88. The length ratio is 4.33",
   "reasoning": "Both ratios and endpoints match source table."
  },
  {
   "claim_id": "C013",
   "loglog_ids": [
    "4"
   ],
   "claim_text": "Three-column combination choice dominates single-column odds.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "column combination choice dominates individual column balance",
   "reasoning": "Source states combination choice dominates individual columns."
  },
  {
   "claim_id": "C014",
   "loglog_ids": [
    "4.1"
   ],
   "claim_text": "Expected rolls L/P: column 2 needs 22.73, column 7 needs 20.18 rolls.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "For column 2: 3/0.132 = 22.73 rolls. For column 7: 13/0.644 = 20.18 rolls",
   "reasoning": "Expected-roll values match source table."
  },
  {
   "claim_id": "C015",
   "loglog_ids": [
    "4.2"
   ],
   "claim_text": "{6,7,8} succeeds 1193/1296 = 92.0% with Q 1.43 markers per roll.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "1193/1296 = 92.0% success rate ... {6,7,8} | 92.0% ... 1.43",
   "reasoning": "Success fraction and Q value match source."
  },
  {
   "claim_id": "C016",
   "loglog_ids": [
    "4.3"
   ],
   "claim_text": "{2,3,12} succeeds only 568/1296 = 43.8% with Q 1.05; bust likelier.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "568/1296 = 43.8% success rate ... {2,3,12} | 43.8% | 56.2% ... 1.05",
   "reasoning": "Success, bust, and Q figures match source."
  },
  {
   "claim_id": "C017",
   "loglog_ids": [
    "4.4"
   ],
   "claim_text": "All 165 combos ranked; 37 excellent at 85%+, median 79.6%, worst 43.8%.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "37 combinations are \"excellent\" (≥85% success rate) ... median combination still succeeds 79.6% ... worst ... 43.8%",
   "reasoning": "Counts and percentages match source distribution summary."
  },
  {
   "claim_id": "C018",
   "loglog_ids": [
    "4.5"
   ],
   "claim_text": "Clean moves only: 39.8% for {6,7,8} and 2.3% for {2,3,12}.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "{6,7,8} only has 39.8% clean moves ... For {2,3,12}: Only 2.3% of rolls are clean",
   "reasoning": "Both clean-move percentages match source."
  },
  {
   "claim_id": "C019",
   "loglog_ids": [
    "5"
   ],
   "claim_text": "Keep rolling while expected gain exceeds expected loss.",
   "claim_type": "recommendation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Keep rolling if: (P_success × Q) > (P_bust × U)",
   "reasoning": "Source states the same expected-gain heuristic."
  },
  {
   "claim_id": "C020",
   "loglog_ids": [
    "5.1"
   ],
   "claim_text": "Rule: continue if (P_success x Q) > (P_bust x U); {6,7,8} gives 1.32 > 0.4.",
   "claim_type": "recommendation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "0.08 × 5 = 0.4 steps ... 0.92 × 1.43 = 1.32 steps ... 1.32 > 0.4",
   "reasoning": "Formula and worked values match source."
  },
  {
   "claim_id": "C021",
   "loglog_ids": [
    "5.2"
   ],
   "claim_text": "{2,3,12} with 2 steps gives 1.12 > 0.46 loss, so stop.",
   "claim_type": "recommendation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Risk: 0.562 × 2 = 1.12 steps ... Expected gain: 0.438 × 1.05 = 0.46 steps ... you should STOP",
   "reasoning": "Source computes the same figures and conclusion."
  },
  {
   "claim_id": "C022",
   "loglog_ids": [
    "5.3"
   ],
   "claim_text": "Continuation usually beats switching, but full quantitative comparison remains open future work.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "The mathematics favor continuation in most cases ... I haven't fully analyzed this aspect quantitatively ... open question for future work",
   "reasoning": "Mirrors source continuation claim and open-question hedge."
  },
  {
   "claim_id": "C023",
   "loglog_ids": [
    "6"
   ],
   "claim_text": "Tournament of 38 strategies across 14 families over 3.6M games crowns FiftyPercentSurvival.",
   "claim_type": "meta",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "I implemented 38 different strategies ... 14 different strategic families ... 3.6 million total games",
   "reasoning": "Strategy count, family count, and game total match source."
  },
  {
   "claim_id": "C024",
   "loglog_ids": [
    "6.1"
   ],
   "claim_text": "Scale: 1,000 trials per strategy, 2,500 games per matchup, 3.6M games total.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "1,000 single-player trials per strategy, 2,500 head-to-head games per matchup, 3.6 million total games",
   "reasoning": "All three simulation scale figures match source."
  },
  {
   "claim_id": "C025",
   "loglog_ids": [
    "6.2"
   ],
   "claim_text": "Fastest GreedyUntil1Col 10.5 turns (median 9, sd 5.73, 7.50 busts); top 15 span 10.5-12.8.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "GreedyUntil1Col | 10.5 | 9 | 5.73 | 7.50 ... The top 15 all complete games in 10.5-12.8 turns",
   "reasoning": "Means, median, std, busts, and span all match source."
  },
  {
   "claim_id": "C026",
   "loglog_ids": [
    "6.3"
   ],
   "claim_text": "Champion FiftyPercentSurvival 69.84% (132,696/190,000); Heuristic(1.5) 66.46% second.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "FiftyPercentSurvival | 69.84% | 132,696/190,000 ... Heuristic(1.5) | 66.46%",
   "reasoning": "Win share and runner-up value match source table."
  },
  {
   "claim_id": "C027",
   "loglog_ids": [
    "6.4"
   ],
   "claim_text": "Champion stops when cumulative survival drops below 50%: n = log(0.5)/log(P_success).",
   "claim_type": "definition",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Roll until cumulative survival probability drops below 50%, calculated as n = log(0.5) / log(P_success)",
   "reasoning": "Formula and threshold match source exactly."
  },
  {
   "claim_id": "C028",
   "loglog_ids": [
    "6.5"
   ],
   "claim_text": "Paradox: GreedyUntil1Col #1 speed but #11 at 58.90%; consistency beats speed.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "GreedyUntil1Col | #1 | 10.5 | #11 | 58.90% ... consistency beats raw speed",
   "reasoning": "Ranks, win rate, and lesson all match source."
  },
  {
   "claim_id": "C029",
   "loglog_ids": [
    "6.6"
   ],
   "claim_text": "First-player advantage +11.18% overall (P1 wins 55.59%); GreedyUntil1Col bias +31.24%.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "First-player advantage: +11.18% ... Player 1 win rate: 55.59% ... GreedyUntil1Col | +31.24%",
   "reasoning": "All three advantage figures match source."
  },
  {
   "claim_id": "C030",
   "loglog_ids": [
    "6.7"
   ],
   "claim_text": "Opponent-aware tweaks did not help; web game plus full code and data released.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Being \"opponent aware\" didn't help ... I've implemented a fully interactive web version ... All analysis code and simulation results are available",
   "reasoning": "Source confirms opponent-aware failure and public web game, code, and data."
  },
  {
   "claim_id": "C031",
   "loglog_ids": [
    "7"
   ],
   "claim_text": "Board fits 1980 constraints; forced-move rule compensates residual imbalance.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "The current design is excellent for 1980. ... rules and mechanics compensate ... that compensating rule is the forced-move rule",
   "reasoning": "SOURCE states design is excellent for 1980 and forced-move rule compensates the imbalance."
  },
  {
   "claim_id": "C032",
   "loglog_ids": [
    "7.1"
   ],
   "claim_text": "Single-column deviations stay within +/-13.6% given integer lengths.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "The deviations are ±13.6% at most. That's pretty good given that lengths must be integers!",
   "reasoning": "Number and qualifier match SOURCE exactly."
  },
  {
   "claim_id": "C033",
   "loglog_ids": [
    "7.2"
   ],
   "claim_text": "Perfect balance needs 171 vs 834 steps, about an 8-hour game.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Column 2/12: 171 steps ... Column 7: 834 steps. Game duration: ~8 hours.",
   "reasoning": "Step counts and duration match SOURCE."
  },
  {
   "claim_id": "C034",
   "loglog_ids": [
    "7.3"
   ],
   "claim_text": "Optimal +-1-step board [3,5,8,10,12,14,12,10,8,5,3] cuts deviation to +/-3.09%, 4x better.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Max deviation: ±3.09% ... Lengths: [3, 5, 8, 10, 12, 14, 12, 10, 8, 5, 3] ... 4× more balanced with just +1 step!",
   "reasoning": "Lengths, deviation, and 4x improvement all match SOURCE."
  },
  {
   "claim_id": "C035",
   "loglog_ids": [
    "7.4"
   ],
   "claim_text": "Best under-20 board [4,7,11,14,17,20,17,14,11,7,4] hits +/-2.17%; integer linear design +/-3.32%.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Max deviation: ±2.17% ... [4, 7, 11, 14, 17, 20, 17, 14, 11, 7, 4] ... integer step (base=5, step=4): ... Max deviation: ±3.32%",
   "reasoning": "Both boards and deviations match SOURCE numbers."
  },
  {
   "claim_id": "C036",
   "loglog_ids": [
    "7.5"
   ],
   "claim_text": "Advice: play 50% rule on columns 5-9; designers prioritize playability plus handicaps.",
   "claim_type": "recommendation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Use the FiftyPercentSurvival strategy ... Aim for columns 5-9 ... Prioritize playability over mathematical perfection ... consider handicap systems",
   "reasoning": "Both player and designer advice match SOURCE conclusion."
  }
 ],
 "metrics": {
  "total_claims": 36,
  "supported": 36,
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
 "source_id": "03_cant_stop_addicted_to_shindig",
 "key_points": [
  {
   "point_id": "K01",
   "point_text": "Central thesis: Can't Stop is a masterclass in practical game design, where imperfect mathematical balance is acceptable and rules are used to compensate for it.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L002",
    "L032"
   ],
   "evidence_quote": "four dice flatten odds, middle columns dominate, consistent probabilistic strategies win, design favors playability",
   "reasoning": "L002 states the top-level conclusions including design favors playability, and L032 explicitly says design favors playability and the forced-move rule compensates residual imbalance, matching the thesis."
  },
  {
   "point_id": "K02",
   "point_text": "Game rules: roll four dice, pair them to move markers on columns 2 through 12, need three completed columns to win; column lengths are 3,5,7,9,11,13,11,9,7,5,3.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L003",
    "L004"
   ],
   "evidence_quote": "Columns 2-12 have lengths 3-5-7-9-11-13-11-9-7-5-3; complete three columns to win.",
   "reasoning": "L003 gives four dice, pairing, advancing three active markers, and L004 gives exact column lengths and the three-column win condition. All numbers and rules intact."
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
   "evidence_quote": "chosen pairing forces ALL its legal moves, even unwanted ones.",
   "reasoning": "L005 captures the forced-move rule exactly including 'even unwanted ones', and L006 provides the concrete example confirming no cherry-picking."
  },
  {
   "point_id": "K04",
   "point_text": "Two-dice baseline: sum 7 is most likely at 16.67%, exactly 6 times more likely than sum 2 at 2.78%.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L007",
    "L008"
   ],
   "evidence_quote": "Two-dice baseline peaks at 7 with 16.67%, exactly 6x likelier than 2 at 2.78%.",
   "reasoning": "L007 gives 16.67% and the exact 6x ratio versus 2.78%, and L008 supports with the 36-way distribution counts."
  },
  {
   "point_id": "K05",
   "point_text": "With four dice the distribution flattens: P(can make 7) = 64.4% and P(can make 2) = 13.2%, only a 4.88x ratio versus 6x with two dice.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L011",
    "L012",
    "L013"
   ],
   "evidence_quote": "P(can make 7) = 834/1296 approx 64.4% ... P(can make 2) = 171/1296 approx 13.2% ... probability ratio 4.88",
   "reasoning": "L011, L012, and L013 give both endpoints and the 4.88 ratio, explicitly contrasted with the two-dice case. All numbers intact."
  },
  {
   "point_id": "K06",
   "point_text": "Expected rolls to complete a column = length / probability; column 2 needs about 22.73 rolls while column 7 needs about 20.18, so 7 is slightly faster despite being 4x longer.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L015",
    "L013"
   ],
   "evidence_quote": "Expected rolls L/P: column 2 needs 22.73, column 7 needs 20.18 rolls.",
   "reasoning": "L015 states the L/P formula and both roll counts. L013 supplies the 4.33 length ratio that underpins the 'despite being 4x longer' claim."
  },
  {
   "point_id": "K07",
   "point_text": "Column combinations matter: {6,7,8} succeeds 92.0% of the time versus 43.8% for {2,3,12}; all 165 three-column combinations were analyzed, with 37 rated excellent (>=85% success) and a median success of 79.6%.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L016",
    "L017",
    "L018"
   ],
   "evidence_quote": "{6,7,8} succeeds 1193/1296 = 92.0% ... {2,3,12} succeeds only 568/1296 = 43.8% ... All 165 combos ranked; 37 excellent at 85%+, median 79.6%",
   "reasoning": "L016, L017, and L018 capture all four data points: the two combination success rates, the 165-combo universe, the 37 excellent count, and the 79.6% median."
  },
  {
   "point_id": "K08",
   "point_text": "\"Clean\" moves are rare: even the best combination {6,7,8} yields only 39.8% clean rolls, and {2,3,12} only 2.3%, so the forced-move rule contaminates good combinations.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L019",
    "L039"
   ],
   "evidence_quote": "Clean moves only: 39.8% for {6,7,8} and 2.3% for {2,3,12}.",
   "reasoning": "L019 gives both clean-move rates, and L039 explicitly notes forced moves contaminate good combos, matching the causal conclusion."
  },
  {
   "point_id": "K09",
   "point_text": "Stopping heuristic: keep rolling if (P_success x Q) > (P_bust x U), where Q is expected markers advanced and U is unsaved progress; example on {6,7,8} says roll (1.32 > 0.4) and on {2,3,12} says stop (1.12 > 0.46).",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L021",
    "L022"
   ],
   "evidence_quote": "continue if (P_success x Q) > (P_bust x U); {6,7,8} gives 1.32 > 0.4 ... {2,3,12} with 2 steps gives 1.12 > 0.46 loss, so stop.",
   "reasoning": "L021 and L022 give the rule and both worked examples with their numeric comparisons. The meaning of Q and U is implicit via L016/L017's Q values but the decision logic is fully conveyed."
  },
  {
   "point_id": "K10",
   "point_text": "Tournament of 38 strategies across 2,500 head-to-head games each (3.6M total games) found FiftyPercentSurvival the champion at 69.84% win rate, and probabilistic strategies dominate the top rankings.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L024",
    "L025",
    "L027"
   ],
   "evidence_quote": "Tournament of 38 strategies ... 3.6M games ... Champion FiftyPercentSurvival 69.84% (132,696/190,000)",
   "reasoning": "L024, L025, and L027 give the strategy count, the 2,500 games per matchup, 3.6M total, and the 69.84% champion win rate. L027 also shows a probabilistic runner-up, supporting the dominance claim."
  },
  {
   "point_id": "K11",
   "point_text": "Consistency beats speed: GreedyUntil1Col is fastest (10.5 turns) but only ranks #11 at 58.90% due to high variance and bust rate, while FiftyPercentSurvival at 11.3 turns wins most.",
   "weight": "Must have",
   "presence": "Partial",
   "loglog_ids": [
    "L026",
    "L029"
   ],
   "evidence_quote": "GreedyUntil1Col #1 speed but #11 at 58.90%; consistency beats speed.",
   "reasoning": "The core claim and most figures (10.5 turns, #11, 58.90%, variance via sd 5.73 and 7.50 busts, consistency beats speed) are captured by L026 and L029. However the champion FiftyPercentSurvival's 11.3-turn count is not stated anywhere, a dropped number, which per the strict rule caps this Must have at Partial."
  },
  {
   "point_id": "K12",
   "point_text": "Significant first-player advantage: P1 wins 55.59% of games for a +11.18% edge, larger than chess (~5%) or Go (~7%); GreedyUntil1Col shows extreme bias at +31.24%.",
   "weight": "Must have",
   "presence": "Partial",
   "loglog_ids": [
    "L030"
   ],
   "evidence_quote": "First-player advantage +11.18% overall (P1 wins 55.59%); GreedyUntil1Col bias +31.24%.",
   "reasoning": "L030 captures the primary statistics (55.59%, +11.18%, +31.24%). The comparative anchors against chess (~5%) and Go (~7%) are absent, so the 'larger than' framing is lost. Dropped comparative numbers make this Must have Partial."
  },
  {
   "point_id": "K13",
   "point_text": "Balance analysis: single-column completion times deviate at most +/-13.6% from 20 rolls, an optimal board one step from current reaches +/-3.09%, and a 20-step board reaches +/-2.17%.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L033",
    "L035",
    "L036"
   ],
   "evidence_quote": "Single-column deviations stay within +/-13.6% ... Optimal +-1-step board ... cuts deviation to +/-3.09% ... Best under-20 board ... +/-2.17%",
   "reasoning": "L033, L035, and L036 give all three deviation figures. The ~20-roll baseline is corroborated by L015's 20.18/22.73 and L034's balance discussion, so the point survives intact."
  },
  {
   "point_id": "K14",
   "point_text": "Stated caveat: continuation versus switching strategies were not fully analyzed quantitatively and remain an open question for future work.",
   "weight": "Nice to have",
   "presence": "Present",
   "loglog_ids": [
    "L023",
    "L043"
   ],
   "evidence_quote": "Continuation usually beats switching, but full quantitative comparison remains open future work.",
   "reasoning": "L023 states the caveat verbatim and L043 reiterates that the open switching question limits the stopping rule's scope."
  },
  {
   "point_id": "K15",
   "point_text": "Recommendations: players should use FiftyPercentSurvival and aim for columns 5-9 while avoiding forced activation of 2-3 and 11-12; designers should prioritize playability and use rules to compensate for imbalance, considering handicaps for turn order.",
   "weight": "Must have",
   "presence": "Partial",
   "loglog_ids": [
    "L037"
   ],
   "evidence_quote": "Advice: play 50% rule on columns 5-9; designers prioritize playability plus handicaps.",
   "reasoning": "L037 captures the 50% rule, columns 5-9 target, designer playability priority, and handicaps for turn order. The specific condition to avoid forced activation of columns 2-3 and 11-12 is not stated, a dropped actionable condition, capping this Must have at Partial."
  }
 ],
 "metrics": {
  "total_points": 15,
  "must_have_total": 14,
  "must_have_present": 11,
  "must_have_partial": 3,
  "must_have_missing": 0,
  "overall_present": 12,
  "must_recall": 0.8929,
  "overall_recall": 0.9
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
    "0"
   ],
   "label": "Duplicate",
   "canonical_id": "C009",
   "reasoning": "Summary recaps body points (flatten odds, dominance, consistency, playability); adds no new claim beyond C009 and peers."
  },
  {
   "claim_id": "C002",
   "loglog_ids": [
    "1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Core game mechanics rule, not restated elsewhere."
  },
  {
   "claim_id": "C003",
   "loglog_ids": [
    "1.1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Column lengths and win condition numbers appear only here."
  },
  {
   "claim_id": "C004",
   "loglog_ids": [
    "1.2"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Forced-move definition distinct from its later design-role use."
  },
  {
   "claim_id": "C005",
   "loglog_ids": [
    "1.3"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Concrete forced-move instance; adds worked detail to C004."
  },
  {
   "claim_id": "C006",
   "loglog_ids": [
    "2"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Two-dice peak value and sixfold ratio are baseline numbers."
  },
  {
   "claim_id": "C007",
   "loglog_ids": [
    "2.1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Full sum distribution and ordered-way evidence new here."
  },
  {
   "claim_id": "C008",
   "loglog_ids": [
    "2.2"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Length-ratio correction (4.33 not 6) is a distinct caveat."
  },
  {
   "claim_id": "C009",
   "loglog_ids": [
    "3"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Canonical four-dice flatten claim; adds three pairings."
  },
  {
   "claim_id": "C010",
   "loglog_ids": [
    "3.1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Probability of making 2 computed, new quantitative result."
  },
  {
   "claim_id": "C011",
   "loglog_ids": [
    "3.2"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Probability of making 7 with inclusion-exclusion detail."
  },
  {
   "claim_id": "C012",
   "loglog_ids": [
    "3.3"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Probability-to-length ratio comparison adds new relation despite restated endpoints."
  },
  {
   "claim_id": "C013",
   "loglog_ids": [
    "4"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Three-column combination dominance differs from single-column odds."
  },
  {
   "claim_id": "C014",
   "loglog_ids": [
    "4.1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Expected-roll figures for two columns appear only here."
  },
  {
   "claim_id": "C015",
   "loglog_ids": [
    "4.2"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "{6,7,8} success rate and Q are distinct quantitative facts."
  },
  {
   "claim_id": "C016",
   "loglog_ids": [
    "4.3"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "{2,3,12} success rate and bust note distinct from C015."
  },
  {
   "claim_id": "C017",
   "loglog_ids": [
    "4.4"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Ranking distribution adds combo count and median."
  },
  {
   "claim_id": "C018",
   "loglog_ids": [
    "4.5"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Clean-move caveat is a distinct qualifier on C015/C016."
  },
  {
   "claim_id": "C019",
   "loglog_ids": [
    "5"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Generic stopping principle, not restated verbatim later."
  },
  {
   "claim_id": "C020",
   "loglog_ids": [
    "5.1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Quantitative continuation rule with figures new."
  },
  {
   "claim_id": "C021",
   "loglog_ids": [
    "5.2"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Stop-advice instance for {2,3,12} adds numbers."
  },
  {
   "claim_id": "C022",
   "loglog_ids": [
    "5.3"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Switching comparison and open-question caveat distinct."
  },
  {
   "claim_id": "C023",
   "loglog_ids": [
    "6"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Tournament headline with strategy and family counts."
  },
  {
   "claim_id": "C024",
   "loglog_ids": [
    "6.1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Adds trials-per-strategy and games-per-matchup detail."
  },
  {
   "claim_id": "C025",
   "loglog_ids": [
    "6.2"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Speed statistics for GreedyUntil1Col new here."
  },
  {
   "claim_id": "C026",
   "loglog_ids": [
    "6.3"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Champion win rate and runner-up numbers distinct."
  },
  {
   "claim_id": "C027",
   "loglog_ids": [
    "6.4"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Champion stopping formula is a distinct definition."
  },
  {
   "claim_id": "C028",
   "loglog_ids": [
    "6.5"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Speed-versus-ranking paradox adds rank and rate."
  },
  {
   "claim_id": "C029",
   "loglog_ids": [
    "6.6"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "First-player advantage figures appear only here."
  },
  {
   "claim_id": "C030",
   "loglog_ids": [
    "6.7"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Negative result plus artifact release is new information."
  },
  {
   "claim_id": "C031",
   "loglog_ids": [
    "7"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Board design context and compensation role distinct from C004."
  },
  {
   "claim_id": "C032",
   "loglog_ids": [
    "7.1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Deviation bound for integer lengths new."
  },
  {
   "claim_id": "C033",
   "loglog_ids": [
    "7.2"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Perfect-balance step counts and game length distinct."
  },
  {
   "claim_id": "C034",
   "loglog_ids": [
    "7.3"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Optimal board deviation figure and factor new."
  },
  {
   "claim_id": "C035",
   "loglog_ids": [
    "7.4"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Under-20 board and integer-design bounds new."
  },
  {
   "claim_id": "C036",
   "loglog_ids": [
    "7.5"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Practical 50% advice on columns 5-9 is new."
  }
 ],
 "metrics": {
  "scored_claims": 36,
  "unique": 35,
  "duplicates": 1,
  "trivia": 0,
  "redundancy_rate": 0.0278,
  "trivia_rate": 0.0,
  "structured_tokens": 604,
  "tokens_per_unique_claim": 17.26
 },
 "prune_list": [
  "C001 duplicates C009/C013/C026/C031; summary is a recap, safe to compress or drop"
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
   "claim_text": "Can't Stop analysis: four dice flatten odds, middle columns dominate, consistent probabilistic strategies win, design favors playability.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Four-dice probabilities flatten the distribution ... Probabilistic strategies dominate ... Perfect balance isn't necessary",
   "reasoning": "All summary strands (flattened odds, middle-column dominance, probabilistic winners, playability) appear in source conclusion."
  },
  {
   "claim_id": "C002",
   "loglog_ids": [
    "1"
   ],
   "claim_text": "Roll four dice, pair freely, advance three active markers; bust loses the turn's progress.",
   "claim_type": "definition",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "roll four dice, pair them up however you want ... if you can't move any of your three active markers, you lose everything you've gained that turn",
   "reasoning": "Source states exactly this rule set."
  },
  {
   "claim_id": "C003",
   "loglog_ids": [
    "1.1"
   ],
   "claim_text": "Columns 2-12 have lengths 3-5-7-9-11-13-11-9-7-5-3; complete three columns to win.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "2 and 12: 3 steps ... 7: 13 steps. You need to complete three columns to win",
   "reasoning": "Sequence matches the source column lengths and win condition."
  },
  {
   "claim_id": "C004",
   "loglog_ids": [
    "1.2"
   ],
   "claim_text": "Forced-move rule: chosen pairing forces ALL its legal moves, even unwanted ones.",
   "claim_type": "definition",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "you must take all available moves ... you must make ALL legal moves from that pairing, even if you don't want them",
   "reasoning": "Direct restatement of the forced-move rule."
  },
  {
   "claim_id": "C005",
   "loglog_ids": [
    "1.3"
   ],
   "claim_text": "(1,1,3,4) as 2+7 on {6,7,8} forces taking both 2 and 7.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "you roll (1,1,3,4) ... pairing (1,1)+(3,4) = 2+7 ... forced to take BOTH the 2 and the 7",
   "reasoning": "Source example matches numbers and forced outcome."
  },
  {
   "claim_id": "C006",
   "loglog_ids": [
    "2"
   ],
   "claim_text": "Two-dice baseline peaks at 7 with 16.67%, exactly 6x likelier than 2 at 2.78%.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Sum 7 is the most likely at 16.67%, and it's exactly 6× more likely than sum 2 at 2.78%",
   "reasoning": "Peak, values, and 6x ratio all match source exactly."
  },
  {
   "claim_id": "C007",
   "loglog_ids": [
    "2.1"
   ],
   "claim_text": "Sums 2-12 have 1-2-3-4-5-6-5-4-3-2-1 ways of 36; 1 way versus 6 ordered ways.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "For sum 2, there's only one way ... sum 7 ... order matters, so that's 6 ways total out of 36",
   "reasoning": "Way counts mirror the source table and proof."
  },
  {
   "claim_id": "C008",
   "loglog_ids": [
    "2.2"
   ],
   "claim_text": "Column 7 is only about 4.3x longer (13/3) than column 2, not 6x.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "it's only 13/3 ≈ 4.3× longer",
   "reasoning": "Source states the 4.3x figure via 13/3."
  },
  {
   "claim_id": "C009",
   "loglog_ids": [
    "3"
   ],
   "claim_text": "Four-dice pairing offers three pairings and sharply flattens the distribution.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "That's it, just three possible pairings ... Did the distribution get flatter?",
   "reasoning": "Source confirms three pairings and a flatter distribution."
  },
  {
   "claim_id": "C010",
   "loglog_ids": [
    "3.1"
   ],
   "claim_text": "P(can make 2) = 171/1296 approx 13.2%, up from two-dice 2.78%.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "P(can make a 2) = 1 - 625/1296 - 500/1296 = 171/1296 ≈ 13.2%",
   "reasoning": "Fraction and percentage match source."
  },
  {
   "claim_id": "C011",
   "loglog_ids": [
    "3.2"
   ],
   "claim_text": "P(can make 7) = 834/1296 approx 64.4% via inclusion-exclusion; overlaps 24/1296, triple 0.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "P(A cap B) = ... 24/1296 ... P(A cap B cap C) = 0 ... P(can make a 7) = 834/1296 ≈ 64.4%",
   "reasoning": "All four numbers match source inclusion-exclusion result."
  },
  {
   "claim_id": "C012",
   "loglog_ids": [
    "3.3"
   ],
   "claim_text": "Full range 13.2% to 64.4%; probability ratio 4.88 nearly matches length ratio 4.33.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "The probability ratio from 2 to 7 is 4.88. The length ratio is 4.33",
   "reasoning": "Both ratios and endpoints match source table."
  },
  {
   "claim_id": "C013",
   "loglog_ids": [
    "4"
   ],
   "claim_text": "Three-column combination choice dominates single-column odds.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "column combination choice dominates individual column balance",
   "reasoning": "Source states combination choice dominates individual columns."
  },
  {
   "claim_id": "C014",
   "loglog_ids": [
    "4.1"
   ],
   "claim_text": "Expected rolls L/P: column 2 needs 22.73, column 7 needs 20.18 rolls.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "For column 2: 3/0.132 = 22.73 rolls. For column 7: 13/0.644 = 20.18 rolls",
   "reasoning": "Expected-roll values match source table."
  },
  {
   "claim_id": "C015",
   "loglog_ids": [
    "4.2"
   ],
   "claim_text": "{6,7,8} succeeds 1193/1296 = 92.0% with Q 1.43 markers per roll.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "1193/1296 = 92.0% success rate ... {6,7,8} | 92.0% ... 1.43",
   "reasoning": "Success fraction and Q value match source."
  },
  {
   "claim_id": "C016",
   "loglog_ids": [
    "4.3"
   ],
   "claim_text": "{2,3,12} succeeds only 568/1296 = 43.8% with Q 1.05; bust likelier.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "568/1296 = 43.8% success rate ... {2,3,12} | 43.8% | 56.2% ... 1.05",
   "reasoning": "Success, bust, and Q figures match source."
  },
  {
   "claim_id": "C017",
   "loglog_ids": [
    "4.4"
   ],
   "claim_text": "All 165 combos ranked; 37 excellent at 85%+, median 79.6%, worst 43.8%.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "37 combinations are \"excellent\" (≥85% success rate) ... median combination still succeeds 79.6% ... worst ... 43.8%",
   "reasoning": "Counts and percentages match source distribution summary."
  },
  {
   "claim_id": "C018",
   "loglog_ids": [
    "4.5"
   ],
   "claim_text": "Clean moves only: 39.8% for {6,7,8} and 2.3% for {2,3,12}.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "{6,7,8} only has 39.8% clean moves ... For {2,3,12}: Only 2.3% of rolls are clean",
   "reasoning": "Both clean-move percentages match source."
  },
  {
   "claim_id": "C019",
   "loglog_ids": [
    "5"
   ],
   "claim_text": "Keep rolling while expected gain exceeds expected loss.",
   "claim_type": "recommendation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Keep rolling if: (P_success × Q) > (P_bust × U)",
   "reasoning": "Source states the same expected-gain heuristic."
  },
  {
   "claim_id": "C020",
   "loglog_ids": [
    "5.1"
   ],
   "claim_text": "Rule: continue if (P_success x Q) > (P_bust x U); {6,7,8} gives 1.32 > 0.4.",
   "claim_type": "recommendation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "0.08 × 5 = 0.4 steps ... 0.92 × 1.43 = 1.32 steps ... 1.32 > 0.4",
   "reasoning": "Formula and worked values match source."
  },
  {
   "claim_id": "C021",
   "loglog_ids": [
    "5.2"
   ],
   "claim_text": "{2,3,12} with 2 steps gives 1.12 > 0.46 loss, so stop.",
   "claim_type": "recommendation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Risk: 0.562 × 2 = 1.12 steps ... Expected gain: 0.438 × 1.05 = 0.46 steps ... you should STOP",
   "reasoning": "Source computes the same figures and conclusion."
  },
  {
   "claim_id": "C022",
   "loglog_ids": [
    "5.3"
   ],
   "claim_text": "Continuation usually beats switching, but full quantitative comparison remains open future work.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "The mathematics favor continuation in most cases ... I haven't fully analyzed this aspect quantitatively ... open question for future work",
   "reasoning": "Mirrors source continuation claim and open-question hedge."
  },
  {
   "claim_id": "C023",
   "loglog_ids": [
    "6"
   ],
   "claim_text": "Tournament of 38 strategies across 14 families over 3.6M games crowns FiftyPercentSurvival.",
   "claim_type": "meta",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "I implemented 38 different strategies ... 14 different strategic families ... 3.6 million total games",
   "reasoning": "Strategy count, family count, and game total match source."
  },
  {
   "claim_id": "C024",
   "loglog_ids": [
    "6.1"
   ],
   "claim_text": "Scale: 1,000 trials per strategy, 2,500 games per matchup, 3.6M games total.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "1,000 single-player trials per strategy, 2,500 head-to-head games per matchup, 3.6 million total games",
   "reasoning": "All three simulation scale figures match source."
  },
  {
   "claim_id": "C025",
   "loglog_ids": [
    "6.2"
   ],
   "claim_text": "Fastest GreedyUntil1Col 10.5 turns (median 9, sd 5.73, 7.50 busts); top 15 span 10.5-12.8.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "GreedyUntil1Col | 10.5 | 9 | 5.73 | 7.50 ... The top 15 all complete games in 10.5-12.8 turns",
   "reasoning": "Means, median, std, busts, and span all match source."
  },
  {
   "claim_id": "C026",
   "loglog_ids": [
    "6.3"
   ],
   "claim_text": "Champion FiftyPercentSurvival 69.84% (132,696/190,000); Heuristic(1.5) 66.46% second.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "FiftyPercentSurvival | 69.84% | 132,696/190,000 ... Heuristic(1.5) | 66.46%",
   "reasoning": "Win share and runner-up value match source table."
  },
  {
   "claim_id": "C027",
   "loglog_ids": [
    "6.4"
   ],
   "claim_text": "Champion stops when cumulative survival drops below 50%: n = log(0.5)/log(P_success).",
   "claim_type": "definition",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Roll until cumulative survival probability drops below 50%, calculated as n = log(0.5) / log(P_success)",
   "reasoning": "Formula and threshold match source exactly."
  },
  {
   "claim_id": "C028",
   "loglog_ids": [
    "6.5"
   ],
   "claim_text": "Paradox: GreedyUntil1Col #1 speed but #11 at 58.90%; consistency beats speed.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "GreedyUntil1Col | #1 | 10.5 | #11 | 58.90% ... consistency beats raw speed",
   "reasoning": "Ranks, win rate, and lesson all match source."
  },
  {
   "claim_id": "C029",
   "loglog_ids": [
    "6.6"
   ],
   "claim_text": "First-player advantage +11.18% overall (P1 wins 55.59%); GreedyUntil1Col bias +31.24%.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "First-player advantage: +11.18% ... Player 1 win rate: 55.59% ... GreedyUntil1Col | +31.24%",
   "reasoning": "All three advantage figures match source."
  },
  {
   "claim_id": "C030",
   "loglog_ids": [
    "6.7"
   ],
   "claim_text": "Opponent-aware tweaks did not help; web game plus full code and data released.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Being \"opponent aware\" didn't help ... I've implemented a fully interactive web version ... All analysis code and simulation results are available",
   "reasoning": "Source confirms opponent-aware failure and public web game, code, and data."
  },
  {
   "claim_id": "C031",
   "loglog_ids": [
    "7"
   ],
   "claim_text": "Board fits 1980 constraints; forced-move rule compensates residual imbalance.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "The current design is excellent for 1980. ... rules and mechanics compensate ... that compensating rule is the forced-move rule",
   "reasoning": "SOURCE states design is excellent for 1980 and forced-move rule compensates the imbalance."
  },
  {
   "claim_id": "C032",
   "loglog_ids": [
    "7.1"
   ],
   "claim_text": "Single-column deviations stay within +/-13.6% given integer lengths.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "The deviations are ±13.6% at most. That's pretty good given that lengths must be integers!",
   "reasoning": "Number and qualifier match SOURCE exactly."
  },
  {
   "claim_id": "C033",
   "loglog_ids": [
    "7.2"
   ],
   "claim_text": "Perfect balance needs 171 vs 834 steps, about an 8-hour game.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Column 2/12: 171 steps ... Column 7: 834 steps. Game duration: ~8 hours.",
   "reasoning": "Step counts and duration match SOURCE."
  },
  {
   "claim_id": "C034",
   "loglog_ids": [
    "7.3"
   ],
   "claim_text": "Optimal +-1-step board [3,5,8,10,12,14,12,10,8,5,3] cuts deviation to +/-3.09%, 4x better.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Max deviation: ±3.09% ... Lengths: [3, 5, 8, 10, 12, 14, 12, 10, 8, 5, 3] ... 4× more balanced with just +1 step!",
   "reasoning": "Lengths, deviation, and 4x improvement all match SOURCE."
  },
  {
   "claim_id": "C035",
   "loglog_ids": [
    "7.4"
   ],
   "claim_text": "Best under-20 board [4,7,11,14,17,20,17,14,11,7,4] hits +/-2.17%; integer linear design +/-3.32%.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Max deviation: ±2.17% ... [4, 7, 11, 14, 17, 20, 17, 14, 11, 7, 4] ... integer step (base=5, step=4): ... Max deviation: ±3.32%",
   "reasoning": "Both boards and deviations match SOURCE numbers."
  },
  {
   "claim_id": "C036",
   "loglog_ids": [
    "7.5"
   ],
   "claim_text": "Advice: play 50% rule on columns 5-9; designers prioritize playability plus handicaps.",
   "claim_type": "recommendation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Use the FiftyPercentSurvival strategy ... Aim for columns 5-9 ... Prioritize playability over mathematical perfection ... consider handicap systems",
   "reasoning": "Both player and designer advice match SOURCE conclusion."
  }
 ],
 "metrics": {
  "total_claims": 36,
  "supported": 36,
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
 "source_id": "03_cant_stop_addicted_to_shindig",
 "key_points": [
  {
   "point_id": "K01",
   "point_text": "Central thesis: Can't Stop is a masterclass in practical game design, where imperfect mathematical balance is acceptable and rules are used to compensate for it.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L002",
    "L032"
   ],
   "evidence_quote": "four dice flatten odds, middle columns dominate, consistent probabilistic strategies win, design favors playability",
   "reasoning": "L002 states the top-level conclusions including design favors playability, and L032 explicitly says design favors playability and the forced-move rule compensates residual imbalance, matching the thesis."
  },
  {
   "point_id": "K02",
   "point_text": "Game rules: roll four dice, pair them to move markers on columns 2 through 12, need three completed columns to win; column lengths are 3,5,7,9,11,13,11,9,7,5,3.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L003",
    "L004"
   ],
   "evidence_quote": "Columns 2-12 have lengths 3-5-7-9-11-13-11-9-7-5-3; complete three columns to win.",
   "reasoning": "L003 gives four dice, pairing, advancing three active markers, and L004 gives exact column lengths and the three-column win condition. All numbers and rules intact."
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
   "evidence_quote": "chosen pairing forces ALL its legal moves, even unwanted ones.",
   "reasoning": "L005 captures the forced-move rule exactly including 'even unwanted ones', and L006 provides the concrete example confirming no cherry-picking."
  },
  {
   "point_id": "K04",
   "point_text": "Two-dice baseline: sum 7 is most likely at 16.67%, exactly 6 times more likely than sum 2 at 2.78%.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L007",
    "L008"
   ],
   "evidence_quote": "Two-dice baseline peaks at 7 with 16.67%, exactly 6x likelier than 2 at 2.78%.",
   "reasoning": "L007 gives 16.67% and the exact 6x ratio versus 2.78%, and L008 supports with the 36-way distribution counts."
  },
  {
   "point_id": "K05",
   "point_text": "With four dice the distribution flattens: P(can make 7) = 64.4% and P(can make 2) = 13.2%, only a 4.88x ratio versus 6x with two dice.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L011",
    "L012",
    "L013"
   ],
   "evidence_quote": "P(can make 7) = 834/1296 approx 64.4% ... P(can make 2) = 171/1296 approx 13.2% ... probability ratio 4.88",
   "reasoning": "L011, L012, and L013 give both endpoints and the 4.88 ratio, explicitly contrasted with the two-dice case. All numbers intact."
  },
  {
   "point_id": "K06",
   "point_text": "Expected rolls to complete a column = length / probability; column 2 needs about 22.73 rolls while column 7 needs about 20.18, so 7 is slightly faster despite being 4x longer.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L015",
    "L013"
   ],
   "evidence_quote": "Expected rolls L/P: column 2 needs 22.73, column 7 needs 20.18 rolls.",
   "reasoning": "L015 states the L/P formula and both roll counts. L013 supplies the 4.33 length ratio that underpins the 'despite being 4x longer' claim."
  },
  {
   "point_id": "K07",
   "point_text": "Column combinations matter: {6,7,8} succeeds 92.0% of the time versus 43.8% for {2,3,12}; all 165 three-column combinations were analyzed, with 37 rated excellent (>=85% success) and a median success of 79.6%.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L016",
    "L017",
    "L018"
   ],
   "evidence_quote": "{6,7,8} succeeds 1193/1296 = 92.0% ... {2,3,12} succeeds only 568/1296 = 43.8% ... All 165 combos ranked; 37 excellent at 85%+, median 79.6%",
   "reasoning": "L016, L017, and L018 capture all four data points: the two combination success rates, the 165-combo universe, the 37 excellent count, and the 79.6% median."
  },
  {
   "point_id": "K08",
   "point_text": "\"Clean\" moves are rare: even the best combination {6,7,8} yields only 39.8% clean rolls, and {2,3,12} only 2.3%, so the forced-move rule contaminates good combinations.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L019",
    "L039"
   ],
   "evidence_quote": "Clean moves only: 39.8% for {6,7,8} and 2.3% for {2,3,12}.",
   "reasoning": "L019 gives both clean-move rates, and L039 explicitly notes forced moves contaminate good combos, matching the causal conclusion."
  },
  {
   "point_id": "K09",
   "point_text": "Stopping heuristic: keep rolling if (P_success x Q) > (P_bust x U), where Q is expected markers advanced and U is unsaved progress; example on {6,7,8} says roll (1.32 > 0.4) and on {2,3,12} says stop (1.12 > 0.46).",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L021",
    "L022"
   ],
   "evidence_quote": "continue if (P_success x Q) > (P_bust x U); {6,7,8} gives 1.32 > 0.4 ... {2,3,12} with 2 steps gives 1.12 > 0.46 loss, so stop.",
   "reasoning": "L021 and L022 give the rule and both worked examples with their numeric comparisons. The meaning of Q and U is implicit via L016/L017's Q values but the decision logic is fully conveyed."
  },
  {
   "point_id": "K10",
   "point_text": "Tournament of 38 strategies across 2,500 head-to-head games each (3.6M total games) found FiftyPercentSurvival the champion at 69.84% win rate, and probabilistic strategies dominate the top rankings.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L024",
    "L025",
    "L027"
   ],
   "evidence_quote": "Tournament of 38 strategies ... 3.6M games ... Champion FiftyPercentSurvival 69.84% (132,696/190,000)",
   "reasoning": "L024, L025, and L027 give the strategy count, the 2,500 games per matchup, 3.6M total, and the 69.84% champion win rate. L027 also shows a probabilistic runner-up, supporting the dominance claim."
  },
  {
   "point_id": "K11",
   "point_text": "Consistency beats speed: GreedyUntil1Col is fastest (10.5 turns) but only ranks #11 at 58.90% due to high variance and bust rate, while FiftyPercentSurvival at 11.3 turns wins most.",
   "weight": "Must have",
   "presence": "Partial",
   "loglog_ids": [
    "L026",
    "L029"
   ],
   "evidence_quote": "GreedyUntil1Col #1 speed but #11 at 58.90%; consistency beats speed.",
   "reasoning": "The core claim and most figures (10.5 turns, #11, 58.90%, variance via sd 5.73 and 7.50 busts, consistency beats speed) are captured by L026 and L029. However the champion FiftyPercentSurvival's 11.3-turn count is not stated anywhere, a dropped number, which per the strict rule caps this Must have at Partial."
  },
  {
   "point_id": "K12",
   "point_text": "Significant first-player advantage: P1 wins 55.59% of games for a +11.18% edge, larger than chess (~5%) or Go (~7%); GreedyUntil1Col shows extreme bias at +31.24%.",
   "weight": "Must have",
   "presence": "Partial",
   "loglog_ids": [
    "L030"
   ],
   "evidence_quote": "First-player advantage +11.18% overall (P1 wins 55.59%); GreedyUntil1Col bias +31.24%.",
   "reasoning": "L030 captures the primary statistics (55.59%, +11.18%, +31.24%). The comparative anchors against chess (~5%) and Go (~7%) are absent, so the 'larger than' framing is lost. Dropped comparative numbers make this Must have Partial."
  },
  {
   "point_id": "K13",
   "point_text": "Balance analysis: single-column completion times deviate at most +/-13.6% from 20 rolls, an optimal board one step from current reaches +/-3.09%, and a 20-step board reaches +/-2.17%.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L033",
    "L035",
    "L036"
   ],
   "evidence_quote": "Single-column deviations stay within +/-13.6% ... Optimal +-1-step board ... cuts deviation to +/-3.09% ... Best under-20 board ... +/-2.17%",
   "reasoning": "L033, L035, and L036 give all three deviation figures. The ~20-roll baseline is corroborated by L015's 20.18/22.73 and L034's balance discussion, so the point survives intact."
  },
  {
   "point_id": "K14",
   "point_text": "Stated caveat: continuation versus switching strategies were not fully analyzed quantitatively and remain an open question for future work.",
   "weight": "Nice to have",
   "presence": "Present",
   "loglog_ids": [
    "L023",
    "L043"
   ],
   "evidence_quote": "Continuation usually beats switching, but full quantitative comparison remains open future work.",
   "reasoning": "L023 states the caveat verbatim and L043 reiterates that the open switching question limits the stopping rule's scope."
  },
  {
   "point_id": "K15",
   "point_text": "Recommendations: players should use FiftyPercentSurvival and aim for columns 5-9 while avoiding forced activation of 2-3 and 11-12; designers should prioritize playability and use rules to compensate for imbalance, considering handicaps for turn order.",
   "weight": "Must have",
   "presence": "Partial",
   "loglog_ids": [
    "L037"
   ],
   "evidence_quote": "Advice: play 50% rule on columns 5-9; designers prioritize playability plus handicaps.",
   "reasoning": "L037 captures the 50% rule, columns 5-9 target, designer playability priority, and handicaps for turn order. The specific condition to avoid forced activation of columns 2-3 and 11-12 is not stated, a dropped actionable condition, capping this Must have at Partial."
  }
 ],
 "metrics": {
  "total_points": 15,
  "must_have_total": 14,
  "must_have_present": 11,
  "must_have_partial": 3,
  "must_have_missing": 0,
  "overall_present": 12,
  "must_recall": 0.8929,
  "overall_recall": 0.9
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
    "0"
   ],
   "label": "Duplicate",
   "canonical_id": "C009",
   "reasoning": "Summary recaps body points (flatten odds, dominance, consistency, playability); adds no new claim beyond C009 and peers."
  },
  {
   "claim_id": "C002",
   "loglog_ids": [
    "1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Core game mechanics rule, not restated elsewhere."
  },
  {
   "claim_id": "C003",
   "loglog_ids": [
    "1.1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Column lengths and win condition numbers appear only here."
  },
  {
   "claim_id": "C004",
   "loglog_ids": [
    "1.2"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Forced-move definition distinct from its later design-role use."
  },
  {
   "claim_id": "C005",
   "loglog_ids": [
    "1.3"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Concrete forced-move instance; adds worked detail to C004."
  },
  {
   "claim_id": "C006",
   "loglog_ids": [
    "2"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Two-dice peak value and sixfold ratio are baseline numbers."
  },
  {
   "claim_id": "C007",
   "loglog_ids": [
    "2.1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Full sum distribution and ordered-way evidence new here."
  },
  {
   "claim_id": "C008",
   "loglog_ids": [
    "2.2"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Length-ratio correction (4.33 not 6) is a distinct caveat."
  },
  {
   "claim_id": "C009",
   "loglog_ids": [
    "3"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Canonical four-dice flatten claim; adds three pairings."
  },
  {
   "claim_id": "C010",
   "loglog_ids": [
    "3.1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Probability of making 2 computed, new quantitative result."
  },
  {
   "claim_id": "C011",
   "loglog_ids": [
    "3.2"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Probability of making 7 with inclusion-exclusion detail."
  },
  {
   "claim_id": "C012",
   "loglog_ids": [
    "3.3"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Probability-to-length ratio comparison adds new relation despite restated endpoints."
  },
  {
   "claim_id": "C013",
   "loglog_ids": [
    "4"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Three-column combination dominance differs from single-column odds."
  },
  {
   "claim_id": "C014",
   "loglog_ids": [
    "4.1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Expected-roll figures for two columns appear only here."
  },
  {
   "claim_id": "C015",
   "loglog_ids": [
    "4.2"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "{6,7,8} success rate and Q are distinct quantitative facts."
  },
  {
   "claim_id": "C016",
   "loglog_ids": [
    "4.3"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "{2,3,12} success rate and bust note distinct from C015."
  },
  {
   "claim_id": "C017",
   "loglog_ids": [
    "4.4"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Ranking distribution adds combo count and median."
  },
  {
   "claim_id": "C018",
   "loglog_ids": [
    "4.5"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Clean-move caveat is a distinct qualifier on C015/C016."
  },
  {
   "claim_id": "C019",
   "loglog_ids": [
    "5"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Generic stopping principle, not restated verbatim later."
  },
  {
   "claim_id": "C020",
   "loglog_ids": [
    "5.1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Quantitative continuation rule with figures new."
  },
  {
   "claim_id": "C021",
   "loglog_ids": [
    "5.2"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Stop-advice instance for {2,3,12} adds numbers."
  },
  {
   "claim_id": "C022",
   "loglog_ids": [
    "5.3"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Switching comparison and open-question caveat distinct."
  },
  {
   "claim_id": "C023",
   "loglog_ids": [
    "6"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Tournament headline with strategy and family counts."
  },
  {
   "claim_id": "C024",
   "loglog_ids": [
    "6.1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Adds trials-per-strategy and games-per-matchup detail."
  },
  {
   "claim_id": "C025",
   "loglog_ids": [
    "6.2"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Speed statistics for GreedyUntil1Col new here."
  },
  {
   "claim_id": "C026",
   "loglog_ids": [
    "6.3"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Champion win rate and runner-up numbers distinct."
  },
  {
   "claim_id": "C027",
   "loglog_ids": [
    "6.4"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Champion stopping formula is a distinct definition."
  },
  {
   "claim_id": "C028",
   "loglog_ids": [
    "6.5"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Speed-versus-ranking paradox adds rank and rate."
  },
  {
   "claim_id": "C029",
   "loglog_ids": [
    "6.6"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "First-player advantage figures appear only here."
  },
  {
   "claim_id": "C030",
   "loglog_ids": [
    "6.7"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Negative result plus artifact release is new information."
  },
  {
   "claim_id": "C031",
   "loglog_ids": [
    "7"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Board design context and compensation role distinct from C004."
  },
  {
   "claim_id": "C032",
   "loglog_ids": [
    "7.1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Deviation bound for integer lengths new."
  },
  {
   "claim_id": "C033",
   "loglog_ids": [
    "7.2"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Perfect-balance step counts and game length distinct."
  },
  {
   "claim_id": "C034",
   "loglog_ids": [
    "7.3"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Optimal board deviation figure and factor new."
  },
  {
   "claim_id": "C035",
   "loglog_ids": [
    "7.4"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Under-20 board and integer-design bounds new."
  },
  {
   "claim_id": "C036",
   "loglog_ids": [
    "7.5"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Practical 50% advice on columns 5-9 is new."
  }
 ],
 "metrics": {
  "scored_claims": 36,
  "unique": 35,
  "duplicates": 1,
  "trivia": 0,
  "redundancy_rate": 0.0278,
  "trivia_rate": 0.0,
  "structured_tokens": 604,
  "tokens_per_unique_claim": 17.26
 },
 "prune_list": [
  "C001 duplicates C009/C013/C026/C031; summary is a recap, safe to compress or drop"
 ]
}
```

## Judge Top (overall), opencode-go/deepseek-v4.1-flash

```json
{
 "judge": "overall",
 "judge_version": "1.0.0",
 "model": "opencode-go/deepseek-v4.1-flash, 2026-09-15",
 "source_id": "unspecified",
 "inputs": {
  "faithfulness_precision": 1.0,
  "critical_errors": 0,
  "must_recall": 0.8929,
  "overall_recall": 0.9,
  "redundancy_rate": 0.0278,
  "trivia_rate": 0.0
 },
 "weights_used": {
  "faithfulness_precision": 0.4,
  "coverage_must_recall": 0.4,
  "redundancy_penalty": 0.2
 },
 "computation": "weighted score = 0.4 * 1.0 + 0.4 * 0.8929 - 0.2 * 0.0278 = 0.4 + 0.35716 - 0.00556 = 0.7516",
 "weighted_score": 0.7516,
 "verdict": "Fail",
 "tradeoff_note": "Hard gate missed: must_recall 0.8929 falls below the 0.9 minimum, so the sample fails regardless of perfect faithfulness and low redundancy. The shortfall traces to three Must-have points (K11, K12, K15) each capped at Partial by dropped numbers, not to any contradiction.",
 "fix_list": [
  "Restore the dropped champion turn count in K11: state that FiftyPercentSurvival wins in 11.3 turns (loglog L026/L029), so the consistency-beats-speed contrast is complete.",
  "Restore the comparative anchors in K12: chess (~5%) and Go (~7%) first-player edges (loglog L030), so the 'larger than' framing is not lost.",
  "Restore the avoided-activation condition in K15: explicitly warn against forcing activation of columns 2-3 and 11-12 (loglog L037).",
  "Prune C001, which duplicates C009/C013/C026/C031; pure recap with no unique content (redundancy only 0.0278, so low leverage but harmless to compress)."
 ],
 "reasoning": "Gate checks against config pass_gates. (1) critical_contradicted_max = 0: faithfulness critical_errors = 0 and contradicted = 0, so this gate passes. (2) faithfulness_precision_min = 0.95: precision = 36/36 = 1.0, passes. (3) must_recall_min = 0.9: must_have_total = 14, must_have_present = 11, must_have_partial = 3, must_have_missing = 0; with partials at half credit, must_recall = (11 + 0.5*3)/14 = 12.5/14 = 0.8929, which is below 0.9. This is a hard gate miss and forces a Fail verdict before any weighting. (4) redundancy_max = 0.15: redundancy_rate = 1/36 = 0.0278, passes, and trivia_rate = 0.0. Because a hard gate failed, the weighted score is computed for audit only, not for ranking: 0.4*1.0 (faithfulness) + 0.4*0.8929 (must recall) - 0.2*0.0278 (redundancy penalty) = 0.4 + 0.35716 - 0.00556 = 0.7516. All three Partial Must-have points in the coverage JSON are the direct cause: K11 (loglog L026, L029) drops FiftyPercentSurvival's 11.3-turn figure, K12 (loglog L030) drops the chess ~5% and Go ~7% anchors, K15 (loglog L037) drops the avoid-forced-activation-of-columns-2-3-and-11-12 condition. Each is Partial strictly because a specific number or condition was omitted, not because the spine is wrong. No fact conflict between the aspect judges arose, so SOURCE was not reread. Concision cannot rescue this fail per the top policy, and the sole duplicate C001 offers only marginal benefit since redundancy already sits well under the max. The single highest-leverage repair is adding the 11.3-turn figure to K11, which moves must_recall from 0.8929 toward the 0.9 threshold; closing all three partials returns must_recall to 1.0 and would clear the gate assuming faithfulness holds at 1.0."
}
```
