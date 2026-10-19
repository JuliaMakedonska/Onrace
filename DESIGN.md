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
  field-line-sheet: "#757B82"
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
  glass-bar: "color-mix(in srgb, #0F1114 85%, transparent)"
  glass-ground: "color-mix(in srgb, #131518 85%, transparent)"
  glass-sheet: "color-mix(in srgb, #272B30 90%, transparent)"
typography:
  title:
    fontFamily: "Schibsted Grotesk, Hanken Grotesk, sans-serif"
    fontSize: "34px"
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
    fontSize: "15px"
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
  radius-sheet: "38px"
  radius-bar-control: "22px"
  radius-bar-inner: "18px"
  radius-avatar: "50%"
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
    rounded: "{rounded.radius-bar-control}"
    padding: "4px"
  segment:
    textColor: "{colors.text-2}"
    rounded: "{rounded.radius-bar-inner}"
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
    backgroundColor: "{colors.glass-bar}"
    rounded: "32px"
    textColor: "{colors.text-2}"
    typography: "{typography.tab-label}"
    height: "64px"
  tab-current:
    textColor: "{colors.accent}"
  filters-sheet:
    backgroundColor: "{colors.glass-sheet}"
    rounded: "{rounded.radius-sheet}"
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

Every value comes from `ui/kit.css` and `ui/map.css` (until Lesson 7 step 3a, `concept/tokens.css`, `concept/map.css` and `concept/components.css`), and was checked against the computed styles of the rendered screens at 390×844. The screens are the source of truth. The artifact pages (`concept.html`, `directions*.html`, `voice.html`, `ia.html`, the workspace shell) are not the product, and nothing here describes them.

The other eight screens are still grayscale wireframes. They take this system in Lesson 7.

