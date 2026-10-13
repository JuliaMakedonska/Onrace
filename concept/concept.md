# Visual concept

Lesson 6, step 2, 2026-10-13. Built on `references.md` (the techniques) and `../research/` (the reasons). The concept screens are Race browse (base, `-empty`, `-error`, `-loading`; filtered = base page with active chips) and Results list (base, `-empty`, `-error`, `-loading`). Map view is out of scope.

---

## Designer's taste

The designer's own judgment, recorded in their words. It isn't derived from research; the attributes below must not contradict it.

**Like:**

1. **Strava.** The date leads the race card in its own left column; the finish time is the row's largest, boldest figure. Clear hierarchy without decoration.
2. **The hybrid-racing products from Lesson 1** (RoxFit, RoxConnect, RoxMatchUp, fitnessracingcalendar, ocrbase), both the dark and the light ones. Strong visuals; especially the race format as a small uppercase chip with a high-contrast fill ("DEKA FIT" on fitnessracingcalendar).
3. **Nike Run Club: typography.** Bold but refined. (Added 2026-10-13, after round 1.)
4. **Whoop: typography.** Technical and clean. (Added 2026-10-13, after round 1.)
5. **Black-and-white race photos.** From round 1, Direction 1.
6. **A high-contrast accent.** From round 1, Direction 3's yellow (`#F5B649`). **Open question:** it may read as HYROX yellow. See attribute 3 (c, "Each format by name, not one sport's look").

**Don't want:**

- **LinkedIn's look.** The logic of a gray source line under a claim is good, but the styling feels corporate and dated.
- **Letterboxd's diary.** A dense dark list where it's unclear what matters.
- **Aggressive "energy" red.**
- **One heavy condensed display face used for everything.** Crude, not stylish. (Added 2026-10-13, after round 1.)
- **No radius at all.** It looks like a wireframe, not a product. (Added 2026-10-13, after round 1.)

**Shape: slightly rounded, small radius.** This is a designer decision (2026-10-13).

**Theme: dark.** This is a designer decision. It isn't inherited from the brief (which also says dark) or from the artifact pages (which are dark too). The guardrail on artifact-page values still applies (`#0b0c0e`, the `#ff4d2e` family, `src/style.css`, the wireframe grays). Onrace's dark has to be derived from the attributes below, not copied from the docs.

---

## Hierarchy rules (designer)

Decided 2026-10-13, after reviewing screenshots of round 1's "Direction 1 + yellow" variant, which broke basic hierarchy. They apply to every direction from round 2 on.

1. **Accent is scarce.** At most one or two accent uses per screen, reserved for the single most important thing (the primary action, or the active state). Not on every chip, not on every finish time.
2. **Format chips are metadata.** Neutral: a subtle fill or a quiet outline, never the accent. The active filter chip differs from inactive ones by a clear but calm state, not by being the brightest thing on screen.
3. **Button hierarchy.** Exactly one primary per screen (filled). Secondary actions are tonal or outlined; tertiary actions are text links. On Race browse, Filters is secondary, not primary. On Results list, Log result is the primary.
4. **Type hierarchy.** The display face only for the screen title and the key numbers (finish time, date day). Race names, chips, buttons, tab labels and meta use the text face, in sentence case. Chips stay uppercase via CSS (decision A). At least three clearly distinct levels: screen title, item title, meta.
5. **The finish time stays the loudest thing on the row** (attribute 1) through size and weight, not through accent color on every row.
6. **The proof line has one link icon,** not two.

---

## Race card details (designer, decided 2026-10-13)

Round 2 left two details open as A/B options in `directions.html`. The designer decided both:

1. **The date sits on a tile:** a background on the date column, the day large, the month and year below it. Chosen over a plain date column.
2. **The format chip has a format dot:** a small colored dot before the format name, inside a neutral chip. Chosen over a text-only chip. The chip itself stays neutral metadata (Hierarchy rule 2).

**Card anatomy, applied to round 2 Direction A ("Podium"):** round 1 Direction 2's card: the photo inside the card (inset, with its own radius), then two columns. On the left, the date tile. On the right, a text column of the race title, then the format chip with its dot, then the location with the map-point icon. Direction A's colors, type, radius, surfaces and icon style are unchanged; only the anatomy changed. The same card is used on every card of the Race browse preview.

**Dot colors:** derived from Direction A's palette and muted: each format hue is mixed 50% into Ink 2 (`#A3A9B0`), so the dots' chroma stays at 3–29 against the accent's 63, and none competes with the accent (Hierarchy rule 1). Each dot passes 3:1 against its chip, checked by script.

**Markup hooks (not in the wireframes):**
- `data-sport="…"` on each format tag and filter chip, so CSS can color the dot.
- one `<img>` per race card for the photo. The wireframes have no photo slot.

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
- **Uppercase:** decided, CSS `text-transform` only, so the name in the markup stays as `voice.md` principle 4 requires (Tension A below).

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

Dark and high-contrast, with bold type. The intensity comes from weight, contrast and the format chip, not from alarm colors.
- **The dark** has depth, but it isn't pure `#000` and it isn't "black plus one hot accent" (Tension C).
- **How much color** varies across the step-3 directions, from restrained to rich (Tension D). It isn't fixed by this attribute.

- **Data:**
  - `../CLAUDE.md` → Design / brand tone: "high-energy, athletic, performance-driven visual identity (dark, intense, bold typography)".
  - `../voice.md` → principle 3: "Plain words; the look carries the energy". Its counter-example is "Crush your next race."
- **Technique:**
  - Strava's hierarchy without decoration (`references.md` § 4, Base)
  - the format chip (§ 4b)
  - the hybrid-racing set's range of color amount, from RoxFit's and RoxConnect's small accents to fitnessracingcalendar's and RoxMatchUp's heavier use (§ 4b)
