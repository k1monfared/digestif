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
   "claim_text": "Can't Stop's four-dice probabilities and forced-move rule make it nearly balanced, and simulations show probabilistic, consistent play wins, though going first is a large advantage.",
   "claim_type": "interpretation",
   "verdict": "Partially supported",
   "severity": "Minor",
   "evidence_quote": "The game heavily favors middle columns.",
   "reasoning": "Probabilistic consistency and first-player advantage are supported, but source says combination play is badly imbalanced, not 'nearly balanced'."
  },
  {
   "claim_id": "C002",
   "loglog_ids": [
    "1"
   ],
   "claim_text": "Can't Stop has players roll four dice, pair them into sums, and advance markers on columns 2 through 12, needing three completed columns to win.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "roll four dice, pair them up however you want, move your markers on a board ... You need to complete three columns to win.",
   "reasoning": "Source states the four-dice, pairing, column and three-column win rules directly."
  },
  {
   "claim_id": "C003",
   "loglog_ids": [
    "1.1"
   ],
   "claim_text": "You can keep rolling as long as you want, but busting when no marker can move loses the turn's gains.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "you can keep rolling as long as you want, but if you can't move any of your three active markers, you lose everything you've gained that turn.",
   "reasoning": "Matches source wording on continued rolling and losing accumulated progress on bust."
  },
  {
   "claim_id": "C004",
   "loglog_ids": [
    "1.2"
   ],
   "claim_text": "Column lengths run 3, 5, 7, 9, 11, 13, 11, 9, 7, 5, and 3 steps for columns 2 through 12.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Columns 2 and 12: 3 steps ... Column 7: 13 steps",
   "reasoning": "Sequence matches the source's column length list exactly."
  },
  {
   "claim_id": "C005",
   "loglog_ids": [
    "1.3"
   ],
   "claim_text": "The forced-move rule requires taking all legal moves from a chosen pairing, even unwanted ones.",
   "claim_type": "definition",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "you must take all available moves ... you must make ALL legal moves from that pairing, even if you don't want them.",
   "reasoning": "Direct restatement of the forced-move rule."
  },
  {
   "claim_id": "C006",
   "loglog_ids": [
    "1.4"
   ],
   "claim_text": "On {6,7,8}, rolling (1,1,3,4) and pairing 2+7 forces moving both 2 and 7 as well.",
   "claim_type": "example",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "you could choose pairing (1,1)+(3,4) = 2+7. But if you do, you're forced to take BOTH the 2 and the 7",
   "reasoning": "Source gives exactly this example with the same dice and columns."
  },
  {
   "claim_id": "C007",
   "loglog_ids": [
    "1.5"
   ],
   "claim_text": "The forced-move rule prevents trivial play and adds tactical depth.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "This rule prevents the game from being trivially easy and adds tactical depth.",
   "reasoning": "Near-verbatim restatement of source conclusion."
  },
  {
   "claim_id": "C008",
   "loglog_ids": [
    "1.6"
   ],
   "claim_text": "An interactive web version exists with a Python/FastAPI backend and React frontend.",
   "claim_type": "evidence",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "I've implemented a fully interactive web version of the game with a Python/FastAPI backend and React frontend.",
   "reasoning": "Directly stated in the source."
  },
  {
   "claim_id": "C009",
   "loglog_ids": [
    "2"
   ],
   "claim_text": "Four dice flatten the distribution: P(7) rises to 64.4% and P(2) to 13.2%, far closer together than with two dice.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "P(7) = 64.4% vs P(2) = 13.2%, only a 4.88× difference compared to 6× with two dice",
   "reasoning": "Numbers match the source's four-dice flattening claim."
  },
  {
   "claim_id": "C010",
   "loglog_ids": [
    "2.1"
   ],
   "claim_text": "With two dice, sum 7 is most likely at 16.67% and exactly 6× more likely than sum 2 at 2.78%.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Sum 7 is the most likely at 16.67%, and it's exactly 6× more likely than sum 2 at 2.78%.",
   "reasoning": "Exact restatement of source values."
  },
  {
   "claim_id": "C011",
   "loglog_ids": [
    "2.1.1"
   ],
   "claim_text": "Sum 2 requires both dice showing 1 (1/36); sum 7 has 6 order-sensitive ways: (1,6), (2,5), (3,4).",
   "claim_type": "evidence",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "both dice must show 1. That's 1/6 × 1/6 = 1/36 ... complementary pairs: (1,6), (2,5), or (3,4), and order matters, so that's 6 ways",
   "reasoning": "Matches the source proof exactly."
  },
  {
   "claim_id": "C012",
   "loglog_ids": [
    "2.2"
   ],
   "claim_text": "If Can't Stop used two dice, column 7 would need to be 6× longer than column 2, but it is only 13/3 ≈ 4.3×.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "column 7 would need to be 6× longer than column 2 to be equally hard. Instead it's only 13/3 ≈ 4.3× longer.",
   "reasoning": "Values and framing match the source."
  },
  {
   "claim_id": "C013",
   "loglog_ids": [
    "2.3"
   ],
   "claim_text": "Rolling 2, 3, 4, 5 gives just three pairings: 5 and 9, 6 and 8, or 7 and 7.",
   "claim_type": "example",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "(2,3)+(4,5) = 5 and 9 ... (2,4)+(3,5) = 6 and 8 ... (2,5)+(3,4) = 7 and 7",
   "reasoning": "Exact list from the source."
  },
  {
   "claim_id": "C014",
   "loglog_ids": [
    "2.4"
   ],
   "claim_text": "Four dice give P(can make a 2) = 171/1296 ≈ 13.2%, requiring at least two 1s among the four.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "P(can make a 2) = 1 - 625/1296 - 500/1296 = 171/1296 ≈ 13.2%",
   "reasoning": "Fraction and percentage match the source calculation."
  },
  {
   "claim_id": "C015",
   "loglog_ids": [
    "2.4.1"
   ],
   "claim_text": "P(zero 1s) = 625/1296 and P(exactly one 1) = 500/1296, so P(can make 2) = 1 - 625/1296 - 500/1296.",
   "claim_type": "evidence",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "P(zero 1's) = (5/6)^4 = 625/1296 ... P(exactly one 1) = ... = 500/1296",
   "reasoning": "Intermediate probabilities match the source exactly."
  },
  {
   "claim_id": "C016",
   "loglog_ids": [
    "2.5"
   ],
   "claim_text": "Four dice give P(can make a 7) = 834/1296 ≈ 64.4%, via inclusion-exclusion over pairs (1,6), (2,5), (3,4).",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "P(can make a 7) = P(A ∪ B ∪ C) = 302 + 302 + 302 - 24 - 24 - 24 + 0 = 834/1296 ≈ 64.4%",
   "reasoning": "Result and method match the source."
  },
  {
   "claim_id": "C017",
   "loglog_ids": [
    "2.5.1"
   ],
   "claim_text": "Each pair event has probability 302/1296, each pairwise overlap 24/1296, and the triple overlap is 0.",
   "claim_type": "evidence",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "P(B) = 302/1296 and P(C) = 302/1296 ... = 24/1296 ... P(A ∩ B ∩ C) = 0",
   "reasoning": "All three component values match the source."
  },
  {
   "claim_id": "C018",
   "loglog_ids": [
    "2.5.2"
   ],
   "claim_text": "Final sum: 302 + 302 + 302 - 24 - 24 - 24 + 0 = 834/1296 ≈ 64.4%.",
   "claim_type": "evidence",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "= 302 + 302 + 302 - 24 - 24 - 24 + 0 = 834/1296 ≈ 64.4%",
   "reasoning": "Exact arithmetic restatement from source."
  },
  {
   "claim_id": "C019",
   "loglog_ids": [
    "2.6"
   ],
   "claim_text": "The full four-dice table shows at-least-one-pair counts from 171 (13.2%) for sum 2 up to 834 (64.4%) for sum 7.",
   "claim_type": "evidence",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "| 2 | 171 (13.2%) ... | 7 | 834 (64.4%)",
   "reasoning": "Table endpoints match the source table."
  },
  {
   "claim_id": "C020",
   "loglog_ids": [
    "2.7"
   ],
   "claim_text": "The probability ratio from column 2 to 7 is 4.88 against a length ratio of 4.33, close enough to suggest deliberate design.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "The probability ratio from 2 to 7 is 4.88. The length ratio is 4.33. Pretty close! The game designers were definitely thinking about this.",
   "reasoning": "Ratios and design inference match the source."
  },
  {
   "claim_id": "C021",
   "loglog_ids": [
    "2.8"
   ],
   "claim_text": "The conclusion restates this: four-dice probabilities flatten the distribution, with P(7) = 64.4% versus P(2) = 13.2%, only a 4.88× difference.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Four-dice probabilities flatten the distribution - P(7) = 64.4% vs P(2) = 13.2%, only a 4.88× difference",
   "reasoning": "Matches the source conclusion item verbatim."
  },
  {
   "claim_id": "C022",
   "loglog_ids": [
    "3"
   ],
   "claim_text": "Single columns are nearly balanced: expected rolls stay between 19.60 and 22.73 across all columns.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "| 6, 8 | 11 | 56.1% | 19.60 | ... | 2, 12 | 3 | 13.2% | 22.73 |",
   "reasoning": "Min and max of the source table match the stated range."
  },
  {
   "claim_id": "C023",
   "loglog_ids": [
    "3.1"
   ],
   "claim_text": "Expected rolls equal length over probability: column 2 needs 3/0.132 = 22.73 rolls; column 7 needs 13/0.644 = 20.18.",
   "claim_type": "evidence",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "For column 2: 3/0.132 = 22.73 rolls, For column 7: 13/0.644 = 20.18 rolls",
   "reasoning": "Formula and values match the source."
  },
  {
   "claim_id": "C024",
   "loglog_ids": [
    "3.2"
   ],
   "claim_text": "Column 7 is slightly faster than column 2 even though it is 4× longer.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Column 7 is slightly faster, even though it's 4× longer.",
   "reasoning": "Near-verbatim source statement."
  },
  {
   "claim_id": "C025",
   "loglog_ids": [
    "3.3"
   ],
   "claim_text": "Expected rolls by column: 22.73 (2/12), 21.46 (3/11), 19.67 (4/10), 20.09 (5/9), 19.60 (6/8), 20.18 (7).",
   "claim_type": "evidence",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "| 2, 12 | 3 | 13.2% | 22.73 | ... | 7 | 13 | 64.4% | 20.18 |",
   "reasoning": "All listed values match the source table."
  },
  {
   "claim_id": "C026",
   "loglog_ids": [
    "3.4"
   ],
   "claim_text": "Columns 2 and 12 require the most rolls; columns 6, 7, and 8 cluster near 20.",
   "claim_type": "evidence",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Columns 2 and 12 require the most rolls. Columns 6, 7, and 8 are all close to each other around 20 rolls.",
   "reasoning": "Direct restatement of source observation."
  },
  {
   "claim_id": "C027",
   "loglog_ids": [
    "3.5"
   ],
   "claim_text": "Column 2 is only 3 steps but hit 13.2% of the time; column 7 is 13 steps but hit 64.4% of the time.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "column 2 is only 3 steps ... you'll only hit it 13.2% of the time. Column 7 is 13 steps but you hit it 64.4% of the time.",
   "reasoning": "Steps and percentages match the source."
  },
  {
   "claim_id": "C028",
   "loglog_ids": [
    "4"
   ],
   "claim_text": "{6,7,8} succeeds 92.0% of the time while {2,3,12} succeeds only 43.8%.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "Result: 1193/1296 = 92.0% success rate ... Result: 568/1296 = 43.8% success rate",
   "reasoning": "SOURCE states both success percentages exactly for the same two combinations."
  },
  {
   "claim_id": "C029",
   "loglog_ids": [
    "4.1"
   ],
   "claim_text": "{6,7,8} succeeds on 1193/1296 rolls; {2,3,12} on 568/1296, less than half.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "1193/1296 = 92.0% success rate ... 568/1296 = 43.8% success rate ... Less than 50% chance of not busting",
   "reasoning": "Counts and the less-than-half qualifier match SOURCE exactly."
  },
  {
   "claim_id": "C030",
   "loglog_ids": [
    "4.2"
   ],
   "claim_text": "Across all 165 combinations, 37 are excellent at ≥85% success, the median is 79.6%, and the worst fall to 43.8%.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "37 combinations are \"excellent\" (≥85% success rate) ... median combination still succeeds 79.6% ... worst combinations drop ... to just 43.8%",
   "reasoning": "All four figures (165, 37, 79.6%, 43.8%) appear verbatim in SOURCE."
  },
  {
   "claim_id": "C031",
   "loglog_ids": [
    "4.3"
   ],
   "claim_text": "The best combination, {6,7,8}, has 92.0% success, 8.0% bust, 39.8% clean moves, and Q = 1.43.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "| 1 | {6,7,8} | 92.0% | 8.0% | 39.8% | 1.43 |",
   "reasoning": "Every value matches the top table row for {6,7,8} in SOURCE."
  },
  {
   "claim_id": "C032",
   "loglog_ids": [
    "4.4"
   ],
   "claim_text": "The worst, {2,11,12}, has 43.8% success, 56.2% bust, 2.3% clean moves, and Q = 1.05.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "| 165 | {2,11,12} | 43.8% | 56.2% | 2.3% | 1.05 |",
   "reasoning": "All four values match the rank-165 row for {2,11,12} in SOURCE."
  },
  {
   "claim_id": "C033",
   "loglog_ids": [
    "4.5"
   ],
   "claim_text": "A 'clean' move hits only wanted columns; even {6,7,8} is clean only 39.8% of the time.",
   "claim_type": "definition",
   "verdict": "Supported",
   "severity": "Minor",
   "evidence_quote": "A \"clean\" move is one where you only hit columns you actually want. Even the best combination {6,7,8} only has 39.8% clean moves",
   "reasoning": "Definition and the 39.8% figure match SOURCE verbatim."
  },
  {
   "claim_id": "C034",
   "loglog_ids": [
    "4.6"
   ],
   "claim_text": "52.2% of {6,7,8} rolls force unwanted columns, and only 2.3% of {2,3,12} rolls are clean.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "The other 52.2% of rolls ... force you onto unwanted columns ... For {2,3,12}: Only 2.3% of rolls are clean!",
   "reasoning": "Both percentages correspond exactly to SOURCE statements for those combinations."
  },
  {
   "claim_id": "C035",
   "loglog_ids": [
    "4.7"
   ],
   "claim_text": "The forced-move rule is a balancing mechanism preventing {6,7,8} from being completely dominant, and is the design's compensating rule.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Minor",
   "evidence_quote": "The forced-move rule is a balancing mechanism. It prevents {6,7,8} from being completely dominant ... It compensates for mathematical imbalances",
   "reasoning": "Both the balancing claim and compensating-rule framing are stated in SOURCE."
  },
  {
   "claim_id": "C036",
   "loglog_ids": [
    "4.8"
   ],
   "claim_text": "The conclusion restates: column combinations matter more than individual columns, {6,7,8} at 92% success and {2,3,12} at 44%.",
   "claim_type": "meta",
   "verdict": "Supported",
   "severity": "Minor",
   "evidence_quote": "Column combinations matter more than individual columns** - {6,7,8} has 92% success rate, {2,3,12} has 44%",
   "reasoning": "SOURCE conclusion states this point with the same rounded percentages."
  },
  {
   "claim_id": "C037",
   "loglog_ids": [
    "5"
   ],
   "claim_text": "The stopping rule is EV-based: keep rolling if P(success) × Q exceeds P(bust) × U.",
   "claim_type": "definition",
   "verdict": "Supported",
   "severity": "Minor",
   "evidence_quote": "**Keep rolling if:** $(P_{\\text{success}} \\times Q) > (P_{\\text{bust}} \\times U)$",
   "reasoning": "The inequality and its variable meanings match SOURCE exactly."
  },
  {
   "claim_id": "C038",
   "loglog_ids": [
    "5.1"
   ],
   "claim_text": "For {6,7,8} with 5 unsaved steps: loss 0.08 × 5 = 0.4 versus gain 0.92 × 1.43 = 1.32, so keep rolling.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "Expected loss: $0.08 \\times 5 = 0.4$ steps ... Expected gain: $0.92 \\times 1.43 = 1.32$ steps ... Since $1.32 > 0.4$, you should keep rolling.",
   "reasoning": "Inputs, products, and the keep-rolling conclusion match SOURCE arithmetic."
  },
  {
   "claim_id": "C039",
   "loglog_ids": [
    "5.2"
   ],
   "claim_text": "For {2,3,12} with 2 unsaved steps: loss 0.562 × 2 = 1.12 versus gain 0.438 × 1.05 = 0.46, so stop.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "**Risk:** $0.562 \\times 2 = 1.12$ steps ... **Expected gain:** $0.438 \\times 1.05 = 0.46$ steps ... Since $1.12 > 0.46$, you should STOP.",
   "reasoning": "All values and the stop conclusion match SOURCE exactly."
  },
  {
   "claim_id": "C040",
   "loglog_ids": [
    "5.3"
   ],
   "claim_text": "Q is expected markers advanced on a successful roll; U is unsaved progress lost on a bust.",
   "claim_type": "definition",
   "verdict": "Supported",
   "severity": "Minor",
   "evidence_quote": "$Q$ = expected number of markers you'll advance on a successful roll ... $U$ = unsaved progress (steps you'd lose if you bust)",
   "reasoning": "Both variable definitions match SOURCE wording."
  },
  {
   "claim_id": "C041",
   "loglog_ids": [
    "6"
   ],
   "claim_text": "Simulations of 38 strategies across 14 families (3.6 million games) show probabilistic play winning and consistency beating speed.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "I tested 38 strategies across 14 different strategic families (¶48); 3.6 million total games (¶47); Probabilistic strategies dominate (¶77); consistency beats raw speed (¶70)",
   "reasoning": "SOURCE states all three components: 38 strategies, 14 families, 3.6M games, probabilistic dominance, consistency over speed."
  },
  {
   "claim_id": "C042",
   "loglog_ids": [
    "6.1"
   ],
   "claim_text": "Single-player, GreedyUntil1Col is fastest at 10.5 turns but has sigma = 5.73 and 7.50 busts per game.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "GreedyUntil1Col is fastest (10.5 turns) but has high variance (σ=5.73) and bust rate (7.5 per game) (¶54); table 7.50 (¶53)",
   "reasoning": "All figures 10.5, 5.73, 7.50 match SOURCE table and key insights."
  },
  {
   "claim_id": "C043",
   "loglog_ids": [
    "6.2"
   ],
   "claim_text": "FiftyPercentSurvival is second at 11.3 turns with sigma = 2.86 and only 2.67 busts per game.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "FiftyPercentSurvival balances speed with remarkable consistency (σ=2.86, only 2.67 busts) (¶54); rank 2, 11.3 (¶53)",
   "reasoning": "Rank 2, 11.3 turns, σ=2.86, 2.67 busts all match SOURCE."
  },
  {
   "claim_id": "C044",
   "loglog_ids": [
    "6.3"
   ],
   "claim_text": "Head-to-head, FiftyPercentSurvival wins 69.84% (132,696/190,000), then Heuristic(1.5) 66.46% and Heuristic(2.0) 63.26%.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "FiftyPercentSurvival 69.84% 132,696/190,000; Heuristic(1.5) 66.46%; Heuristic(2.0) 63.26% (¶57)",
   "reasoning": "All percentages and counts match the head-to-head table."
  },
  {
   "claim_id": "C045",
   "loglog_ids": [
    "6.4"
   ],
   "claim_text": "The champion rolls until cumulative survival probability drops below 50%, with n = log(0.5)/log(P_success).",
   "claim_type": "definition",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Roll until cumulative survival probability drops below 50%, calculated as n = log(0.5) / log(P_success) (¶60)",
   "reasoning": "Direct restatement of SOURCE strategy definition with identical formula."
  },
  {
   "claim_id": "C046",
   "loglog_ids": [
    "6.5"
   ],
   "claim_text": "It wins through sound probability math, balanced risk, speed and consistency (sigma = 2.86), and only +9.42% position bias.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Mathematically sound... Optimal risk tolerance... Low variance, σ of 2.86... Moderate position bias - +9.42% (¶61)",
   "reasoning": "All five listed reasons match SOURCE points, including σ=2.86 and +9.42%."
  },
  {
   "claim_id": "C047",
   "loglog_ids": [
    "6.6"
   ],
   "claim_text": "Its favorite columns are middle ones: most completed 8 (42.0%), 7 (38.4%), 6 (37.7%).",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Most completed: Column 8 (42.0%), Column 7 (38.4%), Column 6 (37.7%) (¶62)",
   "reasoning": "Percentages and column ordering match SOURCE exactly."
  },
  {
   "claim_id": "C048",
   "loglog_ids": [
    "6.7"
   ],
   "claim_text": "Key matchups: 55.22% vs GreedyUntil1Col, 54.38% vs Heuristic(1.5), 63.09% vs MonteCarloLookahead, 50.00% in self-play.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "vs GreedyUntil1Col: 55.22%; vs Heuristic(1.5): 54.38%; vs MonteCarloLookahead: 63.09%; vs itself: 50.00% (¶63)",
   "reasoning": "All four matchup percentages match SOURCE exactly."
  },
  {
   "claim_id": "C049",
   "loglog_ids": [
    "6.8"
   ],
   "claim_text": "GreedyUntil1Col finishes in 10.5 turns but wins only 58.90%, while FiftyPercentSurvival takes 0.8 turns longer and wins 10.9% more.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "only achieves 58.90% competitive win rate (¶68); takes 0.8 turns longer but wins 10.9% more games (¶69)",
   "reasoning": "58.90%, 0.8 turns, and 10.9% all match SOURCE."
  },
  {
   "claim_id": "C050",
   "loglog_ids": [
    "6.8.1"
   ],
   "claim_text": "The fastest strategy is not the best competitive strategy.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "the fastest strategy is not the best competitive strategy (¶66)",
   "reasoning": "Verbatim match to SOURCE."
  },
  {
   "claim_id": "C051",
   "loglog_ids": [
    "6.9"
   ],
   "claim_text": "Core families: Greedy and Random (30% stop), Conservative(k) with k in {1,2,3,4}, Heuristic(alpha) with alpha in {0.3,0.5,1.0,1.5,2.0}, and OpponentAware variants.",
   "claim_type": "definition",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Greedy (always rolls) and Random (30% stop probability); Conservative(k) k ∈ {1,2,3,4}; Heuristic(α) α ∈ {0.3,0.5,1.0,1.5,2.0}; OpponentAware... four variants (¶49)",
   "reasoning": "Family names and parameter sets match SOURCE exactly."
  },
  {
   "claim_id": "C052",
   "loglog_ids": [
    "6.10"
   ],
   "claim_text": "Other core types: Greedy-Improved, Adaptive, Proportional, progressive milestones, probabilistic, and column-count strategies.",
   "claim_type": "definition",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "5. Greedy-Improved... 6. Adaptive... 7. Proportional... 8. Progressive Milestones... 9. Probabilistic... 10. Column-Count (¶50)",
   "reasoning": "All six listed family names match SOURCE groups 5-10."
  },
  {
   "claim_id": "C053",
   "loglog_ids": [
    "6.11"
   ],
   "claim_text": "Newer groups 11-14 cover outside/middle preference, runner-aware, column-quality, and hybrid/advanced strategies.",
   "claim_type": "definition",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "New Strategy Types (Groups 11-14): 11. Outside/Middle Preference... 12. Runner-Aware... 13. Column-Quality... 14. Hybrid/Advanced (¶51)",
   "reasoning": "Groups 11-14 labels match SOURCE exactly."
  },
  {
   "claim_id": "C054",
   "loglog_ids": [
    "6.12"
   ],
   "claim_text": "RiskBudget caps cumulative bust risk at 20% per turn; MonteCarloLookahead simulates 100 future rolls.",
   "claim_type": "definition",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "RiskBudget (20% cumulative bust limit per turn), and MonteCarloLookahead (simulates 100 future rolls (¶51)",
   "reasoning": "20% cap and 100 rolls match SOURCE definitions."
  },
  {
   "claim_id": "C055",
   "loglog_ids": [
    "6.13"
   ],
   "claim_text": "The top 15 all finish in 10.5 to 12.8 turns; conservative strategies like Heuristic(2.0) average under 1 bust per game.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Conservative strategies like Heuristic(2.0) and MonteCarloLookahead average <1 bust per game; The top 15 all complete games in 10.5-12.8 turns (¶54)",
   "reasoning": "Range 10.5-12.8 and <1 bust statement match SOURCE."
  },
  {
   "claim_id": "C056",
   "loglog_ids": [
    "6.14"
   ],
   "claim_text": "A full head-to-head win-rate matrix and a downloadable CSV accompany the rankings.",
   "claim_type": "meta",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Here's the complete head-to-head win-rate matrix... [Download full CSV] (¶64)",
   "reasoning": "SOURCE provides the matrix and a CSV download link."
  },
  {
   "claim_id": "C057",
   "loglog_ids": [
    "6.15"
   ],
   "claim_text": "Probabilistic strategies dominate: the top 7 all use probability calculations, and pure Greedy lost essentially every game.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "The top 7 strategies ALL use mathematical probability calculations... The pure Greedy strategy (never stop voluntarily) lost essentially every game (¶77)",
   "reasoning": "Both statements match SOURCE verbatim."
  },
  {
   "claim_id": "C058",
   "loglog_ids": [
    "6.16"
   ],
   "claim_text": "MonteCarloLookahead, simulating 100 future rolls, only places 4th at 63.09%, so simpler rules are near-optimal.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Despite simulating 100 future rolls per decision... MonteCarloLookahead only places 4th (63.09%)... suggesting we've found near-optimal play (¶78)",
   "reasoning": "100 rolls, 4th place, 63.09%, and near-optimal inference all match SOURCE."
  },
  {
   "claim_id": "C059",
   "loglog_ids": [
    "6.17"
   ],
   "claim_text": "Opponent-aware variants all underperformed simple thresholds because they only looked at completed columns, not partial progress.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "All three performed worse than simple threshold strategies. The problem? They only looked at completed columns, not partial progress (¶78)",
   "reasoning": "The underperformance and stated reason match SOURCE exactly."
  },
  {
   "claim_id": "C060",
   "loglog_ids": [
    "6.18"
   ],
   "claim_text": "For players: use FiftyPercentSurvival, aim for columns 5-9, avoid forced activation of 2-3 and 11-12, and prioritize consistency.",
   "claim_type": "recommendation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Use the FiftyPercentSurvival strategy... Aim for columns 5-9, avoid forcing activation of columns 2-3 and 11-12, and prioritize consistency (¶100)",
   "reasoning": "Recommendation matches SOURCE player advice verbatim."
  },
  {
   "claim_id": "C061",
   "loglog_ids": [
    "6.19"
   ],
   "claim_text": "For probability nerds: near-optimal play sits near 70% win rate; breaking the 75% barrier remains an open question.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "we've found near-optimal play at ~70% win rate. The question is whether any strategy can break the 75% barrier (¶101)",
   "reasoning": "~70% and the 75% barrier question match SOURCE."
  },
  {
   "claim_id": "C062",
   "loglog_ids": [
    "6.20"
   ],
   "claim_text": "The conclusion restates this: probabilistic strategies dominate, with FiftyPercentSurvival's 69.84% win rate beating even Monte Carlo 'perfect play'.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Probabilistic strategies dominate - The champion strategy (FiftyPercentSurvival, 69.84% win rate)... beating even \"perfect play\" Monte Carlo simulation (¶97)",
   "reasoning": "Conclusion point 3 matches SOURCE exactly."
  },
  {
   "claim_id": "C063",
   "loglog_ids": [
    "6.21"
   ],
   "claim_text": "The conclusion restates this: consistency beats speed, since finishing in 11 turns reliably outperforms averaging 10.5 with high variance.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Consistency beats speed - Finishing in 11 turns reliably outperforms averaging 10.5 turns with high variance (¶97)",
   "reasoning": "Conclusion point 4 matches SOURCE verbatim."
  },
  {
   "claim_id": "C064",
   "loglog_ids": [
    "7"
   ],
   "claim_text": "Simulations revealed a significant first-player advantage: Player 1 wins 55.59%, +11.18%, larger than chess (~5%) or Go (~7%).",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Player 1 win rate: 55.59%... First-player advantage: +11.18% (¶71); larger than chess (~5%) or Go (~7%) (¶72)",
   "reasoning": "All figures 55.59%, +11.18%, ~5%, ~7% match SOURCE."
  },
  {
   "claim_id": "C065",
   "loglog_ids": [
    "7.1"
   ],
   "claim_text": "Going first likely helps via first access to middle columns 6-8, setting the pace, and initiative in column selection.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "likely due to: 1. First access to middle columns (6-8) 2. Setting the pace... 3. Initiative in column selection (¶72)",
   "reasoning": "All three proposed reasons match SOURCE and retain the hedge likely."
  },
  {
   "claim_id": "C066",
   "loglog_ids": [
    "7.2"
   ],
   "claim_text": "GreedyUntil1Col (+31.24%) and GreedyFraction(0.5) (+31.00%) show severe position bias; OpponentAware(0.3,1,2) is high at +18.94%.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "GreedyUntil1Col +31.24% SEVERE bias; GreedyFraction(0.5) +31.00% SEVERE bias; OpponentAware(0.3,1,2) +18.94% High bias (¶73)",
   "reasoning": "All three percentages and bias labels match SOURCE table."
  },
  {
   "claim_id": "C067",
   "loglog_ids": [
    "7.3"
   ],
   "claim_text": "Fairest: OpponentAware(2,1,0.3) at -4.14% favors P2, Greedy -0.03%, Heuristic(0.3) +0.65%, Heuristic(0.5) +3.30%.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "OpponentAware(2,1,0.3) -4.14%; Greedy -0.03%; Heuristic(0.3) +0.65%; Heuristic(0.5) +3.30% (¶74)",
   "reasoning": "All four values and the P2 interpretation match SOURCE table."
  },
  {
   "claim_id": "C068",
   "loglog_ids": [
    "7.4"
   ],
   "claim_text": "High position bias may overrate strategies like GreedyUntil1Col in aggregate statistics.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Strategies with high position bias (like GreedyUntil1Col) may be overrated in aggregate statistics (¶75)",
   "reasoning": "Verbatim match, including the hedge may."
  },
  {
   "claim_id": "C069",
   "loglog_ids": [
    "7.5"
   ],
   "claim_text": "The 'opposite' OpponentAware, conservative when behind, performs better as Player 2, suggesting catching up rewards patience.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "The \"opposite\" OpponentAware strategy (conservative when behind, aggressive when ahead) actually performs better as Player 2, suggesting that catching up rewards patience (¶75)",
   "reasoning": "Matches SOURCE description and stated suggestion exactly."
  },
  {
   "claim_id": "C070",
   "loglog_ids": [
    "7.6"
   ],
   "claim_text": "GreedyUntil1Col wins 73% as P1 but only 42% as P2, with sigma = 5.73 and 7.5 busts per game.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "High variance (σ=5.73)... Extreme bust rate (7.5 per game)... Wins 73% as P1, only 42% as P2 (¶68)",
   "reasoning": "All figures 73%, 42%, 5.73, 7.5 match SOURCE."
  },
  {
   "claim_id": "C071",
   "loglog_ids": [
    "7.7"
   ],
   "claim_text": "The conclusion restates this: the first-player advantage is significant, Player 1 winning 55.59% (+11.18%), larger than chess or Go.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "First-player advantage is significant - Player 1 wins 55.59% of games (+11.18% advantage), larger than chess or Go (¶98)",
   "reasoning": "Conclusion point 5 matches SOURCE exactly."
  },
  {
   "claim_id": "C072",
   "loglog_ids": [
    "8"
   ],
   "claim_text": "The designers balanced individual columns but not combinations; the forced-move rule compensates, and better boards exist.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "The designers DID balance individual column completion times, but they couldn't (or didn't want to) balance the three-column combinations.",
   "reasoning": "Source states individual columns balanced, combinations not, forced-move compensates, and optimization shows better boards exist."
  },
  {
   "claim_id": "C073",
   "loglog_ids": [
    "8.1"
   ],
   "claim_text": "Single-column deviations from 20 expected rolls are at most ±13.6% on the current board, good given integer lengths.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "The deviations are ±13.6% at most. That's pretty good given that lengths must be integers!",
   "reasoning": "Source states identical figure ±13.6% and same justification about integer lengths."
  },
  {
   "claim_id": "C074",
   "loglog_ids": [
    "8.2"
   ],
   "claim_text": "In multi-column play, column 7 in {6,7,8} completes in about 2 turns while column 2 in {2,3,12} takes about 30.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "- Column 7 in {6,7,8}: expected completion in ~2 turns\n- Column 2 in {2,3,12}: expected completion in ~30 turns",
   "reasoning": "Source gives same approximations, ~2 turns and ~30 turns, for the same column sets."
  },
  {
   "claim_id": "C075",
   "loglog_ids": [
    "8.3"
   ],
   "claim_text": "Design constraints were simplicity (the 3-5-7-9-11-13 board), 1980 manufacturability, and emotional engagement from visual length.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "1. **Simple enough to understand** - The current board (3-5-7-9-11-13)... 2. **Physically manufacturable**... 3. **Engaging to a broad audience** - The visual length creates emotional investment",
   "reasoning": "Source lists the same three constraints with matching board and 1980 context."
  },
  {
   "claim_id": "C076",
   "loglog_ids": [
    "8.4"
   ],
   "claim_text": "The forced-move rule compensates by forcing sub-optimal columns, preventing all-{6,7,8} play, and adding tactical complexity.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "Forces players into sub-optimal column combinations - Prevents the game from devolving into \"everyone only picks {6,7,8}\" - Adds tactical complexity",
   "reasoning": "Source lists these exact effects of the forced-move rule."
  },
  {
   "claim_id": "C077",
   "loglog_ids": [
    "8.5"
   ],
   "claim_text": "Perfect balance needs lengths as exact multiples of probability: 171 steps for columns 2/12 and 834 for column 7, about 8 hours per game.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "- Column 2/12: 171 steps\n- Column 7: 834 steps\n\nGame duration: ~8 hours.",
   "reasoning": "Source states identical numbers 171, 834, and ~8 hours."
  },
  {
   "claim_id": "C078",
   "loglog_ids": [
    "8.6"
   ],
   "claim_text": "The current board has maximum height 13 steps and maximum deviation ±13.6%.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "**Current board:**\n- Max height: 13 steps\n- Max deviation: ±13.6%",
   "reasoning": "Source gives identical figures for the current board."
  },
  {
   "claim_id": "C079",
   "loglog_ids": [
    "8.7"
   ],
   "claim_text": "A board one step higher per column (max 14) cuts maximum deviation to ±3.09%, 4× more balanced.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "- Max height: 14 steps\n- Max deviation: ±3.09%\n- **4× more balanced with just +1 step!**",
   "reasoning": "Source states same height 14, deviation ±3.09%, and 4× claim."
  },
  {
   "claim_id": "C080",
   "loglog_ids": [
    "8.8"
   ],
   "claim_text": "A 20-step board gives lengths [4,7,11,14,17,20,17,14,11,7,4] and maximum deviation ±2.17%, a 6× improvement.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "- Max height: 20 steps\n- Max deviation: ±2.17%\n- Lengths: [4, 7, 11, 14, 17, 20, 17, 14, 11, 7, 4]\n- **6× improvement in balance**",
   "reasoning": "Source gives identical lengths, deviation ±2.17%, and 6× improvement."
  },
  {
   "claim_id": "C081",
   "loglog_ids": [
    "8.9"
   ],
   "claim_text": "The designers likely kept the current board for round numbers, intentional tension, 1980 testing limits, and player psychology.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "1. **Round numbers**... 2. **Intentional imbalance** - Maybe they wanted strategic tension 3. **Testing limitations** - In 1980... 4. **Player psychology**",
   "reasoning": "Source lists the same four likely reasons for the designers' choice."
  },
  {
   "claim_id": "C082",
   "loglog_ids": [
    "8.10"
   ],
   "claim_text": "The current lengths rise by 2 steps; a linear step=2.25 design gives ±3.09%, 3.2× better balance with +1 step.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "columns increase by exactly 2 steps each time... **Best linear design with similar size (step=2.25):**... Max deviation: ±3.09%... **3.2× better balance with just +1 step!**",
   "reasoning": "Source states step of 2, step=2.25 design, ±3.09%, and 3.2× with +1 step."
  },
  {
   "claim_id": "C083",
   "loglog_ids": [
    "8.11"
   ],
   "claim_text": "An integer linear design (base=5, step=4) yields lengths 5 to 25 and ±3.32% deviation, keeping odd, manufacturable numbers.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "**Best with integer step (base=5, step=4):**\n- Lengths: [5, 9, 13, 17, 21, 25, ...]\n- Max deviation: ±3.32%\n- Maintains aesthetic appeal (all odd numbers, easy to manufacture)",
   "reasoning": "Source gives same base/step, length range 5-25, ±3.32%, and odd/manufacturable note."
  },
  {
   "claim_id": "C084",
   "loglog_ids": [
    "8.12"
   ],
   "claim_text": "Linear designs can never achieve perfect balance because the probability curve is nonlinear.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "Linear designs can never achieve perfect balance because the probability curve is nonlinear",
   "reasoning": "Source states this verbatim, including the 'never' negation."
  },
  {
   "claim_id": "C085",
   "loglog_ids": [
    "8.13"
   ],
   "claim_text": "The author would seriously consider the 20-step board for a modern Can't Stop 2.0.",
   "claim_type": "recommendation",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "For a modern Can't Stop 2.0, I'd seriously consider the 20-step board.",
   "reasoning": "Source states this recommendation verbatim."
  },
  {
   "claim_id": "C086",
   "loglog_ids": [
    "8.14"
   ],
   "claim_text": "For designers: prioritize playability over mathematical perfection, compensate imbalances with rules, and consider turn-order handicaps.",
   "claim_type": "recommendation",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "**For game designers:** Prioritize playability over mathematical perfection, then use rules to compensate for inevitable imbalances... consider handicap systems for competitive play.",
   "reasoning": "Source gives the same three designer recommendations."
  },
  {
   "claim_id": "C087",
   "loglog_ids": [
    "8.15"
   ],
   "claim_text": "The conclusion restates this: perfect balance isn't necessary, as the game is engaging despite (or because of) favoring middle columns.",
   "claim_type": "claim",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "7. **Perfect balance isn't necessary** - The game is engaging despite (or because of) favoring middle columns",
   "reasoning": "Source conclusion item matches the claim nearly verbatim."
  },
  {
   "claim_id": "C088",
   "loglog_ids": [
    "9"
   ],
   "claim_text": "Continuation versus switching depends on progress: the math favors continuing, but forced-move contamination can force strategic switches.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "The mathematics favor continuation in most cases... However, the forced-move rule gradually contaminates good combinations over time, sometimes forcing strategic switches.",
   "reasoning": "Source states math favors continuing and contamination can sometimes force switches, hedge preserved."
  },
  {
   "claim_id": "C089",
   "loglog_ids": [
    "9.1"
   ],
   "claim_text": "With columns nearly complete (e.g., 10/11 steps) continuing makes sense; with 2-3 steps, switching might be faster.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "if columns are nearly complete (e.g., 10/11 steps), continuing makes sense. But with minimal progress (2-3 steps), switching to a better combination might be faster.",
   "reasoning": "Source gives identical step thresholds and same hedged wording."
  },
  {
   "claim_id": "C090",
   "loglog_ids": [
    "9.2"
   ],
   "claim_text": "The author has not analyzed this quantitatively; comparing 'always continue' versus 'switch when X' is left open.",
   "claim_type": "meta",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "**Note:** I haven't fully analyzed this aspect quantitatively... simulating \"always continue\" vs \"switch when X\" strategies... is an interesting open question",
   "reasoning": "Source explicitly says not fully analyzed and frames it as open future work."
  },
  {
   "claim_id": "C091",
   "loglog_ids": [
    "10"
   ],
   "claim_text": "All analysis code and simulation data are linked: probability, column-combination, strategy, and design scripts plus results.",
   "claim_type": "meta",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "All analysis code and simulation results are available",
   "reasoning": "Source links scripts across probability, column-combination, strategy, design, and results sections."
  }
 ],
 "metrics": {
  "total_claims": 91,
  "supported": 90,
  "partially_supported": 1,
  "unverifiable": 0,
  "contradicted": 0,
  "critical_errors": 0,
  "faithfulness_precision": 0.989
 },
 "fail_list": [
  "C001"
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
    "L088"
   ],
   "evidence_quote": "perfect balance isn't necessary, as the game is engaging despite (or because of) favoring middle columns",
   "reasoning": "Summary L002 and conclusion L088 both capture the thesis that near-balance is acceptable and rules compensate. The forced-move rule as compensating mechanism is stated at L036/L077."
  },
  {
   "point_id": "K02",
   "point_text": "Game rules: roll four dice, pair them to move markers on columns 2 through 12, need three completed columns to win; column lengths are 3,5,7,9,11,13,11,9,7,5,3.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L003",
    "L005"
   ],
   "evidence_quote": "Column lengths run 3, 5, 7, 9, 11, 13, 11, 9, 7, 5, and 3 steps for columns 2 through 12.",
   "reasoning": "L003 states roll four dice, pair into sums, columns 2-12, three completed to win. L005 gives the full length sequence exactly."
  },
  {
   "point_id": "K03",
   "point_text": "Forced-move rule: if a chosen pairing creates any valid move you must take all legal moves from that pairing, even onto unwanted columns; you cannot cherry-pick.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L006",
    "L007"
   ],
   "evidence_quote": "The forced-move rule requires taking all legal moves from a chosen pairing, even unwanted ones.",
   "reasoning": "L006 states the rule with the 'even unwanted ones' qualifier; L007 gives the {6,7,8} 2+7 example. Meaning intact."
  },
  {
   "point_id": "K04",
   "point_text": "Two-dice baseline: sum 7 is most likely at 16.67%, exactly 6 times more likely than sum 2 at 2.78%.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L011"
   ],
   "evidence_quote": "With two dice, sum 7 is most likely at 16.67% and exactly 6× more likely than sum 2 at 2.78%.",
   "reasoning": "L011 carries both exact percentages and the 6x ratio with no qualifier loss."
  },
  {
   "point_id": "K05",
   "point_text": "With four dice the distribution flattens: P(can make 7) = 64.4% and P(can make 2) = 13.2%, only a 4.88x ratio versus 6x with two dice.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L010",
    "L022"
   ],
   "evidence_quote": "P(7) = 64.4% versus P(2) = 13.2%, only a 4.88× difference",
   "reasoning": "L010 states 64.4% and 13.2%; L022 restates the 4.88x ratio in conclusion. The contrast with 6x is available via L011/L021."
  },
  {
   "point_id": "K06",
   "point_text": "Expected rolls to complete a column = length / probability; column 2 needs about 22.73 rolls while column 7 needs about 20.18, so 7 is slightly faster despite being 4x longer.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L024",
    "L025"
   ],
   "evidence_quote": "column 2 needs 3/0.132 = 22.73 rolls; column 7 needs 13/0.644 = 20.18 ... Column 7 is slightly faster than column 2 even though it is 4× longer.",
   "reasoning": "L024 gives formula and both numbers; L025 preserves the surprising faster-despite-longer conclusion."
  },
  {
   "point_id": "K07",
   "point_text": "Column combinations matter: {6,7,8} succeeds 92.0% of the time versus 43.8% for {2,3,12}; all 165 three-column combinations were analyzed, with 37 rated excellent (>=85% success) and a median success of 79.6%.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L029",
    "L031"
   ],
   "evidence_quote": "{6,7,8} succeeds on 1193/1296 rolls; {2,3,12} on only 568/1296 ... Across all 165 combinations, 37 are excellent at ≥85% success, the median is 79.6%",
   "reasoning": "L029 gives the 92.0%/43.8% contrast; L031 gives 165 combinations, 37 at >=85%, median 79.6%. All numbers and qualifiers intact."
  },
  {
   "point_id": "K08",
   "point_text": "\"Clean\" moves are rare: even the best combination {6,7,8} yields only 39.8% clean rolls, and {2,3,12} only 2.3%, so the forced-move rule contaminates good combinations.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L034",
    "L035"
   ],
   "evidence_quote": "even {6,7,8} is clean only 39.8% of the time ... only 2.3% of {2,3,12} rolls are clean",
   "reasoning": "L034 gives 39.8% clean and the clean definition; L035 gives 2.3% and states forced moves contaminate good combinations."
  },
  {
   "point_id": "K09",
   "point_text": "Stopping heuristic: keep rolling if (P_success x Q) > (P_bust x U), where Q is expected markers advanced and U is unsaved progress; example on {6,7,8} says roll (1.32 > 0.4) and on {2,3,12} says stop (1.12 > 0.46).",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L038",
    "L039",
    "L040",
    "L041"
   ],
   "evidence_quote": "keep rolling if P(success) × Q exceeds P(bust) × U ... 0.92 × 1.43 = 1.32, so keep rolling ... 0.562 × 2 = 1.12 versus gain 0.438 × 1.05 = 0.46, so stop",
   "reasoning": "L038 gives the inequality, L041 defines Q and U, L039/L040 give both worked examples with matching values."
  },
  {
   "point_id": "K10",
   "point_text": "Tournament of 38 strategies across 2,500 head-to-head games each (3.6M total games) found FiftyPercentSurvival the champion at 69.84% win rate, and probabilistic strategies dominate the top rankings.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L042",
    "L045",
    "L058"
   ],
   "evidence_quote": "Simulations of 38 strategies across 14 families (3.6 million games) ... FiftyPercentSurvival wins 69.84% ... the top 7 all use probability calculations",
   "reasoning": "L042 gives 38 strategies and 3.6M games; L045 gives 69.84% champion; L058 gives probabilistic dominance. The '2,500 per pairing' granularity is omitted but the structure and headline figures are intact, so full credit stands."
  },
  {
   "point_id": "K11",
   "point_text": "Consistency beats speed: GreedyUntil1Col is fastest (10.5 turns) but only ranks #11 at 58.90% due to high variance and bust rate, while FiftyPercentSurvival at 11.3 turns wins most.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L043",
    "L050",
    "L051",
    "L064"
   ],
   "evidence_quote": "GreedyUntil1Col finishes in 10.5 turns but wins only 58.90%, while FiftyPercentSurvival takes 0.8 turns longer and wins 10.9% more ... The fastest strategy is not the best competitive strategy.",
   "reasoning": "L043 gives 10.5 turns with sigma 5.73 and 7.50 busts; L050/L051 give 58.90% and the consistency lesson; L064 restates that reliable 11 turns beats variable 10.5."
  },
  {
   "point_id": "K12",
   "point_text": "Significant first-player advantage: P1 wins 55.59% of games for a +11.18% edge, larger than chess (~5%) or Go (~7%); GreedyUntil1Col shows extreme bias at +31.24%.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L065",
    "L067"
   ],
   "evidence_quote": "Player 1 wins 55.59%, +11.18%, larger than chess (~5%) or Go (~7%) ... GreedyUntil1Col (+31.24%)",
   "reasoning": "L065 gives 55.59%, +11.18%, and both comparison numbers; L067 gives +31.24% for GreedyUntil1Col."
  },
  {
   "point_id": "K13",
   "point_text": "Balance analysis: single-column completion times deviate at most +/-13.6% from 20 rolls, an optimal board one step from current reaches +/-3.09%, and a 20-step board reaches +/-2.17%.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L074",
    "L080",
    "L081"
   ],
   "evidence_quote": "Single-column deviations from 20 expected rolls are at most ±13.6% ... A board one step higher per column (max 14) cuts maximum deviation to ±3.09% ... A 20-step board ... maximum deviation ±2.17%",
   "reasoning": "L074 gives ±13.6%, L080 gives ±3.09%, L081 gives ±2.17%. All three figures and their board conditions preserved."
  },
  {
   "point_id": "K14",
   "point_text": "Stated caveat: continuation versus switching strategies were not fully analyzed quantitatively and remain an open question for future work.",
   "weight": "Nice to have",
   "presence": "Present",
   "loglog_ids": [
    "L091"
   ],
   "evidence_quote": "The author has not analyzed this quantitatively; comparing 'always continue' versus 'switch when X' is left open.",
   "reasoning": "L091 explicitly preserves the open-question caveat with the same scope."
  },
  {
   "point_id": "K15",
   "point_text": "Recommendations: players should use FiftyPercentSurvival and aim for columns 5-9 while avoiding forced activation of 2-3 and 11-12; designers should prioritize playability and use rules to compensate for imbalance, considering handicaps for turn order.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L061",
    "L087"
   ],
   "evidence_quote": "use FiftyPercentSurvival, aim for columns 5-9, avoid forced activation of 2-3 and 11-12, and prioritize consistency ... prioritize playability over mathematical perfection, compensate imbalances with rules, and consider turn-order handicaps",
   "reasoning": "L061 carries the player recommendation with exact column ranges and avoidance targets; L087 carries the designer recommendation including handicaps."
  }
 ],
 "metrics": {
  "total_points": 15,
  "must_have_total": 14,
  "must_have_present": 14,
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
 "source_id": "03_cant_stop_addicted_to_shindig",
 "claims": [
  {
   "claim_id": "C001",
   "loglog_ids": [
    "0"
   ],
   "claim_text": "Can't Stop's four-dice probabilities and forced-move rule make it nearly balanced, and simulations show probabilistic, consistent play wins, though going first is a large advantage.",
   "claim_type": "interpretation",
   "verdict": "Partially supported",
   "severity": "Minor",
   "evidence_quote": "The game heavily favors middle columns.",
   "reasoning": "Probabilistic consistency and first-player advantage are supported, but source says combination play is badly imbalanced, not 'nearly balanced'."
  },
  {
   "claim_id": "C002",
   "loglog_ids": [
    "1"
   ],
   "claim_text": "Can't Stop has players roll four dice, pair them into sums, and advance markers on columns 2 through 12, needing three completed columns to win.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "roll four dice, pair them up however you want, move your markers on a board ... You need to complete three columns to win.",
   "reasoning": "Source states the four-dice, pairing, column and three-column win rules directly."
  },
  {
   "claim_id": "C003",
   "loglog_ids": [
    "1.1"
   ],
   "claim_text": "You can keep rolling as long as you want, but busting when no marker can move loses the turn's gains.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "you can keep rolling as long as you want, but if you can't move any of your three active markers, you lose everything you've gained that turn.",
   "reasoning": "Matches source wording on continued rolling and losing accumulated progress on bust."
  },
  {
   "claim_id": "C004",
   "loglog_ids": [
    "1.2"
   ],
   "claim_text": "Column lengths run 3, 5, 7, 9, 11, 13, 11, 9, 7, 5, and 3 steps for columns 2 through 12.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Columns 2 and 12: 3 steps ... Column 7: 13 steps",
   "reasoning": "Sequence matches the source's column length list exactly."
  },
  {
   "claim_id": "C005",
   "loglog_ids": [
    "1.3"
   ],
   "claim_text": "The forced-move rule requires taking all legal moves from a chosen pairing, even unwanted ones.",
   "claim_type": "definition",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "you must take all available moves ... you must make ALL legal moves from that pairing, even if you don't want them.",
   "reasoning": "Direct restatement of the forced-move rule."
  },
  {
   "claim_id": "C006",
   "loglog_ids": [
    "1.4"
   ],
   "claim_text": "On {6,7,8}, rolling (1,1,3,4) and pairing 2+7 forces moving both 2 and 7 as well.",
   "claim_type": "example",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "you could choose pairing (1,1)+(3,4) = 2+7. But if you do, you're forced to take BOTH the 2 and the 7",
   "reasoning": "Source gives exactly this example with the same dice and columns."
  },
  {
   "claim_id": "C007",
   "loglog_ids": [
    "1.5"
   ],
   "claim_text": "The forced-move rule prevents trivial play and adds tactical depth.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "This rule prevents the game from being trivially easy and adds tactical depth.",
   "reasoning": "Near-verbatim restatement of source conclusion."
  },
  {
   "claim_id": "C008",
   "loglog_ids": [
    "1.6"
   ],
   "claim_text": "An interactive web version exists with a Python/FastAPI backend and React frontend.",
   "claim_type": "evidence",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "I've implemented a fully interactive web version of the game with a Python/FastAPI backend and React frontend.",
   "reasoning": "Directly stated in the source."
  },
  {
   "claim_id": "C009",
   "loglog_ids": [
    "2"
   ],
   "claim_text": "Four dice flatten the distribution: P(7) rises to 64.4% and P(2) to 13.2%, far closer together than with two dice.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "P(7) = 64.4% vs P(2) = 13.2%, only a 4.88× difference compared to 6× with two dice",
   "reasoning": "Numbers match the source's four-dice flattening claim."
  },
  {
   "claim_id": "C010",
   "loglog_ids": [
    "2.1"
   ],
   "claim_text": "With two dice, sum 7 is most likely at 16.67% and exactly 6× more likely than sum 2 at 2.78%.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Sum 7 is the most likely at 16.67%, and it's exactly 6× more likely than sum 2 at 2.78%.",
   "reasoning": "Exact restatement of source values."
  },
  {
   "claim_id": "C011",
   "loglog_ids": [
    "2.1.1"
   ],
   "claim_text": "Sum 2 requires both dice showing 1 (1/36); sum 7 has 6 order-sensitive ways: (1,6), (2,5), (3,4).",
   "claim_type": "evidence",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "both dice must show 1. That's 1/6 × 1/6 = 1/36 ... complementary pairs: (1,6), (2,5), or (3,4), and order matters, so that's 6 ways",
   "reasoning": "Matches the source proof exactly."
  },
  {
   "claim_id": "C012",
   "loglog_ids": [
    "2.2"
   ],
   "claim_text": "If Can't Stop used two dice, column 7 would need to be 6× longer than column 2, but it is only 13/3 ≈ 4.3×.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "column 7 would need to be 6× longer than column 2 to be equally hard. Instead it's only 13/3 ≈ 4.3× longer.",
   "reasoning": "Values and framing match the source."
  },
  {
   "claim_id": "C013",
   "loglog_ids": [
    "2.3"
   ],
   "claim_text": "Rolling 2, 3, 4, 5 gives just three pairings: 5 and 9, 6 and 8, or 7 and 7.",
   "claim_type": "example",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "(2,3)+(4,5) = 5 and 9 ... (2,4)+(3,5) = 6 and 8 ... (2,5)+(3,4) = 7 and 7",
   "reasoning": "Exact list from the source."
  },
  {
   "claim_id": "C014",
   "loglog_ids": [
    "2.4"
   ],
   "claim_text": "Four dice give P(can make a 2) = 171/1296 ≈ 13.2%, requiring at least two 1s among the four.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "P(can make a 2) = 1 - 625/1296 - 500/1296 = 171/1296 ≈ 13.2%",
   "reasoning": "Fraction and percentage match the source calculation."
  },
  {
   "claim_id": "C015",
   "loglog_ids": [
    "2.4.1"
   ],
   "claim_text": "P(zero 1s) = 625/1296 and P(exactly one 1) = 500/1296, so P(can make 2) = 1 - 625/1296 - 500/1296.",
   "claim_type": "evidence",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "P(zero 1's) = (5/6)^4 = 625/1296 ... P(exactly one 1) = ... = 500/1296",
   "reasoning": "Intermediate probabilities match the source exactly."
  },
  {
   "claim_id": "C016",
   "loglog_ids": [
    "2.5"
   ],
   "claim_text": "Four dice give P(can make a 7) = 834/1296 ≈ 64.4%, via inclusion-exclusion over pairs (1,6), (2,5), (3,4).",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "P(can make a 7) = P(A ∪ B ∪ C) = 302 + 302 + 302 - 24 - 24 - 24 + 0 = 834/1296 ≈ 64.4%",
   "reasoning": "Result and method match the source."
  },
  {
   "claim_id": "C017",
   "loglog_ids": [
    "2.5.1"
   ],
   "claim_text": "Each pair event has probability 302/1296, each pairwise overlap 24/1296, and the triple overlap is 0.",
   "claim_type": "evidence",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "P(B) = 302/1296 and P(C) = 302/1296 ... = 24/1296 ... P(A ∩ B ∩ C) = 0",
   "reasoning": "All three component values match the source."
  },
  {
   "claim_id": "C018",
   "loglog_ids": [
    "2.5.2"
   ],
   "claim_text": "Final sum: 302 + 302 + 302 - 24 - 24 - 24 + 0 = 834/1296 ≈ 64.4%.",
   "claim_type": "evidence",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "= 302 + 302 + 302 - 24 - 24 - 24 + 0 = 834/1296 ≈ 64.4%",
   "reasoning": "Exact arithmetic restatement from source."
  },
  {
   "claim_id": "C019",
   "loglog_ids": [
    "2.6"
   ],
   "claim_text": "The full four-dice table shows at-least-one-pair counts from 171 (13.2%) for sum 2 up to 834 (64.4%) for sum 7.",
   "claim_type": "evidence",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "| 2 | 171 (13.2%) ... | 7 | 834 (64.4%)",
   "reasoning": "Table endpoints match the source table."
  },
  {
   "claim_id": "C020",
   "loglog_ids": [
    "2.7"
   ],
   "claim_text": "The probability ratio from column 2 to 7 is 4.88 against a length ratio of 4.33, close enough to suggest deliberate design.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "The probability ratio from 2 to 7 is 4.88. The length ratio is 4.33. Pretty close! The game designers were definitely thinking about this.",
   "reasoning": "Ratios and design inference match the source."
  },
  {
   "claim_id": "C021",
   "loglog_ids": [
    "2.8"
   ],
   "claim_text": "The conclusion restates this: four-dice probabilities flatten the distribution, with P(7) = 64.4% versus P(2) = 13.2%, only a 4.88× difference.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Four-dice probabilities flatten the distribution - P(7) = 64.4% vs P(2) = 13.2%, only a 4.88× difference",
   "reasoning": "Matches the source conclusion item verbatim."
  },
  {
   "claim_id": "C022",
   "loglog_ids": [
    "3"
   ],
   "claim_text": "Single columns are nearly balanced: expected rolls stay between 19.60 and 22.73 across all columns.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "| 6, 8 | 11 | 56.1% | 19.60 | ... | 2, 12 | 3 | 13.2% | 22.73 |",
   "reasoning": "Min and max of the source table match the stated range."
  },
  {
   "claim_id": "C023",
   "loglog_ids": [
    "3.1"
   ],
   "claim_text": "Expected rolls equal length over probability: column 2 needs 3/0.132 = 22.73 rolls; column 7 needs 13/0.644 = 20.18.",
   "claim_type": "evidence",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "For column 2: 3/0.132 = 22.73 rolls, For column 7: 13/0.644 = 20.18 rolls",
   "reasoning": "Formula and values match the source."
  },
  {
   "claim_id": "C024",
   "loglog_ids": [
    "3.2"
   ],
   "claim_text": "Column 7 is slightly faster than column 2 even though it is 4× longer.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Column 7 is slightly faster, even though it's 4× longer.",
   "reasoning": "Near-verbatim source statement."
  },
  {
   "claim_id": "C025",
   "loglog_ids": [
    "3.3"
   ],
   "claim_text": "Expected rolls by column: 22.73 (2/12), 21.46 (3/11), 19.67 (4/10), 20.09 (5/9), 19.60 (6/8), 20.18 (7).",
   "claim_type": "evidence",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "| 2, 12 | 3 | 13.2% | 22.73 | ... | 7 | 13 | 64.4% | 20.18 |",
   "reasoning": "All listed values match the source table."
  },
  {
   "claim_id": "C026",
   "loglog_ids": [
    "3.4"
   ],
   "claim_text": "Columns 2 and 12 require the most rolls; columns 6, 7, and 8 cluster near 20.",
   "claim_type": "evidence",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Columns 2 and 12 require the most rolls. Columns 6, 7, and 8 are all close to each other around 20 rolls.",
   "reasoning": "Direct restatement of source observation."
  },
  {
   "claim_id": "C027",
   "loglog_ids": [
    "3.5"
   ],
   "claim_text": "Column 2 is only 3 steps but hit 13.2% of the time; column 7 is 13 steps but hit 64.4% of the time.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "column 2 is only 3 steps ... you'll only hit it 13.2% of the time. Column 7 is 13 steps but you hit it 64.4% of the time.",
   "reasoning": "Steps and percentages match the source."
  },
  {
   "claim_id": "C028",
   "loglog_ids": [
    "4"
   ],
   "claim_text": "{6,7,8} succeeds 92.0% of the time while {2,3,12} succeeds only 43.8%.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "Result: 1193/1296 = 92.0% success rate ... Result: 568/1296 = 43.8% success rate",
   "reasoning": "SOURCE states both success percentages exactly for the same two combinations."
  },
  {
   "claim_id": "C029",
   "loglog_ids": [
    "4.1"
   ],
   "claim_text": "{6,7,8} succeeds on 1193/1296 rolls; {2,3,12} on 568/1296, less than half.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "1193/1296 = 92.0% success rate ... 568/1296 = 43.8% success rate ... Less than 50% chance of not busting",
   "reasoning": "Counts and the less-than-half qualifier match SOURCE exactly."
  },
  {
   "claim_id": "C030",
   "loglog_ids": [
    "4.2"
   ],
   "claim_text": "Across all 165 combinations, 37 are excellent at ≥85% success, the median is 79.6%, and the worst fall to 43.8%.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "37 combinations are \"excellent\" (≥85% success rate) ... median combination still succeeds 79.6% ... worst combinations drop ... to just 43.8%",
   "reasoning": "All four figures (165, 37, 79.6%, 43.8%) appear verbatim in SOURCE."
  },
  {
   "claim_id": "C031",
   "loglog_ids": [
    "4.3"
   ],
   "claim_text": "The best combination, {6,7,8}, has 92.0% success, 8.0% bust, 39.8% clean moves, and Q = 1.43.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "| 1 | {6,7,8} | 92.0% | 8.0% | 39.8% | 1.43 |",
   "reasoning": "Every value matches the top table row for {6,7,8} in SOURCE."
  },
  {
   "claim_id": "C032",
   "loglog_ids": [
    "4.4"
   ],
   "claim_text": "The worst, {2,11,12}, has 43.8% success, 56.2% bust, 2.3% clean moves, and Q = 1.05.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "| 165 | {2,11,12} | 43.8% | 56.2% | 2.3% | 1.05 |",
   "reasoning": "All four values match the rank-165 row for {2,11,12} in SOURCE."
  },
  {
   "claim_id": "C033",
   "loglog_ids": [
    "4.5"
   ],
   "claim_text": "A 'clean' move hits only wanted columns; even {6,7,8} is clean only 39.8% of the time.",
   "claim_type": "definition",
   "verdict": "Supported",
   "severity": "Minor",
   "evidence_quote": "A \"clean\" move is one where you only hit columns you actually want. Even the best combination {6,7,8} only has 39.8% clean moves",
   "reasoning": "Definition and the 39.8% figure match SOURCE verbatim."
  },
  {
   "claim_id": "C034",
   "loglog_ids": [
    "4.6"
   ],
   "claim_text": "52.2% of {6,7,8} rolls force unwanted columns, and only 2.3% of {2,3,12} rolls are clean.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "The other 52.2% of rolls ... force you onto unwanted columns ... For {2,3,12}: Only 2.3% of rolls are clean!",
   "reasoning": "Both percentages correspond exactly to SOURCE statements for those combinations."
  },
  {
   "claim_id": "C035",
   "loglog_ids": [
    "4.7"
   ],
   "claim_text": "The forced-move rule is a balancing mechanism preventing {6,7,8} from being completely dominant, and is the design's compensating rule.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Minor",
   "evidence_quote": "The forced-move rule is a balancing mechanism. It prevents {6,7,8} from being completely dominant ... It compensates for mathematical imbalances",
   "reasoning": "Both the balancing claim and compensating-rule framing are stated in SOURCE."
  },
  {
   "claim_id": "C036",
   "loglog_ids": [
    "4.8"
   ],
   "claim_text": "The conclusion restates: column combinations matter more than individual columns, {6,7,8} at 92% success and {2,3,12} at 44%.",
   "claim_type": "meta",
   "verdict": "Supported",
   "severity": "Minor",
   "evidence_quote": "Column combinations matter more than individual columns** - {6,7,8} has 92% success rate, {2,3,12} has 44%",
   "reasoning": "SOURCE conclusion states this point with the same rounded percentages."
  },
  {
   "claim_id": "C037",
   "loglog_ids": [
    "5"
   ],
   "claim_text": "The stopping rule is EV-based: keep rolling if P(success) × Q exceeds P(bust) × U.",
   "claim_type": "definition",
   "verdict": "Supported",
   "severity": "Minor",
   "evidence_quote": "**Keep rolling if:** $(P_{\\text{success}} \\times Q) > (P_{\\text{bust}} \\times U)$",
   "reasoning": "The inequality and its variable meanings match SOURCE exactly."
  },
  {
   "claim_id": "C038",
   "loglog_ids": [
    "5.1"
   ],
   "claim_text": "For {6,7,8} with 5 unsaved steps: loss 0.08 × 5 = 0.4 versus gain 0.92 × 1.43 = 1.32, so keep rolling.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "Expected loss: $0.08 \\times 5 = 0.4$ steps ... Expected gain: $0.92 \\times 1.43 = 1.32$ steps ... Since $1.32 > 0.4$, you should keep rolling.",
   "reasoning": "Inputs, products, and the keep-rolling conclusion match SOURCE arithmetic."
  },
  {
   "claim_id": "C039",
   "loglog_ids": [
    "5.2"
   ],
   "claim_text": "For {2,3,12} with 2 unsaved steps: loss 0.562 × 2 = 1.12 versus gain 0.438 × 1.05 = 0.46, so stop.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "**Risk:** $0.562 \\times 2 = 1.12$ steps ... **Expected gain:** $0.438 \\times 1.05 = 0.46$ steps ... Since $1.12 > 0.46$, you should STOP.",
   "reasoning": "All values and the stop conclusion match SOURCE exactly."
  },
  {
   "claim_id": "C040",
   "loglog_ids": [
    "5.3"
   ],
   "claim_text": "Q is expected markers advanced on a successful roll; U is unsaved progress lost on a bust.",
   "claim_type": "definition",
   "verdict": "Supported",
   "severity": "Minor",
   "evidence_quote": "$Q$ = expected number of markers you'll advance on a successful roll ... $U$ = unsaved progress (steps you'd lose if you bust)",
   "reasoning": "Both variable definitions match SOURCE wording."
  },
  {
   "claim_id": "C041",
   "loglog_ids": [
    "6"
   ],
   "claim_text": "Simulations of 38 strategies across 14 families (3.6 million games) show probabilistic play winning and consistency beating speed.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "I tested 38 strategies across 14 different strategic families (¶48); 3.6 million total games (¶47); Probabilistic strategies dominate (¶77); consistency beats raw speed (¶70)",
   "reasoning": "SOURCE states all three components: 38 strategies, 14 families, 3.6M games, probabilistic dominance, consistency over speed."
  },
  {
   "claim_id": "C042",
   "loglog_ids": [
    "6.1"
   ],
   "claim_text": "Single-player, GreedyUntil1Col is fastest at 10.5 turns but has sigma = 5.73 and 7.50 busts per game.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "GreedyUntil1Col is fastest (10.5 turns) but has high variance (σ=5.73) and bust rate (7.5 per game) (¶54); table 7.50 (¶53)",
   "reasoning": "All figures 10.5, 5.73, 7.50 match SOURCE table and key insights."
  },
  {
   "claim_id": "C043",
   "loglog_ids": [
    "6.2"
   ],
   "claim_text": "FiftyPercentSurvival is second at 11.3 turns with sigma = 2.86 and only 2.67 busts per game.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "FiftyPercentSurvival balances speed with remarkable consistency (σ=2.86, only 2.67 busts) (¶54); rank 2, 11.3 (¶53)",
   "reasoning": "Rank 2, 11.3 turns, σ=2.86, 2.67 busts all match SOURCE."
  },
  {
   "claim_id": "C044",
   "loglog_ids": [
    "6.3"
   ],
   "claim_text": "Head-to-head, FiftyPercentSurvival wins 69.84% (132,696/190,000), then Heuristic(1.5) 66.46% and Heuristic(2.0) 63.26%.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "FiftyPercentSurvival 69.84% 132,696/190,000; Heuristic(1.5) 66.46%; Heuristic(2.0) 63.26% (¶57)",
   "reasoning": "All percentages and counts match the head-to-head table."
  },
  {
   "claim_id": "C045",
   "loglog_ids": [
    "6.4"
   ],
   "claim_text": "The champion rolls until cumulative survival probability drops below 50%, with n = log(0.5)/log(P_success).",
   "claim_type": "definition",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Roll until cumulative survival probability drops below 50%, calculated as n = log(0.5) / log(P_success) (¶60)",
   "reasoning": "Direct restatement of SOURCE strategy definition with identical formula."
  },
  {
   "claim_id": "C046",
   "loglog_ids": [
    "6.5"
   ],
   "claim_text": "It wins through sound probability math, balanced risk, speed and consistency (sigma = 2.86), and only +9.42% position bias.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Mathematically sound... Optimal risk tolerance... Low variance, σ of 2.86... Moderate position bias - +9.42% (¶61)",
   "reasoning": "All five listed reasons match SOURCE points, including σ=2.86 and +9.42%."
  },
  {
   "claim_id": "C047",
   "loglog_ids": [
    "6.6"
   ],
   "claim_text": "Its favorite columns are middle ones: most completed 8 (42.0%), 7 (38.4%), 6 (37.7%).",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Most completed: Column 8 (42.0%), Column 7 (38.4%), Column 6 (37.7%) (¶62)",
   "reasoning": "Percentages and column ordering match SOURCE exactly."
  },
  {
   "claim_id": "C048",
   "loglog_ids": [
    "6.7"
   ],
   "claim_text": "Key matchups: 55.22% vs GreedyUntil1Col, 54.38% vs Heuristic(1.5), 63.09% vs MonteCarloLookahead, 50.00% in self-play.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "vs GreedyUntil1Col: 55.22%; vs Heuristic(1.5): 54.38%; vs MonteCarloLookahead: 63.09%; vs itself: 50.00% (¶63)",
   "reasoning": "All four matchup percentages match SOURCE exactly."
  },
  {
   "claim_id": "C049",
   "loglog_ids": [
    "6.8"
   ],
   "claim_text": "GreedyUntil1Col finishes in 10.5 turns but wins only 58.90%, while FiftyPercentSurvival takes 0.8 turns longer and wins 10.9% more.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "only achieves 58.90% competitive win rate (¶68); takes 0.8 turns longer but wins 10.9% more games (¶69)",
   "reasoning": "58.90%, 0.8 turns, and 10.9% all match SOURCE."
  },
  {
   "claim_id": "C050",
   "loglog_ids": [
    "6.8.1"
   ],
   "claim_text": "The fastest strategy is not the best competitive strategy.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "the fastest strategy is not the best competitive strategy (¶66)",
   "reasoning": "Verbatim match to SOURCE."
  },
  {
   "claim_id": "C051",
   "loglog_ids": [
    "6.9"
   ],
   "claim_text": "Core families: Greedy and Random (30% stop), Conservative(k) with k in {1,2,3,4}, Heuristic(alpha) with alpha in {0.3,0.5,1.0,1.5,2.0}, and OpponentAware variants.",
   "claim_type": "definition",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Greedy (always rolls) and Random (30% stop probability); Conservative(k) k ∈ {1,2,3,4}; Heuristic(α) α ∈ {0.3,0.5,1.0,1.5,2.0}; OpponentAware... four variants (¶49)",
   "reasoning": "Family names and parameter sets match SOURCE exactly."
  },
  {
   "claim_id": "C052",
   "loglog_ids": [
    "6.10"
   ],
   "claim_text": "Other core types: Greedy-Improved, Adaptive, Proportional, progressive milestones, probabilistic, and column-count strategies.",
   "claim_type": "definition",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "5. Greedy-Improved... 6. Adaptive... 7. Proportional... 8. Progressive Milestones... 9. Probabilistic... 10. Column-Count (¶50)",
   "reasoning": "All six listed family names match SOURCE groups 5-10."
  },
  {
   "claim_id": "C053",
   "loglog_ids": [
    "6.11"
   ],
   "claim_text": "Newer groups 11-14 cover outside/middle preference, runner-aware, column-quality, and hybrid/advanced strategies.",
   "claim_type": "definition",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "New Strategy Types (Groups 11-14): 11. Outside/Middle Preference... 12. Runner-Aware... 13. Column-Quality... 14. Hybrid/Advanced (¶51)",
   "reasoning": "Groups 11-14 labels match SOURCE exactly."
  },
  {
   "claim_id": "C054",
   "loglog_ids": [
    "6.12"
   ],
   "claim_text": "RiskBudget caps cumulative bust risk at 20% per turn; MonteCarloLookahead simulates 100 future rolls.",
   "claim_type": "definition",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "RiskBudget (20% cumulative bust limit per turn), and MonteCarloLookahead (simulates 100 future rolls (¶51)",
   "reasoning": "20% cap and 100 rolls match SOURCE definitions."
  },
  {
   "claim_id": "C055",
   "loglog_ids": [
    "6.13"
   ],
   "claim_text": "The top 15 all finish in 10.5 to 12.8 turns; conservative strategies like Heuristic(2.0) average under 1 bust per game.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Conservative strategies like Heuristic(2.0) and MonteCarloLookahead average <1 bust per game; The top 15 all complete games in 10.5-12.8 turns (¶54)",
   "reasoning": "Range 10.5-12.8 and <1 bust statement match SOURCE."
  },
  {
   "claim_id": "C056",
   "loglog_ids": [
    "6.14"
   ],
   "claim_text": "A full head-to-head win-rate matrix and a downloadable CSV accompany the rankings.",
   "claim_type": "meta",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Here's the complete head-to-head win-rate matrix... [Download full CSV] (¶64)",
   "reasoning": "SOURCE provides the matrix and a CSV download link."
  },
  {
   "claim_id": "C057",
   "loglog_ids": [
    "6.15"
   ],
   "claim_text": "Probabilistic strategies dominate: the top 7 all use probability calculations, and pure Greedy lost essentially every game.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "The top 7 strategies ALL use mathematical probability calculations... The pure Greedy strategy (never stop voluntarily) lost essentially every game (¶77)",
   "reasoning": "Both statements match SOURCE verbatim."
  },
  {
   "claim_id": "C058",
   "loglog_ids": [
    "6.16"
   ],
   "claim_text": "MonteCarloLookahead, simulating 100 future rolls, only places 4th at 63.09%, so simpler rules are near-optimal.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Despite simulating 100 future rolls per decision... MonteCarloLookahead only places 4th (63.09%)... suggesting we've found near-optimal play (¶78)",
   "reasoning": "100 rolls, 4th place, 63.09%, and near-optimal inference all match SOURCE."
  },
  {
   "claim_id": "C059",
   "loglog_ids": [
    "6.17"
   ],
   "claim_text": "Opponent-aware variants all underperformed simple thresholds because they only looked at completed columns, not partial progress.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "All three performed worse than simple threshold strategies. The problem? They only looked at completed columns, not partial progress (¶78)",
   "reasoning": "The underperformance and stated reason match SOURCE exactly."
  },
  {
   "claim_id": "C060",
   "loglog_ids": [
    "6.18"
   ],
   "claim_text": "For players: use FiftyPercentSurvival, aim for columns 5-9, avoid forced activation of 2-3 and 11-12, and prioritize consistency.",
   "claim_type": "recommendation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Use the FiftyPercentSurvival strategy... Aim for columns 5-9, avoid forcing activation of columns 2-3 and 11-12, and prioritize consistency (¶100)",
   "reasoning": "Recommendation matches SOURCE player advice verbatim."
  },
  {
   "claim_id": "C061",
   "loglog_ids": [
    "6.19"
   ],
   "claim_text": "For probability nerds: near-optimal play sits near 70% win rate; breaking the 75% barrier remains an open question.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "we've found near-optimal play at ~70% win rate. The question is whether any strategy can break the 75% barrier (¶101)",
   "reasoning": "~70% and the 75% barrier question match SOURCE."
  },
  {
   "claim_id": "C062",
   "loglog_ids": [
    "6.20"
   ],
   "claim_text": "The conclusion restates this: probabilistic strategies dominate, with FiftyPercentSurvival's 69.84% win rate beating even Monte Carlo 'perfect play'.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Probabilistic strategies dominate - The champion strategy (FiftyPercentSurvival, 69.84% win rate)... beating even \"perfect play\" Monte Carlo simulation (¶97)",
   "reasoning": "Conclusion point 3 matches SOURCE exactly."
  },
  {
   "claim_id": "C063",
   "loglog_ids": [
    "6.21"
   ],
   "claim_text": "The conclusion restates this: consistency beats speed, since finishing in 11 turns reliably outperforms averaging 10.5 with high variance.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Consistency beats speed - Finishing in 11 turns reliably outperforms averaging 10.5 turns with high variance (¶97)",
   "reasoning": "Conclusion point 4 matches SOURCE verbatim."
  },
  {
   "claim_id": "C064",
   "loglog_ids": [
    "7"
   ],
   "claim_text": "Simulations revealed a significant first-player advantage: Player 1 wins 55.59%, +11.18%, larger than chess (~5%) or Go (~7%).",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Player 1 win rate: 55.59%... First-player advantage: +11.18% (¶71); larger than chess (~5%) or Go (~7%) (¶72)",
   "reasoning": "All figures 55.59%, +11.18%, ~5%, ~7% match SOURCE."
  },
  {
   "claim_id": "C065",
   "loglog_ids": [
    "7.1"
   ],
   "claim_text": "Going first likely helps via first access to middle columns 6-8, setting the pace, and initiative in column selection.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "likely due to: 1. First access to middle columns (6-8) 2. Setting the pace... 3. Initiative in column selection (¶72)",
   "reasoning": "All three proposed reasons match SOURCE and retain the hedge likely."
  },
  {
   "claim_id": "C066",
   "loglog_ids": [
    "7.2"
   ],
   "claim_text": "GreedyUntil1Col (+31.24%) and GreedyFraction(0.5) (+31.00%) show severe position bias; OpponentAware(0.3,1,2) is high at +18.94%.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "GreedyUntil1Col +31.24% SEVERE bias; GreedyFraction(0.5) +31.00% SEVERE bias; OpponentAware(0.3,1,2) +18.94% High bias (¶73)",
   "reasoning": "All three percentages and bias labels match SOURCE table."
  },
  {
   "claim_id": "C067",
   "loglog_ids": [
    "7.3"
   ],
   "claim_text": "Fairest: OpponentAware(2,1,0.3) at -4.14% favors P2, Greedy -0.03%, Heuristic(0.3) +0.65%, Heuristic(0.5) +3.30%.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "OpponentAware(2,1,0.3) -4.14%; Greedy -0.03%; Heuristic(0.3) +0.65%; Heuristic(0.5) +3.30% (¶74)",
   "reasoning": "All four values and the P2 interpretation match SOURCE table."
  },
  {
   "claim_id": "C068",
   "loglog_ids": [
    "7.4"
   ],
   "claim_text": "High position bias may overrate strategies like GreedyUntil1Col in aggregate statistics.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Strategies with high position bias (like GreedyUntil1Col) may be overrated in aggregate statistics (¶75)",
   "reasoning": "Verbatim match, including the hedge may."
  },
  {
   "claim_id": "C069",
   "loglog_ids": [
    "7.5"
   ],
   "claim_text": "The 'opposite' OpponentAware, conservative when behind, performs better as Player 2, suggesting catching up rewards patience.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "The \"opposite\" OpponentAware strategy (conservative when behind, aggressive when ahead) actually performs better as Player 2, suggesting that catching up rewards patience (¶75)",
   "reasoning": "Matches SOURCE description and stated suggestion exactly."
  },
  {
   "claim_id": "C070",
   "loglog_ids": [
    "7.6"
   ],
   "claim_text": "GreedyUntil1Col wins 73% as P1 but only 42% as P2, with sigma = 5.73 and 7.5 busts per game.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "High variance (σ=5.73)... Extreme bust rate (7.5 per game)... Wins 73% as P1, only 42% as P2 (¶68)",
   "reasoning": "All figures 73%, 42%, 5.73, 7.5 match SOURCE."
  },
  {
   "claim_id": "C071",
   "loglog_ids": [
    "7.7"
   ],
   "claim_text": "The conclusion restates this: the first-player advantage is significant, Player 1 winning 55.59% (+11.18%), larger than chess or Go.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "First-player advantage is significant - Player 1 wins 55.59% of games (+11.18% advantage), larger than chess or Go (¶98)",
   "reasoning": "Conclusion point 5 matches SOURCE exactly."
  },
  {
   "claim_id": "C072",
   "loglog_ids": [
    "8"
   ],
   "claim_text": "The designers balanced individual columns but not combinations; the forced-move rule compensates, and better boards exist.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "The designers DID balance individual column completion times, but they couldn't (or didn't want to) balance the three-column combinations.",
   "reasoning": "Source states individual columns balanced, combinations not, forced-move compensates, and optimization shows better boards exist."
  },
  {
   "claim_id": "C073",
   "loglog_ids": [
    "8.1"
   ],
   "claim_text": "Single-column deviations from 20 expected rolls are at most ±13.6% on the current board, good given integer lengths.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "The deviations are ±13.6% at most. That's pretty good given that lengths must be integers!",
   "reasoning": "Source states identical figure ±13.6% and same justification about integer lengths."
  },
  {
   "claim_id": "C074",
   "loglog_ids": [
    "8.2"
   ],
   "claim_text": "In multi-column play, column 7 in {6,7,8} completes in about 2 turns while column 2 in {2,3,12} takes about 30.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "- Column 7 in {6,7,8}: expected completion in ~2 turns\n- Column 2 in {2,3,12}: expected completion in ~30 turns",
   "reasoning": "Source gives same approximations, ~2 turns and ~30 turns, for the same column sets."
  },
  {
   "claim_id": "C075",
   "loglog_ids": [
    "8.3"
   ],
   "claim_text": "Design constraints were simplicity (the 3-5-7-9-11-13 board), 1980 manufacturability, and emotional engagement from visual length.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "1. **Simple enough to understand** - The current board (3-5-7-9-11-13)... 2. **Physically manufacturable**... 3. **Engaging to a broad audience** - The visual length creates emotional investment",
   "reasoning": "Source lists the same three constraints with matching board and 1980 context."
  },
  {
   "claim_id": "C076",
   "loglog_ids": [
    "8.4"
   ],
   "claim_text": "The forced-move rule compensates by forcing sub-optimal columns, preventing all-{6,7,8} play, and adding tactical complexity.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "Forces players into sub-optimal column combinations - Prevents the game from devolving into \"everyone only picks {6,7,8}\" - Adds tactical complexity",
   "reasoning": "Source lists these exact effects of the forced-move rule."
  },
  {
   "claim_id": "C077",
   "loglog_ids": [
    "8.5"
   ],
   "claim_text": "Perfect balance needs lengths as exact multiples of probability: 171 steps for columns 2/12 and 834 for column 7, about 8 hours per game.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "- Column 2/12: 171 steps\n- Column 7: 834 steps\n\nGame duration: ~8 hours.",
   "reasoning": "Source states identical numbers 171, 834, and ~8 hours."
  },
  {
   "claim_id": "C078",
   "loglog_ids": [
    "8.6"
   ],
   "claim_text": "The current board has maximum height 13 steps and maximum deviation ±13.6%.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "**Current board:**\n- Max height: 13 steps\n- Max deviation: ±13.6%",
   "reasoning": "Source gives identical figures for the current board."
  },
  {
   "claim_id": "C079",
   "loglog_ids": [
    "8.7"
   ],
   "claim_text": "A board one step higher per column (max 14) cuts maximum deviation to ±3.09%, 4× more balanced.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "- Max height: 14 steps\n- Max deviation: ±3.09%\n- **4× more balanced with just +1 step!**",
   "reasoning": "Source states same height 14, deviation ±3.09%, and 4× claim."
  },
  {
   "claim_id": "C080",
   "loglog_ids": [
    "8.8"
   ],
   "claim_text": "A 20-step board gives lengths [4,7,11,14,17,20,17,14,11,7,4] and maximum deviation ±2.17%, a 6× improvement.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "- Max height: 20 steps\n- Max deviation: ±2.17%\n- Lengths: [4, 7, 11, 14, 17, 20, 17, 14, 11, 7, 4]\n- **6× improvement in balance**",
   "reasoning": "Source gives identical lengths, deviation ±2.17%, and 6× improvement."
  },
  {
   "claim_id": "C081",
   "loglog_ids": [
    "8.9"
   ],
   "claim_text": "The designers likely kept the current board for round numbers, intentional tension, 1980 testing limits, and player psychology.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "1. **Round numbers**... 2. **Intentional imbalance** - Maybe they wanted strategic tension 3. **Testing limitations** - In 1980... 4. **Player psychology**",
   "reasoning": "Source lists the same four likely reasons for the designers' choice."
  },
  {
   "claim_id": "C082",
   "loglog_ids": [
    "8.10"
   ],
   "claim_text": "The current lengths rise by 2 steps; a linear step=2.25 design gives ±3.09%, 3.2× better balance with +1 step.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "columns increase by exactly 2 steps each time... **Best linear design with similar size (step=2.25):**... Max deviation: ±3.09%... **3.2× better balance with just +1 step!**",
   "reasoning": "Source states step of 2, step=2.25 design, ±3.09%, and 3.2× with +1 step."
  },
  {
   "claim_id": "C083",
   "loglog_ids": [
    "8.11"
   ],
   "claim_text": "An integer linear design (base=5, step=4) yields lengths 5 to 25 and ±3.32% deviation, keeping odd, manufacturable numbers.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "**Best with integer step (base=5, step=4):**\n- Lengths: [5, 9, 13, 17, 21, 25, ...]\n- Max deviation: ±3.32%\n- Maintains aesthetic appeal (all odd numbers, easy to manufacture)",
   "reasoning": "Source gives same base/step, length range 5-25, ±3.32%, and odd/manufacturable note."
  },
  {
   "claim_id": "C084",
   "loglog_ids": [
    "8.12"
   ],
   "claim_text": "Linear designs can never achieve perfect balance because the probability curve is nonlinear.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "Linear designs can never achieve perfect balance because the probability curve is nonlinear",
   "reasoning": "Source states this verbatim, including the 'never' negation."
  },
  {
   "claim_id": "C085",
   "loglog_ids": [
    "8.13"
   ],
   "claim_text": "The author would seriously consider the 20-step board for a modern Can't Stop 2.0.",
   "claim_type": "recommendation",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "For a modern Can't Stop 2.0, I'd seriously consider the 20-step board.",
   "reasoning": "Source states this recommendation verbatim."
  },
  {
   "claim_id": "C086",
   "loglog_ids": [
    "8.14"
   ],
   "claim_text": "For designers: prioritize playability over mathematical perfection, compensate imbalances with rules, and consider turn-order handicaps.",
   "claim_type": "recommendation",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "**For game designers:** Prioritize playability over mathematical perfection, then use rules to compensate for inevitable imbalances... consider handicap systems for competitive play.",
   "reasoning": "Source gives the same three designer recommendations."
  },
  {
   "claim_id": "C087",
   "loglog_ids": [
    "8.15"
   ],
   "claim_text": "The conclusion restates this: perfect balance isn't necessary, as the game is engaging despite (or because of) favoring middle columns.",
   "claim_type": "claim",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "7. **Perfect balance isn't necessary** - The game is engaging despite (or because of) favoring middle columns",
   "reasoning": "Source conclusion item matches the claim nearly verbatim."
  },
  {
   "claim_id": "C088",
   "loglog_ids": [
    "9"
   ],
   "claim_text": "Continuation versus switching depends on progress: the math favors continuing, but forced-move contamination can force strategic switches.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "The mathematics favor continuation in most cases... However, the forced-move rule gradually contaminates good combinations over time, sometimes forcing strategic switches.",
   "reasoning": "Source states math favors continuing and contamination can sometimes force switches, hedge preserved."
  },
  {
   "claim_id": "C089",
   "loglog_ids": [
    "9.1"
   ],
   "claim_text": "With columns nearly complete (e.g., 10/11 steps) continuing makes sense; with 2-3 steps, switching might be faster.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "if columns are nearly complete (e.g., 10/11 steps), continuing makes sense. But with minimal progress (2-3 steps), switching to a better combination might be faster.",
   "reasoning": "Source gives identical step thresholds and same hedged wording."
  },
  {
   "claim_id": "C090",
   "loglog_ids": [
    "9.2"
   ],
   "claim_text": "The author has not analyzed this quantitatively; comparing 'always continue' versus 'switch when X' is left open.",
   "claim_type": "meta",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "**Note:** I haven't fully analyzed this aspect quantitatively... simulating \"always continue\" vs \"switch when X\" strategies... is an interesting open question",
   "reasoning": "Source explicitly says not fully analyzed and frames it as open future work."
  },
  {
   "claim_id": "C091",
   "loglog_ids": [
    "10"
   ],
   "claim_text": "All analysis code and simulation data are linked: probability, column-combination, strategy, and design scripts plus results.",
   "claim_type": "meta",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "All analysis code and simulation results are available",
   "reasoning": "Source links scripts across probability, column-combination, strategy, design, and results sections."
  }
 ],
 "metrics": {
  "total_claims": 91,
  "supported": 90,
  "partially_supported": 1,
  "unverifiable": 0,
  "contradicted": 0,
  "critical_errors": 0,
  "faithfulness_precision": 0.989
 },
 "fail_list": [
  "C001"
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
    "L088"
   ],
   "evidence_quote": "perfect balance isn't necessary, as the game is engaging despite (or because of) favoring middle columns",
   "reasoning": "Summary L002 and conclusion L088 both capture the thesis that near-balance is acceptable and rules compensate. The forced-move rule as compensating mechanism is stated at L036/L077."
  },
  {
   "point_id": "K02",
   "point_text": "Game rules: roll four dice, pair them to move markers on columns 2 through 12, need three completed columns to win; column lengths are 3,5,7,9,11,13,11,9,7,5,3.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L003",
    "L005"
   ],
   "evidence_quote": "Column lengths run 3, 5, 7, 9, 11, 13, 11, 9, 7, 5, and 3 steps for columns 2 through 12.",
   "reasoning": "L003 states roll four dice, pair into sums, columns 2-12, three completed to win. L005 gives the full length sequence exactly."
  },
  {
   "point_id": "K03",
   "point_text": "Forced-move rule: if a chosen pairing creates any valid move you must take all legal moves from that pairing, even onto unwanted columns; you cannot cherry-pick.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L006",
    "L007"
   ],
   "evidence_quote": "The forced-move rule requires taking all legal moves from a chosen pairing, even unwanted ones.",
   "reasoning": "L006 states the rule with the 'even unwanted ones' qualifier; L007 gives the {6,7,8} 2+7 example. Meaning intact."
  },
  {
   "point_id": "K04",
   "point_text": "Two-dice baseline: sum 7 is most likely at 16.67%, exactly 6 times more likely than sum 2 at 2.78%.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L011"
   ],
   "evidence_quote": "With two dice, sum 7 is most likely at 16.67% and exactly 6× more likely than sum 2 at 2.78%.",
   "reasoning": "L011 carries both exact percentages and the 6x ratio with no qualifier loss."
  },
  {
   "point_id": "K05",
   "point_text": "With four dice the distribution flattens: P(can make 7) = 64.4% and P(can make 2) = 13.2%, only a 4.88x ratio versus 6x with two dice.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L010",
    "L022"
   ],
   "evidence_quote": "P(7) = 64.4% versus P(2) = 13.2%, only a 4.88× difference",
   "reasoning": "L010 states 64.4% and 13.2%; L022 restates the 4.88x ratio in conclusion. The contrast with 6x is available via L011/L021."
  },
  {
   "point_id": "K06",
   "point_text": "Expected rolls to complete a column = length / probability; column 2 needs about 22.73 rolls while column 7 needs about 20.18, so 7 is slightly faster despite being 4x longer.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L024",
    "L025"
   ],
   "evidence_quote": "column 2 needs 3/0.132 = 22.73 rolls; column 7 needs 13/0.644 = 20.18 ... Column 7 is slightly faster than column 2 even though it is 4× longer.",
   "reasoning": "L024 gives formula and both numbers; L025 preserves the surprising faster-despite-longer conclusion."
  },
  {
   "point_id": "K07",
   "point_text": "Column combinations matter: {6,7,8} succeeds 92.0% of the time versus 43.8% for {2,3,12}; all 165 three-column combinations were analyzed, with 37 rated excellent (>=85% success) and a median success of 79.6%.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L029",
    "L031"
   ],
   "evidence_quote": "{6,7,8} succeeds on 1193/1296 rolls; {2,3,12} on only 568/1296 ... Across all 165 combinations, 37 are excellent at ≥85% success, the median is 79.6%",
   "reasoning": "L029 gives the 92.0%/43.8% contrast; L031 gives 165 combinations, 37 at >=85%, median 79.6%. All numbers and qualifiers intact."
  },
  {
   "point_id": "K08",
   "point_text": "\"Clean\" moves are rare: even the best combination {6,7,8} yields only 39.8% clean rolls, and {2,3,12} only 2.3%, so the forced-move rule contaminates good combinations.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L034",
    "L035"
   ],
   "evidence_quote": "even {6,7,8} is clean only 39.8% of the time ... only 2.3% of {2,3,12} rolls are clean",
   "reasoning": "L034 gives 39.8% clean and the clean definition; L035 gives 2.3% and states forced moves contaminate good combinations."
  },
  {
   "point_id": "K09",
   "point_text": "Stopping heuristic: keep rolling if (P_success x Q) > (P_bust x U), where Q is expected markers advanced and U is unsaved progress; example on {6,7,8} says roll (1.32 > 0.4) and on {2,3,12} says stop (1.12 > 0.46).",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L038",
    "L039",
    "L040",
    "L041"
   ],
   "evidence_quote": "keep rolling if P(success) × Q exceeds P(bust) × U ... 0.92 × 1.43 = 1.32, so keep rolling ... 0.562 × 2 = 1.12 versus gain 0.438 × 1.05 = 0.46, so stop",
   "reasoning": "L038 gives the inequality, L041 defines Q and U, L039/L040 give both worked examples with matching values."
  },
  {
   "point_id": "K10",
   "point_text": "Tournament of 38 strategies across 2,500 head-to-head games each (3.6M total games) found FiftyPercentSurvival the champion at 69.84% win rate, and probabilistic strategies dominate the top rankings.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L042",
    "L045",
    "L058"
   ],
   "evidence_quote": "Simulations of 38 strategies across 14 families (3.6 million games) ... FiftyPercentSurvival wins 69.84% ... the top 7 all use probability calculations",
   "reasoning": "L042 gives 38 strategies and 3.6M games; L045 gives 69.84% champion; L058 gives probabilistic dominance. The '2,500 per pairing' granularity is omitted but the structure and headline figures are intact, so full credit stands."
  },
  {
   "point_id": "K11",
   "point_text": "Consistency beats speed: GreedyUntil1Col is fastest (10.5 turns) but only ranks #11 at 58.90% due to high variance and bust rate, while FiftyPercentSurvival at 11.3 turns wins most.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L043",
    "L050",
    "L051",
    "L064"
   ],
   "evidence_quote": "GreedyUntil1Col finishes in 10.5 turns but wins only 58.90%, while FiftyPercentSurvival takes 0.8 turns longer and wins 10.9% more ... The fastest strategy is not the best competitive strategy.",
   "reasoning": "L043 gives 10.5 turns with sigma 5.73 and 7.50 busts; L050/L051 give 58.90% and the consistency lesson; L064 restates that reliable 11 turns beats variable 10.5."
  },
  {
   "point_id": "K12",
   "point_text": "Significant first-player advantage: P1 wins 55.59% of games for a +11.18% edge, larger than chess (~5%) or Go (~7%); GreedyUntil1Col shows extreme bias at +31.24%.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L065",
    "L067"
   ],
   "evidence_quote": "Player 1 wins 55.59%, +11.18%, larger than chess (~5%) or Go (~7%) ... GreedyUntil1Col (+31.24%)",
   "reasoning": "L065 gives 55.59%, +11.18%, and both comparison numbers; L067 gives +31.24% for GreedyUntil1Col."
  },
  {
   "point_id": "K13",
   "point_text": "Balance analysis: single-column completion times deviate at most +/-13.6% from 20 rolls, an optimal board one step from current reaches +/-3.09%, and a 20-step board reaches +/-2.17%.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L074",
    "L080",
    "L081"
   ],
   "evidence_quote": "Single-column deviations from 20 expected rolls are at most ±13.6% ... A board one step higher per column (max 14) cuts maximum deviation to ±3.09% ... A 20-step board ... maximum deviation ±2.17%",
   "reasoning": "L074 gives ±13.6%, L080 gives ±3.09%, L081 gives ±2.17%. All three figures and their board conditions preserved."
  },
  {
   "point_id": "K14",
   "point_text": "Stated caveat: continuation versus switching strategies were not fully analyzed quantitatively and remain an open question for future work.",
   "weight": "Nice to have",
   "presence": "Present",
   "loglog_ids": [
    "L091"
   ],
   "evidence_quote": "The author has not analyzed this quantitatively; comparing 'always continue' versus 'switch when X' is left open.",
   "reasoning": "L091 explicitly preserves the open-question caveat with the same scope."
  },
  {
   "point_id": "K15",
   "point_text": "Recommendations: players should use FiftyPercentSurvival and aim for columns 5-9 while avoiding forced activation of 2-3 and 11-12; designers should prioritize playability and use rules to compensate for imbalance, considering handicaps for turn order.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L061",
    "L087"
   ],
   "evidence_quote": "use FiftyPercentSurvival, aim for columns 5-9, avoid forced activation of 2-3 and 11-12, and prioritize consistency ... prioritize playability over mathematical perfection, compensate imbalances with rules, and consider turn-order handicaps",
   "reasoning": "L061 carries the player recommendation with exact column ranges and avoidance targets; L087 carries the designer recommendation including handicaps."
  }
 ],
 "metrics": {
  "total_points": 15,
  "must_have_total": 14,
  "must_have_present": 14,
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
 "source_id": "03_cant_stop_addicted_to_shindig",
 "labels": [
  {
   "claim_id": "C001",
   "loglog_ids": [
    "L002"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Opening thesis/summary, first occurrence framing the whole analysis."
  },
  {
   "claim_id": "C002",
   "loglog_ids": [
    "L003"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Core rules fact, no prior occurrence."
  },
  {
   "claim_id": "C003",
   "loglog_ids": [
    "L004"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Roll-until-bust rule, distinct mechanic."
  },
  {
   "claim_id": "C004",
   "loglog_ids": [
    "L005"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Board column lengths, foundational numbers."
  },
  {
   "claim_id": "C005",
   "loglog_ids": [
    "L006"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Forced-move definition, needed later."
  },
  {
   "claim_id": "C006",
   "loglog_ids": [
    "L007"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Concrete forced-move example, not repeated."
  },
  {
   "claim_id": "C007",
   "loglog_ids": [
    "L008"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Depth interpretation; distinct from balancing claim."
  },
  {
   "claim_id": "C008",
   "loglog_ids": [
    "L009"
   ],
   "label": "Trivia",
   "canonical_id": null,
   "reasoning": "Web artifact mention, low analytical value for the argument."
  },
  {
   "claim_id": "C009",
   "loglog_ids": [
    "L010"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Four-dice distribution claim, canonical for its recaps."
  },
  {
   "claim_id": "C010",
   "loglog_ids": [
    "L011"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Two-dice baseline, new comparative data."
  },
  {
   "claim_id": "C011",
   "loglog_ids": [
    "L012"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Combinatorial evidence with counts, never trivia."
  },
  {
   "claim_id": "C012",
   "loglog_ids": [
    "L013"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Counterfactual length ratio, distinct nuance."
  },
  {
   "claim_id": "C013",
   "loglog_ids": [
    "L014"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Pairing example, distinct illustration."
  },
  {
   "claim_id": "C014",
   "loglog_ids": [
    "L015"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "P(can make 2) result, numeric."
  },
  {
   "claim_id": "C015",
   "loglog_ids": [
    "L016"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Derivation of that probability, numeric evidence."
  },
  {
   "claim_id": "C016",
   "loglog_ids": [
    "L017"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "P(can make 7) result, numeric."
  },
  {
   "claim_id": "C017",
   "loglog_ids": [
    "L018"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Inclusion-exclusion terms, supporting numeric detail."
  },
  {
   "claim_id": "C018",
   "loglog_ids": [
    "L019"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Arithmetic sum, numeric evidence."
  },
  {
   "claim_id": "C019",
   "loglog_ids": [
    "L020"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Full-table evidence, adds table existence beyond C009."
  },
  {
   "claim_id": "C020",
   "loglog_ids": [
    "L021"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Ratio-versus-length design inference, distinct."
  },
  {
   "claim_id": "C021",
   "loglog_ids": [
    "L022"
   ],
   "label": "Duplicate",
   "canonical_id": "C009",
   "reasoning": "Explicit conclusion recap of section 2; adds nothing."
  },
  {
   "claim_id": "C022",
   "loglog_ids": [
    "L023"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Expected-rolls balance claim, new section."
  },
  {
   "claim_id": "C023",
   "loglog_ids": [
    "L024"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Formula and two worked values, numeric."
  },
  {
   "claim_id": "C024",
   "loglog_ids": [
    "L025"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Column 7 faster nuance, distinct interpretation."
  },
  {
   "claim_id": "C025",
   "loglog_ids": [
    "L026"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Full expected-rolls table, numeric evidence."
  },
  {
   "claim_id": "C026",
   "loglog_ids": [
    "L027"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Which columns cost most, numeric summary."
  },
  {
   "claim_id": "C027",
   "loglog_ids": [
    "L028"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Length-versus-frequency juxtaposition, distinct framing."
  },
  {
   "claim_id": "C028",
   "loglog_ids": [
    "L029"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Combination success claim, new section."
  },
  {
   "claim_id": "C029",
   "loglog_ids": [
    "L030"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Counts evidence, canonical for its recap."
  },
  {
   "claim_id": "C030",
   "loglog_ids": [
    "L031"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Distribution across 165 combos, new numbers."
  },
  {
   "claim_id": "C031",
   "loglog_ids": [
    "L032"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Best-combo stats, numeric."
  },
  {
   "claim_id": "C032",
   "loglog_ids": [
    "L033"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Worst-combo stats, numeric."
  },
  {
   "claim_id": "C033",
   "loglog_ids": [
    "L034"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Clean-move definition, needed for Q."
  },
  {
   "claim_id": "C034",
   "loglog_ids": [
    "L035"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Contamination rates, numeric."
  },
  {
   "claim_id": "C035",
   "loglog_ids": [
    "L036"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Balancing interpretation, canonical for C076."
  },
  {
   "claim_id": "C036",
   "loglog_ids": [
    "L037"
   ],
   "label": "Duplicate",
   "canonical_id": "C029",
   "reasoning": "Explicit conclusion recap of section 4; adds nothing."
  },
  {
   "claim_id": "C037",
   "loglog_ids": [
    "L038"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "EV stopping-rule definition, new."
  },
  {
   "claim_id": "C038",
   "loglog_ids": [
    "L039"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Worked EV example, numeric."
  },
  {
   "claim_id": "C039",
   "loglog_ids": [
    "L040"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Second worked EV example, numeric."
  },
  {
   "claim_id": "C040",
   "loglog_ids": [
    "L041"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Q and U definitions, needed for the rule."
  },
  {
   "claim_id": "C041",
   "loglog_ids": [
    "L042"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Simulation headline, new results."
  },
  {
   "claim_id": "C042",
   "loglog_ids": [
    "L043"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Greedy speed/variance numbers, numeric."
  },
  {
   "claim_id": "C043",
   "loglog_ids": [
    "L044"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Second-place numbers, numeric."
  },
  {
   "claim_id": "C044",
   "loglog_ids": [
    "L045"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Head-to-head win rates, numeric."
  },
  {
   "claim_id": "C045",
   "loglog_ids": [
    "L046"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Champion rule definition, new."
  },
  {
   "claim_id": "C046",
   "loglog_ids": [
    "L047"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Champion strengths including new +9.42% bias."
  },
  {
   "claim_id": "C047",
   "loglog_ids": [
    "L048"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Favorite-column percentages, numeric."
  },
  {
   "claim_id": "C048",
   "loglog_ids": [
    "L049"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Matchup percentages, numeric."
  },
  {
   "claim_id": "C049",
   "loglog_ids": [
    "L050"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Speed-versus-wins comparison, numeric."
  },
  {
   "claim_id": "C050",
   "loglog_ids": [
    "L051"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Fastest-is-not-best lesson, canonical for C063."
  },
  {
   "claim_id": "C051",
   "loglog_ids": [
    "L052"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Strategy-family enumeration with parameters, defines scope."
  },
  {
   "claim_id": "C052",
   "loglog_ids": [
    "L053"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Additional strategy types, defines scope."
  },
  {
   "claim_id": "C053",
   "loglog_ids": [
    "L054"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Newer strategy groups, defines scope."
  },
  {
   "claim_id": "C054",
   "loglog_ids": [
    "L055"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "RiskBudget/MonteCarlo definitions with numbers."
  },
  {
   "claim_id": "C055",
   "loglog_ids": [
    "L056"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Top-15 turn range, numeric."
  },
  {
   "claim_id": "C056",
   "loglog_ids": [
    "L057"
   ],
   "label": "Trivia",
   "canonical_id": null,
   "reasoning": "Matrix/CSV artifact mention, no analytical value."
  },
  {
   "claim_id": "C057",
   "loglog_ids": [
    "L058"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Probabilistic-dominance claim, canonical for C062."
  },
  {
   "claim_id": "C058",
   "loglog_ids": [
    "L059"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "MonteCarlo fourth-place nuance, numeric."
  },
  {
   "claim_id": "C059",
   "loglog_ids": [
    "L060"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Opponent-aware failure cause, distinct."
  },
  {
   "claim_id": "C060",
   "loglog_ids": [
    "L061"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Player recommendation, actionable."
  },
  {
   "claim_id": "C061",
   "loglog_ids": [
    "L062"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Win-rate target and open question, distinct."
  },
  {
   "claim_id": "C062",
   "loglog_ids": [
    "L063"
   ],
   "label": "Duplicate",
   "canonical_id": "C057",
   "reasoning": "Conclusion recap of probabilistic dominance; repeats C057/C044."
  },
  {
   "claim_id": "C063",
   "loglog_ids": [
    "L064"
   ],
   "label": "Duplicate",
   "canonical_id": "C050",
   "reasoning": "Conclusion recap of consistency-beats-speed; repeats C050."
  },
  {
   "claim_id": "C064",
   "loglog_ids": [
    "L065"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "First-player advantage claim, canonical for C071."
  },
  {
   "claim_id": "C065",
   "loglog_ids": [
    "L066"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Causal explanation of the advantage, distinct."
  },
  {
   "claim_id": "C066",
   "loglog_ids": [
    "L067"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Position-bias magnitudes, numeric."
  },
  {
   "claim_id": "C067",
   "loglog_ids": [
    "L068"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Fairest strategies list, numeric."
  },
  {
   "claim_id": "C068",
   "loglog_ids": [
    "L069"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Bias overrating interpretation, distinct."
  },
  {
   "claim_id": "C069",
   "loglog_ids": [
    "L070"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Opposite-variant P2 strength, distinct causal link."
  },
  {
   "claim_id": "C070",
   "loglog_ids": [
    "L071"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Greedy P1/P2 split, numeric."
  },
  {
   "claim_id": "C071",
   "loglog_ids": [
    "L072"
   ],
   "label": "Duplicate",
   "canonical_id": "C064",
   "reasoning": "Conclusion recap of first-player advantage; adds nothing."
  },
  {
   "claim_id": "C072",
   "loglog_ids": [
    "L073"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Design conclusion, canonical for C087."
  },
  {
   "claim_id": "C073",
   "loglog_ids": [
    "L074"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Single-column deviation bound, numeric."
  },
  {
   "claim_id": "C074",
   "loglog_ids": [
    "L075"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Multi-column turn comparison, numeric."
  },
  {
   "claim_id": "C075",
   "loglog_ids": [
    "L076"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Design constraints, historical context."
  },
  {
   "claim_id": "C076",
   "loglog_ids": [
    "L077"
   ],
   "label": "Duplicate",
   "canonical_id": "C035",
   "reasoning": "Restates 4.7 balancing mechanism per cross-link; same point."
  },
  {
   "claim_id": "C077",
   "loglog_ids": [
    "L078"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Perfect-balance lengths, numeric."
  },
  {
   "claim_id": "C078",
   "loglog_ids": [
    "L079"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Current board max/deviation, numeric."
  },
  {
   "claim_id": "C079",
   "loglog_ids": [
    "L080"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "14-step board alternative, numeric."
  },
  {
   "claim_id": "C080",
   "loglog_ids": [
    "L081"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "20-step board alternative, numeric."
  },
  {
   "claim_id": "C081",
   "loglog_ids": [
    "L082"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Why current board kept, distinct interpretation."
  },
  {
   "claim_id": "C082",
   "loglog_ids": [
    "L083"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Linear step=2.25 design, numeric."
  },
  {
   "claim_id": "C083",
   "loglog_ids": [
    "L084"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Integer linear design, numeric."
  },
  {
   "claim_id": "C084",
   "loglog_ids": [
    "L085"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Linear-cannot-balance causal claim, distinct."
  },
  {
   "claim_id": "C085",
   "loglog_ids": [
    "L086"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Author preference recommendation, distinct."
  },
  {
   "claim_id": "C086",
   "loglog_ids": [
    "L087"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Designer recommendations, actionable."
  },
  {
   "claim_id": "C087",
   "loglog_ids": [
    "L088"
   ],
   "label": "Duplicate",
   "canonical_id": "C072",
   "reasoning": "Conclusion recap of design conclusion; adds nothing."
  },
  {
   "claim_id": "C088",
   "loglog_ids": [
    "L089"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Continue-versus-switch tradeoff, new section."
  },
  {
   "claim_id": "C089",
   "loglog_ids": [
    "L090"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Progress-dependent guidance, distinct."
  },
  {
   "claim_id": "C090",
   "loglog_ids": [
    "L091"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Caveat that this is unanalyzed; caveats never trivia."
  },
  {
   "claim_id": "C091",
   "loglog_ids": [
    "L092"
   ],
   "label": "Trivia",
   "canonical_id": null,
   "reasoning": "Code/data link meta, no analytical value."
  }
 ],
 "metrics": {
  "scored_claims": 91,
  "unique": 81,
  "duplicates": 7,
  "trivia": 3,
  "redundancy_rate": 0.0769,
  "trivia_rate": 0.033,
  "structured_tokens": 112,
  "tokens_per_unique_claim": 1.38
 },
 "prune_list": [
  "C021 duplicates C009, safe to merge (section 2 recap)",
  "C036 duplicates C029, safe to merge (section 4 recap)",
  "C062 duplicates C057, safe to merge (section 6 recap)",
  "C063 duplicates C050, safe to merge (section 6 recap)",
  "C071 duplicates C064, safe to merge (section 7 recap)",
  "C076 duplicates C035, safe to merge (same balancing mechanism)",
  "C087 duplicates C072, safe to merge (section 8 recap)",
  "C008 artifact mention, low value, consider cutting",
  "C056 artifact mention, low value, consider cutting",
  "C091 artifact mention, low value, consider cutting"
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
   "claim_text": "Can't Stop's four-dice probabilities and forced-move rule make it nearly balanced, and simulations show probabilistic, consistent play wins, though going first is a large advantage.",
   "claim_type": "interpretation",
   "verdict": "Partially supported",
   "severity": "Minor",
   "evidence_quote": "The game heavily favors middle columns.",
   "reasoning": "Probabilistic consistency and first-player advantage are supported, but source says combination play is badly imbalanced, not 'nearly balanced'."
  },
  {
   "claim_id": "C002",
   "loglog_ids": [
    "1"
   ],
   "claim_text": "Can't Stop has players roll four dice, pair them into sums, and advance markers on columns 2 through 12, needing three completed columns to win.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "roll four dice, pair them up however you want, move your markers on a board ... You need to complete three columns to win.",
   "reasoning": "Source states the four-dice, pairing, column and three-column win rules directly."
  },
  {
   "claim_id": "C003",
   "loglog_ids": [
    "1.1"
   ],
   "claim_text": "You can keep rolling as long as you want, but busting when no marker can move loses the turn's gains.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "you can keep rolling as long as you want, but if you can't move any of your three active markers, you lose everything you've gained that turn.",
   "reasoning": "Matches source wording on continued rolling and losing accumulated progress on bust."
  },
  {
   "claim_id": "C004",
   "loglog_ids": [
    "1.2"
   ],
   "claim_text": "Column lengths run 3, 5, 7, 9, 11, 13, 11, 9, 7, 5, and 3 steps for columns 2 through 12.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Columns 2 and 12: 3 steps ... Column 7: 13 steps",
   "reasoning": "Sequence matches the source's column length list exactly."
  },
  {
   "claim_id": "C005",
   "loglog_ids": [
    "1.3"
   ],
   "claim_text": "The forced-move rule requires taking all legal moves from a chosen pairing, even unwanted ones.",
   "claim_type": "definition",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "you must take all available moves ... you must make ALL legal moves from that pairing, even if you don't want them.",
   "reasoning": "Direct restatement of the forced-move rule."
  },
  {
   "claim_id": "C006",
   "loglog_ids": [
    "1.4"
   ],
   "claim_text": "On {6,7,8}, rolling (1,1,3,4) and pairing 2+7 forces moving both 2 and 7 as well.",
   "claim_type": "example",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "you could choose pairing (1,1)+(3,4) = 2+7. But if you do, you're forced to take BOTH the 2 and the 7",
   "reasoning": "Source gives exactly this example with the same dice and columns."
  },
  {
   "claim_id": "C007",
   "loglog_ids": [
    "1.5"
   ],
   "claim_text": "The forced-move rule prevents trivial play and adds tactical depth.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "This rule prevents the game from being trivially easy and adds tactical depth.",
   "reasoning": "Near-verbatim restatement of source conclusion."
  },
  {
   "claim_id": "C008",
   "loglog_ids": [
    "1.6"
   ],
   "claim_text": "An interactive web version exists with a Python/FastAPI backend and React frontend.",
   "claim_type": "evidence",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "I've implemented a fully interactive web version of the game with a Python/FastAPI backend and React frontend.",
   "reasoning": "Directly stated in the source."
  },
  {
   "claim_id": "C009",
   "loglog_ids": [
    "2"
   ],
   "claim_text": "Four dice flatten the distribution: P(7) rises to 64.4% and P(2) to 13.2%, far closer together than with two dice.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "P(7) = 64.4% vs P(2) = 13.2%, only a 4.88× difference compared to 6× with two dice",
   "reasoning": "Numbers match the source's four-dice flattening claim."
  },
  {
   "claim_id": "C010",
   "loglog_ids": [
    "2.1"
   ],
   "claim_text": "With two dice, sum 7 is most likely at 16.67% and exactly 6× more likely than sum 2 at 2.78%.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Sum 7 is the most likely at 16.67%, and it's exactly 6× more likely than sum 2 at 2.78%.",
   "reasoning": "Exact restatement of source values."
  },
  {
   "claim_id": "C011",
   "loglog_ids": [
    "2.1.1"
   ],
   "claim_text": "Sum 2 requires both dice showing 1 (1/36); sum 7 has 6 order-sensitive ways: (1,6), (2,5), (3,4).",
   "claim_type": "evidence",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "both dice must show 1. That's 1/6 × 1/6 = 1/36 ... complementary pairs: (1,6), (2,5), or (3,4), and order matters, so that's 6 ways",
   "reasoning": "Matches the source proof exactly."
  },
  {
   "claim_id": "C012",
   "loglog_ids": [
    "2.2"
   ],
   "claim_text": "If Can't Stop used two dice, column 7 would need to be 6× longer than column 2, but it is only 13/3 ≈ 4.3×.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "column 7 would need to be 6× longer than column 2 to be equally hard. Instead it's only 13/3 ≈ 4.3× longer.",
   "reasoning": "Values and framing match the source."
  },
  {
   "claim_id": "C013",
   "loglog_ids": [
    "2.3"
   ],
   "claim_text": "Rolling 2, 3, 4, 5 gives just three pairings: 5 and 9, 6 and 8, or 7 and 7.",
   "claim_type": "example",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "(2,3)+(4,5) = 5 and 9 ... (2,4)+(3,5) = 6 and 8 ... (2,5)+(3,4) = 7 and 7",
   "reasoning": "Exact list from the source."
  },
  {
   "claim_id": "C014",
   "loglog_ids": [
    "2.4"
   ],
   "claim_text": "Four dice give P(can make a 2) = 171/1296 ≈ 13.2%, requiring at least two 1s among the four.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "P(can make a 2) = 1 - 625/1296 - 500/1296 = 171/1296 ≈ 13.2%",
   "reasoning": "Fraction and percentage match the source calculation."
  },
  {
   "claim_id": "C015",
   "loglog_ids": [
    "2.4.1"
   ],
   "claim_text": "P(zero 1s) = 625/1296 and P(exactly one 1) = 500/1296, so P(can make 2) = 1 - 625/1296 - 500/1296.",
   "claim_type": "evidence",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "P(zero 1's) = (5/6)^4 = 625/1296 ... P(exactly one 1) = ... = 500/1296",
   "reasoning": "Intermediate probabilities match the source exactly."
  },
  {
   "claim_id": "C016",
   "loglog_ids": [
    "2.5"
   ],
   "claim_text": "Four dice give P(can make a 7) = 834/1296 ≈ 64.4%, via inclusion-exclusion over pairs (1,6), (2,5), (3,4).",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "P(can make a 7) = P(A ∪ B ∪ C) = 302 + 302 + 302 - 24 - 24 - 24 + 0 = 834/1296 ≈ 64.4%",
   "reasoning": "Result and method match the source."
  },
  {
   "claim_id": "C017",
   "loglog_ids": [
    "2.5.1"
   ],
   "claim_text": "Each pair event has probability 302/1296, each pairwise overlap 24/1296, and the triple overlap is 0.",
   "claim_type": "evidence",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "P(B) = 302/1296 and P(C) = 302/1296 ... = 24/1296 ... P(A ∩ B ∩ C) = 0",
   "reasoning": "All three component values match the source."
  },
  {
   "claim_id": "C018",
   "loglog_ids": [
    "2.5.2"
   ],
   "claim_text": "Final sum: 302 + 302 + 302 - 24 - 24 - 24 + 0 = 834/1296 ≈ 64.4%.",
   "claim_type": "evidence",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "= 302 + 302 + 302 - 24 - 24 - 24 + 0 = 834/1296 ≈ 64.4%",
   "reasoning": "Exact arithmetic restatement from source."
  },
  {
   "claim_id": "C019",
   "loglog_ids": [
    "2.6"
   ],
   "claim_text": "The full four-dice table shows at-least-one-pair counts from 171 (13.2%) for sum 2 up to 834 (64.4%) for sum 7.",
   "claim_type": "evidence",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "| 2 | 171 (13.2%) ... | 7 | 834 (64.4%)",
   "reasoning": "Table endpoints match the source table."
  },
  {
   "claim_id": "C020",
   "loglog_ids": [
    "2.7"
   ],
   "claim_text": "The probability ratio from column 2 to 7 is 4.88 against a length ratio of 4.33, close enough to suggest deliberate design.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "The probability ratio from 2 to 7 is 4.88. The length ratio is 4.33. Pretty close! The game designers were definitely thinking about this.",
   "reasoning": "Ratios and design inference match the source."
  },
  {
   "claim_id": "C021",
   "loglog_ids": [
    "2.8"
   ],
   "claim_text": "The conclusion restates this: four-dice probabilities flatten the distribution, with P(7) = 64.4% versus P(2) = 13.2%, only a 4.88× difference.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Four-dice probabilities flatten the distribution - P(7) = 64.4% vs P(2) = 13.2%, only a 4.88× difference",
   "reasoning": "Matches the source conclusion item verbatim."
  },
  {
   "claim_id": "C022",
   "loglog_ids": [
    "3"
   ],
   "claim_text": "Single columns are nearly balanced: expected rolls stay between 19.60 and 22.73 across all columns.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "| 6, 8 | 11 | 56.1% | 19.60 | ... | 2, 12 | 3 | 13.2% | 22.73 |",
   "reasoning": "Min and max of the source table match the stated range."
  },
  {
   "claim_id": "C023",
   "loglog_ids": [
    "3.1"
   ],
   "claim_text": "Expected rolls equal length over probability: column 2 needs 3/0.132 = 22.73 rolls; column 7 needs 13/0.644 = 20.18.",
   "claim_type": "evidence",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "For column 2: 3/0.132 = 22.73 rolls, For column 7: 13/0.644 = 20.18 rolls",
   "reasoning": "Formula and values match the source."
  },
  {
   "claim_id": "C024",
   "loglog_ids": [
    "3.2"
   ],
   "claim_text": "Column 7 is slightly faster than column 2 even though it is 4× longer.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Column 7 is slightly faster, even though it's 4× longer.",
   "reasoning": "Near-verbatim source statement."
  },
  {
   "claim_id": "C025",
   "loglog_ids": [
    "3.3"
   ],
   "claim_text": "Expected rolls by column: 22.73 (2/12), 21.46 (3/11), 19.67 (4/10), 20.09 (5/9), 19.60 (6/8), 20.18 (7).",
   "claim_type": "evidence",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "| 2, 12 | 3 | 13.2% | 22.73 | ... | 7 | 13 | 64.4% | 20.18 |",
   "reasoning": "All listed values match the source table."
  },
  {
   "claim_id": "C026",
   "loglog_ids": [
    "3.4"
   ],
   "claim_text": "Columns 2 and 12 require the most rolls; columns 6, 7, and 8 cluster near 20.",
   "claim_type": "evidence",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Columns 2 and 12 require the most rolls. Columns 6, 7, and 8 are all close to each other around 20 rolls.",
   "reasoning": "Direct restatement of source observation."
  },
  {
   "claim_id": "C027",
   "loglog_ids": [
    "3.5"
   ],
   "claim_text": "Column 2 is only 3 steps but hit 13.2% of the time; column 7 is 13 steps but hit 64.4% of the time.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "column 2 is only 3 steps ... you'll only hit it 13.2% of the time. Column 7 is 13 steps but you hit it 64.4% of the time.",
   "reasoning": "Steps and percentages match the source."
  },
  {
   "claim_id": "C028",
   "loglog_ids": [
    "4"
   ],
   "claim_text": "{6,7,8} succeeds 92.0% of the time while {2,3,12} succeeds only 43.8%.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "Result: 1193/1296 = 92.0% success rate ... Result: 568/1296 = 43.8% success rate",
   "reasoning": "SOURCE states both success percentages exactly for the same two combinations."
  },
  {
   "claim_id": "C029",
   "loglog_ids": [
    "4.1"
   ],
   "claim_text": "{6,7,8} succeeds on 1193/1296 rolls; {2,3,12} on 568/1296, less than half.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "1193/1296 = 92.0% success rate ... 568/1296 = 43.8% success rate ... Less than 50% chance of not busting",
   "reasoning": "Counts and the less-than-half qualifier match SOURCE exactly."
  },
  {
   "claim_id": "C030",
   "loglog_ids": [
    "4.2"
   ],
   "claim_text": "Across all 165 combinations, 37 are excellent at ≥85% success, the median is 79.6%, and the worst fall to 43.8%.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "37 combinations are \"excellent\" (≥85% success rate) ... median combination still succeeds 79.6% ... worst combinations drop ... to just 43.8%",
   "reasoning": "All four figures (165, 37, 79.6%, 43.8%) appear verbatim in SOURCE."
  },
  {
   "claim_id": "C031",
   "loglog_ids": [
    "4.3"
   ],
   "claim_text": "The best combination, {6,7,8}, has 92.0% success, 8.0% bust, 39.8% clean moves, and Q = 1.43.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "| 1 | {6,7,8} | 92.0% | 8.0% | 39.8% | 1.43 |",
   "reasoning": "Every value matches the top table row for {6,7,8} in SOURCE."
  },
  {
   "claim_id": "C032",
   "loglog_ids": [
    "4.4"
   ],
   "claim_text": "The worst, {2,11,12}, has 43.8% success, 56.2% bust, 2.3% clean moves, and Q = 1.05.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "| 165 | {2,11,12} | 43.8% | 56.2% | 2.3% | 1.05 |",
   "reasoning": "All four values match the rank-165 row for {2,11,12} in SOURCE."
  },
  {
   "claim_id": "C033",
   "loglog_ids": [
    "4.5"
   ],
   "claim_text": "A 'clean' move hits only wanted columns; even {6,7,8} is clean only 39.8% of the time.",
   "claim_type": "definition",
   "verdict": "Supported",
   "severity": "Minor",
   "evidence_quote": "A \"clean\" move is one where you only hit columns you actually want. Even the best combination {6,7,8} only has 39.8% clean moves",
   "reasoning": "Definition and the 39.8% figure match SOURCE verbatim."
  },
  {
   "claim_id": "C034",
   "loglog_ids": [
    "4.6"
   ],
   "claim_text": "52.2% of {6,7,8} rolls force unwanted columns, and only 2.3% of {2,3,12} rolls are clean.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "The other 52.2% of rolls ... force you onto unwanted columns ... For {2,3,12}: Only 2.3% of rolls are clean!",
   "reasoning": "Both percentages correspond exactly to SOURCE statements for those combinations."
  },
  {
   "claim_id": "C035",
   "loglog_ids": [
    "4.7"
   ],
   "claim_text": "The forced-move rule is a balancing mechanism preventing {6,7,8} from being completely dominant, and is the design's compensating rule.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Minor",
   "evidence_quote": "The forced-move rule is a balancing mechanism. It prevents {6,7,8} from being completely dominant ... It compensates for mathematical imbalances",
   "reasoning": "Both the balancing claim and compensating-rule framing are stated in SOURCE."
  },
  {
   "claim_id": "C036",
   "loglog_ids": [
    "4.8"
   ],
   "claim_text": "The conclusion restates: column combinations matter more than individual columns, {6,7,8} at 92% success and {2,3,12} at 44%.",
   "claim_type": "meta",
   "verdict": "Supported",
   "severity": "Minor",
   "evidence_quote": "Column combinations matter more than individual columns** - {6,7,8} has 92% success rate, {2,3,12} has 44%",
   "reasoning": "SOURCE conclusion states this point with the same rounded percentages."
  },
  {
   "claim_id": "C037",
   "loglog_ids": [
    "5"
   ],
   "claim_text": "The stopping rule is EV-based: keep rolling if P(success) × Q exceeds P(bust) × U.",
   "claim_type": "definition",
   "verdict": "Supported",
   "severity": "Minor",
   "evidence_quote": "**Keep rolling if:** $(P_{\\text{success}} \\times Q) > (P_{\\text{bust}} \\times U)$",
   "reasoning": "The inequality and its variable meanings match SOURCE exactly."
  },
  {
   "claim_id": "C038",
   "loglog_ids": [
    "5.1"
   ],
   "claim_text": "For {6,7,8} with 5 unsaved steps: loss 0.08 × 5 = 0.4 versus gain 0.92 × 1.43 = 1.32, so keep rolling.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "Expected loss: $0.08 \\times 5 = 0.4$ steps ... Expected gain: $0.92 \\times 1.43 = 1.32$ steps ... Since $1.32 > 0.4$, you should keep rolling.",
   "reasoning": "Inputs, products, and the keep-rolling conclusion match SOURCE arithmetic."
  },
  {
   "claim_id": "C039",
   "loglog_ids": [
    "5.2"
   ],
   "claim_text": "For {2,3,12} with 2 unsaved steps: loss 0.562 × 2 = 1.12 versus gain 0.438 × 1.05 = 0.46, so stop.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "**Risk:** $0.562 \\times 2 = 1.12$ steps ... **Expected gain:** $0.438 \\times 1.05 = 0.46$ steps ... Since $1.12 > 0.46$, you should STOP.",
   "reasoning": "All values and the stop conclusion match SOURCE exactly."
  },
  {
   "claim_id": "C040",
   "loglog_ids": [
    "5.3"
   ],
   "claim_text": "Q is expected markers advanced on a successful roll; U is unsaved progress lost on a bust.",
   "claim_type": "definition",
   "verdict": "Supported",
   "severity": "Minor",
   "evidence_quote": "$Q$ = expected number of markers you'll advance on a successful roll ... $U$ = unsaved progress (steps you'd lose if you bust)",
   "reasoning": "Both variable definitions match SOURCE wording."
  },
  {
   "claim_id": "C041",
   "loglog_ids": [
    "6"
   ],
   "claim_text": "Simulations of 38 strategies across 14 families (3.6 million games) show probabilistic play winning and consistency beating speed.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "I tested 38 strategies across 14 different strategic families (¶48); 3.6 million total games (¶47); Probabilistic strategies dominate (¶77); consistency beats raw speed (¶70)",
   "reasoning": "SOURCE states all three components: 38 strategies, 14 families, 3.6M games, probabilistic dominance, consistency over speed."
  },
  {
   "claim_id": "C042",
   "loglog_ids": [
    "6.1"
   ],
   "claim_text": "Single-player, GreedyUntil1Col is fastest at 10.5 turns but has sigma = 5.73 and 7.50 busts per game.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "GreedyUntil1Col is fastest (10.5 turns) but has high variance (σ=5.73) and bust rate (7.5 per game) (¶54); table 7.50 (¶53)",
   "reasoning": "All figures 10.5, 5.73, 7.50 match SOURCE table and key insights."
  },
  {
   "claim_id": "C043",
   "loglog_ids": [
    "6.2"
   ],
   "claim_text": "FiftyPercentSurvival is second at 11.3 turns with sigma = 2.86 and only 2.67 busts per game.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "FiftyPercentSurvival balances speed with remarkable consistency (σ=2.86, only 2.67 busts) (¶54); rank 2, 11.3 (¶53)",
   "reasoning": "Rank 2, 11.3 turns, σ=2.86, 2.67 busts all match SOURCE."
  },
  {
   "claim_id": "C044",
   "loglog_ids": [
    "6.3"
   ],
   "claim_text": "Head-to-head, FiftyPercentSurvival wins 69.84% (132,696/190,000), then Heuristic(1.5) 66.46% and Heuristic(2.0) 63.26%.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "FiftyPercentSurvival 69.84% 132,696/190,000; Heuristic(1.5) 66.46%; Heuristic(2.0) 63.26% (¶57)",
   "reasoning": "All percentages and counts match the head-to-head table."
  },
  {
   "claim_id": "C045",
   "loglog_ids": [
    "6.4"
   ],
   "claim_text": "The champion rolls until cumulative survival probability drops below 50%, with n = log(0.5)/log(P_success).",
   "claim_type": "definition",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Roll until cumulative survival probability drops below 50%, calculated as n = log(0.5) / log(P_success) (¶60)",
   "reasoning": "Direct restatement of SOURCE strategy definition with identical formula."
  },
  {
   "claim_id": "C046",
   "loglog_ids": [
    "6.5"
   ],
   "claim_text": "It wins through sound probability math, balanced risk, speed and consistency (sigma = 2.86), and only +9.42% position bias.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Mathematically sound... Optimal risk tolerance... Low variance, σ of 2.86... Moderate position bias - +9.42% (¶61)",
   "reasoning": "All five listed reasons match SOURCE points, including σ=2.86 and +9.42%."
  },
  {
   "claim_id": "C047",
   "loglog_ids": [
    "6.6"
   ],
   "claim_text": "Its favorite columns are middle ones: most completed 8 (42.0%), 7 (38.4%), 6 (37.7%).",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Most completed: Column 8 (42.0%), Column 7 (38.4%), Column 6 (37.7%) (¶62)",
   "reasoning": "Percentages and column ordering match SOURCE exactly."
  },
  {
   "claim_id": "C048",
   "loglog_ids": [
    "6.7"
   ],
   "claim_text": "Key matchups: 55.22% vs GreedyUntil1Col, 54.38% vs Heuristic(1.5), 63.09% vs MonteCarloLookahead, 50.00% in self-play.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "vs GreedyUntil1Col: 55.22%; vs Heuristic(1.5): 54.38%; vs MonteCarloLookahead: 63.09%; vs itself: 50.00% (¶63)",
   "reasoning": "All four matchup percentages match SOURCE exactly."
  },
  {
   "claim_id": "C049",
   "loglog_ids": [
    "6.8"
   ],
   "claim_text": "GreedyUntil1Col finishes in 10.5 turns but wins only 58.90%, while FiftyPercentSurvival takes 0.8 turns longer and wins 10.9% more.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "only achieves 58.90% competitive win rate (¶68); takes 0.8 turns longer but wins 10.9% more games (¶69)",
   "reasoning": "58.90%, 0.8 turns, and 10.9% all match SOURCE."
  },
  {
   "claim_id": "C050",
   "loglog_ids": [
    "6.8.1"
   ],
   "claim_text": "The fastest strategy is not the best competitive strategy.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "the fastest strategy is not the best competitive strategy (¶66)",
   "reasoning": "Verbatim match to SOURCE."
  },
  {
   "claim_id": "C051",
   "loglog_ids": [
    "6.9"
   ],
   "claim_text": "Core families: Greedy and Random (30% stop), Conservative(k) with k in {1,2,3,4}, Heuristic(alpha) with alpha in {0.3,0.5,1.0,1.5,2.0}, and OpponentAware variants.",
   "claim_type": "definition",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Greedy (always rolls) and Random (30% stop probability); Conservative(k) k ∈ {1,2,3,4}; Heuristic(α) α ∈ {0.3,0.5,1.0,1.5,2.0}; OpponentAware... four variants (¶49)",
   "reasoning": "Family names and parameter sets match SOURCE exactly."
  },
  {
   "claim_id": "C052",
   "loglog_ids": [
    "6.10"
   ],
   "claim_text": "Other core types: Greedy-Improved, Adaptive, Proportional, progressive milestones, probabilistic, and column-count strategies.",
   "claim_type": "definition",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "5. Greedy-Improved... 6. Adaptive... 7. Proportional... 8. Progressive Milestones... 9. Probabilistic... 10. Column-Count (¶50)",
   "reasoning": "All six listed family names match SOURCE groups 5-10."
  },
  {
   "claim_id": "C053",
   "loglog_ids": [
    "6.11"
   ],
   "claim_text": "Newer groups 11-14 cover outside/middle preference, runner-aware, column-quality, and hybrid/advanced strategies.",
   "claim_type": "definition",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "New Strategy Types (Groups 11-14): 11. Outside/Middle Preference... 12. Runner-Aware... 13. Column-Quality... 14. Hybrid/Advanced (¶51)",
   "reasoning": "Groups 11-14 labels match SOURCE exactly."
  },
  {
   "claim_id": "C054",
   "loglog_ids": [
    "6.12"
   ],
   "claim_text": "RiskBudget caps cumulative bust risk at 20% per turn; MonteCarloLookahead simulates 100 future rolls.",
   "claim_type": "definition",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "RiskBudget (20% cumulative bust limit per turn), and MonteCarloLookahead (simulates 100 future rolls (¶51)",
   "reasoning": "20% cap and 100 rolls match SOURCE definitions."
  },
  {
   "claim_id": "C055",
   "loglog_ids": [
    "6.13"
   ],
   "claim_text": "The top 15 all finish in 10.5 to 12.8 turns; conservative strategies like Heuristic(2.0) average under 1 bust per game.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Conservative strategies like Heuristic(2.0) and MonteCarloLookahead average <1 bust per game; The top 15 all complete games in 10.5-12.8 turns (¶54)",
   "reasoning": "Range 10.5-12.8 and <1 bust statement match SOURCE."
  },
  {
   "claim_id": "C056",
   "loglog_ids": [
    "6.14"
   ],
   "claim_text": "A full head-to-head win-rate matrix and a downloadable CSV accompany the rankings.",
   "claim_type": "meta",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Here's the complete head-to-head win-rate matrix... [Download full CSV] (¶64)",
   "reasoning": "SOURCE provides the matrix and a CSV download link."
  },
  {
   "claim_id": "C057",
   "loglog_ids": [
    "6.15"
   ],
   "claim_text": "Probabilistic strategies dominate: the top 7 all use probability calculations, and pure Greedy lost essentially every game.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "The top 7 strategies ALL use mathematical probability calculations... The pure Greedy strategy (never stop voluntarily) lost essentially every game (¶77)",
   "reasoning": "Both statements match SOURCE verbatim."
  },
  {
   "claim_id": "C058",
   "loglog_ids": [
    "6.16"
   ],
   "claim_text": "MonteCarloLookahead, simulating 100 future rolls, only places 4th at 63.09%, so simpler rules are near-optimal.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Despite simulating 100 future rolls per decision... MonteCarloLookahead only places 4th (63.09%)... suggesting we've found near-optimal play (¶78)",
   "reasoning": "100 rolls, 4th place, 63.09%, and near-optimal inference all match SOURCE."
  },
  {
   "claim_id": "C059",
   "loglog_ids": [
    "6.17"
   ],
   "claim_text": "Opponent-aware variants all underperformed simple thresholds because they only looked at completed columns, not partial progress.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "All three performed worse than simple threshold strategies. The problem? They only looked at completed columns, not partial progress (¶78)",
   "reasoning": "The underperformance and stated reason match SOURCE exactly."
  },
  {
   "claim_id": "C060",
   "loglog_ids": [
    "6.18"
   ],
   "claim_text": "For players: use FiftyPercentSurvival, aim for columns 5-9, avoid forced activation of 2-3 and 11-12, and prioritize consistency.",
   "claim_type": "recommendation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Use the FiftyPercentSurvival strategy... Aim for columns 5-9, avoid forcing activation of columns 2-3 and 11-12, and prioritize consistency (¶100)",
   "reasoning": "Recommendation matches SOURCE player advice verbatim."
  },
  {
   "claim_id": "C061",
   "loglog_ids": [
    "6.19"
   ],
   "claim_text": "For probability nerds: near-optimal play sits near 70% win rate; breaking the 75% barrier remains an open question.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "we've found near-optimal play at ~70% win rate. The question is whether any strategy can break the 75% barrier (¶101)",
   "reasoning": "~70% and the 75% barrier question match SOURCE."
  },
  {
   "claim_id": "C062",
   "loglog_ids": [
    "6.20"
   ],
   "claim_text": "The conclusion restates this: probabilistic strategies dominate, with FiftyPercentSurvival's 69.84% win rate beating even Monte Carlo 'perfect play'.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Probabilistic strategies dominate - The champion strategy (FiftyPercentSurvival, 69.84% win rate)... beating even \"perfect play\" Monte Carlo simulation (¶97)",
   "reasoning": "Conclusion point 3 matches SOURCE exactly."
  },
  {
   "claim_id": "C063",
   "loglog_ids": [
    "6.21"
   ],
   "claim_text": "The conclusion restates this: consistency beats speed, since finishing in 11 turns reliably outperforms averaging 10.5 with high variance.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Consistency beats speed - Finishing in 11 turns reliably outperforms averaging 10.5 turns with high variance (¶97)",
   "reasoning": "Conclusion point 4 matches SOURCE verbatim."
  },
  {
   "claim_id": "C064",
   "loglog_ids": [
    "7"
   ],
   "claim_text": "Simulations revealed a significant first-player advantage: Player 1 wins 55.59%, +11.18%, larger than chess (~5%) or Go (~7%).",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Player 1 win rate: 55.59%... First-player advantage: +11.18% (¶71); larger than chess (~5%) or Go (~7%) (¶72)",
   "reasoning": "All figures 55.59%, +11.18%, ~5%, ~7% match SOURCE."
  },
  {
   "claim_id": "C065",
   "loglog_ids": [
    "7.1"
   ],
   "claim_text": "Going first likely helps via first access to middle columns 6-8, setting the pace, and initiative in column selection.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "likely due to: 1. First access to middle columns (6-8) 2. Setting the pace... 3. Initiative in column selection (¶72)",
   "reasoning": "All three proposed reasons match SOURCE and retain the hedge likely."
  },
  {
   "claim_id": "C066",
   "loglog_ids": [
    "7.2"
   ],
   "claim_text": "GreedyUntil1Col (+31.24%) and GreedyFraction(0.5) (+31.00%) show severe position bias; OpponentAware(0.3,1,2) is high at +18.94%.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "GreedyUntil1Col +31.24% SEVERE bias; GreedyFraction(0.5) +31.00% SEVERE bias; OpponentAware(0.3,1,2) +18.94% High bias (¶73)",
   "reasoning": "All three percentages and bias labels match SOURCE table."
  },
  {
   "claim_id": "C067",
   "loglog_ids": [
    "7.3"
   ],
   "claim_text": "Fairest: OpponentAware(2,1,0.3) at -4.14% favors P2, Greedy -0.03%, Heuristic(0.3) +0.65%, Heuristic(0.5) +3.30%.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "OpponentAware(2,1,0.3) -4.14%; Greedy -0.03%; Heuristic(0.3) +0.65%; Heuristic(0.5) +3.30% (¶74)",
   "reasoning": "All four values and the P2 interpretation match SOURCE table."
  },
  {
   "claim_id": "C068",
   "loglog_ids": [
    "7.4"
   ],
   "claim_text": "High position bias may overrate strategies like GreedyUntil1Col in aggregate statistics.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Strategies with high position bias (like GreedyUntil1Col) may be overrated in aggregate statistics (¶75)",
   "reasoning": "Verbatim match, including the hedge may."
  },
  {
   "claim_id": "C069",
   "loglog_ids": [
    "7.5"
   ],
   "claim_text": "The 'opposite' OpponentAware, conservative when behind, performs better as Player 2, suggesting catching up rewards patience.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "The \"opposite\" OpponentAware strategy (conservative when behind, aggressive when ahead) actually performs better as Player 2, suggesting that catching up rewards patience (¶75)",
   "reasoning": "Matches SOURCE description and stated suggestion exactly."
  },
  {
   "claim_id": "C070",
   "loglog_ids": [
    "7.6"
   ],
   "claim_text": "GreedyUntil1Col wins 73% as P1 but only 42% as P2, with sigma = 5.73 and 7.5 busts per game.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "High variance (σ=5.73)... Extreme bust rate (7.5 per game)... Wins 73% as P1, only 42% as P2 (¶68)",
   "reasoning": "All figures 73%, 42%, 5.73, 7.5 match SOURCE."
  },
  {
   "claim_id": "C071",
   "loglog_ids": [
    "7.7"
   ],
   "claim_text": "The conclusion restates this: the first-player advantage is significant, Player 1 winning 55.59% (+11.18%), larger than chess or Go.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "First-player advantage is significant - Player 1 wins 55.59% of games (+11.18% advantage), larger than chess or Go (¶98)",
   "reasoning": "Conclusion point 5 matches SOURCE exactly."
  },
  {
   "claim_id": "C072",
   "loglog_ids": [
    "8"
   ],
   "claim_text": "The designers balanced individual columns but not combinations; the forced-move rule compensates, and better boards exist.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "The designers DID balance individual column completion times, but they couldn't (or didn't want to) balance the three-column combinations.",
   "reasoning": "Source states individual columns balanced, combinations not, forced-move compensates, and optimization shows better boards exist."
  },
  {
   "claim_id": "C073",
   "loglog_ids": [
    "8.1"
   ],
   "claim_text": "Single-column deviations from 20 expected rolls are at most ±13.6% on the current board, good given integer lengths.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "The deviations are ±13.6% at most. That's pretty good given that lengths must be integers!",
   "reasoning": "Source states identical figure ±13.6% and same justification about integer lengths."
  },
  {
   "claim_id": "C074",
   "loglog_ids": [
    "8.2"
   ],
   "claim_text": "In multi-column play, column 7 in {6,7,8} completes in about 2 turns while column 2 in {2,3,12} takes about 30.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "- Column 7 in {6,7,8}: expected completion in ~2 turns\n- Column 2 in {2,3,12}: expected completion in ~30 turns",
   "reasoning": "Source gives same approximations, ~2 turns and ~30 turns, for the same column sets."
  },
  {
   "claim_id": "C075",
   "loglog_ids": [
    "8.3"
   ],
   "claim_text": "Design constraints were simplicity (the 3-5-7-9-11-13 board), 1980 manufacturability, and emotional engagement from visual length.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "1. **Simple enough to understand** - The current board (3-5-7-9-11-13)... 2. **Physically manufacturable**... 3. **Engaging to a broad audience** - The visual length creates emotional investment",
   "reasoning": "Source lists the same three constraints with matching board and 1980 context."
  },
  {
   "claim_id": "C076",
   "loglog_ids": [
    "8.4"
   ],
   "claim_text": "The forced-move rule compensates by forcing sub-optimal columns, preventing all-{6,7,8} play, and adding tactical complexity.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "Forces players into sub-optimal column combinations - Prevents the game from devolving into \"everyone only picks {6,7,8}\" - Adds tactical complexity",
   "reasoning": "Source lists these exact effects of the forced-move rule."
  },
  {
   "claim_id": "C077",
   "loglog_ids": [
    "8.5"
   ],
   "claim_text": "Perfect balance needs lengths as exact multiples of probability: 171 steps for columns 2/12 and 834 for column 7, about 8 hours per game.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "- Column 2/12: 171 steps\n- Column 7: 834 steps\n\nGame duration: ~8 hours.",
   "reasoning": "Source states identical numbers 171, 834, and ~8 hours."
  },
  {
   "claim_id": "C078",
   "loglog_ids": [
    "8.6"
   ],
   "claim_text": "The current board has maximum height 13 steps and maximum deviation ±13.6%.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "**Current board:**\n- Max height: 13 steps\n- Max deviation: ±13.6%",
   "reasoning": "Source gives identical figures for the current board."
  },
  {
   "claim_id": "C079",
   "loglog_ids": [
    "8.7"
   ],
   "claim_text": "A board one step higher per column (max 14) cuts maximum deviation to ±3.09%, 4× more balanced.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "- Max height: 14 steps\n- Max deviation: ±3.09%\n- **4× more balanced with just +1 step!**",
   "reasoning": "Source states same height 14, deviation ±3.09%, and 4× claim."
  },
  {
   "claim_id": "C080",
   "loglog_ids": [
    "8.8"
   ],
   "claim_text": "A 20-step board gives lengths [4,7,11,14,17,20,17,14,11,7,4] and maximum deviation ±2.17%, a 6× improvement.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "- Max height: 20 steps\n- Max deviation: ±2.17%\n- Lengths: [4, 7, 11, 14, 17, 20, 17, 14, 11, 7, 4]\n- **6× improvement in balance**",
   "reasoning": "Source gives identical lengths, deviation ±2.17%, and 6× improvement."
  },
  {
   "claim_id": "C081",
   "loglog_ids": [
    "8.9"
   ],
   "claim_text": "The designers likely kept the current board for round numbers, intentional tension, 1980 testing limits, and player psychology.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "1. **Round numbers**... 2. **Intentional imbalance** - Maybe they wanted strategic tension 3. **Testing limitations** - In 1980... 4. **Player psychology**",
   "reasoning": "Source lists the same four likely reasons for the designers' choice."
  },
  {
   "claim_id": "C082",
   "loglog_ids": [
    "8.10"
   ],
   "claim_text": "The current lengths rise by 2 steps; a linear step=2.25 design gives ±3.09%, 3.2× better balance with +1 step.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "columns increase by exactly 2 steps each time... **Best linear design with similar size (step=2.25):**... Max deviation: ±3.09%... **3.2× better balance with just +1 step!**",
   "reasoning": "Source states step of 2, step=2.25 design, ±3.09%, and 3.2× with +1 step."
  },
  {
   "claim_id": "C083",
   "loglog_ids": [
    "8.11"
   ],
   "claim_text": "An integer linear design (base=5, step=4) yields lengths 5 to 25 and ±3.32% deviation, keeping odd, manufacturable numbers.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "**Best with integer step (base=5, step=4):**\n- Lengths: [5, 9, 13, 17, 21, 25, ...]\n- Max deviation: ±3.32%\n- Maintains aesthetic appeal (all odd numbers, easy to manufacture)",
   "reasoning": "Source gives same base/step, length range 5-25, ±3.32%, and odd/manufacturable note."
  },
  {
   "claim_id": "C084",
   "loglog_ids": [
    "8.12"
   ],
   "claim_text": "Linear designs can never achieve perfect balance because the probability curve is nonlinear.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "Linear designs can never achieve perfect balance because the probability curve is nonlinear",
   "reasoning": "Source states this verbatim, including the 'never' negation."
  },
  {
   "claim_id": "C085",
   "loglog_ids": [
    "8.13"
   ],
   "claim_text": "The author would seriously consider the 20-step board for a modern Can't Stop 2.0.",
   "claim_type": "recommendation",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "For a modern Can't Stop 2.0, I'd seriously consider the 20-step board.",
   "reasoning": "Source states this recommendation verbatim."
  },
  {
   "claim_id": "C086",
   "loglog_ids": [
    "8.14"
   ],
   "claim_text": "For designers: prioritize playability over mathematical perfection, compensate imbalances with rules, and consider turn-order handicaps.",
   "claim_type": "recommendation",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "**For game designers:** Prioritize playability over mathematical perfection, then use rules to compensate for inevitable imbalances... consider handicap systems for competitive play.",
   "reasoning": "Source gives the same three designer recommendations."
  },
  {
   "claim_id": "C087",
   "loglog_ids": [
    "8.15"
   ],
   "claim_text": "The conclusion restates this: perfect balance isn't necessary, as the game is engaging despite (or because of) favoring middle columns.",
   "claim_type": "claim",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "7. **Perfect balance isn't necessary** - The game is engaging despite (or because of) favoring middle columns",
   "reasoning": "Source conclusion item matches the claim nearly verbatim."
  },
  {
   "claim_id": "C088",
   "loglog_ids": [
    "9"
   ],
   "claim_text": "Continuation versus switching depends on progress: the math favors continuing, but forced-move contamination can force strategic switches.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "The mathematics favor continuation in most cases... However, the forced-move rule gradually contaminates good combinations over time, sometimes forcing strategic switches.",
   "reasoning": "Source states math favors continuing and contamination can sometimes force switches, hedge preserved."
  },
  {
   "claim_id": "C089",
   "loglog_ids": [
    "9.1"
   ],
   "claim_text": "With columns nearly complete (e.g., 10/11 steps) continuing makes sense; with 2-3 steps, switching might be faster.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "if columns are nearly complete (e.g., 10/11 steps), continuing makes sense. But with minimal progress (2-3 steps), switching to a better combination might be faster.",
   "reasoning": "Source gives identical step thresholds and same hedged wording."
  },
  {
   "claim_id": "C090",
   "loglog_ids": [
    "9.2"
   ],
   "claim_text": "The author has not analyzed this quantitatively; comparing 'always continue' versus 'switch when X' is left open.",
   "claim_type": "meta",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "**Note:** I haven't fully analyzed this aspect quantitatively... simulating \"always continue\" vs \"switch when X\" strategies... is an interesting open question",
   "reasoning": "Source explicitly says not fully analyzed and frames it as open future work."
  },
  {
   "claim_id": "C091",
   "loglog_ids": [
    "10"
   ],
   "claim_text": "All analysis code and simulation data are linked: probability, column-combination, strategy, and design scripts plus results.",
   "claim_type": "meta",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "All analysis code and simulation results are available",
   "reasoning": "Source links scripts across probability, column-combination, strategy, design, and results sections."
  }
 ],
 "metrics": {
  "total_claims": 91,
  "supported": 90,
  "partially_supported": 1,
  "unverifiable": 0,
  "contradicted": 0,
  "critical_errors": 0,
  "faithfulness_precision": 0.989
 },
 "fail_list": [
  "C001"
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
    "L088"
   ],
   "evidence_quote": "perfect balance isn't necessary, as the game is engaging despite (or because of) favoring middle columns",
   "reasoning": "Summary L002 and conclusion L088 both capture the thesis that near-balance is acceptable and rules compensate. The forced-move rule as compensating mechanism is stated at L036/L077."
  },
  {
   "point_id": "K02",
   "point_text": "Game rules: roll four dice, pair them to move markers on columns 2 through 12, need three completed columns to win; column lengths are 3,5,7,9,11,13,11,9,7,5,3.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L003",
    "L005"
   ],
   "evidence_quote": "Column lengths run 3, 5, 7, 9, 11, 13, 11, 9, 7, 5, and 3 steps for columns 2 through 12.",
   "reasoning": "L003 states roll four dice, pair into sums, columns 2-12, three completed to win. L005 gives the full length sequence exactly."
  },
  {
   "point_id": "K03",
   "point_text": "Forced-move rule: if a chosen pairing creates any valid move you must take all legal moves from that pairing, even onto unwanted columns; you cannot cherry-pick.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L006",
    "L007"
   ],
   "evidence_quote": "The forced-move rule requires taking all legal moves from a chosen pairing, even unwanted ones.",
   "reasoning": "L006 states the rule with the 'even unwanted ones' qualifier; L007 gives the {6,7,8} 2+7 example. Meaning intact."
  },
  {
   "point_id": "K04",
   "point_text": "Two-dice baseline: sum 7 is most likely at 16.67%, exactly 6 times more likely than sum 2 at 2.78%.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L011"
   ],
   "evidence_quote": "With two dice, sum 7 is most likely at 16.67% and exactly 6× more likely than sum 2 at 2.78%.",
   "reasoning": "L011 carries both exact percentages and the 6x ratio with no qualifier loss."
  },
  {
   "point_id": "K05",
   "point_text": "With four dice the distribution flattens: P(can make 7) = 64.4% and P(can make 2) = 13.2%, only a 4.88x ratio versus 6x with two dice.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L010",
    "L022"
   ],
   "evidence_quote": "P(7) = 64.4% versus P(2) = 13.2%, only a 4.88× difference",
   "reasoning": "L010 states 64.4% and 13.2%; L022 restates the 4.88x ratio in conclusion. The contrast with 6x is available via L011/L021."
  },
  {
   "point_id": "K06",
   "point_text": "Expected rolls to complete a column = length / probability; column 2 needs about 22.73 rolls while column 7 needs about 20.18, so 7 is slightly faster despite being 4x longer.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L024",
    "L025"
   ],
   "evidence_quote": "column 2 needs 3/0.132 = 22.73 rolls; column 7 needs 13/0.644 = 20.18 ... Column 7 is slightly faster than column 2 even though it is 4× longer.",
   "reasoning": "L024 gives formula and both numbers; L025 preserves the surprising faster-despite-longer conclusion."
  },
  {
   "point_id": "K07",
   "point_text": "Column combinations matter: {6,7,8} succeeds 92.0% of the time versus 43.8% for {2,3,12}; all 165 three-column combinations were analyzed, with 37 rated excellent (>=85% success) and a median success of 79.6%.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L029",
    "L031"
   ],
   "evidence_quote": "{6,7,8} succeeds on 1193/1296 rolls; {2,3,12} on only 568/1296 ... Across all 165 combinations, 37 are excellent at ≥85% success, the median is 79.6%",
   "reasoning": "L029 gives the 92.0%/43.8% contrast; L031 gives 165 combinations, 37 at >=85%, median 79.6%. All numbers and qualifiers intact."
  },
  {
   "point_id": "K08",
   "point_text": "\"Clean\" moves are rare: even the best combination {6,7,8} yields only 39.8% clean rolls, and {2,3,12} only 2.3%, so the forced-move rule contaminates good combinations.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L034",
    "L035"
   ],
   "evidence_quote": "even {6,7,8} is clean only 39.8% of the time ... only 2.3% of {2,3,12} rolls are clean",
   "reasoning": "L034 gives 39.8% clean and the clean definition; L035 gives 2.3% and states forced moves contaminate good combinations."
  },
  {
   "point_id": "K09",
   "point_text": "Stopping heuristic: keep rolling if (P_success x Q) > (P_bust x U), where Q is expected markers advanced and U is unsaved progress; example on {6,7,8} says roll (1.32 > 0.4) and on {2,3,12} says stop (1.12 > 0.46).",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L038",
    "L039",
    "L040",
    "L041"
   ],
   "evidence_quote": "keep rolling if P(success) × Q exceeds P(bust) × U ... 0.92 × 1.43 = 1.32, so keep rolling ... 0.562 × 2 = 1.12 versus gain 0.438 × 1.05 = 0.46, so stop",
   "reasoning": "L038 gives the inequality, L041 defines Q and U, L039/L040 give both worked examples with matching values."
  },
  {
   "point_id": "K10",
   "point_text": "Tournament of 38 strategies across 2,500 head-to-head games each (3.6M total games) found FiftyPercentSurvival the champion at 69.84% win rate, and probabilistic strategies dominate the top rankings.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L042",
    "L045",
    "L058"
   ],
   "evidence_quote": "Simulations of 38 strategies across 14 families (3.6 million games) ... FiftyPercentSurvival wins 69.84% ... the top 7 all use probability calculations",
   "reasoning": "L042 gives 38 strategies and 3.6M games; L045 gives 69.84% champion; L058 gives probabilistic dominance. The '2,500 per pairing' granularity is omitted but the structure and headline figures are intact, so full credit stands."
  },
  {
   "point_id": "K11",
   "point_text": "Consistency beats speed: GreedyUntil1Col is fastest (10.5 turns) but only ranks #11 at 58.90% due to high variance and bust rate, while FiftyPercentSurvival at 11.3 turns wins most.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L043",
    "L050",
    "L051",
    "L064"
   ],
   "evidence_quote": "GreedyUntil1Col finishes in 10.5 turns but wins only 58.90%, while FiftyPercentSurvival takes 0.8 turns longer and wins 10.9% more ... The fastest strategy is not the best competitive strategy.",
   "reasoning": "L043 gives 10.5 turns with sigma 5.73 and 7.50 busts; L050/L051 give 58.90% and the consistency lesson; L064 restates that reliable 11 turns beats variable 10.5."
  },
  {
   "point_id": "K12",
   "point_text": "Significant first-player advantage: P1 wins 55.59% of games for a +11.18% edge, larger than chess (~5%) or Go (~7%); GreedyUntil1Col shows extreme bias at +31.24%.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L065",
    "L067"
   ],
   "evidence_quote": "Player 1 wins 55.59%, +11.18%, larger than chess (~5%) or Go (~7%) ... GreedyUntil1Col (+31.24%)",
   "reasoning": "L065 gives 55.59%, +11.18%, and both comparison numbers; L067 gives +31.24% for GreedyUntil1Col."
  },
  {
   "point_id": "K13",
   "point_text": "Balance analysis: single-column completion times deviate at most +/-13.6% from 20 rolls, an optimal board one step from current reaches +/-3.09%, and a 20-step board reaches +/-2.17%.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L074",
    "L080",
    "L081"
   ],
   "evidence_quote": "Single-column deviations from 20 expected rolls are at most ±13.6% ... A board one step higher per column (max 14) cuts maximum deviation to ±3.09% ... A 20-step board ... maximum deviation ±2.17%",
   "reasoning": "L074 gives ±13.6%, L080 gives ±3.09%, L081 gives ±2.17%. All three figures and their board conditions preserved."
  },
  {
   "point_id": "K14",
   "point_text": "Stated caveat: continuation versus switching strategies were not fully analyzed quantitatively and remain an open question for future work.",
   "weight": "Nice to have",
   "presence": "Present",
   "loglog_ids": [
    "L091"
   ],
   "evidence_quote": "The author has not analyzed this quantitatively; comparing 'always continue' versus 'switch when X' is left open.",
   "reasoning": "L091 explicitly preserves the open-question caveat with the same scope."
  },
  {
   "point_id": "K15",
   "point_text": "Recommendations: players should use FiftyPercentSurvival and aim for columns 5-9 while avoiding forced activation of 2-3 and 11-12; designers should prioritize playability and use rules to compensate for imbalance, considering handicaps for turn order.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L061",
    "L087"
   ],
   "evidence_quote": "use FiftyPercentSurvival, aim for columns 5-9, avoid forced activation of 2-3 and 11-12, and prioritize consistency ... prioritize playability over mathematical perfection, compensate imbalances with rules, and consider turn-order handicaps",
   "reasoning": "L061 carries the player recommendation with exact column ranges and avoidance targets; L087 carries the designer recommendation including handicaps."
  }
 ],
 "metrics": {
  "total_points": 15,
  "must_have_total": 14,
  "must_have_present": 14,
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
 "source_id": "03_cant_stop_addicted_to_shindig",
 "labels": [
  {
   "claim_id": "C001",
   "loglog_ids": [
    "L002"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Opening thesis/summary, first occurrence framing the whole analysis."
  },
  {
   "claim_id": "C002",
   "loglog_ids": [
    "L003"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Core rules fact, no prior occurrence."
  },
  {
   "claim_id": "C003",
   "loglog_ids": [
    "L004"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Roll-until-bust rule, distinct mechanic."
  },
  {
   "claim_id": "C004",
   "loglog_ids": [
    "L005"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Board column lengths, foundational numbers."
  },
  {
   "claim_id": "C005",
   "loglog_ids": [
    "L006"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Forced-move definition, needed later."
  },
  {
   "claim_id": "C006",
   "loglog_ids": [
    "L007"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Concrete forced-move example, not repeated."
  },
  {
   "claim_id": "C007",
   "loglog_ids": [
    "L008"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Depth interpretation; distinct from balancing claim."
  },
  {
   "claim_id": "C008",
   "loglog_ids": [
    "L009"
   ],
   "label": "Trivia",
   "canonical_id": null,
   "reasoning": "Web artifact mention, low analytical value for the argument."
  },
  {
   "claim_id": "C009",
   "loglog_ids": [
    "L010"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Four-dice distribution claim, canonical for its recaps."
  },
  {
   "claim_id": "C010",
   "loglog_ids": [
    "L011"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Two-dice baseline, new comparative data."
  },
  {
   "claim_id": "C011",
   "loglog_ids": [
    "L012"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Combinatorial evidence with counts, never trivia."
  },
  {
   "claim_id": "C012",
   "loglog_ids": [
    "L013"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Counterfactual length ratio, distinct nuance."
  },
  {
   "claim_id": "C013",
   "loglog_ids": [
    "L014"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Pairing example, distinct illustration."
  },
  {
   "claim_id": "C014",
   "loglog_ids": [
    "L015"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "P(can make 2) result, numeric."
  },
  {
   "claim_id": "C015",
   "loglog_ids": [
    "L016"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Derivation of that probability, numeric evidence."
  },
  {
   "claim_id": "C016",
   "loglog_ids": [
    "L017"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "P(can make 7) result, numeric."
  },
  {
   "claim_id": "C017",
   "loglog_ids": [
    "L018"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Inclusion-exclusion terms, supporting numeric detail."
  },
  {
   "claim_id": "C018",
   "loglog_ids": [
    "L019"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Arithmetic sum, numeric evidence."
  },
  {
   "claim_id": "C019",
   "loglog_ids": [
    "L020"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Full-table evidence, adds table existence beyond C009."
  },
  {
   "claim_id": "C020",
   "loglog_ids": [
    "L021"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Ratio-versus-length design inference, distinct."
  },
  {
   "claim_id": "C021",
   "loglog_ids": [
    "L022"
   ],
   "label": "Duplicate",
   "canonical_id": "C009",
   "reasoning": "Explicit conclusion recap of section 2; adds nothing."
  },
  {
   "claim_id": "C022",
   "loglog_ids": [
    "L023"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Expected-rolls balance claim, new section."
  },
  {
   "claim_id": "C023",
   "loglog_ids": [
    "L024"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Formula and two worked values, numeric."
  },
  {
   "claim_id": "C024",
   "loglog_ids": [
    "L025"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Column 7 faster nuance, distinct interpretation."
  },
  {
   "claim_id": "C025",
   "loglog_ids": [
    "L026"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Full expected-rolls table, numeric evidence."
  },
  {
   "claim_id": "C026",
   "loglog_ids": [
    "L027"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Which columns cost most, numeric summary."
  },
  {
   "claim_id": "C027",
   "loglog_ids": [
    "L028"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Length-versus-frequency juxtaposition, distinct framing."
  },
  {
   "claim_id": "C028",
   "loglog_ids": [
    "L029"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Combination success claim, new section."
  },
  {
   "claim_id": "C029",
   "loglog_ids": [
    "L030"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Counts evidence, canonical for its recap."
  },
  {
   "claim_id": "C030",
   "loglog_ids": [
    "L031"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Distribution across 165 combos, new numbers."
  },
  {
   "claim_id": "C031",
   "loglog_ids": [
    "L032"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Best-combo stats, numeric."
  },
  {
   "claim_id": "C032",
   "loglog_ids": [
    "L033"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Worst-combo stats, numeric."
  },
  {
   "claim_id": "C033",
   "loglog_ids": [
    "L034"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Clean-move definition, needed for Q."
  },
  {
   "claim_id": "C034",
   "loglog_ids": [
    "L035"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Contamination rates, numeric."
  },
  {
   "claim_id": "C035",
   "loglog_ids": [
    "L036"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Balancing interpretation, canonical for C076."
  },
  {
   "claim_id": "C036",
   "loglog_ids": [
    "L037"
   ],
   "label": "Duplicate",
   "canonical_id": "C029",
   "reasoning": "Explicit conclusion recap of section 4; adds nothing."
  },
  {
   "claim_id": "C037",
   "loglog_ids": [
    "L038"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "EV stopping-rule definition, new."
  },
  {
   "claim_id": "C038",
   "loglog_ids": [
    "L039"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Worked EV example, numeric."
  },
  {
   "claim_id": "C039",
   "loglog_ids": [
    "L040"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Second worked EV example, numeric."
  },
  {
   "claim_id": "C040",
   "loglog_ids": [
    "L041"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Q and U definitions, needed for the rule."
  },
  {
   "claim_id": "C041",
   "loglog_ids": [
    "L042"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Simulation headline, new results."
  },
  {
   "claim_id": "C042",
   "loglog_ids": [
    "L043"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Greedy speed/variance numbers, numeric."
  },
  {
   "claim_id": "C043",
   "loglog_ids": [
    "L044"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Second-place numbers, numeric."
  },
  {
   "claim_id": "C044",
   "loglog_ids": [
    "L045"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Head-to-head win rates, numeric."
  },
  {
   "claim_id": "C045",
   "loglog_ids": [
    "L046"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Champion rule definition, new."
  },
  {
   "claim_id": "C046",
   "loglog_ids": [
    "L047"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Champion strengths including new +9.42% bias."
  },
  {
   "claim_id": "C047",
   "loglog_ids": [
    "L048"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Favorite-column percentages, numeric."
  },
  {
   "claim_id": "C048",
   "loglog_ids": [
    "L049"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Matchup percentages, numeric."
  },
  {
   "claim_id": "C049",
   "loglog_ids": [
    "L050"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Speed-versus-wins comparison, numeric."
  },
  {
   "claim_id": "C050",
   "loglog_ids": [
    "L051"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Fastest-is-not-best lesson, canonical for C063."
  },
  {
   "claim_id": "C051",
   "loglog_ids": [
    "L052"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Strategy-family enumeration with parameters, defines scope."
  },
  {
   "claim_id": "C052",
   "loglog_ids": [
    "L053"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Additional strategy types, defines scope."
  },
  {
   "claim_id": "C053",
   "loglog_ids": [
    "L054"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Newer strategy groups, defines scope."
  },
  {
   "claim_id": "C054",
   "loglog_ids": [
    "L055"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "RiskBudget/MonteCarlo definitions with numbers."
  },
  {
   "claim_id": "C055",
   "loglog_ids": [
    "L056"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Top-15 turn range, numeric."
  },
  {
   "claim_id": "C056",
   "loglog_ids": [
    "L057"
   ],
   "label": "Trivia",
   "canonical_id": null,
   "reasoning": "Matrix/CSV artifact mention, no analytical value."
  },
  {
   "claim_id": "C057",
   "loglog_ids": [
    "L058"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Probabilistic-dominance claim, canonical for C062."
  },
  {
   "claim_id": "C058",
   "loglog_ids": [
    "L059"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "MonteCarlo fourth-place nuance, numeric."
  },
  {
   "claim_id": "C059",
   "loglog_ids": [
    "L060"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Opponent-aware failure cause, distinct."
  },
  {
   "claim_id": "C060",
   "loglog_ids": [
    "L061"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Player recommendation, actionable."
  },
  {
   "claim_id": "C061",
   "loglog_ids": [
    "L062"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Win-rate target and open question, distinct."
  },
  {
   "claim_id": "C062",
   "loglog_ids": [
    "L063"
   ],
   "label": "Duplicate",
   "canonical_id": "C057",
   "reasoning": "Conclusion recap of probabilistic dominance; repeats C057/C044."
  },
  {
   "claim_id": "C063",
   "loglog_ids": [
    "L064"
   ],
   "label": "Duplicate",
   "canonical_id": "C050",
   "reasoning": "Conclusion recap of consistency-beats-speed; repeats C050."
  },
  {
   "claim_id": "C064",
   "loglog_ids": [
    "L065"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "First-player advantage claim, canonical for C071."
  },
  {
   "claim_id": "C065",
   "loglog_ids": [
    "L066"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Causal explanation of the advantage, distinct."
  },
  {
   "claim_id": "C066",
   "loglog_ids": [
    "L067"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Position-bias magnitudes, numeric."
  },
  {
   "claim_id": "C067",
   "loglog_ids": [
    "L068"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Fairest strategies list, numeric."
  },
  {
   "claim_id": "C068",
   "loglog_ids": [
    "L069"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Bias overrating interpretation, distinct."
  },
  {
   "claim_id": "C069",
   "loglog_ids": [
    "L070"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Opposite-variant P2 strength, distinct causal link."
  },
  {
   "claim_id": "C070",
   "loglog_ids": [
    "L071"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Greedy P1/P2 split, numeric."
  },
  {
   "claim_id": "C071",
   "loglog_ids": [
    "L072"
   ],
   "label": "Duplicate",
   "canonical_id": "C064",
   "reasoning": "Conclusion recap of first-player advantage; adds nothing."
  },
  {
   "claim_id": "C072",
   "loglog_ids": [
    "L073"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Design conclusion, canonical for C087."
  },
  {
   "claim_id": "C073",
   "loglog_ids": [
    "L074"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Single-column deviation bound, numeric."
  },
  {
   "claim_id": "C074",
   "loglog_ids": [
    "L075"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Multi-column turn comparison, numeric."
  },
  {
   "claim_id": "C075",
   "loglog_ids": [
    "L076"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Design constraints, historical context."
  },
  {
   "claim_id": "C076",
   "loglog_ids": [
    "L077"
   ],
   "label": "Duplicate",
   "canonical_id": "C035",
   "reasoning": "Restates 4.7 balancing mechanism per cross-link; same point."
  },
  {
   "claim_id": "C077",
   "loglog_ids": [
    "L078"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Perfect-balance lengths, numeric."
  },
  {
   "claim_id": "C078",
   "loglog_ids": [
    "L079"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Current board max/deviation, numeric."
  },
  {
   "claim_id": "C079",
   "loglog_ids": [
    "L080"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "14-step board alternative, numeric."
  },
  {
   "claim_id": "C080",
   "loglog_ids": [
    "L081"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "20-step board alternative, numeric."
  },
  {
   "claim_id": "C081",
   "loglog_ids": [
    "L082"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Why current board kept, distinct interpretation."
  },
  {
   "claim_id": "C082",
   "loglog_ids": [
    "L083"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Linear step=2.25 design, numeric."
  },
  {
   "claim_id": "C083",
   "loglog_ids": [
    "L084"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Integer linear design, numeric."
  },
  {
   "claim_id": "C084",
   "loglog_ids": [
    "L085"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Linear-cannot-balance causal claim, distinct."
  },
  {
   "claim_id": "C085",
   "loglog_ids": [
    "L086"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Author preference recommendation, distinct."
  },
  {
   "claim_id": "C086",
   "loglog_ids": [
    "L087"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Designer recommendations, actionable."
  },
  {
   "claim_id": "C087",
   "loglog_ids": [
    "L088"
   ],
   "label": "Duplicate",
   "canonical_id": "C072",
   "reasoning": "Conclusion recap of design conclusion; adds nothing."
  },
  {
   "claim_id": "C088",
   "loglog_ids": [
    "L089"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Continue-versus-switch tradeoff, new section."
  },
  {
   "claim_id": "C089",
   "loglog_ids": [
    "L090"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Progress-dependent guidance, distinct."
  },
  {
   "claim_id": "C090",
   "loglog_ids": [
    "L091"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Caveat that this is unanalyzed; caveats never trivia."
  },
  {
   "claim_id": "C091",
   "loglog_ids": [
    "L092"
   ],
   "label": "Trivia",
   "canonical_id": null,
   "reasoning": "Code/data link meta, no analytical value."
  }
 ],
 "metrics": {
  "scored_claims": 91,
  "unique": 81,
  "duplicates": 7,
  "trivia": 3,
  "redundancy_rate": 0.0769,
  "trivia_rate": 0.033,
  "structured_tokens": 112,
  "tokens_per_unique_claim": 1.38
 },
 "prune_list": [
  "C021 duplicates C009, safe to merge (section 2 recap)",
  "C036 duplicates C029, safe to merge (section 4 recap)",
  "C062 duplicates C057, safe to merge (section 6 recap)",
  "C063 duplicates C050, safe to merge (section 6 recap)",
  "C071 duplicates C064, safe to merge (section 7 recap)",
  "C076 duplicates C035, safe to merge (same balancing mechanism)",
  "C087 duplicates C072, safe to merge (section 8 recap)",
  "C008 artifact mention, low value, consider cutting",
  "C056 artifact mention, low value, consider cutting",
  "C091 artifact mention, low value, consider cutting"
 ]
}
```

## Judge Top (overall), opencode-go/deepseek-v4.1-flash

```json
{
 "judge": "overall",
 "judge_version": "1.0.0",
 "model": "deepseek-v4.1-flash (2026-09-15)",
 "source_id": "not provided in inputs",
 "inputs": {
  "faithfulness_precision": 0.989,
  "critical_errors": 0,
  "must_recall": 1.0,
  "overall_recall": 1.0,
  "redundancy_rate": 0.0769,
  "trivia_rate": 0.033
 },
 "weights_used": {
  "faithfulness_precision": 0.4,
  "coverage_must_recall": 0.4,
  "redundancy_penalty": 0.2
 },
 "computation": "weighted_score = 0.4 * 0.989 + 0.4 * 1.0 - 0.2 * 0.0769 = 0.3956 + 0.4 - 0.01538 = 0.78022",
 "weighted_score": 0.7802,
 "verdict": "Borderline",
 "tradeoff_note": "Full must-have coverage (14/14) and zero critical errors clear all hard gates, and length cost is justified because redundancy (0.0769) stays below the 0.15 max. The one Partially supported claim C001 is on a Must-have balance point, so human review is advised despite a strong weighted score.",
 "fix_list": [
  "Fix C001: source loglog line 0 says combination play is 'badly imbalanced' and 'heavily favors middle columns', so soften 'nearly balanced' on the Must-have balance point.",
  "Fix C076: merge into C035, same balancing mechanism, redundant.",
  "Fix C021/C036/C062/C063/C071/C087: merge section recaps into their originals C009/C029/C057/C050/C064/C072.",
  "Cut low-value artifact claims C008, C056, C091, which add trivia without supporting a point."
 ],
 "reasoning": "Gate check in policy order. Hard fails: critical_errors = 0 <= critical_contradicted_max 0, pass. must_recall = 1.0 >= must_recall_min 0.9, pass. faithfulness_precision = 0.989 >= faithfulness_precision_min 0.95, pass. No hard gate missed, so the sample is not a Fail. Weighted score computed with configured aspect_weights 0.4/0.4/0.2 -> 0.78022, a comfortable numeric pass. Concision role: redundancy_rate 0.0769 < redundancy_max 0.15, so the length is not penalized beyond the small 0.01538 deduction, and coverage gain justifies the extra length under the top_policy. Borderline trigger: gates pass on numbers, but a Partial claim affects a Must-have point. C001 is 'Partially supported' (Minor) and cites loglog id 0, the balance point: it claims Can't Stop is 'nearly balanced' while the evidence_quote states 'The game heavily favors middle columns' and 'badly imbalanced'. Because must_have_total = 14 with 14 present and C001 maps to the balance Must-have, this is exactly the gates-pass-but-review case, so Borderline over Pass. The weighted score math uses the Coverage must_recall 1.0 (not overall_recall 1.0, which coincides) and the Concision redundancy_rate 0.0769, both from the aspect JSONs; trivia_rate 0.033 and tokens_per_unique_claim 1.38 are recorded for audit but carry no weight. Prune list items C021, C036, C062, C063, C071, C087 (recaps) and C076 (duplicate mechanism) are reflected in the 7 duplicates driving the 0.0769 rate and are the highest-leverage length fixes after the C001 accuracy fix."
}
```