**Updated 2026-10-19 (Lesson 7, step 3b), the native iOS pass.** The kit changed on purpose: glass bars and sheet (C1), the HIG type mapping (C3), a neutral control tint (C4), a skeleton pulse (C6), concentric controls in bars (C7), and the Kit (CSS) gaps (G1, G2, G6, G7, G10, G11, G13, G16, G22, G23, G25–G29). The sections below describe the screens after that pass. Values marked **[?]** (glass opacity margins, blur, rim, sheet radius, the sheet's top gap) are provisional: Apple's iOS 26 design kit wasn't read; the one Apple number used is HIG Materials' 35% dimming layer, as a floor.

## Overview

**Creative North Star: "Podium"**

A graphite stand with one amber light on it. The ground is dark but never black, and it gets lighter in small, even steps from the tab bar up to the raised controls. Type and contrast carry the energy, not color: the screen title and the key numbers (finish time, date day) sit in a heavy display face, and everything else is a quiet text face in sentence case. The amber accent appears once or twice per screen, only where you can act or where you are.

The product is an iPhone-shaped app (390px wide) in Operate mode: athletes scan a calendar of races and pull up their own results as proof. So hierarchy beats decoration. On a race card the date and the place lead and the photo is a black-and-white band, not a poster. On a result row the finish time is the loudest thing. The proof line under it says where the result comes from ("Self-reported · via results.hyrox.com"). It never stamps the result as verified.

What the screens refuse: aggressive "energy" red, pure black with one hot accent, one heavy condensed face for everything, no radius at all, per-format colors, success-green on results, and the artifact pages' values (`#0b0c0e`, the `#ff4d2e` family).

**Key Characteristics:**
- Dark with depth: five background levels between L* 4.99 and 19.67, all near-neutral (C* ≤ 3.87).
- One scarce accent, sodium amber `#F5B649`: the primary action and the current tab, and nothing else.
- Two faces: Schibsted Grotesk 800 for the title and key numbers, Hanken Grotesk 400/600 for everything else.
- Small radii: 4px inside, 6px outside in content. Bar chrome is native: the floating tab bar is a capsule, controls inside bars are concentric capsules (C7), the Filters sheet takes the sheet radius (38px [?]), and Profile initials are the one circle.
- Flat content, glass chrome: the tab bar, the controls bar, the top bar and the Filters sheet are translucent graphite with blur (C1). Cards never are. Shadows belong to what floats: the sheet and the tab bar.
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
- **Hairline** (`#31363C`, `--line`): dividers only (above the sheet footer, before "Newest first", between Profile rows). Never a fill. Bars use the glass rim instead (step 3b).
- **Field Line** (`#686E75`, `--field-line`): the 1px boundary of inputs, the pressed segment's outline, the hover ring on cards, the map frame. 3:1 against `--bg-0` and `--bg-1`.
- **Field Line, sheet** (`#757B82`, `--field-line-sheet`): the same boundary on the glass Filters sheet (its fields, checkboxes, the outlined Cancel, the grabber). Field Line is only 2.6:1 there; this is 3:1 against the sheet's worst case.
- **Chalk** (`#F4F5F6`, `--text-1`): titles, race names, finish times, date days, body text, links, focus rings, the dot on a map pin, a checked checkbox. 16.76:1 on `--bg-0`.
- **Ash** (`#A3A9B0`, `--text-2`): meta (date month and year, location, counts, proof line), placeholder text, inactive tabs, sheet labels, the active filter chip's outline. 6.90:1 on `--bg-1`.
- **Chip Text** (`#BFC4CA`, `--chip-text`): the format chip's label. 8.11:1 on `--bg-2`.
- **Disabled** (`#6B7178`, `--text-disabled`): a disabled sort control only. Never content.

### Glass (C1, step 3b)
- **Tab-bar glass** (`--glass-bar`): `--bg-bar` at 85% with a 20px blur [?] and a faint Chalk rim at 8% [?]. The floating tab bar, a shade darker than the page so it separates.
- **Ground glass** (`--glass-ground`): `--bg-0` at 85% with the same blur. Bars that sit on the page (the controls bar, the top bar, the status-bar edge): at rest they match the page; they show only when content runs under them, as a scroll edge effect.
- **Sheet glass** (`--glass-sheet`): `--bg-2` at 90% with the blur, over the scrim (C4: the raised level).
- **How the opacities were set:** the build composites each glass over the worst case behind it (Text 1, the brightest thing that can scroll under; for the sheet, Text 1 under the scrim), without counting on the blur, and every text pair on it must pass AA. The lowest passing opacities are 81% (tab bar), 82% (ground), 87% (sheet); the values carry a margin. All are above HIG's 35% dimming layer.
- **Reduce Transparency:** every glass turns into the solid level it's tinted from.

### States
- **Soft Coral** (`#EE8B84`, `--error`): the one error icon before an error heading, the ring of an invalid field (`--invalid`), and the text of a destructive alert action, Sign out (`--destructive`). Not the banned aggressive red.
- **Coral Wash** (`#3A2F31`, `--error-bg`): the error status surface (defined; not shown on these two screens).
- **Scrim** (`rgba(0, 0, 0, 0.6)`, `--scrim`): behind the open Filters sheet.

`--success` and `--success-bg` exist in `ui/kit.css` for the stand's specimen only. No product screen uses them.

### Named Rules
**The Two Lights Rule.** The amber appears at most twice on a screen: the current tab, plus the one primary action if the screen has one. Race browse at rest has only the tab. Log result has no tab bar and no other amber, so its Save, in the top bar, is the screen's one primary and takes amber text, like a native bar button. Every other active state stays neutral: the active filter chip is an outline, the pressed segment is `--bg-3`, a checked checkbox is `--control-tint` (Text 1, C4), the focus ring is `--text-1`.

**The Stated, Not Stamped Rule.** No green, no check icon and no "verified" mark on any result or anywhere on Results list. The saved confirmation is `--bg-1` with a gray save glyph.

**The Depth of Dark Rule.** Every background level has L* between 4.5 and 20 and C* ≤ 6, and each level is at least 1.5 L* above the one below it. `#000` and `#0B0C0E` are out.

## Typography

**Display Font:** Schibsted Grotesk 800 (fallback Hanken Grotesk, sans-serif)
**Body Font:** Hanken Grotesk 400 and 600 (fallback sans-serif)

**Character:** A bold, tight display grotesque for the three things worth shouting (the screen title, the finish time, the date day) against a clean, technical text grotesque for everything else. Each page loads the fonts from its `<head>` (preconnect plus the Google Fonts stylesheet), not from CSS.

### Hierarchy
- **Title** (Schibsted 800, 34px = HIG Large Title, line-height 1, -0.03em): the screen's `h1` ("Discover", "My Results").
- **Finish time** (Schibsted 800, 32px, line-height 1, -0.03em): the finish time on a result row. Proportional figures, `--text-1`, never the accent.
- **Date day** (Schibsted 800, 30px, line-height 1, -0.03em): the day on a race card's date tile (the tile's `::first-line`).
- **Item** (Hanken 600, 17px, line-height 1.2): race names on cards and rows, empty and error headings, the sheet's heading.
- **Body** (Hanken 400, 15px, line-height 1.45): base text, the search field, sheet checkbox labels and fields.
- **Button** (Hanken 600, 15px, line-height 1): primary and secondary buttons, sheet buttons.
- **Meta** (Hanken 400, 15px = HIG Subheadline, line-height 1.45): location, counts ("**7** upcoming races", the number in 600), the sort label, result dates, state body text, the tertiary "Clear all filters". The List/Map segments and the sort value use 15px at 600. Meta shares body's size and stays apart from it by color (`--text-2`).
- **Proof** (Hanken 400, 13px, line-height 1.45): the proof line; the month and year under the date day (line-height 1.2 there).
- **Label** (Hanken 600, 11px, 0.07em, UPPERCASE by CSS only): format chips and active filter chips. The markup keeps the format's own name ("Half marathon").
- **Tab label** (Hanken 600, 11px, line-height 1.45, sentence case): tab labels and map pin labels.

