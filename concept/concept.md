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

## Color rules (designer, 2026-10-13)

Added before step 5. `scripts/concept/build_stand.py` checks rules 1–3 on every build. Rules 1, 2 and 3a stop the build when broken. Rule 3b is reported on the stand and doesn't block, because the designer keeps the current amber knowingly.

1. **Accent placement.** Amber only where you can act or where you are: the primary action, the current tab, an active state. Never on a result, a finish time, a count or a status. *Build check:* every `components.css` rule that uses `--accent` or `--accent-hover` must target an allowed selector (primary button, `.header-action`, primary `.state-action`, the current tab). Specimen swatches on the stand are the only other place.
2. **No success color on results.** Results are self-reported, and Onrace can't verify them, so there's no green and no "verified" mark anywhere on a result. The proof line stays neutral (attribute 4, d: proof stated, not stamped). *Build check:* `--success` and `--success-bg` appear on no product screen: the build allows them only on the stand's status specimen and its swatch. The saved confirmation on Results list is neutral (decided 2026-10-14: a green check next to a race name reads as a "verified" stamp). No result row contains a check icon or the word "verified".
3. **Two taste rules, made measurable** (CIELAB, D65):
   - **a. Depth of dark, not #000.** Every background level (`--bg-bar`, `--bg-0`, `--bg-1`, `--bg-2`) has a lightness L* between 4.5 and 20 and a chroma C* of at most 6 (near-neutral, not tinted). Each level is at least 1.5 L* lighter than the one below it, so the levels read as depth. For reference, #000 is L* 0 and the guardrail `#0B0C0E` is L* 3.3; both fall outside the range. *Current:* L* 4.99 / 6.69 / 12.10 / 17.33, C* 2.0–3.9. **Passes.**
   - **b. Amber, not HYROX yellow.** HYROX yellow [~] is measured from `research/screens/`. There's no screenshot of HYROX's own site there, so the reference is the HYROX-ecosystem apps: RoxFit `#FFEC00` (5,786 pixels in `roxfit-how-it-works.png`) and RoxMatchUp `#F5E401` (2,770 pixels in `roxmatchup-home.png`). The accent must be at least as far from the nearer of the two as named orange is: hue distance ≥ 25° and ΔE2000 ≥ 24. CSS `orange` `#FFA500` sits at 24.6° and ΔE 24.0 from `#FFEC00`. *Current amber `#F5B649`:* 19.2° and ΔE 18.7 from RoxFit's yellow (19.6° and ΔE 17.9 from RoxMatchUp's). It fails the threshold.
     - **Overridden by the designer, with reason (2026-10-14).** The amber `#F5B649` stays, as a conscious choice. Three things keep it from reading as HYROX's look:
       - the accent is scarce: 1–2 uses per screen (rule 1)
       - the ground is graphite, not black (rule 3a)
       - the format chips are neutral (Hierarchy rule 2)
     - The designer compared it side by side with a halfway version `#FCB24D` and a warmer `#FFB05C` that just passes. The warmer one moves toward Strava orange.
     - The build still measures rule 3b and shows it on the stand as "accepted by designer". The override covers this exact hex only: any other accent is checked against the threshold again.

---

## Race card anatomy (decided by the designer, 2026-10-13)

**Borrowed from round 1 "Format colors": layout only, no colors.** In Direction A "Podium"'s own colors, type, radius, surfaces and icons:
- the photo sits inside the card (inset, with its own radius)
- below it, on the left: the date on a tile (a raised background, the day large, the month and year below)
- on the right, a text column: the race title, the neutral format chip, the location with the map-point icon

**No per-format colors.** The format chip is Podium's neutral chip, the same for every format (Hierarchy rule 2). The format-dot option was dropped.

**Photo band: 3:1 (decided 2026-10-14).** `--photo-ratio: 3 / 1` in `tokens.css`, which gave a 109px band at 390px wide and a 213px card on the stand.
- *Step 5, on the real screen* (`wireframes/race-browse.html`): the card is 215px (114px band). The page now sizes boxes including their padding, so the photo is 342px wide, and the date column is 68px to fit "May 2027".
  - **Inside the wireframes viewer, which is the phone** (a 757px page between the status bar and home strip): **2 full cards with no filters, with 8.6px to spare**, and **1 full + 78%** with two filters on.
  - Opened directly at 390×844: 2 full + 39%, or 2 full + 13% with two filters on.
- *First screen at 390×844* (measured with `concept/first-screen.html`): **2 full race cards** with no filters (7 races); **1 full + 79% of the next** with two filters on (4 races).
- *Compared with 16:7:* a 143px band and a 247px card, giving 1 full + 77% with no filters and 1 full + 54% with two filters on.
- *Attribute b (a calendar, not a poster):* two full races on the first screen make the list read as a run of dates, not one poster per screen. The photo stays, as a band, not a hero.
- *Margin:* 3:1 fits two cards with 6px to spare. The tightest fit, a 114px band (2.86:1), had 0px.

**Markup hook the card needs (not in the wireframes):** one `<img>` per race card for the photo. The wireframes have no photo slot.

---

## Results list details (designer, 2026-10-14)

- **Saved confirmation: neutral.** "Saved: …" sits on a neutral surface (`--bg-1`) with a neutral "save" glyph in Text 2. No success color and no green check: next to a race name, a green check reads as a "verified" stamp (attribute 4, d). The text carries the meaning. Color rule 2's build check no longer allows success color anywhere on Results list.
- **Finish times: proportional figures.** They stay proportional, so digit widths vary slightly down the column. Schibsted Grotesk's tabular figures space the colons wide ("24 : 36"), which breaks the time as one number. Decided in round 2, kept by the designer.

