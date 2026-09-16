# Judge trace (scripted pipeline, opencode-go/deepseek-v4.1-flash)

## Judge F (faithfulness), opencode-go/deepseek-v4.1-flash

```json
{
 "judge": "faithfulness",
 "judge_version": "1.0.0",
 "model": "opencode-go/deepseek-v4.1-flash (opencode) scripted pipeline 2026-09-15",
 "source_id": "10_parde_begardan_fa",
 "claims": [
  {
   "claim_id": "C001",
   "loglog_ids": [
    "0"
   ],
   "claim_text": "راوی از شیفتگی کودکی به سنتور و محدودیت کوک دیاتونیک آن به سنتور کلیددار تازه‌ای می‌رسد که جابه‌جایی آزاد میان دستگاه‌ها را ممکن می‌کند.",
   "claim_type": "meta",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "سنتور یه ساز دیاتونیک هست ... اگه بخوای مدلاسیون انجام بدی باید کوک عوض بشه ... یه سنتوری درست کردن که از چنگ ایده گرفتن و یه سری کلید تعبیه کردن",
   "reasoning": "Summary faithfully compresses the childhood fascination, the diatonic tuning limit, and the keyed santur enabling free movement."
  },
  {
   "claim_id": "C002",
   "loglog_ids": [
    "1"
   ],
   "claim_text": "شیفتگی آغازین: دیدار هفت‌سالگی با سنتور خاله و اصرار برای داشتن آن.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "۷ سالم که بود یه شب شام خونه خاله‌م بودیم ... تمام طول راه رو زر زدم که سنتور میخوام",
   "reasoning": "Age seven, aunt's santur, and the insistent demand are all present in the source."
  },
  {
   "claim_id": "C003",
   "loglog_ids": [
    "1.1"
   ],
   "claim_text": "سنتور گوشه اتاق بود و خاله «زرد ملیجه» را نواخت.",
   "claim_type": "fact",
   "verdict": "Partially supported",
   "severity": "Minor",
   "evidence_quote": "یه آهنگ هم برامون زد، «زرد ملیجه» بود فکر کنم",
   "reasoning": "Source hedges the song with فکر کنم (I think); loglog states it as certain, dropping the hedge."
  },
  {
   "claim_id": "C004",
   "loglog_ids": [
    "1.2"
   ],
   "claim_text": "آخر شب به‌زور او را از پای ساز بلند کردند.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "آخر شب به زور من رو از پای ساز بلند کردن که بریم خونه",
   "reasoning": "Direct restatement of the source's forced removal from the santur."
  },
  {
   "claim_id": "C005",
   "loglog_ids": [
    "1.3"
   ],
   "claim_text": "شش ماه اصرار تا خرید سنتور هجده‌هزار تومانی انجامید.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "شیش ماه که این زر زدن‌ها و لج‌کردن‌ها ادامه داشت ... ۲۰هزار تومن، با تخفیف شد ۱۸هزار تومن",
   "reasoning": "Six months of insistence and the final 18-thousand price match the source."
  },
  {
   "claim_id": "C006",
   "loglog_ids": [
    "2"
   ],
   "claim_text": "سال‌های آموزش: کلاس، اتاق سرد پذیرایی و دشواری کوک.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "سنتورم تو اتاق پذیرایی بود که همیشه درش بسته بود و سردتر از بقیه اتاقها ... کار هرکسی نیست کوک کردنش",
   "reasoning": "Cold living room, lessons, and tuning difficulty are all stated in the source."
  },
  {
   "claim_id": "C007",
   "loglog_ids": [
    "2.1"
   ],
   "claim_text": "استاد نخست به خانه می‌آمد چون آموزشگاهی در شهر نبود.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "اوایل استادم میومد خونه، چون تو شهرمون آموزشگاهی نبود که من برم",
   "reasoning": "Exact restatement of the early home lessons and absence of a local institute."
  },
  {
   "claim_id": "C008",
   "loglog_ids": [
    "2.2"
   ],
   "claim_text": "ساز بزرگ‌تر از کودک بود و برای کوک ۷۲ سیم به کلاس می‌رفت.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "سازم از خودم گنده‌تر بود ... باید ساز رو میبردم که کوک بشه چون لاکردار ۷۲ تا سیم داره",
   "reasoning": "Both the oversized santur and the 72 strings requiring class tuning are stated."
  },
  {
   "claim_id": "C009",
   "loglog_ids": [
    "2.3"
   ],
   "claim_text": "با آمدن تیونر دیگر لازم نبود ساز برای کوک به کلاس برده شود.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "بعدترها که تیونر اومد بازار دیگه نیاز نبود ساز رو ببرم سر کلاس",
   "reasoning": "Directly restates the source's statement about the tuner removing the need."
  },
  {
   "claim_id": "C010",
   "loglog_ids": [
    "3"
   ],
   "claim_text": "محدودیت دیاتونیک: یک دستگاه در هر کوک و رنج بازی ناتمام.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "در آن واحد فقط میشه یک دستگاه/گام رو روش نواخت ... نمیتونستم بازی دیگه‌ای بکنم",
   "reasoning": "One dastgah per tuning and the incomplete-game feeling are both in the source."
  },
  {
   "claim_id": "C011",
   "loglog_ids": [
    "3.1"
   ],
   "claim_text": "مدولاسیون نیازمند صرف زمان برای تغییر کوک بود.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "اگه بخوای مدلاسیون انجام بدی باید کوک عوض بشه که خب زمانبره",
   "reasoning": "Matches the source's statement that modulation requires time-consuming retuning."
  },
  {
   "claim_id": "C012",
   "loglog_ids": [
    "3.2"
   ],
   "claim_text": "حس بچه‌ای که در مهمانی فقط یک بازی برایش مجاز است.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "حس بچه‌ای رو داشته باشم که تو مهمونی بهش فقط اجازه یه بازی رو داده باشن",
   "reasoning": "Close paraphrase preserving the only-one-game-at-a-party analogy."
  },
  {
   "claim_id": "C013",
   "loglog_ids": [
    "3.3"
   ],
   "claim_text": "بازی محبوب دیگران را فقط از گوشه‌ای ساکت نگاه می‌کرد.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "من مجبور بودم ساکت بشینم یه گوشه‌ای و نگاهشون کنم. حتی اگه اون بازی‌ رو خیلی دوست داشتم",
   "reasoning": "The quiet corner-watching of a game he liked is accurately conveyed."
  },
  {
   "claim_id": "C014",
   "loglog_ids": [
    "4"
   ],
   "claim_text": "گشایش: سنتور کلیددار الهام‌گرفته از چنگ با مدولاسیون ثانیه‌ای.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "یه سنتوری درست کردن که از چنگ ایده گرفتن و یه سری کلید تعبیه کردن ... در کسری از ثانیه",
   "reasoning": "Harp-inspired keyed santur and second-scale modulation are both stated."
  },
  {
   "claim_id": "C015",
   "loglog_ids": [
    "4.1"
   ],
   "claim_text": "کلیدها هر نت را در کسری از ثانیه ربع یا نیم پرده زیرتر می‌کنند.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "کلید تعبیه کردن که ربع یا نیم پرده زیرتر کردن هر نتی رو در کسری از ثانیه میشه انجام داد",
   "reasoning": "Exact preservation of quarter/half-tone raising and the fraction-of-a-second timing."
  },
  {
   "claim_id": "C016",
   "loglog_ids": [
    "4.2"
   ],
   "claim_text": "جابه‌جایی میان دستگاه‌ها فقط با چند کلیک ممکن شد.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "میشد سریع از هر دستگاهی به هر دستگاه دیگه برم، فقط با چند کلیک، فقط در چند ثانیه",
   "reasoning": "Matches the source's any-dastgah switch via a few clicks in seconds."
  },
  {
   "claim_id": "C017",
   "loglog_ids": [
    "5"
   ],
   "claim_text": "وصال پس از دو سال انتظار: از لنگرود تا لنگفورد.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "دو سالی بود که بهش فکر میکردم ولی نمیدونستم چطور میتونم سالم از لنگرود بیارمش لنگفورد",
   "reasoning": "Two-year wait and the Langroud-to-Langford transport are both stated."
  },
  {
   "claim_id": "C018",
   "loglog_ids": [
    "5.1"
   ],
   "claim_text": "با کمک خانواده و دوستان و مسئولان ساز سالم به دستش رسید.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "با کمکهای بی دریغ خانواده و دوستان و مسئولین و ائمه امروز رسید به دستم",
   "reasoning": "Core claim holds; source additionally lists ائمه, but omission does not alter the asserted meaning."
  },
  {
   "claim_id": "C019",
   "loglog_ids": [
    "5.2"
   ],
   "claim_text": "بی‌وقفه از اصفهان به سه‌گاه و نوا و شور و همایون رفت.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "هی از این دستگاه رفتم تو اون دستگاه، از اصفهان به سه‌گاه، از سه‌گاه به نوا، از نوا به شور، از شور به همایون",
   "reasoning": "The exact dastgah sequence is preserved; the repeated هی supports the continuous reading."
  },
  {
   "claim_id": "C020",
   "loglog_ids": [
    "5.3"
   ],
   "claim_text": "باورش نمی‌شد این کار این‌قدر راحت باشد؛ انگار خواب می‌دید.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "اصلا نمیتونستم تصورش رو هم بکنم که اینقدر راحته این کار، انگار داشتم خواب میدیدم",
   "reasoning": "Close restatement of the disbelief, easiness, and dream-like feeling."
  },
  {
   "claim_id": "C021",
   "loglog_ids": [
    "6"
   ],
   "claim_text": "سرمستی نوازندگی بی‌وقفه و دلتنگی سفر پیش رو.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "هی ساز زدم، اینقدر که پشتم درد گرفت ... حالا از فردا یک هفته‌ای مسافرتم، ناراحتم",
   "reasoning": "Continuous playing and sadness over the upcoming trip are both present."
  },
  {
   "claim_id": "C022",
   "loglog_ids": [
    "6.1"
   ],
   "claim_text": "ناهار نخورد و آن‌قدر زد تا پشتش درد گرفت.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "نهار نخوردم، هی ساز زدم، اینقدر که پشتم درد گرفت",
   "reasoning": "Direct restatement of skipping lunch and playing until back pain."
  },
  {
   "claim_id": "C023",
   "loglog_ids": [
    "6.2"
   ],
   "claim_text": "حس شب اول خاله، کودک آزاد در بازی و گوینده آزاد در سخن.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "حس شب اولی رو داشتم که خاله‌م مضراب‌های سنتور رو داد دستم ... حس کسی رو داشتم که هر حرفی رو میخواست میتونست بزنه",
   "reasoning": "All three feelings from the closing passage are accurately reflected."
  },
  {
   "claim_id": "C024",
   "loglog_ids": [
    "6.3"
   ],
   "claim_text": "از فردا یک هفته سفر است و دلتنگ ساز ننواخته مانده است.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "حالا از فردا یک هفته‌ای مسافرتم، ناراحتم که چرا خونه نیستم که ساز بزنم",
   "reasoning": "One-week trip and sadness at being away from playing are both stated."
  }
 ],
 "metrics": {
  "total_claims": 24,
  "supported": 23,
  "partially_supported": 1,
  "unverifiable": 0,
  "contradicted": 0,
  "critical_errors": 0,
  "faithfulness_precision": 0.9583
 },
 "fail_list": [
  "C003"
 ]
}
```

