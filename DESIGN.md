---
name: Onrace
description: A race calendar and personal results archive for hybrid athletes. Direction A, "Podium".
colors:
  bg-bar: "#0F1114"
  bg-0: "#131518"
  bg-1: "#1D2024"
  bg-2: "#272B30"
  bg-3: "#2C3035"
  line: "#31363C"
  field-line: "#686E75"
  text-1: "#F4F5F6"
  text-2: "#A3A9B0"
  text-disabled: "#6B7178"
  chip-text: "#BFC4CA"
  accent: "#F5B649"
  accent-hover: "#FFC46A"
  on-accent: "#131518"
  error: "#EE8B84"
  error-bg: "#3A2F31"
  scrim: "rgba(0, 0, 0, 0.6)"
typography:
  title:
    fontFamily: "Schibsted Grotesk, Hanken Grotesk, sans-serif"
    fontSize: "38px"
    fontWeight: 800
    lineHeight: 1
    letterSpacing: "-0.03em"
  finish-time:
    fontFamily: "Schibsted Grotesk, Hanken Grotesk, sans-serif"
    fontSize: "32px"
    fontWeight: 800
    lineHeight: 1
    letterSpacing: "-0.03em"
  date-day:
    fontFamily: "Schibsted Grotesk, Hanken Grotesk, sans-serif"
    fontSize: "30px"
    fontWeight: 800
    lineHeight: 1
    letterSpacing: "-0.03em"
  item:
    fontFamily: "Hanken Grotesk, sans-serif"
    fontSize: "17px"
    fontWeight: 600
    lineHeight: 1.2
  body:
    fontFamily: "Hanken Grotesk, sans-serif"
    fontSize: "15px"
    fontWeight: 400
    lineHeight: 1.45
  button:
    fontFamily: "Hanken Grotesk, sans-serif"
    fontSize: "15px"
    fontWeight: 600
    lineHeight: 1
  meta:
    fontFamily: "Hanken Grotesk, sans-serif"
    fontSize: "14px"
    fontWeight: 400
    lineHeight: 1.45
  proof:
    fontFamily: "Hanken Grotesk, sans-serif"
    fontSize: "13px"
    fontWeight: 400
    lineHeight: 1.45
  label:
    fontFamily: "Hanken Grotesk, sans-serif"
    fontSize: "11px"
    fontWeight: 600
    lineHeight: 1
    letterSpacing: "0.07em"
  tab-label:
    fontFamily: "Hanken Grotesk, sans-serif"
    fontSize: "11px"
    fontWeight: 600
    lineHeight: 1.45
rounded:
  radius-1: "4px"
  radius-2: "6px"
  radius-3: "12px"
spacing:
  space-1: "4px"
  space-2: "8px"
  space-3: "12px"
  space-4: "16px"
  space-5: "20px"
  space-6: "24px"
  space-7: "32px"
  space-8: "48px"
  space-9: "64px"
