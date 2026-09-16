---
tags: life
---
# Empathy vs. sympathy vs. compassion: feature matrix

**Legend:**

    ✓ = present / defining
    ~ = partial / possible
      = absent / not required

The four component columns (cognitive and affective empathy, sympathy, compassion) sit left of the double rule. The five to the right are whole-person profiles, arranged darkest to lightest: psychopath, sociopath, empath, altruist, and the integrated ideal. Rows stay ordered by the two dark profiles' contrast, in four blocks separated by blank dividers: present in both, in the psychopath only, in the sociopath only, and in neither.

<style>
/* Break out of the centered column to use the full window width, and cap the
   height to the viewport so the table never grows taller than the screen:
   short screens scroll internally (header stays pinned), tall screens show all. */
.matrix-scroll {
  width: 90vw;
  margin: 1.5em calc(50% - 45vw);
  box-sizing: border-box;
  overflow: auto;
  max-height: 80vh;
  max-height: 80dvh;
}
.matrix-scroll table { width: 100%; margin: 0; }
/* sticky header row */
.matrix-scroll thead th {
  position: sticky; top: 0; z-index: 2;
  background: var(--header-bg);
  box-shadow: inset 0 -1px var(--border);
}
/* sticky first (feature) column */
.matrix-scroll th:first-child,
.matrix-scroll td:first-child {
  position: sticky; left: 0; z-index: 1;
  text-align: left; min-width: 18rem;
  background: var(--bg);
  box-shadow: inset -1px 0 var(--border);
}
/* top-left corner sits above both sticky axes */
.matrix-scroll thead th:first-child {
  z-index: 3; background: var(--header-bg);
  box-shadow: inset -1px -1px var(--border);
}
/* double rule dividing the empathy components from the profile columns */
.matrix-scroll th:nth-child(5),
.matrix-scroll td:nth-child(5) { border-right: 4px double var(--text-muted); }
/* double rules dividing the four row blocks (after rows 3, 4, and 12) */
.matrix-scroll tbody tr:nth-child(3) td,
.matrix-scroll tbody tr:nth-child(4) td,
.matrix-scroll tbody tr:nth-child(12) td { border-bottom: 4px double var(--text-muted); }
</style>

<div class="matrix-scroll" markdown="1">

| Feature | Empathy: cognitive | Empathy: affective | Sympathy | Compassion | Psychopath | Sociopath | Empath | Altruist | Integrated |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Accurately modeling the other's mental state | ✓ | ~ | ~ | ✓ | ✓ | ~ | ~ | ✓ | ✓ |
| Maintains self/other boundary | ✓ |   | ✓ | ✓ | ✓ | ~ |   | ✓ | ✓ |
| Can exist in manipulators / con artists | ✓ |   |   |   | ✓ | ~ |   |   |   |
| Controlled / instrumental rather than reactive / impulsive | ✓ |   | ~ | ✓ | ✓ |   |   | ✓ | ✓ |
| Actually sharing / mirroring the emotion |   | ✓ |   |   |   | ~ | ✓ | ~ | ✓ |
| Capacity to genuinely care about the person *at all* |   | ~ | ✓ | ✓ |   | ✓ | ✓ | ✓ | ✓ |
| Motivation to help or act |   | ~ | ~ | ✓ |   | ~ | ~ | ✓ | ✓ |
| Produces guilt / remorse after causing harm |   | ~ | ~ | ~ |   | ~ | ✓ | ~ | ~ |
| Risk of emotional contagion and burnout |   | ✓ | ~ |   |   | ~ | ✓ |   | ~ |
| Biased toward vivid, similar individuals | ~ | ✓ | ~ |   |   | ✓ | ✓ |   | ~ |
| Treats people as ends, not means (Kantianism) |   | ~ | ~ | ✓ |   | ~ | ✓ | ✓ | ✓ |
| Values each person's dignity and worth (Humanism) |   | ~ | ✓ | ✓ |   | ~ | ✓ | ✓ | ✓ |
| Concern reaches *beyond* a vivid / similar in-group |   |   | ~ | ✓ |   |   |   | ✓ | ✓ |
| Believes people are fundamentally good (Faith in Humanity) |   |   | ~ | ~ |   |   | ✓ | ✓ | ✓ |
| Sustainable and scalable as a moral guide | ~ |   | ~ | ✓ |   |   |   | ✓ | ✓ |

