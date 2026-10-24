# Visual concept

Lesson 6, step 2, 2026-10-13. Built on `references.md` (the techniques) and `../research/` (the reasons). The concept screens are Race browse (base, `-empty`, `-error`, `-loading`; filtered = base page with active chips) and Results list (base, `-empty`, `-error`, `-loading`, and the saved state `?saved=`). Map view is out of scope.

> **Updated 2026-10-18 (Lesson 7, step 1), to match the screens.** "Map view is out of scope" was true on 2026-10-13. The Map view on `race-browse.html` is now painted in Podium: a static Natural Earth map with pins on real coordinates (see [Map](#map-designer-decision-2026-10-14), decided 2026-10-14). The Filters sheet is painted too. Only the interactive map (clusters, controls, real tiles, pan and zoom) stays out of scope. The saved state of Results list (`?saved=`) is added to the list because it's a painted state of its own (see Results list details). The product summary of these screens is now `../DESIGN.md`, made from their code; where the two disagree, the screens win and this file is changed to match.

---

## Designer's taste

The designer's own judgment, recorded in their words. It isn't derived from research; the attributes below must not contradict it.

**Like:**

1. **Strava.** The date leads the race card in its own left column; the finish time is the row's largest, boldest figure. Clear hierarchy without decoration.
2. **The hybrid-racing products from Lesson 1** (RoxFit, RoxConnect, RoxMatchUp, fitnessracingcalendar, ocrbase), both the dark and the light ones. Strong visuals; especially the race format as a small uppercase chip ("DEKA FIT" on fitnessracingcalendar). The chip is neutral: a subtle fill, the same for every format, never the accent (Hierarchy rule 2, the designer's choice of 2026-10-13). *(Signed 2026-10-13: the designer's neutral chip from Hierarchy rule 2. Written in here on 2026-10-18 in place of "with a high-contrast fill", which the screens never used.)*
3. **Nike Run Club: typography.** Bold but refined. (Added 2026-10-13, after round 1.)
4. **Whoop: typography.** Technical and clean. (Added 2026-10-13, after round 1.)
5. **Black-and-white race photos.** From round 1, Direction 1.
6. **A high-contrast accent.** From round 1, Direction 3's yellow (`#F5B649`). It could read as HYROX yellow, against attribute 3 (c, "Each format by name, not one sport's look"). **Settled 2026-10-14:** the designer keeps this amber as an override of [Color rules → 3b](#color-rules-designer-2026-10-13). The accent is scarce, the ground is graphite, and the format chips are neutral.

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
3. **Button hierarchy.** Exactly one primary per screen (filled). Secondary actions are tonal or outlined; tertiary actions are text links. On Race browse, Filters is secondary, not primary. On Results list, Log result is the primary. In empty and error states, the state's own action is the primary (Change filters, Try again, Log your first result), and a header action steps down to secondary (Log result on Results list `-empty` and `-error`). *(Reworded 2026-10-18 by the designer, to match the screens: the old wording made Log result the primary in every state.)*
4. **Type hierarchy.** The display face only for the screen title and the key numbers (finish time, date day). Race names, chips, buttons, tab labels and meta use the text face, in sentence case. Chips stay uppercase via CSS (decision A). At least three clearly distinct levels: screen title, item title, meta.
5. **The finish time stays the loudest thing on the row** (attribute 1) through size and weight, not through accent color on every row.
6. **The proof line has one link icon,** not two.

---

## Color rules (designer, 2026-10-13)

Added before step 5. `scripts/concept/build_stand.py` checks rules 1–3 on every build. Rules 1, 2 and 3a stop the build when broken. Rule 3b is reported on the stand and doesn't block, because the designer keeps the current amber knowingly.

1. **Accent placement.** Amber only where you can act or where you are: the primary action, the current tab, an active state. Never on a result, a finish time, a count or a status. *Build check:* every rule in `ui/kit.css` and `stand.css` (until 2026-10-18, `components.css`) that uses `--accent` or `--accent-hover` must target an allowed selector (primary button, `.header-action`, primary `.state-action`, the Filters sheet's Apply filters button `.sheet-actions button[type="submit"]`, the grayscale screens' primary `.register-btn`, `.open-btn` and `.submit-btn` (added with the kit, 2026-10-18), the current tab). Specimen swatches on the stand are the only other place.
   - **Updated 2026-10-18 (Lesson 7, step 1), to match the screens.**
     - *The sheet's primary button was missing from the list above.* Apply filters is filled amber on the screen, and `build_stand.py` already allows `.sheet-actions button[type="submit"]`. With the sheet open, Race browse shows two amber uses: the current tab and Apply filters.
     - *"An active state" is never amber on the screens.* The only amber "where you are" is the current tab. Every other active state is neutral: the active filter chip is a `--text-2` outline, the pressed List/Map segment is `--bg-3` with a `--field-line` outline, Filters with its sheet open is `--bg-3`, a checked checkbox is `--text-1`, and the focus ring is `--text-1`. The rule's wording still allows an amber active state; the screens don't use one.
2. **No success color on results.** Results are self-reported, and Onrace can't verify them, so there's no green and no "verified" mark anywhere on a result. The proof line stays neutral (attribute 4, d: proof stated, not stamped). *Build check:* `--success` and `--success-bg` appear on no product screen: the build allows them only on the stand's status specimen and its swatch. The saved confirmation on Results list is neutral (decided 2026-10-14: a green check next to a race name reads as a "verified" stamp). No result row contains a check icon or the word "verified".
3. **Two taste rules, made measurable** (CIELAB, D65):
   - **a. Depth of dark, not #000.** Every background level (`--bg-bar`, `--bg-0`, `--bg-1`, `--bg-2`) has a lightness L* between 4.5 and 20 and a chroma C* of at most 6 (near-neutral, not tinted). Each level is at least 1.5 L* lighter than the one below it, so the levels read as depth. For reference, #000 is L* 0 and the guardrail `#0B0C0E` is L* 3.3; both fall outside the range. *Current:* L* 4.99 / 6.69 / 12.10 / 17.33, C* 2.0–3.9. **Passes.**
     - **Updated 2026-10-18 (Lesson 7, step 1), to match the screens.** There are five levels, not four. `--bg-3` `#2C3035` (L* 19.67, C* 3.81, 2.34 above `--bg-2`) is the pressed level: the secondary button's hover, the pressed List/Map segment, Filters while its sheet is open, the map pin label's hover, and the map's coastlines and borders. `build_stand.py` already checks it as the fifth level (`BG_LEVELS`). *Current, all five:* L* 4.99 / 6.69 / 12.10 / 17.33 / 19.67, C* 2.0–3.9. **Passes.**
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
- **Background:** Natural Earth 1:110m land and country borders (public domain), Mercator, cropped to North America and Europe, centred on 43°N. `scripts/concept/build_map.py` turns them into two shape masks in `map.css` (moved out of `tokens.css` in step 7, so only the Race browse pages download them). The colors are tokens only: water `--bg-bar`, land `--bg-1`, coastlines and borders `--bg-3`, no accent (Color rule 1). It's a CSS layer, with no markup change and no network request.
- **Pins:** each dot sits on its race's real latitude and longitude. Where labels would collide (London, Chamonix, Berlin; Boston, Killington), the label moves above or below on a leader line and the dot stays put. Pins are neutral.
- **Still deferred:** clusters, floating controls, real tiles, pan and zoom.
- **Caption text: a designer-approved exception (2026-10-14).** After the static map put each pin on its real coordinates, the old caption "[ map placeholder — pin positions are approximate; pan/zoom changes what's visible, not which races match ]" became untrue. Only the untrue part changed; the new caption is "[ static map — pan/zoom changes what's visible, not which races match ]" (`wireframes/race-browse.html`; `microcopy.md` row 114).

---

## Deferred to Lesson 7 (markup)

Recorded 2026-10-14, before step 6. Each item needs a change to markup or script, which steps 5–6 don't allow (only the race card photo was allowed). **In step 7, these are reported as "deferred by designer", not as new defects.**

| Item | File | Reason it waits |
|---|---|---|
| Heading levels skip h1 → h3 on Race browse: the race names are `<h3>` directly under the `<h1>` "Discover" | `wireframes/race-browse.html` | Fixing it means changing heading levels (`<h2>` for race names, or a visually hidden `<h2>`), which is structure **Done (markup pass, 2026-10-23).** |
| The Filters sheet doesn't move focus into itself when it opens, and doesn't close on Escape | `wireframes/race-browse*.html` (the sheet's script: `openSheet()` / `closeSheet()`) | It's wireframe JavaScript, not styling **Done (markup pass, 2026-10-23).** |
| Short buttons need full accessible names: "Try again" → "Try loading races again", the nav-bar "Save" → "Save result", "Dismiss" → "Dismiss this message" | "Try again" on Race browse, Race detail, Race picker, Results list, Result detail and Profile (their `-error` pages); "Save" on `log-result.html`; "Dismiss" on Race detail and Result detail. Rule: `voice.md` → Microcopy → Button; tracked in `wireframes/_critique.md` #10 | It's a markup pass (`aria-label` or visually hidden text), already planned as its own pass **Done (markup pass, 2026-10-23).** |
| Results list `-empty`: the header's "Log result" and the empty state's "Log your first result" do the same job. CSS keeps only one filled (the header action steps down to secondary), but two buttons remain | `wireframes/results-list-empty.html` | Removing or merging a button changes structure **Done (markup pass, 2026-10-23).** |
| The saved confirmation ("Saved: …") has `role="status"`, which screen readers may not announce when the element is already present at page load | `wireframes/results-list.html` (`.saved-status`, shown by script from `?saved=`) | Fixing it means changing when the script fills or reveals the live region, which is script and markup **Done (markup pass, 2026-10-23).** |
| The map pins' old approximate `left`/`top` values are still inline in the markup; `components.css` overrides them with the real coordinates. Remove the inline values | `wireframes/race-browse.html` (each `.map-pin`) | Removing an attribute is a markup change **Done (markup pass, 2026-10-23).** |
| The old hand-drawn wireframe tab-bar `<svg>`s are still in the markup (3 per page, hidden by `components.css`; the tab icons are Solar masks). Remove them. Added in step 7 (defect #4) | `wireframes/race-browse*.html`, `wireframes/results-list*.html` (`.bottom-nav .tab-icon`) | Deleting elements is a markup change **Done (markup pass, 2026-10-23).** |
| The race card's date splits into day and month only because CSS wraps the text (`time::first-line` in a 68px column). Long month names, other languages, text zoom or a font swap can break it; a separate day element is sturdier | `wireframes/race-browse.html` (each `<time>` in a card); `concept/components.css` (`.race-card time`) | A separate day element is a markup change **Done (markup pass, 2026-10-23).** |

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

Every card names its format: a small uppercase chip, neutral (Hierarchy rule 2): a subtle `--bg-2` fill with a `--chip-text` label, the same for every format, never the accent. No single sport sets the look. *(Signed 2026-10-13: the designer's neutral chip from Hierarchy rule 2. Written in here on 2026-10-18 in place of "the most visible label on a card … with a high-contrast fill". The chip is metadata; the race name and the date lead the card.)*

- **Data:**
  - `../research/jtbd.md` → Emotional job: "be recognized as what I actually am — a hybrid athlete — so that the tools I use reflect my training identity instead of forcing me into a single-sport box."
  - `../research/jtbd.md` → Related job 1: "the formats I actually care about".
  - `../voice.md` → principle 4, "Every format, by its own name".
- **Technique:** the format as a small uppercase chip, from fitnessracingcalendar and RoxFit (`references.md` § 4b; visual only, on the existing `.sport-tag`). The shape and the uppercase are taken; their high-contrast fill isn't (Hierarchy rule 2, 2026-10-13).
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

Dark and high-contrast, with bold type. The intensity comes from weight and contrast (with one scarce amber), not from alarm colors. *(Updated 2026-10-18 by the designer: the energy no longer comes from the format chip. Since Hierarchy rule 2 (2026-10-13) the chip is neutral metadata, so it carries the format's name, not the energy.)*
- **The dark** has depth, but it isn't pure `#000` and it isn't "black plus one hot accent" (Tension C).
- **How much color** varies across the step-3 directions, from restrained to rich (Tension D). It isn't fixed by this attribute.

- **Data:**
  - `../CLAUDE.md` → Design / brand tone: "high-energy, athletic, performance-driven visual identity (dark, intense, bold typography)".
  - `../voice.md` → principle 3: "Plain words; the look carries the energy". Its counter-example is "Crush your next race."
- **Technique:**
  - Strava's hierarchy without decoration (`references.md` § 4, Base)
  - *(Removed 2026-10-18 by the designer: "the format chip (§ 4b)". The chip is neutral metadata now, not a source of energy.)*
  - the hybrid-racing set's range of color amount, from RoxFit's and RoxConnect's small accents to fitnessracingcalendar's and RoxMatchUp's heavier use (§ 4b)
- **Strength:** data for "dark, intense, bold". **[?]** That type and contrast can carry the energy without red is a hypothesis; step 3 tested it (Tension B). *(2026-10-18: "or the chip" removed with the chip's energy.)*
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
  - **Updated 2026-10-18 (Lesson 7, step 1), to match the screens.** "6px radius" describes the round-2 direction. On the screens, Podium has two product radii: 4px for inner shapes (the photo inside a card, the date tile, chips, List/Map segments, map pin labels, checkboxes) and 6px for outer shapes (cards, result rows, buttons, fields, the List/Map track, the saved confirmation, the map frame). The Filters sheet isn't one of these: it follows the native iOS sheet (designer decision 2026-10-18, see [Native iOS](#native-ios-designer-rule-2026-10-18)), so its current 12px top corners are a gap to close in step 3, not a third Podium radius. *(Closed 2026-10-19, step 3b: the sheet takes `--radius-sheet`, 38px [?]; `--radius-3` (12px) is stand panels only.)*
- Its values now live in `tokens.css`, its components in `components.css`, and its stand in `concept.html`.
- **Settled:** the amber's resemblance to HYROX yellow (Designer's taste → Like 6; attribute 3). Measured against the HYROX-ecosystem yellow in `research/screens/` (RoxFit `#FFEC00`), it is 19.2° of hue and ΔE 18.7 away, below Color rule 3b's threshold (≥ 25° and ΔE ≥ 24). **Decided 2026-10-14:** kept, as a designer override of rule 3b. The reason is recorded under Color rules → 3b.

**Not picked:**
- **Direction B, "Telemetry"** (periwinkle `#A9B8FF` on blue-black, Saira + Sofia Sans, 4px). Its Results list read like a timing board. But its critique found Race browse "could belong to any dark fintech or fitness app": blue on dark drifts toward a generic tech look, and its energy depended on dimming everything that isn't data.
- **Direction C, "Bib number"** (orchid `#FF9BE6` on pine green, Mona Sans wide + Host Grotesk, 10px). It was the rich-color direction, with energy from the format chip. Under Hierarchy rule 2 the chips became neutral metadata, so its color and energy had nowhere left to go. Mona Sans is also flagged by the detector as an overused face, and pink risked reading as lifestyle, not race.

---

## Step 7 check (2026-10-14 to 2026-10-15)

`concept.html`, Race browse (all states, filtered, Filters sheet, Map) and Results list (all states) checked against this file, plus `/impeccable audit`. Nine defects found, eight fixed (the ninth was a detector false positive: the `--` in token names counted as em-dashes):

1. Hanken 700 was faked by the browser (`<strong>`, `<b>`): `strong` and `b` now use `--weight-strong` (600).
2. The Filters sheet's date fields drew the browser's calendar glyph: now Solar calendar bold, from `--icon-calendar`.
3. The filter chip's remove mark was a text "×": now Solar close-circle bold, from `--icon-close`, drawn by CSS (the text stays, aria-hidden, until Lesson 7).
4. Hidden wireframe tab-bar SVGs: added to Deferred to Lesson 7 above.
5. 69 tokens had no signed row on the stand: all signed now, and `build_stand.py` stops if a token in `tokens.css` or `map.css` has none.
6. No reduced-motion version: under `prefers-reduced-motion: reduce`, `--dur-fast` and `--dur-sheet` are 0ms.
7. Fonts came through a CSS `@import`: each page's `<head>` now preconnects and links the Google Fonts stylesheet.
8. The map masks loaded on every page: they live in `map.css`, linked only by the Race browse pages.


---

## Native iOS (designer rule, 2026-10-18)

**The rule.** Every element that has a native iOS counterpart follows Apple's Human Interface Guidelines (HIG) for anatomy, metrics and behavior: sizes, placement, grabber, large title, safe areas, 44pt targets, sheet detents, and search and segmented-control behavior. Podium keeps the visual language: colors, fonts, Solar icons and photos. Where HIG and Podium's visual language conflict, the designer decides: the seven conflicts (C1–C7) were decided on 2026-10-18, below.

The screens change through the kit in steps 3 and 5, not in this step. HIG was read on 2026-10-18 from Apple's own page data. Every link below returned HTTP 200 with no redirect, so none needed replacing. Several pages were updated for Liquid Glass (tab bars: 2025-07-28, 2025-12-16, 2026-06-08; sheets: button placement on 2026-03-24).

### Component → HIG

HIG gives no point values for a sheet's corner radius, the grabber, the tab bar's height or the search field's height on iOS: the system draws them. "System" in the table means exactly that.

| Component on the screens | HIG page | What native means for it | What Podium keeps |
|---|---|---|---|
| Tab bar (Discover, My Results, Profile) | [Tab bars](https://developer.apple.com/design/human-interface-guidelines/tab-bars) | For navigation, not actions. Visible in every section; only a modal may cover it. Labels under icons, single words where possible. Prefer filled icons. On iOS it floats above content at the bottom on a Liquid Glass background, and content shows through beneath it. It may include a search tab at the trailing end. | Solar bold icons (filled, as HIG prefers), Hanken labels, amber on the current tab. Material: translucent graphite with blur in Podium tones (**C1**). Icons: Solar (**C2**). |
| Screen title ("Discover", "My Results") and top bar | [Toolbars](https://developer.apple.com/design/human-interface-guidelines/toolbars), [Typography](https://developer.apple.com/design/human-interface-guidelines/typography) | A large title that turns into a standard inline title in the top bar as people scroll, and back to large at the top. Titles under 15 characters. Actions sit in the toolbar; the key action uses the `.prominent` style, only one, on the trailing side. Prefer symbols to text for toolbar items. Fewer custom toolbar backgrounds: a scroll edge effect separates bar and content. | The title's text in Schibsted Grotesk 800 at Large Title size, 34 (**C3**). Top bar: translucent graphite with blur (**C1**). The amber on the one primary action. |
| Search field (Race browse) | [Search fields](https://developer.apple.com/design/human-interface-guidelines/search-fields), [Text fields](https://developer.apple.com/design/human-interface-guidelines/text-fields) | A search icon, placeholder text, and a Clear button at the trailing end. Search starts as people type. An inline field sits above the list it filters and can pin to the top toolbar on scroll. Bottom-toolbar search or a search tab are the other native placements. | `--bg-1` field, `--field-line` boundary, Solar magnifier (**C2**), the placeholder "Race name or city". Inside a bar, its corners are concentric with the bar (**C7**). |
| List / Map segmented control | [Segmented controls](https://developer.apple.com/design/human-interface-guidelines/segmented-controls) | For closely related subviews (List and Map qualify). Segments of equal width, text only, nouns, at most about five on iPhone. | `--bg-2` track, `--bg-3` selected segment, Hanken 14/600. Inside the controls bar, corners concentric with the bar (**C7**). |
| Buttons (Filters, Log result, state actions, sheet actions) | [Buttons](https://developer.apple.com/design/human-interface-guidelines/buttons) | Hit region at least 44×44pt. A press state on every custom button. One or two prominent buttons per view. Style, not size, separates the preferred choice. The primary role takes the accent. A delayed action shows an activity indicator inside the button, with an alternative label ("Checking out…"). | Amber primary, tonal secondary, underlined tertiary, Hanken 15/600, the 1px press. Buttons in content keep 6px (**C7**); a button inside a bar is concentric with it. |
| Filters sheet | [Sheets](https://developer.apple.com/design/human-interface-guidelines/sheets) | See *Native sheet anatomy* below. | Our raised graphite level as its background (**C4**), translucent with blur (**C1**), the scrim, Hanken type, Solar icons inside. |
| Region select (sheet) | [Pull-down buttons](https://developer.apple.com/design/human-interface-guidelines/pull-down-buttons), [Pickers](https://developer.apple.com/design/human-interface-guidelines/pickers) | A short list of choices (6 regions) is a menu from a button, not a picker. Mutually exclusive choices that aren't commands belong in a pop-up button, which shows the current value. | The button: Hanken 15, `--text-1` value, Solar chevron (**C2**). The menu it opens is the system's (**C2**). |
| Race date from / to (sheet) | [Pickers](https://developer.apple.com/design/human-interface-guidelines/pickers) | A compact date picker: a button showing the current value in the app's accent color, which opens a calendar editor in a modal view. Values and their order follow the device's locale. | The date picker is drawn by the system (**C2**). Its tint is neutral text color, not amber (**C4**). Hanken type on our button. |
| Sport-type choices (sheet) | [Toggles](https://developer.apple.com/design/human-interface-guidelines/toggles), [Lists and tables](https://developer.apple.com/design/human-interface-guidelines/lists-and-tables) | iOS has no checkbox. In a list row, use a switch (default green, or the app's accent), or a selectable row that adds a checkmark when chosen. Outside a list, use a button that behaves like a toggle. | Hanken 15 labels, `--text-1`. Checkmark or switch tinted in neutral text color, never amber or green (**C4**). |
| Sort ("Sort: Soonest first") | [Pull-down buttons](https://developer.apple.com/design/human-interface-guidelines/pull-down-buttons) | A button that opens a menu; sorting is HIG's own example. A menu should list at least three items; for one or two, consider other controls. For mutually exclusive choices, use a pop-up button. | Hanken 14/600, "Sort:" in `--text-2`, Solar chevron on our button (**C2**). The menu is the system's (**C2**). |
| Result rows; race cards | [Lists and tables](https://developer.apple.com/design/human-interface-guidelines/lists-and-tables) | A row that drills into a detail view shows a disclosure indicator. Selection gives feedback (a highlight). Items that vary in size or carry many images suit a collection rather than a list, so the photo-led race cards are a collection. | Cards, photos, the date tile, the finish time, the proof line, 4/6px radii (content keeps 4/6, **C7**). Disclosure chevron in Solar (**C2**). Never glass (**C1**). |
| Error states | [Alerts](https://developer.apple.com/design/human-interface-guidelines/alerts) | Don't use an alert only to inform, or for a connection problem: show it in context with a non-intrusive label. An alert is for something people must act on. | The inline state message, the coral icon. No gap: the screens already do this. |
| Loading | [Progress indicators](https://developer.apple.com/design/human-interface-guidelines/progress-indicators) | Indeterminate loading uses an activity indicator, and indicators keep moving ("people associate a stationary indicator with a stalled process"). Lists support pull-to-refresh, and content also refreshes on its own. | Skeleton shapes in `--bg-2` with a subtle pulse, still under Reduce Motion (**C6**). |
| Status bar | [Status bars](https://developer.apple.com/design/human-interface-guidelines/status-bars) | Transparent, never permanently hidden. Content under it is obscured, preferably with a scroll edge effect. | Light content on the graphite ground (as the viewer already samples). A scroll edge effect in Podium tones (**C1**). |
| Safe areas and margins | [Layout](https://developer.apple.com/design/human-interface-guidelines/layout) | Respect the safe areas (Dynamic Island at the top, home indicator at the bottom) and system margins. Layouts adapt to text-size changes. Controls are set off from content by Liquid Glass and a scroll edge effect, not a solid background. | 16px gutter and the spacing scale, where HIG doesn't set the margin. Bars in translucent graphite (**C1**). |
| Type | [Typography](https://developer.apple.com/design/human-interface-guidelines/typography) | SF Pro and the text styles. At the default size: Large Title 34pt Regular (Bold when emphasized), Headline 17 Semibold, Body 17, Subhead 15, Footnote 13, Caption 2 11. Minimum 11pt. Support Dynamic Type; custom fonts must implement Dynamic Type and Bold Text themselves. | Schibsted Grotesk 800 and Hanken Grotesk 400/600, mapped onto the HIG text styles (**C3**; see the mapping below). |
| Appearance | [Dark Mode](https://developer.apple.com/design/human-interface-guidelines/dark-mode) | Respect the system appearance; don't offer an in-app setting. Dark-only only "in rare cases", such as immersive media. Prefer system background colors, base and elevated (a modal sheet takes the elevated one). Contrast at least 4.5:1; aim for 7:1 for custom colors in small text. | Dark only, a designer decision (**C5**). Our graphite levels, not system backgrounds (**C4**). |
| Accessibility | [Accessibility](https://developer.apple.com/design/human-interface-guidelines/accessibility) | Controls 44×44pt (28×28 minimum). About 12pt of space around elements with a bezel, 24pt around those without. Contrast 4.5:1 up to 17pt; 3:1 at 18pt or in bold. Text can grow to 200%. Respect Reduce Motion. Don't convey meaning with color alone. Label everything for VoiceOver. Give every swipe an on-screen alternative. | AA contrast on all 65 pairs, 44px targets, reduced motion at 0ms, icon plus text in state messages. |

### Native sheet anatomy (the Filters sheet, designer decision 2026-10-18)

The Filters sheet follows the native iOS sheet instead of a one-off 12px exception ([Sheets](https://developer.apple.com/design/human-interface-guidelines/sheets), iOS):
- **Corner radius:** the system's sheet radius. HIG publishes no number; step 3 takes the value from Apple's iOS design resources and records it as a token. It replaces the 12px from `--radius-3`. `tokens.css`'s comment, the stand and CLAUDE.md change in step 3. *(Step 3b, 2026-10-19: `--radius-sheet: 38px`, **provisional [?]**: Apple's kit couldn't be read, see [Step 3b](#step-3b-native-ios-pass-in-the-kit-2026-10-19). The kit's and the stand's 12px comments are updated.)*
- **Grabber:** a small horizontal indicator at the top edge, shown because the sheet is resizable. Dragging it resizes; tapping it cycles through the detents; VoiceOver can operate it. System size and color; HIG gives no number.
- **Detents:** large (fully expanded) is always supported; medium is about half. A filter form is more useful at full height, but medium allows progressive disclosure. Which detents Filters uses is for step 3; today the sheet has one fixed height (75%). *(Decided 2026-10-19: the large detent only.)*
- **Buttons:** a top toolbar with Cancel on the leading edge and the confirming action on the trailing edge (Done in HIG; here Apply filters, `.prominent`). Not a bottom footer.
- **Dismissal:** swipe down to dismiss. If filters were changed but not applied, ask to confirm with an action sheet. Cancel stays as the on-screen alternative.
- **Background:** our raised graphite level, `--bg-2` (**C4**, decided 2026-10-18), translucent with blur (**C1**). Confirmed by the designer, 2026-10-18; applied in step 3b (sheet glass, `--bg-2` at 90%).

### Gaps: the two screens against HIG (2026-10-18)

What the screens do now, measured at 390×844. These are fixed through the kit in steps 3 and 5; nothing changes in this step.

| # | Element | What HIG says | What the screen does now |
|---|---|---|---|
| G1 | Tab bar | Floats above content at the bottom on Liquid Glass; content shows through beneath it ([Tab bars](https://developer.apple.com/design/human-interface-guidelines/tab-bars), iOS) | A full-width solid `--bg-bar` bar fixed to the bottom edge with a hairline on top, 64px; content stops above it |
| G2 | Tab bar, bottom safe area | Respect the safe area ([Layout](https://developer.apple.com/design/human-interface-guidelines/layout), Guides and safe areas) | No bottom inset in the tab bar: `--tabbar-h` assumes the wireframes viewer draws the home indicator outside the page |
| G3 | Tab label "My Results" | Single-word labels where possible ([Tab bars](https://developer.apple.com/design/human-interface-guidelines/tab-bars)) | Two words (fixed by `voice.md`: "results archive (label: My Results)") |
| G4 | Large title | Turns into a standard inline title in the top bar on scroll, and back to large at the top ([Toolbars](https://developer.apple.com/design/human-interface-guidelines/toolbars), iOS) | The `h1` scrolls away entirely; no title stays on screen (scrolled 400px, the title is 354px above the top) |
| G5 | Log result (Results list header) | The key action sits in the toolbar, `.prominent`, one only, on the trailing side; prefer symbols to text ([Toolbars](https://developer.apple.com/design/human-interface-guidelines/toolbars), Actions) | A filled text button in the large-title row; it scrolls away with the title |
| G6 | Top safe area, status bar | Respect the top safe area; obscure content under the status bar with a scroll edge effect ([Status bars](https://developer.apple.com/design/human-interface-guidelines/status-bars), [Layout](https://developer.apple.com/design/human-interface-guidelines/layout)) | No top inset (`env(safe-area-inset-top)` isn't used); the header starts 8px from the page top, and the viewer draws the status bar outside the page |
| G7 | Sticky controls bar (Filters, List/Map, chips) | Fewer custom bar backgrounds; separate controls from content with a scroll edge effect, not a solid background ([Toolbars](https://developer.apple.com/design/human-interface-guidelines/toolbars), [Layout](https://developer.apple.com/design/human-interface-guidelines/layout)) | A solid `--bg-0` bar with a hairline under it |
| G8 | Search field, position | An inline field sits above the list it searches; consider pinning it to the top toolbar on scroll ([Search fields](https://developer.apple.com/design/human-interface-guidelines/search-fields), iOS) | Above the list, but in the header, so it scrolls away; only the controls below it stay pinned |
| G9 | Search, behavior | Start searching as people type ([Search fields](https://developer.apple.com/design/human-interface-guidelines/search-fields)) | Searches only when the keyboard's Search key submits the form |
| G10 | Search, Clear button | A Clear button at the trailing end ([Text fields](https://developer.apple.com/design/human-interface-guidelines/text-fields), iOS) | None: CSS hides the browser's own (`::-webkit-search-cancel-button`) and adds nothing |
| G11 | List / Map segments | Segments of equal width ([Segmented controls](https://developer.apple.com/design/human-interface-guidelines/segmented-controls)) | Sized by their text: List 54px, Map 60px |
| G12 | Sheet buttons | Cancel on the leading edge of the top toolbar, Done on the trailing edge ([Sheets](https://developer.apple.com/design/human-interface-guidelines/sheets), iOS, 2026-03-24) | Cancel and Apply filters as equal halves of a sticky bottom footer |
| G13 | Sheet detents | Large always; medium (about half) to consider; the sheet rests at its detents ([Sheets](https://developer.apple.com/design/human-interface-guidelines/sheets)) | One fixed height: up to 75% (633px of 844), not resizable |
| G14 | Grabber | In a resizable sheet: drag to resize, tap to cycle detents, VoiceOver can operate it ([Sheets](https://developer.apple.com/design/human-interface-guidelines/sheets)) | A decorative 32×4px `div` in `--field-line`: not draggable or tappable, and not exposed to VoiceOver |
| G15 | Swipe to dismiss | People expect to swipe down to dismiss a sheet; confirm if there are unsaved changes ([Sheets](https://developer.apple.com/design/human-interface-guidelines/sheets)) | Closes only on Cancel or a tap on the scrim |
| G16 | Sheet corners | The system's sheet radius ([Sheets](https://developer.apple.com/design/human-interface-guidelines/sheets); designer decision 2026-10-18) | 12px (`--radius-3`, labeled "stand panels only") |
| G17 | Region | A short list is a menu from a button; a mutually exclusive choice is a pop-up button showing the value ([Pickers](https://developer.apple.com/design/human-interface-guidelines/pickers), [Pull-down buttons](https://developer.apple.com/design/human-interface-guidelines/pull-down-buttons)) | A `<select>` drawn as a field, with a label above it and a Solar triangle chevron |
| G18 | Race date from / to | A compact date picker: a button with the value in the accent color, opening a calendar editor ([Pickers](https://developer.apple.com/design/human-interface-guidelines/pickers), iOS) | Two field-like `<input type="date">` with a Solar calendar glyph; the value's format comes from the browser ("23.09.2026") |
| G19 | Sport types | No checkbox on iOS: a switch in a list row, or a row that shows a checkmark when chosen ([Toggles](https://developer.apple.com/design/human-interface-guidelines/toggles), [Lists and tables](https://developer.apple.com/design/human-interface-guidelines/lists-and-tables)) | Seven 18px square checkboxes, `--text-1` when checked |
| G20 | Sheet form layout | Options in a list; the grouped style separates groups with headers and space ([Lists and tables](https://developer.apple.com/design/human-interface-guidelines/lists-and-tables), Style) | Stacked label-over-field groups on the sheet surface, not list sections |
| G21 | Sort | A menu button; at least three items to justify a menu; mutually exclusive → pop-up button ([Pull-down buttons](https://developer.apple.com/design/human-interface-guidelines/pull-down-buttons)) | A `<select>` with two options (Soonest first, Latest first), drawn as text plus a Solar triangle chevron |
| G22 | Result rows, drill-in | A row that opens a detail view shows a disclosure indicator ([Lists and tables](https://developer.apple.com/design/human-interface-guidelines/lists-and-tables), iOS) | The whole row is a link with no chevron (race cards are a collection, so no gap there) |
| G23 | Selection feedback | Give feedback when people select an item, such as a highlight ([Lists and tables](https://developer.apple.com/design/human-interface-guidelines/lists-and-tables)) | Race cards and result rows have a hover ring only (pointer); no pressed state on tap |
| G24 | Pull to refresh | Lists offer a refresh control, plus automatic updates ([Progress indicators](https://developer.apple.com/design/human-interface-guidelines/progress-indicators), iOS) | None; re-tapping My Results reloads (`flows.md`) |
| G25 | Loading | An activity indicator for indeterminate loading; keep indicators moving ([Progress indicators](https://developer.apple.com/design/human-interface-guidelines/progress-indicators)) | Static skeletons, no spinner, no shimmer (**C6**) |
| G26 | Busy button | An activity indicator inside the button with an alternative label ([Buttons](https://developer.apple.com/design/human-interface-guidelines/buttons), iOS) | `components.css` defines busy as a text change only ("Saving…"); not shown on these two screens |
| G27 | Spacing between active filter chips | About 12pt around elements with a bezel ([Accessibility](https://developer.apple.com/design/human-interface-guidelines/accessibility), Mobility) | 8px (`--space-2`) between outlined chips, and between the chips and "Clear all filters" |
| G28 | Dynamic Type and Bold Text | Support text-size changes up to 200%; custom fonts must implement Dynamic Type and Bold Text ([Typography](https://developer.apple.com/design/human-interface-guidelines/typography), [Accessibility](https://developer.apple.com/design/human-interface-guidelines/accessibility)) | Fixed px sizes; the 68px date column and `::first-line` day split would break at large sizes (already in Deferred to Lesson 7) |
| G29 | Text sizes | Default body 17pt; minimum 11pt ([Typography](https://developer.apple.com/design/human-interface-guidelines/typography)) | Body 15px, meta 14px, proof 13px, labels 11px (the minimum holds). Whether the sizes move is part of **C3** |
| G30 | Contrast for small custom-colored text | At least 4.5:1; aim for 7:1 for custom colors in small text ([Dark Mode](https://developer.apple.com/design/human-interface-guidelines/dark-mode)) | All pairs pass 4.5:1. Under 7:1: `--text-2` on `--bg-1` 6.90:1 (location, proof line, result date) and on `--bg-2` 6.01:1 (month and year on the date tile, the unselected segment) |
| G31 | Appearance | Respect the system's light or dark setting; dark-only in rare cases ([Dark Mode](https://developer.apple.com/design/human-interface-guidelines/dark-mode)) | Dark only (`color-scheme: dark`); no light appearance (**C5**) |
| G32 | Sheet focus and Escape | VoiceOver and keyboard reach everything; Escape cancels a modal ([Accessibility](https://developer.apple.com/design/human-interface-guidelines/accessibility), [Alerts](https://developer.apple.com/design/human-interface-guidelines/alerts)) | Focus doesn't move into the sheet and Escape doesn't close it (already in Deferred to Lesson 7) |
| G33 | Heading levels | Label the interface for VoiceOver ([Accessibility](https://developer.apple.com/design/human-interface-guidelines/accessibility)) | Race browse skips `h1` → `h3` (already in Deferred to Lesson 7) |

**Already native:** 44px targets (chips and the tertiary link extend to 44), a press state on buttons, one primary per screen, errors shown in context rather than as alerts, an explanation when a tab is empty, tabs never hidden or disabled (the gated tabs open Sign in), Reduce Motion (0ms), titles under 15 characters, filled tab icons.

### HIG against Podium's visual language: decided (designer, 2026-10-18)

The seven conflicts, as they were put to the designer, and the decision on each. They land through the kit in steps 3 and 5.

| # | HIG wanted | Podium had | Decision (designer, 2026-10-18) |
|---|---|---|---|
| **C1** | Tab bar, toolbars and search on Liquid Glass; a scroll edge effect instead of solid bar backgrounds | Solid, flat graphite levels (`--bg-bar` tab bar, `--bg-0` sticky controls, hairlines), no blur | **Adopt glass for bars and the sheet:** the tab bar, the top bar, the controls bar and the Filters sheet become translucent graphite with blur, in Podium's tones. **Never on cards.** Content stays flat. |
| **C2** | SF Symbols for tab icons, toolbar items, Clear, disclosure and pop-up chevrons, Back and Close | Solar bold everywhere | **Solar stays for our icons.** Controls the system draws (the date picker, system menus) stay system, with their own glyphs. |
| **C3** | SF Pro and the text styles (Large Title 34pt, Body 17pt), Dynamic Type | Schibsted Grotesk 800 at 38px, Hanken Grotesk at 15/14/13/11px | **Keep Schibsted and Hanken. Map Podium's type scale onto the HIG text styles** (Large Title 34, Headline 17, Subheadline 15, Footnote 13, Caption 11). The proposed mapping and its measured effect are below. |
| **C4** | System base/elevated backgrounds; native controls tint with the accent (date picker value, switch, checkmark); the switch defaults to green | Graphite tokens; amber only on the one primary and the current tab; no green | **Control tint is neutral (text color)** for checkmarks and switches. **Amber stays only per Color rule 1.** The sheet's background is our raised graphite level. |
| **C5** | Respect the system appearance; dark-only in rare cases | Dark only | **Dark only, kept.** Reason, the designer's decision: dark is Onrace's identity (Designer's taste → Theme, 2026-10-13: "Theme: dark"), derived from the brand tone ("dark, intense, bold", `../CLAUDE.md`) and the five attributes, and every color rule (1–3a), the 65 checked contrast pairs and the black-and-white photos were built for it. A light appearance would be a second visual system to design and check, not a toggle. |
| **C6** | A moving activity indicator; indicators keep moving | Still skeletons, "no spinner, no shimmer" | **A subtle pulse on skeletons**, off under `prefers-reduced-motion` (skeletons stay still). Still no spinner and no shimmer. |
| **C7** | Corners concentric with the bar for components inside bars; system controls draw their own shapes | 4px inner / 6px outer everywhere | **Concentric only for elements inside bars** (the search field, the segmented control). **Content keeps 4/6px.** **Designer decision, 2026-10-19 (3b review):** bar controls are all full capsules, iOS 26 style (radius = half the height, `--radius-bar-control`): the search field, the Filters button and the List/Map control, with the List/Map segment concentric inside (`--radius-bar-inner`). Content (cards, chips, tiles, buttons outside bars) keeps 4/6px. |

### Type scale on the HIG text styles (C3): the proposed mapping

**Approved as proposed by the designer, 2026-10-18.** Lands in step 3b. Fonts stay Schibsted Grotesk 800 and Hanken Grotesk 400/600; only sizes change. HIG's default (Large) sizes from [Typography](https://developer.apple.com/design/human-interface-guidelines/typography); leading stays Podium's (`--leading-*`) until the Dynamic Type work (G28).

| Podium role | Now | HIG text style | Proposed | Change |
|---|---|---|---|---|
| Screen title (`--size-title`) | Schibsted 800, 38px | Large Title (34) | 34px | −4 |
| Finish time (`--size-time`) | Schibsted 800, 32px | none: a display figure, not text; not in the five styles named | 32px, scales with Large Title under Dynamic Type | 0. **Decided 2026-10-18 (designer): stays 32px as a display figure** (attribute a: the finish time is the loudest thing on the row) |
| Date day (`--size-day`) | Schibsted 800, 30px | none: a display figure | 30px, scales with Large Title | 0. **Decided 2026-10-18 (designer): stays 30px as a display figure** (attribute a) |
| Item title (`--size-item`) | Hanken 600, 17px | Headline (17, Semibold) | 17px | 0 |
| Body, buttons (`--size-body`) | Hanken 400/600, 15px | Subheadline (15; emphasized Semibold) | 15px | 0 |
| Meta (`--size-meta`): location, counts, sort, result date, state body | Hanken 400, 14px | Subheadline (15) | 15px | +1 |
| Proof line, month under the day (`--size-proof`) | Hanken 400, 13px | Footnote (13) | 13px | 0 |
| Chip and tab labels (`--size-label`) | Hanken 600, 11px | Caption 2 (11, emphasized Semibold) | 11px | 0 |

Why meta goes up to Subheadline, not down to Footnote: at 13 it would be the same size as the proof line, and the two are different levels (meta under a title, proof under a claim). At 15 it shares Subheadline with body text and stays apart from it by color (`--text-2`).

**Re-measured first screen** (the proposed sizes injected over `tokens.css` in the browser at 390px wide; no file changed). The race card grows 214.7 → 216.1px (the location line); the title saves 4px.

| Screen, state | Viewport | Now | Proposed |
|---|---|---|---|
| Race browse, no filters | viewer page, 757px | 2 full cards, 8.6px to spare | 2 full cards, 9.7px to spare |
| Race browse, two filters (`?sport=hyrox&sport=marathon`) | viewer page, 757px | 1 full + 78% | 1 full + 79% |
| Race browse, no filters | 390×844 | 2 full + 39% | 2 full + 39% |
| Race browse, two filters | 390×844 | 2 full + 13% | 2 full + 13% |
| Results list | both | 4 rows, all full | 4 rows, all full |

Attribute b holds: two full race cards on the first screen. This measure is before C1: a floating glass tab bar lets content run under it, which changes these numbers again in step 3.

### Gap triage (2026-10-18)

The triage covers the two Podium screens. The HIG gap check of the eight grayscale screens is done per group in step 5 (designer, 2026-10-18).

The 33 gaps above, sorted by how they get fixed. The designer's decisions C1–C7 are applied.

**Kit: styles only, steps 3 and 5 (24; G36, G38 from step 5, Discovery; G51, G52, G62, G63, G65, G66 from Archive and Infrastructure, fixed; G67 open).**

| Gap | Why it's styles only |
|---|---|
| G1 Tab bar floats on glass | Position, inset, radius, translucent fill and `backdrop-filter` (C1) |
| G2 Tab bar bottom safe area | `env(safe-area-inset-bottom)` padding |
| G6 Top safe area, scroll edge | `env(safe-area-inset-top)` and a blurred edge (C1) |
| G7 Controls bar background | Translucent graphite with blur instead of solid `--bg-0` (C1) |
| G10 Search Clear button | Stop hiding the browser's own clear button and style it; it's system-drawn (C2) |
| G11 Equal segment widths | `flex: 1` on the segments |
| G13 Sheet resting height | The large detent as a CSS height; dragging between detents is G14/G15 |
| G16 Sheet corners | The system sheet radius as a token (designer decision 2026-10-18) |
| G22 Disclosure chevron on result rows | A Solar chevron drawn by CSS (C2) |
| G23 Pressed highlight | `:active` on cards and rows |
| G25 Loading motion | A subtle pulse on skeletons, off under reduced motion (C6) |
| G26 Busy button indicator | A spinner drawn by CSS on `[aria-busy]` buttons |
| G27 12pt between bezeled chips | `gap` on the chips row |
| G28 Dynamic Type and Bold Text | Sizes in scalable units anchored to the system text size. The date tile's day split depends on the markup item already deferred |
| G29 Text sizes | The C3 mapping, in `ui/kit.css` |
| G36 Official site link target (Race detail) | `min-height` on the link, the line kept in place (step 5) |
| G38 Register / Open button in the action bar | C7: a control inside a bar is a capsule (step 5) |
| G51 Race picker search field | The search capsule, icon and sheet boundary (C4, C7) on `form.search` |
| G52 Race picker as a sheet | Rests at the large detent over Log result under the scrim |
| G62 44pt on small text links | Forgot password?, Reset password again, a row's Try again: tap padding, the lines unmoved |
| G63, G66 Busy indicators | The spinner on "Sending…" (Send a new link) and on Profile's "Saving…" row note |
| G65 Profile pop-up rows | A Solar chevron after Country and Language; rows 44px |
| G67 Confirm alert material and radius | **Closed 2026-10-23 (designer):** the sheet glass over the scrim, the glass rim, `--radius-alert` 34px **[?]** (provisional like `--radius-sheet`, to be replaced from Apple's kit), as iOS 26 alerts. Contrast floors as the sheet's glass: title 12.13:1, body 5.59:1, Sign out 5.46:1 over the worst case |
| G68 Sign out in its row | **Closed 2026-10-23 (designer):** a destructive action, coral (`--destructive`) in the Profile row too, not only in the alert. 6.74:1 on `--bg-1`, 5.87:1 on hover |

**Markup pass: changes structure, controls or text, between steps 5 and 6 (34; the wireframe annotations row from the step 5 review, designer 2026-10-23; G34, G35, G37 added in step 5, Discovery; two rows from the Discovery review, designer 2026-10-22; G40–G64 from step 5, Archive and Infrastructure).**

| Gap | Why it needs markup |
|---|---|
| G3 "My Results" tab label | A text change, governed by `voice.md` (the Dictionary's "label: My Results"); the voice decides, not the kit **Done (markup pass, 2026-10-23).** |
| G4 Large title collapses into the bar | An inline title element in the top bar and a scroll trigger **Done (markup pass, 2026-10-23).** |
| G5 Log result in the top bar | Moves the action out of the large-title row into a toolbar **Done (markup pass, 2026-10-23).** |
| G8 Search pinned on scroll | Moves the search field into the pinned block; also reverses `_conventions.md` § 1 ("outside the sticky block") **Closed (round 2, designer, 2026-10-23): no change.** The search field scrolls away with the large title, as it does in iOS: it belongs to the header, and the controls bar pins what filters the list. |
| G12 Sheet buttons in a top toolbar | Moves Cancel and Apply filters from the footer to the top **Done (markup pass, 2026-10-23).** |
| G14 Interactive grabber | A real control (a button with a label) instead of a decorative `div` **Closed (markup pass, 2026-10-23):** the grabber is removed, not made interactive: the Filters sheet rests at one detent, and HIG shows a grabber only on a resizable sheet. |
| G17 Region as a menu button | Replaces the `<select>` field with a pop-up button **Done (markup pass, 2026-10-23).** |
| G18 Compact date picker | Replaces the two date fields with date-picker buttons **Done (markup pass, 2026-10-23).** |
| G19 Sport types as checkmark rows | Replaces checkboxes with selectable list rows **Done (markup pass, 2026-10-23).** |
| G20 Sheet form as grouped list | Regroups the sheet's fields into list sections **Done (markup pass, 2026-10-23).** |
| G21 Sort as a menu button | Replaces the two-option `<select>`; with only two options, which control replaces it is decided in the markup pass (designer, 2026-10-18; HIG asks for three items in a menu) **Done (markup pass, 2026-10-23).** |
| G32 Sheet focus and Escape | Script and markup (already in Deferred to Lesson 7) **Done (markup pass, 2026-10-23).** |
| G33 Heading levels | Heading structure (already in Deferred to Lesson 7) **Done (markup pass, 2026-10-23).** |
| G34 Race detail: inline title on scroll | The race name has to appear in the top bar (a centered `.bar-title`) once the `h1` scrolls under it: a new element plus a scroll trigger, as G4 **Done (markup pass, 2026-10-23).** |
| G35 Race detail: content under the action bar | Running content under the glass needs the bar’s live height as scroll padding (it grows with the inline error): a script, or the bar moved inside the scroll area **Done (markup pass, 2026-10-23).** |
| G37 Race detail `-error`: no `h1` | DetailError’s heading is an `h2` and the page has no `h1`; it needs a heading level change (or a visually hidden `h1`) **Done (markup pass, 2026-10-23).** |
| Race detail: "Couldn’t open the link" as a native alert (designer, 2026-10-22) | RegLinkError becomes a native alert ([Alerts](https://developer.apple.com/design/human-interface-guidelines/alerts)) instead of an inline error that grows the bottom action bar: a `dialog.alert` like Profile’s Sign out confirm, opened by the Register script. The action bar keeps one fixed height, which also makes G35 simpler **Done (markup pass, 2026-10-23).** |
| Race detail: action caption "Opens in a new tab" → "Opens the race website" (designer, 2026-10-22) | A text change: on iOS the link opens Safari or an in-app browser, not a tab. When the pass runs, update `microcopy.md` (the Race detail action-bar caption rows) and re-run `scripts/build_voice_html.py` for `voice.html` **Done (markup pass, 2026-10-23).** |
| G40 Log result as a modal | A self-contained create task is a sheet with Cancel and the confirming action ([Sheets](https://developer.apple.com/design/human-interface-guidelines/sheets)); today a pushed drill-down with "‹ My Results" + Save. Changes navigation (`flows.md`) **Done (markup pass, round 2, 2026-10-23).** |
| G41 Log result: confirm before discarding | Back drops typed data silently; HIG asks to confirm. Script and an alert **Done (markup pass, round 2, 2026-10-23).** |
| G42 Log result form as a grouped list | Stacked label-over-field, as G20 **Done (markup pass, round 2, 2026-10-23).** |
| G43 Log result: Sport type as a pop-up button | A `<select>` drawn as a field, as G17 **Done (markup pass, round 2, 2026-10-23).** |
| G44 Log result: compact date picker | `input type=date` shows the browser's locale format, as G18 **Done (markup pass, round 2, 2026-10-23).** |
| G45 Log result: Finish time keyboard | `type=text` without `inputmode`: the full keyboard opens **Done (markup pass, round 2, 2026-10-23).** |
| G47 Race picker: mark the linked race | With `?catalog=` the chosen race isn't checkmarked **Done (markup pass, round 2, 2026-10-23).** |
| G48 Race picker: heading levels | `h1` then row `h3`s, as G33 **Done (markup pass, 2026-10-23).** |
| G53 Result detail: inline title on scroll | As G34 **Done (markup pass, 2026-10-23).** |
| G54 Result detail: content under the action bar | As G35 **Done (markup pass, 2026-10-23).** |
| G55 Result detail `-error`: no `h1` | As G37 **Done (markup pass, 2026-10-23).** |
| G56 Result detail: Open button label | "Open official result on valenciaciudaddelrunning.com" wraps the capsule to two lines; a text change (`voice.md`) **Done (markup pass, round 2, 2026-10-23).** |
| G60 Gates: confirming action in the bar | Sign in, Reset password, New password: Cancel leading, the confirm action trailing in the bar, instead of a full-width button at the form's end. Designer decides (Log result already uses a bar Save) **Done (markup pass, round 2, 2026-10-23).** |
| G61 Gates: forms as grouped lists | As G42 **Done (markup pass, round 2, 2026-10-23).** |
| Wireframe annotations on the working pages (designer, 2026-10-23) | Remove the bracketed wireframe notes from `wireframes/*.html` ("[ map placeholder — no pins: races failed to load ]" and the like): on a painted screen they read as product text. The frozen snapshot `wireframes/_wireframe/` keeps them. **Hidden through the kit meanwhile (2026-10-23):** `.map-caption` and the `p` before a map state's heading are `display: none` (out of the layout and the accessibility tree); the loading map's note is a bare text node, so CSS can only collapse it (`font-size: 0`): it stays as static text inside the map's `img` in Chromium's accessibility tree until this pass removes it **Done (markup pass, 2026-10-23).** |
| G64 Gates' full-screen errors: heading levels | New password `-error?cause=expired`, Sign in `-error?cause=confirm`: only the bar title is an `h1`, the state heading an `h2` (as G37) **Closed (markup pass, 2026-10-23):** checked: the bar title is the page’s `h1` and the state heading an `h2` under it, which is the right order; no change. |

**Out of scope: prototype behavior, or not our standard (10).**

| Gap | Reason |
|---|---|
| G9 Search as you type | Prototype behavior: the wireframes have no live data, and `flows.md` routes every search through Loading on submit. A real search backend decides this |
| G15 Swipe down to dismiss | A gesture in a static prototype. Cancel and a tap on the scrim stay as the on-screen ways out, which HIG asks for anyway ([Accessibility](https://developer.apple.com/design/human-interface-guidelines/accessibility): offer alternatives to gestures) |
| G24 Pull to refresh | Prototype behavior: there's nothing to refresh in sample data. Re-tapping My Results reloads (`flows.md`) |
| G30 7:1 for small custom text | Our standard is WCAG AA (4.5:1), checked on all 65 pairs by `build_stand.py`; HIG's 7:1 is "strive for", not its minimum |
| G31 System light appearance | Dark only is a designer decision (C5) |
| G39 Swipe from the edge to go back (Race detail) | A gesture in a static prototype; the "‹ Discover" back button is the on-screen way, which HIG asks for anyway |
| G46 Log result: Save as `.prominent` | Amber text Save is a designer decision (Kit feedback #2, 2026-10-19) |
| G49 Race picker: swipe down to dismiss | As G15 |
| G50 Race picker: search as you type | As G9 |
| G57 Log result, Result detail: edge swipe back | As G39 |

### Kit feedback (designer, 2026-10-19)

Applied in `ui/kit.css` and `ui/kit.html` before step 3b; the grayscale screens pick it up in step 5.

1. **Profile initials: a circle.** iOS avatars are circular. `--radius-avatar: 50%`. Recorded in `DESIGN.md` → Shapes as the one exception to "no circles in content".
2. **Save on Log result: amber text.** Counted: Log result (all three pages) has no tab bar and no other primary (no `.state-action`, `.submit-btn`, `.register-btn`, `.open-btn` or `.header-action`), so it shows 0 amber uses today. Save is the screen's one primary (Color rule 1) and takes `--accent` text, `--accent-hover` on hover, like a native bar button. `build_stand.py` allows `.top-bar .save-btn` under rule 1. "Saving…" stays `--text-2`.
3. **Sign out alert: destructive style.** `dialog.alert #signout-confirm` takes `--destructive` (= `--error`, coral) text; Cancel stays Text 1 (HIG Alerts). The kit's specimen carries the screen's `id="signout-confirm"`. 6.74:1 on `--bg-1`.
4. **Invalid field: coral ring.** `--invalid` (= `--error`), 2px inside the field; focus keeps the white 2px ring outside. An invalid field with focus shows both, so the two never look alike.
5. **Detector, cramped padding.** The file-wide ignore of `cramped-padding` on `ui/kit.html` is removed from `.impeccable/config.json`; the check stays on. It reports two known hits, each printed twice (the static and the rendered pass), both on the Profile `.rows` list:
   - `<ul> "rows": children flush against bg on top/bottom (no inset)`
   - `<ul> "rows": children flush against bg on all sides (no inset)`

   **Known false positives.** Each row inside the list is 44px tall with its text centred and 16px side padding (`.row`), the iOS grouped-list anatomy ([Lists and tables](https://developer.apple.com/design/human-interface-guidelines/lists-and-tables)), so the list itself needs no inset. Report them as known, not as defects; any third `cramped-padding` hit is new.

**Also checked:** `public/workspace.html` routes the Filtered state correctly. `#04/race-browse?sport=hyrox&sport=marathon` opens the viewer on that state and the screen shows 2 chips and "4 races match your filters"; clicking Filtered in the viewer's tree writes the same hash to the workspace; with `&mode=wireframe` the frozen snapshot loads with the same filters, and a reload keeps it.

### Step 3b: native iOS pass in the kit (2026-10-19)

A separate signed pass, in `ui/kit.css` only (plus the showcase and the stand). Scope, as the designer set it: the **Kit (CSS)** gap group plus **C1, C3, C4, C6, C7**. No markup changed on any screen.

**Values from Apple: what was and wasn't available.** Apple's resources page (developer.apple.com/design/resources, read 2026-10-19) links only the **iOS and iPadOS 27** kits now. The iOS 26 kit exists in Figma's and Sketch's libraries, but it couldn't be opened from this session. HIG publishes one number for the material: [Materials](https://developer.apple.com/design/human-interface-guidelines/materials), "If the underlying content is bright, consider adding a dark dimming layer of 35% opacity" (for clear Liquid Glass). [Sheets](https://developer.apple.com/design/human-interface-guidelines/sheets) gives no radius. **Designer decision (2026-10-19): provisional values, marked [?]**, to be replaced from Apple's kit:

| Token | Value | Status |
|---|---|---|
| `--glass-opacity` (tab bar, controls bar, top bar, status-bar edge) | 85% | Set by contrast: the lowest that passes AA over the worst case is 81% (tab-bar glass) and 82% (ground glass), checked by the build; the margin is [?]. Above HIG's 35% floor. |
| `--glass-opacity-sheet` | 90% | Lowest passing over the scrim and the worst case: 87%; margin [?] |
| `--glass-blur` | 20px | [?] |
| `--glass-edge` (the rim) | Text 1 at 8% | [?] |
| `--radius-sheet` | 38px | [?] |
| `--sheet-gap-top` (above the large detent) | 12px | [?] |

**Worst case behind the glass.** The brightest thing that can scroll under a bar is Text 1 (`#F4F5F6`, a title); a photo's lightest tone after the black-and-white filter is about `#D9D9D9`, below it. Under the sheet the same Text 1 sits behind the 60% scrim. The build composites each glass over that worst case in sRGB, with no help from the blur, and every text pair on the glass must pass AA (11 pairs). `build_stand.py` also stops if a glass opacity drops below the computed minimum or below HIG's 35%.

**What changed, by item:**

| Item | In the kit |
|---|---|
| **C1** glass | `--glass-bar` (`--bg-bar` 85%) on the floating tab bar; `--glass-ground` (`--bg-0` 85%) on the controls bar, the top bar and the status-bar edge, so at rest they match the page and show only when content runs under them; `--glass-sheet` (`--bg-2` 90%) on the Filters sheet and Race picker's top bar. Blur 20px, a rim instead of hairlines. Never on cards. Under Reduce Transparency every glass is solid. |
| **C3** type | `--size-title` 38 → 34 (Large Title), `--size-meta` 14 → 15 (Subheadline); the rest unchanged (finish time 32 and date day 30 as display figures). |
| **C4** tint | `--control-tint` (Text 1) on checked boxes and as `accent-color` for every system-drawn control. The sheet on `--bg-2`. Consequence: on the `--bg-2` sheet, Field line is 2.6:1, so boundaries there take `--field-line-sheet` `#757B82` (3:1 against the sheet's worst case), and Cancel is outlined, since a tonal `--bg-2` button would vanish. |
| **C6** pulse | Skeletons pulse to 0.55 opacity and back over 1.6s; still under reduced motion. |
| **C7** concentric | Inside a bar: a capsule (`--radius-bar-control`, 22px), a segment concentric inside it (`--radius-bar-inner`, 18 = 22 − 4). Today that's List/Map in the controls bar; the search field gets it once the markup pass pins it (G8). |
| **G1, G2** tab bar | Floats 16px in from the sides and 8px above the bottom safe area, a 64px capsule with the float shadow; content runs under it, and the scroll padding lets the last item clear it. |
| **G6** top safe area | `--safe-top` (`env(safe-area-inset-top)`) on the header, the sticky controls and the top bar, and a ground-glass edge under the status bar (0px inside the viewer). |
| **G7** controls bar | Ground glass with a rim, no solid `--bg-0` and no hairline. |
| **G10** Clear | The browser's own Clear button is shown (system-drawn, C2) instead of hidden. |
| **G11** equal segments | The segmented track is a grid of equal columns. |
| **G13** detent | The large detent only: full height less the top safe area and 12px [?]; the footer sits at the sheet's bottom edge. |
| **G16** sheet corners | `--radius-sheet` 38px [?], replacing the 12px. |
| **G22** disclosure | A 15px Solar alt-arrow-right in Text 2 at a result row's trailing edge. |
| **G23** pressed | Race cards and result rows take `--bg-3` while pressed. |
| **G25** loading motion | The pulse (C6). |
| **G26** busy button | A CSS spinner before the label on `[aria-busy="true"]` and before "Saving…" in the top bar. It keeps turning under reduced motion: HIG, "people associate a stationary indicator with a stalled process". The grayscale screens' busy buttons need `aria-busy` in their markup to show it (step 5 / markup pass). |
| **G27** chip spacing | 12px between active filter chips, and before "Clear all filters". |
| **G28** Dynamic Type | Every `--size-*` and the date column are type units (`--type-unit` = 1rem ÷ 16; on iOS the root takes `-apple-system-body` and the unit is 1rem ÷ 17), so text follows the system size at 1:1 by default. Bold Text has no web hook; untested on a device. |
| **G29** text sizes | The C3 mapping. |

**Not in this pass, then decided in the 3b review (2026-10-19):** the action bar and the Filters button. See Step 3b review below.

**First screen, re-measured with content under the glass tab bar** (Chrome, 390 wide, step 3b CSS):

| Where | List starts | Tab bar top | Clear of the bar | On screen, through the glass |
|---|---|---|---|---|
| Viewer (757px), no filters | 239px | 685px | 2 full + 0%, **1.7px to spare** | 2 full + 29% |
| Viewer, two filters | 295px | 685px | 1 full + 75% | 2 full + 3% |
| 390×844, no filters | 239px | 772px | 2 full + 35% | 2 full + 69% |
| 390×844, two filters | 295px | 772px | 2 full + 10% | 2 full + 43% |

Attribute b holds (two full cards clear of the bar on the first screen), but only by 1.7px inside the viewer: the floating bar's top sits 8px higher than the old bar's. Any growth of the card or the header will push the second card under the glass.

**Checked:** `build_stand.py`: Color rules 1, 2, 3a pass (3b accepted by designer), 99 contrast pairs pass (88 solid, 11 over glass), 172 of 172 tokens signed. The look changed on purpose, so there's no pixel-identical check; every painted state was shot at 390×844 before and after, side by side on the review page.

### Step 3b review (designer, 2026-10-19)

1. **Bar controls are all capsules (C7, designer decision).** The search field, the Filters button and the List/Map control get full capsule corners, radius = half the height (`--radius-bar-control`, 22px at 44px); the List/Map segment is concentric inside (`--radius-bar-inner`, 18px). The search field's icon and text move in to 16px so they clear the curve. Content (cards, chips, tiles, buttons outside bars) keeps 4/6px. Recorded under C7 above.
2. **Action bar (Race detail, Result detail): glass, like every other bar.** `--glass-bar` (the Tab bar level it had, at 85%), the blur, a rim instead of the hairline, padding for the bottom safe area. Same contrast floor: its caption (`--text-2`) is checked over the worst case behind it (4.65:1). The build now checks 12 pairs over glass.
3. **Result rows: the chevron stays, the layout doesn't move.** The disclosure indicator now ends the meta row (`.card-meta::after`, pushed to the trailing edge), under the finish time's right edge, instead of taking 23px from the whole row. Measured at 390×844 against commit `f7492ca` (before 3b): all 4 finish times sit at exactly the same left and right pixel (right edge 358px), every proof line is one line (Valencia included), and every row has its chevron, in the base and saved states. Empty and error have no rows; the loading skeleton is back to the row's own 16px padding.
4. **`.impeccable/design.json` refreshed from DESIGN.md** by a new script, `scripts/build_design_sidecar.py` (re-run it after every DESIGN.md change). 21 colors with OKLCH and tonal ramps (the four new ones included), 10 type styles, 10 components (segmented control, result row and tab bar updated; Filters sheet added), and the narrative quoted from DESIGN.md.
5. **Empty and error states: one component, the iOS ContentUnavailableView pattern.** `.state-message` is centered horizontally and vertically in the free area below the header and above the floating tab bar (`#list-view` fills that area when it holds a state). A 48px Solar icon on top (`--icon-state`), drawn as a CSS mask, then the title, the body and the actions, centered. Text and markup unchanged.
   - **Race browse empty:** magnifer, `--text-2`: nothing matches a search or filter (iOS's own search-unavailable pattern).
   - **Results list empty:** archive (`--icon-archive`, new), `--text-2`: the results archive.
   - **Errors** (`role="alert"`, `.is-error`, or a block with a retry action): the error icon in `--error`, the screen's only coral. It replaces the 18px icon before the heading.
   - The same component fills the map panel's empty and error messages. Race picker, Race detail, Result detail and Profile use `.state-message` too and pick it up in step 5. Race picker empty will show the magnifier as well.

**First screen, re-measured after these changes** (Chrome, 390 wide): unchanged from step 3b, because none of the five changes alters a height above the list.

| Where | Clear of the bar | On screen, through the glass |
|---|---|---|
| Viewer (757px), no filters | 2 full, 1.7px to spare | 2 full + 29% |
| Viewer, two filters | **1 full + 75%** | 2 full + 3% |
| 390×844, no filters | 2 full + 35% | 2 full + 69% |
| 390×844, two filters | 2 full + 10% | 2 full + 43% |

One figure is below 2 full cards: the viewer with two filters on, 1 full + 75% clear of the bar. It was already below before step 3b (1 full + 78%), and counting what shows through the glass it's 2 full + 3%.

### Step 5, Discovery: Race detail on the kit (2026-10-22)

Lesson 7 step 5, first group. `race-detail.html`, `-error` and `-loading` link `ui/kit.css` and lost their `<style>` blocks; `class="onrace"` on the body. Structure and text are the wireframes', checked by `git diff`: the only markup added is one `<img class="photo">` per race and one photo bar in the loading skeleton; the only markup removed is three inline `style="width:…"` on skeleton bars (the kit sizes them). Race detail is a drill-down screen, so the shell's large title and tab bar don't apply; its top bar was already in the markup. The filtered Race browse state (`?sport=`) was already on the kit; nothing was left.

**Photo: kept, a designer decision (2026-10-22).** A structural exception to "structure exactly as in the wireframe": Race detail opens with the race’s photo, the same file, 3:1 band and focus class as the race’s card on Race browse, so it shows exactly the band retouched in round 3. Any other crop needs another retouch pass first (`visuals/README.md`). Each race's card file and focus class, at 3:1 like the card, full content width (358 × 119 at 390). Measured in the browser, in the 1536 × 1024 source: Berlin y 379–891, London 307–819, Dallas 225–737, DEKA and Spartan 92–604, Boston and UTMB 369–881, the full width in every case. The same as the round-3 bands, so no unretouched mark shows. `alt=""` as on the card: the photo is decorative, the race name is the `h1` under it.

**Added to the kit** (`ui/kit.css`, `ui/kit.html`, `ui/inventory.md` first, then used):
- `.race > .photo` and `.race .bar.photo`: the detail photo and its skeleton, outer 6px radius (it sits on the page).
- The drill-down layout: a page with an action bar is a column, the page scrolls above the bar; a page without a tab bar has no tab-bar scroll padding; the top bar and `main` fill the screen with no stray scroll.
- A full-screen `.state-message` (DetailError) centered under the top bar, with the 16px gutter; `.state-message[hidden]`.
- G36, G38 (below). No new token, no new color pair: every color on these pages is an existing pair (the build re-ran all 91 solid + 12 glass pairs).

**HIG check, Discovery group** (Race browse was checked in step 1; this is Race detail against the Native iOS table):

| # | Element | HIG | Race detail now | Fix |
|---|---|---|---|---|
| G34 | Top bar title | A detail view's title shows inline in the navigation bar once the large title scrolls away ([Toolbars](https://developer.apple.com/design/human-interface-guidelines/toolbars)) | Back button only; the race name scrolls out of view | **M** (markup pass) |
| G35 | Action bar | Content scrolls under bars, separated by the scroll edge effect ([Toolbars](https://developer.apple.com/design/human-interface-guidelines/toolbars), [Layout](https://developer.apple.com/design/human-interface-guidelines/layout)) | Glass, but the page stops at its top edge, because the bar's height changes with the inline error | **M** |
| G36 | Official site link | 44 × 44pt targets ([Accessibility](https://developer.apple.com/design/human-interface-guidelines/accessibility)) | A 22px inline text link | **K, fixed:** 44px tall, the text line unmoved |
| G37 | DetailError headings | Label the interface for VoiceOver ([Accessibility](https://developer.apple.com/design/human-interface-guidelines/accessibility)) | The page has no `h1`; the message is an `h2` | **M** |
| G38 | Register in the action bar | Controls in a bar are concentric with it (C7, 3b review: bar controls are capsules) | 6px corners | **K, fixed:** `--radius-bar-control`, the skeleton too |
| G39 | Back | Swipe from the leading edge goes back | Back button only | **O** (a gesture in a static prototype) |

**Already native on Race detail:** the back button names the destination ("‹ Discover"); one primary (Register, amber) per state, Try again on DetailError; errors in context (ContentUnavailableView for DetailError, the inline error beside Register for RegLinkError), no alert; the skeleton pulses and the back button works while loading; 44px Register and Dismiss; Dynamic Type sizes from the kit. "Dismiss" and "Try again" still need full accessible names (Deferred to Lesson 7).

**Discovery review (designer, 2026-10-22).** The photo stays (above). Two items go to the markup pass (Gap triage → Markup pass): "Couldn’t open the link" becomes a native alert, and the action caption becomes "Opens the race website". DESIGN.md now covers Race detail. Two kit fixes reach every screen:
- **Active filter chips:** iOS capsules (`--radius-filter-chip`, half the 32px height; C7, they sit in the controls bar) in a quiet `--bg-2` fill with no outline, the format’s name in sentence case (13px / 600), the Solar close-circle inside in `--text-2`; hover `--bg-3`. Format chips on cards keep 4px and uppercase. Contrast by the build: label 13.05:1 on `--bg-2` (12.17:1 on hover), the remove icon 6.01:1 (5.60:1). The old outline pair and the chip pairs over glass are gone (the capsule is opaque).
- **Empty and error states never framed.** The frame on `race-browse-error.html` (and `-empty`) was in the Map view: `.map-placeholder { box-shadow: inset 0 0 0 var(--border) var(--field-line); background: var(--map-water) }` (a 1px `#686E75` outline on the water, with the land masks over it) plus `.map-placeholder .state-message { background: var(--bg-1); border-radius: var(--radius-2); padding: var(--space-4) }` (a raised panel). Now, while the map holds a state, it drops its outline, water and land, and the state has no panel: it sits on the page as in List view. Checked on every painted empty and error state; the other screens' states are checked as their groups are painted. Before and after: `ui/review-step5.html`.

### Step 5, Archive and Infrastructure on the kit (2026-10-22)

The rest of step 5, in parallel, one subagent per group, with the Discovery rules. **Every screen is now on the kit:** all 35 pages link `ui/kit.css`, with no `<style>` block and no inline style (the map pins' `left`/`top` on Race browse stay, deferred). `wireframes/_wireframe/` untouched.

**Archive** (Log result, Race picker, Result detail; 10 pages). Markup touches: the busy and invalid hooks were already in the markup; Result detail `-loading` lost two inline skeleton widths. No shell (drill-downs and a sheet). In the kit, block `step 5 · Archive`:
- Log result's `header.top-bar` stays a bar (the large-title header grid no longer catches it).
- **Race picker is a sheet screen:** the page shows the sheet at its large detent over Log result under the scrim (it rendered blank before: the Filters sheet's off-screen start); its top bar is plain inside the sheet (no second glass); its search field is the search capsule with the Solar magnifier and the sheet boundary (C4, C7); the secondary "Type it in instead" is outlined on the sheet, as the Filters sheet's Cancel (a tonal button vanishes on `--bg-2`).
- The state message inside the sheet takes the sheet's gutter.

**Infrastructure** (Sign in / Sign up, Reset password, New password, Profile; 14 pages). Markup touches: `aria-busy="true"` on the busy submit button of the three gates' `-loading` pages (G26 spinner). Profile's header and tab bar already matched the shell; the gates are modals with top bars, no shell. In the kit, block `step 5 · Infrastructure`:
- A top bar that is a child of `body` (the gates) floats over the page, which starts below it and scrolls under its glass (before: 45px cut off at the bottom).
- `.view-toggle[hidden]` hides (it showed on `cause=confirm`).
- **Full-screen gate errors as ContentUnavailableView:** New password `-error?cause=expired` and Sign in `-error?cause=confirm` (the form is gone, so the inline error is the whole state and loses its `--error-bg` surface there only; inside a form, inline errors and form alerts keep theirs). A judgment call by the subagent, to review.
- Profile's load error centered with the gutter; spinners on "Sending…" and Profile "Saving…"; 44pt on small text links (G62); Profile rows 44px with a pop-up chevron (G65); the alert's focus ring no longer clipped.

**Checked by the lead:** `build_stand.py` passes (rules 1, 2, 3a; 94 solid pairs + 13 over glass; 176 of 176 tokens; four new pairs: the picker's search boundary, Profile's row chevron, and the error icon and Text 1 on the picker's sheet glass). Every empty and error state on every screen audited in the browser: none has an outline, border, shadow or surface around it except Race picker's own sheet (the screen itself). Amber per state: at most the one primary and the current tab (Profile `-error`: Try again + the tab). Shots of every state: `ui/review-step5.html`.

**HIG, the two groups:** Archive G40–G57, Infrastructure G60–G68, in the triage above. Two needed the designer, both decided 2026-10-23 (Step 5 review below): **G67** (the confirm alert's system radius and material, a value from Apple's kit) and **G68** (HIG shows Sign Out in red in Settings; the kit keeps coral only in the alert, decision 2026-10-19), out of scope until decided.

### Step 5 review (designer, 2026-10-23)

1. **G67, the confirm alert:** as iOS 26 alerts. The sheet's glass (`--glass-sheet`) over the scrim, with its blur and rim, and `--radius-alert` 34px **[?]** (provisional, like the sheet radius). The same contrast floor as the sheet glass, checked by the build over the worst case behind it: title and Cancel 12.13:1, body 5.59:1, Sign out (coral) 5.46:1. The buttons' hover takes `--bg-3`, one level above the raised glass.
2. **G68, Sign out:** coral (`--destructive`) in its Profile row too, as a destructive action. 6.74:1 on `--bg-1`, 5.87:1 on hover. Coral now means error *and* destructive: on Profile `-error?cause=save` the row's error icon and Sign out are both coral.
3. **Sign in, expired confirmation link, as a full-screen state:** agreed (kept as the subagent made it).
4. **Wireframe annotations:** to the markup pass (Gap triage → Markup pass): removed from the working pages, kept in `_wireframe/`.
5. **Race picker cards one level above the sheet:** `--bg-3` (the skeleton cards too). Pressed can't go a level higher, so it keeps the level and takes a 1px `--text-2` ring. The separation stays subtle: the card against the sheet is 1.12:1 (it was 1.10:1, darker than the sheet), because `--bg-3` is the top of the scale and only 2.3 L* above `--bg-2`. The meta on the card: `--text-2` on `--bg-3`, 5.60:1. **Then (designer, 2026-10-23): a hairline outline in `--line`**, no further background level. The hairline is decorative (the card's text identifies it; no 3:1 boundary needed): 1.22:1 against the sheet at rest, 1.09:1 against the card and against the sheet's worst case; checked by the build as an info pair.
6. **Log result while saving:** measured in Chromium at 390×844, with the locked fields filled in: every value renders in `--text-2` (`#A3A9B0`), not near-white; with nothing typed, what shows is the placeholder, also `--text-2`. Nothing to fix there. Safari paints disabled values with its own fill color, so the kit adds `-webkit-text-fill-color: currentColor` (no change in Chromium; Safari untested here).

### Consolidation (2026-10-23)

`ui/kit.css` after step 5 had two override blocks from the subagents and a few Discovery overrides beside the action bar. Each rule now lives with the component it overrides, so each component is defined in one place:
- **Top bar:** its placements on a gate (the body's own child, floating) and on a sheet (plain); Log result's `header.top-bar` no longer needs an override (the large-title rule is `header:not(.top-bar)`).
- **Modal sheet:** the sheet as a whole screen (Race picker), its scroll area and gutter.
- **Search field:** one component on the page and on a sheet (`.race-search`, `.sheet > form.search`), the sheet's boundary token as its only variant.
- **Race card:** the photo-less card and the picker's raised cards, with the card's states.
- **State message:** `.state-msg` (New password's expired link) is now the same component as `.state-message`; every placement (list, drill-down, Profile's section, the sheet, a gate) sits together; the expired confirmation link on Sign in, an inline error that is the whole screen, sits beside it.
- **Buttons:** the outlined secondary on a sheet; the busy secondary; the spinner rule covers the script-swapped labels ("Sending…", "Saving…").
- **Rows, the alert, text links:** the pop-up chevron and the 44pt select; the alert's focus ring; the 44pt targets on the inline links next to their shared look; the form alert's link in one rule.
- **Screen layouts:** drill-down, action bar and gate layouts next to `.phone-screen`.

**Removed** (no screen uses them): `.photo--high` and `--photo-focus-high`, `.screen-title`, the plain `.skeleton`. **Moved** to a new `concept/specimens.css`, linked by the stand and `first-screen.html` (no screen uses them, those two pages do): the `.btn` family, `.icon` in a button, the `.status` messages. The build checks the color rules over the kit, the stand and the specimens. No token is left unused.

**No visual change, checked by script** (Chromium, 390×844, animations frozen at frame 0, reduced motion, fresh URLs):
- **Screenshots:** 64 states of the 35 pages (every URL cause, Map view, the Filters sheet, the Sign out alert), plus `ui/kit.html` (1280 and 390 wide, full page), `ui/shell.html` and `first-screen.html`, before and after, diffed pixel by pixel. Two runs of the same build differ by at most 1/255 in a channel, only under the blur of glass bars, so "changed" means a channel delta over 1. Result: **no change** on any of them. The stand's own content changed (its row for the removed token, one sentence), so it was checked with the same content under both stylesheets: identical.
- **Computed styles:** every element and `::before`/`::after` on all 35 pages (2,491 boxes), old kit against merged kit. The only differences are on boxes that don't render: a hidden segmented control's margin, an `h2::before` that was `content: none` and is now not generated at all, and `gap: 0px` vs `normal` on Log result's flex top bar (both 0).
- **Interaction states:** all 60 `:hover`, `:active` and `:focus` rules compared declaration by declaration: identical.

**Loading Map view (designer, 2026-10-23):** the map surface pulses like the skeletons (C6), so a loading map no longer reads as an empty one. The kit adds `.map-placeholder[aria-busy="true"]` to the skeletons' pulse rule and to their reduced-motion rule, so it shares the same keyframes, 1.6s, ease and 0.55 low point, and stands still under `prefers-reduced-motion`. Checked in the browser: running with the skeleton bars' exact timing; opacity 0.55 at the low point; no animation under reduced motion; no other map (base, empty, error) animates. Every page and state at 390×844, frozen at frame 0: unchanged.

### Markup pass (2026-10-23)

Structure, controls and text on the working pages in `wireframes/` (never `_wireframe/`), every change on every state page of its screen. New or changed components went into `ui/kit.css`, `ui/kit.html` and `ui/inventory.md` first; text went through `microcopy.md` first (13 rows changed, 17 added: rows 535–551), then `voice.html` was regenerated.

**The decisions, as done:**
1. **Sort (G21):** one button, `.sort-toggle`, "Soonest first" with the Solar sort icon (`--icon-sort`, new, signed); it flips to "Latest first" and reverses the list. Its name reads "Sort: Soonest first". Disabled while loading; hidden in Map view.
2. **"My Results" → "Results"** on the tab (11 pages and the shell) and as Results list's title; the back buttons name it ("‹ Results"); `voice.md`'s Dictionary changed with it.
3. **Sport types (G19):** rows with a neutral checkmark at the trailing edge (`.row--check`; C4).
4. **Region (G17):** a row whose value opens the native menu (the `<select>` in a row, Profile's pop-up pattern, with its chevron).
5. **Dates (G18):** native compact pickers: the value on a pill in a row; the system's calendar when tapped.
6. **Sheet buttons (G12):** a top bar: Cancel leading, the title, Apply filters trailing (amber text, the sheet's one primary). The options are grouped rows on the level above the sheet (G20). No grabber (G14). Focus moves into the sheet, Escape closes it, focus returns to Filters, Tab stays inside (G32).
7. **Large title (G4):** a top bar floats over it (`.top-bar--large[data-collapse]`), transparent and empty at rest; once the h1 is mostly scrolled away it turns to glass and shows the small title. The same script gives Race detail and Result detail their inline title (G34, G53). Race browse's controls stick under the bar.
8. **Log result (G5):** a text button at the bar's trailing edge (`.bar-action`), amber; Text 1 when a state brings its own primary (`-error`).
9. **Results list empty:** the bar's Log result is hidden; only "Log your first result" stays.
10. **Race detail:** "Couldn’t open the link" is a native alert (`dialog.alert`, one action, Dismiss); the action bar is the scroll area's last child, sticky at its bottom, so its height never changes and content runs under its glass (G35; Result detail too, G54).
11. **Caption:** "Opens the race website — registration and payment happen there."
12. **The rest of the lists:** race names `h2` (G33, G48); the `-error` state heading is the page's `h1` where it has no other (G37, G55); short buttons carry their full accessible names (`voice.md` → Button); the date's day is its own `span.day` (no `::first-line`); the old drawn tab-bar SVGs, the bracketed annotations and the map pins' inline positions are gone (the kit places the pins without `!important`); the Results list empty icon keys on `.state-message--archive`; the saved confirmation and "Password changed" sit in a live region that exists from the start and are revealed a moment after load; "Saving…" on Log result and "Sending…" on Send a new link are buttons with `aria-busy` (the kit's spinner).

**Retired from the kit:** `.header-action`, `.sheet-handle`, `.sheet-actions`, the sheet's checkbox and field styles, `.save-progress`, the annotation-hiding rules. The old `.sort-control` and the drawn tab-icon sizing moved to `concept/specimens.css` (the stand and `first-screen.html` still show them).

**First screen, re-measured** (Chrome, 390 wide; before → after):

| Where | List starts | Clear of the tab bar | On screen, through the glass |
|---|---|---|---|
| Viewer (757px), no filters | 239 → **217** | 2 full, 1.7px to spare → **2 full + 6%, 24px to spare** | 2 full + 29% → 2 full + 39% |
| Viewer, two filters | 295 → 273 | 1 full + 75% → **1 full + 85%** | 2 full + 3% → 2 full + 13% |
| 390×844, no filters | 239 → 217 | 2 full + 35% → 2 full + 46% | 2 full + 69% → 2 full + 79% |
| 390×844, two filters | 295 → 273 | 2 full + 10% → 2 full + 20% | 2 full + 43% → 2 full + 53% |
| Results list (both) | 102 → 93 | 4 rows, all full | 4 rows |

Race browse gains 22px: the Sort button keeps its 44pt target inside the row's text height (the old `<select>` was 44px tall). Results list gains 9px: the title row no longer holds a 44px button. The overlay title bar adds nothing at rest. Attribute b holds with room now (24px instead of 1.7px).

**Checked:** the build (color rules 1, 2, 3a; 106 solid contrast pairs plus the glass pairs, among them Apply filters and Log result in amber over glass; 177 of 177 tokens signed). Every page and state at 390×844 before and after, plus scrolled states and the open sheet (72 shots): 45 changed, all intended; 27 unchanged, among them Race picker's cards (the day element renders exactly as the old `::first-line`) and Race detail's error page (`h2` → `h1` is invisible). Race picker's empty and error states changed because an old `.sheet h2` rule had leaked a 16px margin into their headings; with the sheet's rules rewritten, they match every other state. In the browser: the title collapses after scrolling and returns at the top on all five screens; focus moves into the sheet, Escape closes it and focus returns; the checkmark follows the sport filter; at most two amber elements per state. Before and after: `ui/review-markup.html`.

**Still open after the pass** (not among its decisions): G8 search pinned, G40–G45 Log result (modal, discard confirm, grouped form, pop-up Sport type, compact date, finish-time keyboard), G47 the linked race's checkmark in Race picker, G56 the long Open button label, G60–G61 the gates' confirm action and grouped forms. Result detail's "Couldn’t open the link" stays inline in its bar (the alert decision was for Race detail).

### Markup pass, round 2 (2026-10-23)

Same rules as round 1. Every change on every state page of its screen in `wireframes/` (never `_wireframe/`); the kit first; text through `microcopy.md` (38 rows changed, 5 added: 552–556) and `voice.md`, then `voice.html` regenerated.

1. **G8, search on scroll: no change** (designer). The search field scrolls away with the large title, as in iOS. Recorded in the triage.
2. **Log result, native (G40–G45):**
   - **G40:** a modal sheet over Results (the sheet-as-a-screen pattern Race picker uses; Race picker now stacks over it), with Cancel on the leading edge of its bar and Save on the trailing edge.
   - **G41:** Cancel with anything entered or a race linked opens an **action sheet** (new component: "This result isn’t saved yet.", **Discard result** in coral, **Keep editing** apart at the bottom, bold).
   - **G42:** a grouped form, `form.form-rows`. The catalog row is a navigation row, the race facts are one group, finish time and the official result link one group each (the link stacked). Hints are the groups' footers, errors sit under their rows, and an invalid row is ringed coral.
   - **G43, G44:** native pickers for Sport type (a menu row) and the race date (a compact picker on a pill).
   - **G45:** the numeric keypad for the finish time. The colons are put in as people type ("31248" → "3:12:48").
3. **G47:** Race picker marks the linked race with the filter rows' neutral checkmark and `aria-current`.
4. **G56:** Result detail's Open button reads "Open official result"; its accessible name carries the domain.
5. **G60–G61, the sign-in screens:** grouped forms, and the confirm action at the top bar's trailing edge (HIG Toolbars, Sheets). The label is short so it never meets the title: "Sign in", "Create", "Send", "Save". The accessible name starts with it ("Create account", "Send reset link", "Save new password"). While it works, the spinner alone. New password's save error now says "tap Save".
6. **Result detail's "Couldn’t open the link"** is a native alert, as on Race detail, with Dismiss and Try again (Try again re-runs the same check). Its action bar keeps one height.
7. **Alert copy:** "Couldn’t open the race website" / "The race website didn’t open. …" (Race detail); "Couldn’t open the official result" / "The official result on \<domain\> didn’t open. … paste it into your browser." (Result detail). To match, Result detail's caption is now "Opens the official timing site." (it still said "Opens in a new tab.").
8. **WCAG 2.5.3:** every accessible name starts with its control's visible label: "Try again, loading races" (and the other Try agains), "Soonest first, sort order" (set by script when it flips), "HYROX, remove filter", "London, HYROX London, 6 Dec 2026" (the map pins), the Open button, the bar actions.
9. **"My Results" → "Results"** in `sitemap.md`, `flows.md` and `ia.html` (each notes the rename, dated), and in CLAUDE.md's IA summary.

**Kit:** new: the action sheet, form rows (`.form-rows`, `.row--stacked`, `.row--nav`, errors under rows, the invalid row), the linked race's checkmark, the busy bar action as the spinner alone. Retired: `.field`, `.hint`, `.field-hint`, `.catalog-row`, `.dismiss`, `.alert-btn`, the inline error's action row.

**Checked:**
- **Build:** passes (color rules 1, 2, 3a; 106 solid pairs plus the glass pairs; 177 of 177 tokens). Every new color use is an existing pair: coral on the sheet's glass, Text 1 and Text 2 on the raised rows, Text 2 on the sheet.
- **Screenshots:** 75 states at 390×844 before and after. 31 changed, all in scope: Log result, the sign-in screens, Race detail's alert, Result detail, Race picker's linked race. The other 44 are unchanged.
- **First screen:** unchanged from round 1. Nothing above either list moved: list top 217 (Race browse), 93 (Results).
- **In the browser:** Cancel with nothing entered leaves; with data it asks, Keep editing returns, Discard result leaves; "31248" becomes "3:12:48"; Result detail's alert opens, describes its domain and dismisses; at most two amber elements in every state.
- **Names (WCAG 2.5.3):** 189 controls on 43 page states start with their visible labels, confirmed against Chromium's computed names for the short bar actions and the Open button.
- **Review page:** before and after at `ui/review-markup-2.html`.

### Race picker pushed (designer, 2026-10-24)

Race picker is no longer a modal sheet over Log result. It's a screen pushed inside Log result's navigation, as picking a value in iOS Settings:
- **The screen:** full-screen with square corners, on the page ground. Its top bar has "‹ Log result" and the title "Find a race", and no Cancel.
- **Choosing:** tapping a race goes back to Log result with it filled in (unchanged). The back button returns with every typed value.

All four state pages changed. `flows.md` changed its edge from "cancels — form unchanged" to "goes back — form unchanged", and `ia.html` carries the same edge. `sitemap.md`, `_conventions.md` ("Pickers are pushed screens"), `_screens.md`, CLAUDE.md and `microcopy.md` row 265 ("Cancel" → the back button "Log result") are updated too.

**Kit:** the picker-only sheet styles are removed, since nothing else used them:
- the raised cards and their hairline;
- the outlined secondary on a sheet;
- the search field's sheet variant.

The search field's second placement is `.phone-screen > form.search`, and the list takes the page gutter. The sheet-as-a-screen rules stay, because Log result uses them. The build dropped four contrast pairs that described the picker on the sheet and added the checkmark on a page card (control tint on `--bg-1`): 104 pairs.

**Checked:**
- **Screenshots:** all 75 states against round 2. Only the six Race picker states changed.
- **In the browser:** "‹ Log result" goes back with the typed values; tapping UTMB returns to Log result with the race linked and the finish time kept; there is no Cancel and no corner radius.
- **Review:** before and after at `ui/review-markup-2.html` → Race picker pushed.


### Overflow fix: the controls bar (designer report, 2026-10-24)

**The defect:** Race browse `-empty` at 390 wide, with its three active filters, overflowed. The List/Map control was pushed off-screen (only "List" showed), the third chip was clipped mid-text ("1 Oct – 30 No…"), "Clear all filters" was cut to "Clear", and the screen scrolled sideways.

**The cause:** `.controls` is a grid whose single column was `auto`. An auto column grows to its content's min-content width, and the chips row's min-content width is every chip side by side: 437px with three chips, 953px with five. The column widened, and it carried `.control-row` (Filters + List/Map) and `.chips-bar` past the screen with it. The chips row's own `overflow-x: auto` never got the chance to scroll, because its box was never narrower than its content.

**The fix, in the kit (`ui/kit.css`), no page changed:**
- `.controls`: `grid-template-columns: minmax(0, 1fr)`. The column is the screen's width, never its content's.
- `.control-row .view-toggle`: `flex: none`. List/Map keeps its full size and never shrinks.
- `.control-row .filters-trigger`: `flex: 1 1 0; min-width: min-content; white-space: nowrap`. Filters takes the remaining width and can shrink, but never below its label ("Filters · 5" stays whole at 320).
- The chips row (unchanged): one row, `flex: 1; min-width: 0; overflow-x: auto`, fading over its last 24px. Chips never shrink or ellipsize; the only cut is at the scroll edge, under the fade, which is the scroll affordance.

**"Clear all filters": pinned at the end of the row, not on its own line.** Two reasons:
- **iOS pattern:** a horizontally scrolling row of tokens is the iOS filter-bar idiom, and an action that acts on the whole row belongs on that row, at its trailing end, where it stays put while the tokens scroll. **[?]** Not checked against a specific iOS 26 screen or Mobbin reference.
- **Height:** a line of its own adds 44px to a sticky bar on every filtered state, and attribute b (two full race cards on the first screen) holds with 24px to spare.

**Why no earlier check caught it:**
- **Where the overflow lived:** it scrolled inside `.phone-screen`, while the document stayed at 390. The document-level checks saw nothing.
- **What was shot:** the screenshot runs used `race-browse-empty.html?sport=hyrox` (one chip), never the page's own three filters, and only ever at 390.
- **No width check:** nothing failed on overflow; it was left to eyes on screenshots.

**The new check:** `scripts/check_overflow.mjs`, run by `build_stand.py` on every build (the build stops on a failure; it is skipped with a message only when Node or Chrome is missing). It opens every `wireframes/*.html` state in headless Chrome at 390×844 and 320×568 (iPhone SE), Race browse with 0, 1, 2, 3 and 5 active filters using the longest chip texts in `microcopy.md` (North America, DEKA / functional fitness, a date range across two years, a search chip), in List, Map and with the Filters sheet open, plus the sign-out alert and the discard confirm: 206 states. It fails when any element reaches past either screen edge, or any element other than the chips row scrolls sideways. Before the fix: 64 of 206 states failed. After: none.

**Checked:** Race browse in every state, 98 shots before and after (390 and 320, 0–5 filters, List / Map / sheet). The states with 2 or more filters (and `-empty`'s own three) changed; 0 and 1 filter, error and scrolled are identical or differ by glass-blur noise (channel delta 1). Review: `ui/review-overflow.html`.