components:
  button-primary:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-accent}"
    typography: "{typography.button}"
    rounded: "{rounded.radius-2}"
    padding: "0 20px"
    height: "44px"
  button-primary-hover:
    backgroundColor: "{colors.accent-hover}"
    textColor: "{colors.on-accent}"
  button-secondary:
    backgroundColor: "{colors.bg-2}"
    textColor: "{colors.text-1}"
    typography: "{typography.button}"
    rounded: "{rounded.radius-2}"
    padding: "0 20px"
    height: "44px"
  button-secondary-hover:
    backgroundColor: "{colors.bg-3}"
    textColor: "{colors.text-1}"
  button-tertiary:
    textColor: "{colors.text-1}"
    typography: "{typography.meta}"
    padding: "0 4px"
    height: "44px"
  button-tertiary-hover:
    textColor: "{colors.text-2}"
  format-chip:
    backgroundColor: "{colors.bg-2}"
    textColor: "{colors.chip-text}"
    typography: "{typography.label}"
    rounded: "{rounded.radius-1}"
    padding: "0 8px"
    height: "24px"
  filter-chip:
    textColor: "{colors.text-1}"
    typography: "{typography.label}"
    rounded: "{rounded.radius-1}"
    padding: "0 12px"
    height: "32px"
  search-field:
    backgroundColor: "{colors.bg-1}"
    textColor: "{colors.text-1}"
    typography: "{typography.body}"
    rounded: "{rounded.radius-2}"
    padding: "0 12px 0 42px"
    height: "44px"
  sheet-field:
    backgroundColor: "{colors.bg-0}"
    textColor: "{colors.text-1}"
    typography: "{typography.body}"
    rounded: "{rounded.radius-2}"
    padding: "0 12px"
    height: "44px"
  segmented-track:
    backgroundColor: "{colors.bg-2}"
    rounded: "{rounded.radius-2}"
    padding: "4px"
  segment:
    textColor: "{colors.text-2}"
    rounded: "{rounded.radius-1}"
    padding: "0 16px"
    height: "36px"
  segment-pressed:
    backgroundColor: "{colors.bg-3}"
    textColor: "{colors.text-1}"
  race-card:
    backgroundColor: "{colors.bg-1}"
    rounded: "{rounded.radius-2}"
    padding: "8px"
  date-tile:
    backgroundColor: "{colors.bg-2}"
    textColor: "{colors.text-2}"
    typography: "{typography.proof}"
    rounded: "{rounded.radius-1}"
    padding: "12px 4px"
    width: "68px"
  result-row:
    backgroundColor: "{colors.bg-1}"
    rounded: "{rounded.radius-2}"
    padding: "12px 16px 16px"
  saved-status:
    backgroundColor: "{colors.bg-1}"
    textColor: "{colors.text-1}"
    typography: "{typography.meta}"
    rounded: "{rounded.radius-2}"
    padding: "12px 16px"
  tab-bar:
    backgroundColor: "{colors.bg-bar}"
    textColor: "{colors.text-2}"
    typography: "{typography.tab-label}"
    height: "64px"
  tab-current:
    textColor: "{colors.accent}"
  filters-sheet:
    backgroundColor: "{colors.bg-1}"
    rounded: "{rounded.radius-3}"
    padding: "8px 16px 0"
  map-pin-label:
    backgroundColor: "{colors.bg-2}"
    textColor: "{colors.text-1}"
    typography: "{typography.tab-label}"
    rounded: "{rounded.radius-1}"
    padding: "0 8px"
    height: "22px"
---

# Design System: Onrace

Documented on 2026-10-18 (Lesson 7, step 1) from the two painted screens and all their states:
- `wireframes/race-browse.html`, `-empty`, `-error`, `-loading`; the filtered state (`?sport=hyrox&sport=marathon`); the Filters sheet open; the Map view
- `wireframes/results-list.html`, `-empty`, `-error`, `-loading`; the saved state (`?saved=`)

Every value comes from `concept/tokens.css`, `concept/map.css` and `concept/components.css`, and was checked against the computed styles of the rendered screens at 390×844. The screens are the source of truth. The artifact pages (`concept.html`, `directions*.html`, `voice.html`, `ia.html`, the workspace shell) are not the product, and nothing here describes them.

The other eight screens are still grayscale wireframes. They take this system in Lesson 7.

## Overview

**Creative North Star: "Podium"**

A graphite stand with one amber light on it. The ground is dark but never black, and it gets lighter in small, even steps from the tab bar up to the raised controls. Type and contrast carry the energy, not color: the screen title and the key numbers (finish time, date day) sit in a heavy display face, and everything else is a quiet text face in sentence case. The amber accent appears once or twice per screen, only where you can act or where you are.

The product is an iPhone-shaped app (390px wide) in Operate mode: athletes scan a calendar of races and pull up their own results as proof. So hierarchy beats decoration. On a race card the date and the place lead and the photo is a black-and-white band, not a poster. On a result row the finish time is the loudest thing. The proof line under it says where the result comes from ("Self-reported · via results.hyrox.com"). It never stamps the result as verified.

What the screens refuse: aggressive "energy" red, pure black with one hot accent, one heavy condensed face for everything, no radius at all, per-format colors, success-green on results, and the artifact pages' values (`#0b0c0e`, the `#ff4d2e` family).

**Key Characteristics:**
- Dark with depth: five background levels between L* 4.99 and 19.67, all near-neutral (C* ≤ 3.87).
- One scarce accent, sodium amber `#F5B649`: the primary action and the current tab, and nothing else.
- Two faces: Schibsted Grotesk 800 for the title and key numbers, Hanken Grotesk 400/600 for everything else.
- Small radii: 4px inside, 6px outside; 12px only on the Filters sheet's top corners.
- Flat surfaces. The one shadow belongs to the Filters sheet.
- Neutral metadata: format chips, filter chips, map pins, the saved confirmation and every pressed state stay gray.
- Black-and-white photos, 3:1, inset in the race card.
- Solar bold icons, drawn as CSS masks in the color of their text.

