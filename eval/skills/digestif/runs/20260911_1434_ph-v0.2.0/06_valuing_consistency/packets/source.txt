---
tags: philosophy, observation, personal-finance, immigration
title: What Do We Value When We Value Consistency?
---

I'm often interested in understanding why people believe the things they believe and why they behave the way they behave. Usually the former is a reason for the latter. Pondering these, I've realized there is a word I keep reaching for when describing people's behavior that is vaguer than I'd like, and it doesn't let me build any structure around it. Worse, I attach a moral value to it: sometimes it's a compliment, sometimes an accusation. So I want to pin down what this concept actually means: consistency.

The story that made me notice the problem is one my mom tells. Before the 1979 revolution in Iran, someone she knew wore mini skirts all the time. Right after the revolution she switched to chador and niqab. Others in the same circle dressed modestly before the revolution and dressed modestly after it, changing only slightly how much they covered.

My instinct reads the first woman's swing as a moral failing and the others' steadiness as integrity. But that's not the only reading on offer. A more cynical observer might call the first woman cunning, quick to adapt to the new situation, and call the others slow to catch up. And even those of us who'd judge her harshly tend to agree that being able to "update" your beliefs on certain topics is a virtue, that nobody should be stoneheaded. So the swing itself can't be what we're judging. Consistency, in the plain sense of "did the behavior stay the same", is not carrying the moral weight I assumed it did. Something underneath it is. This post is my attempt to find that something.

## A small model

To think clearly I need something concrete to push against, so let's put numbers on the clothing story. Measure clothing openness on a scale from $-1$ (fully closed) to $1$ (fully open). Say society's average sits at $-0.5$ in the closed state and $0.5$ in the open state. Start with one of the modest women from the story: say we observe her at $-0.1$ in the closed state and $0.1$ in the open state. A slight change, but not zero.

Hypothesis: her behavior is a blend of her own fixed point and the social reference,

$$\text{Behavior} = w \times \text{Reference} + (1 - w) \times \text{Anchor}$$

where the Anchor is what she'd do if the reference had no pull on her, and $w$, the Responsiveness, is how much weight the reference actually carries. Two observations give two equations:

$$-0.5w + (1-w)a = -0.1$$
$$0.5w + (1-w)a = 0.1$$

Adding them gives $2(1-w)a = 0$, so the anchor is $a = 0$. Subtracting gives $w = 0.2$. Her behavior is exactly $0.2 \times \text{Reference}$, both times. She has a fixed anchor at neutral and yields a fixed twenty percent of the distance toward whatever society is doing.

This is the first place the vague word cracks open. Her *output* moved: $-0.1$ then $0.1$, no fixed value. Her *rule* never did: same anchor, same responsiveness, both times. An unusually stable person, conceding a fixed fraction of ground under pressure.

Now the other woman from the story, the one who wore mini skirts before the revolution and chador after. In numbers she is at $0.9$ when society is $0.5$, and at $-0.9$ when society is $-0.5$. Same solving:

$$0.5w + (1-w)a = 0.9$$
$$-0.5w + (1-w)a = -0.9$$

The anchor comes out to $0$ again, and $w$ comes out to $1.8$. She doesn't just follow the reference, she amplifies it: more open than the open society, more closed than the closed society. And here is the uncomfortable part. Her rule is exactly as consistent as the modest woman's. One anchor, one responsiveness, both times. Someone judging only her output would call her a fashion-following chameleon, and the output judgment is fair. But the inference that comes with it, that she has no fixed point, that she stands for nothing, is wrong. The difference between the two women is not that one has a stable rule and the other doesn't. Both do. The difference is what the rule says: concede a fifth of the distance to society, or overshoot it by eighty percent.

Step back and notice that "consistency" has now been asked of three different things, and it can pass or fail on each one independently. Consistency of **output**: did the behavior stay the same. Consistency of **policy**: did the rule stay the same, same anchor, same responsiveness. Consistency of **anchor**: did the fixed point itself stay fixed. The two women fail the first in opposite amounts, one barely, one spectacularly, and pass the second and third completely. An observer watching only output would see a consistency gap between them that doesn't exist at either deeper layer.

The third layer is where the real action is. Policy can stay fixed while the anchor drifts underneath it, invisibly, in steps small enough that no single moment feels like a change of mind. That drift is where the moral weight lives, and it's what the rest of this post is about.

## The contrarian next door

Now picture a third woman in the same two societies. She is observed at $0.2$ when the average is $-0.5$, and at $-0.2$ when the average is $0.5$. Same method:

$$-0.5w + (1-w)a = 0.2$$
$$0.5w + (1-w)a = -0.2$$

The anchor comes out to $0$ again. The responsiveness comes out to $-0.4$.

She runs the same model as the modest woman, with the sign flipped and the magnitude doubled: a fixed neutral point, a fixed reaction coefficient, pushing away from the reference instead of toward it.

