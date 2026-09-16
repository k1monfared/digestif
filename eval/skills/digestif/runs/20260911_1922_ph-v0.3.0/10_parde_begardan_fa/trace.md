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
   "claim_text": "کودکی که عاشق سنتور شد، سال‌ها با محدودیت کوک دیاتونیک ساخت و با سنتور کلیددار به آزادی مدولاسیون رسید.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "سنتور یه ساز دیاتونیک هست... اگه بخوای مدلاسیون انجام بدی باید کوک عوض بشه... یه سنتوری درست کردن که... کلید تعبیه کردن",
   "reasoning": "Summary faithfully combines the childhood love, the diatonic tuning constraint, and the keyed santur's modulation freedom."
  },
  {
   "claim_id": "C002",
   "loglog_ids": [
    "1"
   ],
   "claim_text": "شبی در هفت‌سالگی با سنتور خاله و زرد ملیجه عاشق ساز شدم.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "۷ سالم که بود یه شب شام خونه خاله‌م بودیم... یه آهنگ هم برامون زد، «زرد ملیجه» بود فکر کنم",
   "reasoning": "Age seven, the aunt's santur, and Zard Malijeh are stated; falling for the instrument is directly implied by the night's account."
  },
  {
   "claim_id": "C003",
   "loglog_ids": [
    "1.1"
   ],
   "claim_text": "هفت سالم بود، سنتور خاله کنج اتاق بود، زرد ملیجه زد، فکر کنم.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "۷ سالم که بود... سنتوری که تازه خریده بود... تو کنج اتاق بود. یه آهنگ هم برامون زد، «زرد ملیجه» بود فکر کنم",
   "reasoning": "All details align, including the preserved hedge 'فکر کنم'."
  },
  {
   "claim_id": "C004",
   "loglog_ids": [
    "1.2"
   ],
   "claim_text": "از اولین درس‌ها بود؛ مضراب یاد گرفتم و به‌زور از پای ساز بلندم کردند.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "از اولین آهنگهاییه که تو آموزش سنتور یاد میدن... مضراب دست گرفتن رو بهم نشون داد... آخر شب به زور من رو از پای ساز بلند کردن",
   "reasoning": "Song-first is rephrased as lesson-first with unchanged meaning; mezrab instruction and forced removal are stated."
  },
  {
   "claim_id": "C005",
   "loglog_ids": [
    "1.3"
   ],
   "claim_text": "احتمالا فقط شام پای ساز نبودم؛ تمام راه زر زدم و شیش ماه لج کردم.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "احتمالا فقط موقع شام پای ساز نبودم. تمام طول راه رو زر زدم... شیش ماه که این زر زدن‌ها و لج‌کردن‌ها ادامه داشت",
   "reasoning": "Probability hedge, whole-route nagging, and six months of persistence all match the source."
  },
  {
   "claim_id": "C006",
   "loglog_ids": [
    "2"
   ],
   "claim_text": "با تخفیف سنتور خریدم و با سازی گنده‌تر از خودم کلاس رفتم.",
   "claim_type": "interpretation",
   "verdict": "Partially supported",
   "severity": "Minor",
   "evidence_quote": "بالاخره برام یه سنتور خریدن... با تخفیف شد ۱۸هزار تومن... سازم از خودم گنده‌تر بود",
   "reasoning": "Source says family bought it for him; claim states 'I bought', shifting agency. Discount and oversized santur are supported."
  },
  {
   "claim_id": "C007",
   "loglog_ids": [
    "2.1"
   ],
   "claim_text": "۲۰هزار تومن با تخفیف ۱۸هزار شد؛ شیش ماه بعدتر رفتم کلاس.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "۲۰هزار تومن، با تخفیف شد ۱۸هزار تومن. شیش ماه بعدتر هم رفتم کلاس",
   "reasoning": "Both figures and the six-month interval match exactly."
  },
  {
   "claim_id": "C008",
   "loglog_ids": [
    "2.2"
   ],
   "claim_text": "اول استاد به خانه می‌آمد؛ اتاق پذیرایی سرد بود، حداقل اینطور یادم مانده.",
   "claim_type": "fact",
   "verdict": "Partially supported",
   "severity": "Harmless",
   "evidence_quote": "استادم میومد خونه... سنتورم تو اتاق پذیرایی بود... سردتر از بقیه اتاقها. حداقل اینطور تو ذهن من مونده",
   "reasoning": "Comparative 'colder than other rooms' is flattened to 'cold', though the memory hedge is retained."
  },
  {
   "claim_id": "C009",
   "loglog_ids": [
    "2.3"
   ],
   "claim_text": "بعد اداره ارشاد کلاس گذاشت؛ مبل‌ها فقط برای مهمان بود.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "مبل‌ها هم تو اون اتاق بودن و فقط وقتی مهمون داشتیم استفاده میشدن. بعدترها اداره ارشاد کلاس دایر کرد",
   "reasoning": "Both the student-only sofa use and the Ershad office classes are stated."
  },
  {
   "claim_id": "C010",
   "loglog_ids": [
    "2.4"
   ],
   "claim_text": "ساز از خودم گنده‌تر بود؛ ۷۲ سیم داشت و کوکش کار هرکسی نبود.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "سازم از خودم گنده‌تر بود... ۷۲ تا سیم داره و کار هرکسی نیست کوک کردنش",
   "reasoning": "Oversized instrument, 72 strings, and non-trivial tuning are all directly stated."
  },
  {
   "claim_id": "C011",
   "loglog_ids": [
    "3"
   ],
   "claim_text": "کوک زمان‌بر، سنتور دیاتونیک را به یک بازی در مهمانی محدود می‌کرد.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "مدلاسیون انجام بدی باید کوک عوض بشه که خب زمانبره... حس بچه‌ای... بهش فقط اجازه یه بازی رو داده باشن",
   "reasoning": "The time-consuming tuning and the one-game-at-a-party metaphor match the source."
  },
  {
   "claim_id": "C012",
   "loglog_ids": [
    "3.1"
   ],
   "claim_text": "با تیونر دیگر لازم نبود ساز را برای کوک به کلاس ببرم.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "بعدترها که تیونر اومد بازار دیگه نیاز نبود ساز رو ببرم سر کلاس چون دیگه خودم میتونستم کوکش کنم",
   "reasoning": "Negation and condition match exactly."
  },
  {
   "claim_id": "C013",
   "loglog_ids": [
    "3.2"
   ],
   "claim_text": "سنتور دیاتونیک است؛ یک دستگاه در آن واحد، مدولاسیون زمان‌بر است.",
   "claim_type": "definition",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "سنتور یه ساز دیاتونیک هست، ینی در آن واحد فقط میشه یک دستگاه/گام رو روش نواخت... باید کوک عوض بشه که خب زمانبره",
   "reasoning": "The definition and its consequence are stated verbatim in meaning."
  },
  {
   "claim_id": "C014",
   "loglog_ids": [
    "3.3"
   ],
   "claim_text": "مثل بچه‌ای بودم که فقط یک بازی مجاز است؛ اگه خسته می‌شدم نمی‌صرفید.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "حس بچه‌ای... بهش فقط اجازه یه بازی رو داده باشن... نمیصرفید، تا اون موقع حس بازی میرفت",
   "reasoning": "Both the single-game limitation and the 'not worth it' conclusion are present."
  },
  {
   "claim_id": "C015",
   "loglog_ids": [
    "3.4"
   ],
   "claim_text": "اگه بچه‌ها بازی عوض می‌کردند، حتی با علاقه گوشه می‌نشستم و نگاه می‌کردم.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "من مجبور بودم ساکت بشینم یه گوشه‌ای و نگاهشون کنم. حتی اگه اون بازی‌ رو خیلی دوست داشتم",
   "reasoning": "Sitting silently in a corner and watching, even when fond of the game, is stated."
  },
  {
   "claim_id": "C016",
   "loglog_ids": [
    "4"
   ],
   "claim_text": "سنتور کلیددار با ایده چنگ، تغییر ربع‌پرده را به ثانیه رساند.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "از چنگ ایده گرفتن و یه سری کلید تعبیه کردن که ربع یا نیم پرده زیرتر کردن هر نتی رو در کسری از ثانیه میشه انجام داد",
   "reasoning": "Harp-derived idea, keys, quarter-tone shifts, and sub-second speed are all present."
  },
  {
   "claim_id": "C017",
   "loglog_ids": [
    "4.1"
   ],
   "claim_text": "کلیدها ربع یا نیم پرده را در کسری از ثانیه زیرتر می‌کنند؛ مدولاسیون چندثانیه‌ای شد.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "ربع یا نیم پرده زیرتر کردن هر نتی رو در کسری از ثانیه... فقط با چند کلیک، فقط در چند ثانیه",
   "reasoning": "Quarter/half-tone shifts and multi-second modulation are stated precisely."
  },
  {
   "claim_id": "C018",
   "loglog_ids": [
    "4.2"
   ],
   "claim_text": "دو سالی به آن فکر می‌کردم؛ سالم از لنگرود به لنگفورد آوردنش را نمی‌دانستم.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "دو سالی بود که بهش فکر میکردم ولی نمیدونستم چطور میتونم سالم از لنگرود بیارمش لنگفورد",
   "reasoning": "Two years of thinking, the negation, the route, and 'safely' all match."
  },
  {
   "claim_id": "C019",
   "loglog_ids": [
    "4.3"
   ],
   "claim_text": "با کمک خانواده و دوستان و مسئولین و ائمه امروز به دستم رسید.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "با کمکهای بی دریغ خانواده و دوستان و مسئولین و ائمه امروز رسید به دستم",
   "reasoning": "All four helper groups and the timing are stated verbatim in meaning."
  },
  {
   "claim_id": "C020",
   "loglog_ids": [
    "5"
   ],
   "claim_text": "از اصفهان تا همایون بی‌وقفه نواختم؛ حالا یک هفته سفر، چشم‌انتظار بازگشتم.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "از اصفهان به سه‌گاه... از شور به همایون... نهار نخوردم، هی ساز زدم... حالا از فردا یک هفته‌ای مسافرتم... منتظرم برگردم",
   "reasoning": "Nonstop playing across the modes, the one-week trip, and longing to return are all present."
  },
  {
   "claim_id": "C021",
   "loglog_ids": [
    "5.1"
   ],
   "claim_text": "از اصفهان به سه‌گاه، نوا، شور، همایون رفتم؛ انگار خواب می‌دیدم.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "از اصفهان به سه‌گاه، از سه‌گاه به نوا، از نوا به شور، از شور به همایون... انگار داشتم خواب میدیدم",
   "reasoning": "Mode sequence and dream simile match exactly."
  },
  {
   "claim_id": "C022",
   "loglog_ids": [
    "5.2"
   ],
   "claim_text": "مثل گوسفند پرواری دویدم، نهار نخوردم، پشتم درد گرفت؛ حس شب اول بود.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "حکم گوسفند پرواری‌ای... بدون وقفه داشت میدوید، نهار نخوردم... پشتم درد گرفت. حس شب اولی رو داشتم",
   "reasoning": "The sheep metaphor, skipped lunch, back pain, and first-night feeling are all stated."
  },
  {
   "claim_id": "C023",
   "loglog_ids": [
    "5.3"
   ],
   "claim_text": "مثل بچه‌ای با هر بازی و کسی با هر حرف؛ از فردا یک هفته‌ای مسافرم.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "حس بچه‌ای... هر بازی‌ای که دوست داشت... حس کسی... هر حرفی رو میخواست... حالا از فردا یک هفته‌ای مسافرتم",
   "reasoning": "Both similes and the one-week trip are directly stated."
  },
  {
   "claim_id": "C024",
   "loglog_ids": [
    "5.4"
   ],
   "claim_text": "نرفته منتظر برگشتن و نشستن پای سازم.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "نرفته منتظرم برگردم و بشینم پای ساز",
   "reasoning": "The negation and both awaited actions match exactly."
  }
 ],
 "metrics": {
  "total_claims": 24,
  "supported": 22,
  "partially_supported": 2,
  "unverifiable": 0,
  "contradicted": 0,
  "critical_errors": 0,
  "faithfulness_precision": 0.9167
 },
 "fail_list": [
  "C006",
  "C008"
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
   "presence": "Present",
   "loglog_ids": [
    "L004",
    "L005"
   ],
   "evidence_quote": "هفت سالم بود، سنتور خاله کنج اتاق بود ... مضراب یاد گرفتم و به‌زور از پای ساز بلندم کردند.",
   "reasoning": "Age 7, the aunt's santur at her house, the first encounter, learning the mizrab, and being forcibly lifted from the instrument are all captured. The 'cousin' attribution is compressed to 'aunt', a harmless simplification that does not change the origin-story meaning."
  },
  {
   "point_id": "K02",
   "point_text": "The first tune he heard on that santur was likely 'Zard Maliheh' (زرد ملیجه), one of the first songs taught to santur beginners.",
   "weight": "Nice to have",
   "presence": "Present",
   "loglog_ids": [
    "L004"
   ],
   "evidence_quote": "زرد ملیجه زد، فکر کنم.",
   "reasoning": "The tune name is preserved along with the hedging 'I think', matching the source's uncertainty."
  },
  {
   "point_id": "K03",
   "point_text": "After six months of nagging and sulking, his family finally bought him a santur for 20,000 toman, discounted to 18,000 toman.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L008"
   ],
   "evidence_quote": "۲۰هزار تومن با تخفیف ۱۸هزار شد؛ شیش ماه بعدتر رفتم کلاس.",
   "reasoning": "Both numbers (20,000 and discounted 18,000) are intact, and the six-month wait/sulking is captured at L006-L008, so the acquisition milestone holds."
  },
  {
   "point_id": "K04",
   "point_text": "He started lessons six months later; the teacher initially came to his home because their city had no school, and only later did the Ershad office open a class where the teacher taught.",
   "weight": "Nice to have",
   "presence": "Present",
   "loglog_ids": [
    "L008",
    "L009",
    "L010"
   ],
   "evidence_quote": "شیش ماه بعدتر رفتم کلاس ... اول استاد به خانه می‌آمد ... بعد اداره ارشاد کلاس گذاشت.",
   "reasoning": "All three beats (six months later, teacher at home, later Ershad office class) are present in the correct sequence."
  },
  {
   "point_id": "K05",
   "point_text": "The santur has 72 strings and is hard for an ordinary person to tune, so he had to haul the oversized instrument to class to be tuned, until electronic tuners reached the market and he could tune it himself.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L011",
    "L013"
   ],
   "evidence_quote": "۷۲ سیم داشت و کوکش کار هرکسی نبود ... با تیونر دیگر لازم نبود ساز را برای کوک به کلاس ببرم.",
   "reasoning": "The 72-string number, the tuning difficulty, the hauling to class, and the electronic tuner resolution are all preserved."
  },
  {
   "point_id": "K06",
   "point_text": "The santur is a diatonic instrument: only one dastgah/scale can be played at a time, and modulation requires retuning, which is time-consuming.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L014"
   ],
   "evidence_quote": "سنتور دیاتونیک است؛ یک دستگاه در آن واحد، مدولاسیون زمان‌بر است.",
   "reasoning": "Diatonic nature, single-dastgah-at-a-time constraint, and time-consuming modulation are all captured verbatim."
  },
  {
   "point_id": "K07",
   "point_text": "This limitation made him feel like a child at a party allowed only one game: to switch he would have to pack up all his toys first, by which time the mood is gone, or else sit silently aside while the other children move to a game he loves.",
   "weight": "Nice to have",
   "presence": "Present",
   "loglog_ids": [
    "L015",
    "L016"
   ],
   "evidence_quote": "مثل بچه‌ای بودم که فقط یک بازی مجاز است ... اگه بچه‌ها بازی عوض می‌کردند، حتی با علاقه گوشه می‌نشستم و نگاه می‌کردم.",
   "reasoning": "The one-game-at-a-party analogy and the sitting-aside-while-others-switch image are both preserved, though the 'packing up toys' clause is implied rather than explicit."
  },
  {
   "point_id": "K08",
   "point_text": "Recently a santur was built inspired by the harp, with a set of keys allowing any note to be lowered by a quarter or half step in a fraction of a second.",
   "weight": "Must have",
   "presence": "Partial",
   "loglog_ids": [
    "L017",
    "L018"
   ],
   "evidence_quote": "سنتور کلیددار با ایده چنگ ... کلیدها ربع یا نیم پرده را در کسری از ثانیه زیرتر می‌کنند.",
   "reasoning": "The harp-inspired keyed santur, the quarter/half-step change, and the fraction-of-a-second speed are all present. But the loglog says the keys make notes 'زیرتر' (higher), reversing the source's 'lowered' direction. This directional inversion is a meaning change on a Must have point, so at most Partial."
  },
  {
   "point_id": "K09",
   "point_text": "This makes it possible to move quickly from any dastgah to any other with a few clicks, in just seconds.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L018",
    "L029"
   ],
   "evidence_quote": "مدولاسیون چندثانیه‌ای شد.",
   "reasoning": "The fast, few-seconds modulation across dastgahs is captured, and the cross-link L029 ties the played sequence to this capability."
  },
  {
   "point_id": "K10",
   "point_text": "He had been thinking about such an instrument for two years but did not know how to bring it safely from Langroud to Langford.",
   "weight": "Nice to have",
   "presence": "Present",
   "loglog_ids": [
    "L019"
   ],
   "evidence_quote": "دو سالی به آن فکر می‌کردم؛ سالم از لنگرود به لنگفورد آوردنش را نمی‌دانستم.",
   "reasoning": "Both the two-year rumination and the Langroud-to-Langford transport problem are preserved."
  },
  {
   "point_id": "K11",
   "point_text": "With the unstinting help of family, friends, officials, and clerics/community leaders, the instrument finally reached him today.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L020"
   ],
   "evidence_quote": "با کمک خانواده و دوستان و مسئولین و ائمه امروز به دستم رسید.",
   "reasoning": "The arrival today and the full list of helpers (family, friends, officials, imams/leaders) are all captured."
  },
  {
   "point_id": "K12",
   "point_text": "He tuned it and played, moving from dastgah to dastgah: Isfahan to Segah, Segah to Nava, Nava to Shur, Shur to Homayoun.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L022"
   ],
   "evidence_quote": "از اصفهان به سه‌گاه، نوا، شور، همایون رفتم.",
   "reasoning": "The exact modulation sequence Isfahan, Segah, Nava, Shur, Homayoun is preserved."
  },
  {
   "point_id": "K13",
   "point_text": "He felt like a penned fattened sheep set loose, running without pause: he skipped lunch and played so long his back ached.",
   "weight": "Nice to have",
   "presence": "Present",
   "loglog_ids": [
    "L023"
   ],
   "evidence_quote": "مثل گوسفند پرواری دویدم، نهار نخوردم، پشتم درد گرفت.",
   "reasoning": "The fattened-sheep image, the skipped lunch, and the aching back are all captured."
  },
  {
   "point_id": "K14",
   "point_text": "He felt like the first night his aunt put the mizrabs in his hand, like a child allowed to play any game he wants, like a person free to say anything he wishes.",
   "weight": "Nice to have",
   "presence": "Present",
   "loglog_ids": [
    "L023",
    "L024"
   ],
   "evidence_quote": "حس شب اول بود ... مثل بچه‌ای با هر بازی و کسی با هر حرف.",
   "reasoning": "The callback to the first night, the any-game child, and the free-to-say-anything person are all represented."
  },
  {
   "point_id": "K15",
   "point_text": "He leaves tomorrow on a week of travel and is unhappy at not being home to play, already waiting to return and sit at the instrument.",
   "weight": "Nice to have",
   "presence": "Present",
   "loglog_ids": [
    "L024",
    "L025"
   ],
   "evidence_quote": "از فردا یک هفته‌ای مسافرم ... نرفته منتظر برگشتن و نشستن پای سازم.",
   "reasoning": "The week of travel starting tomorrow and his preemptive longing to return and sit at the instrument are both preserved."
  }
 ],
 "metrics": {
  "total_points": 15,
  "must_have_total": 8,
  "must_have_present": 7,
  "must_have_partial": 1,
  "must_have_missing": 0,
  "overall_present": 14,
  "must_recall": 0.9375,
  "overall_recall": 0.9667
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
   "claim_text": "کودکی که عاشق سنتور شد، سال‌ها با محدودیت کوک دیاتونیک ساخت و با سنتور کلیددار به آزادی مدولاسیون رسید.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "سنتور یه ساز دیاتونیک هست... اگه بخوای مدلاسیون انجام بدی باید کوک عوض بشه... یه سنتوری درست کردن که... کلید تعبیه کردن",
   "reasoning": "Summary faithfully combines the childhood love, the diatonic tuning constraint, and the keyed santur's modulation freedom."
  },
  {
   "claim_id": "C002",
   "loglog_ids": [
    "1"
   ],
   "claim_text": "شبی در هفت‌سالگی با سنتور خاله و زرد ملیجه عاشق ساز شدم.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "۷ سالم که بود یه شب شام خونه خاله‌م بودیم... یه آهنگ هم برامون زد، «زرد ملیجه» بود فکر کنم",
   "reasoning": "Age seven, the aunt's santur, and Zard Malijeh are stated; falling for the instrument is directly implied by the night's account."
  },
  {
   "claim_id": "C003",
   "loglog_ids": [
    "1.1"
   ],
   "claim_text": "هفت سالم بود، سنتور خاله کنج اتاق بود، زرد ملیجه زد، فکر کنم.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "۷ سالم که بود... سنتوری که تازه خریده بود... تو کنج اتاق بود. یه آهنگ هم برامون زد، «زرد ملیجه» بود فکر کنم",
   "reasoning": "All details align, including the preserved hedge 'فکر کنم'."
  },
  {
   "claim_id": "C004",
   "loglog_ids": [
    "1.2"
   ],
   "claim_text": "از اولین درس‌ها بود؛ مضراب یاد گرفتم و به‌زور از پای ساز بلندم کردند.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "از اولین آهنگهاییه که تو آموزش سنتور یاد میدن... مضراب دست گرفتن رو بهم نشون داد... آخر شب به زور من رو از پای ساز بلند کردن",
   "reasoning": "Song-first is rephrased as lesson-first with unchanged meaning; mezrab instruction and forced removal are stated."
  },
  {
   "claim_id": "C005",
   "loglog_ids": [
    "1.3"
   ],
   "claim_text": "احتمالا فقط شام پای ساز نبودم؛ تمام راه زر زدم و شیش ماه لج کردم.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "احتمالا فقط موقع شام پای ساز نبودم. تمام طول راه رو زر زدم... شیش ماه که این زر زدن‌ها و لج‌کردن‌ها ادامه داشت",
   "reasoning": "Probability hedge, whole-route nagging, and six months of persistence all match the source."
  },
  {
   "claim_id": "C006",
   "loglog_ids": [
    "2"
   ],
   "claim_text": "با تخفیف سنتور خریدم و با سازی گنده‌تر از خودم کلاس رفتم.",
   "claim_type": "interpretation",
   "verdict": "Partially supported",
   "severity": "Minor",
   "evidence_quote": "بالاخره برام یه سنتور خریدن... با تخفیف شد ۱۸هزار تومن... سازم از خودم گنده‌تر بود",
   "reasoning": "Source says family bought it for him; claim states 'I bought', shifting agency. Discount and oversized santur are supported."
  },
  {
   "claim_id": "C007",
   "loglog_ids": [
    "2.1"
   ],
   "claim_text": "۲۰هزار تومن با تخفیف ۱۸هزار شد؛ شیش ماه بعدتر رفتم کلاس.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "۲۰هزار تومن، با تخفیف شد ۱۸هزار تومن. شیش ماه بعدتر هم رفتم کلاس",
   "reasoning": "Both figures and the six-month interval match exactly."
  },
  {
   "claim_id": "C008",
   "loglog_ids": [
    "2.2"
   ],
   "claim_text": "اول استاد به خانه می‌آمد؛ اتاق پذیرایی سرد بود، حداقل اینطور یادم مانده.",
   "claim_type": "fact",
   "verdict": "Partially supported",
   "severity": "Harmless",
   "evidence_quote": "استادم میومد خونه... سنتورم تو اتاق پذیرایی بود... سردتر از بقیه اتاقها. حداقل اینطور تو ذهن من مونده",
   "reasoning": "Comparative 'colder than other rooms' is flattened to 'cold', though the memory hedge is retained."
  },
  {
   "claim_id": "C009",
   "loglog_ids": [
    "2.3"
   ],
   "claim_text": "بعد اداره ارشاد کلاس گذاشت؛ مبل‌ها فقط برای مهمان بود.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "مبل‌ها هم تو اون اتاق بودن و فقط وقتی مهمون داشتیم استفاده میشدن. بعدترها اداره ارشاد کلاس دایر کرد",
   "reasoning": "Both the student-only sofa use and the Ershad office classes are stated."
  },
  {
   "claim_id": "C010",
   "loglog_ids": [
    "2.4"
   ],
   "claim_text": "ساز از خودم گنده‌تر بود؛ ۷۲ سیم داشت و کوکش کار هرکسی نبود.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "سازم از خودم گنده‌تر بود... ۷۲ تا سیم داره و کار هرکسی نیست کوک کردنش",
   "reasoning": "Oversized instrument, 72 strings, and non-trivial tuning are all directly stated."
  },
  {
   "claim_id": "C011",
   "loglog_ids": [
    "3"
   ],
   "claim_text": "کوک زمان‌بر، سنتور دیاتونیک را به یک بازی در مهمانی محدود می‌کرد.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "مدلاسیون انجام بدی باید کوک عوض بشه که خب زمانبره... حس بچه‌ای... بهش فقط اجازه یه بازی رو داده باشن",
   "reasoning": "The time-consuming tuning and the one-game-at-a-party metaphor match the source."
  },
  {
   "claim_id": "C012",
   "loglog_ids": [
    "3.1"
   ],
   "claim_text": "با تیونر دیگر لازم نبود ساز را برای کوک به کلاس ببرم.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "بعدترها که تیونر اومد بازار دیگه نیاز نبود ساز رو ببرم سر کلاس چون دیگه خودم میتونستم کوکش کنم",
   "reasoning": "Negation and condition match exactly."
  },
  {
   "claim_id": "C013",
   "loglog_ids": [
    "3.2"
   ],
   "claim_text": "سنتور دیاتونیک است؛ یک دستگاه در آن واحد، مدولاسیون زمان‌بر است.",
   "claim_type": "definition",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "سنتور یه ساز دیاتونیک هست، ینی در آن واحد فقط میشه یک دستگاه/گام رو روش نواخت... باید کوک عوض بشه که خب زمانبره",
   "reasoning": "The definition and its consequence are stated verbatim in meaning."
  },
  {
   "claim_id": "C014",
   "loglog_ids": [
    "3.3"
   ],
   "claim_text": "مثل بچه‌ای بودم که فقط یک بازی مجاز است؛ اگه خسته می‌شدم نمی‌صرفید.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "حس بچه‌ای... بهش فقط اجازه یه بازی رو داده باشن... نمیصرفید، تا اون موقع حس بازی میرفت",
   "reasoning": "Both the single-game limitation and the 'not worth it' conclusion are present."
  },
  {
   "claim_id": "C015",
   "loglog_ids": [
    "3.4"
   ],
   "claim_text": "اگه بچه‌ها بازی عوض می‌کردند، حتی با علاقه گوشه می‌نشستم و نگاه می‌کردم.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "من مجبور بودم ساکت بشینم یه گوشه‌ای و نگاهشون کنم. حتی اگه اون بازی‌ رو خیلی دوست داشتم",
   "reasoning": "Sitting silently in a corner and watching, even when fond of the game, is stated."
  },
  {
   "claim_id": "C016",
   "loglog_ids": [
    "4"
   ],
   "claim_text": "سنتور کلیددار با ایده چنگ، تغییر ربع‌پرده را به ثانیه رساند.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "از چنگ ایده گرفتن و یه سری کلید تعبیه کردن که ربع یا نیم پرده زیرتر کردن هر نتی رو در کسری از ثانیه میشه انجام داد",
   "reasoning": "Harp-derived idea, keys, quarter-tone shifts, and sub-second speed are all present."
  },
  {
   "claim_id": "C017",
   "loglog_ids": [
    "4.1"
   ],
   "claim_text": "کلیدها ربع یا نیم پرده را در کسری از ثانیه زیرتر می‌کنند؛ مدولاسیون چندثانیه‌ای شد.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "ربع یا نیم پرده زیرتر کردن هر نتی رو در کسری از ثانیه... فقط با چند کلیک، فقط در چند ثانیه",
   "reasoning": "Quarter/half-tone shifts and multi-second modulation are stated precisely."
  },
  {
   "claim_id": "C018",
   "loglog_ids": [
    "4.2"
   ],
   "claim_text": "دو سالی به آن فکر می‌کردم؛ سالم از لنگرود به لنگفورد آوردنش را نمی‌دانستم.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "دو سالی بود که بهش فکر میکردم ولی نمیدونستم چطور میتونم سالم از لنگرود بیارمش لنگفورد",
   "reasoning": "Two years of thinking, the negation, the route, and 'safely' all match."
  },
  {
   "claim_id": "C019",
   "loglog_ids": [
    "4.3"
   ],
   "claim_text": "با کمک خانواده و دوستان و مسئولین و ائمه امروز به دستم رسید.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "با کمکهای بی دریغ خانواده و دوستان و مسئولین و ائمه امروز رسید به دستم",
   "reasoning": "All four helper groups and the timing are stated verbatim in meaning."
  },
  {
   "claim_id": "C020",
   "loglog_ids": [
    "5"
   ],
   "claim_text": "از اصفهان تا همایون بی‌وقفه نواختم؛ حالا یک هفته سفر، چشم‌انتظار بازگشتم.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "از اصفهان به سه‌گاه... از شور به همایون... نهار نخوردم، هی ساز زدم... حالا از فردا یک هفته‌ای مسافرتم... منتظرم برگردم",
   "reasoning": "Nonstop playing across the modes, the one-week trip, and longing to return are all present."
  },
  {
   "claim_id": "C021",
   "loglog_ids": [
    "5.1"
   ],
   "claim_text": "از اصفهان به سه‌گاه، نوا، شور، همایون رفتم؛ انگار خواب می‌دیدم.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "از اصفهان به سه‌گاه، از سه‌گاه به نوا، از نوا به شور، از شور به همایون... انگار داشتم خواب میدیدم",
   "reasoning": "Mode sequence and dream simile match exactly."
  },
  {
   "claim_id": "C022",
   "loglog_ids": [
    "5.2"
   ],
   "claim_text": "مثل گوسفند پرواری دویدم، نهار نخوردم، پشتم درد گرفت؛ حس شب اول بود.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "حکم گوسفند پرواری‌ای... بدون وقفه داشت میدوید، نهار نخوردم... پشتم درد گرفت. حس شب اولی رو داشتم",
   "reasoning": "The sheep metaphor, skipped lunch, back pain, and first-night feeling are all stated."
  },
  {
   "claim_id": "C023",
   "loglog_ids": [
    "5.3"
   ],
   "claim_text": "مثل بچه‌ای با هر بازی و کسی با هر حرف؛ از فردا یک هفته‌ای مسافرم.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "حس بچه‌ای... هر بازی‌ای که دوست داشت... حس کسی... هر حرفی رو میخواست... حالا از فردا یک هفته‌ای مسافرتم",
   "reasoning": "Both similes and the one-week trip are directly stated."
  },
  {
   "claim_id": "C024",
   "loglog_ids": [
    "5.4"
   ],
   "claim_text": "نرفته منتظر برگشتن و نشستن پای سازم.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "نرفته منتظرم برگردم و بشینم پای ساز",
   "reasoning": "The negation and both awaited actions match exactly."
  }
 ],
 "metrics": {
  "total_claims": 24,
  "supported": 22,
  "partially_supported": 2,
  "unverifiable": 0,
  "contradicted": 0,
  "critical_errors": 0,
  "faithfulness_precision": 0.9167
 },
 "fail_list": [
  "C006",
  "C008"
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
   "presence": "Present",
   "loglog_ids": [
    "L004",
    "L005"
   ],
   "evidence_quote": "هفت سالم بود، سنتور خاله کنج اتاق بود ... مضراب یاد گرفتم و به‌زور از پای ساز بلندم کردند.",
   "reasoning": "Age 7, the aunt's santur at her house, the first encounter, learning the mizrab, and being forcibly lifted from the instrument are all captured. The 'cousin' attribution is compressed to 'aunt', a harmless simplification that does not change the origin-story meaning."
  },
  {
   "point_id": "K02",
   "point_text": "The first tune he heard on that santur was likely 'Zard Maliheh' (زرد ملیجه), one of the first songs taught to santur beginners.",
   "weight": "Nice to have",
   "presence": "Present",
   "loglog_ids": [
    "L004"
   ],
   "evidence_quote": "زرد ملیجه زد، فکر کنم.",
   "reasoning": "The tune name is preserved along with the hedging 'I think', matching the source's uncertainty."
  },
  {
   "point_id": "K03",
   "point_text": "After six months of nagging and sulking, his family finally bought him a santur for 20,000 toman, discounted to 18,000 toman.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L008"
   ],
   "evidence_quote": "۲۰هزار تومن با تخفیف ۱۸هزار شد؛ شیش ماه بعدتر رفتم کلاس.",
   "reasoning": "Both numbers (20,000 and discounted 18,000) are intact, and the six-month wait/sulking is captured at L006-L008, so the acquisition milestone holds."
  },
  {
   "point_id": "K04",
   "point_text": "He started lessons six months later; the teacher initially came to his home because their city had no school, and only later did the Ershad office open a class where the teacher taught.",
   "weight": "Nice to have",
   "presence": "Present",
   "loglog_ids": [
    "L008",
    "L009",
    "L010"
   ],
   "evidence_quote": "شیش ماه بعدتر رفتم کلاس ... اول استاد به خانه می‌آمد ... بعد اداره ارشاد کلاس گذاشت.",
   "reasoning": "All three beats (six months later, teacher at home, later Ershad office class) are present in the correct sequence."
  },
  {
   "point_id": "K05",
   "point_text": "The santur has 72 strings and is hard for an ordinary person to tune, so he had to haul the oversized instrument to class to be tuned, until electronic tuners reached the market and he could tune it himself.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L011",
    "L013"
   ],
   "evidence_quote": "۷۲ سیم داشت و کوکش کار هرکسی نبود ... با تیونر دیگر لازم نبود ساز را برای کوک به کلاس ببرم.",
   "reasoning": "The 72-string number, the tuning difficulty, the hauling to class, and the electronic tuner resolution are all preserved."
  },
  {
   "point_id": "K06",
   "point_text": "The santur is a diatonic instrument: only one dastgah/scale can be played at a time, and modulation requires retuning, which is time-consuming.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L014"
   ],
   "evidence_quote": "سنتور دیاتونیک است؛ یک دستگاه در آن واحد، مدولاسیون زمان‌بر است.",
   "reasoning": "Diatonic nature, single-dastgah-at-a-time constraint, and time-consuming modulation are all captured verbatim."
  },
  {
   "point_id": "K07",
   "point_text": "This limitation made him feel like a child at a party allowed only one game: to switch he would have to pack up all his toys first, by which time the mood is gone, or else sit silently aside while the other children move to a game he loves.",
   "weight": "Nice to have",
   "presence": "Present",
   "loglog_ids": [
    "L015",
    "L016"
   ],
   "evidence_quote": "مثل بچه‌ای بودم که فقط یک بازی مجاز است ... اگه بچه‌ها بازی عوض می‌کردند، حتی با علاقه گوشه می‌نشستم و نگاه می‌کردم.",
   "reasoning": "The one-game-at-a-party analogy and the sitting-aside-while-others-switch image are both preserved, though the 'packing up toys' clause is implied rather than explicit."
  },
  {
   "point_id": "K08",
   "point_text": "Recently a santur was built inspired by the harp, with a set of keys allowing any note to be lowered by a quarter or half step in a fraction of a second.",
   "weight": "Must have",
   "presence": "Partial",
   "loglog_ids": [
    "L017",
    "L018"
   ],
   "evidence_quote": "سنتور کلیددار با ایده چنگ ... کلیدها ربع یا نیم پرده را در کسری از ثانیه زیرتر می‌کنند.",
   "reasoning": "The harp-inspired keyed santur, the quarter/half-step change, and the fraction-of-a-second speed are all present. But the loglog says the keys make notes 'زیرتر' (higher), reversing the source's 'lowered' direction. This directional inversion is a meaning change on a Must have point, so at most Partial."
  },
  {
   "point_id": "K09",
   "point_text": "This makes it possible to move quickly from any dastgah to any other with a few clicks, in just seconds.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L018",
    "L029"
   ],
   "evidence_quote": "مدولاسیون چندثانیه‌ای شد.",
   "reasoning": "The fast, few-seconds modulation across dastgahs is captured, and the cross-link L029 ties the played sequence to this capability."
  },
  {
   "point_id": "K10",
   "point_text": "He had been thinking about such an instrument for two years but did not know how to bring it safely from Langroud to Langford.",
   "weight": "Nice to have",
   "presence": "Present",
   "loglog_ids": [
    "L019"
   ],
   "evidence_quote": "دو سالی به آن فکر می‌کردم؛ سالم از لنگرود به لنگفورد آوردنش را نمی‌دانستم.",
   "reasoning": "Both the two-year rumination and the Langroud-to-Langford transport problem are preserved."
  },
  {
   "point_id": "K11",
   "point_text": "With the unstinting help of family, friends, officials, and clerics/community leaders, the instrument finally reached him today.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L020"
   ],
   "evidence_quote": "با کمک خانواده و دوستان و مسئولین و ائمه امروز به دستم رسید.",
   "reasoning": "The arrival today and the full list of helpers (family, friends, officials, imams/leaders) are all captured."
  },
  {
   "point_id": "K12",
   "point_text": "He tuned it and played, moving from dastgah to dastgah: Isfahan to Segah, Segah to Nava, Nava to Shur, Shur to Homayoun.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L022"
   ],
   "evidence_quote": "از اصفهان به سه‌گاه، نوا، شور، همایون رفتم.",
   "reasoning": "The exact modulation sequence Isfahan, Segah, Nava, Shur, Homayoun is preserved."
  },
  {
   "point_id": "K13",
   "point_text": "He felt like a penned fattened sheep set loose, running without pause: he skipped lunch and played so long his back ached.",
   "weight": "Nice to have",
   "presence": "Present",
   "loglog_ids": [
    "L023"
   ],
   "evidence_quote": "مثل گوسفند پرواری دویدم، نهار نخوردم، پشتم درد گرفت.",
   "reasoning": "The fattened-sheep image, the skipped lunch, and the aching back are all captured."
  },
  {
   "point_id": "K14",
   "point_text": "He felt like the first night his aunt put the mizrabs in his hand, like a child allowed to play any game he wants, like a person free to say anything he wishes.",
   "weight": "Nice to have",
   "presence": "Present",
   "loglog_ids": [
    "L023",
    "L024"
   ],
   "evidence_quote": "حس شب اول بود ... مثل بچه‌ای با هر بازی و کسی با هر حرف.",
   "reasoning": "The callback to the first night, the any-game child, and the free-to-say-anything person are all represented."
  },
  {
   "point_id": "K15",
   "point_text": "He leaves tomorrow on a week of travel and is unhappy at not being home to play, already waiting to return and sit at the instrument.",
   "weight": "Nice to have",
   "presence": "Present",
   "loglog_ids": [
    "L024",
    "L025"
   ],
   "evidence_quote": "از فردا یک هفته‌ای مسافرم ... نرفته منتظر برگشتن و نشستن پای سازم.",
   "reasoning": "The week of travel starting tomorrow and his preemptive longing to return and sit at the instrument are both preserved."
  }
 ],
 "metrics": {
  "total_points": 15,
  "must_have_total": 8,
  "must_have_present": 7,
  "must_have_partial": 1,
  "must_have_missing": 0,
  "overall_present": 14,
  "must_recall": 0.9375,
  "overall_recall": 0.9667
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
   "reasoning": "Top-level arc: childhood love, diatonic limitation, keyed freedom. The document's thesis, not restated elsewhere."
  },
  {
   "claim_id": "C002",
   "loglog_ids": [
    "1"
   ],
   "label": "Trivia",
   "canonical_id": null,
   "reasoning": "Restated section header; the concrete detail lives in C003-C005 and the summary."
  },
  {
   "claim_id": "C003",
   "loglog_ids": [
    "1.1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Specifics: age seven, aunt's santur in the corner, Zard-e-Malijeh, hedged memory."
  },
  {
   "claim_id": "C004",
   "loglog_ids": [
    "1.2"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "First lessons, learning mizrab, being forced off the instrument. New content."
  },
  {
   "claim_id": "C005",
   "loglog_ids": [
    "1.3"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Stubbornness, six months of sulking, walking the whole road. Distinct detail."
  },
  {
   "claim_id": "C006",
   "loglog_ids": [
    "2"
   ],
   "label": "Trivia",
   "canonical_id": null,
   "reasoning": "Restated section header; all substance carried by C007-C010."
  },
  {
   "claim_id": "C007",
   "loglog_ids": [
    "2.1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Discounted price 20k to 18k and six-month delay are non-trivial numbers."
  },
  {
   "claim_id": "C008",
   "loglog_ids": [
    "2.2"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Teacher came home, cold living room, explicit hedge. Caveat keeps it in scope."
  },
  {
   "claim_id": "C009",
   "loglog_ids": [
    "2.3"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Ershad office hosted classes later; couches reserved for guests. Human detail."
  },
  {
   "claim_id": "C010",
   "loglog_ids": [
    "2.4"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Seventy-two strings and hard tuning are concrete facts beyond the header."
  },
  {
   "claim_id": "C011",
   "loglog_ids": [
    "3"
   ],
   "label": "Trivia",
   "canonical_id": null,
   "reasoning": "Restated section header; limitation and tuning cost detailed in C013-C015."
  },
  {
   "claim_id": "C012",
   "loglog_ids": [
    "3.1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Tuner removed the need to carry the instrument to class. New operational fact."
  },
  {
   "claim_id": "C013",
   "loglog_ids": [
    "3.2"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Explicit definition: diatonic, one dastgah per time, time-consuming modulation."
  },
  {
   "claim_id": "C014",
   "loglog_ids": [
    "3.3"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Child-with-one-permitted-game analogy adds the boredom consequence, not just the image."
  },
  {
   "claim_id": "C015",
   "loglog_ids": [
    "3.4"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Watching from the corner when others switch games. Distinct behavioral detail."
  },
  {
   "claim_id": "C016",
   "loglog_ids": [
    "4"
   ],
   "label": "Trivia",
   "canonical_id": null,
   "reasoning": "Restated section header; the quarter-tone mechanism is developed in C017-C019."
  },
  {
   "claim_id": "C017",
   "loglog_ids": [
    "4.1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Quarter or half tone raised in fractions of a second; adds half-step and timing."
  },
  {
   "claim_id": "C018",
   "loglog_ids": [
    "4.2"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Two years of thinking and the Langarud-to-Langford transfer problem. Specific."
  },
  {
   "claim_id": "C019",
   "loglog_ids": [
    "4.3"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Arrival credited to family, friends, officials, and imams. Specific and unsourced elsewhere."
  },
  {
   "claim_id": "C020",
   "loglog_ids": [
    "5"
   ],
   "label": "Trivia",
   "canonical_id": null,
   "reasoning": "Restated section header; the return and one-week trip recur concretely in C023-C024."
  },
  {
   "claim_id": "C021",
   "loglog_ids": [
    "5.1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Named dastgahs, Isfahan through Homayoun, dream-like feel. Detail beyond the header."
  },
  {
   "claim_id": "C022",
   "loglog_ids": [
    "5.2"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Vivid specifics: no lunch, back pain, fattened-lamb simile, first-night feeling."
  },
  {
   "claim_id": "C023",
   "loglog_ids": [
    "5.3"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Child-with-every-game simile plus departing tomorrow for a week. New framing."
  },
  {
   "claim_id": "C024",
   "loglog_ids": [
    "5.4"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Waiting to return and sit at the instrument adds a distinct longing image."
  }
 ],
 "metrics": {
  "scored_claims": 24,
  "unique": 19,
  "duplicates": 0,
  "trivia": 5,
  "redundancy_rate": 0.0,
  "trivia_rate": 0.2083,
  "structured_tokens": 24,
  "tokens_per_unique_claim": 1.26
 },
 "prune_list": [
  "C002 restated header, redundant with C003-C005, safe to cut",
  "C006 restated header, redundant with C007-C010, safe to cut",
  "C011 restated header, redundant with C013-C015, safe to cut",
  "C016 restated header, redundant with C017-C019, safe to cut",
  "C020 restated header, redundant with C021-C024, safe to cut"
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
   "claim_text": "کودکی که عاشق سنتور شد، سال‌ها با محدودیت کوک دیاتونیک ساخت و با سنتور کلیددار به آزادی مدولاسیون رسید.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "سنتور یه ساز دیاتونیک هست... اگه بخوای مدلاسیون انجام بدی باید کوک عوض بشه... یه سنتوری درست کردن که... کلید تعبیه کردن",
   "reasoning": "Summary faithfully combines the childhood love, the diatonic tuning constraint, and the keyed santur's modulation freedom."
  },
  {
   "claim_id": "C002",
   "loglog_ids": [
    "1"
   ],
   "claim_text": "شبی در هفت‌سالگی با سنتور خاله و زرد ملیجه عاشق ساز شدم.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "۷ سالم که بود یه شب شام خونه خاله‌م بودیم... یه آهنگ هم برامون زد، «زرد ملیجه» بود فکر کنم",
   "reasoning": "Age seven, the aunt's santur, and Zard Malijeh are stated; falling for the instrument is directly implied by the night's account."
  },
  {
   "claim_id": "C003",
   "loglog_ids": [
    "1.1"
   ],
   "claim_text": "هفت سالم بود، سنتور خاله کنج اتاق بود، زرد ملیجه زد، فکر کنم.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "۷ سالم که بود... سنتوری که تازه خریده بود... تو کنج اتاق بود. یه آهنگ هم برامون زد، «زرد ملیجه» بود فکر کنم",
   "reasoning": "All details align, including the preserved hedge 'فکر کنم'."
  },
  {
   "claim_id": "C004",
   "loglog_ids": [
    "1.2"
   ],
   "claim_text": "از اولین درس‌ها بود؛ مضراب یاد گرفتم و به‌زور از پای ساز بلندم کردند.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "از اولین آهنگهاییه که تو آموزش سنتور یاد میدن... مضراب دست گرفتن رو بهم نشون داد... آخر شب به زور من رو از پای ساز بلند کردن",
   "reasoning": "Song-first is rephrased as lesson-first with unchanged meaning; mezrab instruction and forced removal are stated."
  },
  {
   "claim_id": "C005",
   "loglog_ids": [
    "1.3"
   ],
   "claim_text": "احتمالا فقط شام پای ساز نبودم؛ تمام راه زر زدم و شیش ماه لج کردم.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "احتمالا فقط موقع شام پای ساز نبودم. تمام طول راه رو زر زدم... شیش ماه که این زر زدن‌ها و لج‌کردن‌ها ادامه داشت",
   "reasoning": "Probability hedge, whole-route nagging, and six months of persistence all match the source."
  },
  {
   "claim_id": "C006",
   "loglog_ids": [
    "2"
   ],
   "claim_text": "با تخفیف سنتور خریدم و با سازی گنده‌تر از خودم کلاس رفتم.",
   "claim_type": "interpretation",
   "verdict": "Partially supported",
   "severity": "Minor",
   "evidence_quote": "بالاخره برام یه سنتور خریدن... با تخفیف شد ۱۸هزار تومن... سازم از خودم گنده‌تر بود",
   "reasoning": "Source says family bought it for him; claim states 'I bought', shifting agency. Discount and oversized santur are supported."
  },
  {
   "claim_id": "C007",
   "loglog_ids": [
    "2.1"
   ],
   "claim_text": "۲۰هزار تومن با تخفیف ۱۸هزار شد؛ شیش ماه بعدتر رفتم کلاس.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "۲۰هزار تومن، با تخفیف شد ۱۸هزار تومن. شیش ماه بعدتر هم رفتم کلاس",
   "reasoning": "Both figures and the six-month interval match exactly."
  },
  {
   "claim_id": "C008",
   "loglog_ids": [
    "2.2"
   ],
   "claim_text": "اول استاد به خانه می‌آمد؛ اتاق پذیرایی سرد بود، حداقل اینطور یادم مانده.",
   "claim_type": "fact",
   "verdict": "Partially supported",
   "severity": "Harmless",
   "evidence_quote": "استادم میومد خونه... سنتورم تو اتاق پذیرایی بود... سردتر از بقیه اتاقها. حداقل اینطور تو ذهن من مونده",
   "reasoning": "Comparative 'colder than other rooms' is flattened to 'cold', though the memory hedge is retained."
  },
  {
   "claim_id": "C009",
   "loglog_ids": [
    "2.3"
   ],
   "claim_text": "بعد اداره ارشاد کلاس گذاشت؛ مبل‌ها فقط برای مهمان بود.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "مبل‌ها هم تو اون اتاق بودن و فقط وقتی مهمون داشتیم استفاده میشدن. بعدترها اداره ارشاد کلاس دایر کرد",
   "reasoning": "Both the student-only sofa use and the Ershad office classes are stated."
  },
  {
   "claim_id": "C010",
   "loglog_ids": [
    "2.4"
   ],
   "claim_text": "ساز از خودم گنده‌تر بود؛ ۷۲ سیم داشت و کوکش کار هرکسی نبود.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "سازم از خودم گنده‌تر بود... ۷۲ تا سیم داره و کار هرکسی نیست کوک کردنش",
   "reasoning": "Oversized instrument, 72 strings, and non-trivial tuning are all directly stated."
  },
  {
   "claim_id": "C011",
   "loglog_ids": [
    "3"
   ],
   "claim_text": "کوک زمان‌بر، سنتور دیاتونیک را به یک بازی در مهمانی محدود می‌کرد.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "مدلاسیون انجام بدی باید کوک عوض بشه که خب زمانبره... حس بچه‌ای... بهش فقط اجازه یه بازی رو داده باشن",
   "reasoning": "The time-consuming tuning and the one-game-at-a-party metaphor match the source."
  },
  {
   "claim_id": "C012",
   "loglog_ids": [
    "3.1"
   ],
   "claim_text": "با تیونر دیگر لازم نبود ساز را برای کوک به کلاس ببرم.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "بعدترها که تیونر اومد بازار دیگه نیاز نبود ساز رو ببرم سر کلاس چون دیگه خودم میتونستم کوکش کنم",
   "reasoning": "Negation and condition match exactly."
  },
  {
   "claim_id": "C013",
   "loglog_ids": [
    "3.2"
   ],
   "claim_text": "سنتور دیاتونیک است؛ یک دستگاه در آن واحد، مدولاسیون زمان‌بر است.",
   "claim_type": "definition",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "سنتور یه ساز دیاتونیک هست، ینی در آن واحد فقط میشه یک دستگاه/گام رو روش نواخت... باید کوک عوض بشه که خب زمانبره",
   "reasoning": "The definition and its consequence are stated verbatim in meaning."
  },
  {
   "claim_id": "C014",
   "loglog_ids": [
    "3.3"
   ],
   "claim_text": "مثل بچه‌ای بودم که فقط یک بازی مجاز است؛ اگه خسته می‌شدم نمی‌صرفید.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "حس بچه‌ای... بهش فقط اجازه یه بازی رو داده باشن... نمیصرفید، تا اون موقع حس بازی میرفت",
   "reasoning": "Both the single-game limitation and the 'not worth it' conclusion are present."
  },
  {
   "claim_id": "C015",
   "loglog_ids": [
    "3.4"
   ],
   "claim_text": "اگه بچه‌ها بازی عوض می‌کردند، حتی با علاقه گوشه می‌نشستم و نگاه می‌کردم.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "من مجبور بودم ساکت بشینم یه گوشه‌ای و نگاهشون کنم. حتی اگه اون بازی‌ رو خیلی دوست داشتم",
   "reasoning": "Sitting silently in a corner and watching, even when fond of the game, is stated."
  },
  {
   "claim_id": "C016",
   "loglog_ids": [
    "4"
   ],
   "claim_text": "سنتور کلیددار با ایده چنگ، تغییر ربع‌پرده را به ثانیه رساند.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "از چنگ ایده گرفتن و یه سری کلید تعبیه کردن که ربع یا نیم پرده زیرتر کردن هر نتی رو در کسری از ثانیه میشه انجام داد",
   "reasoning": "Harp-derived idea, keys, quarter-tone shifts, and sub-second speed are all present."
  },
  {
   "claim_id": "C017",
   "loglog_ids": [
    "4.1"
   ],
   "claim_text": "کلیدها ربع یا نیم پرده را در کسری از ثانیه زیرتر می‌کنند؛ مدولاسیون چندثانیه‌ای شد.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "ربع یا نیم پرده زیرتر کردن هر نتی رو در کسری از ثانیه... فقط با چند کلیک، فقط در چند ثانیه",
   "reasoning": "Quarter/half-tone shifts and multi-second modulation are stated precisely."
  },
  {
   "claim_id": "C018",
   "loglog_ids": [
    "4.2"
   ],
   "claim_text": "دو سالی به آن فکر می‌کردم؛ سالم از لنگرود به لنگفورد آوردنش را نمی‌دانستم.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "دو سالی بود که بهش فکر میکردم ولی نمیدونستم چطور میتونم سالم از لنگرود بیارمش لنگفورد",
   "reasoning": "Two years of thinking, the negation, the route, and 'safely' all match."
  },
  {
   "claim_id": "C019",
   "loglog_ids": [
    "4.3"
   ],
   "claim_text": "با کمک خانواده و دوستان و مسئولین و ائمه امروز به دستم رسید.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "با کمکهای بی دریغ خانواده و دوستان و مسئولین و ائمه امروز رسید به دستم",
   "reasoning": "All four helper groups and the timing are stated verbatim in meaning."
  },
  {
   "claim_id": "C020",
   "loglog_ids": [
    "5"
   ],
   "claim_text": "از اصفهان تا همایون بی‌وقفه نواختم؛ حالا یک هفته سفر، چشم‌انتظار بازگشتم.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "از اصفهان به سه‌گاه... از شور به همایون... نهار نخوردم، هی ساز زدم... حالا از فردا یک هفته‌ای مسافرتم... منتظرم برگردم",
   "reasoning": "Nonstop playing across the modes, the one-week trip, and longing to return are all present."
  },
  {
   "claim_id": "C021",
   "loglog_ids": [
    "5.1"
   ],
   "claim_text": "از اصفهان به سه‌گاه، نوا، شور، همایون رفتم؛ انگار خواب می‌دیدم.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "از اصفهان به سه‌گاه، از سه‌گاه به نوا، از نوا به شور، از شور به همایون... انگار داشتم خواب میدیدم",
   "reasoning": "Mode sequence and dream simile match exactly."
  },
  {
   "claim_id": "C022",
   "loglog_ids": [
    "5.2"
   ],
   "claim_text": "مثل گوسفند پرواری دویدم، نهار نخوردم، پشتم درد گرفت؛ حس شب اول بود.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "حکم گوسفند پرواری‌ای... بدون وقفه داشت میدوید، نهار نخوردم... پشتم درد گرفت. حس شب اولی رو داشتم",
   "reasoning": "The sheep metaphor, skipped lunch, back pain, and first-night feeling are all stated."
  },
  {
   "claim_id": "C023",
   "loglog_ids": [
    "5.3"
   ],
   "claim_text": "مثل بچه‌ای با هر بازی و کسی با هر حرف؛ از فردا یک هفته‌ای مسافرم.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "حس بچه‌ای... هر بازی‌ای که دوست داشت... حس کسی... هر حرفی رو میخواست... حالا از فردا یک هفته‌ای مسافرتم",
   "reasoning": "Both similes and the one-week trip are directly stated."
  },
  {
   "claim_id": "C024",
   "loglog_ids": [
    "5.4"
   ],
   "claim_text": "نرفته منتظر برگشتن و نشستن پای سازم.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Critical",
   "evidence_quote": "نرفته منتظرم برگردم و بشینم پای ساز",
   "reasoning": "The negation and both awaited actions match exactly."
  }
 ],
 "metrics": {
  "total_claims": 24,
  "supported": 22,
  "partially_supported": 2,
  "unverifiable": 0,
  "contradicted": 0,
  "critical_errors": 0,
  "faithfulness_precision": 0.9167
 },
 "fail_list": [
  "C006",
  "C008"
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
   "presence": "Present",
   "loglog_ids": [
    "L004",
    "L005"
   ],
   "evidence_quote": "هفت سالم بود، سنتور خاله کنج اتاق بود ... مضراب یاد گرفتم و به‌زور از پای ساز بلندم کردند.",
   "reasoning": "Age 7, the aunt's santur at her house, the first encounter, learning the mizrab, and being forcibly lifted from the instrument are all captured. The 'cousin' attribution is compressed to 'aunt', a harmless simplification that does not change the origin-story meaning."
  },
  {
   "point_id": "K02",
   "point_text": "The first tune he heard on that santur was likely 'Zard Maliheh' (زرد ملیجه), one of the first songs taught to santur beginners.",
   "weight": "Nice to have",
   "presence": "Present",
   "loglog_ids": [
    "L004"
   ],
   "evidence_quote": "زرد ملیجه زد، فکر کنم.",
   "reasoning": "The tune name is preserved along with the hedging 'I think', matching the source's uncertainty."
  },
  {
   "point_id": "K03",
   "point_text": "After six months of nagging and sulking, his family finally bought him a santur for 20,000 toman, discounted to 18,000 toman.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L008"
   ],
   "evidence_quote": "۲۰هزار تومن با تخفیف ۱۸هزار شد؛ شیش ماه بعدتر رفتم کلاس.",
   "reasoning": "Both numbers (20,000 and discounted 18,000) are intact, and the six-month wait/sulking is captured at L006-L008, so the acquisition milestone holds."
  },
  {
   "point_id": "K04",
   "point_text": "He started lessons six months later; the teacher initially came to his home because their city had no school, and only later did the Ershad office open a class where the teacher taught.",
   "weight": "Nice to have",
   "presence": "Present",
   "loglog_ids": [
    "L008",
    "L009",
    "L010"
   ],
   "evidence_quote": "شیش ماه بعدتر رفتم کلاس ... اول استاد به خانه می‌آمد ... بعد اداره ارشاد کلاس گذاشت.",
   "reasoning": "All three beats (six months later, teacher at home, later Ershad office class) are present in the correct sequence."
  },
  {
   "point_id": "K05",
   "point_text": "The santur has 72 strings and is hard for an ordinary person to tune, so he had to haul the oversized instrument to class to be tuned, until electronic tuners reached the market and he could tune it himself.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L011",
    "L013"
   ],
   "evidence_quote": "۷۲ سیم داشت و کوکش کار هرکسی نبود ... با تیونر دیگر لازم نبود ساز را برای کوک به کلاس ببرم.",
   "reasoning": "The 72-string number, the tuning difficulty, the hauling to class, and the electronic tuner resolution are all preserved."
  },
  {
   "point_id": "K06",
   "point_text": "The santur is a diatonic instrument: only one dastgah/scale can be played at a time, and modulation requires retuning, which is time-consuming.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L014"
   ],
   "evidence_quote": "سنتور دیاتونیک است؛ یک دستگاه در آن واحد، مدولاسیون زمان‌بر است.",
   "reasoning": "Diatonic nature, single-dastgah-at-a-time constraint, and time-consuming modulation are all captured verbatim."
  },
  {
   "point_id": "K07",
   "point_text": "This limitation made him feel like a child at a party allowed only one game: to switch he would have to pack up all his toys first, by which time the mood is gone, or else sit silently aside while the other children move to a game he loves.",
   "weight": "Nice to have",
   "presence": "Present",
   "loglog_ids": [
    "L015",
    "L016"
   ],
   "evidence_quote": "مثل بچه‌ای بودم که فقط یک بازی مجاز است ... اگه بچه‌ها بازی عوض می‌کردند، حتی با علاقه گوشه می‌نشستم و نگاه می‌کردم.",
   "reasoning": "The one-game-at-a-party analogy and the sitting-aside-while-others-switch image are both preserved, though the 'packing up toys' clause is implied rather than explicit."
  },
  {
   "point_id": "K08",
   "point_text": "Recently a santur was built inspired by the harp, with a set of keys allowing any note to be lowered by a quarter or half step in a fraction of a second.",
   "weight": "Must have",
   "presence": "Partial",
   "loglog_ids": [
    "L017",
    "L018"
   ],
   "evidence_quote": "سنتور کلیددار با ایده چنگ ... کلیدها ربع یا نیم پرده را در کسری از ثانیه زیرتر می‌کنند.",
   "reasoning": "The harp-inspired keyed santur, the quarter/half-step change, and the fraction-of-a-second speed are all present. But the loglog says the keys make notes 'زیرتر' (higher), reversing the source's 'lowered' direction. This directional inversion is a meaning change on a Must have point, so at most Partial."
  },
  {
   "point_id": "K09",
   "point_text": "This makes it possible to move quickly from any dastgah to any other with a few clicks, in just seconds.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L018",
    "L029"
   ],
   "evidence_quote": "مدولاسیون چندثانیه‌ای شد.",
   "reasoning": "The fast, few-seconds modulation across dastgahs is captured, and the cross-link L029 ties the played sequence to this capability."
  },
  {
   "point_id": "K10",
   "point_text": "He had been thinking about such an instrument for two years but did not know how to bring it safely from Langroud to Langford.",
   "weight": "Nice to have",
   "presence": "Present",
   "loglog_ids": [
    "L019"
   ],
   "evidence_quote": "دو سالی به آن فکر می‌کردم؛ سالم از لنگرود به لنگفورد آوردنش را نمی‌دانستم.",
   "reasoning": "Both the two-year rumination and the Langroud-to-Langford transport problem are preserved."
  },
  {
   "point_id": "K11",
   "point_text": "With the unstinting help of family, friends, officials, and clerics/community leaders, the instrument finally reached him today.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L020"
   ],
   "evidence_quote": "با کمک خانواده و دوستان و مسئولین و ائمه امروز به دستم رسید.",
   "reasoning": "The arrival today and the full list of helpers (family, friends, officials, imams/leaders) are all captured."
  },
  {
   "point_id": "K12",
   "point_text": "He tuned it and played, moving from dastgah to dastgah: Isfahan to Segah, Segah to Nava, Nava to Shur, Shur to Homayoun.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L022"
   ],
   "evidence_quote": "از اصفهان به سه‌گاه، نوا، شور، همایون رفتم.",
   "reasoning": "The exact modulation sequence Isfahan, Segah, Nava, Shur, Homayoun is preserved."
  },
  {
   "point_id": "K13",
   "point_text": "He felt like a penned fattened sheep set loose, running without pause: he skipped lunch and played so long his back ached.",
   "weight": "Nice to have",
   "presence": "Present",
   "loglog_ids": [
    "L023"
   ],
   "evidence_quote": "مثل گوسفند پرواری دویدم، نهار نخوردم، پشتم درد گرفت.",
   "reasoning": "The fattened-sheep image, the skipped lunch, and the aching back are all captured."
  },
  {
   "point_id": "K14",
   "point_text": "He felt like the first night his aunt put the mizrabs in his hand, like a child allowed to play any game he wants, like a person free to say anything he wishes.",
   "weight": "Nice to have",
   "presence": "Present",
   "loglog_ids": [
    "L023",
    "L024"
   ],
   "evidence_quote": "حس شب اول بود ... مثل بچه‌ای با هر بازی و کسی با هر حرف.",
   "reasoning": "The callback to the first night, the any-game child, and the free-to-say-anything person are all represented."
  },
  {
   "point_id": "K15",
   "point_text": "He leaves tomorrow on a week of travel and is unhappy at not being home to play, already waiting to return and sit at the instrument.",
   "weight": "Nice to have",
   "presence": "Present",
   "loglog_ids": [
    "L024",
    "L025"
   ],
   "evidence_quote": "از فردا یک هفته‌ای مسافرم ... نرفته منتظر برگشتن و نشستن پای سازم.",
   "reasoning": "The week of travel starting tomorrow and his preemptive longing to return and sit at the instrument are both preserved."
  }
 ],
 "metrics": {
  "total_points": 15,
  "must_have_total": 8,
  "must_have_present": 7,
  "must_have_partial": 1,
  "must_have_missing": 0,
  "overall_present": 14,
  "must_recall": 0.9375,
  "overall_recall": 0.9667
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
   "reasoning": "Top-level arc: childhood love, diatonic limitation, keyed freedom. The document's thesis, not restated elsewhere."
  },
  {
   "claim_id": "C002",
   "loglog_ids": [
    "1"
   ],
   "label": "Trivia",
   "canonical_id": null,
   "reasoning": "Restated section header; the concrete detail lives in C003-C005 and the summary."
  },
  {
   "claim_id": "C003",
   "loglog_ids": [
    "1.1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Specifics: age seven, aunt's santur in the corner, Zard-e-Malijeh, hedged memory."
  },
  {
   "claim_id": "C004",
   "loglog_ids": [
    "1.2"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "First lessons, learning mizrab, being forced off the instrument. New content."
  },
  {
   "claim_id": "C005",
   "loglog_ids": [
    "1.3"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Stubbornness, six months of sulking, walking the whole road. Distinct detail."
  },
  {
   "claim_id": "C006",
   "loglog_ids": [
    "2"
   ],
   "label": "Trivia",
   "canonical_id": null,
   "reasoning": "Restated section header; all substance carried by C007-C010."
  },
  {
   "claim_id": "C007",
   "loglog_ids": [
    "2.1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Discounted price 20k to 18k and six-month delay are non-trivial numbers."
  },
  {
   "claim_id": "C008",
   "loglog_ids": [
    "2.2"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Teacher came home, cold living room, explicit hedge. Caveat keeps it in scope."
  },
  {
   "claim_id": "C009",
   "loglog_ids": [
    "2.3"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Ershad office hosted classes later; couches reserved for guests. Human detail."
  },
  {
   "claim_id": "C010",
   "loglog_ids": [
    "2.4"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Seventy-two strings and hard tuning are concrete facts beyond the header."
  },
  {
   "claim_id": "C011",
   "loglog_ids": [
    "3"
   ],
   "label": "Trivia",
   "canonical_id": null,
   "reasoning": "Restated section header; limitation and tuning cost detailed in C013-C015."
  },
  {
   "claim_id": "C012",
   "loglog_ids": [
    "3.1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Tuner removed the need to carry the instrument to class. New operational fact."
  },
  {
   "claim_id": "C013",
   "loglog_ids": [
    "3.2"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Explicit definition: diatonic, one dastgah per time, time-consuming modulation."
  },
  {
   "claim_id": "C014",
   "loglog_ids": [
    "3.3"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Child-with-one-permitted-game analogy adds the boredom consequence, not just the image."
  },
  {
   "claim_id": "C015",
   "loglog_ids": [
    "3.4"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Watching from the corner when others switch games. Distinct behavioral detail."
  },
  {
   "claim_id": "C016",
   "loglog_ids": [
    "4"
   ],
   "label": "Trivia",
   "canonical_id": null,
   "reasoning": "Restated section header; the quarter-tone mechanism is developed in C017-C019."
  },
  {
   "claim_id": "C017",
   "loglog_ids": [
    "4.1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Quarter or half tone raised in fractions of a second; adds half-step and timing."
  },
  {
   "claim_id": "C018",
   "loglog_ids": [
    "4.2"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Two years of thinking and the Langarud-to-Langford transfer problem. Specific."
  },
  {
   "claim_id": "C019",
   "loglog_ids": [
    "4.3"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Arrival credited to family, friends, officials, and imams. Specific and unsourced elsewhere."
  },
  {
   "claim_id": "C020",
   "loglog_ids": [
    "5"
   ],
   "label": "Trivia",
   "canonical_id": null,
   "reasoning": "Restated section header; the return and one-week trip recur concretely in C023-C024."
  },
  {
   "claim_id": "C021",
   "loglog_ids": [
    "5.1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Named dastgahs, Isfahan through Homayoun, dream-like feel. Detail beyond the header."
  },
  {
   "claim_id": "C022",
   "loglog_ids": [
    "5.2"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Vivid specifics: no lunch, back pain, fattened-lamb simile, first-night feeling."
  },
  {
   "claim_id": "C023",
   "loglog_ids": [
    "5.3"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Child-with-every-game simile plus departing tomorrow for a week. New framing."
  },
  {
   "claim_id": "C024",
   "loglog_ids": [
    "5.4"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Waiting to return and sit at the instrument adds a distinct longing image."
  }
 ],
 "metrics": {
  "scored_claims": 24,
  "unique": 19,
  "duplicates": 0,
  "trivia": 5,
  "redundancy_rate": 0.0,
  "trivia_rate": 0.2083,
  "structured_tokens": 24,
  "tokens_per_unique_claim": 1.26
 },
 "prune_list": [
  "C002 restated header, redundant with C003-C005, safe to cut",
  "C006 restated header, redundant with C007-C010, safe to cut",
  "C011 restated header, redundant with C013-C015, safe to cut",
  "C016 restated header, redundant with C017-C019, safe to cut",
  "C020 restated header, redundant with C021-C024, safe to cut"
 ]
}
```

## Judge Top (overall), opencode-go/deepseek-v4.1-flash

```json
{
 "judge": "overall",
 "judge_version": "1.0.0",
 "model": "opencode-go/deepseek-v4.1-flash 2026-09-15",
 "source_id": "unspecified",
 "inputs": {
  "faithfulness_precision": 0.9167,
  "critical_errors": 0,
  "must_recall": 0.9375,
  "overall_recall": 0.9667,
  "redundancy_rate": 0.0,
  "trivia_rate": 0.2083
 },
 "weights_used": {
  "faithfulness_precision": 0.4,
  "coverage_must_recall": 0.4,
  "redundancy_penalty": 0.2
 },
 "computation": "weighted score = 0.4*0.9167 + 0.4*0.9375 - 0.2*0.0 = 0.36668 + 0.37500 - 0.00000 = 0.74168",
 "weighted_score": 0.7417,
 "verdict": "Fail",
 "tradeoff_note": "All quality gates pass except faithfulness_precision, which at 0.9167 falls below the 0.95 minimum, so the sample fails regardless of the solid must_recall (0.9375) and zero redundancy. Coverage and concision cannot rescue a faithfulness gate miss.",
 "fix_list": [
  "Repair claim C006: source says the family bought the santur (بالاخره برام یه سنتور خریدن) but the draft states 'I bought it' (با تخفیف سنتور خریدم), shifting agency. Correcting this one claim raises supported to 23/24 = 0.9583, clearing the 0.95 precision gate.",
  "Repair claim C008: source says the room was 'colder than the other rooms' (سردتر از بقیه اتاقها) but the draft flattens it to merely 'cold' (سرد بود). Restore the comparative to convert this from Partially supported to supported.",
  "Fix point K08: the loglog says the harp-inspired keys make notes زیرتر (higher), inverting the source's 'lowered by a quarter or half step' direction. This directional inversion is a meaning change on a Must have point and must be corrected to preserve both recall and factual accuracy."
 ],
 "reasoning": "Gate checks in order. (1) Hard fail on critical errors: faithfulness critical_errors = 0, equals critical_contradicted_max of 0, so this gate passes. (2) Hard fail on must recall: must_recall = 0.9375 from coverage (7 present + 1 partial of 8 must-have points), and 0.9375 >= must_recall_min of 0.90, so this gate passes. The single partial, K08, is under the minimum threshold. (3) Hard fail on faithfulness precision: faithfulness_precision = 0.9167 (22 supported of 24 total claims), which is below faithfulness_precision_min of 0.95. This gate is missed, so per policy the sample fails. The two non-supported claims driving this are C006 (agency shift: 'I bought' versus source's family purchase, Minor) and C008 (comparative 'colder' flattened to 'cold', Harmless). Either one lifted to supported yields 23/24 = 0.9583 and clears the gate, making C006 the highest-leverage fix since it also removes a semantic misattribution. For completeness the weighted score is computed: 0.4*0.9167 = 0.36668, 0.4*0.9375 = 0.37500, minus 0.2*0.0 = 0.00000, totaling 0.74168. Concision contributes nothing here since redundancy_rate = 0.0 sits below redundancy_max of 0.15, and trivia_rate of 0.2083 with the five header-restatement entries (C002, C006, C011, C016, C020) is a polish issue only, not a gate. Borderline is not applicable: a numerical gate was missed, so the verdict is a hard Fail, not a borderline pass. The failure is narrow and cheap to reverse, but per policy concision and coverage gains never compensate for a faithfulness precision miss."
}
```