## Colors

A graphite ramp, two text grays, one amber, and a soft coral for errors only.

### Primary
- **Sodium Amber** (`#F5B649`, `--accent`): the fill of the screen's one primary button (Log result in the Results list header; Change filters on Race browse `-empty`; Try again on both `-error` pages; Apply filters in the Filters sheet) and the icon and label of the current tab. On-accent text `#131518` is 10.16:1 on it. The current tab label is 10.51:1 on the tab bar.
- **Amber, hover** (`#FFC46A`, `--accent-hover`): the primary button under the pointer. Never at rest.
- **On Accent** (`#131518`, `--on-accent`): text and icons on the amber. The same hex as `--bg-0`.

### Neutral
- **Tab-bar Black** (`#0F1114`, `--bg-bar`, L* 4.99): the tab bar (the frame), and the water on the static map.
- **Graphite Ground** (`#131518`, `--bg-0`, L* 6.69): the page, the sticky controls bar, the fields inside the Filters sheet, an unchecked checkbox.
- **Graphite Surface** (`#1D2024`, `--bg-1`, L* 12.10): race cards, result rows, the search field, the saved confirmation, the Filters sheet, land on the map.
- **Graphite Raised** (`#272B30`, `--bg-2`, L* 17.33): the secondary button, the format chip, the date tile, the List/Map track, map pin labels, skeleton bars.
- **Graphite Pressed** (`#2C3035`, `--bg-3`, L* 19.67): hover, open and pressed fills on raised controls (secondary hover, the pressed List/Map segment, Filters while its sheet is open, pin hover) and the coastlines and borders on the map. Never at rest on a card.
- **Hairline** (`#31363C`, `--line`): dividers only (below the controls, above the tab bar, above the sheet footer, before "Newest first"). Never a fill.
- **Field Line** (`#686E75`, `--field-line`): the 1px boundary of inputs, the pressed segment's outline, the hover ring on cards, the map frame, the sheet handle. 3:1 against `--bg-0` and `--bg-1`.
- **Chalk** (`#F4F5F6`, `--text-1`): titles, race names, finish times, date days, body text, links, focus rings, the dot on a map pin, a checked checkbox. 16.76:1 on `--bg-0`.
- **Ash** (`#A3A9B0`, `--text-2`): meta (date month and year, location, counts, proof line), placeholder text, inactive tabs, sheet labels, the active filter chip's outline. 6.90:1 on `--bg-1`.
- **Chip Text** (`#BFC4CA`, `--chip-text`): the format chip's label. 8.11:1 on `--bg-2`.
- **Disabled** (`#6B7178`, `--text-disabled`): a disabled sort control only. Never content.

### States
- **Soft Coral** (`#EE8B84`, `--error`): the one error icon before an error heading. Not the banned aggressive red.
- **Coral Wash** (`#3A2F31`, `--error-bg`): the error status surface (defined; not shown on these two screens).
- **Scrim** (`rgba(0, 0, 0, 0.6)`, `--scrim`): behind the open Filters sheet.

`--success` and `--success-bg` exist in `tokens.css` for the stand's specimen only. No product screen uses them.

### Named Rules
**The Two Lights Rule.** The amber appears at most twice on a screen: the current tab, plus the one primary action if the screen has one. Race browse at rest has only the tab. Every other active state stays neutral: the active filter chip is an outline, the pressed segment is `--bg-3`, a checked checkbox is `--text-1`, the focus ring is `--text-1`.

**The Stated, Not Stamped Rule.** No green, no check icon and no "verified" mark on any result or anywhere on Results list. The saved confirmation is `--bg-1` with a gray save glyph.

**The Depth of Dark Rule.** Every background level has L* between 4.5 and 20 and C* ≤ 6, and each level is at least 1.5 L* above the one below it. `#000` and `#0B0C0E` are out.

## Typography

**Display Font:** Schibsted Grotesk 800 (fallback Hanken Grotesk, sans-serif)
**Body Font:** Hanken Grotesk 400 and 600 (fallback sans-serif)