---

## Map (designer decision, 2026-10-14)

**Map: static Natural Earth background (designer decision); the interactive Map upgrade stays deferred.**
- **Background:** Natural Earth 1:110m land and country borders (public domain), Mercator, cropped to North America and Europe, centred on 43°N. `scripts/concept/build_map.py` turns them into two shape masks in `tokens.css`. The colors are tokens only: water `--bg-bar`, land `--bg-1`, coastlines and borders `--bg-3`, no accent (Color rule 1). It's a CSS layer, with no markup change and no network request.
- **Pins:** each dot sits on its race's real latitude and longitude. Where labels would collide (London, Chamonix, Berlin; Boston, Killington), the label moves above or below on a leader line and the dot stays put. Pins are neutral.
- **Still deferred:** clusters, floating controls, real tiles, pan and zoom.
- **Caption text: a designer-approved exception (2026-10-14).** After the static map put each pin on its real coordinates, the old caption "[ map placeholder — pin positions are approximate; pan/zoom changes what's visible, not which races match ]" became untrue. Only the untrue part changed; the new caption is "[ static map — pan/zoom changes what's visible, not which races match ]" (`wireframes/race-browse.html`; `microcopy.md` row 114).

---

## Deferred to Lesson 7 (markup)

Recorded 2026-10-14, before step 6. Each item needs a change to markup or script, which steps 5–6 don't allow (only the race card photo was allowed). **In step 7, these are reported as "deferred by designer", not as new defects.**

| Item | File | Reason it waits |
|---|---|---|
| Heading levels skip h1 → h3 on Race browse: the race names are `<h3>` directly under the `<h1>` "Discover" | `wireframes/race-browse.html` | Fixing it means changing heading levels (`<h2>` for race names, or a visually hidden `<h2>`), which is structure |
| The Filters sheet doesn't move focus into itself when it opens, and doesn't close on Escape | `wireframes/race-browse*.html` (the sheet's script: `openSheet()` / `closeSheet()`) | It's wireframe JavaScript, not styling |
| Short buttons need full accessible names: "Try again" → "Try loading races again", the nav-bar "Save" → "Save result", "Dismiss" → "Dismiss this message" | "Try again" on Race browse, Race detail, Race picker, Results list, Result detail and Profile (their `-error` pages); "Save" on `log-result.html`; "Dismiss" on Race detail and Result detail. Rule: `voice.md` → Microcopy → Button; tracked in `wireframes/_critique.md` #10 | It's a markup pass (`aria-label` or visually hidden text), already planned as its own pass |
| Results list `-empty`: the header's "Log result" and the empty state's "Log your first result" do the same job. CSS keeps only one filled (the header action steps down to secondary), but two buttons remain | `wireframes/results-list-empty.html` | Removing or merging a button changes structure |
| The saved confirmation ("Saved: …") has `role="status"`, which screen readers may not announce when the element is already present at page load | `wireframes/results-list.html` (`.saved-status`, shown by script from `?saved=`) | Fixing it means changing when the script fills or reveals the live region, which is script and markup |
| The map pins' old approximate `left`/`top` values are still inline in the markup; `components.css` overrides them with the real coordinates. Remove the inline values | `wireframes/race-browse.html` (each `.map-pin`) | Removing an attribute is a markup change |
| The race card's date splits into day and month only because CSS wraps the text (`time::first-line` in a 68px column). Long month names, other languages, text zoom or a font swap can break it; a separate day element is sturdier | `wireframes/race-browse.html` (each `<time>` in a card); `concept/components.css` (`.race-card time`) | A separate day element is a markup change |

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

---

## Directions (step 3, chosen 2026-10-13)

Round 2, in `directions.html`. All three were built under the Hierarchy rules above, and critiqued with `/impeccable critique`.

**Chosen: Direction A, "Podium".** Why: it keeps the clearest hierarchy, uses the accent scarcely (once or twice per screen), and has the black-and-white photos.
- Graphite ground `#131518`, sodium amber accent `#F5B649` (round 1 Direction 3's accent, exactly), Schibsted Grotesk (display) + Hanken Grotesk (text), 6px radius, Solar bold icons.
- Its values now live in `tokens.css`, its components in `components.css`, and its stand in `concept.html`.
- **Still open:** the amber's resemblance to HYROX yellow (Designer's taste → Like 6; attribute 3). Measured against the HYROX-ecosystem yellow in `research/screens/` (RoxFit `#FFEC00`), it is 19.2° of hue and ΔE 18.7 away, below Color rule 3b's threshold (≥ 25° and ΔE ≥ 24). **Decided 2026-10-14:** kept, as a designer override of rule 3b. The reason is recorded under Color rules → 3b.

**Not picked:**
- **Direction B, "Telemetry"** (periwinkle `#A9B8FF` on blue-black, Saira + Sofia Sans, 4px). Its Results list read like a timing board. But its critique found Race browse "could belong to any dark fintech or fitness app": blue on dark drifts toward a generic tech look, and its energy depended on dimming everything that isn't data.
- **Direction C, "Bib number"** (orchid `#FF9BE6` on pine green, Mona Sans wide + Host Grotesk, 10px). It was the rich-color direction, with energy from the format chip. Under Hierarchy rule 2 the chips became neutral metadata, so its color and energy had nowhere left to go. Mona Sans is also flagged by the detector as an overused face, and pink risked reading as lifestyle, not race.