There is no 700. `strong` and `b` render at 600, because Hanken loads only 400 and 600.

The sizes above are the HIG mapping (C3, approved 2026-10-18, applied in step 3b): the title went 38 → 34 and meta 14 → 15; finish time (32px) and date day (30px) stay as display figures (attribute a). They're the sizes at the default text size: every size is a number of type units (`--type-unit`, 1rem ÷ 16 in browsers, 1rem ÷ 17 on iOS, where the root follows Dynamic Type), so text grows with the system setting (G28). The 68px date column grows with it.

### Named Rules
**The Three Shouts Rule.** The display face is used for the screen title, the finish time and the date day, and nowhere else. Race names, chips, buttons, tabs and meta are the text face.

**The Name Stays Rule.** Uppercase is `text-transform` only. The format name in the markup never changes.

## Layout

- **Screen:** 390px wide (`--screen-w`), one column, scrolling inside `.phone-screen`. Content runs under the floating tab bar; 72px of bottom padding (bar + gap + safe area) lets the last item scroll clear of it.
- **Gutter:** 16px (`--space-4`) on every side of the content.
- **Header:** `8px 16px 4px` below the top safe area, gap 12px. On Results list the title and the Log result button share a row (`1fr auto`).
- **Controls (Race browse):** sticky below the top safe area on ground glass, padding `12px 16px`, the glass rim under it. The Filters button fills the row; the List/Map track (a capsule, equal segments) sits at its end. Active filter chips scroll in one row, 12px apart, which fades out over its last 24px; "Clear all filters" sits 12px after it.
- **Count row:** padding `12px 16px`, count on the left, sort control (Race browse) or nothing (Results list) on the right.
- **Lists:** cards and rows stacked with a 12px gap.
- **Race card:** an 8px inset; the photo band (3:1, 114px tall at 342px); below it a grid of a 68px date column and the text column, 12px apart. 216px tall.
- **First screen (step 3b):** in the viewer (757px), 2 full race cards clear of the tab bar with 1.7px to spare, and part of a third showing through the glass (2 full + 29% on screen); with two filters on, 1 full + 75% clear. At 390×844: 2 full + 35% clear, 2 full + 10% with two filters on.
- **Tab bar:** floats 16px in from the sides and 8px above the bottom safe area; a 64px glass capsule, three equal columns, 44px targets.
- **Filters sheet:** slides up over a scrim and rests at the large detent only (the full height less the top safe area and a 12px gap [?]), with a sticky footer (Cancel and Apply filters, 12px apart) above a hairline.
- **Map view:** a frame that fills the space below the controls, with 16px gutters. Pins sit on each race's real latitude and longitude; labels that would collide move above or below on a leader line.
- **Targets:** 44px minimum (`--target`). The 32px filter chips and the tertiary link extend to 44px with an invisible tap area.
- **Running text:** 65ch maximum (`--measure`).

Spacing scale: 4, 8, 12, 16, 20, 24, 32, 48, 64.

## Elevation & Depth

Flat by default. Depth comes from tonal layering: the tab bar (`--bg-bar`) under the page (`--bg-0`) under cards (`--bg-1`) under raised controls (`--bg-2`) under pressed fills (`--bg-3`). Cards have no shadow and no border at rest. On hover a card gets a 1px inset ring in `--field-line`.

### Shadow Vocabulary
- **Float** (`box-shadow: 0 12px 32px -12px rgba(0, 0, 0, 0.6)`, `--shadow-sheet`): what floats over content, the Filters sheet and (since step 3b) the floating tab bar. A `rgba(0, 0, 0, 0.6)` scrim dims the page behind the sheet.

