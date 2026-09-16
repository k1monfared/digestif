---
tags: simulation, statistics, philosophy, observation, python
---
# Manufacturing Taste

I asked Hadi, half-jokingly, whether Bach was the Justin Bieber of his time. Are we just listening to the most "popular" artists of the 1700s and calling it high culture? And the flip side: will people 300 years from now be listening to Bieber and think that was the best we had to offer? He strongly disagreed, but the question stuck with me.

Because here's the thing: in 18th-century Vienna alone, there were somewhere between 200 and 500 active composers at any given time. Across all of Europe during the Classical era, [IMSLP catalogs over 3,400 composers](https://imslp.org/wiki/Category:People_from_the_Classical_era) whose work survived in some form, and many more left no trace at all. [Wikipedia's curated list](https://en.wikipedia.org/wiki/List_of_Classical-era_composers) names several hundred. We remember fewer than 20. The standard explanation says we remember the best ones. But were they the best? Or were they the ones who happened to have the right patron, the right court position, the right access to orchestras and publishers?

We can't rewind history and run it again with different initial conditions. If the Esterházy family had hired a different Kapellmeister instead of Haydn, would we still know Haydn's name? We literally cannot answer that question empirically. But we can build a model of how cultural markets work and run *that* thousands of times.

So that's what I did. I built a [simulation](https://github.com/k1monfared/manufacturing_taste) to find out. The full technical paper is [here](https://github.com/k1monfared/manufacturing_taste/blob/master/paper/paper.pdf). This post is the less formal version.

## Three Stories About How Canons Form

I set up the project to test three competing hypotheses. Each tells a different story.

**Story 1: The Cream Rises.** The works we remember are the best works. Period. Money might help someone get a head start, but over long enough time horizons, genuine quality wins. If you replayed history with different patrons, you'd end up with roughly the same canon.

**Story 2: Money Writes History.** Success is mostly about who gets heard first. A composer with a wealthy patron gets performed; audiences grow to like what they hear (a real psychological phenomenon, more on this below); that familiarity gets retroactively interpreted as quality; and institutions lock it in for future generations. Quality is almost irrelevant.

**Story 3: Floors and Ceilings.** Both are partly right. The truly terrible never succeed no matter how much money backs them. The truly transcendent sometimes break through despite everything. But for the vast majority in the middle, the "very good but not obviously once-in-a-generation" group, whether they become famous or forgotten depends on luck, money, and timing, not on the difference between their talent and their peers'.

Think of it like a job market. The very best candidate and the very worst are easy to rank. But among the twenty "pretty good" candidates, who gets hired often comes down to who knew someone, who happened to interview on a good day, or whose resume landed on top of the pile. The classical music canon is the same problem at civilizational scale.

## The Mechanisms

The model incorporates three phenomena that are individually well-documented in psychology and economics, but whose *combined* effect on cultural canons hasn't been quantified.

**The Mere Exposure Effect.** We tend to like things we've encountered before. A song that plays on the radio ten times starts to feel "catchy" even if it didn't grab you the first time. This isn't about learning to appreciate complexity. It happens with nonsense syllables, abstract shapes, faces of strangers. Zajonc demonstrated this in 1968, and Bornstein's 1989 meta-analysis across 208 experiments confirmed it with an average effect size of r = 0.26. The effect peaks at moderate exposure and reverses with overexposure (hence "I'm sick of that song").

What this means for canons: artists who get more initial airtime develop an artificial quality advantage. Audiences genuinely perceive their work as better, not because they're deluded, but because familiarity really does affect aesthetic experience. The problem isn't that people are bad judges. It's that the judging is contaminated by the exposure, and the exposure was determined by money.

**Social Influence.** We look at what others consume and use it as a shortcut for what's good. Bestseller lists, download counts, "trending" labels, view counts: all social signals that nudge us toward what's already popular. This creates snowball effects. The [Salganik MusicLab experiment](https://doi.org/10.1126/science.1121066) (2006) demonstrated this beautifully: they created an online music market where 14,341 participants could listen to 48 unknown songs. Some participants saw download counts; others didn't. Result: the same song could rank 1st in one version of the world and 40th in another, purely because of random early differences in who happened to download it first.

**Cumulative Advantage.** The rich get richer. An artist whose first album sells well gets a bigger marketing budget, better tour slots, more press, more prominent playlist placement, all of which make the second album more likely to succeed regardless of whether it's better. The sociologist Robert Merton called this the Matthew Effect. Small initial differences, which may be due to luck or timing or money, get magnified into enormous gaps over time. A composer who secures a court position at age 20 accumulates decades of performances, publications, and reputation that a composer who missed that appointment by one year never gets to build.

Each of these alone is well-understood. What I wanted to know is: when you put all three together in a system and let them interact over many generations, what happens?

## What The Simulation Does

The model has three types of agents: producers (composers/artists), consumers (audiences), and gatekeepers (critics, curators, playlist editors). Each producer gets a quality score drawn randomly (how good their work actually is) and a capital score drawn independently (how much money and access they start with). Quality and capital are uncorrelated. Being wealthy doesn't make you talented.

Then the simulation runs. Producers with more capital get more exposure. Consumers form opinions based on actual quality plus the mere exposure effect plus social signals. Success feeds back into more exposure (cumulative advantage). After many rounds, some producers achieve "canonical" status. They're the ones we remember.

I ran this thousands of times under different conditions. Each run takes about two minutes with 1,000 producers and 10,000 consumers, so I parallelized it across CPU cores and ran 360+ per condition for the main experiments, with formal power analysis to make sure the sample sizes were sufficient.

## What Happened

### Does social influence weaken the quality-success link?

Yes. When simulated listeners can see what others are consuming, the correlation between actual quality and commercial success drops significantly (p < 0.0001 across 360 runs per condition). In a world where nobody could see what anyone else was listening to, quality would be a moderately good predictor of success. But in a world with charts, recommendations, and "trending" labels (our world), the link gets weaker. A mediocre work that gets lucky early can ride social proof to stardom, while an equally good work that starts slow may never recover.

This is, incidentally, why I distrust recommendation algorithms so much. Every "Top 40" chart, every "Customers Also Bought" widget, every view count is a form of social influence that systematically pushes us away from independent judgment. It's the measurement trap I wrote about [before](https://k1monfared.com/notes/blog/20251023-from-measurement-to-intention/). We use popularity as a proxy for quality, then optimize for the proxy, then forget it was a proxy.

### If we replayed history, would we get the same canon?

This is the experiment that surprised me most. I held talent constant. Every simulated composer kept the exact same quality score. I only reshuffled their resources: who had wealthy patrons and who didn't. Then I ran it 200 times.

The counterfactual distance was 0.88 on a 0-to-1 scale, where 0 means "identical canon every time" and 1 means "completely different canons every time." Almost entirely different canons from just reshuffling money.

Only the top 10% of talent had a meaningful shot at fame regardless of funding, and even then it was only about 1 in 4. For everyone in the 50th to 90th percentile of quality, the solidly good but not unmistakably transcendent, canonical status was effectively a lottery.

This is the simulation equivalent of the Haydn question. If the Esterházys had hired someone else, Haydn would very likely be one of the hundreds of forgotten 18th-century composers you've never heard of. Not because he wasn't excellent, but because excellence alone isn't enough when the exposure pipeline is this narrow.

### What matters more: unequal money or herd behavior?

I ran the simulation under four conditions, removing one factor at a time:

1. **Full model** (everything active): quality-canon correlation = 0.32
2. **No social influence** (people judge independently): 0.35
3. **Equal capital** (everyone starts with the same resources): 0.46
4. **Quality only** (no social influence, no capital inequality): 0.46

Turning off social influence barely helps. But equalizing starting resources jumps the quality-canon correlation by 44%. The biggest distortion isn't that audiences follow trends. It's that some artists never get heard in the first place.

This maps directly to the modern world. The problem isn't that people blindly follow Spotify playlists. It's that only major-label artists get on those playlists to begin with. Capital gates access to the exposure pipeline, and everything downstream of that is noise amplification.

### What about 18th-century Vienna specifically?

I built a stylized version: 300 composers, a handful of very wealthy patrons, strong word-of-mouth, no recording technology. The counterfactual distance was 0.97, near maximum. Only 2.5% of canonical composers were shared between any two alternate histories.

To say that plainly: if you could rewind to 1750 and randomly reassign which composers got which court positions, the names we teach in music history would be almost entirely different. The winners in our timeline were very likely excellent. You had to be good to compete for a court position. But dozens of equally excellent composers were lost to history because they drew the short straw in the patronage lottery.

That's what "manufacturing taste" means. Not that the winners were bad. That the losers weren't meaningfully worse.

### How robust is this?

I varied every parameter by ±50%. The single most important factor is how steeply money converts into attention. If doubling your marketing budget more than doubles your audience (a convex relationship), the rich get richer very fast and quality barely matters. If doubling your budget less than doubles your audience, quality has more room to breathe.

This isn't just a modeling knob. It corresponds to a real structural question about the industry. When a major label can buy a front-page Spotify placement reaching 50 million listeners while an independent artist's self-promotion reaches 500, the capital-to-exposure curve is extremely steep. Our model predicts that under those conditions, quality has very little to do with who becomes famous.

## What This Means

Story 3 wins. Quality acts as a loose filter. It sets a floor below which you can't succeed and a ceiling above which you probably will. But the vast middle ground, where most artists live, is dominated by capital and luck.

There are a few implications worth spelling out.

**When someone says "Bach is the greatest composer who ever lived,"** a more precise statement would be: "Bach is the greatest composer who ever lived among those who had the resources to be heard, published, and preserved." There may have been equally gifted composers whose music was never performed, never published, and never survived. We don't know. We can't know. But the simulation says it's very likely.

**The mechanisms are stronger today, not weaker.** The feedback loops we model (exposure bias, social influence, cumulative advantage) operate faster in the age of algorithmic recommendations. An 18th-century patronage decision played out over decades. A Spotify playlist placement plays out in hours. The scale of winner-take-all dynamics is vastly larger than anything in the historical record.

**The highest-leverage intervention isn't better judgment, it's wider exposure.** Our model says audiences are already decent judges of quality within the limits of what they're exposed to. The bottleneck is the exposure itself. Blind auditions for orchestras, widely adopted in the 1970s-80s, are the proof of concept: when the screen went up, the proportion of women hired by major US orchestras went from 5% to 25%. The talent was always there. The barrier was exposure.

This connects to something I keep coming back to in these posts: the gap between the metric and the thing we actually care about. We use "survived into the canon" as a proxy for "was the best," then build entire curricula and cultural narratives on that proxy, forgetting it was ever a proxy at all. The simulation doesn't tell us what the canon *should* look like. It just tells us that the one we got is far more contingent than we assume.

## The Caveats

I want to be honest about what this can and can't tell us.

The model assumes quality is a real, stable property that exists independently of who hears it. That's philosophically debatable. If "quality" is partly constituted by social processes, if great art is partly art that has been widely shared and discussed, then the whole decomposition may be ill-posed. I don't have a satisfying answer to this. I just think it's worth noting.

The calibration data comes from the Salganik MusicLab experiment, which studied American teenagers evaluating pop songs over weeks. Generalizing to 18th-century European aristocrats evaluating orchestral music over decades requires a leap of faith. The mechanisms (mere exposure, social influence, cumulative advantage) are well-documented across many contexts, but the specific parameter values are uncertain.

There are important things the model doesn't include: genre formation, critical discourse, technological change, cultural politics. Any model is a simplification. The question is whether it's a useful simplification, and I think it is. The direction of the effects is robust across a wide range of parameter values, even if the precise magnitudes are uncertain.

## So, Was Bach the Justin Bieber of His Time?

After all of this, I have an answer to the question I asked Hadi. Not exactly, but closer than I expected.

The Bieber analogy gets the mechanism right but the quality floor wrong. The pop music pipeline can take someone who is good enough (can carry a tune, looks good on camera, millions meet that bar) and manufacture a global phenomenon through marketing and algorithmic promotion. Bach's world was different: to hold a court position you had to write music that worked for liturgical services, entertain aristocrats, train choirs, improvise fugues on demand. The quality floor was genuinely high.

So Bach wasn't just popular. He was excellent AND well-positioned. But the simulation tells us the "AND" is doing most of the work, and the second half matters more than the first. Reshuffle patronage and you get an almost entirely different canon. Only 2.5% overlap between alternate histories.

I think Bach was less like Justin Bieber and more like the one surgeon who gets famous out of fifty equally skilled surgeons at major hospitals. All fifty are excellent. All fifty could do the job. But one happened to get a profile in the New York Times, which led to speaking invitations, which led to a book deal, which led to a reputation as "the best surgeon in the country." The other 49 are just as good. You've never heard of them.

The question was never whether Bach was great. He almost certainly was. The question is whether we're listening to him because he was the *greatest*, or because he was great AND he landed the right church job in Leipzig. The simulation says it's the second. And it says there were probably 20 to 50 of his contemporaries who were equally great, whose names we will never know, because they didn't get that job.

That's what sits with me. Not that the canon is wrong. But that it's one canon out of hundreds of equally valid ones we could have ended up with, and we treat it as if it were inevitable.

And there's a deeper question here that I haven't been able to shake. We think of Bach's music as what "great music" sounds like. His harmonic language, his structures, his aesthetic sensibility: these are the foundations of how we hear and judge music today. But if someone else had gotten the Leipzig job, if a different set of composers had survived into the canon, we would have inherited a different set of foundations. We would hear differently. We would judge differently. What we call "good taste" would be a different taste entirely.

That's the real meaning of the title. It's not just that the canon was manufactured. It's that our taste was manufactured along with it. We like what we were taught to like, and we were taught to like the survivors, and the survivors were selected by money and luck as much as by merit. The whole chain from "who got funded" to "what counts as beautiful" is more contingent than it feels from the inside.

As for the other half of the question, whether people 300 years from now will be listening to Bieber and calling it the peak of our era, I honestly don't know. But if the mechanisms in this simulation are right, then whoever survives into the canon of the 2000s will have more to do with who had the best distribution deals and the most favorable algorithms than with who made the best music. And we won't be around to correct them.
