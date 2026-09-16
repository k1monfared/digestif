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
   "severity": "Harmless",
   "evidence_quote": "سنتور یه ساز دیاتونیک هست ... اگه بخوای مدلاسیون انجام بدی باید کوک عوض بشه ... یه سنتوری درست کردن که ... کلید تعبیه کردن",
   "reasoning": "Summary of love for santur, diatonic limitation, and keyed solution matches source narrative."
  },
  {
   "claim_id": "C002",
   "loglog_ids": [
    "1"
   ],
   "claim_text": "شبی در هفت‌سالگی با سنتور خاله و آهنگی که فکر کنم زرد ملیجه بود، عاشق ساز شدم.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "۷ سالم که بود ... شام خونه خاله‌م بودیم ... «زرد ملیجه» بود فکر کنم",
   "reasoning": "Age, aunt's santur, and hedged Zard Malijeh are stated; love is a fair reading of the encounter."
  },
  {
   "claim_id": "C003",
   "loglog_ids": [
    "1.1"
   ],
   "claim_text": "هفت سالم بود؛ سنتور خاله که تازه خریده بود و داشت یاد می‌گرفت کنج اتاق بود و زرد ملیجه زد، فکر کنم.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "۷ سالم که بود ... سنتوری که تازه خریده بود و داشت یاد میگرفت ... تو کنج اتاق بود. یه آهنگ هم برامون زد، «زرد ملیجه» بود فکر کنم.",
   "reasoning": "All details and the hedging match the source span directly."
  },
  {
   "claim_id": "C004",
   "loglog_ids": [
    "1.2"
   ],
   "claim_text": "زرد ملیجه از اولین آهنگ‌هایی بود که در آموزش سنتور یاد می‌دهند؛ با روی گشاده مضراب دست گرفتن را نشانم داد.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "از اولین آهنگهاییه که تو آموزش سنتور یاد میدن ... اونم با روی گشاده ... مضراب دست گرفتن رو بهم نشون داد.",
   "reasoning": "Both the song's early-place status and the open-handed mizrab instruction are stated."
  },
  {
   "claim_id": "C005",
   "loglog_ids": [
    "1.3"
   ],
   "claim_text": "تنها چیز یادم از آن شب این است که آخر شب به زور از پای ساز بلندم کردند.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "تنها چیزی که از اون شب یادم میاد اینه که آخر شب به زور من رو از پای ساز بلند کردن",
   "reasoning": "Near-verbatim match with the source sentence."
  },
  {
   "claim_id": "C006",
   "loglog_ids": [
    "1.4"
   ],
   "claim_text": "احتمالا فقط موقع شام پای ساز نبودم؛ تمام طول راه زر زدم که سنتور می‌خواهم.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "احتمالا فقط موقع شام پای ساز نبودم. تمام طول راه رو زر زدم که سنتور میخوام.",
   "reasoning": "Wording and the hedge احتمالا preserved exactly."
  },
  {
   "claim_id": "C007",
   "loglog_ids": [
    "1.5"
   ],
   "claim_text": "شیش ماه زر زدن و لج‌کردن ادامه داشت تا بالاخره برایم سنتور خریدند.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "شیش ماه که این زر زدن‌ها و لج‌کردن‌ها ادامه داشت بالاخره برام یه سنتور خریدن.",
   "reasoning": "Duration and the plural buyer attribution match the source."
  },
  {
   "claim_id": "C008",
   "loglog_ids": [
    "2"
   ],
   "claim_text": "سنتور را با تخفیف خریدم و یادگیری را با دشواری‌های ساز و مکان شروع کردم.",
   "claim_type": "interpretation",
   "verdict": "Contradicted",
   "severity": "Critical",
   "evidence_quote": "بالاخره برام یه سنتور خریدن. ۲۰هزار تومن، با تخفیف شد ۱۸هزار تومن.",
   "reasoning": "Source says the santur was bought for the author (خریدن), but the node attributes the purchase to the author (خریدم): wrong attribution."
  },
  {
   "claim_id": "C009",
   "loglog_ids": [
    "2.1"
   ],
   "claim_text": "۲۰هزار تومن بود، با تخفیف ۱۸هزار شد؛ شیش ماه بعدتر رفتم کلاس و شروع کردم به یاد گرفتن.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "۲۰هزار تومن، با تخفیف شد ۱۸هزار تومن. شیش ماه بعدتر هم رفتم کلاس و شروع کردم به یاد گرفتن.",
   "reasoning": "Both prices and the six-month gap match the source exactly."
  },
  {
   "claim_id": "C010",
   "loglog_ids": [
    "2.2"
   ],
   "claim_text": "اوایل استاد به خانه می‌آمد چون در شهرمان آموزشگاهی نبود؛ سنتورم در اتاق پذیرایی دربسته و از بقیه سردتر بود، حداقل این‌طور در ذهنم مانده.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "اوایل استادم میومد خونه، چون تو شهرمون آموزشگاهی نبود ... سنتورم تو اتاق پذیرایی بود که همیشه درش بسته بود و سردتر از بقیه اتاقها. حداقل اینطور تو ذهن من مونده.",
   "reasoning": "All clauses and the memory hedge are directly stated."
  },
  {
   "claim_id": "C011",
   "loglog_ids": [
    "2.3"
   ],
   "claim_text": "مبل‌های آن اتاق فقط وقتی مهمان داشتیم استفاده می‌شدند؛ بعدترها اداره ارشاد کلاس دایر کرد و استاد همان‌جا تدریس می‌کرد.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "فقط وقتی مهمون داشتیم استفاده میشدن. بعدترها اداره ارشاد کلاس دایر کرد و استادم همونجا تدریس میکرد",
   "reasoning": "The 'only' restriction and the Ershad class detail match the source."
  },
  {
   "claim_id": "C012",
   "loglog_ids": [
    "2.4"
   ],
   "claim_text": "سازم از خودم گنده‌تر بود و به زور می‌بردمش سر کلاس؛ ۷۲ سیم داشت و کوکش کار هرکسی نبود.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "سازم از خودم گنده‌تر بود و به زور میکشیدمش که ببرمش سر کلاس ... ۷۲ تا سیم داره و کار هرکسی نیست کوک کردنش.",
   "reasoning": "The 72-string count and the 'not everyone's job' negation are preserved."
  },
  {
   "claim_id": "C013",
   "loglog_ids": [
    "3"
   ],
   "claim_text": "محدودیت کوک دیاتونیک، نواختن سنتور را مثل یک بازی محدود می‌کرد.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "این باعث شده بود که همیشه موقع ساز زدن حس بچه‌ای رو داشته باشم که تو مهمونی بهش فقط اجازه یه بازی رو داده باشن.",
   "reasoning": "The restricted-game metaphor is the source's own image for the tuning limitation."
  },
  {
   "claim_id": "C014",
   "loglog_ids": [
    "3.1"
   ],
   "claim_text": "بعدترها تیونر آمد و دیگر لازم نبود ساز را برای کوک به کلاس ببرم؛ اما این محدودیت جنبه‌های دیگر هم داشت.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "بعدترها که تیونر اومد بازار دیگه نیاز نبود ساز رو ببرم سر کلاس ... اما این محدودیت کوک سنتور جنبه‌های دیگه هم داشت.",
   "reasoning": "The tuner arrival, removal of the need, and 'other aspects' clause all match."
  },
  {
   "claim_id": "C015",
   "loglog_ids": [
    "3.2"
   ],
   "claim_text": "سنتور دیاتونیک است: در آن واحد فقط یک دستگاه/گام، و مدولاسیون یعنی عوض کردن کوک که زمانبر است.",
   "claim_type": "definition",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "سنتور یه ساز دیاتونیک هست، ینی در آن واحد فقط میشه یک دستگاه/گام رو روش نواخت و اگه بخوای مدلاسیون انجام بدی باید کوک عوض بشه که خب زمانبره.",
   "reasoning": "Definition and the 'only one' limitation and time-consuming retuning are preserved."
  },
  {
   "claim_id": "C016",
   "loglog_ids": [
    "3.3"
   ],
   "claim_text": "حس بچه‌ای را داشتم که در مهمانی فقط اجازه یک بازی به او داده شده باشد.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "حس بچه‌ای رو داشته باشم که تو مهمونی بهش فقط اجازه یه بازی رو داده باشن.",
   "reasoning": "The simile and its 'only' restriction match the source."
  },
  {
   "claim_id": "C017",
   "loglog_ids": [
    "3.4"
   ],
   "claim_text": "اگر از آن بازی خسته می‌شدم، اول باید همه اسباب‌بازی‌ها را جمع می‌کردم و بعد بازی دیگری در می‌آوردم؛ نمی‌صرفید، حس بازی می‌رفت.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "اگه از اون بازی خسته میشدم ... باید اول همه اسباب‌بازی‌هام رو جمع میکردم و بعد اسباب‌بازی‌های دیگه رو در میاوردم. نمیصرفید، تا اون موقع حس بازی میرفت.",
   "reasoning": "Conditional and consequence match; omission of one clause does not change the meaning."
  },
  {
   "claim_id": "C018",
   "loglog_ids": [
    "3.5"
   ],
   "claim_text": "اگر بچه‌ها از یک بازی به بازی دیگر می‌رفتند، مجبور بودم ساکت گوشه‌ای بنشینم و نگاه کنم، حتی اگر آن بازی را خیلی دوست داشتم.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "وقتی اونا از یه بازی میرفتن به بازی دیگه‌ای، من مجبور بودم ساکت بشینم یه گوشه‌ای و نگاهشون کنم. حتی اگه اون بازی‌ رو خیلی دوست داشتم.",
   "reasoning": "Both the circumstances and the 'even if I liked it' clause are stated."
  },
  {
   "claim_id": "C019",
   "loglog_ids": [
    "4"
   ],
   "claim_text": "راه‌حل کلیددار با ایده چنگ، محدودیت دیاتونیک را برداشت.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "یه سنتوری درست کردن که از چنگ ایده گرفتن و یه سری کلید تعبیه کردن ... این یعنی میشد سریع از هر دستگاهی به هر دستگاه دیگه برم",
   "reasoning": "Harp-inspired keys and removal of the tuning limitation follow from the source."
  },
  {
   "claim_id": "C020",
   "loglog_ids": [
    "4.1"
   ],
   "claim_text": "کلیدها ربع یا نیم پرده زیرتر کردن هر نت را در کسری از ثانیه ممکن کردند.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "یه سری کلید تعبیه کردن که ربع یا نیم پرده زیرتر کردن هر نتی رو در کسری از ثانیه میشه انجام داد.",
   "reasoning": "The quarter/half-tone shift and fraction-of-a-second timing are verbatim."
  },
  {
   "claim_id": "C021",
   "loglog_ids": [
    "4.2"
   ],
   "claim_text": "جابه‌جایی سریع از هر دستگاهی به هر دستگاه دیگر ممکن شد، فقط با چند کلیک و در چند ثانیه.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "میشد سریع از هر دستگاهی به هر دستگاه دیگه برم، فقط با چند کلیک، فقط در چند ثانیه.",
   "reasoning": "The clicks and seconds qualifiers and the 'any dastgah' scope match."
  },
  {
   "claim_id": "C022",
   "loglog_ids": [
    "4.3"
   ],
   "claim_text": "دو سالی بود به آن فکر می‌کردم ولی نمی‌دانستم چطور سالم از لنگرود به لنگفورد بیاورمش.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "دو سالی بود که بهش فکر میکردم ولی نمیدونستم چطور میتونم سالم از لنگرود بیارمش لنگفورد.",
   "reasoning": "Two years, the doubt, and both place names are preserved."
  },
  {
   "claim_id": "C023",
   "loglog_ids": [
    "4.4"
   ],
   "claim_text": "با کمک‌های بی‌دریغ خانواده و دوستان و مسئولین و ائمه، امروز به دستم رسید.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "بالاخره با کمک‌های بی دریغ خانواده و دوستان و مسئولین و ائمه امروز رسید به دستم.",
   "reasoning": "The list of helpers and today's arrival match the source."
  },
  {
   "claim_id": "C024",
   "loglog_ids": [
    "5"
   ],
   "claim_text": "شعف نواختن آزاد و دلتنگی سفر پیش رو.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "هی از این دستگاه رفتم تو اون دستگاه ... ناراحتم که چرا خونه نیستم که ساز بزنم. نرفته منتظرم برگردم",
   "reasoning": "Joy of free playing and sadness about the trip match the source's tone."
  },
  {
   "claim_id": "C025",
   "loglog_ids": [
    "5.1"
   ],
   "claim_text": "از اصفهان به سه‌گاه، از سه‌گاه به نوا، از نوا به شور، از شور به همایون رفتم؛ انگار خواب می‌دیدم.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "از اصفهان به سه‌گاه، از سه‌گاه به نوا، از نوا به شور، از شور به همایون. ... انگار داشتم خواب میدیدم.",
   "reasoning": "The modulation chain and dream simile are verbatim from the source."
  },
  {
   "claim_id": "C026",
   "loglog_ids": [
    "5.2"
   ],
   "claim_text": "حکم گوسفند پرواری رهاشده‌ای را داشتم که بدون وقفه می‌دوید؛ نهار نخوردم و آن‌قدر ساز زدم که پشتم درد گرفت.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "حکم گوسفند پرواری‌ای رو داشتم که بازش کرده بودن و بدون وقفه داشت میدوید، نهار نخوردم، هی ساز زدم، اینقدر که پشتم درد گرفت.",
   "reasoning": "The sheep simile, skipping lunch, and back pain all match."
  },
  {
   "claim_id": "C027",
   "loglog_ids": [
    "5.3"
   ],
   "claim_text": "حس شب اولی را داشتم که خاله‌م مضراب‌ها را داد دستم؛ حس بچه‌ای با هر بازی و کسی با هر حرف.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "حس شب اولی رو داشتم که خاله‌م مضراب‌های سنتور رو داد دستم. حس بچه‌ای ... هر بازی‌ای ... حس کسی ... هر حرفی",
   "reasoning": "First-night feeling, aunt's mizrabs, and the two freedoms are all present."
  },
  {
   "claim_id": "C028",
   "loglog_ids": [
    "5.4"
   ],
   "claim_text": "از فردا یک هفته‌ای مسافرم؛ ناراحتم که چرا خانه نیستم که ساز بزنم.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "حالا از فردا یک هفته‌ای مسافرتم، ناراحتم که چرا خونه نیستم که ساز بزنم.",
   "reasoning": "The one-week trip starting tomorrow and the sadness match verbatim."
  },
  {
   "claim_id": "C029",
   "loglog_ids": [
    "5.5"
   ],
   "claim_text": "نرفته منتظرم برگردم و بنشینم پای ساز.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "نرفته منتظرم برگردم و بشینم پای ساز.",
   "reasoning": "Near-verbatim match with the closing sentence."
  }
 ],
 "metrics": {
  "total_claims": 29,
  "supported": 28,
  "partially_supported": 0,
  "unverifiable": 0,
  "contradicted": 1,
  "critical_errors": 1,
  "faithfulness_precision": 0.9655
 },
 "fail_list": [
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
    "L003",
    "L004",
    "L005",
    "L006"
   ],
   "evidence_quote": "هفت سالم بود؛ سنتور خاله که تازه خریده بود ... با روی گشاده مضراب دست گرفتن را نشانم داد ... آخر شب به زور از پای ساز بلندم کردند",
   "reasoning": "Age (7), the aunt's house, the newly bought santur, the teaching of how to hold the mizrab, and being forcibly lifted from the instrument at night's end are all present. The loglog attributes the purchase to خاله (aunt) rather than the cousin named in the key point, but since the key point itself conflates the aunt/cousin, the origin story is fully preserved."
  },
  {
   "point_id": "K02",
   "point_text": "The first tune he heard on that santur was likely 'Zard Maliheh' (زرد ملیجه), one of the first songs taught to santur beginners.",
   "weight": "Nice to have",
   "presence": "Present",
   "loglog_ids": [
    "L004",
    "L005"
   ],
   "evidence_quote": "زرد ملیجه زد، فکر کنم ... زرد ملیجه از اولین آهنگ‌هایی بود که در آموزش سنتور یاد می‌دهند",
   "reasoning": "Both the tune name and the hedged certainty (فکر کنم) plus its status as a beginner song are captured."
  },
  {
   "point_id": "K03",
   "point_text": "After six months of nagging and sulking, his family finally bought him a santur for 20,000 toman, discounted to 18,000 toman.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L007",
    "L008",
    "L010"
   ],
   "evidence_quote": "شیش ماه زر زدن و لج‌کردن ادامه داشت تا بالاخره برایم سنتور خریدند ... ۲۰هزار تومن بود، با تخفیف ۱۸هزار شد",
   "reasoning": "Six months of nagging/sulking, the purchase, and both numbers (20,000 and discounted 18,000 toman) are intact."
  },
  {
   "point_id": "K04",
   "point_text": "He started lessons six months later; the teacher initially came to his home because their city had no school, and only later did the Ershad office open a class where the teacher taught.",
   "weight": "Nice to have",
   "presence": "Present",
   "loglog_ids": [
    "L010",
    "L011",
    "L012"
   ],
   "evidence_quote": "شیش ماه بعدتر رفتم کلاس ... اوایل استاد به خانه می‌آمد چون در شهرمان آموزشگاهی نبود ... بعدترها اداره ارشاد کلاس دایر کرد",
   "reasoning": "Six-month gap, home lessons due to absence of a school, and the later Ershad office class are all present."
  },
  {
   "point_id": "K05",
   "point_text": "The santur has 72 strings and is hard for an ordinary person to tune, so he had to haul the oversized instrument to class to be tuned, until electronic tuners reached the market and he could tune it himself.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L013",
    "L015"
   ],
   "evidence_quote": "سازم از خودم گنده‌تر بود و به زور می‌بردمش سر کلاس؛ ۷۲ سیم داشت و کوکش کار هرکسی نبود ... بعدترها تیونر آمد و دیگر لازم نبود ساز را برای کوک به کلاس ببرم",
   "reasoning": "The 72-string count, untunability for an ordinary person, hauling the oversized instrument to class, and the arrival of the tuner are all preserved, including the cross-link L033 noting the tuner solved only the transport problem."
  },
  {
   "point_id": "K06",
   "point_text": "The santur is a diatonic instrument: only one dastgah/scale can be played at a time, and modulation requires retuning, which is time-consuming.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L016"
   ],
   "evidence_quote": "سنتور دیاتونیک است: در آن واحد فقط یک دستگاه/گام، و مدولاسیون یعنی عوض کردن کوک که زمانبر است",
   "reasoning": "The central limitation is stated exactly: diatonic, one dastgah at a time, modulation means retuning, and retuning is time-consuming."
  },
  {
   "point_id": "K07",
   "point_text": "This limitation made him feel like a child at a party allowed only one game: to switch he would have to pack up all his toys first, by which time the mood is gone, or else sit silently aside while the other children move to a game he loves.",
   "weight": "Nice to have",
   "presence": "Present",
   "loglog_ids": [
    "L017",
    "L018",
    "L019"
   ],
   "evidence_quote": "حس بچه‌ای را داشتم که در مهمانی فقط اجازه یک بازی به او داده شده باشد ... اول باید همه اسباب‌بازی‌ها را جمع می‌کردم ... مجبور بودم ساکت گوشه‌ای بنشینم",
   "reasoning": "All three beats of the analogy are present: one-game child, packing toys with the mood gone, and sitting silently aside."
  },
  {
   "point_id": "K08",
   "point_text": "Recently a santur was built inspired by the harp, with a set of keys allowing any note to be lowered by a quarter or half step in a fraction of a second.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L020",
    "L021"
   ],
   "evidence_quote": "راه‌حل کلیددار با ایده چنگ ... کلیدها ربع یا نیم پرده زیرتر کردن هر نت را در کسری از ثانیه ممکن کردند",
   "reasoning": "The harp-inspired keyed design and the quarter/half-step lowering in a fraction of a second are both captured."
  },
  {
   "point_id": "K09",
   "point_text": "This makes it possible to move quickly from any dastgah to any other with a few clicks, in just seconds.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L022"
   ],
   "evidence_quote": "جابه‌جایی سریع از هر دستگاهی به هر دستگاه دیگر ممکن شد، فقط با چند کلیک و در چند ثانیه",
   "reasoning": "The payoff is stated with the qualifiers any-to-any, a few clicks, and seconds."
  },
  {
   "point_id": "K10",
   "point_text": "He had been thinking about such an instrument for two years but did not know how to bring it safely from Langroud to Langford.",
   "weight": "Nice to have",
   "presence": "Present",
   "loglog_ids": [
    "L023"
   ],
   "evidence_quote": "دو سالی بود به آن فکر می‌کردم ولی نمی‌دانستم چطور سالم از لنگرود به لنگفورد بیاورمش",
   "reasoning": "The two-year wait and the Langroud-to-Langford migration problem are both present."
  },
  {
   "point_id": "K11",
   "point_text": "With the unstinting help of family, friends, officials, and clerics/community leaders, the instrument finally reached him today.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L024"
   ],
   "evidence_quote": "با کمک‌های بی‌دریغ خانواده و دوستان و مسئولین و ائمه، امروز به دستم رسید",
   "reasoning": "All four helper groups are named and the arrival today is stated."
  },
  {
   "point_id": "K12",
   "point_text": "He tuned it and played, moving from dastgah to dastgah: Isfahan to Segah, Segah to Nava, Nava to Shur, Shur to Homayoun.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L026"
   ],
   "evidence_quote": "از اصفهان به سه‌گاه، از سه‌گاه به نوا، از نوا به شور، از شور به همایون رفتم",
   "reasoning": "The full modulation chain Isfahan-Segah-Nava-Shur-Homayoun is preserved in order."
  },
  {
   "point_id": "K13",
   "point_text": "He felt like a penned fattened sheep set loose, running without pause: he skipped lunch and played so long his back ached.",
   "weight": "Nice to have",
   "presence": "Present",
   "loglog_ids": [
    "L027"
   ],
   "evidence_quote": "حکم گوسفند پرواری رهاشده‌ای را داشتم که بدون وقفه می‌دوید؛ نهار نخوردم و آن‌قدر ساز زدم که پشتم درد گرفت",
   "reasoning": "The sheep simile, running without pause, skipping lunch, and the aching back are all present."
  },
  {
   "point_id": "K14",
   "point_text": "He felt like the first night his aunt put the mizrabs in his hand, like a child allowed to play any game he wants, like a person free to say anything he wishes.",
   "weight": "Nice to have",
   "presence": "Present",
   "loglog_ids": [
    "L028"
   ],
   "evidence_quote": "حس شب اولی را داشتم که خاله‌م مضراب‌ها را داد دستم؛ حس بچه‌ای با هر بازی و کسی با هر حرف",
   "reasoning": "All three comparisons are present, including the callback to the aunt's mizrabs."
  },
  {
   "point_id": "K15",
   "point_text": "He leaves tomorrow on a week of travel and is unhappy at not being home to play, already waiting to return and sit at the instrument.",
   "weight": "Nice to have",
   "presence": "Present",
   "loglog_ids": [
    "L029",
    "L030"
   ],
   "evidence_quote": "از فردا یک هفته‌ای مسافرم؛ ناراحتم که چرا خانه نیستم که ساز بزنم ... نرفته منتظرم برگردم و بنشینم پای ساز",
   "reasoning": "The week of travel, his unhappiness at being away, and the anticipatory longing to return are all captured."
  }
 ],
 "metrics": {
  "total_points": 15,
  "must_have_total": 8,
  "must_have_present": 8,
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
   "severity": "Harmless",
   "evidence_quote": "سنتور یه ساز دیاتونیک هست ... اگه بخوای مدلاسیون انجام بدی باید کوک عوض بشه ... یه سنتوری درست کردن که ... کلید تعبیه کردن",
   "reasoning": "Summary of love for santur, diatonic limitation, and keyed solution matches source narrative."
  },
  {
   "claim_id": "C002",
   "loglog_ids": [
    "1"
   ],
   "claim_text": "شبی در هفت‌سالگی با سنتور خاله و آهنگی که فکر کنم زرد ملیجه بود، عاشق ساز شدم.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "۷ سالم که بود ... شام خونه خاله‌م بودیم ... «زرد ملیجه» بود فکر کنم",
   "reasoning": "Age, aunt's santur, and hedged Zard Malijeh are stated; love is a fair reading of the encounter."
  },
  {
   "claim_id": "C003",
   "loglog_ids": [
    "1.1"
   ],
   "claim_text": "هفت سالم بود؛ سنتور خاله که تازه خریده بود و داشت یاد می‌گرفت کنج اتاق بود و زرد ملیجه زد، فکر کنم.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "۷ سالم که بود ... سنتوری که تازه خریده بود و داشت یاد میگرفت ... تو کنج اتاق بود. یه آهنگ هم برامون زد، «زرد ملیجه» بود فکر کنم.",
   "reasoning": "All details and the hedging match the source span directly."
  },
  {
   "claim_id": "C004",
   "loglog_ids": [
    "1.2"
   ],
   "claim_text": "زرد ملیجه از اولین آهنگ‌هایی بود که در آموزش سنتور یاد می‌دهند؛ با روی گشاده مضراب دست گرفتن را نشانم داد.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "از اولین آهنگهاییه که تو آموزش سنتور یاد میدن ... اونم با روی گشاده ... مضراب دست گرفتن رو بهم نشون داد.",
   "reasoning": "Both the song's early-place status and the open-handed mizrab instruction are stated."
  },
  {
   "claim_id": "C005",
   "loglog_ids": [
    "1.3"
   ],
   "claim_text": "تنها چیز یادم از آن شب این است که آخر شب به زور از پای ساز بلندم کردند.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "تنها چیزی که از اون شب یادم میاد اینه که آخر شب به زور من رو از پای ساز بلند کردن",
   "reasoning": "Near-verbatim match with the source sentence."
  },
  {
   "claim_id": "C006",
   "loglog_ids": [
    "1.4"
   ],
   "claim_text": "احتمالا فقط موقع شام پای ساز نبودم؛ تمام طول راه زر زدم که سنتور می‌خواهم.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "احتمالا فقط موقع شام پای ساز نبودم. تمام طول راه رو زر زدم که سنتور میخوام.",
   "reasoning": "Wording and the hedge احتمالا preserved exactly."
  },
  {
   "claim_id": "C007",
   "loglog_ids": [
    "1.5"
   ],
   "claim_text": "شیش ماه زر زدن و لج‌کردن ادامه داشت تا بالاخره برایم سنتور خریدند.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "شیش ماه که این زر زدن‌ها و لج‌کردن‌ها ادامه داشت بالاخره برام یه سنتور خریدن.",
   "reasoning": "Duration and the plural buyer attribution match the source."
  },
  {
   "claim_id": "C008",
   "loglog_ids": [
    "2"
   ],
   "claim_text": "سنتور را با تخفیف خریدم و یادگیری را با دشواری‌های ساز و مکان شروع کردم.",
   "claim_type": "interpretation",
   "verdict": "Contradicted",
   "severity": "Critical",
   "evidence_quote": "بالاخره برام یه سنتور خریدن. ۲۰هزار تومن، با تخفیف شد ۱۸هزار تومن.",
   "reasoning": "Source says the santur was bought for the author (خریدن), but the node attributes the purchase to the author (خریدم): wrong attribution."
  },
  {
   "claim_id": "C009",
   "loglog_ids": [
    "2.1"
   ],
   "claim_text": "۲۰هزار تومن بود، با تخفیف ۱۸هزار شد؛ شیش ماه بعدتر رفتم کلاس و شروع کردم به یاد گرفتن.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "۲۰هزار تومن، با تخفیف شد ۱۸هزار تومن. شیش ماه بعدتر هم رفتم کلاس و شروع کردم به یاد گرفتن.",
   "reasoning": "Both prices and the six-month gap match the source exactly."
  },
  {
   "claim_id": "C010",
   "loglog_ids": [
    "2.2"
   ],
   "claim_text": "اوایل استاد به خانه می‌آمد چون در شهرمان آموزشگاهی نبود؛ سنتورم در اتاق پذیرایی دربسته و از بقیه سردتر بود، حداقل این‌طور در ذهنم مانده.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "اوایل استادم میومد خونه، چون تو شهرمون آموزشگاهی نبود ... سنتورم تو اتاق پذیرایی بود که همیشه درش بسته بود و سردتر از بقیه اتاقها. حداقل اینطور تو ذهن من مونده.",
   "reasoning": "All clauses and the memory hedge are directly stated."
  },
  {
   "claim_id": "C011",
   "loglog_ids": [
    "2.3"
   ],
   "claim_text": "مبل‌های آن اتاق فقط وقتی مهمان داشتیم استفاده می‌شدند؛ بعدترها اداره ارشاد کلاس دایر کرد و استاد همان‌جا تدریس می‌کرد.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "فقط وقتی مهمون داشتیم استفاده میشدن. بعدترها اداره ارشاد کلاس دایر کرد و استادم همونجا تدریس میکرد",
   "reasoning": "The 'only' restriction and the Ershad class detail match the source."
  },
  {
   "claim_id": "C012",
   "loglog_ids": [
    "2.4"
   ],
   "claim_text": "سازم از خودم گنده‌تر بود و به زور می‌بردمش سر کلاس؛ ۷۲ سیم داشت و کوکش کار هرکسی نبود.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "سازم از خودم گنده‌تر بود و به زور میکشیدمش که ببرمش سر کلاس ... ۷۲ تا سیم داره و کار هرکسی نیست کوک کردنش.",
   "reasoning": "The 72-string count and the 'not everyone's job' negation are preserved."
  },
  {
   "claim_id": "C013",
   "loglog_ids": [
    "3"
   ],
   "claim_text": "محدودیت کوک دیاتونیک، نواختن سنتور را مثل یک بازی محدود می‌کرد.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "این باعث شده بود که همیشه موقع ساز زدن حس بچه‌ای رو داشته باشم که تو مهمونی بهش فقط اجازه یه بازی رو داده باشن.",
   "reasoning": "The restricted-game metaphor is the source's own image for the tuning limitation."
  },
  {
   "claim_id": "C014",
   "loglog_ids": [
    "3.1"
   ],
   "claim_text": "بعدترها تیونر آمد و دیگر لازم نبود ساز را برای کوک به کلاس ببرم؛ اما این محدودیت جنبه‌های دیگر هم داشت.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "بعدترها که تیونر اومد بازار دیگه نیاز نبود ساز رو ببرم سر کلاس ... اما این محدودیت کوک سنتور جنبه‌های دیگه هم داشت.",
   "reasoning": "The tuner arrival, removal of the need, and 'other aspects' clause all match."
  },
  {
   "claim_id": "C015",
   "loglog_ids": [
    "3.2"
   ],
   "claim_text": "سنتور دیاتونیک است: در آن واحد فقط یک دستگاه/گام، و مدولاسیون یعنی عوض کردن کوک که زمانبر است.",
   "claim_type": "definition",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "سنتور یه ساز دیاتونیک هست، ینی در آن واحد فقط میشه یک دستگاه/گام رو روش نواخت و اگه بخوای مدلاسیون انجام بدی باید کوک عوض بشه که خب زمانبره.",
   "reasoning": "Definition and the 'only one' limitation and time-consuming retuning are preserved."
  },
  {
   "claim_id": "C016",
   "loglog_ids": [
    "3.3"
   ],
   "claim_text": "حس بچه‌ای را داشتم که در مهمانی فقط اجازه یک بازی به او داده شده باشد.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "حس بچه‌ای رو داشته باشم که تو مهمونی بهش فقط اجازه یه بازی رو داده باشن.",
   "reasoning": "The simile and its 'only' restriction match the source."
  },
  {
   "claim_id": "C017",
   "loglog_ids": [
    "3.4"
   ],
   "claim_text": "اگر از آن بازی خسته می‌شدم، اول باید همه اسباب‌بازی‌ها را جمع می‌کردم و بعد بازی دیگری در می‌آوردم؛ نمی‌صرفید، حس بازی می‌رفت.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "اگه از اون بازی خسته میشدم ... باید اول همه اسباب‌بازی‌هام رو جمع میکردم و بعد اسباب‌بازی‌های دیگه رو در میاوردم. نمیصرفید، تا اون موقع حس بازی میرفت.",
   "reasoning": "Conditional and consequence match; omission of one clause does not change the meaning."
  },
  {
   "claim_id": "C018",
   "loglog_ids": [
    "3.5"
   ],
   "claim_text": "اگر بچه‌ها از یک بازی به بازی دیگر می‌رفتند، مجبور بودم ساکت گوشه‌ای بنشینم و نگاه کنم، حتی اگر آن بازی را خیلی دوست داشتم.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "وقتی اونا از یه بازی میرفتن به بازی دیگه‌ای، من مجبور بودم ساکت بشینم یه گوشه‌ای و نگاهشون کنم. حتی اگه اون بازی‌ رو خیلی دوست داشتم.",
   "reasoning": "Both the circumstances and the 'even if I liked it' clause are stated."
  },
  {
   "claim_id": "C019",
   "loglog_ids": [
    "4"
   ],
   "claim_text": "راه‌حل کلیددار با ایده چنگ، محدودیت دیاتونیک را برداشت.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "یه سنتوری درست کردن که از چنگ ایده گرفتن و یه سری کلید تعبیه کردن ... این یعنی میشد سریع از هر دستگاهی به هر دستگاه دیگه برم",
   "reasoning": "Harp-inspired keys and removal of the tuning limitation follow from the source."
  },
  {
   "claim_id": "C020",
   "loglog_ids": [
    "4.1"
   ],
   "claim_text": "کلیدها ربع یا نیم پرده زیرتر کردن هر نت را در کسری از ثانیه ممکن کردند.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "یه سری کلید تعبیه کردن که ربع یا نیم پرده زیرتر کردن هر نتی رو در کسری از ثانیه میشه انجام داد.",
   "reasoning": "The quarter/half-tone shift and fraction-of-a-second timing are verbatim."
  },
  {
   "claim_id": "C021",
   "loglog_ids": [
    "4.2"
   ],
   "claim_text": "جابه‌جایی سریع از هر دستگاهی به هر دستگاه دیگر ممکن شد، فقط با چند کلیک و در چند ثانیه.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "میشد سریع از هر دستگاهی به هر دستگاه دیگه برم، فقط با چند کلیک، فقط در چند ثانیه.",
   "reasoning": "The clicks and seconds qualifiers and the 'any dastgah' scope match."
  },
  {
   "claim_id": "C022",
   "loglog_ids": [
    "4.3"
   ],
   "claim_text": "دو سالی بود به آن فکر می‌کردم ولی نمی‌دانستم چطور سالم از لنگرود به لنگفورد بیاورمش.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "دو سالی بود که بهش فکر میکردم ولی نمیدونستم چطور میتونم سالم از لنگرود بیارمش لنگفورد.",
   "reasoning": "Two years, the doubt, and both place names are preserved."
  },
  {
   "claim_id": "C023",
   "loglog_ids": [
    "4.4"
   ],
   "claim_text": "با کمک‌های بی‌دریغ خانواده و دوستان و مسئولین و ائمه، امروز به دستم رسید.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "بالاخره با کمک‌های بی دریغ خانواده و دوستان و مسئولین و ائمه امروز رسید به دستم.",
   "reasoning": "The list of helpers and today's arrival match the source."
  },
  {
   "claim_id": "C024",
   "loglog_ids": [
    "5"
   ],
   "claim_text": "شعف نواختن آزاد و دلتنگی سفر پیش رو.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "هی از این دستگاه رفتم تو اون دستگاه ... ناراحتم که چرا خونه نیستم که ساز بزنم. نرفته منتظرم برگردم",
   "reasoning": "Joy of free playing and sadness about the trip match the source's tone."
  },
  {
   "claim_id": "C025",
   "loglog_ids": [
    "5.1"
   ],
   "claim_text": "از اصفهان به سه‌گاه، از سه‌گاه به نوا، از نوا به شور، از شور به همایون رفتم؛ انگار خواب می‌دیدم.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "از اصفهان به سه‌گاه، از سه‌گاه به نوا، از نوا به شور، از شور به همایون. ... انگار داشتم خواب میدیدم.",
   "reasoning": "The modulation chain and dream simile are verbatim from the source."
  },
  {
   "claim_id": "C026",
   "loglog_ids": [
    "5.2"
   ],
   "claim_text": "حکم گوسفند پرواری رهاشده‌ای را داشتم که بدون وقفه می‌دوید؛ نهار نخوردم و آن‌قدر ساز زدم که پشتم درد گرفت.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "حکم گوسفند پرواری‌ای رو داشتم که بازش کرده بودن و بدون وقفه داشت میدوید، نهار نخوردم، هی ساز زدم، اینقدر که پشتم درد گرفت.",
   "reasoning": "The sheep simile, skipping lunch, and back pain all match."
  },
  {
   "claim_id": "C027",
   "loglog_ids": [
    "5.3"
   ],
   "claim_text": "حس شب اولی را داشتم که خاله‌م مضراب‌ها را داد دستم؛ حس بچه‌ای با هر بازی و کسی با هر حرف.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "حس شب اولی رو داشتم که خاله‌م مضراب‌های سنتور رو داد دستم. حس بچه‌ای ... هر بازی‌ای ... حس کسی ... هر حرفی",
   "reasoning": "First-night feeling, aunt's mizrabs, and the two freedoms are all present."
  },
  {
   "claim_id": "C028",
   "loglog_ids": [
    "5.4"
   ],
   "claim_text": "از فردا یک هفته‌ای مسافرم؛ ناراحتم که چرا خانه نیستم که ساز بزنم.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "حالا از فردا یک هفته‌ای مسافرتم، ناراحتم که چرا خونه نیستم که ساز بزنم.",
   "reasoning": "The one-week trip starting tomorrow and the sadness match verbatim."
  },
  {
   "claim_id": "C029",
   "loglog_ids": [
    "5.5"
   ],
   "claim_text": "نرفته منتظرم برگردم و بنشینم پای ساز.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "نرفته منتظرم برگردم و بشینم پای ساز.",
   "reasoning": "Near-verbatim match with the closing sentence."
  }
 ],
 "metrics": {
  "total_claims": 29,
  "supported": 28,
  "partially_supported": 0,
  "unverifiable": 0,
  "contradicted": 1,
  "critical_errors": 1,
  "faithfulness_precision": 0.9655
 },
 "fail_list": [
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
    "L003",
    "L004",
    "L005",
    "L006"
   ],
   "evidence_quote": "هفت سالم بود؛ سنتور خاله که تازه خریده بود ... با روی گشاده مضراب دست گرفتن را نشانم داد ... آخر شب به زور از پای ساز بلندم کردند",
   "reasoning": "Age (7), the aunt's house, the newly bought santur, the teaching of how to hold the mizrab, and being forcibly lifted from the instrument at night's end are all present. The loglog attributes the purchase to خاله (aunt) rather than the cousin named in the key point, but since the key point itself conflates the aunt/cousin, the origin story is fully preserved."
  },
  {
   "point_id": "K02",
   "point_text": "The first tune he heard on that santur was likely 'Zard Maliheh' (زرد ملیجه), one of the first songs taught to santur beginners.",
   "weight": "Nice to have",
   "presence": "Present",
   "loglog_ids": [
    "L004",
    "L005"
   ],
   "evidence_quote": "زرد ملیجه زد، فکر کنم ... زرد ملیجه از اولین آهنگ‌هایی بود که در آموزش سنتور یاد می‌دهند",
   "reasoning": "Both the tune name and the hedged certainty (فکر کنم) plus its status as a beginner song are captured."
  },
  {
   "point_id": "K03",
   "point_text": "After six months of nagging and sulking, his family finally bought him a santur for 20,000 toman, discounted to 18,000 toman.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L007",
    "L008",
    "L010"
   ],
   "evidence_quote": "شیش ماه زر زدن و لج‌کردن ادامه داشت تا بالاخره برایم سنتور خریدند ... ۲۰هزار تومن بود، با تخفیف ۱۸هزار شد",
   "reasoning": "Six months of nagging/sulking, the purchase, and both numbers (20,000 and discounted 18,000 toman) are intact."
  },
  {
   "point_id": "K04",
   "point_text": "He started lessons six months later; the teacher initially came to his home because their city had no school, and only later did the Ershad office open a class where the teacher taught.",
   "weight": "Nice to have",
   "presence": "Present",
   "loglog_ids": [
    "L010",
    "L011",
    "L012"
   ],
   "evidence_quote": "شیش ماه بعدتر رفتم کلاس ... اوایل استاد به خانه می‌آمد چون در شهرمان آموزشگاهی نبود ... بعدترها اداره ارشاد کلاس دایر کرد",
   "reasoning": "Six-month gap, home lessons due to absence of a school, and the later Ershad office class are all present."
  },
  {
   "point_id": "K05",
   "point_text": "The santur has 72 strings and is hard for an ordinary person to tune, so he had to haul the oversized instrument to class to be tuned, until electronic tuners reached the market and he could tune it himself.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L013",
    "L015"
   ],
   "evidence_quote": "سازم از خودم گنده‌تر بود و به زور می‌بردمش سر کلاس؛ ۷۲ سیم داشت و کوکش کار هرکسی نبود ... بعدترها تیونر آمد و دیگر لازم نبود ساز را برای کوک به کلاس ببرم",
   "reasoning": "The 72-string count, untunability for an ordinary person, hauling the oversized instrument to class, and the arrival of the tuner are all preserved, including the cross-link L033 noting the tuner solved only the transport problem."
  },
  {
   "point_id": "K06",
   "point_text": "The santur is a diatonic instrument: only one dastgah/scale can be played at a time, and modulation requires retuning, which is time-consuming.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L016"
   ],
   "evidence_quote": "سنتور دیاتونیک است: در آن واحد فقط یک دستگاه/گام، و مدولاسیون یعنی عوض کردن کوک که زمانبر است",
   "reasoning": "The central limitation is stated exactly: diatonic, one dastgah at a time, modulation means retuning, and retuning is time-consuming."
  },
  {
   "point_id": "K07",
   "point_text": "This limitation made him feel like a child at a party allowed only one game: to switch he would have to pack up all his toys first, by which time the mood is gone, or else sit silently aside while the other children move to a game he loves.",
   "weight": "Nice to have",
   "presence": "Present",
   "loglog_ids": [
    "L017",
    "L018",
    "L019"
   ],
   "evidence_quote": "حس بچه‌ای را داشتم که در مهمانی فقط اجازه یک بازی به او داده شده باشد ... اول باید همه اسباب‌بازی‌ها را جمع می‌کردم ... مجبور بودم ساکت گوشه‌ای بنشینم",
   "reasoning": "All three beats of the analogy are present: one-game child, packing toys with the mood gone, and sitting silently aside."
  },
  {
   "point_id": "K08",
   "point_text": "Recently a santur was built inspired by the harp, with a set of keys allowing any note to be lowered by a quarter or half step in a fraction of a second.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L020",
    "L021"
   ],
   "evidence_quote": "راه‌حل کلیددار با ایده چنگ ... کلیدها ربع یا نیم پرده زیرتر کردن هر نت را در کسری از ثانیه ممکن کردند",
   "reasoning": "The harp-inspired keyed design and the quarter/half-step lowering in a fraction of a second are both captured."
  },
  {
   "point_id": "K09",
   "point_text": "This makes it possible to move quickly from any dastgah to any other with a few clicks, in just seconds.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L022"
   ],
   "evidence_quote": "جابه‌جایی سریع از هر دستگاهی به هر دستگاه دیگر ممکن شد، فقط با چند کلیک و در چند ثانیه",
   "reasoning": "The payoff is stated with the qualifiers any-to-any, a few clicks, and seconds."
  },
  {
   "point_id": "K10",
   "point_text": "He had been thinking about such an instrument for two years but did not know how to bring it safely from Langroud to Langford.",
   "weight": "Nice to have",
   "presence": "Present",
   "loglog_ids": [
    "L023"
   ],
   "evidence_quote": "دو سالی بود به آن فکر می‌کردم ولی نمی‌دانستم چطور سالم از لنگرود به لنگفورد بیاورمش",
   "reasoning": "The two-year wait and the Langroud-to-Langford migration problem are both present."
  },
  {
   "point_id": "K11",
   "point_text": "With the unstinting help of family, friends, officials, and clerics/community leaders, the instrument finally reached him today.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L024"
   ],
   "evidence_quote": "با کمک‌های بی‌دریغ خانواده و دوستان و مسئولین و ائمه، امروز به دستم رسید",
   "reasoning": "All four helper groups are named and the arrival today is stated."
  },
  {
   "point_id": "K12",
   "point_text": "He tuned it and played, moving from dastgah to dastgah: Isfahan to Segah, Segah to Nava, Nava to Shur, Shur to Homayoun.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L026"
   ],
   "evidence_quote": "از اصفهان به سه‌گاه، از سه‌گاه به نوا، از نوا به شور، از شور به همایون رفتم",
   "reasoning": "The full modulation chain Isfahan-Segah-Nava-Shur-Homayoun is preserved in order."
  },
  {
   "point_id": "K13",
   "point_text": "He felt like a penned fattened sheep set loose, running without pause: he skipped lunch and played so long his back ached.",
   "weight": "Nice to have",
   "presence": "Present",
   "loglog_ids": [
    "L027"
   ],
   "evidence_quote": "حکم گوسفند پرواری رهاشده‌ای را داشتم که بدون وقفه می‌دوید؛ نهار نخوردم و آن‌قدر ساز زدم که پشتم درد گرفت",
   "reasoning": "The sheep simile, running without pause, skipping lunch, and the aching back are all present."
  },
  {
   "point_id": "K14",
   "point_text": "He felt like the first night his aunt put the mizrabs in his hand, like a child allowed to play any game he wants, like a person free to say anything he wishes.",
   "weight": "Nice to have",
   "presence": "Present",
   "loglog_ids": [
    "L028"
   ],
   "evidence_quote": "حس شب اولی را داشتم که خاله‌م مضراب‌ها را داد دستم؛ حس بچه‌ای با هر بازی و کسی با هر حرف",
   "reasoning": "All three comparisons are present, including the callback to the aunt's mizrabs."
  },
  {
   "point_id": "K15",
   "point_text": "He leaves tomorrow on a week of travel and is unhappy at not being home to play, already waiting to return and sit at the instrument.",
   "weight": "Nice to have",
   "presence": "Present",
   "loglog_ids": [
    "L029",
    "L030"
   ],
   "evidence_quote": "از فردا یک هفته‌ای مسافرم؛ ناراحتم که چرا خانه نیستم که ساز بزنم ... نرفته منتظرم برگردم و بنشینم پای ساز",
   "reasoning": "The week of travel, his unhappiness at being away, and the anticipatory longing to return are all captured."
  }
 ],
 "metrics": {
  "total_points": 15,
  "must_have_total": 8,
  "must_have_present": 8,
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
 "source_id": "10_parde_begardan_fa",
 "labels": [
  {
   "claim_id": "C001",
   "loglog_ids": [
    "0"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Top-level thesis of the whole arc; no single branch claim carries the full trajectory."
  },
  {
   "claim_id": "C002",
   "loglog_ids": [
    "1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Section-1 topic sentence; adds the love realization absent from its subpoints."
  },
  {
   "claim_id": "C003",
   "loglog_ids": [
    "1.1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Concrete first-night detail (aunt learning, corner); not repeated elsewhere."
  },
  {
   "claim_id": "C004",
   "loglog_ids": [
    "1.2"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "New explanatory fact that Zard-e-Melije is a standard first teaching piece."
  },
  {
   "claim_id": "C005",
   "loglog_ids": [
    "1.3"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Specific sensory memory (forced off the instrument); distinct from C006."
  },
  {
   "claim_id": "C006",
   "loglog_ids": [
    "1.4"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Narrower memory claim (only away at dinner); adds information beyond C005."
  },
  {
   "claim_id": "C007",
   "loglog_ids": [
    "1.5"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Contains number/date (six months); never trivia per rules."
  },
  {
   "claim_id": "C008",
   "loglog_ids": [
    "2"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Contradicted in Judge F; out of scope for concision credit, kept visible."
  },
  {
   "claim_id": "C009",
   "loglog_ids": [
    "2.1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Contains prices and dates; distinct six-month-after timeline."
  },
  {
   "claim_id": "C010",
   "loglog_ids": [
    "2.2"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "New facts (teacher home visits, cold room); not duplicated elsewhere."
  },
  {
   "claim_id": "C011",
   "loglog_ids": [
    "2.3"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "New facts (guest furniture, Ershad classes); distinct from C010."
  },
  {
   "claim_id": "C012",
   "loglog_ids": [
    "2.4"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Contains number (72 strings); unique instrument detail."
  },
  {
   "claim_id": "C013",
   "loglog_ids": [
    "3"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Section-3 topic sentence; introduces the limited-game framing."
  },
  {
   "claim_id": "C014",
   "loglog_ids": [
    "3.1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Contains qualifier linking tuner to the limitation; never trivia per rules."
  },
  {
   "claim_id": "C015",
   "loglog_ids": [
    "3.2"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Definitional content (diatonic, one dastgah, slow modulation) is unique."
  },
  {
   "claim_id": "C016",
   "loglog_ids": [
    "3.3"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Introduces the party/one-game metaphor; not stated by subpoints."
  },
  {
   "claim_id": "C017",
   "loglog_ids": [
    "3.4"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Distinct scenario (packing up toys); adds detail beyond C016."
  },
  {
   "claim_id": "C018",
   "loglog_ids": [
    "3.5"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Distinct scenario (others switch, I watch quietly); new information."
  },
  {
   "claim_id": "C019",
   "loglog_ids": [
    "4"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Section-4 topic sentence; carries the harp idea absent from subpoints."
  },
  {
   "claim_id": "C020",
   "loglog_ids": [
    "4.1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Mechanism detail (quarter/half-step lowering per note) is specific."
  },
  {
   "claim_id": "C021",
   "loglog_ids": [
    "4.2"
   ],
   "label": "Duplicate",
   "canonical_id": "C020",
   "reasoning": "Rapid key retuning restated; reader learns nothing new beyond C020."
  },
  {
   "claim_id": "C022",
   "loglog_ids": [
    "4.3"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Contains number (two years); never trivia per rules."
  },
  {
   "claim_id": "C023",
   "loglog_ids": [
    "4.4"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Names specific helpers (family, friends, officials, imams); new content."
  },
  {
   "claim_id": "C024",
   "loglog_ids": [
    "5"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Section-5 topic sentence; frames delight plus upcoming-trip longing."
  },
  {
   "claim_id": "C025",
   "loglog_ids": [
    "5.1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Concrete dastgah sequence; adds specifics not present in C020 or C021."
  },
  {
   "claim_id": "C026",
   "loglog_ids": [
    "5.2"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Vivid simile plus physical detail (no lunch, back ache)."
  },
  {
   "claim_id": "C027",
   "loglog_ids": [
    "5.3"
   ],
   "label": "Duplicate",
   "canonical_id": "C002",
   "reasoning": "Recaps the first-night scene (C002/C003) and kid metaphor (C016); adds no information."
  },
  {
   "claim_id": "C028",
   "loglog_ids": [
    "5.4"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "States the upcoming one-week trip; new time-bound fact."
  },
  {
   "claim_id": "C029",
   "loglog_ids": [
    "5.5"
   ],
   "label": "Duplicate",
   "canonical_id": "C028",
   "reasoning": "Same travel-longing as C028; only a rhetorical inversion is added."
  }
 ],
 "metrics": {
  "scored_claims": 29,
  "unique": 26,
  "duplicates": 3,
  "trivia": 0,
  "redundancy_rate": 0.1034,
  "trivia_rate": 0.0,
  "structured_tokens": 768,
  "tokens_per_unique_claim": 30.7
 },
 "prune_list": [
  "C021 duplicates C020, safe to merge",
  "C027 duplicates C002 and echoes C016, safe to drop as recap",
  "C029 duplicates C028, safe to merge"
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
   "severity": "Harmless",
   "evidence_quote": "سنتور یه ساز دیاتونیک هست ... اگه بخوای مدلاسیون انجام بدی باید کوک عوض بشه ... یه سنتوری درست کردن که ... کلید تعبیه کردن",
   "reasoning": "Summary of love for santur, diatonic limitation, and keyed solution matches source narrative."
  },
  {
   "claim_id": "C002",
   "loglog_ids": [
    "1"
   ],
   "claim_text": "شبی در هفت‌سالگی با سنتور خاله و آهنگی که فکر کنم زرد ملیجه بود، عاشق ساز شدم.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "۷ سالم که بود ... شام خونه خاله‌م بودیم ... «زرد ملیجه» بود فکر کنم",
   "reasoning": "Age, aunt's santur, and hedged Zard Malijeh are stated; love is a fair reading of the encounter."
  },
  {
   "claim_id": "C003",
   "loglog_ids": [
    "1.1"
   ],
   "claim_text": "هفت سالم بود؛ سنتور خاله که تازه خریده بود و داشت یاد می‌گرفت کنج اتاق بود و زرد ملیجه زد، فکر کنم.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "۷ سالم که بود ... سنتوری که تازه خریده بود و داشت یاد میگرفت ... تو کنج اتاق بود. یه آهنگ هم برامون زد، «زرد ملیجه» بود فکر کنم.",
   "reasoning": "All details and the hedging match the source span directly."
  },
  {
   "claim_id": "C004",
   "loglog_ids": [
    "1.2"
   ],
   "claim_text": "زرد ملیجه از اولین آهنگ‌هایی بود که در آموزش سنتور یاد می‌دهند؛ با روی گشاده مضراب دست گرفتن را نشانم داد.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "از اولین آهنگهاییه که تو آموزش سنتور یاد میدن ... اونم با روی گشاده ... مضراب دست گرفتن رو بهم نشون داد.",
   "reasoning": "Both the song's early-place status and the open-handed mizrab instruction are stated."
  },
  {
   "claim_id": "C005",
   "loglog_ids": [
    "1.3"
   ],
   "claim_text": "تنها چیز یادم از آن شب این است که آخر شب به زور از پای ساز بلندم کردند.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "تنها چیزی که از اون شب یادم میاد اینه که آخر شب به زور من رو از پای ساز بلند کردن",
   "reasoning": "Near-verbatim match with the source sentence."
  },
  {
   "claim_id": "C006",
   "loglog_ids": [
    "1.4"
   ],
   "claim_text": "احتمالا فقط موقع شام پای ساز نبودم؛ تمام طول راه زر زدم که سنتور می‌خواهم.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "احتمالا فقط موقع شام پای ساز نبودم. تمام طول راه رو زر زدم که سنتور میخوام.",
   "reasoning": "Wording and the hedge احتمالا preserved exactly."
  },
  {
   "claim_id": "C007",
   "loglog_ids": [
    "1.5"
   ],
   "claim_text": "شیش ماه زر زدن و لج‌کردن ادامه داشت تا بالاخره برایم سنتور خریدند.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "شیش ماه که این زر زدن‌ها و لج‌کردن‌ها ادامه داشت بالاخره برام یه سنتور خریدن.",
   "reasoning": "Duration and the plural buyer attribution match the source."
  },
  {
   "claim_id": "C008",
   "loglog_ids": [
    "2"
   ],
   "claim_text": "سنتور را با تخفیف خریدم و یادگیری را با دشواری‌های ساز و مکان شروع کردم.",
   "claim_type": "interpretation",
   "verdict": "Contradicted",
   "severity": "Critical",
   "evidence_quote": "بالاخره برام یه سنتور خریدن. ۲۰هزار تومن، با تخفیف شد ۱۸هزار تومن.",
   "reasoning": "Source says the santur was bought for the author (خریدن), but the node attributes the purchase to the author (خریدم): wrong attribution."
  },
  {
   "claim_id": "C009",
   "loglog_ids": [
    "2.1"
   ],
   "claim_text": "۲۰هزار تومن بود، با تخفیف ۱۸هزار شد؛ شیش ماه بعدتر رفتم کلاس و شروع کردم به یاد گرفتن.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "۲۰هزار تومن، با تخفیف شد ۱۸هزار تومن. شیش ماه بعدتر هم رفتم کلاس و شروع کردم به یاد گرفتن.",
   "reasoning": "Both prices and the six-month gap match the source exactly."
  },
  {
   "claim_id": "C010",
   "loglog_ids": [
    "2.2"
   ],
   "claim_text": "اوایل استاد به خانه می‌آمد چون در شهرمان آموزشگاهی نبود؛ سنتورم در اتاق پذیرایی دربسته و از بقیه سردتر بود، حداقل این‌طور در ذهنم مانده.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "اوایل استادم میومد خونه، چون تو شهرمون آموزشگاهی نبود ... سنتورم تو اتاق پذیرایی بود که همیشه درش بسته بود و سردتر از بقیه اتاقها. حداقل اینطور تو ذهن من مونده.",
   "reasoning": "All clauses and the memory hedge are directly stated."
  },
  {
   "claim_id": "C011",
   "loglog_ids": [
    "2.3"
   ],
   "claim_text": "مبل‌های آن اتاق فقط وقتی مهمان داشتیم استفاده می‌شدند؛ بعدترها اداره ارشاد کلاس دایر کرد و استاد همان‌جا تدریس می‌کرد.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "فقط وقتی مهمون داشتیم استفاده میشدن. بعدترها اداره ارشاد کلاس دایر کرد و استادم همونجا تدریس میکرد",
   "reasoning": "The 'only' restriction and the Ershad class detail match the source."
  },
  {
   "claim_id": "C012",
   "loglog_ids": [
    "2.4"
   ],
   "claim_text": "سازم از خودم گنده‌تر بود و به زور می‌بردمش سر کلاس؛ ۷۲ سیم داشت و کوکش کار هرکسی نبود.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "سازم از خودم گنده‌تر بود و به زور میکشیدمش که ببرمش سر کلاس ... ۷۲ تا سیم داره و کار هرکسی نیست کوک کردنش.",
   "reasoning": "The 72-string count and the 'not everyone's job' negation are preserved."
  },
  {
   "claim_id": "C013",
   "loglog_ids": [
    "3"
   ],
   "claim_text": "محدودیت کوک دیاتونیک، نواختن سنتور را مثل یک بازی محدود می‌کرد.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "این باعث شده بود که همیشه موقع ساز زدن حس بچه‌ای رو داشته باشم که تو مهمونی بهش فقط اجازه یه بازی رو داده باشن.",
   "reasoning": "The restricted-game metaphor is the source's own image for the tuning limitation."
  },
  {
   "claim_id": "C014",
   "loglog_ids": [
    "3.1"
   ],
   "claim_text": "بعدترها تیونر آمد و دیگر لازم نبود ساز را برای کوک به کلاس ببرم؛ اما این محدودیت جنبه‌های دیگر هم داشت.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "بعدترها که تیونر اومد بازار دیگه نیاز نبود ساز رو ببرم سر کلاس ... اما این محدودیت کوک سنتور جنبه‌های دیگه هم داشت.",
   "reasoning": "The tuner arrival, removal of the need, and 'other aspects' clause all match."
  },
  {
   "claim_id": "C015",
   "loglog_ids": [
    "3.2"
   ],
   "claim_text": "سنتور دیاتونیک است: در آن واحد فقط یک دستگاه/گام، و مدولاسیون یعنی عوض کردن کوک که زمانبر است.",
   "claim_type": "definition",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "سنتور یه ساز دیاتونیک هست، ینی در آن واحد فقط میشه یک دستگاه/گام رو روش نواخت و اگه بخوای مدلاسیون انجام بدی باید کوک عوض بشه که خب زمانبره.",
   "reasoning": "Definition and the 'only one' limitation and time-consuming retuning are preserved."
  },
  {
   "claim_id": "C016",
   "loglog_ids": [
    "3.3"
   ],
   "claim_text": "حس بچه‌ای را داشتم که در مهمانی فقط اجازه یک بازی به او داده شده باشد.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "حس بچه‌ای رو داشته باشم که تو مهمونی بهش فقط اجازه یه بازی رو داده باشن.",
   "reasoning": "The simile and its 'only' restriction match the source."
  },
  {
   "claim_id": "C017",
   "loglog_ids": [
    "3.4"
   ],
   "claim_text": "اگر از آن بازی خسته می‌شدم، اول باید همه اسباب‌بازی‌ها را جمع می‌کردم و بعد بازی دیگری در می‌آوردم؛ نمی‌صرفید، حس بازی می‌رفت.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "اگه از اون بازی خسته میشدم ... باید اول همه اسباب‌بازی‌هام رو جمع میکردم و بعد اسباب‌بازی‌های دیگه رو در میاوردم. نمیصرفید، تا اون موقع حس بازی میرفت.",
   "reasoning": "Conditional and consequence match; omission of one clause does not change the meaning."
  },
  {
   "claim_id": "C018",
   "loglog_ids": [
    "3.5"
   ],
   "claim_text": "اگر بچه‌ها از یک بازی به بازی دیگر می‌رفتند، مجبور بودم ساکت گوشه‌ای بنشینم و نگاه کنم، حتی اگر آن بازی را خیلی دوست داشتم.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "وقتی اونا از یه بازی میرفتن به بازی دیگه‌ای، من مجبور بودم ساکت بشینم یه گوشه‌ای و نگاهشون کنم. حتی اگه اون بازی‌ رو خیلی دوست داشتم.",
   "reasoning": "Both the circumstances and the 'even if I liked it' clause are stated."
  },
  {
   "claim_id": "C019",
   "loglog_ids": [
    "4"
   ],
   "claim_text": "راه‌حل کلیددار با ایده چنگ، محدودیت دیاتونیک را برداشت.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "یه سنتوری درست کردن که از چنگ ایده گرفتن و یه سری کلید تعبیه کردن ... این یعنی میشد سریع از هر دستگاهی به هر دستگاه دیگه برم",
   "reasoning": "Harp-inspired keys and removal of the tuning limitation follow from the source."
  },
  {
   "claim_id": "C020",
   "loglog_ids": [
    "4.1"
   ],
   "claim_text": "کلیدها ربع یا نیم پرده زیرتر کردن هر نت را در کسری از ثانیه ممکن کردند.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "یه سری کلید تعبیه کردن که ربع یا نیم پرده زیرتر کردن هر نتی رو در کسری از ثانیه میشه انجام داد.",
   "reasoning": "The quarter/half-tone shift and fraction-of-a-second timing are verbatim."
  },
  {
   "claim_id": "C021",
   "loglog_ids": [
    "4.2"
   ],
   "claim_text": "جابه‌جایی سریع از هر دستگاهی به هر دستگاه دیگر ممکن شد، فقط با چند کلیک و در چند ثانیه.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "میشد سریع از هر دستگاهی به هر دستگاه دیگه برم، فقط با چند کلیک، فقط در چند ثانیه.",
   "reasoning": "The clicks and seconds qualifiers and the 'any dastgah' scope match."
  },
  {
   "claim_id": "C022",
   "loglog_ids": [
    "4.3"
   ],
   "claim_text": "دو سالی بود به آن فکر می‌کردم ولی نمی‌دانستم چطور سالم از لنگرود به لنگفورد بیاورمش.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "دو سالی بود که بهش فکر میکردم ولی نمیدونستم چطور میتونم سالم از لنگرود بیارمش لنگفورد.",
   "reasoning": "Two years, the doubt, and both place names are preserved."
  },
  {
   "claim_id": "C023",
   "loglog_ids": [
    "4.4"
   ],
   "claim_text": "با کمک‌های بی‌دریغ خانواده و دوستان و مسئولین و ائمه، امروز به دستم رسید.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "بالاخره با کمک‌های بی دریغ خانواده و دوستان و مسئولین و ائمه امروز رسید به دستم.",
   "reasoning": "The list of helpers and today's arrival match the source."
  },
  {
   "claim_id": "C024",
   "loglog_ids": [
    "5"
   ],
   "claim_text": "شعف نواختن آزاد و دلتنگی سفر پیش رو.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "هی از این دستگاه رفتم تو اون دستگاه ... ناراحتم که چرا خونه نیستم که ساز بزنم. نرفته منتظرم برگردم",
   "reasoning": "Joy of free playing and sadness about the trip match the source's tone."
  },
  {
   "claim_id": "C025",
   "loglog_ids": [
    "5.1"
   ],
   "claim_text": "از اصفهان به سه‌گاه، از سه‌گاه به نوا، از نوا به شور، از شور به همایون رفتم؛ انگار خواب می‌دیدم.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "از اصفهان به سه‌گاه، از سه‌گاه به نوا، از نوا به شور، از شور به همایون. ... انگار داشتم خواب میدیدم.",
   "reasoning": "The modulation chain and dream simile are verbatim from the source."
  },
  {
   "claim_id": "C026",
   "loglog_ids": [
    "5.2"
   ],
   "claim_text": "حکم گوسفند پرواری رهاشده‌ای را داشتم که بدون وقفه می‌دوید؛ نهار نخوردم و آن‌قدر ساز زدم که پشتم درد گرفت.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "حکم گوسفند پرواری‌ای رو داشتم که بازش کرده بودن و بدون وقفه داشت میدوید، نهار نخوردم، هی ساز زدم، اینقدر که پشتم درد گرفت.",
   "reasoning": "The sheep simile, skipping lunch, and back pain all match."
  },
  {
   "claim_id": "C027",
   "loglog_ids": [
    "5.3"
   ],
   "claim_text": "حس شب اولی را داشتم که خاله‌م مضراب‌ها را داد دستم؛ حس بچه‌ای با هر بازی و کسی با هر حرف.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "حس شب اولی رو داشتم که خاله‌م مضراب‌های سنتور رو داد دستم. حس بچه‌ای ... هر بازی‌ای ... حس کسی ... هر حرفی",
   "reasoning": "First-night feeling, aunt's mizrabs, and the two freedoms are all present."
  },
  {
   "claim_id": "C028",
   "loglog_ids": [
    "5.4"
   ],
   "claim_text": "از فردا یک هفته‌ای مسافرم؛ ناراحتم که چرا خانه نیستم که ساز بزنم.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "حالا از فردا یک هفته‌ای مسافرتم، ناراحتم که چرا خونه نیستم که ساز بزنم.",
   "reasoning": "The one-week trip starting tomorrow and the sadness match verbatim."
  },
  {
   "claim_id": "C029",
   "loglog_ids": [
    "5.5"
   ],
   "claim_text": "نرفته منتظرم برگردم و بنشینم پای ساز.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "نرفته منتظرم برگردم و بشینم پای ساز.",
   "reasoning": "Near-verbatim match with the closing sentence."
  }
 ],
 "metrics": {
  "total_claims": 29,
  "supported": 28,
  "partially_supported": 0,
  "unverifiable": 0,
  "contradicted": 1,
  "critical_errors": 1,
  "faithfulness_precision": 0.9655
 },
 "fail_list": [
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
    "L003",
    "L004",
    "L005",
    "L006"
   ],
   "evidence_quote": "هفت سالم بود؛ سنتور خاله که تازه خریده بود ... با روی گشاده مضراب دست گرفتن را نشانم داد ... آخر شب به زور از پای ساز بلندم کردند",
   "reasoning": "Age (7), the aunt's house, the newly bought santur, the teaching of how to hold the mizrab, and being forcibly lifted from the instrument at night's end are all present. The loglog attributes the purchase to خاله (aunt) rather than the cousin named in the key point, but since the key point itself conflates the aunt/cousin, the origin story is fully preserved."
  },
  {
   "point_id": "K02",
   "point_text": "The first tune he heard on that santur was likely 'Zard Maliheh' (زرد ملیجه), one of the first songs taught to santur beginners.",
   "weight": "Nice to have",
   "presence": "Present",
   "loglog_ids": [
    "L004",
    "L005"
   ],
   "evidence_quote": "زرد ملیجه زد، فکر کنم ... زرد ملیجه از اولین آهنگ‌هایی بود که در آموزش سنتور یاد می‌دهند",
   "reasoning": "Both the tune name and the hedged certainty (فکر کنم) plus its status as a beginner song are captured."
  },
  {
   "point_id": "K03",
   "point_text": "After six months of nagging and sulking, his family finally bought him a santur for 20,000 toman, discounted to 18,000 toman.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L007",
    "L008",
    "L010"
   ],
   "evidence_quote": "شیش ماه زر زدن و لج‌کردن ادامه داشت تا بالاخره برایم سنتور خریدند ... ۲۰هزار تومن بود، با تخفیف ۱۸هزار شد",
   "reasoning": "Six months of nagging/sulking, the purchase, and both numbers (20,000 and discounted 18,000 toman) are intact."
  },
  {
   "point_id": "K04",
   "point_text": "He started lessons six months later; the teacher initially came to his home because their city had no school, and only later did the Ershad office open a class where the teacher taught.",
   "weight": "Nice to have",
   "presence": "Present",
   "loglog_ids": [
    "L010",
    "L011",
    "L012"
   ],
   "evidence_quote": "شیش ماه بعدتر رفتم کلاس ... اوایل استاد به خانه می‌آمد چون در شهرمان آموزشگاهی نبود ... بعدترها اداره ارشاد کلاس دایر کرد",
   "reasoning": "Six-month gap, home lessons due to absence of a school, and the later Ershad office class are all present."
  },
  {
   "point_id": "K05",
   "point_text": "The santur has 72 strings and is hard for an ordinary person to tune, so he had to haul the oversized instrument to class to be tuned, until electronic tuners reached the market and he could tune it himself.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L013",
    "L015"
   ],
   "evidence_quote": "سازم از خودم گنده‌تر بود و به زور می‌بردمش سر کلاس؛ ۷۲ سیم داشت و کوکش کار هرکسی نبود ... بعدترها تیونر آمد و دیگر لازم نبود ساز را برای کوک به کلاس ببرم",
   "reasoning": "The 72-string count, untunability for an ordinary person, hauling the oversized instrument to class, and the arrival of the tuner are all preserved, including the cross-link L033 noting the tuner solved only the transport problem."
  },
  {
   "point_id": "K06",
   "point_text": "The santur is a diatonic instrument: only one dastgah/scale can be played at a time, and modulation requires retuning, which is time-consuming.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L016"
   ],
   "evidence_quote": "سنتور دیاتونیک است: در آن واحد فقط یک دستگاه/گام، و مدولاسیون یعنی عوض کردن کوک که زمانبر است",
   "reasoning": "The central limitation is stated exactly: diatonic, one dastgah at a time, modulation means retuning, and retuning is time-consuming."
  },
  {
   "point_id": "K07",
   "point_text": "This limitation made him feel like a child at a party allowed only one game: to switch he would have to pack up all his toys first, by which time the mood is gone, or else sit silently aside while the other children move to a game he loves.",
   "weight": "Nice to have",
   "presence": "Present",
   "loglog_ids": [
    "L017",
    "L018",
    "L019"
   ],
   "evidence_quote": "حس بچه‌ای را داشتم که در مهمانی فقط اجازه یک بازی به او داده شده باشد ... اول باید همه اسباب‌بازی‌ها را جمع می‌کردم ... مجبور بودم ساکت گوشه‌ای بنشینم",
   "reasoning": "All three beats of the analogy are present: one-game child, packing toys with the mood gone, and sitting silently aside."
  },
  {
   "point_id": "K08",
   "point_text": "Recently a santur was built inspired by the harp, with a set of keys allowing any note to be lowered by a quarter or half step in a fraction of a second.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L020",
    "L021"
   ],
   "evidence_quote": "راه‌حل کلیددار با ایده چنگ ... کلیدها ربع یا نیم پرده زیرتر کردن هر نت را در کسری از ثانیه ممکن کردند",
   "reasoning": "The harp-inspired keyed design and the quarter/half-step lowering in a fraction of a second are both captured."
  },
  {
   "point_id": "K09",
   "point_text": "This makes it possible to move quickly from any dastgah to any other with a few clicks, in just seconds.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L022"
   ],
   "evidence_quote": "جابه‌جایی سریع از هر دستگاهی به هر دستگاه دیگر ممکن شد، فقط با چند کلیک و در چند ثانیه",
   "reasoning": "The payoff is stated with the qualifiers any-to-any, a few clicks, and seconds."
  },
  {
   "point_id": "K10",
   "point_text": "He had been thinking about such an instrument for two years but did not know how to bring it safely from Langroud to Langford.",
   "weight": "Nice to have",
   "presence": "Present",
   "loglog_ids": [
    "L023"
   ],
   "evidence_quote": "دو سالی بود به آن فکر می‌کردم ولی نمی‌دانستم چطور سالم از لنگرود به لنگفورد بیاورمش",
   "reasoning": "The two-year wait and the Langroud-to-Langford migration problem are both present."
  },
  {
   "point_id": "K11",
   "point_text": "With the unstinting help of family, friends, officials, and clerics/community leaders, the instrument finally reached him today.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L024"
   ],
   "evidence_quote": "با کمک‌های بی‌دریغ خانواده و دوستان و مسئولین و ائمه، امروز به دستم رسید",
   "reasoning": "All four helper groups are named and the arrival today is stated."
  },
  {
   "point_id": "K12",
   "point_text": "He tuned it and played, moving from dastgah to dastgah: Isfahan to Segah, Segah to Nava, Nava to Shur, Shur to Homayoun.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L026"
   ],
   "evidence_quote": "از اصفهان به سه‌گاه، از سه‌گاه به نوا، از نوا به شور، از شور به همایون رفتم",
   "reasoning": "The full modulation chain Isfahan-Segah-Nava-Shur-Homayoun is preserved in order."
  },
  {
   "point_id": "K13",
   "point_text": "He felt like a penned fattened sheep set loose, running without pause: he skipped lunch and played so long his back ached.",
   "weight": "Nice to have",
   "presence": "Present",
   "loglog_ids": [
    "L027"
   ],
   "evidence_quote": "حکم گوسفند پرواری رهاشده‌ای را داشتم که بدون وقفه می‌دوید؛ نهار نخوردم و آن‌قدر ساز زدم که پشتم درد گرفت",
   "reasoning": "The sheep simile, running without pause, skipping lunch, and the aching back are all present."
  },
  {
   "point_id": "K14",
   "point_text": "He felt like the first night his aunt put the mizrabs in his hand, like a child allowed to play any game he wants, like a person free to say anything he wishes.",
   "weight": "Nice to have",
   "presence": "Present",
   "loglog_ids": [
    "L028"
   ],
   "evidence_quote": "حس شب اولی را داشتم که خاله‌م مضراب‌ها را داد دستم؛ حس بچه‌ای با هر بازی و کسی با هر حرف",
   "reasoning": "All three comparisons are present, including the callback to the aunt's mizrabs."
  },
  {
   "point_id": "K15",
   "point_text": "He leaves tomorrow on a week of travel and is unhappy at not being home to play, already waiting to return and sit at the instrument.",
   "weight": "Nice to have",
   "presence": "Present",
   "loglog_ids": [
    "L029",
    "L030"
   ],
   "evidence_quote": "از فردا یک هفته‌ای مسافرم؛ ناراحتم که چرا خانه نیستم که ساز بزنم ... نرفته منتظرم برگردم و بنشینم پای ساز",
   "reasoning": "The week of travel, his unhappiness at being away, and the anticipatory longing to return are all captured."
  }
 ],
 "metrics": {
  "total_points": 15,
  "must_have_total": 8,
  "must_have_present": 8,
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
 "source_id": "10_parde_begardan_fa",
 "labels": [
  {
   "claim_id": "C001",
   "loglog_ids": [
    "0"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Top-level thesis of the whole arc; no single branch claim carries the full trajectory."
  },
  {
   "claim_id": "C002",
   "loglog_ids": [
    "1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Section-1 topic sentence; adds the love realization absent from its subpoints."
  },
  {
   "claim_id": "C003",
   "loglog_ids": [
    "1.1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Concrete first-night detail (aunt learning, corner); not repeated elsewhere."
  },
  {
   "claim_id": "C004",
   "loglog_ids": [
    "1.2"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "New explanatory fact that Zard-e-Melije is a standard first teaching piece."
  },
  {
   "claim_id": "C005",
   "loglog_ids": [
    "1.3"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Specific sensory memory (forced off the instrument); distinct from C006."
  },
  {
   "claim_id": "C006",
   "loglog_ids": [
    "1.4"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Narrower memory claim (only away at dinner); adds information beyond C005."
  },
  {
   "claim_id": "C007",
   "loglog_ids": [
    "1.5"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Contains number/date (six months); never trivia per rules."
  },
  {
   "claim_id": "C008",
   "loglog_ids": [
    "2"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Contradicted in Judge F; out of scope for concision credit, kept visible."
  },
  {
   "claim_id": "C009",
   "loglog_ids": [
    "2.1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Contains prices and dates; distinct six-month-after timeline."
  },
  {
   "claim_id": "C010",
   "loglog_ids": [
    "2.2"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "New facts (teacher home visits, cold room); not duplicated elsewhere."
  },
  {
   "claim_id": "C011",
   "loglog_ids": [
    "2.3"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "New facts (guest furniture, Ershad classes); distinct from C010."
  },
  {
   "claim_id": "C012",
   "loglog_ids": [
    "2.4"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Contains number (72 strings); unique instrument detail."
  },
  {
   "claim_id": "C013",
   "loglog_ids": [
    "3"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Section-3 topic sentence; introduces the limited-game framing."
  },
  {
   "claim_id": "C014",
   "loglog_ids": [
    "3.1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Contains qualifier linking tuner to the limitation; never trivia per rules."
  },
  {
   "claim_id": "C015",
   "loglog_ids": [
    "3.2"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Definitional content (diatonic, one dastgah, slow modulation) is unique."
  },
  {
   "claim_id": "C016",
   "loglog_ids": [
    "3.3"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Introduces the party/one-game metaphor; not stated by subpoints."
  },
  {
   "claim_id": "C017",
   "loglog_ids": [
    "3.4"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Distinct scenario (packing up toys); adds detail beyond C016."
  },
  {
   "claim_id": "C018",
   "loglog_ids": [
    "3.5"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Distinct scenario (others switch, I watch quietly); new information."
  },
  {
   "claim_id": "C019",
   "loglog_ids": [
    "4"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Section-4 topic sentence; carries the harp idea absent from subpoints."
  },
  {
   "claim_id": "C020",
   "loglog_ids": [
    "4.1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Mechanism detail (quarter/half-step lowering per note) is specific."
  },
  {
   "claim_id": "C021",
   "loglog_ids": [
    "4.2"
   ],
   "label": "Duplicate",
   "canonical_id": "C020",
   "reasoning": "Rapid key retuning restated; reader learns nothing new beyond C020."
  },
  {
   "claim_id": "C022",
   "loglog_ids": [
    "4.3"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Contains number (two years); never trivia per rules."
  },
  {
   "claim_id": "C023",
   "loglog_ids": [
    "4.4"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Names specific helpers (family, friends, officials, imams); new content."
  },
  {
   "claim_id": "C024",
   "loglog_ids": [
    "5"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Section-5 topic sentence; frames delight plus upcoming-trip longing."
  },
  {
   "claim_id": "C025",
   "loglog_ids": [
    "5.1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Concrete dastgah sequence; adds specifics not present in C020 or C021."
  },
  {
   "claim_id": "C026",
   "loglog_ids": [
    "5.2"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Vivid simile plus physical detail (no lunch, back ache)."
  },
  {
   "claim_id": "C027",
   "loglog_ids": [
    "5.3"
   ],
   "label": "Duplicate",
   "canonical_id": "C002",
   "reasoning": "Recaps the first-night scene (C002/C003) and kid metaphor (C016); adds no information."
  },
  {
   "claim_id": "C028",
   "loglog_ids": [
    "5.4"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "States the upcoming one-week trip; new time-bound fact."
  },
  {
   "claim_id": "C029",
   "loglog_ids": [
    "5.5"
   ],
   "label": "Duplicate",
   "canonical_id": "C028",
   "reasoning": "Same travel-longing as C028; only a rhetorical inversion is added."
  }
 ],
 "metrics": {
  "scored_claims": 29,
  "unique": 26,
  "duplicates": 3,
  "trivia": 0,
  "redundancy_rate": 0.1034,
  "trivia_rate": 0.0,
  "structured_tokens": 768,
  "tokens_per_unique_claim": 30.7
 },
 "prune_list": [
  "C021 duplicates C020, safe to merge",
  "C027 duplicates C002 and echoes C016, safe to drop as recap",
  "C029 duplicates C028, safe to merge"
 ]
}
```

## Judge Top (overall), opencode-go/deepseek-v4.1-flash

```json
{
 "judge": "overall",
 "judge_version": "1.0.0",
 "model": "deepseek-v4.1-flash (2026-09-15)",
 "source_id": "point-hierarchy run: 15 points / 29 claims",
 "inputs": {
  "faithfulness_precision": 0.9655,
  "critical_errors": 1,
  "must_recall": 1.0,
  "overall_recall": 1.0,
  "redundancy_rate": 0.1034,
  "trivia_rate": 0.0
 },
 "weights_used": {
  "faithfulness_precision": 0.4,
  "coverage_must_recall": 0.4,
  "redundancy_penalty": 0.2
 },
 "computation": "Hard gates first: critical_contradicted_max=0, but critical_errors=1 (C008) -> FAIL. (For audit, gate checks: faithfulness_precision 0.9655 >= 0.95 PASS; must_recall 1.0 >= 0.9 PASS; redundancy 0.1034 <= 0.15 PASS.) Weighted score (computed but non-decisive since a hard gate failed): 0.4*0.9655 + 0.4*1.0 - 0.2*0.1034 = 0.3862 + 0.4 - 0.02068 = 0.76552",
 "weighted_score": 0.76552,
 "verdict": "Fail",
 "tradeoff_note": "Coverage is perfect (must_recall 1.0) and redundancy is within budget, but none of that rescues the sample: the single Critical contradicted claim C008 flips the santur purchase into a first-person action, which fails the critical_contradicted_max gate.",
 "fix_list": [
  "Fix C008 (loglog id 2): change 'سنتور را با تخفیف خریدم' to reflect that the santur was bought for the author (برام یه سنتور خریدن), not by the author, since wrong attribution contradicts the source quote 'بالاخره برام یه سنتور خریدن. ۲۰هزار تومن، با تخفیف شد ۱۸هزار تومن.'",
  "Remove C021 (merge into C020), C027 (recap echoing C002/C016), and C029 (merge into C028) to drop redundancy_rate from 0.1034 toward ~0 without any coverage loss."
 ],
 "reasoning": "Gate evaluation in policy order. (1) Hard fail on critical errors: Judge F reports critical_errors=1, driven solely by C008, a Contradicted/Critical interpretation claim tied to loglog id 2. The source states the santur was bought for the author ('برام یه سنتور خریدن'), while the claim renders it as the author's own purchase ('خریدم'). Policy sets critical_contradicted_max=0, so any Critical contradicted claim fails the sample regardless of other metrics. (2) Must-have recall gate: 8/8 must-have points present, must_have_partial=0, must_have_missing=0, must_recall=1.0 >= 0.9 -> PASS. (3) Faithfulness precision gate: 28 supported of 29 total, faithfulness_precision=0.9655 >= 0.95 -> PASS numerically, though the one miss is the Critical C008, which is why the numeric pass does not save the sample. (4) Redundancy gate: 3 duplicates of 29 scored claims, redundancy_rate=0.1034 <= 0.15 -> PASS; trivia_rate=0.0. (5) Tradeoff among passes is moot because the hard gate failed, but for audit the weighted score is 0.4*0.9655 + 0.4*1.0 - 0.2*0.1034 = 0.3862 + 0.4 - 0.02068 = 0.76552. Coverage is maximal and concision is inside budget, so there is no coverage-vs-length tension to resolve; the verdict is decided entirely by the C008 attribution error. Verdict: Fail. Highest-leverage fix is repairing C008's attribution at loglog id 2, followed by pruning the three flagged duplicates for a clean concision pass on the next run."
}
```