### Named Rules
**The Float Rule.** Only what floats casts a shadow: the sheet and the floating tab bar. Everything else is a tone step.

**The Glass Rule (C1, step 3b).** Bars and the sheet are glass (see Colors → Glass); content never is. A card, a row, a chip or a field stays a flat tone.

## Shapes

Slightly rounded in content, never sharp. Pills only in bar chrome (C7).
- **4px** (`--radius-1`), inner shapes: the photo inside a card, the date tile, format and filter chips, List/Map segments, skeleton bars, map pin labels, checkboxes, the sheet handle.
- **6px** (`--radius-2`), outer shapes: cards, result rows, buttons, the search field in content, sheet fields, the Sign in segmented track, the saved confirmation, the map frame.
- **Bar chrome (step 3b):** the floating tab bar is a capsule (`--radius-tabbar`, 32px); a control inside a bar is a capsule (`--radius-bar-control`, 22px) and a segment inside it is concentric (`--radius-bar-inner`, 18px = 22 − the 4px track padding). Today that's the List/Map control in the controls bar; the search field takes it once the markup pass pins it to a bar (G8). The Filters button beside it keeps 6px (C7 names only the search field and the segmented control).
- **Sheet** (`--radius-sheet`, 38px [?]): the Filters sheet's and Race picker's top corners, the native sheet radius. Replaces the 12px they had until step 3b. `--radius-3` (12px) is now stand panels only.
- **Circles:** the map pin dot, the busy spinner, and **Profile initials** (`--radius-avatar`, 50%): the one exception to "no circles in content", because iOS avatars are circular (designer, 2026-10-19).
- **Borders** are drawn as 1px inset box-shadows (`--border`), so they never change a box's size.

## Components