</div>

## Notes

1. **Sympathy gets "~" on modeling the other's mind** because you can pity someone while badly misreading them. Accurate understanding helps sympathy but isn't constitutive of it, the way it is for cognitive empathy.
2. **Affective empathy gets "~" on "capacity to care"**: emotional contagion can happen involuntarily, without any real concern for the person: you can catch someone's anxiety and simply want to get away from them.
3. **The "manipulators" row is the sharpest diagnostic** for the cognitive/affective split, and it is essentially the psychopath's signature. Cognitive empathy alone is compatible with cruelty: a skilled con artist models minds precisely without resonating with or caring about them.
4. **The "sustainable and scalable" row reflects the Bloom/Singer argument** (Paul Bloom, *Against Empathy*, and Tania Singer's compassion-training research), which is a position, not a consensus. Critics reply that compassion without empathic grounding risks becoming abstract or paternalistic.
5. **Boundary maintenance is the structural difference** between affective empathy and everything else in the table: empathizing affectively means partially merging with the other's state, which is what drives both its motivational power and its burnout and bias problems.
6. **Reading the two dark profiles as columns**: the psychopath is close to the *cognitive-empathy column standing alone*, accurate modeling with the affective and caring machinery deleted. The sociopath is close to the *affective-empathy and sympathy columns clamped to a narrow in-group* and stripped of regulation. The row groups make the asymmetry visible: almost everything the psychopath has, the sociopath also has in degraded form, so the psychopath's one distinguishing possession is cold instrumental control, while a whole cluster of affective and caring rows belongs to the sociopath and not the psychopath.
7. **Etiology is deliberately left out as a row**: psychopathy is often theorized as innate and temperamental, sociopathy as environmentally acquired. That is a claim about *causes*, not about the shape of the response, so it does not belong in a feature table. Every other row answers "what is the response like," and mixing in an origin variable would muddy that logic.
8. **Clinical caveat on the two profiles**: "psychopath" and "sociopath" are not formal diagnoses. Both fall under Antisocial Personality Disorder, and the split between them is a contested, largely theoretical convention. Treat these two columns as ideal types, not categories.
9. **Terminology caveat**: usage varies across the literature. Some authors use "empathic concern" roughly where this table uses "compassion," and pop-psych usage (e.g. Brené Brown) treats "sympathy" as inherently distancing. This table uses the more neutral research sense.
10. **The five profile columns are ideal types on a dark-to-light spectrum.** The psychopath is the cognitive column standing alone. The sociopath is affective empathy plus sympathy clamped to an in-group and stripped of regulation. The empath is the affective column maxed out and unregulated, which is why it lights up emotion-sharing, contagion, and vividness bias while failing on boundary, scope, and scalability: it is the opposite of the psychopath's coldness but it inherits the sociopath's distortions, so it is not the moral ideal. The altruist is the compassion column embodied, matching the research "Light Triad" (Kantianism, Humanism, and Faith in Humanity, from Kaufman et al., 2019). The integrated ideal is the only column that scores well across every block, including the "present in neither" rows, so it is the true opposite of both dark profiles at once.
11. **The three Light Triad rows partly restate earlier rows.** "Treats people as ends, not means" (Kantianism) is essentially the inverse of the "manipulators" row: the psychopath is blank here precisely because it excels at instrumentalizing people. "Values each person's dignity and worth" (Humanism) overlaps with the caring and beyond-the-in-group rows. Only "Believes people are fundamentally good" (Faith in Humanity) adds a genuinely new dimension, an attitude rather than an empathy component, which is why both dark profiles score blank while the empath and the lighter profiles do not.