- **Strength:** data for "dark, intense, bold". **[?]** That type, contrast or the chip can carry the energy without red is a hypothesis; step 3 tests it (Tension B).
- **Taste:**
  - matches "Don't want: aggressive 'energy' red" and the dark theme
  - takes RoxConnect's depth of dark, not its formula (Tension C)

---

## Where data and taste pull apart (decided 2026-10-13)

**A. Uppercase format chip vs. `voice.md` principle 4.** The taste wants the format chip in uppercase ("DEKA FIT"). Principle 4 asks for every format "by its own name … exactly". CSS uppercase leaves the markup text unchanged, but it renders "Half marathon" as "HALF MARATHON" and "Marathon" as "MARATHON". Is uppercase still "its own name"? The options:
- uppercase every chip
- uppercase only names that are already all caps (HYROX, DEKA, OCR), which would need a per-format rule
- keep sentence case and get the chip's energy from fill and weight alone

**Decision: keep the uppercase chip, via CSS `text-transform` only.** The format name in the markup stays exactly as `voice.md` principle 4 requires ("Half marathon"). Only the rendering is uppercase. This satisfies principle 4 because the name itself doesn't change.

**B. "High-energy … in the spirit of HYROX/CrossFit branding" vs. "no aggressive energy red".** The brief asks for high energy and names HYROX/CrossFit as the spirit. The taste rules out aggressive red as the way to get there. These don't contradict each other, since the brief names no color. But it leaves the energy to type weight, contrast and the format chip, and step 3 has to show that this is enough. No research says whether athletes read energy from color or from type.

**Decision: accepted as a hypothesis [?].** Step 3 is the test. Each of the three directions shows a different main source of energy (type, contrast, or the format chip), so the designer can judge in the browser whether that's enough without red.

**C. RoxConnect: liked, but also an anti-reference.** The taste likes all five hybrid-racing products, RoxConnect included. `references.md` § 4b lists two of RoxConnect's traits as anti-references:
- its big-number stat strip: copy, already banned by `voice.md`, so no visual conflict
- "pure black plus one hot accent", as the fastest route back to the banned artifact-page values

Is RoxConnect's pure-black base part of what's liked, or only its type and contrast?

**Decision: the depth of RoxConnect's dark is liked, not its formula.** Onrace is dark, but not pure `#000`, and not "black plus one hot accent". The anti-reference in `references.md` § 4b stays as written.

**D. How much color.** Most of the liked hybrid products keep color small (RoxFit, RoxConnect). fitnessracingcalendar puts lime on every chip and button, and RoxMatchUp spreads yellow across titles, tags and bubbles. Attribute 5 follows the "small, high-signal" majority. If the "strong visuals" you like include the louder ones, that's a range for step 3 to explore, not a rule yet.

**Decision: a range for step 3.**
- At least one direction is **restrained**: color only on the data and the format chip.
- At least one direction is **rich**: closer to fitnessracingcalendar and RoxMatchUp.
- Amount of color is one of the two required axes of difference (see the step 3 note).

---

## Note for step 3

The theme is fixed as dark, so the three directions must differ on at least two axes:
- **Amount of color (required, Tension D).** At least one direction is restrained (color only on the data and the format chip), and at least one is rich (closer to fitnessracingcalendar and RoxMatchUp).
- **And at least one of:** type character, or element shape.

They must also differ in their **main source of energy**: one each from type, contrast and the format chip. That tests the hypothesis that energy works without red (Tension B, **[?]**).

All three directions share:
- **Dark with depth:** not pure `#000`, not "black plus one hot accent" (Tension C). No aggressive "energy" red.
- **The uppercase format chip**, via CSS `text-transform` only (Tension A).
- **The guardrail:** no artifact-page values (`#0b0c0e`, the `#ff4d2e` family), nothing from `src/style.css`, no wireframe grays.

---

## Step 3, round 1 (rejected 2026-10-13)

Kept for the record in `directions-round-1.html` (live: https://juliamakedonska.github.io/Onrace/concept/directions-round-1.html). All three were dark and followed the step 3 note above.

| Direction | Color | Energy from | Type | Shape |
|---|---|---|---|---|
| 1 · Chalk on rubber | Restrained: warm charcoal `#1C1A17`, chalk `#F3EFE7`, pale magnesium blue `#BFE0EE` on times and chips only | Type | Big Shoulders Display (heavy condensed) + Barlow | Sharp, 0–2px |
| 2 · Format colors | Rich: aubergine `#221827`, a pastel color per format | The format chip | Bricolage Grotesque + Onest | Soft, pills and 20px cards |
| 3 · Floodlight | Middle: petrol night `#0C1820`, sodium amber `#F5B649` on times and the one action, glacier `#CFE6F2` chips | Contrast | Archivo (wide) + Martian Mono | Medium, 4–8px |

**Why it was rejected (the designer's feedback):**
- **Direction 1's layout is the wireframes.** All three phone previews share the wireframe structure, so the layout carried no direction of its own.
- **Direction 1's type is crude:** one heavy condensed face used everywhere.
- **No radius looks like a wireframe**, not a product.

**What carries over to round 2:**
- Direction 1's black-and-white photo treatment.
- The high contrast of Direction 3's accent. A late comparison in round 1 put Direction 3's amber on Direction 1. It showed that the amber's pull is saturation, not luminance: `#F5B649` is 9.65:1 on `#1C1A17`, below magnesium's 12.49:1, but its chroma is 63 against magnesium's 13. Its distance from HYROX's yellow (`~#FFE600` [~]) is ΔE 17.1, the open question in Designer's taste → Like 6.