We usually file contrarians under "independent-minded". The arithmetic disagrees. She is more dependent on the social reference than the modest woman, in absolute terms, because reliably doing the opposite of something requires tracking that thing closely. Contrarianism is dependency with a minus sign, not independence.

## The spectrum

The values of $w$ carve out a named family of postures, all instances of the same equation:

| $w$ | Posture | Behavior |
|---|---|---|
| above $1$ | Amplifier | Overshoots the reference in whichever direction it moves. The chameleon from the story. |
| $1$ | Absolute conformist | The anchor drops out of the formula. Behavior equals the reference, exactly, always. No fixed point to reconstruct a belief from. |
| between $0$ and $1$ | Partial conformist | A real anchor and a real pull toward the reference. The modest woman. |
| $0$ | Independent | Behavior ignores the reference entirely. The only posture that requires no information about the reference to act. |
| between $-1$ and $0$ | Partial contrarian | A real anchor and a real push away from the reference. The contrarian. |
| $-1$ | Absolute contrarian | Maximal dependence on the reference, inverted. Needs to track the reference with more precision than the conformist to reliably oppose it. |

The independent is the only entry that doesn't need to know what the reference is doing. Every other posture, the amplifier and both contrarian rows included, is a reference-tracking system. In this narrow sense the absolute conformist and the absolute contrarian sit closer to each other than either sits to the independent. And the spectrum doesn't stop at the table's ends: below $-1$ sits the mirror image of the chameleon, a contrarian who overshoots, an extremist rebel?

## When moving is right

So far the model is morally neutral, and that's the point. High or low responsiveness is neither good nor bad until you ask what kind of reference is in play.

A normative reference (peer pressure, fashion, social approval) is something your anchor is supposed to resist. High responsiveness there is suspect by default.

A structural reference (a deadline, a budget, a body, a risk exposure) is something your anchor is supposed to track. Zero responsiveness there isn't principle. It's malfunction.

However in an ideal world, IMHO the $|w|$ should be generally small, and everyone should have an educated Anchor. But this is not an ideal world and not everyone can get educated about everything. So, let's stick to our less-than-ideal world.

Retirement investing makes this concrete. A common rule of thumb sets equity allocation at roughly $110$ minus your age: about $85\%$ stocks at 25, about $50\%$ at 60, tapering further as retirement nears. Someone who follows this, aggressive at 25, cautious at 60, is not "inconsistent". Their reference point is the years until the money is needed, and the right exposure to market swings genuinely is a function of that horizon. A 25-year-old can ride out a crash over decades. A retiree drawing down savings cannot. Here, holding behavior fixed across a life would be the failure, not the virtue. An investor who stays at $85\%$ equities at 65 because "I've always been aggressive" isn't showing conviction. They're refusing to let a correctly varying function vary.

The clothing conformist and the lifecycle investor look superficially alike: behavior that moves as a reference moves. Morally they are opposites. The flip side is just as clean: holding output fixed against a moving reference reads as integrity in the clothing case and as ossification in the investing case. Same form, opposite verdict. The verdict depends entirely on which kind of reference is being held fixed against.

## Why anchors move

That settles when *behavior* should move. The harder question is why the *anchor* moves, because that's where the moral weight actually lives.

Two forces can move a person. The world's facts can change, or your grasp of them can, giving you new evidence. Or the cost of expressing a given position can change, with no new evidence at all. Cross those forces with whether the anchor actually moved and you get four cells:

|  | Anchor updates | Anchor stays fixed |
|---|---|---|
| **Driven by evidence** | Rational revision: the good case | Ossification: the bad case |
| **Driven by cost** | Preference laundering: the bad case | Anchor held, two sub-cases below |

- **Rational revision.** The world showed you something true and you believed it.
- **Ossification.** The evidence moved and the anchor refused to. "Not swinging" is stubbornness in the costume of principle.
- **Preference laundering.** "Everyone's doing it now, so I guess it's fine." Social proof gets laundered into belief that was never actually re-examined. The anchor moved, but on cost, not evidence.
- **Anchor held.** When cost changes but the anchor genuinely doesn't move, behavior still needs sorting:
    - **Revealed preference.** Behavior snaps to the anchor once the cost of expressing it drops. The person "swinging" here was consistent the entire time. The swing is what suppression looked like from outside. This is a charitable way to read the clothing story: not a shift in belief, just a cost that finally lifted.
    - **Hysteresis.** Behavior fails to snap back even after the cost is gone, because the fear got installed deeply enough to run on its own. Still flinching at a threat that no longer exists.

One cell deserves a footnote. The evidence column doesn't require the reference itself to have moved. Tax law can sit perfectly still while your grasp of it moves from nothing to something. That still counts as evidence-driven anchor movement, just happening inside your model of a static reference. And since what you gained is a belief rather than a settled fact, a second pass at the very same unchanged reference can overturn it again. Call it perspective gain.