## Judge Cov (coverage), opencode-go/deepseek-v4.1-flash

```json
{
 "judge": "coverage",
 "judge_version": "1.0.0",
 "model": "opencode-go/deepseek-v4.1-flash (opencode) scripted pipeline 2026-09-15",
 "source_id": "10_parde_begardan_fa",
 "key_points": [
  {
   "point_id": "K01",
   "point_text": "At age 7, at his aunt's house, the author first encountered the santur his cousin had just bought; the cousin let him sit at it and taught him how to hold the mizrab, and he had to be dragged away from it at night's end.",
   "weight": "Must have",
   "presence": "Partial",
   "loglog_ids": [
    "L003",
    "L005"
   ],
   "evidence_quote": "دیدار هفت‌سالگی با سنتور خاله ... آخر شب به‌زور او را از پای ساز بلند کردند",
   "reasoning": "Age 7, the aunt's house, the santur, and being dragged away at night are captured. But the source's actor is the cousin who bought the santur and taught him to hold the mizrab. Loglog reassigns the instrument to the aunt (سنتور خاله) and omits the cousin and the mizrab lesson, so the central origin detail is narrowed."
  },
  {
   "point_id": "K02",
   "point_text": "The first tune he heard on that santur was likely 'Zard Maliheh' (زرد ملیجه), one of the first songs taught to santur beginners.",
   "weight": "Nice to have",
   "presence": "Partial",
   "loglog_ids": [
    "L004"
   ],
   "evidence_quote": "خاله «زرد ملیجه» را نواخت",
   "reasoning": "Zard Maliheh as the tune heard is captured, but the qualifier that it is one of the first songs taught to santur beginners is dropped. Also the source hedges the identification ('likely'), which is lost."
  },
  {
   "point_id": "K03",
   "point_text": "After six months of nagging and sulking, his family finally bought him a santur for 20,000 toman, discounted to 18,000 toman.",
   "weight": "Must have",
   "presence": "Partial",
   "loglog_ids": [
    "L006"
   ],
   "evidence_quote": "شش ماه اصرار تا خرید سنتور هجده‌هزار تومانی انجامید",
   "reasoning": "Six months of insistence and the 18,000-toman purchase price are present, but the original 20,000-toman list price and the discount are dropped. A Must have point with a dropped number is at most Partial."
  },
  {
   "point_id": "K04",
   "point_text": "He started lessons six months later; the teacher initially came to his home because their city had no school, and only later did the Ershad office open a class where the teacher taught.",
   "weight": "Nice to have",
   "presence": "Partial",
   "loglog_ids": [
    "L008"
   ],
   "evidence_quote": "استاد نخست به خانه می‌آمد چون آموزشگاهی در شهر نبود",
   "reasoning": "The teacher coming home because the city had no school is captured, but the six-month delay before lessons and the later Ershad office class are omitted, narrowing the background."
  },
  {
   "point_id": "K05",
   "point_text": "The santur has 72 strings and is hard for an ordinary person to tune, so he had to haul the oversized instrument to class to be tuned, until electronic tuners reached the market and he could tune it himself.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L009",
    "L010"
   ],
   "evidence_quote": "برای کوک ۷۲ سیم به کلاس می‌رفت ... با آمدن تیونر دیگر لازم نبود ساز برای کوک به کلاس برده شود",
   "reasoning": "The 72 strings, hauling the oversized instrument to class for tuning, and the arrival of the tuner that removed the need are all captured with correct meaning."
  },
  {
   "point_id": "K06",
   "point_text": "The santur is a diatonic instrument: only one dastgah/scale can be played at a time, and modulation requires retuning, which is time-consuming.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L011",
    "L012"
   ],
   "evidence_quote": "محدودیت دیاتونیک: یک دستگاه در هر کوک ... مدولاسیون نیازمند صرف زمان برای تغییر کوک بود",
   "reasoning": "The diatonic limitation, one dastgah per tuning, and the time cost of retuning for modulation are all captured intact."
  },
  {
   "point_id": "K07",
   "point_text": "This limitation made him feel like a child at a party allowed only one game: to switch he would have to pack up all his toys first, by which time the mood is gone, or else sit silently aside while the other children move to a game he loves.",
   "weight": "Nice to have",
   "presence": "Present",
   "loglog_ids": [
    "L013",
    "L014"
   ],
   "evidence_quote": "حس بچه‌ای که در مهمانی فقط یک بازی برایش مجاز است ... بازی محبوب دیگران را فقط از گوشه‌ای ساکت نگاه می‌کرد",
   "reasoning": "The core analogy of the child at a party with only one permitted game and watching others' game silently from a corner is captured. The 'packing up toys' clause is absent but the image's meaning survives."
  },
  {
   "point_id": "K08",
   "point_text": "Recently a santur was built inspired by the harp, with a set of keys allowing any note to be lowered by a quarter or half step in a fraction of a second.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L015",
    "L016"
   ],
   "evidence_quote": "سنتور کلیددار الهام‌گرفته از چنگ ... کلیدها هر نت را در کسری از ثانیه ربع یا نیم پرده زیرتر می‌کنند",
   "reasoning": "The harp-inspired keyed santur and the quarter/half-step change in a fraction of a second are captured with the key technical detail intact."
  },
  {
   "point_id": "K09",
   "point_text": "This makes it possible to move quickly from any dastgah to any other with a few clicks, in just seconds.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L015",
    "L017"
   ],
   "evidence_quote": "جابه‌جایی میان دستگاه‌ها فقط با چند کلیک ممکن شد",
   "reasoning": "Moving between dastgahs with a few clicks is captured, and the second-scale speed is stated in L015 (مدولاسیون ثانیه‌ای), so the payoff is preserved."
  },
  {
   "point_id": "K10",
   "point_text": "He had been thinking about such an instrument for two years but did not know how to bring it safely from Langroud to Langford.",
   "weight": "Nice to have",
   "presence": "Present",
   "loglog_ids": [
    "L018"
   ],
   "evidence_quote": "وصال پس از دو سال انتظار: از لنگرود تا لنگفورد",
   "reasoning": "The two years of waiting and the Langroud-to-Langford migration thread are captured in the section heading."
  },
  {
   "point_id": "K11",
   "point_text": "With the unstinting help of family, friends, officials, and clerics/community leaders, the instrument finally reached him today.",
   "weight": "Must have",
   "presence": "Partial",
   "loglog_ids": [
    "L019"
   ],
   "evidence_quote": "با کمک خانواده و دوستان و مسئولان ساز سالم به دستش رسید",
   "reasoning": "The arrival with help from family, friends, and officials is captured, but the clerics/community leaders are omitted and the 'today' timing is dropped, narrowing the credited helper set and the event's immediacy."
  },
  {
   "point_id": "K12",
   "point_text": "He tuned it and played, moving from dastgah to dastgah: Isfahan to Segah, Segah to Nava, Nava to Shur, Shur to Homayoun.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L020"
   ],
   "evidence_quote": "بی‌وقفه از اصفهان به سه‌گاه و نوا و شور و همایون رفت",
   "reasoning": "The full modulation sequence Isfahan to Segah to Nava to Shur to Homayoun is captured with all named dastgahs intact."
  },
  {
   "point_id": "K13",
   "point_text": "He felt like a penned fattened sheep set loose, running without pause: he skipped lunch and played so long his back ached.",
   "weight": "Nice to have",
   "presence": "Partial",
   "loglog_ids": [
    "L023"
   ],
   "evidence_quote": "ناهار نخورد و آن‌قدر زد تا پشتش درد گرفت",
   "reasoning": "Skipping lunch and playing until his back hurt are captured, but the leading sheep-set-loose metaphor is dropped, losing the point's most distinctive image."
  },
  {
   "point_id": "K14",
   "point_text": "He felt like the first night his aunt put the mizrabs in his hand, like a child allowed to play any game he wants, like a person free to say anything he wishes.",
   "weight": "Nice to have",
   "presence": "Present",
   "loglog_ids": [
    "L024"
   ],
   "evidence_quote": "حس شب اول خاله، کودک آزاد در بازی و گوینده آزاد در سخن",
   "reasoning": "All three comparisons, the aunt's first night, the child free in any game, and the speaker free in speech, are captured, and the call-back is noted in L027."
  },
  {
   "point_id": "K15",
   "point_text": "He leaves tomorrow on a week of travel and is unhappy at not being home to play, already waiting to return and sit at the instrument.",
   "weight": "Nice to have",
   "presence": "Present",
   "loglog_ids": [
    "L025"
   ],
   "evidence_quote": "از فردا یک هفته سفر است و دلتنگ ساز ننواخته مانده است",
   "reasoning": "The week of travel starting tomorrow and his longing for the unplayed instrument are captured, preserving the coda."
  }
 ],
 "metrics": {
  "total_points": 15,
  "must_have_total": 8,
  "must_have_present": 5,
  "must_have_partial": 3,
  "must_have_missing": 0,
  "overall_present": 9,
  "must_recall": 0.8125,
  "overall_recall": 0.8
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
 "source_id": "10_parde_begardan_fa",
 "claims": [
  {
   "claim_id": "C001",
   "loglog_ids": [
    "0"
   ],
   "claim_text": "راوی از شیفتگی کودکی به سنتور و محدودیت کوک دیاتونیک آن به سنتور کلیددار تازه‌ای می‌رسد که جابه‌جایی آزاد میان دستگاه‌ها را ممکن می‌کند.",
   "claim_type": "meta",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "سنتور یه ساز دیاتونیک هست ... اگه بخوای مدلاسیون انجام بدی باید کوک عوض بشه ... یه سنتوری درست کردن که از چنگ ایده گرفتن و یه سری کلید تعبیه کردن",
   "reasoning": "Summary faithfully compresses the childhood fascination, the diatonic tuning limit, and the keyed santur enabling free movement."
  },
  {
   "claim_id": "C002",
   "loglog_ids": [
    "1"
   ],
   "claim_text": "شیفتگی آغازین: دیدار هفت‌سالگی با سنتور خاله و اصرار برای داشتن آن.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "۷ سالم که بود یه شب شام خونه خاله‌م بودیم ... تمام طول راه رو زر زدم که سنتور میخوام",
   "reasoning": "Age seven, aunt's santur, and the insistent demand are all present in the source."
  },
  {
   "claim_id": "C003",
   "loglog_ids": [
    "1.1"
   ],
   "claim_text": "سنتور گوشه اتاق بود و خاله «زرد ملیجه» را نواخت.",
   "claim_type": "fact",
   "verdict": "Partially supported",
   "severity": "Minor",
   "evidence_quote": "یه آهنگ هم برامون زد، «زرد ملیجه» بود فکر کنم",
   "reasoning": "Source hedges the song with فکر کنم (I think); loglog states it as certain, dropping the hedge."
  },
  {
   "claim_id": "C004",
   "loglog_ids": [
    "1.2"
   ],
   "claim_text": "آخر شب به‌زور او را از پای ساز بلند کردند.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "آخر شب به زور من رو از پای ساز بلند کردن که بریم خونه",
   "reasoning": "Direct restatement of the source's forced removal from the santur."
  },
  {
   "claim_id": "C005",
   "loglog_ids": [
    "1.3"
   ],
   "claim_text": "شش ماه اصرار تا خرید سنتور هجده‌هزار تومانی انجامید.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "شیش ماه که این زر زدن‌ها و لج‌کردن‌ها ادامه داشت ... ۲۰هزار تومن، با تخفیف شد ۱۸هزار تومن",
   "reasoning": "Six months of insistence and the final 18-thousand price match the source."
  },
  {
   "claim_id": "C006",
   "loglog_ids": [
    "2"
   ],
   "claim_text": "سال‌های آموزش: کلاس، اتاق سرد پذیرایی و دشواری کوک.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "سنتورم تو اتاق پذیرایی بود که همیشه درش بسته بود و سردتر از بقیه اتاقها ... کار هرکسی نیست کوک کردنش",
   "reasoning": "Cold living room, lessons, and tuning difficulty are all stated in the source."
  },
  {
   "claim_id": "C007",
   "loglog_ids": [
    "2.1"
   ],
   "claim_text": "استاد نخست به خانه می‌آمد چون آموزشگاهی در شهر نبود.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "اوایل استادم میومد خونه، چون تو شهرمون آموزشگاهی نبود که من برم",
   "reasoning": "Exact restatement of the early home lessons and absence of a local institute."
  },
  {
   "claim_id": "C008",
   "loglog_ids": [
    "2.2"
   ],
   "claim_text": "ساز بزرگ‌تر از کودک بود و برای کوک ۷۲ سیم به کلاس می‌رفت.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "سازم از خودم گنده‌تر بود ... باید ساز رو میبردم که کوک بشه چون لاکردار ۷۲ تا سیم داره",
   "reasoning": "Both the oversized santur and the 72 strings requiring class tuning are stated."
  },
  {
   "claim_id": "C009",
   "loglog_ids": [
    "2.3"
   ],
   "claim_text": "با آمدن تیونر دیگر لازم نبود ساز برای کوک به کلاس برده شود.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "بعدترها که تیونر اومد بازار دیگه نیاز نبود ساز رو ببرم سر کلاس",
   "reasoning": "Directly restates the source's statement about the tuner removing the need."
  },
  {
   "claim_id": "C010",
   "loglog_ids": [
    "3"
   ],
   "claim_text": "محدودیت دیاتونیک: یک دستگاه در هر کوک و رنج بازی ناتمام.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "در آن واحد فقط میشه یک دستگاه/گام رو روش نواخت ... نمیتونستم بازی دیگه‌ای بکنم",
   "reasoning": "One dastgah per tuning and the incomplete-game feeling are both in the source."
  },
  {
   "claim_id": "C011",
   "loglog_ids": [
    "3.1"
   ],
   "claim_text": "مدولاسیون نیازمند صرف زمان برای تغییر کوک بود.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "اگه بخوای مدلاسیون انجام بدی باید کوک عوض بشه که خب زمانبره",
   "reasoning": "Matches the source's statement that modulation requires time-consuming retuning."
  },
  {
   "claim_id": "C012",
   "loglog_ids": [
    "3.2"
   ],
   "claim_text": "حس بچه‌ای که در مهمانی فقط یک بازی برایش مجاز است.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "حس بچه‌ای رو داشته باشم که تو مهمونی بهش فقط اجازه یه بازی رو داده باشن",
   "reasoning": "Close paraphrase preserving the only-one-game-at-a-party analogy."
  },
  {
   "claim_id": "C013",
   "loglog_ids": [
    "3.3"
   ],
   "claim_text": "بازی محبوب دیگران را فقط از گوشه‌ای ساکت نگاه می‌کرد.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "من مجبور بودم ساکت بشینم یه گوشه‌ای و نگاهشون کنم. حتی اگه اون بازی‌ رو خیلی دوست داشتم",
   "reasoning": "The quiet corner-watching of a game he liked is accurately conveyed."
  },
  {
   "claim_id": "C014",
   "loglog_ids": [
    "4"
   ],
   "claim_text": "گشایش: سنتور کلیددار الهام‌گرفته از چنگ با مدولاسیون ثانیه‌ای.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "یه سنتوری درست کردن که از چنگ ایده گرفتن و یه سری کلید تعبیه کردن ... در کسری از ثانیه",
   "reasoning": "Harp-inspired keyed santur and second-scale modulation are both stated."
  },
  {
   "claim_id": "C015",
   "loglog_ids": [
    "4.1"
   ],
   "claim_text": "کلیدها هر نت را در کسری از ثانیه ربع یا نیم پرده زیرتر می‌کنند.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "کلید تعبیه کردن که ربع یا نیم پرده زیرتر کردن هر نتی رو در کسری از ثانیه میشه انجام داد",
   "reasoning": "Exact preservation of quarter/half-tone raising and the fraction-of-a-second timing."
  },
  {
   "claim_id": "C016",
   "loglog_ids": [
    "4.2"
   ],
   "claim_text": "جابه‌جایی میان دستگاه‌ها فقط با چند کلیک ممکن شد.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "میشد سریع از هر دستگاهی به هر دستگاه دیگه برم، فقط با چند کلیک، فقط در چند ثانیه",
   "reasoning": "Matches the source's any-dastgah switch via a few clicks in seconds."
  },
  {
   "claim_id": "C017",
   "loglog_ids": [
    "5"
   ],
   "claim_text": "وصال پس از دو سال انتظار: از لنگرود تا لنگفورد.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "دو سالی بود که بهش فکر میکردم ولی نمیدونستم چطور میتونم سالم از لنگرود بیارمش لنگفورد",
   "reasoning": "Two-year wait and the Langroud-to-Langford transport are both stated."
  },
  {
   "claim_id": "C018",
   "loglog_ids": [
    "5.1"
   ],
   "claim_text": "با کمک خانواده و دوستان و مسئولان ساز سالم به دستش رسید.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "با کمکهای بی دریغ خانواده و دوستان و مسئولین و ائمه امروز رسید به دستم",
   "reasoning": "Core claim holds; source additionally lists ائمه, but omission does not alter the asserted meaning."
  },
  {
   "claim_id": "C019",
   "loglog_ids": [
    "5.2"
   ],
   "claim_text": "بی‌وقفه از اصفهان به سه‌گاه و نوا و شور و همایون رفت.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "هی از این دستگاه رفتم تو اون دستگاه، از اصفهان به سه‌گاه، از سه‌گاه به نوا، از نوا به شور، از شور به همایون",
   "reasoning": "The exact dastgah sequence is preserved; the repeated هی supports the continuous reading."
  },
  {
   "claim_id": "C020",
   "loglog_ids": [
    "5.3"
   ],
   "claim_text": "باورش نمی‌شد این کار این‌قدر راحت باشد؛ انگار خواب می‌دید.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "اصلا نمیتونستم تصورش رو هم بکنم که اینقدر راحته این کار، انگار داشتم خواب میدیدم",
   "reasoning": "Close restatement of the disbelief, easiness, and dream-like feeling."
  },
  {
   "claim_id": "C021",
   "loglog_ids": [
    "6"
   ],
   "claim_text": "سرمستی نوازندگی بی‌وقفه و دلتنگی سفر پیش رو.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "هی ساز زدم، اینقدر که پشتم درد گرفت ... حالا از فردا یک هفته‌ای مسافرتم، ناراحتم",
   "reasoning": "Continuous playing and sadness over the upcoming trip are both present."
  },
  {
   "claim_id": "C022",
   "loglog_ids": [
    "6.1"
   ],
   "claim_text": "ناهار نخورد و آن‌قدر زد تا پشتش درد گرفت.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "نهار نخوردم، هی ساز زدم، اینقدر که پشتم درد گرفت",
   "reasoning": "Direct restatement of skipping lunch and playing until back pain."
  },
  {
   "claim_id": "C023",
   "loglog_ids": [
    "6.2"
   ],
   "claim_text": "حس شب اول خاله، کودک آزاد در بازی و گوینده آزاد در سخن.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "حس شب اولی رو داشتم که خاله‌م مضراب‌های سنتور رو داد دستم ... حس کسی رو داشتم که هر حرفی رو میخواست میتونست بزنه",
   "reasoning": "All three feelings from the closing passage are accurately reflected."
  },
  {
   "claim_id": "C024",
   "loglog_ids": [
    "6.3"
   ],
   "claim_text": "از فردا یک هفته سفر است و دلتنگ ساز ننواخته مانده است.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "حالا از فردا یک هفته‌ای مسافرتم، ناراحتم که چرا خونه نیستم که ساز بزنم",
   "reasoning": "One-week trip and sadness at being away from playing are both stated."
  }
 ],
 "metrics": {
  "total_claims": 24,
  "supported": 23,
  "partially_supported": 1,
  "unverifiable": 0,
  "contradicted": 0,
  "critical_errors": 0,
  "faithfulness_precision": 0.9583
 },
 "fail_list": [
  "C003"
 ]
}
```