**Character:** A bold, tight display grotesque for the three things worth shouting (the screen title, the finish time, the date day) against a clean, technical text grotesque for everything else. Each page loads the fonts from its `<head>` (preconnect plus the Google Fonts stylesheet), not from CSS.

### Hierarchy
- **Title** (Schibsted 800, 38px, line-height 1, -0.03em): the screen's `h1` ("Discover", "My Results").
- **Finish time** (Schibsted 800, 32px, line-height 1, -0.03em): the finish time on a result row. Proportional figures, `--text-1`, never the accent.
- **Date day** (Schibsted 800, 30px, line-height 1, -0.03em): the day on a race card's date tile (the tile's `::first-line`).
- **Item** (Hanken 600, 17px, line-height 1.2): race names on cards and rows, empty and error headings, the sheet's heading.
- **Body** (Hanken 400, 15px, line-height 1.45): base text, the search field, sheet checkbox labels and fields.
- **Button** (Hanken 600, 15px, line-height 1): primary and secondary buttons, sheet buttons.
- **Meta** (Hanken 400, 14px, line-height 1.45): location, counts ("**7** upcoming races", the number in 600), the sort label, result dates, state body text, the tertiary "Clear all filters". The List/Map segments and the sort value use 14px at 600.
- **Proof** (Hanken 400, 13px, line-height 1.45): the proof line; the month and year under the date day (line-height 1.2 there).
- **Label** (Hanken 600, 11px, 0.07em, UPPERCASE by CSS only): format chips and active filter chips. The markup keeps the format's own name ("Half marathon").
- **Tab label** (Hanken 600, 11px, line-height 1.45, sentence case): tab labels and map pin labels.

There is no 700. `strong` and `b` render at 600, because Hanken loads only 400 and 600.

### Named Rules
**The Three Shouts Rule.** The display face is used for the screen title, the finish time and the date day, and nowhere else. Race names, chips, buttons, tabs and meta are the text face.

**The Name Stays Rule.** Uppercase is `text-transform` only. The format name in the markup never changes.

## Layout

- **Screen:** 390px wide (`--screen-w`), one column, scrolling inside `.phone-screen` with 64px of bottom padding for the tab bar.
- **Gutter:** 16px (`--space-4`) on every side of the content.
- **Header:** `8px 16px 4px`, gap 12px. On Results list the title and the Log result button share a row (`1fr auto`).
- **Controls (Race browse):** sticky at the top on `--bg-0`, padding `12px 16px`, a hairline under it. The Filters button fills the row; the List/Map track sits at its end. Active filter chips scroll in one row, which fades out over its last 24px; "Clear all filters" sits after it.
- **Count row:** padding `12px 16px`, count on the left, sort control (Race browse) or nothing (Results list) on the right.
- **Lists:** cards and rows stacked with a 12px gap.
- **Race card:** an 8px inset; the photo band (3:1, 114px tall at 342px); below it a grid of a 68px date column and the text column, 12px apart.
- **First screen at 390×844:** 2 full race cards plus 39% of the third with no filters; 2 full plus 13% with two filters on.
- **Tab bar:** fixed to the bottom, 64px tall, three equal columns, 44px targets.
- **Filters sheet:** slides up over a scrim, at most 75% of the screen, with a sticky footer (Cancel and Apply filters, 12px apart) above a hairline.
- **Map view:** a frame that fills the space below the controls, with 16px gutters. Pins sit on each race's real latitude and longitude; labels that would collide move above or below on a leader line.
- **Targets:** 44px minimum (`--target`). The 32px filter chips and the tertiary link extend to 44px with an invisible tap area.
- **Running text:** 65ch maximum (`--measure`).

Spacing scale: 4, 8, 12, 16, 20, 24, 32, 48, 64.

## Elevation & Depth

Flat by default. Depth comes from tonal layering: the tab bar (`--bg-bar`) under the page (`--bg-0`) under cards (`--bg-1`) under raised controls (`--bg-2`) under pressed fills (`--bg-3`). Cards have no shadow and no border at rest. On hover a card gets a 1px inset ring in `--field-line`.

### Shadow Vocabulary
- **Sheet** (`box-shadow: 0 12px 32px -12px rgba(0, 0, 0, 0.6)`, `--shadow-sheet`): the Filters sheet only, the one surface that floats. A `rgba(0, 0, 0, 0.6)` scrim dims the page behind it.

### Named Rules
**The One Float Rule.** Only a sheet casts a shadow. Everything else is a tone step.