### Buttons
Exactly one filled button per screen.
- **Shape:** 6px radius, 44px minimum height, `0 20px` padding, 15px / 600, 8px gap to an 18px icon.
- **Primary:** `--accent` fill, `--on-accent` text. Hover `--accent-hover`. Pressed moves down 1px. Background and transform ease over 160ms (`--ease-out`, `cubic-bezier(0.2, 0.8, 0.2, 1)`); 0ms under reduced motion.
- **Secondary:** `--bg-2` fill, `--text-1` text, hover `--bg-3`. Filters on Race browse (with the Solar filters icon, `--bg-3` while its sheet is open), Clear all filters in an empty state. On the Filters sheet (itself `--bg-2`), Cancel is outlined instead: transparent with a 1px `--field-line-sheet` boundary.
- **Tertiary:** a text link, 14px / 400, `--text-1`, 1px underline 4px below, hover `--text-2`. "Clear all filters" in the chips row.
- **Stepping down:** when a state block brings its own primary (Log your first result, Try again), the Results list header's Log result becomes secondary, so the screen keeps one filled button.
- **Disabled:** `--bg-2` fill, `--text-disabled` text. **Busy** (`aria-busy="true"`): same fill, a 15px CSS spinner (a 2px ring in the label's color, one turn per 800ms, still turning under reduced motion, as HIG asks) before the present-tense verb ("Saving…") (G26).
- **Pressed cards and rows:** a race card or a result row takes `--bg-3` while pressed (G23).

### Chips
- **Format chip** (metadata): `--bg-2` fill, `--chip-text`, 4px radius, 24px tall, `0 8px`, 11px / 600 uppercase, 0.07em. The same for every format: no per-format color.
- **Active filter chip** (a removable state): transparent with a 1px `--text-2` outline, `--text-1` label, 32px tall, `0 12px`, 4px radius, and a 15px Solar close-circle in `--text-2`.

### Cards / Containers
- **Race card:** `--bg-1`, 6px radius, 8px padding, flat. The whole card is one link, photo included. Inside it: a black-and-white photo (`grayscale(1) contrast(1.12) brightness(0.85)`) at 3:1 with a 4px radius; then the date tile (68px wide, `--bg-2`, 4px radius, `12px 4px` padding, the day in Schibsted 30px `--text-1` over the month and year in 13px `--text-2`); then the race name (17px / 600), the format chip, and the location (14px `--text-2` with a 15px Solar map-point icon).
- **Result row:** `--bg-1`, 6px radius, `12px 39px 16px 16px` padding (room for the disclosure indicator), 8px gaps. A 15px Solar alt-arrow-right in `--text-2` sits at the trailing edge, centered: the row drills into Result detail (G22). Race cards are a collection, so they have none. The race name on the left and the finish time (Schibsted 32px) on the right, sharing a baseline; then the format chip and the date (14px `--text-2`); then the proof line (13px `--text-2`, one 15px Solar link icon, wraps anywhere).
- **Saved confirmation:** `--bg-1`, 6px radius, `12px 16px`, 14px `--text-1` with the race name in 600, and an 18px Solar save glyph in `--text-2`. Never green, never a check.
- **Skeletons (loading):** `--bg-2` bars with a 4px radius, in the exact shape of the card or row they stand for. The finish-time bar is 32px tall, so nothing shifts. A subtle pulse (opacity to 0.55 and back over 1.6s), still under reduced motion (C6). No spinner, no shimmer.

### Inputs / Fields
- **Search field:** `--bg-1`, 6px radius (a capsule inside a bar, C7), 44px tall, a 1px `--field-line` inset boundary, an 18px Solar magnifier in `--text-2`, placeholder in `--text-2`. Hover: the boundary turns `--text-2`. Focus: a 2px `--text-1` outline replaces it. Filled and focused, it shows the browser's own Clear button (system-drawn, C2; G10).
- **Text fields (grayscale screens):** invalid is a 2px `--invalid` (coral) ring inside the field; focus is the 2px white ring outside. An invalid field with focus shows both, so invalid and focus never look alike.
- **Sheet select and date fields:** `--bg-0`, 6px radius, 44px tall, 1px `--field-line-sheet`, 15px text. The select has a 15px Solar chevron; the date field has an 18px Solar calendar instead of the browser's glyph.
- **Checkbox:** 18px, 4px radius, `--bg-0` with a 1px `--field-line-sheet` boundary; checked fills `--control-tint` (Text 1) with a `--bg-0` tick. Never the accent. Every system-drawn control takes the same tint (`accent-color`, C4).
- **Sort control:** borderless, `--text-1` 15px / 600 with a `--text-1` chevron; the label "Sort:" in `--text-2`.
- **Focus (everything):** a 2px `--text-1` outline, 2px offset. Never the accent.

### Navigation
- **Tab bar:** a floating 64px capsule of tab-bar glass with a faint rim and the float shadow, three tabs (Discover, My Results, Profile). Each has a 26px Solar icon (compass, stopwatch, user) over an 11px / 600 label. Inactive: `--text-2`. Current: `--accent`, icon and label.
- **List / Map segmented control:** a `--bg-2` track with 4px padding; in the controls bar a 22px capsule with 18px segments (C7), in content (Sign in) 6px with 4px segments. Segments are of equal width (G11), 36px (44px tap area), 15px / 600, `--text-2`.
- **Top bar (grayscale screens):** ground glass with a rim, below the top safe area. Back and Cancel in `--text-1`; Save on Log result in `--accent` (that screen's one primary); "Saving…" in `--text-2` with the spinner.
- **Confirm alert:** Sign out, the destructive action, is `--destructive` (coral) text; Cancel stays `--text-1` (HIG Alerts). The pressed segment is `--bg-3`, `--text-1`, with a 1px `--field-line` outline.

### Empty and error states
A message block, left-aligned, 24px of vertical padding: a 17px / 600 heading, 15px `--text-2` body (65ch max), then actions in the button hierarchy, 12px apart. An error heading gets one 18px Solar danger-circle in `--error`. Nothing else turns red.

### Filters sheet (signature)
Sheet glass (`--bg-2` at 90%, blurred), 38px top corners [?] with a rim along the top edge, the float shadow, over the scrim. It rests at the large detent only, and slides up over 250ms (`--dur-sheet`, `--ease-out`; 0ms under reduced motion). A 32×4px handle in `--field-line-sheet`; a 17px / 600 heading; 15px `--text-2` labels; fields and checkboxes as above; a sticky footer at the sheet's bottom edge, solid `--bg-2`, with Cancel (outlined) and Apply filters (the sheet's one primary), each half the width. The markup pass moves these to a top toolbar and makes the grabber a real control (G12, G14); swipe-to-dismiss stays out of scope (G15).

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
- **Do** take every value from `ui/kit.css`. Pages and the kit's classes hold no raw values.
- **Do** draw icons as Solar bold masks in the color of their text: 15px in meta, 18px in buttons and fields, 26px in the tab bar.
- **Do** keep 44px targets, a 2px `--text-1` focus ring, and 0ms motion under `prefers-reduced-motion` (skeletons still; only the busy spinner keeps turning).
- **Do** check text on glass against the worst case behind it, not against the glass's own tint.

### Don't:
- **Don't** put the amber on a finish time, a chip, a filter chip, a count, a link, a focus ring, an icon in content, a status, or the map.
- **Don't** use green, a check icon or the word "verified" on a result or on Results list.
- **Don't** give formats their own colors. Every format chip is the same neutral chip.
- **Don't** use pure `#000`, `#0B0C0E`, the `#ff4d2e` family, `src/style.css` or the wireframe grays.
- **Don't** use aggressive "energy" red. Errors are soft coral `#EE8B84`, on the icon only.
- **Don't** set race names, chips, buttons or tabs in the display face, or use one heavy condensed face for everything.
- **Don't** drop the radius to 0, or round content into pills (pills belong to bar chrome only).
- **Don't** give cards a shadow, a border at rest, or glass.
- **Don't** use `--line`, `--field-line` or `--field-line-sheet` as a fill (the sheet's grabber is a drawn 4px line, the one exception).
- **Don't** let invalid and focus look alike: coral inside for invalid, white outside for focus.
- **Don't** use tabular figures on finish times: Schibsted spaces the colons wide ("24 : 36").