## Judge Cov (coverage), opencode-go/deepseek-v4.1-flash

```json
{
 "judge": "coverage",
 "judge_version": "1.0.0",
 "model": "opencode-go/deepseek-v4.1-flash (opencode) scripted pipeline 2026-09-15",
 "source_id": "10_parde_begardan_fa",
 "key_points": [
  {
   "point_id": "K01",
   "point_text": "At age 7, at his aunt's house, the author first encountered the santur his cousin had just bought; the cousin let him sit at it and taught him how to hold the mizrab, and he had to be dragged away from it at night's end.",
   "weight": "Must have",
   "presence": "Partial",
   "loglog_ids": [
    "L003",
    "L005"
   ],
   "evidence_quote": "دیدار هفت‌سالگی با سنتور خاله ... آخر شب به‌زور او را از پای ساز بلند کردند",
   "reasoning": "Age 7, the aunt's house, the santur, and being dragged away at night are captured. But the source's actor is the cousin who bought the santur and taught him to hold the mizrab. Loglog reassigns the instrument to the aunt (سنتور خاله) and omits the cousin and the mizrab lesson, so the central origin detail is narrowed."
  },
  {
   "point_id": "K02",
   "point_text": "The first tune he heard on that santur was likely 'Zard Maliheh' (زرد ملیجه), one of the first songs taught to santur beginners.",
   "weight": "Nice to have",
   "presence": "Partial",
   "loglog_ids": [
    "L004"
   ],
   "evidence_quote": "خاله «زرد ملیجه» را نواخت",
   "reasoning": "Zard Maliheh as the tune heard is captured, but the qualifier that it is one of the first songs taught to santur beginners is dropped. Also the source hedges the identification ('likely'), which is lost."
  },
  {
   "point_id": "K03",
   "point_text": "After six months of nagging and sulking, his family finally bought him a santur for 20,000 toman, discounted to 18,000 toman.",
   "weight": "Must have",
   "presence": "Partial",
   "loglog_ids": [
    "L006"
   ],
   "evidence_quote": "شش ماه اصرار تا خرید سنتور هجده‌هزار تومانی انجامید",
   "reasoning": "Six months of insistence and the 18,000-toman purchase price are present, but the original 20,000-toman list price and the discount are dropped. A Must have point with a dropped number is at most Partial."
  },
  {
   "point_id": "K04",
   "point_text": "He started lessons six months later; the teacher initially came to his home because their city had no school, and only later did the Ershad office open a class where the teacher taught.",
   "weight": "Nice to have",
   "presence": "Partial",
   "loglog_ids": [
    "L008"
   ],
   "evidence_quote": "استاد نخست به خانه می‌آمد چون آموزشگاهی در شهر نبود",
   "reasoning": "The teacher coming home because the city had no school is captured, but the six-month delay before lessons and the later Ershad office class are omitted, narrowing the background."
  },
  {
   "point_id": "K05",
   "point_text": "The santur has 72 strings and is hard for an ordinary person to tune, so he had to haul the oversized instrument to class to be tuned, until electronic tuners reached the market and he could tune it himself.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L009",
    "L010"
   ],
   "evidence_quote": "برای کوک ۷۲ سیم به کلاس می‌رفت ... با آمدن تیونر دیگر لازم نبود ساز برای کوک به کلاس برده شود",
   "reasoning": "The 72 strings, hauling the oversized instrument to class for tuning, and the arrival of the tuner that removed the need are all captured with correct meaning."
  },
  {
   "point_id": "K06",
   "point_text": "The santur is a diatonic instrument: only one dastgah/scale can be played at a time, and modulation requires retuning, which is time-consuming.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L011",
    "L012"
   ],
   "evidence_quote": "محدودیت دیاتونیک: یک دستگاه در هر کوک ... مدولاسیون نیازمند صرف زمان برای تغییر کوک بود",
   "reasoning": "The diatonic limitation, one dastgah per tuning, and the time cost of retuning for modulation are all captured intact."
  },
  {
   "point_id": "K07",
   "point_text": "This limitation made him feel like a child at a party allowed only one game: to switch he would have to pack up all his toys first, by which time the mood is gone, or else sit silently aside while the other children move to a game he loves.",
   "weight": "Nice to have",
   "presence": "Present",
   "loglog_ids": [
    "L013",
    "L014"
   ],
   "evidence_quote": "حس بچه‌ای که در مهمانی فقط یک بازی برایش مجاز است ... بازی محبوب دیگران را فقط از گوشه‌ای ساکت نگاه می‌کرد",
   "reasoning": "The core analogy of the child at a party with only one permitted game and watching others' game silently from a corner is captured. The 'packing up toys' clause is absent but the image's meaning survives."
  },
  {
   "point_id": "K08",
   "point_text": "Recently a santur was built inspired by the harp, with a set of keys allowing any note to be lowered by a quarter or half step in a fraction of a second.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L015",
    "L016"
   ],
   "evidence_quote": "سنتور کلیددار الهام‌گرفته از چنگ ... کلیدها هر نت را در کسری از ثانیه ربع یا نیم پرده زیرتر می‌کنند",
   "reasoning": "The harp-inspired keyed santur and the quarter/half-step change in a fraction of a second are captured with the key technical detail intact."
  },
  {
   "point_id": "K09",
   "point_text": "This makes it possible to move quickly from any dastgah to any other with a few clicks, in just seconds.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L015",
    "L017"
   ],
   "evidence_quote": "جابه‌جایی میان دستگاه‌ها فقط با چند کلیک ممکن شد",
   "reasoning": "Moving between dastgahs with a few clicks is captured, and the second-scale speed is stated in L015 (مدولاسیون ثانیه‌ای), so the payoff is preserved."
  },
  {
   "point_id": "K10",
   "point_text": "He had been thinking about such an instrument for two years but did not know how to bring it safely from Langroud to Langford.",
   "weight": "Nice to have",
   "presence": "Present",
   "loglog_ids": [
    "L018"
   ],
   "evidence_quote": "وصال پس از دو سال انتظار: از لنگرود تا لنگفورد",
   "reasoning": "The two years of waiting and the Langroud-to-Langford migration thread are captured in the section heading."
  },
  {
   "point_id": "K11",
   "point_text": "With the unstinting help of family, friends, officials, and clerics/community leaders, the instrument finally reached him today.",
   "weight": "Must have",
   "presence": "Partial",
   "loglog_ids": [
    "L019"
   ],
   "evidence_quote": "با کمک خانواده و دوستان و مسئولان ساز سالم به دستش رسید",
   "reasoning": "The arrival with help from family, friends, and officials is captured, but the clerics/community leaders are omitted and the 'today' timing is dropped, narrowing the credited helper set and the event's immediacy."
  },
  {
   "point_id": "K12",
   "point_text": "He tuned it and played, moving from dastgah to dastgah: Isfahan to Segah, Segah to Nava, Nava to Shur, Shur to Homayoun.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L020"
   ],
   "evidence_quote": "بی‌وقفه از اصفهان به سه‌گاه و نوا و شور و همایون رفت",
   "reasoning": "The full modulation sequence Isfahan to Segah to Nava to Shur to Homayoun is captured with all named dastgahs intact."
  },
  {
   "point_id": "K13",
   "point_text": "He felt like a penned fattened sheep set loose, running without pause: he skipped lunch and played so long his back ached.",
   "weight": "Nice to have",
   "presence": "Partial",
   "loglog_ids": [
    "L023"
   ],
   "evidence_quote": "ناهار نخورد و آن‌قدر زد تا پشتش درد گرفت",
   "reasoning": "Skipping lunch and playing until his back hurt are captured, but the leading sheep-set-loose metaphor is dropped, losing the point's most distinctive image."
  },
  {
   "point_id": "K14",
   "point_text": "He felt like the first night his aunt put the mizrabs in his hand, like a child allowed to play any game he wants, like a person free to say anything he wishes.",
   "weight": "Nice to have",
   "presence": "Present",
   "loglog_ids": [
    "L024"
   ],
   "evidence_quote": "حس شب اول خاله، کودک آزاد در بازی و گوینده آزاد در سخن",
   "reasoning": "All three comparisons, the aunt's first night, the child free in any game, and the speaker free in speech, are captured, and the call-back is noted in L027."
  },
  {
   "point_id": "K15",
   "point_text": "He leaves tomorrow on a week of travel and is unhappy at not being home to play, already waiting to return and sit at the instrument.",
   "weight": "Nice to have",
   "presence": "Present",
   "loglog_ids": [
    "L025"
   ],
   "evidence_quote": "از فردا یک هفته سفر است و دلتنگ ساز ننواخته مانده است",
   "reasoning": "The week of travel starting tomorrow and his longing for the unplayed instrument are captured, preserving the coda."
  }
 ],
 "metrics": {
  "total_points": 15,
  "must_have_total": 8,
  "must_have_present": 5,
  "must_have_partial": 3,
  "must_have_missing": 0,
  "overall_present": 9,
  "must_recall": 0.8125,
  "overall_recall": 0.8
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
 "source_id": "10_parde_begardan_fa",
 "labels": [
  {
   "claim_id": "C001",
   "loglog_ids": [
    "0"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Thesis states the full childhood-to-keyed-santur arc; frames piece, not restated as one claim."
  },
  {
   "claim_id": "C002",
   "loglog_ids": [
    "1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Theme adds age seven and initial-fascination framing absent from subpoints."
  },
  {
   "claim_id": "C003",
   "loglog_ids": [
    "1.1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Concrete scene plus named piece «زرد ملیجه» carry detail found nowhere else."
  },
  {
   "claim_id": "C004",
   "loglog_ids": [
    "1.2"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Canonical late-night scene; earliest occurrence, later branch restates it."
  },
  {
   "claim_id": "C005",
   "loglog_ids": [
    "1.3"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Carries numbers: six months insistence and eighteen-thousand-toman price."
  },
  {
   "claim_id": "C006",
   "loglog_ids": [
    "2"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Theme adds cold reception room detail absent from its subpoints."
  },
  {
   "claim_id": "C007",
   "loglog_ids": [
    "2.1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Explains why teacher came home; unique causal fact."
  },
  {
   "claim_id": "C008",
   "loglog_ids": [
    "2.2"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Carries 72-string tuning detail and instrument-child size comparison."
  },
  {
   "claim_id": "C009",
   "loglog_ids": [
    "2.3"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Tuner removing need to carry instrument is a new causal fact."
  },
  {
   "claim_id": "C010",
   "loglog_ids": [
    "3"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Theme states one-dastgah-per-tuning and unfinished play-range limitation."
  },
  {
   "claim_id": "C011",
   "loglog_ids": [
    "3.1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Retuning-time mechanism is distinct from the theme statement."
  },
  {
   "claim_id": "C012",
   "loglog_ids": [
    "3.2"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Party-game analogy illustrates limitation; no earlier equivalent claim."
  },
  {
   "claim_id": "C013",
   "loglog_ids": [
    "3.3"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Adds corner-watching behavior image, distinct from C012's inner feeling."
  },
  {
   "claim_id": "C014",
   "loglog_ids": [
    "4"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Theme adds harp inspiration absent from its evidence lines."
  },
  {
   "claim_id": "C015",
   "loglog_ids": [
    "4.1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Quarter/half-step instant retuning detail is unique evidence."
  },
  {
   "claim_id": "C016",
   "loglog_ids": [
    "4.2"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Few-clicks switching is the concrete solution claim."
  },
  {
   "claim_id": "C017",
   "loglog_ids": [
    "5"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Carries two-year wait and Langarud/Loughborough place names."
  },
  {
   "claim_id": "C018",
   "loglog_ids": [
    "5.1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Family, friends, and officials help detail is unique."
  },
  {
   "claim_id": "C019",
   "loglog_ids": [
    "5.2"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Names four dastgahs traversed; unique example."
  },
  {
   "claim_id": "C020",
   "loglog_ids": [
    "5.3"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Disbelief and dream-like reaction is a distinct interpretation."
  },
  {
   "claim_id": "C021",
   "loglog_ids": [
    "6"
   ],
   "label": "Trivia",
   "canonical_id": null,
   "reasoning": "Theme header restates 6.1 and 6.3 with no number, caveat, or new detail."
  },
  {
   "claim_id": "C022",
   "loglog_ids": [
    "6.1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Skipped lunch and back-pain evidence is concrete and unique."
  },
  {
   "claim_id": "C023",
   "loglog_ids": [
    "6.2"
   ],
   "label": "Duplicate",
   "canonical_id": "C004",
   "reasoning": "Restates C004's late-night scene; cross-link confirms the repeat."
  },
  {
   "claim_id": "C024",
   "loglog_ids": [
    "6.3"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "One-week trip and unplayed-instrument longing add specifics."
  }
 ],
 "metrics": {
  "scored_claims": 24,
  "unique": 22,
  "duplicates": 1,
  "trivia": 1,
  "redundancy_rate": 0.0417,
  "trivia_rate": 0.0417,
  "structured_tokens": 429,
  "tokens_per_unique_claim": 19.5
 },
 "prune_list": [
  "C023 duplicates C004, safe to merge",
  "C021 header restates C022 and C024, candidate to drop"
 ]
}
```