## Shapes

Slightly rounded, never pills, never sharp.
- **4px** (`--radius-1`), inner shapes: the photo inside a card, the date tile, format and filter chips, List/Map segments, skeleton bars, map pin labels, checkboxes, the sheet handle.
- **6px** (`--radius-2`), outer shapes: cards, result rows, buttons, the search field, sheet fields, the List/Map track, the saved confirmation, the map frame.
- **12px** (`--radius-3`): the Filters sheet's top corners only. `tokens.css` and the stand label this radius "stand panels only"; the sheet uses it anyway. This waits for the designer's decision (see the concept.md diff in Lesson 7, step 1).
- **Circles:** the map pin dot only.
- **Borders** are drawn as 1px inset box-shadows (`--border`), so they never change a box's size.

## Components

### Buttons
Exactly one filled button per screen.
- **Shape:** 6px radius, 44px minimum height, `0 20px` padding, 15px / 600, 8px gap to an 18px icon.
- **Primary:** `--accent` fill, `--on-accent` text. Hover `--accent-hover`. Pressed moves down 1px. Background and transform ease over 160ms (`--ease-out`, `cubic-bezier(0.2, 0.8, 0.2, 1)`); 0ms under reduced motion.
- **Secondary:** `--bg-2` fill, `--text-1` text, hover `--bg-3`. Filters on Race browse (with the Solar filters icon, `--bg-3` while its sheet is open), Clear all filters in an empty state, Cancel in the sheet.
- **Tertiary:** a text link, 14px / 400, `--text-1`, 1px underline 4px below, hover `--text-2`. "Clear all filters" in the chips row.
- **Stepping down:** when a state block brings its own primary (Log your first result, Try again), the Results list header's Log result becomes secondary, so the screen keeps one filled button.
- **Disabled:** `--bg-2` fill, `--text-disabled` text. **Busy:** same fill, present-tense verb ("Saving…").

### Chips
- **Format chip** (metadata): `--bg-2` fill, `--chip-text`, 4px radius, 24px tall, `0 8px`, 11px / 600 uppercase, 0.07em. The same for every format: no per-format color.
- **Active filter chip** (a removable state): transparent with a 1px `--text-2` outline, `--text-1` label, 32px tall, `0 12px`, 4px radius, and a 15px Solar close-circle in `--text-2`.

### Cards / Containers
- **Race card:** `--bg-1`, 6px radius, 8px padding, flat. The whole card is one link, photo included. Inside it: a black-and-white photo (`grayscale(1) contrast(1.12) brightness(0.85)`) at 3:1 with a 4px radius; then the date tile (68px wide, `--bg-2`, 4px radius, `12px 4px` padding, the day in Schibsted 30px `--text-1` over the month and year in 13px `--text-2`); then the race name (17px / 600), the format chip, and the location (14px `--text-2` with a 15px Solar map-point icon).
- **Result row:** `--bg-1`, 6px radius, `12px 16px 16px` padding, 8px gaps. The race name on the left and the finish time (Schibsted 32px) on the right, sharing a baseline; then the format chip and the date (14px `--text-2`); then the proof line (13px `--text-2`, one 15px Solar link icon, wraps anywhere).
- **Saved confirmation:** `--bg-1`, 6px radius, `12px 16px`, 14px `--text-1` with the race name in 600, and an 18px Solar save glyph in `--text-2`. Never green, never a check.
- **Skeletons (loading):** `--bg-2` bars with a 4px radius, in the exact shape of the card or row they stand for. The finish-time bar is 32px tall, so nothing shifts. No spinner, no shimmer.

### Inputs / Fields
- **Search field:** `--bg-1`, 6px radius, 44px tall, a 1px `--field-line` inset boundary, an 18px Solar magnifier in `--text-2`, placeholder in `--text-2`. Hover: the boundary turns `--text-2`. Focus: a 2px `--text-1` outline replaces it.
- **Sheet select and date fields:** `--bg-0`, 6px radius, 44px tall, 1px `--field-line`, 15px text. The select has a 15px Solar chevron; the date field has an 18px Solar calendar instead of the browser's glyph.
- **Checkbox:** 18px, 4px radius, `--bg-0` with a 1px `--field-line` boundary; checked fills `--text-1` with a `--bg-0` tick. Never the accent.
- **Sort control:** borderless, `--text-1` 14px / 600 with a `--text-1` chevron; the label "Sort:" in `--text-2`.
- **Focus (everything):** a 2px `--text-1` outline, 2px offset. Never the accent.