## Native iOS

**The rule (designer, 2026-10-18).** Every element with a native iOS counterpart follows Apple's Human Interface Guidelines for anatomy, metrics and behavior: sizes, placement, grabber, large title, safe areas, 44pt targets, sheet detents, and search and segmented-control behavior. Podium keeps the visual language: colors, fonts, Solar icons and photos. Where the two conflict, the designer decides: the seven conflicts (**C1–C7**) were decided on 2026-10-18, below. `concept/concept.md` → Native iOS holds the 33 gaps (G1–G33) between today's screens and HIG and their triage (15 kit, 13 markup pass, 5 out of scope). The screens change through the kit in steps 3 and 5.

HIG read on 2026-10-18; every link returned HTTP 200. "System" means HIG publishes no number and the system draws it.

| Component on the screens | HIG page | What native means for it | What Podium keeps |
|---|---|---|---|
| Tab bar (Discover, My Results, Profile) | [Tab bars](https://developer.apple.com/design/human-interface-guidelines/tab-bars) | For navigation, not actions. Visible in every section; only a modal may cover it. Labels under icons, single words where possible. Prefer filled icons. On iOS it floats above content at the bottom on a Liquid Glass background, and content shows through beneath it. It may include a search tab at the trailing end. | Solar bold icons (filled, as HIG prefers), Hanken labels, amber on the current tab. Material: translucent graphite with blur in Podium tones (**C1**). Icons: Solar (**C2**). |
| Screen title ("Discover", "My Results") and top bar | [Toolbars](https://developer.apple.com/design/human-interface-guidelines/toolbars), [Typography](https://developer.apple.com/design/human-interface-guidelines/typography) | A large title that turns into a standard inline title in the top bar as people scroll, and back to large at the top. Titles under 15 characters. Actions sit in the toolbar; the key action uses the `.prominent` style, only one, on the trailing side. Prefer symbols to text for toolbar items. Fewer custom toolbar backgrounds: a scroll edge effect separates bar and content. | The title's text in Schibsted Grotesk 800 at Large Title size, 34 (**C3**). Top bar: translucent graphite with blur (**C1**). The amber on the one primary action. |
| Search field (Race browse) | [Search fields](https://developer.apple.com/design/human-interface-guidelines/search-fields), [Text fields](https://developer.apple.com/design/human-interface-guidelines/text-fields) | A search icon, placeholder text, and a Clear button at the trailing end. Search starts as people type. An inline field sits above the list it filters and can pin to the top toolbar on scroll. Bottom-toolbar search or a search tab are the other native placements. | `--bg-1` field, `--field-line` boundary, Solar magnifier (**C2**), the placeholder "Race name or city". Inside a bar, its corners are concentric with the bar (**C7**). |
| List / Map segmented control | [Segmented controls](https://developer.apple.com/design/human-interface-guidelines/segmented-controls) | For closely related subviews (List and Map qualify). Segments of equal width, text only, nouns, at most about five on iPhone. | `--bg-2` track, `--bg-3` selected segment, Hanken 15/600. Inside the controls bar, corners concentric with the bar (**C7**). |
| Buttons (Filters, Log result, state actions, sheet actions) | [Buttons](https://developer.apple.com/design/human-interface-guidelines/buttons) | Hit region at least 44×44pt. A press state on every custom button. One or two prominent buttons per view. Style, not size, separates the preferred choice. The primary role takes the accent. A delayed action shows an activity indicator inside the button, with an alternative label ("Checking out…"). | Amber primary, tonal secondary, underlined tertiary, Hanken 15/600, the 1px press. Buttons in content keep 6px (**C7**); a button inside a bar is concentric with it. |
| Filters sheet | [Sheets](https://developer.apple.com/design/human-interface-guidelines/sheets) | See *Native sheet anatomy* below. | Our raised graphite level as its background (**C4**), translucent with blur (**C1**), the scrim, Hanken type, Solar icons inside. |
| Region select (sheet) | [Pull-down buttons](https://developer.apple.com/design/human-interface-guidelines/pull-down-buttons), [Pickers](https://developer.apple.com/design/human-interface-guidelines/pickers) | A short list of choices (6 regions) is a menu from a button, not a picker. Mutually exclusive choices that aren't commands belong in a pop-up button, which shows the current value. | The button: Hanken 15, `--text-1` value, Solar chevron (**C2**). The menu it opens is the system's (**C2**). |
| Race date from / to (sheet) | [Pickers](https://developer.apple.com/design/human-interface-guidelines/pickers) | A compact date picker: a button showing the current value in the app's accent color, which opens a calendar editor in a modal view. Values and their order follow the device's locale. | The date picker is drawn by the system (**C2**). Its tint is neutral text color, not amber (**C4**). Hanken type on our button. |
| Sport-type choices (sheet) | [Toggles](https://developer.apple.com/design/human-interface-guidelines/toggles), [Lists and tables](https://developer.apple.com/design/human-interface-guidelines/lists-and-tables) | iOS has no checkbox. In a list row, use a switch (default green, or the app's accent), or a selectable row that adds a checkmark when chosen. Outside a list, use a button that behaves like a toggle. | Hanken 15 labels, `--text-1`. Checkmark or switch tinted in neutral text color, never amber or green (**C4**). |
| Sort ("Sort: Soonest first") | [Pull-down buttons](https://developer.apple.com/design/human-interface-guidelines/pull-down-buttons) | A button that opens a menu; sorting is HIG's own example. A menu should list at least three items; for one or two, consider other controls. For mutually exclusive choices, use a pop-up button. | Hanken 15/600, "Sort:" in `--text-2`, Solar chevron on our button (**C2**). The menu is the system's (**C2**). |
| Result rows; race cards | [Lists and tables](https://developer.apple.com/design/human-interface-guidelines/lists-and-tables) | A row that drills into a detail view shows a disclosure indicator. Selection gives feedback (a highlight). Items that vary in size or carry many images suit a collection rather than a list, so the photo-led race cards are a collection. | Cards, photos, the date tile, the finish time, the proof line, 4/6px radii (content keeps 4/6, **C7**). Disclosure chevron in Solar (**C2**). Never glass (**C1**). |
| Error states | [Alerts](https://developer.apple.com/design/human-interface-guidelines/alerts) | Don't use an alert only to inform, or for a connection problem: show it in context with a non-intrusive label. An alert is for something people must act on. | The inline state message, the coral icon. No gap: the screens already do this. |
| Loading | [Progress indicators](https://developer.apple.com/design/human-interface-guidelines/progress-indicators) | Indeterminate loading uses an activity indicator, and indicators keep moving ("people associate a stationary indicator with a stalled process"). Lists support pull-to-refresh, and content also refreshes on its own. | Skeleton shapes in `--bg-2` with a subtle pulse, still under Reduce Motion (**C6**). |
| Status bar | [Status bars](https://developer.apple.com/design/human-interface-guidelines/status-bars) | Transparent, never permanently hidden. Content under it is obscured, preferably with a scroll edge effect. | Light content on the graphite ground (as the viewer already samples). A scroll edge effect in Podium tones (**C1**). |
| Safe areas and margins | [Layout](https://developer.apple.com/design/human-interface-guidelines/layout) | Respect the safe areas (Dynamic Island at the top, home indicator at the bottom) and system margins. Layouts adapt to text-size changes. Controls are set off from content by Liquid Glass and a scroll edge effect, not a solid background. | 16px gutter and the spacing scale, where HIG doesn't set the margin. Bars in translucent graphite (**C1**). |
| Type | [Typography](https://developer.apple.com/design/human-interface-guidelines/typography) | SF Pro and the text styles. At the default size: Large Title 34pt Regular (Bold when emphasized), Headline 17 Semibold, Body 17, Subhead 15, Footnote 13, Caption 2 11. Minimum 11pt. Support Dynamic Type; custom fonts must implement Dynamic Type and Bold Text themselves. | Schibsted Grotesk 800 and Hanken Grotesk 400/600, mapped onto the HIG text styles (**C3**; see the mapping below). |
| Appearance | [Dark Mode](https://developer.apple.com/design/human-interface-guidelines/dark-mode) | Respect the system appearance; don't offer an in-app setting. Dark-only only "in rare cases", such as immersive media. Prefer system background colors, base and elevated (a modal sheet takes the elevated one). Contrast at least 4.5:1; aim for 7:1 for custom colors in small text. | Dark only, a designer decision (**C5**). Our graphite levels, not system backgrounds (**C4**). |
| Accessibility | [Accessibility](https://developer.apple.com/design/human-interface-guidelines/accessibility) | Controls 44×44pt (28×28 minimum). About 12pt of space around elements with a bezel, 24pt around those without. Contrast 4.5:1 up to 17pt; 3:1 at 18pt or in bold. Text can grow to 200%. Respect Reduce Motion. Don't convey meaning with color alone. Label everything for VoiceOver. Give every swipe an on-screen alternative. | AA contrast on all 99 checked pairs (11 of them over glass, against the worst case), 44px targets, reduced motion at 0ms, Reduce Transparency turns glass solid, icon plus text in state messages. |

### Native sheet anatomy

The Filters sheet follows the native iOS sheet, not a one-off radius (designer decision 2026-10-18):
- **Corners:** the system's sheet radius, `--radius-sheet` (38px), replacing the 12px (step 3b). **[?] Provisional:** Apple's iOS 26 kit wasn't read; HIG publishes no number.
- **Grabber:** at the top edge of a resizable sheet. Drag to resize, tap to cycle detents, operable with VoiceOver.
- **Detents:** large only (designer, 2026-10-19; step 3b). Medium isn't used.
- **Buttons:** Cancel on the leading edge of a top toolbar, Apply filters (prominent) on the trailing edge.
- **Dismissal:** swipe down; confirm with an action sheet if changes weren't applied.
- **Background:** sheet glass, `--bg-2` at 90% with blur (C1, C4), since step 3b.

### HIG vs Podium: decided (designer, 2026-10-18)

- **C1 Liquid Glass:** adopted for bars (tab bar, top bar, controls bar) and the Filters sheet: translucent graphite with blur, in Podium's tones. Never on cards; content stays flat. Applied in step 3b (see Colors → Glass).
- **C2 Icons:** Solar stays for our icons. Controls the system draws (the date picker, system menus) stay system.
- **C3 Fonts:** Schibsted Grotesk and Hanken Grotesk stay, with Podium's scale mapped onto the HIG text styles. Approved 2026-10-18: title 38 → Large Title 34; item 17 = Headline; body and buttons 15 = Subheadline; meta 14 → Subheadline 15; proof 13 = Footnote; labels 11 = Caption 2; finish time 32 and date day 30 stay as display figures (attribute a). Measured before C1: the first screen kept two full race cards (9.7px to spare in the viewer, was 8.6px). After C1 (step 3b), with content under the floating glass tab bar: two full cards clear of the bar, 1.7px to spare (see Layout).
- **C4 Control tint:** neutral (text color) for checkmarks and switches. Amber stays only per Color rule 1. The sheet's background is the raised graphite level, `--bg-2` (confirmed 2026-10-18).
- **C5 Dark only:** kept, as a designer decision. Dark is Onrace's identity from the brand tone and the attributes, and every color rule and contrast check is built for it.
- **C6 Loading:** a subtle pulse on skeletons, still under reduced motion.
- **C7 Corners:** concentric only for elements inside bars (the search field, the segmented control). Content keeps 4/6px.

## Sources

- [`concept/concept.md`](concept/concept.md): the rules and every decision behind these values (Designer's taste, Hierarchy rules, Color rules, race card anatomy, Results list details, Map, Deferred to Lesson 7).
- [`concept/references.md`](concept/references.md): the references, the techniques taken and the anti-references, and the photo log.
- Values and components: [`ui/kit.css`](ui/kit.css), [`ui/map.css`](ui/map.css); the showcase [`ui/kit.html`](ui/kit.html) and the shell [`ui/shell.html`](ui/shell.html); the inventory [`ui/inventory.md`](ui/inventory.md). Signed reasons for each token: the stand, [`concept/concept.html`](concept/concept.html).