## Judge F (faithfulness), opencode-go/deepseek-v4.1-flash

```json
{
 "judge": "faithfulness",
 "judge_version": "1.0.0",
 "model": "opencode-go/deepseek-v4.1-flash (opencode) scripted pipeline 2026-09-15",
 "source_id": "10_parde_begardan_fa",
 "claims": [
  {
   "claim_id": "C001",
   "loglog_ids": [
    "0"
   ],
   "claim_text": "راوی از شیفتگی کودکی به سنتور و محدودیت کوک دیاتونیک آن به سنتور کلیددار تازه‌ای می‌رسد که جابه‌جایی آزاد میان دستگاه‌ها را ممکن می‌کند.",
   "claim_type": "meta",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "سنتور یه ساز دیاتونیک هست ... اگه بخوای مدلاسیون انجام بدی باید کوک عوض بشه ... یه سنتوری درست کردن که از چنگ ایده گرفتن و یه سری کلید تعبیه کردن",
   "reasoning": "Summary faithfully compresses the childhood fascination, the diatonic tuning limit, and the keyed santur enabling free movement."
  },
  {
   "claim_id": "C002",
   "loglog_ids": [
    "1"
   ],
   "claim_text": "شیفتگی آغازین: دیدار هفت‌سالگی با سنتور خاله و اصرار برای داشتن آن.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "۷ سالم که بود یه شب شام خونه خاله‌م بودیم ... تمام طول راه رو زر زدم که سنتور میخوام",
   "reasoning": "Age seven, aunt's santur, and the insistent demand are all present in the source."
  },
  {
   "claim_id": "C003",
   "loglog_ids": [
    "1.1"
   ],
   "claim_text": "سنتور گوشه اتاق بود و خاله «زرد ملیجه» را نواخت.",
   "claim_type": "fact",
   "verdict": "Partially supported",
   "severity": "Minor",
   "evidence_quote": "یه آهنگ هم برامون زد، «زرد ملیجه» بود فکر کنم",
   "reasoning": "Source hedges the song with فکر کنم (I think); loglog states it as certain, dropping the hedge."
  },
  {
   "claim_id": "C004",
   "loglog_ids": [
    "1.2"
   ],
   "claim_text": "آخر شب به‌زور او را از پای ساز بلند کردند.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "آخر شب به زور من رو از پای ساز بلند کردن که بریم خونه",
   "reasoning": "Direct restatement of the source's forced removal from the santur."
  },
  {
   "claim_id": "C005",
   "loglog_ids": [
    "1.3"
   ],
   "claim_text": "شش ماه اصرار تا خرید سنتور هجده‌هزار تومانی انجامید.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "شیش ماه که این زر زدن‌ها و لج‌کردن‌ها ادامه داشت ... ۲۰هزار تومن، با تخفیف شد ۱۸هزار تومن",
   "reasoning": "Six months of insistence and the final 18-thousand price match the source."
  },
  {
   "claim_id": "C006",
   "loglog_ids": [
    "2"
   ],
   "claim_text": "سال‌های آموزش: کلاس، اتاق سرد پذیرایی و دشواری کوک.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "سنتورم تو اتاق پذیرایی بود که همیشه درش بسته بود و سردتر از بقیه اتاقها ... کار هرکسی نیست کوک کردنش",
   "reasoning": "Cold living room, lessons, and tuning difficulty are all stated in the source."
  },
  {
   "claim_id": "C007",
   "loglog_ids": [
    "2.1"
   ],
   "claim_text": "استاد نخست به خانه می‌آمد چون آموزشگاهی در شهر نبود.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "اوایل استادم میومد خونه، چون تو شهرمون آموزشگاهی نبود که من برم",
   "reasoning": "Exact restatement of the early home lessons and absence of a local institute."
  },
  {
   "claim_id": "C008",
   "loglog_ids": [
    "2.2"
   ],
   "claim_text": "ساز بزرگ‌تر از کودک بود و برای کوک ۷۲ سیم به کلاس می‌رفت.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "سازم از خودم گنده‌تر بود ... باید ساز رو میبردم که کوک بشه چون لاکردار ۷۲ تا سیم داره",
   "reasoning": "Both the oversized santur and the 72 strings requiring class tuning are stated."
  },
  {
   "claim_id": "C009",
   "loglog_ids": [
    "2.3"
   ],
   "claim_text": "با آمدن تیونر دیگر لازم نبود ساز برای کوک به کلاس برده شود.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "بعدترها که تیونر اومد بازار دیگه نیاز نبود ساز رو ببرم سر کلاس",
   "reasoning": "Directly restates the source's statement about the tuner removing the need."
  },
  {
   "claim_id": "C010",
   "loglog_ids": [
    "3"
   ],
   "claim_text": "محدودیت دیاتونیک: یک دستگاه در هر کوک و رنج بازی ناتمام.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "در آن واحد فقط میشه یک دستگاه/گام رو روش نواخت ... نمیتونستم بازی دیگه‌ای بکنم",
   "reasoning": "One dastgah per tuning and the incomplete-game feeling are both in the source."
  },
  {
   "claim_id": "C011",
   "loglog_ids": [
    "3.1"
   ],
   "claim_text": "مدولاسیون نیازمند صرف زمان برای تغییر کوک بود.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "اگه بخوای مدلاسیون انجام بدی باید کوک عوض بشه که خب زمانبره",
   "reasoning": "Matches the source's statement that modulation requires time-consuming retuning."
  },
  {
   "claim_id": "C012",
   "loglog_ids": [
    "3.2"
   ],
   "claim_text": "حس بچه‌ای که در مهمانی فقط یک بازی برایش مجاز است.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "حس بچه‌ای رو داشته باشم که تو مهمونی بهش فقط اجازه یه بازی رو داده باشن",
   "reasoning": "Close paraphrase preserving the only-one-game-at-a-party analogy."
  },
  {
   "claim_id": "C013",
   "loglog_ids": [
    "3.3"
   ],
   "claim_text": "بازی محبوب دیگران را فقط از گوشه‌ای ساکت نگاه می‌کرد.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "من مجبور بودم ساکت بشینم یه گوشه‌ای و نگاهشون کنم. حتی اگه اون بازی‌ رو خیلی دوست داشتم",
   "reasoning": "The quiet corner-watching of a game he liked is accurately conveyed."
  },
  {
   "claim_id": "C014",
   "loglog_ids": [
    "4"
   ],
   "claim_text": "گشایش: سنتور کلیددار الهام‌گرفته از چنگ با مدولاسیون ثانیه‌ای.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "یه سنتوری درست کردن که از چنگ ایده گرفتن و یه سری کلید تعبیه کردن ... در کسری از ثانیه",
   "reasoning": "Harp-inspired keyed santur and second-scale modulation are both stated."
  },
  {
   "claim_id": "C015",
   "loglog_ids": [
    "4.1"
   ],
   "claim_text": "کلیدها هر نت را در کسری از ثانیه ربع یا نیم پرده زیرتر می‌کنند.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "کلید تعبیه کردن که ربع یا نیم پرده زیرتر کردن هر نتی رو در کسری از ثانیه میشه انجام داد",
   "reasoning": "Exact preservation of quarter/half-tone raising and the fraction-of-a-second timing."
  },
  {
   "claim_id": "C016",
   "loglog_ids": [
    "4.2"
   ],
   "claim_text": "جابه‌جایی میان دستگاه‌ها فقط با چند کلیک ممکن شد.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "میشد سریع از هر دستگاهی به هر دستگاه دیگه برم، فقط با چند کلیک، فقط در چند ثانیه",
   "reasoning": "Matches the source's any-dastgah switch via a few clicks in seconds."
  },
  {
   "claim_id": "C017",
   "loglog_ids": [
    "5"
   ],
   "claim_text": "وصال پس از دو سال انتظار: از لنگرود تا لنگفورد.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "دو سالی بود که بهش فکر میکردم ولی نمیدونستم چطور میتونم سالم از لنگرود بیارمش لنگفورد",
   "reasoning": "Two-year wait and the Langroud-to-Langford transport are both stated."
  },
  {
   "claim_id": "C018",
   "loglog_ids": [
    "5.1"
   ],
   "claim_text": "با کمک خانواده و دوستان و مسئولان ساز سالم به دستش رسید.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "با کمکهای بی دریغ خانواده و دوستان و مسئولین و ائمه امروز رسید به دستم",
   "reasoning": "Core claim holds; source additionally lists ائمه, but omission does not alter the asserted meaning."
  },
  {
   "claim_id": "C019",
   "loglog_ids": [
    "5.2"
   ],
   "claim_text": "بی‌وقفه از اصفهان به سه‌گاه و نوا و شور و همایون رفت.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "هی از این دستگاه رفتم تو اون دستگاه، از اصفهان به سه‌گاه، از سه‌گاه به نوا، از نوا به شور، از شور به همایون",
   "reasoning": "The exact dastgah sequence is preserved; the repeated هی supports the continuous reading."
  },
  {
   "claim_id": "C020",
   "loglog_ids": [
    "5.3"
   ],
   "claim_text": "باورش نمی‌شد این کار این‌قدر راحت باشد؛ انگار خواب می‌دید.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "اصلا نمیتونستم تصورش رو هم بکنم که اینقدر راحته این کار، انگار داشتم خواب میدیدم",
   "reasoning": "Close restatement of the disbelief, easiness, and dream-like feeling."
  },
  {
   "claim_id": "C021",
   "loglog_ids": [
    "6"
   ],
   "claim_text": "سرمستی نوازندگی بی‌وقفه و دلتنگی سفر پیش رو.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "هی ساز زدم، اینقدر که پشتم درد گرفت ... حالا از فردا یک هفته‌ای مسافرتم، ناراحتم",
   "reasoning": "Continuous playing and sadness over the upcoming trip are both present."
  },
  {
   "claim_id": "C022",
   "loglog_ids": [
    "6.1"
   ],
   "claim_text": "ناهار نخورد و آن‌قدر زد تا پشتش درد گرفت.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "نهار نخوردم، هی ساز زدم، اینقدر که پشتم درد گرفت",
   "reasoning": "Direct restatement of skipping lunch and playing until back pain."
  },
  {
   "claim_id": "C023",
   "loglog_ids": [
    "6.2"
   ],
   "claim_text": "حس شب اول خاله، کودک آزاد در بازی و گوینده آزاد در سخن.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "حس شب اولی رو داشتم که خاله‌م مضراب‌های سنتور رو داد دستم ... حس کسی رو داشتم که هر حرفی رو میخواست میتونست بزنه",
   "reasoning": "All three feelings from the closing passage are accurately reflected."
  },
  {
   "claim_id": "C024",
   "loglog_ids": [
    "6.3"
   ],
   "claim_text": "از فردا یک هفته سفر است و دلتنگ ساز ننواخته مانده است.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "حالا از فردا یک هفته‌ای مسافرتم، ناراحتم که چرا خونه نیستم که ساز بزنم",
   "reasoning": "One-week trip and sadness at being away from playing are both stated."
  }
 ],
 "metrics": {
  "total_claims": 24,
  "supported": 23,
  "partially_supported": 1,
  "unverifiable": 0,
  "contradicted": 0,
  "critical_errors": 0,
  "faithfulness_precision": 0.9583
 },
 "fail_list": [
  "C003"
 ]
}
```