### Navigation
- **Tab bar:** `--bg-bar` with a hairline on top, 64px, three tabs (Discover, My Results, Profile). Each has a 26px Solar icon (compass, stopwatch, user) over an 11px / 600 label. Inactive: `--text-2`. Current: `--accent`, icon and label.
- **List / Map segmented control:** a `--bg-2` track with 4px padding and a 6px radius; segments are 36px (44px tap area), 14px / 600, `--text-2`. The pressed segment is `--bg-3`, `--text-1`, with a 1px `--field-line` outline.

### Empty and error states
A message block, left-aligned, 24px of vertical padding: a 17px / 600 heading, 14px `--text-2` body (65ch max), then actions in the button hierarchy, 12px apart. An error heading gets one 18px Solar danger-circle in `--error`. Nothing else turns red.

### Filters sheet (signature)
`--bg-1`, 12px top corners, the sheet shadow, over the scrim. It slides up over 250ms (`--dur-sheet`, `--ease-out`; 0ms under reduced motion). A 32×4px handle in `--field-line`; a 17px / 600 heading; 14px `--text-2` labels; fields and checkboxes as above; a sticky footer with Cancel (secondary) and Apply filters (the sheet's one primary), each half the width.

### Static map (signature)
A frame in `--bg-bar` (water) with a 1px `--field-line` boundary and a 6px radius. Natural Earth land is masked in `--bg-1`, coastlines and borders in `--bg-3`. Pins: a 10px `--text-1` dot ringed in water color on the real coordinate, and a 22px `--bg-2` label (11px / 600, `--text-1`, 4px radius) joined by a 1px `--text-2` leader line. Hover lifts the label to `--bg-3`. No accent anywhere on the map. The caption is 11px `--text-2`.

## Do's and Don'ts

### Do:
- **Do** keep the amber to the one primary button and the current tab: at most two uses per screen.
- **Do** make the finish time the loudest thing on a result row, through Schibsted 800 at 32px in `--text-1`, not through color.
- **Do** lead a race card with the date tile (day 30px over month and year 13px) beside the name, chip and place.
- **Do** show every photo in black and white (`--photo-filter`), inset at 3:1 with a 4px radius.
- **Do** state proof as its own 13px `--text-2` line with one link icon: "Self-reported · via \<domain\>".
- **Do** step a secondary action up or down so the screen keeps exactly one filled button.
- **Do** take every value from `tokens.css`. Pages and `components.css` hold no raw values.
- **Do** draw icons as Solar bold masks in the color of their text: 15px in meta, 18px in buttons and fields, 26px in the tab bar.
- **Do** keep 44px targets, a 2px `--text-1` focus ring, and 0ms motion under `prefers-reduced-motion`.

### Don't:
- **Don't** put the amber on a finish time, a chip, a filter chip, a count, a link, a focus ring, an icon in content, a status, or the map.
- **Don't** use green, a check icon or the word "verified" on a result or on Results list.
- **Don't** give formats their own colors. Every format chip is the same neutral chip.
- **Don't** use pure `#000`, `#0B0C0E`, the `#ff4d2e` family, `src/style.css` or the wireframe grays.
- **Don't** use aggressive "energy" red. Errors are soft coral `#EE8B84`, on the icon only.
- **Don't** set race names, chips, buttons or tabs in the display face, or use one heavy condensed face for everything.
- **Don't** drop the radius to 0 or round into pills.
- **Don't** give cards a shadow or a border at rest.
- **Don't** use `--line` or `--field-line` as a fill.
- **Don't** use tabular figures on finish times: Schibsted spaces the colons wide ("24 : 36").

## Sources

- [`concept/concept.md`](concept/concept.md): the rules and every decision behind these values (Designer's taste, Hierarchy rules, Color rules, race card anatomy, Results list details, Map, Deferred to Lesson 7).
- [`concept/references.md`](concept/references.md): the references, the techniques taken and the anti-references, and the photo log.
- Values: [`concept/tokens.css`](concept/tokens.css), [`concept/map.css`](concept/map.css), [`concept/components.css`](concept/components.css). Signed reasons for each token: the stand, [`concept/concept.html`](concept/concept.html).