Now the uncomfortable part. Rational revision and preference laundering can produce an identical new anchor from an identical old one. Same destination, opposite process. From outside they are indistinguishable. Often from inside too.

## A parable in one aphorism

You've heard this one: "If you're not a socialist at 20, you have no heart. If you're still a socialist at 40, you have no head."

It gets offered as an evidence-based claim. With age comes direct experience of taxes, hiring, saving, and incentives, and views update accordingly. Structurally that's the lifecycle investing story: rational revision, tracking new information about how the world works.

But the same trajectory falls out of a much less flattering process. As people age they typically acquire assets, income, and things to lose from redistribution. Views can drift to track self-interest rather than evidence. Preference laundering with extra steps. Both processes produce the same trajectory and the same retrospective story: "I used to be naive." Nothing about the shift itself tells you which one occurred.

## Three ways the clean model gets dirty

Real cases add complications the toy model doesn't capture. Three seem unavoidable.

**Confounded attribution.** Circumstances rarely change as pure evidence or pure cost. Usually both move together. A society opening up removes punishment and publicly stress-tests the reasons the old rule was defended on, which is genuine evidence. A person can land on the objectively correct new anchor for the wrong reason, carried by cost while evidence happened to agree. The flaw stays invisible until cost and evidence next point in opposite directions, at which point the process, having never been evidence-driven, follows cost again and gets it wrong that time. A correct belief reached by an unreliable process is not the same asset as a correct belief reached by a reliable one.

**Misperceived reference.** Everything so far assumes the person correctly perceives where the reference sits. They might not: thinking a norm still forbids something it no longer does, or a market is still risk-off when it has turned. This is an error upstream of anchor, responsiveness, and policy entirely. It corrupts every downstream judgment without any of those three being flawed.

**Reference lag.** Sometimes what looks like a fixed anchor resisting a reference is actually perfect tracking of a different, stale reference. Diaspora communities do this with language. Second-generation immigrant communities sometimes preserve older forms of a language than the one currently spoken in the country of origin. Quebec French keeps features that metropolitan French has dropped, and you can hear the same pattern informally in many diaspora communities' speech. A person raised on that preserved form isn't holding out against assimilation into the host country's norm out of principle. Their real reference is a third thing entirely: the origin country's norm at the moment their family left it, frozen the day they emigrated, while the living language back home kept moving. The behavior looks like resistance to one reference and is actually perfect conformity to another that nobody ever intended to freeze. Apparent principle, real conformity to the wrong clock.

## The prior prediction test

Step back and notice the pattern. Nearly every pair above produces identical behavior and identical retrospective self-report: rational revision versus preference laundering, revealed preference versus contaminated drift, rational caution versus hysteresis. "I've always believed this" and "I used to be naive" are available to both the legitimate and illegitimate version, every time. That's what makes the problem hard, rather than merely a matter of introspecting harder.

One thing separates the twins: what the person predicted, before the circumstance changed, that they would do once it did, and on what grounds. A prediction made under the old regime, with reasons attached, is much harder to fake retroactively than a story assembled after the fact.

"I'll understand incentives better by 40" is a falsifiable claim about future evidence, checkable against what actually changed in the person's reasoning. "I'll have more to protect by 40" is a claim about future incentives wearing the vocabulary of insight. "I'd wear this if society let me" is a testable prediction about an anchor, not a post-hoc alibi for wherever behavior ended up.

Where no such prior prediction exists, the answer is that the case is underdetermined. The default should not be to assume the more flattering interpretation.

## So what is consistency?

Back to my mom's story. The word I started with split into three, and the three came apart completely. The woman who swung with the revolution may have been running one unchanging rule the whole time, and the investor who never changes strategy may be the one failing.

What I've landed on is that consistency of behavior was never the thing I admired or condemned. It was a proxy, and a bad one. What I'm actually trying to evaluate is the process: what the person's anchor is, what they're responsive to, and whether the movement I observe came from evidence or from cost. The process is mostly invisible, and the stories people tell about it afterward are mostly unfalsifiable. Which is why the only question I really trust is the one asked in advance: before anything changes, what do you think you'll do when it does, and why?

---

PS1: Note that I deliberately haven't explored the cases where the anchor is closer or farther from the reference. Mainly because I couldn't come up with meaningful examples to study, and hence can't put an interpretation on it.

PS2: An economists perhaps would call the anchor an indogenous variable, and the reference an exogenous variable. I've always struggled with those terms, so I rather use words that I can relate to. And the model here is the most simple model I could think of, a linear convex combination of the two variables but the combining coefficient doesn't need to be between 0 and 1, allowing to explore the region outside of the two and hence the existence of the amplifier personality. 