## Judge Cov (coverage), opencode-go/deepseek-v4.1-flash

```json
{
 "judge": "coverage",
 "judge_version": "1.0.0",
 "model": "opencode-go/deepseek-v4.1-flash (opencode) scripted pipeline 2026-09-15",
 "source_id": "10_parde_begardan_fa",
 "key_points": [
  {
   "point_id": "K01",
   "point_text": "At age 7, at his aunt's house, the author first encountered the santur his cousin had just bought; the cousin let him sit at it and taught him how to hold the mizrab, and he had to be dragged away from it at night's end.",
   "weight": "Must have",
   "presence": "Partial",
   "loglog_ids": [
    "L003",
    "L005"
   ],
   "evidence_quote": "دیدار هفت‌سالگی با سنتور خاله ... آخر شب به‌زور او را از پای ساز بلند کردند",
   "reasoning": "Age 7, the aunt's house, the santur, and being dragged away at night are captured. But the source's actor is the cousin who bought the santur and taught him to hold the mizrab. Loglog reassigns the instrument to the aunt (سنتور خاله) and omits the cousin and the mizrab lesson, so the central origin detail is narrowed."
  },
  {
   "point_id": "K02",
   "point_text": "The first tune he heard on that santur was likely 'Zard Maliheh' (زرد ملیجه), one of the first songs taught to santur beginners.",
   "weight": "Nice to have",
   "presence": "Partial",
   "loglog_ids": [
    "L004"
   ],
   "evidence_quote": "خاله «زرد ملیجه» را نواخت",
   "reasoning": "Zard Maliheh as the tune heard is captured, but the qualifier that it is one of the first songs taught to santur beginners is dropped. Also the source hedges the identification ('likely'), which is lost."
  },
  {
   "point_id": "K03",
   "point_text": "After six months of nagging and sulking, his family finally bought him a santur for 20,000 toman, discounted to 18,000 toman.",
   "weight": "Must have",
   "presence": "Partial",
   "loglog_ids": [
    "L006"
   ],
   "evidence_quote": "شش ماه اصرار تا خرید سنتور هجده‌هزار تومانی انجامید",
   "reasoning": "Six months of insistence and the 18,000-toman purchase price are present, but the original 20,000-toman list price and the discount are dropped. A Must have point with a dropped number is at most Partial."
  },
  {
   "point_id": "K04",
   "point_text": "He started lessons six months later; the teacher initially came to his home because their city had no school, and only later did the Ershad office open a class where the teacher taught.",
   "weight": "Nice to have",
   "presence": "Partial",
   "loglog_ids": [
    "L008"
   ],
   "evidence_quote": "استاد نخست به خانه می‌آمد چون آموزشگاهی در شهر نبود",
   "reasoning": "The teacher coming home because the city had no school is captured, but the six-month delay before lessons and the later Ershad office class are omitted, narrowing the background."
  },
  {
   "point_id": "K05",
   "point_text": "The santur has 72 strings and is hard for an ordinary person to tune, so he had to haul the oversized instrument to class to be tuned, until electronic tuners reached the market and he could tune it himself.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L009",
    "L010"
   ],
   "evidence_quote": "برای کوک ۷۲ سیم به کلاس می‌رفت ... با آمدن تیونر دیگر لازم نبود ساز برای کوک به کلاس برده شود",
   "reasoning": "The 72 strings, hauling the oversized instrument to class for tuning, and the arrival of the tuner that removed the need are all captured with correct meaning."
  },
  {
   "point_id": "K06",
   "point_text": "The santur is a diatonic instrument: only one dastgah/scale can be played at a time, and modulation requires retuning, which is time-consuming.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L011",
    "L012"
   ],
   "evidence_quote": "محدودیت دیاتونیک: یک دستگاه در هر کوک ... مدولاسیون نیازمند صرف زمان برای تغییر کوک بود",
   "reasoning": "The diatonic limitation, one dastgah per tuning, and the time cost of retuning for modulation are all captured intact."
  },
  {
   "point_id": "K07",
   "point_text": "This limitation made him feel like a child at a party allowed only one game: to switch he would have to pack up all his toys first, by which time the mood is gone, or else sit silently aside while the other children move to a game he loves.",
   "weight": "Nice to have",
   "presence": "Present",
   "loglog_ids": [
    "L013",
    "L014"
   ],
   "evidence_quote": "حس بچه‌ای که در مهمانی فقط یک بازی برایش مجاز است ... بازی محبوب دیگران را فقط از گوشه‌ای ساکت نگاه می‌کرد",
   "reasoning": "The core analogy of the child at a party with only one permitted game and watching others' game silently from a corner is captured. The 'packing up toys' clause is absent but the image's meaning survives."
  },
  {
   "point_id": "K08",
   "point_text": "Recently a santur was built inspired by the harp, with a set of keys allowing any note to be lowered by a quarter or half step in a fraction of a second.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L015",
    "L016"
   ],
   "evidence_quote": "سنتور کلیددار الهام‌گرفته از چنگ ... کلیدها هر نت را در کسری از ثانیه ربع یا نیم پرده زیرتر می‌کنند",
   "reasoning": "The harp-inspired keyed santur and the quarter/half-step change in a fraction of a second are captured with the key technical detail intact."
  },
  {
   "point_id": "K09",
   "point_text": "This makes it possible to move quickly from any dastgah to any other with a few clicks, in just seconds.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L015",
    "L017"
   ],
   "evidence_quote": "جابه‌جایی میان دستگاه‌ها فقط با چند کلیک ممکن شد",
   "reasoning": "Moving between dastgahs with a few clicks is captured, and the second-scale speed is stated in L015 (مدولاسیون ثانیه‌ای), so the payoff is preserved."
  },
  {
   "point_id": "K10",
   "point_text": "He had been thinking about such an instrument for two years but did not know how to bring it safely from Langroud to Langford.",
   "weight": "Nice to have",
   "presence": "Present",
   "loglog_ids": [
    "L018"
   ],
   "evidence_quote": "وصال پس از دو سال انتظار: از لنگرود تا لنگفورد",
   "reasoning": "The two years of waiting and the Langroud-to-Langford migration thread are captured in the section heading."
  },
  {
   "point_id": "K11",
   "point_text": "With the unstinting help of family, friends, officials, and clerics/community leaders, the instrument finally reached him today.",
   "weight": "Must have",
   "presence": "Partial",
   "loglog_ids": [
    "L019"
   ],
   "evidence_quote": "با کمک خانواده و دوستان و مسئولان ساز سالم به دستش رسید",
   "reasoning": "The arrival with help from family, friends, and officials is captured, but the clerics/community leaders are omitted and the 'today' timing is dropped, narrowing the credited helper set and the event's immediacy."
  },
  {
   "point_id": "K12",
   "point_text": "He tuned it and played, moving from dastgah to dastgah: Isfahan to Segah, Segah to Nava, Nava to Shur, Shur to Homayoun.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L020"
   ],
   "evidence_quote": "بی‌وقفه از اصفهان به سه‌گاه و نوا و شور و همایون رفت",
   "reasoning": "The full modulation sequence Isfahan to Segah to Nava to Shur to Homayoun is captured with all named dastgahs intact."
  },
  {
   "point_id": "K13",
   "point_text": "He felt like a penned fattened sheep set loose, running without pause: he skipped lunch and played so long his back ached.",
   "weight": "Nice to have",
   "presence": "Partial",
   "loglog_ids": [
    "L023"
   ],
   "evidence_quote": "ناهار نخورد و آن‌قدر زد تا پشتش درد گرفت",
   "reasoning": "Skipping lunch and playing until his back hurt are captured, but the leading sheep-set-loose metaphor is dropped, losing the point's most distinctive image."
  },
  {
   "point_id": "K14",
   "point_text": "He felt like the first night his aunt put the mizrabs in his hand, like a child allowed to play any game he wants, like a person free to say anything he wishes.",
   "weight": "Nice to have",
   "presence": "Present",
   "loglog_ids": [
    "L024"
   ],
   "evidence_quote": "حس شب اول خاله، کودک آزاد در بازی و گوینده آزاد در سخن",
   "reasoning": "All three comparisons, the aunt's first night, the child free in any game, and the speaker free in speech, are captured, and the call-back is noted in L027."
  },
  {
   "point_id": "K15",
   "point_text": "He leaves tomorrow on a week of travel and is unhappy at not being home to play, already waiting to return and sit at the instrument.",
   "weight": "Nice to have",
   "presence": "Present",
   "loglog_ids": [
    "L025"
   ],
   "evidence_quote": "از فردا یک هفته سفر است و دلتنگ ساز ننواخته مانده است",
   "reasoning": "The week of travel starting tomorrow and his longing for the unplayed instrument are captured, preserving the coda."
  }
 ],
 "metrics": {
  "total_points": 15,
  "must_have_total": 8,
  "must_have_present": 5,
  "must_have_partial": 3,
  "must_have_missing": 0,
  "overall_present": 9,
  "must_recall": 0.8125,
  "overall_recall": 0.8
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
 "source_id": "10_parde_begardan_fa",
 "labels": [
  {
   "claim_id": "C001",
   "loglog_ids": [
    "0"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Thesis states the full childhood-to-keyed-santur arc; frames piece, not restated as one claim."
  },
  {
   "claim_id": "C002",
   "loglog_ids": [
    "1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Theme adds age seven and initial-fascination framing absent from subpoints."
  },
  {
   "claim_id": "C003",
   "loglog_ids": [
    "1.1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Concrete scene plus named piece «زرد ملیجه» carry detail found nowhere else."
  },
  {
   "claim_id": "C004",
   "loglog_ids": [
    "1.2"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Canonical late-night scene; earliest occurrence, later branch restates it."
  },
  {
   "claim_id": "C005",
   "loglog_ids": [
    "1.3"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Carries numbers: six months insistence and eighteen-thousand-toman price."
  },
  {
   "claim_id": "C006",
   "loglog_ids": [
    "2"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Theme adds cold reception room detail absent from its subpoints."
  },
  {
   "claim_id": "C007",
   "loglog_ids": [
    "2.1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Explains why teacher came home; unique causal fact."
  },
  {
   "claim_id": "C008",
   "loglog_ids": [
    "2.2"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Carries 72-string tuning detail and instrument-child size comparison."
  },
  {
   "claim_id": "C009",
   "loglog_ids": [
    "2.3"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Tuner removing need to carry instrument is a new causal fact."
  },
  {
   "claim_id": "C010",
   "loglog_ids": [
    "3"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Theme states one-dastgah-per-tuning and unfinished play-range limitation."
  },
  {
   "claim_id": "C011",
   "loglog_ids": [
    "3.1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Retuning-time mechanism is distinct from the theme statement."
  },
  {
   "claim_id": "C012",
   "loglog_ids": [
    "3.2"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Party-game analogy illustrates limitation; no earlier equivalent claim."
  },
  {
   "claim_id": "C013",
   "loglog_ids": [
    "3.3"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Adds corner-watching behavior image, distinct from C012's inner feeling."
  },
  {
   "claim_id": "C014",
   "loglog_ids": [
    "4"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Theme adds harp inspiration absent from its evidence lines."
  },
  {
   "claim_id": "C015",
   "loglog_ids": [
    "4.1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Quarter/half-step instant retuning detail is unique evidence."
  },
  {
   "claim_id": "C016",
   "loglog_ids": [
    "4.2"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Few-clicks switching is the concrete solution claim."
  },
  {
   "claim_id": "C017",
   "loglog_ids": [
    "5"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Carries two-year wait and Langarud/Loughborough place names."
  },
  {
   "claim_id": "C018",
   "loglog_ids": [
    "5.1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Family, friends, and officials help detail is unique."
  },
  {
   "claim_id": "C019",
   "loglog_ids": [
    "5.2"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Names four dastgahs traversed; unique example."
  },
  {
   "claim_id": "C020",
   "loglog_ids": [
    "5.3"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Disbelief and dream-like reaction is a distinct interpretation."
  },
  {
   "claim_id": "C021",
   "loglog_ids": [
    "6"
   ],
   "label": "Trivia",
   "canonical_id": null,
   "reasoning": "Theme header restates 6.1 and 6.3 with no number, caveat, or new detail."
  },
  {
   "claim_id": "C022",
   "loglog_ids": [
    "6.1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Skipped lunch and back-pain evidence is concrete and unique."
  },
  {
   "claim_id": "C023",
   "loglog_ids": [
    "6.2"
   ],
   "label": "Duplicate",
   "canonical_id": "C004",
   "reasoning": "Restates C004's late-night scene; cross-link confirms the repeat."
  },
  {
   "claim_id": "C024",
   "loglog_ids": [
    "6.3"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "One-week trip and unplayed-instrument longing add specifics."
  }
 ],
 "metrics": {
  "scored_claims": 24,
  "unique": 22,
  "duplicates": 1,
  "trivia": 1,
  "redundancy_rate": 0.0417,
  "trivia_rate": 0.0417,
  "structured_tokens": 429,
  "tokens_per_unique_claim": 19.5
 },
 "prune_list": [
  "C023 duplicates C004, safe to merge",
  "C021 header restates C022 and C024, candidate to drop"
 ]
}
```

