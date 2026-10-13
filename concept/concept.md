# Visual concept

Lesson 6, step 2, 2026-10-13. Built on `references.md` (the techniques) and `../research/` (the reasons). The concept screens are Race browse (base, `-empty`, `-error`, `-loading`; filtered = base page with active chips) and Results list (base, `-empty`, `-error`, `-loading`). Map view is out of scope.

---

## Designer's taste

The designer's own judgment, recorded in their words. It isn't derived from research; the attributes below must not contradict it.

**Like:**

1. **Strava.** The date leads the race card in its own left column; the finish time is the row's largest, boldest figure. Clear hierarchy without decoration.
2. **The hybrid-racing products from Lesson 1** (RoxFit, RoxConnect, RoxMatchUp, fitnessracingcalendar, ocrbase), both the dark and the light ones. Strong visuals; especially the race format as a small uppercase chip with a high-contrast fill ("DEKA FIT" on fitnessracingcalendar).

**Don't want:**

- **LinkedIn's look.** The logic of a gray source line under a claim is good, but the styling feels corporate and dated.
- **Letterboxd's diary.** A dense dark list where it's unclear what matters.
- **Aggressive "energy" red.**

**Theme: dark.** This is a designer decision. It isn't inherited from the brief (which also says dark) or from the artifact pages (which are dark too). The guardrail on artifact-page values still applies (`#0b0c0e`, the `#ff4d2e` family, `src/style.css`, the wireframe grays). Onrace's dark has to be derived from the attributes below, not copied from the docs.

---

## Attributes

Visual opposites, "X, not Y". Each one names:
- the data line it comes from
- the technique in `references.md` it relies on
- its strength: **data** (research or brief) or **hypothesis** (a `[?]` line in `personas.md` or `jtbd.md`), marked **[?]**

### 1. The result is the loudest thing on the row, not the frame

The finish time carries the row. Cards, borders, headers and backgrounds stay quiet around it.

- **Data:** `../research/jtbd.md` → Related job 4: "When an elite race asks me to prove a past result, I want to pull that proof up quickly, so that I can apply without scrambling to find it."
- **Technique:** Strava, the finish time as the row's largest, boldest figure (`references.md` § 4, Base; visual only).
- **Strength:** data.
- **Taste:** matches Like 1 ("clear hierarchy without decoration"), and answers the Letterboxd objection that it's "unclear what matters".

### 2. A calendar, not a poster

A race card reads as a date and a place, not as an image or a promotion. The date leads, in its own column.

- **Data:** `../research/jtbd.md` → Related job 1: "When I'm deciding what to enter next, I want to see what's coming up in the formats I actually care about, so that I can plan my season instead of finding out about races too late."
- **Technique:** Strava, the date leads the race card in its own left column (`references.md` § 4, Base; visual only, reduced form). Also AllTrails' photo-led cards, documented as not picked (no race imagery).
- **Strength:** data for the job. **[?]** That a date-first card scans faster than the date inside the meta line is untested (`references.md` § 4).
- **Taste:** matches Like 1.

### 3. Each format by name, not one sport's look

The format is the most visible label on a card: a small uppercase chip with a high-contrast fill. No single sport sets the look.

- **Data:**
  - `../research/jtbd.md` → Emotional job: "be recognized as what I actually am — a hybrid athlete — so that the tools I use reflect my training identity instead of forcing me into a single-sport box."
  - `../research/jtbd.md` → Related job 1: "the formats I actually care about".
  - `../voice.md` → principle 4, "Every format, by its own name".
- **Technique:** the format as a small uppercase chip with a high-contrast fill, from fitnessracingcalendar and RoxFit (`references.md` § 4b; visual only, on the existing `.sport-tag`).
- **Strength:** data for the jobs. **[?]** That the chip reads as "made for hybrid athletes" to real users is untested (`references.md` § 4b).
- **Taste:** matches Like 2.
- **Data and taste pull apart here, so you decide:** see Tension A below.

### 4. Proof stated, not stamped

The source sits as its own quieter line under the claim ("Self-reported · via results.hyrox.com"). No badge, no checkmark, no seal on the time or the race name.

- **Data:**
  - `../voice.md` → principle 1, "Claim only what Onrace can know".
  - `../research/research.md` → BENCHMARK, mechanism 2: "always show 'via [domain of official_result_url],' never a checkmark implying Onrace vouches for it".
  - `../research/personas.md` → Primary → Trust triggers: a product that "visibly labels 'self-reported + source-linked' would be *more transparent than what they're used to*".
- **Technique:** LinkedIn, the source on its own line under the claim, logic only (`references.md` § 4, Donor; visual only). LinkedIn's "Verified" shield is the counter-example.
- **Strength:** data. Hypothesis 4 in `jtbd.md` ("feel confident it won't be dismissed as fake") points the same way, but it's **[?]** and isn't needed for this pair.
- **Taste:** matches "Don't want: LinkedIn's look". Only the logic is taken, and the styling is Onrace's own.

### 5. Intense, not aggressive

Dark, high-contrast, bold type, with one accent on a few high-signal elements. The intensity comes from weight and contrast, not from alarm colors or a wall of saturation.

- **Data:**
  - `../CLAUDE.md` → Design / brand tone: "high-energy, athletic, performance-driven visual identity (dark, intense, bold typography)".
  - `../voice.md` → principle 3: "Plain words; the look carries the energy". Its counter-example is "Crush your next race."
- **Technique:**
  - the hybrid-racing set's color pattern, "color is one accent on small, high-signal elements, not a palette" (`references.md` § 4b, Tally)
  - Strava's hierarchy without decoration (§ 4, Base)
- **Strength:** data.
- **Taste:** matches "Don't want: aggressive 'energy' red" and the dark theme.
- **Data and taste pull apart here, so you decide:** see Tension B below.

---

## Where data and taste pull apart (for the designer to decide)

**A. Uppercase format chip vs. `voice.md` principle 4.** The taste wants the format chip in uppercase ("DEKA FIT"). Principle 4 asks for every format "by its own name … exactly". CSS uppercase leaves the markup text unchanged, but it renders "Half marathon" as "HALF MARATHON" and "Marathon" as "MARATHON". Is uppercase still "its own name"? The options:
- uppercase every chip
- uppercase only names that are already all caps (HYROX, DEKA, OCR), which would need a per-format rule
- keep sentence case and get the chip's energy from fill and weight alone

**B. "High-energy … in the spirit of HYROX/CrossFit branding" vs. "no aggressive energy red".** The brief asks for high energy and names HYROX/CrossFit as the spirit. The taste rules out aggressive red as the way to get there. These don't contradict each other, since the brief names no color. But it leaves the energy to type weight, contrast and the format chip, and step 3 has to show that this is enough. No research says whether athletes read energy from color or from type.

**C. RoxConnect: liked, but also an anti-reference.** The taste likes all five hybrid-racing products, RoxConnect included. `references.md` § 4b lists two of RoxConnect's traits as anti-references:
- its big-number stat strip: copy, already banned by `voice.md`, so no visual conflict
- "pure black plus one hot accent", as the fastest route back to the banned artifact-page values

Is RoxConnect's pure-black base part of what's liked, or only its type and contrast?

**D. How much color.** Most of the liked hybrid products keep color small (RoxFit, RoxConnect). fitnessracingcalendar puts lime on every chip and button, and RoxMatchUp spreads yellow across titles, tags and bubbles. Attribute 5 follows the "small, high-signal" majority. If the "strong visuals" you like include the louder ones, that's a range for step 3 to explore, not a rule yet.

---

## Note for step 3

The theme is fixed as dark, so the three directions must differ on at least two of:
- amount of color
- type character
- element shape