## Judge Top (overall), opencode-go/deepseek-v4.1-flash

```json
{
 "judge": "overall",
 "judge_version": "1.0.0",
 "model": "opencode-go/deepseek-v4.1-flash (2026-09-15)",
 "source_id": "unknown",
 "inputs": {
  "faithfulness_precision": 0.9583,
  "critical_errors": 0,
  "must_recall": 0.8125,
  "overall_recall": 0.8,
  "redundancy_rate": 0.0417,
  "trivia_rate": 0.0417
 },
 "weights_used": {
  "faithfulness_precision": 0.4,
  "coverage_must_recall": 0.4,
  "redundancy_penalty": 0.2
 },
 "computation": "weighted_score = 0.4 * 0.9583 + 0.4 * 0.8125 - 0.2 * 0.0417 = 0.38332 + 0.32500 - 0.00834 = 0.69998 ~ 0.7000",
 "weighted_score": 0.7,
 "verdict": "Fail",
 "tradeoff_note": "Concision is healthy (redundancy 0.0417, below the 0.15 max) but never rescues a gate miss. The coverage gate fails on its own: must_recall 0.8125 is below the 0.9 minimum, driven by Must-have points K01, K03, and K11 sitting at Partial rather than losing to length or redundancy.",
 "fix_list": [
  "Raise must_have recall above 0.9 by fully landing the three Must-have partials: K01 (restore the cousin as instrument-buyer and the mizrab lesson from L003/L005), K03 (restore the 20,000-toman list price and discount from L006), K11 (restore clerics/community leaders and the 'today' timing from L019).",
  "Restore the source hedge on C003 / L004: the song identification is 'فکر کنم' (I think), currently stated as certain in loglog line 1.1; this is the only Partially supported claim and drives faithfulness_precision to 0.9583.",
  "Recover the dropped descriptive detail on Nice-to-have partials K02 (one of the first songs taught to beginners), K04 (six-month lesson delay and Ershad office class), and K13 (the penned fattened-sheep set-loose metaphor from L023) once the Must-haves are fixed.",
  "Merge duplicate C023 into C004 and drop or rewrite the C021 header restatement to trim the residual trivia without touching coverage."
 ],
 "reasoning": "Gate checks in policy order. (1) Critical errors: faithfulness critical_errors = 0, and critical_contradicted_max = 0, so no hard fail here. Contradicted = 0 as well; the single non-supported claim C003 is Partially supported at Minor severity, not contradicted. (2) Faithfulness precision gate: 0.9583 >= faithfulness_precision_min 0.95, so it passes, though only by 0.0083 and entirely dependent on the one partial claim C003 (loglog 1.1 drops the 'فکر کنم' hedge from the source). (3) Must-have recall gate: must_recall = 0.8125 = 5 present / 8 Must have (with 3 partial counting as failures to the strict 0.9 floor), which is below must_recall_min 0.9. This is the decisive hard fail. The three Must-have partials are K01 (age-7 first santur encounter, L003/L005: cousin and mizrab lesson replaced by 'سنتور خاله' and the mizrab teaching omitted), K03 (purchase, L006: 20,000 list price and discount dropped, only the 18,000 figure kept), and K11 (delivery, L019: clerics/community leaders omitted and 'today' timing dropped). Per top_policy, any Must-have recall below minimum fails the sample regardless of other strengths. (4) Coverage is otherwise sound at overall_recall 0.8 with no Must-have fully missing; the remaining partials K02 (L004, drops 'one of the first songs taught to beginners'), K04 (L008, drops six-month lesson delay and Ershad office class), and K13 (L023, drops the sheep-set-loose metaphor) are Nice to have and secondary. (5) Concision: redundancy_rate 0.0417 and trivia_rate 0.0417 both sit far below redundancy_max 0.15; there is ample length budget, so the coverage shortfall is not a length tradeoff, it is omitted content. Duplicates C023/C004 and the C021 header restatement are trivial and non-decisive. Since a hard gate (must_recall) is missed, the verdict is Fail, not Borderline, even though faithfulness and redundancy cleanly pass. Weighted score is reported for audit only (0.69998) and does not override the gate failure."
}
```
