---
name: Onrace
description: A race calendar and personal results archive for hybrid athletes. Direction A, "Podium".
colors:
  frame: "#0F1114"
  page: "#131518"
  surface: "#1D2024"
  raised: "#272B30"
  pressed: "#2C3035"
  group: "#2C3035"
  glass-bar: "color-mix(in srgb, #0F1114 85%, transparent)"
  glass-ground: "color-mix(in srgb, #131518 85%, transparent)"
  glass-sheet: "color-mix(in srgb, #272B30 90%, transparent)"
  glass-rim: "color-mix(in srgb, #F4F5F6 8%, transparent)"
  scrim: "color-mix(in srgb, #000000 60%, transparent)"
  text-primary: "#F4F5F6"
  text-secondary: "#A3A9B0"
  text-disabled: "#6B7178"
  chip-text: "#BFC4CA"
  hairline: "#31363C"
  boundary: "#686E75"
  accent-fill: "#F5B649"
  on-accent-fill: "#131518"
  accent-ink: "#F5B649"
  accent-hover: "#FFC46A"
  accent-ink-hover: "#FFC46A"
  error: "#EE8B84"
  error-surface: "#3A2F31"
  map-water: "#0F1114"
  map-land: "#1D2024"
  map-lines: "#2C3035"
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
  radius-filter-chip: "16px"
  radius-alert: "34px"
  radius-tabbar: "32px"
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
    backgroundColor: "{colors.accent-fill}"
    textColor: "{colors.on-accent-fill}"
    typography: "{typography.button}"
    rounded: "{rounded.radius-2}"
    padding: "0 20px"
    height: "44px"
  button-primary-hover:
    backgroundColor: "{colors.accent-hover}"
    textColor: "{colors.on-accent-fill}"
  button-secondary:
    backgroundColor: "{colors.raised}"
    textColor: "{colors.text-primary}"
    typography: "{typography.button}"
    rounded: "{rounded.radius-2}"
    padding: "0 20px"
    height: "44px"
  button-secondary-hover:
    backgroundColor: "{colors.pressed}"
    textColor: "{colors.text-primary}"
  button-tertiary:
    textColor: "{colors.text-primary}"
    typography: "{typography.meta}"
    padding: "0 4px"
    height: "44px"
  button-tertiary-hover:
    textColor: "{colors.text-secondary}"
  format-chip:
    backgroundColor: "{colors.raised}"
    textColor: "{colors.chip-text}"
    typography: "{typography.label}"
    rounded: "{rounded.radius-1}"
    padding: "0 8px"
    height: "24px"
  filter-chip:
    backgroundColor: "{colors.raised}"
    textColor: "{colors.text-primary}"
    typography: "{typography.proof}"
    rounded: "{rounded.radius-filter-chip}"
    padding: "0 8px 0 12px"
    height: "32px"
  filter-chip-hover:
    backgroundColor: "{colors.pressed}"
    textColor: "{colors.text-primary}"
  race-detail-photo:
    rounded: "{rounded.radius-2}"
  action-bar-button:
    backgroundColor: "{colors.accent-fill}"
    textColor: "{colors.on-accent-fill}"
    typography: "{typography.button}"
    rounded: "{rounded.radius-bar-control}"
    height: "44px"
  search-field:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.text-primary}"
    typography: "{typography.body}"
    rounded: "{rounded.radius-2}"
    padding: "0 12px 0 42px"
    height: "44px"
  sheet-field:
    backgroundColor: "{colors.page}"
    textColor: "{colors.text-primary}"
    typography: "{typography.body}"
    rounded: "{rounded.radius-2}"
    padding: "0 12px"
    height: "44px"
  segmented-track:
    backgroundColor: "{colors.raised}"
    rounded: "{rounded.radius-bar-control}"
    padding: "4px"
  segment:
    textColor: "{colors.text-secondary}"
    rounded: "{rounded.radius-bar-inner}"
    padding: "0 16px"
    height: "36px"
  segment-pressed:
    backgroundColor: "{colors.pressed}"
    textColor: "{colors.text-primary}"
  race-card:
    backgroundColor: "{colors.surface}"
    rounded: "{rounded.radius-2}"
    padding: "8px"
  date-tile:
    backgroundColor: "{colors.raised}"
    textColor: "{colors.text-secondary}"
    typography: "{typography.proof}"
    rounded: "{rounded.radius-1}"
    padding: "12px 4px"
    width: "68px"
  result-row:
    backgroundColor: "{colors.surface}"
    rounded: "{rounded.radius-2}"
    padding: "12px 16px 16px"
  saved-status:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.text-primary}"
    typography: "{typography.meta}"
    rounded: "{rounded.radius-2}"
    padding: "12px 16px"
  tab-bar:
    backgroundColor: "{colors.glass-bar}"
    rounded: "{rounded.radius-tabbar}"
    textColor: "{colors.text-secondary}"
    typography: "{typography.tab-label}"
    height: "64px"
  tab-current:
    textColor: "{colors.accent-ink}"
  filters-sheet:
    backgroundColor: "{colors.glass-sheet}"
    rounded: "{rounded.radius-sheet}"
    padding: "0"
  sheet-row:
    backgroundColor: "{colors.group}"
    textColor: "{colors.text-primary}"
    typography: "{typography.body}"
    rounded: "{rounded.radius-2}"
    padding: "0 16px"
    height: "44px"
  sort-button:
    textColor: "{colors.text-primary}"
    typography: "{typography.meta}"
    height: "44px"
  form-row:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.text-primary}"
    typography: "{typography.body}"
    rounded: "{rounded.radius-2}"
    padding: "0 16px"
    height: "44px"
  action-sheet:
    backgroundColor: "{colors.glass-sheet}"
    textColor: "{colors.text-primary}"
    typography: "{typography.item}"
    rounded: "{rounded.radius-alert}"
  bar-action:
    textColor: "{colors.accent-ink}"
    typography: "{typography.button}"
    height: "44px"
  map-pin-label:
    backgroundColor: "{colors.raised}"
    textColor: "{colors.text-primary}"
    typography: "{typography.tab-label}"
    rounded: "{rounded.radius-1}"
    padding: "0 8px"
    height: "22px"
---

# Design System: Onrace

Documented on 2026-10-18 (Lesson 7, step 1) from the two painted screens and all their states:
- `wireframes/race-browse.html`, `-empty`, `-error`, `-loading`; the filtered state (`?sport=hyrox&sport=marathon`); the Filters sheet open; the Map view
- `wireframes/results-list.html`, `-empty`, `-error`, `-loading`; the saved state (`?saved=`)
- `wireframes/race-detail.html`, `-error` (both causes), `-loading`: added 2026-10-22 (Lesson 7 step 5, Discovery)
- Archive and Infrastructure, added 2026-10-22 (step 5): `log-result`, `race-picker`, `result-detail`, `sign-in-sign-up`, `reset-password`, `new-password`, `profile`, each with all its state pages. Every screen is now on the kit.

Every value comes from `tokens/tokens.css` (two levels: primitives named by hue and L*, and semantic color roles) and `ui/map-data.css`, every component from `components/` (Lesson 8 step 4; before that `ui/kit.css` and `ui/map.css`, and until Lesson 7 step 3a `concept/tokens.css`, `concept/map.css` and `concept/components.css`), and was checked against the computed styles of the rendered screens at 390×844. The screens are the source of truth. The artifact pages (`concept.html`, `directions*.html`, `voice.html`, `ia.html`, the workspace shell) are not the product, and nothing here describes them.

All ten screens use this system since Lesson 7 step 5 (2026-10-22).

**Updated 2026-10-23 (markup pass, round 2):** Log result is a modal sheet with a grouped form and a discard confirm; the sign-in screens are grouped forms with the confirm in the bar; Result detail's link error is an alert; every accessible name starts with its visible label. **Updated 2026-10-23 (markup pass):** Sort is one button, the Filters sheet has a top bar and grouped rows, the large title collapses into the bar, Log result is a bar action, the tab is "Results", Race detail's link error is an alert. **Updated 2026-10-22 (Lesson 7 step 5, Discovery, and its review).** Race detail is on the kit, with the race’s photo on top (a designer decision). Two kit fixes reach every screen: active filter chips are tonal capsules (C7), and empty and error states are never framed.

**Updated 2026-10-19 (Lesson 7, step 3b), the native iOS pass.** The kit changed on purpose: glass bars and sheet (C1), the HIG type mapping (C3), a neutral control tint (C4), a skeleton pulse (C6), concentric controls in bars (C7), and the Kit (CSS) gaps (G1, G2, G6, G7, G10, G11, G13, G16, G22, G23, G25–G29). The sections below describe the screens after that pass. Values marked **[?]** (glass opacity margins, blur, rim, sheet radius, the sheet's top gap) are provisional: Apple's iOS 26 design kit wasn't read; the one Apple number used is HIG Materials' 35% dimming layer, as a floor.

**Updated 2026-10-25 (Lesson 7, step 6), the critique fixes.** Every defect from the step 6 critique is fixed in the kit and carried to the screens, and the designer's decisions on the rest are signed where they apply: the finish time leads Result detail, editable values in Text 1, "Account" on the sign-in screens, Solar Linear for small UI glyphs, one Clear all filters, one locked-form treatment, Results receded behind the Log result sheet. Record: `concept/concept.md` → Step 6.

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
- Flat content, glass chrome: the tab bar, the controls bar, the top bar, the action bar and the Filters sheet are translucent graphite with blur (C1). Cards never are. Shadows belong to what floats: the sheet and the tab bar.
- Neutral metadata: format chips, filter chips (gray capsules), map pins, the saved confirmation and every pressed state stay gray.
- Black-and-white photos, 3:1: inset in the race card, and at full content width on top of Race detail (the same band).
- Solar Bold icons, drawn as CSS masks in the color of their text; the small UI glyphs (back, chevrons, disclosure, the search magnifier) are Solar Linear, a designer exception (step 6, 2026-10-25: iOS thins its symbols at small sizes).

## Colors

A graphite ramp, two text grays, one amber, and a soft coral for errors only.

### Primary
- **Sodium Amber** (`#F5B649`, `--accent-fill`, `--accent-ink`; primitive `--amber-78`): `--accent-fill` is the fill of the screen's one primary button (Log result in the Results list header; Change filters on Race browse `-empty`; Try again on both `-error` pages; Apply filters in the Filters sheet) and `--accent-ink` the icon and label of the current tab and the bar action (two roles on one primitive since Lesson 8: in a light appearance amber text needs a darker amber than the fill). On-accent text `#131518` is 10.16:1 on it. The current tab label is 10.51:1 on the tab bar.
- **Amber, hover** (`#FFC46A`, `--accent-hover`): the primary button under the pointer. Never at rest.
- **Amber ink, hover** (`#FFC46A`, `--accent-ink-hover`): the bar action (Save, Log result) under the pointer. Split from `--accent-hover` in Lesson 8 step 5: the same value in dark, apart in light.
- **On Accent** (`#131518`, `--on-accent-fill`): text and icons on the amber fill. The same primitive as `--page`, `--graphite-7`.

### Neutral
- **Tab-bar Black** (`#0F1114`, `--frame`; primitive `--graphite-5`, L* 4.99): the void behind an open sheet. The tab bar glass (`--glass-bar`) and the water on the static map (`--map-water`) are built on the same primitive.
- **Graphite Ground** (`#131518`, `--page`, L* 6.69): the page, the sticky controls bar, the fields inside the Filters sheet, an unchecked checkbox.
- **Graphite Surface** (`#1D2024`, `--surface`, L* 12.10): race cards, result rows, the search field, the saved confirmation, the Filters sheet, land on the map.
- **Graphite Raised** (`#272B30`, `--raised`, L* 17.33): the secondary button, the format chip, the date tile, the List/Map track, map pin labels, skeleton bars.
- **Graphite Pressed** (`#2C3035`, `--pressed`; primitive `--graphite-20`, L* 19.67): hover, open and pressed fills on raised controls (secondary hover, the pressed List/Map segment, Filters while its sheet is open, pin hover). Never at rest on a card. The same primitive is `--group` (a group of rows one level above its container: the Filters sheet's rows, the linked race on Log result) and `--map-lines` (the coastlines and borders on the map).
- **Hairline** (`#31363C`, `--hairline`): dividers only (above the sheet footer, before "Newest first", between Profile rows). Never a fill. Bars use the glass rim instead (step 3b).
- **Field Line** (`#686E75`, `--boundary`): the 1px boundary of inputs, the pressed segment's outline, the hover ring on cards, the map frame. 3:1 against `--page` and `--surface`.
- **Chalk** (`#F4F5F6`, `--text-primary`): titles, race names, finish times, date days, body text, links, focus rings, the dot on a map pin, a checked checkbox. 16.76:1 on `--page`.
- **Ash** (`#A3A9B0`, `--text-secondary`): meta (date month and year, location, counts, proof line), placeholder text, inactive tabs, sheet labels, the active filter chip's remove mark. 6.90:1 on `--surface`.
- **Chip Text** (`#BFC4CA`, `--chip-text`): the format chip's label. 8.11:1 on `--raised`.
- **Disabled** (`#6B7178`, `--text-disabled`): a disabled sort control only. Never content.

### Glass (C1, step 3b)
- **Tab-bar glass** (`--glass-bar`): `--graphite-5` at 85% (`--alpha-85`) with a 20px blur [?] and a faint Chalk rim at 8% [?]. The floating tab bar and the sticky action bar on Race detail and Result detail, a shade darker than the page so they separate.
- **Ground glass** (`--glass-ground`): `--page` at 85% with the same blur. Bars that sit on the page (the controls bar, the top bar, the status-bar edge): at rest they match the page; they show only when content runs under them, as a scroll edge effect.
- **Sheet glass** (`--glass-sheet`): `--raised` at 90% with the blur, over the scrim (C4: the raised level).
- **How the opacities were set:** the build composites each glass over the worst case behind it (Text 1, the brightest thing that can scroll under; for the sheet, Text 1 under the scrim), without counting on the blur, and every text pair on it must pass AA. The lowest passing opacities are 81% (tab bar), 82% (ground), 87% (sheet); the values carry a margin. All are above HIG's 35% dimming layer.
- **Reduce Transparency:** every glass turns into the solid level it's tinted from.

### States
- **Soft Coral** (`#EE8B84`, `--error`): the one error icon before an error heading, the ring of an invalid field, and the text of a destructive alert action, Sign out (`--invalid` and `--destructive` until Lesson 8, merged into `--error`). Not the banned aggressive red.
- **Coral Wash** (`#3A2F31`, `--error-surface`): the error status surface (defined; not shown on these two screens).
- **Scrim** (`rgba(0, 0, 0, 0.6)`, `--scrim`): behind the open Filters sheet.

`--success` and `--success-bg` exist in `concept/specimens.css` for the stand's specimen only. No product screen uses them.

### Light theme (stress test, Lesson 8 step 5, 2026-10-30): a proof, not a feature
Onrace is dark-only (C5). To prove the roles hold a second appearance, `tokens/tokens.css` has a `:root[data-theme="light"]` block that overrides semantic roles only, on `?theme=light`. It follows iOS light: the page `--graphite-96`, white surfaces and rows, `--graphite-93` raised and `--graphite-89` pressed fills, secondary text `--graphite-39`. Podium stays: the amber fill is the same `#F5B649` with dark text; the ink is `--amber-40` (`#875206`), darker and about 8° warmer, so amber text holds AA on light bars and passes rule 3b without the override; the coral darkens to `--coral-40` (`#A33A32`); photos stay black and white; chips stay neutral. Glass is light and translucent (90–92%), checked over black, the darkest thing that can scroll under it. **Decided (designer, 2026-10-30):** the product stays dark-only. Light stays only as proof of the semantic layer: it isn't offered to users and won't be polished. The viewer's Light / Dark control stays for the course, and the build keeps checking light (contrast, glass, color rules 1 and 2, the 3b report), so a component that reads a color primitive is caught (`concept/concept.md` → The light theme stays a proof, not a feature). Every state in both themes: `ui/review-theme.html`.

### Named Rules
**The Two Lights Rule.** The amber appears at most twice on a screen: the current tab, plus the one primary action if the screen has one. Race browse at rest has only the tab. Log result has no tab bar and no other amber, so its Save, in the top bar, is the screen's one primary and takes amber text, like a native bar button. Every other active state stays neutral: the active filter chip is a gray capsule, the pressed segment is `--pressed`, a checked checkbox is `--text-primary` (Text 1, C4), the focus ring is `--text-primary`.

**The Stated, Not Stamped Rule.** No green, no check icon and no "verified" mark on any result or anywhere on Results list. The saved confirmation is `--surface` with a gray save glyph.

**The Depth of Dark Rule.** Every background level has L* between 4.5 and 20 and C* ≤ 6, and each level is at least 1.5 L* above the one below it. `#000` and `#0B0C0E` are out.

## Typography

**Display Font:** Schibsted Grotesk 800 (fallback Hanken Grotesk, sans-serif)
**Body Font:** Hanken Grotesk 400 and 600 (fallback sans-serif)

**Character:** A bold, tight display grotesque for the three things worth shouting (the screen title, the finish time, the date day) against a clean, technical text grotesque for everything else. Each page loads the fonts from its `<head>` (preconnect plus the Google Fonts stylesheet), not from CSS.

### Hierarchy
- **Title** (Schibsted 800, 34px = HIG Large Title, line-height 1, -0.03em): the screen's `h1` ("Discover", "Results").
- **Finish time** (Schibsted 800, 32px, line-height 1, -0.03em): the finish time on a result row. Proportional figures, `--text-primary`, never the accent.
- **Finish time, leading** (Schibsted 800, 56px, `--size-time-hero`): the finish time on Result detail, the largest thing on that screen (designer, step 6, 2026-10-25; attribute a). The race name above it steps down to Item.
- **Date day** (Schibsted 800, 30px, line-height 1, -0.03em): the day on a race card's date tile, its own `span.day` since the markup pass (2026-10-23; it was the tile's `::first-line`).
- **Item** (Hanken 600, 17px, line-height 1.2): race names on cards and rows, empty and error headings, the sheet's heading.
- **Body** (Hanken 400, 15px, line-height 1.45): base text, the search field, sheet checkbox labels and fields.
- **Button** (Hanken 600, 15px, line-height 1): primary and secondary buttons. Bar text buttons (back, Cancel, Save, the bar action) and alert buttons are 17px, HIG Body (step 6, 2026-10-25).
- **Meta** (Hanken 400, 15px = HIG Subheadline, line-height 1.45): location, counts ("**7** upcoming races", the number in 600), the sort label, result dates, state body text, the tertiary "Clear all filters". The List/Map segments and the sort value use 15px at 600. Meta shares body's size and stays apart from it by color (`--text-secondary`).
- **Proof** (Hanken 400, 13px, line-height 1.45): the proof line; the month and year under the date day (line-height 1.2 there).
- **Label** (Hanken 600, 11px, 0.07em, UPPERCASE by CSS only): format chips. (Active filter chips are 13px / 600 in sentence case, since 2026-10-22.) The markup keeps the format's own name ("Half marathon").
- **Tab label** (Hanken 600, 11px, line-height 1.45, sentence case): tab labels and map pin labels.

There is no 700. `strong` and `b` render at 600, because Hanken loads only 400 and 600.

The sizes above are the HIG mapping (C3, approved 2026-10-18, applied in step 3b): the title went 38 → 34 and meta 14 → 15; finish time (32px) and date day (30px) stay as display figures (attribute a). They're the sizes at the default text size: every size is a number of type units (`--type-unit`, 1rem ÷ 16 in browsers, 1rem ÷ 17 on iOS, where the root follows Dynamic Type), so text grows with the system setting (G28). The 68px date column grows with it. At 200% (the top of the range) every screen still fits 390 wide: the finish time wraps under a result's name, List/Map drops under Filters, a date pill under its label, and Result detail's leading time stops at `--size-time-hero-cap` (22vw); `scripts/check_overflow.mjs` checks every state at 200% (step 7).

### Named Rules
**The Three Shouts Rule.** The display face is used for the screen title, the finish time and the date day, and nowhere else. Race names, chips, buttons, tabs and meta are the text face.

**The Name Stays Rule.** Uppercase is `text-transform` only. The format name in the markup never changes.

## Layout

- **Screen:** 390px wide (`--screen-w`), one column, scrolling inside `.phone-screen`. Content runs under the floating tab bar; 72px of bottom padding (bar + gap + safe area) lets the last item scroll clear of it.
- **Gutter:** 16px (`--space-4`) on every side of the content.
- **Header:** `8px 16px 4px` below the top safe area, gap 12px. A top bar floats over it on every tab screen (44px, transparent and empty at rest, see Navigation); on Results list it carries Log result at its trailing edge, level with the title.
- **Controls (Race browse):** sticky below the top safe area on ground glass, padding `12px 16px`, the glass rim under it. The List/Map track (a capsule, equal segments) sits at the row's end at its full size and never shrinks; the Filters button takes the remaining width and shrinks down to its label, never below it. The bar is never wider than the screen (its grid column is `minmax(0, 1fr)`). Active filter chips scroll in one row, 12px apart, which fades out over its last 24px; chips never shrink or truncate, only the scroll edge cuts them. "Clear all filters" is pinned 12px after the row, always whole. Checked at 390 and 320 wide with 0–5 filters by `scripts/check_overflow.mjs` (2026-10-24).
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

Flat by default. Depth comes from tonal layering: the tab bar (`--graphite-5`) under the page (`--page`) under cards (`--surface`) under raised controls (`--raised`) under pressed fills (`--pressed`). Cards have no shadow and no border at rest. On hover a card gets a 1px inset ring in `--boundary`.

### Shadow Vocabulary
- **Float** (`box-shadow: 0 12px 32px -12px`, black at 60%, `--float-shadow`): what floats over content, the Filters sheet and (since step 3b) the floating tab bar. A scrim of black at 60% (`--scrim`) dims the page behind the sheet.

### Named Rules
**The Float Rule.** Only what floats casts a shadow: the sheet and the floating tab bar. Everything else is a tone step.

**The Glass Rule (C1, step 3b).** Bars and the sheet are glass (see Colors → Glass); content never is. A card, a row, a chip or a field stays a flat tone.

## Shapes

Slightly rounded in content, never sharp. Pills only in bar chrome (C7).
- **4px** (`--radius-1`), inner shapes: the photo inside a card, the date tile, format chips, List/Map segments, skeleton bars, map pin labels.
- **6px** (`--radius-2`), outer shapes: cards, result rows, the Race detail photo (it sits on the page), buttons outside bars, the date pills, the Sign in segmented track, the saved confirmation, the map frame.
- **Bar chrome (step 3b; designer decision 2026-10-19, C7):** bar controls are all full capsules, iOS 26 style: radius = half the height. The floating tab bar (`--radius-tabbar`, 32px); the search field, the Filters button and the List/Map track (`--radius-bar-control`, 22px); the List/Map segment concentric inside (`--radius-bar-inner`, 18px = 22 − the 4px track padding); the action bar's Register / Open button (22px, step 5); the active filter chips (`--radius-filter-chip`, 16px = half of 32; designer 2026-10-22). Content (cards, format chips, tiles, buttons outside bars) keeps 4/6px.
- **Sheet** (`--radius-sheet`, 38px [?]): the top corners of the Filters sheet and the Log result sheet, the native sheet radius (Race picker is a pushed screen with square corners since 2026-10-24); also the receded edge of Results behind the Log result sheet. Replaces the 12px they had until step 3b. `--radius-3` (12px) is now stand panels only.
- **Confirm alert** (`--radius-alert`, 34px [?]): as iOS 26 alerts (G67, designer 2026-10-23), provisional like the sheet radius. Its last row of buttons follows the corners, so the inset focus ring and the hover fill do too (step 6).
- **Tab bar** (`--radius-tabbar`, 32px = half its 64px height): the floating capsule.
- **Circles:** the map pin dot, the busy spinner, and **Profile initials** (`--radius-avatar`, 50%): the one exception to "no circles in content", because iOS avatars are circular (designer, 2026-10-19).
- **Borders** are drawn as 1px inset box-shadows (`--border`), so they never change a box's size.

## Components

### Buttons
Exactly one filled button per screen.
- **Shape:** 6px radius, 44px minimum height, `0 20px` padding, 15px / 600, 8px gap to an 18px icon.
- **Primary:** `--accent-fill` fill, `--on-accent-fill` text. Hover `--accent-hover`. Pressed moves down 1px. Background and transform ease over 160ms (`--ease-out`, `cubic-bezier(0.2, 0.8, 0.2, 1)`); 0ms under reduced motion.
- **Secondary:** `--raised` fill, `--text-primary` text, hover `--pressed`. Filters on Race browse (with the Solar filters icon, `--pressed` while its sheet is open), "Type it in instead" on Race picker `-error`. (Race browse `-empty` has one "Clear all filters" since step 6: the pinned link in the chips row; its state's own action is "Change filters".)
- **Tertiary:** a text link, 15px / 400, `--text-primary`, 1px underline 4px below, hover `--text-secondary`, a 44pt target. "Clear all filters" in the chips row; "Copy link" under the official result link (Result detail, step 6); "Unlink race" on the linked race card (on the sheet's `--group`, a tonal fill would vanish; step 6); the check-inbox links, left-aligned with their text.
- **Stepping down:** when a state block brings its own primary (Try again on Results list `-error`), the bar's Log result turns Text 1, so the screen keeps two lights; on `-empty` it's hidden and "Log your first result" is the one way in (markup pass, 2026-10-23).
- **Disabled:** `--raised` fill, `--text-disabled` text. **Busy** (`aria-busy="true"`): same fill, a 15px CSS spinner (a 2px ring in the label's color, one turn per 800ms, still turning under reduced motion, as HIG asks) before the present-tense verb ("Saving…") (G26).
- **Pressed cards and rows:** a race card or a result row takes `--pressed` while pressed (G23).

### Chips
- **Format chip** (metadata): `--raised` fill, `--chip-text`, 4px radius, 24px tall, `0 8px`, 11px / 600 uppercase, 0.07em. The same for every format: no per-format color.
- **Active filter chip** (a removable state, in the controls bar): an iOS capsule (16px radius, C7) in a quiet `--raised` fill with no outline; the format's own name in sentence case, 13px / 600 `--text-primary` (13.05:1); 32px tall (44px tap area), `0 8px 0 12px`; the 15px Solar close-circle inside, 4px after the name, in `--text-secondary` (6.01:1). Hover `--pressed`. Designer, 2026-10-22.

### Cards / Containers
- **Race card:** `--surface`, 6px radius, 8px padding, flat. The whole card is one link, photo included. Inside it: a black-and-white photo (`grayscale(1) contrast(1.12) brightness(0.85)`) at 3:1 with a 4px radius, the file itself pre-cropped to its 3:1 band (684 and 1026 px wide, AVIF / WebP / JPEG, `srcset`; step 7, `visuals/README.md` → Export); then the date tile (68px wide, `--raised`, 4px radius, `12px 4px` padding, the day in Schibsted 30px `--text-primary` over the month and year in 13px `--text-secondary`); then the race name (17px / 600), the format chip, and the location (14px `--text-secondary` with a 15px Solar map-point icon).
- **Result row:** `--surface`, 6px radius, `12px 16px 16px` padding, 8px gaps. A 15px Solar alt-arrow-right in `--text-secondary` ends the meta row, under the finish time's right edge: the row drills into Result detail (G22). The finish time and the proof line keep the row's full width, so the time sits where it always did and no proof line wraps. Race cards are a collection, so they have none. The race name on the left and the finish time (Schibsted 32px) on the right, sharing a baseline; then the format chip and the date (15px `--text-secondary`, C3); then the proof line (13px `--text-secondary`, one 15px Solar link icon, wraps anywhere).
- **Race detail** (step 5, 2026-10-22): a drill-down with no tab bar. Under the ground-glass top bar ("‹ Discover", a Solar back chevron): the race's photo, the same file, 3:1 band and focus class as its card (so exactly the band retouched in round 3), at full content width (358 × 119 at 390), 6px radius, black and white (a designer decision, 2026-10-22: a structural exception to the wireframe); the race name as the 34px title; the facts as a two-column list (labels 15px `--text-secondary`, values `--text-primary`); "About this race" and "Official race website" as 17px / 600 headings over 15px body; the official site an underlined `--text-primary` link with a 44pt target (G36). The page scrolls above the action bar and stops at its top edge (G35, markup pass). Loading: the same zones as `--raised` bars, the photo band included.
- **Saved confirmation:** `--surface`, 6px radius, `12px 16px`, 14px `--text-primary` with the race name in 600, and an 18px Solar save glyph in `--text-secondary`. Never green, never a check.
- **Skeletons (loading):** `--raised` bars with a 4px radius, in the exact shape of the card or row they stand for. The finish-time bar is 32px tall, so nothing shifts. A subtle pulse (opacity to 0.55 and back over 1.6s), still under reduced motion (C6). No spinner, no shimmer.

### Inputs / Fields
- **Search field:** `--surface`, a full capsule (C7), 44px tall, a 1px `--boundary` inset boundary, an 18px Solar magnifier (Linear, step 6) in `--text-secondary` 16px in from the start, placeholder in `--text-secondary`. Hover: the boundary turns `--text-secondary`. Focus: a 2px `--text-primary` outline replaces it. Filled and focused, it shows the browser's own Clear button (system-drawn, C2; G10).
- **Form rows (round 2, 2026-10-23):** Log result and the sign-in screens are grouped forms, as iOS: a label (15px Text 1) and its field in a 44px row on the rows' level (`--surface` on the page, `--group` on a sheet), the value in Text 1, left-aligned; a long value (the official result link) stacks under its label. Pickers sit at the row's trailing edge: a menu value with its chevron, a date on a `--raised` pill. Editable text values are Text 1; read-only values (Profile's Email) and menu values are Text 2, as iOS Settings (designer, step 6). Hints are the group's footer (13px Text 2); an error sits under its row (15px / 600 Text 1 after an 18px coral icon; Profile's row error is the same since step 6), and the invalid rows take one 2px `--error` ring (`--invalid-ring` wide) inside, around each run of adjacent invalid rows, with the hairlines that touch it hidden (step 6); focus is the white ring outside, so the two never look alike. A navigation row (Find in race catalog) ends in a Text 2 disclosure chevron; it goes while a race is linked (the card's Unlink changes it; step 6). The finish time takes the numeric keypad. Empty required fields hold the bar's confirm in Text disabled until they're filled (Sign in, Create, Send; step 6, HIG Sheets), so an empty submit never reaches the browser's bubble; password rows say "Required". While saving, the whole form is locked in one treatment: every control in Text disabled, the bar's Cancel with it; the help text stays Text 2 (step 6).
- **Date pill** (step 6, 2026-10-25; one button since step 7): the date written as the chips and cards write it ("23 Sep 2026"), 15px Text 1 on a `--raised` pill (6px radius). The pill is one button (one Tab stop, one focus ring; its name "23 Sep 2026, race date") that opens the system's calendar (`showPicker()`); the native date input beside it holds the value, out of the tab order. At large text sizes the pill goes under its label. No glyph and no browser locale mask: empty, it says "Choose a date" in Text 2. Filters sheet (From, To), Log result (Race date).
- **Checkmark row:** a sport type is a row; checked, a 26px Solar check in `--text-primary` (the control tint, C4) at its trailing edge (the glyph about 17px wide, as HIG's list checkmark; step 6), nothing when off. Race picker's linked race carries the same checkmark. Never the accent. Every system-drawn control takes the same tint (`accent-color`, C4).
- **Sort button:** one button that flips the order, showing the current one: "Soonest first" in `--text-primary` 15px / 600, then the 15px Solar sort icon (G21; markup pass, 2026-10-23). Its name starts with its label: "Soonest first, sort order". Disabled in `--text-disabled` while loading; a 44pt target inside the row's text height. It never shrinks and never wraps: the count beside it takes the remaining width and wraps there instead (2026-10-25; checked at 320 by `scripts/check_overflow.mjs`).
- **Focus (everything):** a 2px `--text-primary` outline, 2px offset. Never the accent.

### Navigation
- **Tab bar:** a floating 64px capsule of tab-bar glass with a faint rim and the float shadow, three tabs (Discover, Results, Profile). Each has a 26px Solar icon (compass, stopwatch, user) over an 11px / 600 label. Inactive: `--text-secondary`. Current: `--accent-ink`, icon and label.
- **List / Map segmented control:** a `--raised` track with 4px padding; in the controls bar a 22px capsule with 18px segments (C7), in content (Sign in) 6px with 4px segments. Segments are of equal width (G11), 36px (44px tap area), 15px / 600, `--text-secondary`.
- **Action bar (Race detail, Result detail):** tab-bar glass with a rim instead of the hairline, above the bottom safe area (C1, designer 2026-10-19). Its caption passes AA over the worst case behind it. Its one button (Register on \<domain\>, Open official result) is the screen's amber primary and a 22px capsule, as every control inside a bar (C7, step 5). On a drill-down the top bar and the action bar are transparent, with no rim, while nothing runs under them (iOS 26 scroll edge; step 6): glass once content scrolls under. A link that won't open is the confirm alert (markup pass).
- **Top bar:** one element on every screen, `header.top-bar` (step 7); ground glass with a rim, below the top safe area; its text buttons 17px. The back link is `a.back`, its Solar Linear chevron drawn by the kit (no glyph in the markup). Back (a Solar Linear chevron and the parent's name) and Cancel in `--text-primary`; Save on Log result in `--accent-ink` (that screen's one primary); saving, the spinner alone, Cancel locked. The sign-in screens' title is "Account" in both modes (step 6): the segmented switch carries the mode, the bar action does it.
- **Collapsing title (G4, G34, G53; markup pass, 2026-10-23):** on Race browse, Results and Profile a top bar floats over the large title, transparent and empty at rest; once the h1 has mostly scrolled away it turns to ground glass with its rim and shows the small title (17px / 600), fading over 160ms. Race browse's controls stick under it. Race detail and Result detail show the race name in their bar the same way, truncated between the back button and the edge.
- **Bar action:** the screen's one primary in a bar, amber text 17px / 600 like a native bar button (15px until step 6): Save on Log result, Log result on Results (G5), Apply filters on the Filters sheet (G12). "Saving…" is the Save button with `aria-busy`: Text 2 and the spinner. On the sign-in screens it is the confirm action ("Sign in", "Create", "Send", "Save", short so it never meets the title; the accessible name starts with it). While it works, the spinner alone (round 2).
- **Confirm alert:** the sheet's glass over the scrim, with its blur and rim, 34px corners [?] (G67, designer 2026-10-23: as iOS 26 alerts). Sign out, the destructive action, is `--error` (coral) text, in the alert and in its Profile row (G68); Cancel stays `--text-primary` (HIG Alerts). The pressed segment is `--pressed`, `--text-primary`, with a 1px `--boundary` outline. Race detail uses the same alert for "Couldn’t open the race website", with one action, Dismiss, bold as the default (markup pass, 2026-10-23); its body says "Tap Register again" (step 6). Alert buttons are 17px (step 6). Result detail uses it too for "Couldn’t open the official result", with Dismiss and Try again (round 2); its body points to Copy link (step 6).

### The other screens (step 5, 2026-10-22)
- **Log result:** a modal sheet over Results (round 2, G40): the sheet glass at the large detent, Results receded under the scrim; Cancel (Text 1) on the leading edge of its bar, "Log result", **Save in amber text** (the one primary). Saving: the spinner alone in Save's place. A grouped form (see Form rows): the catalog row, the race facts (or the linked race's card), the finish time, the official result link, each with its footer. Cancel with anything entered opens the **action sheet**: two glass blocks at the bottom, 34px corners [?], a 13px Text 2 message ("This result isn’t saved yet."), **Discard result** in coral, and **Keep editing** apart below it, 600.
- **Race picker:** a screen pushed inside Log result's navigation, as picking a value in iOS Settings (designer, 2026-10-24; a sheet before): full-screen on the page ground, the ground-glass top bar with "‹ Log result" and "Find a race", no Cancel. Under it the search capsule (the page gutter, `--boundary`), the list intro, race cards on `--surface` without photos; the linked race carries the neutral checkmark (G47). Tapping a race goes back to Log result with it filled in. Its empty and error states sit on the page; "Type it in instead" is the amber primary on `-empty` (the state's one action) and the tonal secondary on `-error`, after Try again.
- **Result detail:** as Race detail, without a photo: the race name (Item, 17px / 600; step 6), then the finish time leading the screen (Schibsted 56px, `--size-time-hero`, the largest element; designer, step 6, attribute a) 4px under its label, the facts, the proof section (the full link, breaking only after / . -, then Copy link, the proof line, the note "Onrace doesn't verify results."), and the action bar's capsule "Open official result on \<domain\>". Round 2: the Open button reads "Open official result" (its name carries the domain), the caption "Opens the official timing site.", and a link that won't open is the confirm alert, so the action bar keeps one height.
- **Sign in / Sign up, Reset password, New password (the gates):** modals with a ground-glass top bar (Cancel or "‹ Sign in", the centered title) that floats over the page, which scrolls under it. A gate intro in `--text-secondary`, the Sign in / Create account segmented control (6px in content), fields, one full-width amber submit; busy: the spinner and the present-tense label, the form locked. Small text links (Forgot password?, Reset password again) have 44pt targets. Check your inbox: the address in 600, Send a new link (secondary, a spinner while sending). Full-screen errors (an expired reset or confirmation link) are the empty/error component on the page, not a box. Round 2 (G60, G61): the fields are a grouped form and the confirm action is the bar's trailing button, not a full-width button at the form's end.
- **Profile:** a top-level tab with the large title and the floating tab bar (the current tab its one amber). The initials in an 80px circle on `--raised`; the name and email; the grouped Account rows on `--surface` (44px; the editable Name in `--text-primary`, the read-only Email and the menu values (Country, Language) in `--text-secondary`, as iOS Settings: designer decisions, step 6 and step 7; a Solar chevron after Country and Language), the group footer; Sign out as a full-width `--surface` button in coral (`--error`, a destructive action; G68, 2026-10-23); its confirm alert with Cancel and Sign out in coral (`--destructive`).

### Empty and error states
One component, the iOS ContentUnavailableView pattern (designer, 2026-10-19). Centered horizontally and vertically in the free area below the header and above the floating tab bar: a 48px Solar icon on top (`--icon-state`), then a 17px / 600 heading, 15px `--text-secondary` body (65ch max), then actions in the button hierarchy, centered, 12px apart.
- **Empty:** a muted `--text-secondary` icon that names what's missing: magnifier on Race browse (nothing matches), archive on Results list (the results archive is empty).
- **Error:** Solar danger-circle in `--error`. Coral means error, and since 2026-10-23 also destructive (Sign out); nothing else turns red.
- Icons are CSS masks chosen by context; the markup is the wireframes'.
- **On the page, never framed** (designer, 2026-10-22): no outline, frame or surface around the state, on any screen. In Race browse's Map view, while the map holds an empty or error state, the map frame drops its outline, water and land, and the state has no panel: it looks as it does in List view. On a drill-down (Race detail) it is centered in the area under the top bar, with the 16px gutter.

### Filters sheet (signature)
Sheet glass (`--graphite-17` at 90%, blurred), 38px top corners [?] with a rim along the top edge, the float shadow, over the scrim. It rests at the large detent only, and slides up over 250ms (`--dur-sheet`, `--ease-out`; 0ms under reduced motion). Markup pass (2026-10-23): no grabber (one detent, not resizable); a top bar with Cancel (Text 1) on the leading edge, "Filters" (17px / 600) centered, Apply filters (amber text, the sheet's one primary) on the trailing edge (G12). The options are grouped rows on `--pressed`, the level above the sheet, 44px each with `--hairline` dividers (G20): Region shows its value in `--text-secondary` with a chevron and opens the native menu (G17); the race dates are compact pickers, the value in `--text-primary` on a `--raised` pill with a small Solar calendar (G18); under the "SPORT TYPE" group heading, seven rows with a neutral `--text-primary` checkmark at the trailing edge when chosen (G19, C4). Focus moves into the sheet when it opens, Escape closes it and focus returns to Filters.

### Static map (signature)
A frame in `--map-water` with a 1px `--boundary` boundary and a 6px radius. Natural Earth land is masked in `--map-land`, coastlines and borders in `--map-lines`. Pins: a 10px `--text-primary` dot ringed in water color on the real coordinate, and a 22px `--raised` label (11px / 600, `--text-primary`, 4px radius) joined by a 1px `--text-secondary` leader line. Each pin is a 44pt target centred on its label; the dot and the leader take no taps, so where dots nearly touch (Boston, Killington) each label is its own target (step 6). Hover lifts the label to `--pressed`. Each pin's place is map data in `ui/map.css`, keyed on its `data-pin`. No accent anywhere on the map. The map has no caption: the wireframe note in its place ("[ static map … ]") is hidden on the working pages (2026-10-23), as are the bracketed notes in its empty, error and loading states. While the map holds an empty or error state, the frame gives way (see Empty and error states). While it loads (`aria-busy`), the whole map surface pulses with the skeletons (C6: to 0.55 and back over 1.6s; still under reduced motion; designer 2026-10-23).

## Do's and Don'ts

### Do:
- **Do** keep the amber to the one primary button and the current tab: at most two uses per screen.
- **Do** make the finish time the loudest thing on a result row, through Schibsted 800 at 32px in `--text-primary`, not through color.
- **Do** lead a race card with the date tile (day 30px over month and year 13px) beside the name, chip and place.
- **Do** show every photo in black and white (`--photo-filter`), inset at 3:1 with a 4px radius.
- **Do** state proof as its own 13px `--text-secondary` line with one link icon: "Self-reported · via \<domain\>".
- **Do** step a secondary action up or down so the screen keeps exactly one filled button.
- **Do** take every value from `tokens/tokens.css`, and give components semantic roles, never color primitives. Pages and the components hold no raw values.
- **Do** draw icons as Solar Bold masks in the color of their text: 15px in meta, 18px in buttons and fields, 26px in the tab bar. The small UI glyphs (back, chevrons, disclosure, the search magnifier) are Solar Linear (designer exception, step 6).
- **Do** keep 44px targets, a 2px `--text-primary` focus ring, and 0ms motion under `prefers-reduced-motion` (skeletons still; only the busy spinner keeps turning).
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
- **Don't** use `--hairline` or `--boundary` as a fill.
- **Don't** let invalid and focus look alike: coral inside for invalid, white outside for focus.
- **Don't** use tabular figures on finish times: Schibsted spaces the colons wide ("24 : 36").

## Native iOS

**The rule (designer, 2026-10-18).** Every element with a native iOS counterpart follows Apple's Human Interface Guidelines for anatomy, metrics and behavior: sizes, placement, grabber, large title, safe areas, 44pt targets, sheet detents, and search and segmented-control behavior. Podium keeps the visual language: colors, fonts, Solar icons and photos. Where the two conflict, the designer decides: the seven conflicts (**C1–C7**) were decided on 2026-10-18, below. `concept/concept.md` → Native iOS holds the 33 gaps (G1–G33) between today's screens and HIG and their triage (15 kit, 13 markup pass, 5 out of scope). The screens change through the kit in steps 3 and 5.

HIG read on 2026-10-18; every link returned HTTP 200. "System" means HIG publishes no number and the system draws it.

| Component on the screens | HIG page | What native means for it | What Podium keeps |
|---|---|---|---|
| Tab bar (Discover, Results, Profile) | [Tab bars](https://developer.apple.com/design/human-interface-guidelines/tab-bars) | For navigation, not actions. Visible in every section; only a modal may cover it. Labels under icons, single words where possible. Prefer filled icons. On iOS it floats above content at the bottom on a Liquid Glass background, and content shows through beneath it. It may include a search tab at the trailing end. | Solar bold icons (filled, as HIG prefers), Hanken labels, amber on the current tab. Material: translucent graphite with blur in Podium tones (**C1**). Icons: Solar (**C2**). |
| Screen title ("Discover", "Results") and top bar | [Toolbars](https://developer.apple.com/design/human-interface-guidelines/toolbars), [Typography](https://developer.apple.com/design/human-interface-guidelines/typography) | A large title that turns into a standard inline title in the top bar as people scroll, and back to large at the top. Titles under 15 characters. Actions sit in the toolbar; the key action uses the `.prominent` style, only one, on the trailing side. Prefer symbols to text for toolbar items. Fewer custom toolbar backgrounds: a scroll edge effect separates bar and content. | The title's text in Schibsted Grotesk 800 at Large Title size, 34 (**C3**). Top bar: translucent graphite with blur (**C1**). The amber on the one primary action. |
| Search field (Race browse) | [Search fields](https://developer.apple.com/design/human-interface-guidelines/search-fields), [Text fields](https://developer.apple.com/design/human-interface-guidelines/text-fields) | A search icon, placeholder text, and a Clear button at the trailing end. Search starts as people type. An inline field sits above the list it filters and can pin to the top toolbar on scroll. Bottom-toolbar search or a search tab are the other native placements. | `--surface` field, `--boundary` boundary, Solar magnifier (**C2**), the placeholder "Race name or city". Inside a bar, its corners are concentric with the bar (**C7**). |
| List / Map segmented control | [Segmented controls](https://developer.apple.com/design/human-interface-guidelines/segmented-controls) | For closely related subviews (List and Map qualify). Segments of equal width, text only, nouns, at most about five on iPhone. | `--raised` track, `--pressed` selected segment, Hanken 15/600. Inside the controls bar, corners concentric with the bar (**C7**). |
| Buttons (Filters, Log result, state actions, sheet actions) | [Buttons](https://developer.apple.com/design/human-interface-guidelines/buttons) | Hit region at least 44×44pt. A press state on every custom button. One or two prominent buttons per view. Style, not size, separates the preferred choice. The primary role takes the accent. A delayed action shows an activity indicator inside the button, with an alternative label ("Checking out…"). | Amber primary, tonal secondary, underlined tertiary, Hanken 15/600, the 1px press. Buttons in content keep 6px (**C7**); a button inside a bar is concentric with it. |
| Filters sheet | [Sheets](https://developer.apple.com/design/human-interface-guidelines/sheets) | See *Native sheet anatomy* below. | Our raised graphite level as its background (**C4**), translucent with blur (**C1**), the scrim, Hanken type, Solar icons inside. |
| Region select (sheet) | [Pull-down buttons](https://developer.apple.com/design/human-interface-guidelines/pull-down-buttons), [Pickers](https://developer.apple.com/design/human-interface-guidelines/pickers) | A short list of choices (6 regions) is a menu from a button, not a picker. Mutually exclusive choices that aren't commands belong in a pop-up button, which shows the current value. | The button: Hanken 15, `--text-primary` value, Solar chevron (**C2**). The menu it opens is the system's (**C2**). |
| Race date from / to (sheet) | [Pickers](https://developer.apple.com/design/human-interface-guidelines/pickers) | A compact date picker: a button showing the current value in the app's accent color, which opens a calendar editor in a modal view. Values and their order follow the device's locale. | The date picker is drawn by the system (**C2**). Its tint is neutral text color, not amber (**C4**). Hanken type on our button. |
| Sport-type choices (sheet) | [Toggles](https://developer.apple.com/design/human-interface-guidelines/toggles), [Lists and tables](https://developer.apple.com/design/human-interface-guidelines/lists-and-tables) | iOS has no checkbox. In a list row, use a switch (default green, or the app's accent), or a selectable row that adds a checkmark when chosen. Outside a list, use a button that behaves like a toggle. | Hanken 15 labels, `--text-primary`. Checkmark or switch tinted in neutral text color, never amber or green (**C4**). |
| Sort ("Sort: Soonest first") | [Pull-down buttons](https://developer.apple.com/design/human-interface-guidelines/pull-down-buttons) | A button that opens a menu; sorting is HIG's own example. A menu should list at least three items; for one or two, consider other controls. For mutually exclusive choices, use a pop-up button. | Hanken 15/600, "Sort:" in `--text-secondary`, Solar chevron on our button (**C2**). The menu is the system's (**C2**). |
| Result rows; race cards | [Lists and tables](https://developer.apple.com/design/human-interface-guidelines/lists-and-tables) | A row that drills into a detail view shows a disclosure indicator. Selection gives feedback (a highlight). Items that vary in size or carry many images suit a collection rather than a list, so the photo-led race cards are a collection. | Cards, photos, the date tile, the finish time, the proof line, 4/6px radii (content keeps 4/6, **C7**). Disclosure chevron in Solar (**C2**). Never glass (**C1**). |
| Error states | [Alerts](https://developer.apple.com/design/human-interface-guidelines/alerts) | Don't use an alert only to inform, or for a connection problem: show it in context with a non-intrusive label. An alert is for something people must act on. | The inline state message, the coral icon. No gap: the screens already do this. |
| Loading | [Progress indicators](https://developer.apple.com/design/human-interface-guidelines/progress-indicators) | Indeterminate loading uses an activity indicator, and indicators keep moving ("people associate a stationary indicator with a stalled process"). Lists support pull-to-refresh, and content also refreshes on its own. | Skeleton shapes in `--raised` with a subtle pulse, still under Reduce Motion (**C6**). |
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
- **Background:** sheet glass, `--raised` at 90% with blur (C1, C4), since step 3b.

### HIG vs Podium: decided (designer, 2026-10-18)

- **C1 Liquid Glass:** adopted for bars (tab bar, top bar, controls bar, and the action bar, added 2026-10-19) and the Filters sheet: translucent graphite with blur, in Podium's tones. Never on cards; content stays flat. Applied in step 3b (see Colors → Glass).
- **C2 Icons:** Solar stays for our icons. Controls the system draws (the date picker, system menus) stay system.
- **C3 Fonts:** Schibsted Grotesk and Hanken Grotesk stay, with Podium's scale mapped onto the HIG text styles. Approved 2026-10-18: title 38 → Large Title 34; item 17 = Headline; body and buttons 15 = Subheadline; meta 14 → Subheadline 15; proof 13 = Footnote; labels 11 = Caption 2; finish time 32 and date day 30 stay as display figures (attribute a). Measured before C1: the first screen kept two full race cards (9.7px to spare in the viewer, was 8.6px). After C1 (step 3b), with content under the floating glass tab bar: two full cards clear of the bar, 1.7px to spare (see Layout).
- **C4 Control tint:** neutral (text color) for checkmarks and switches. Amber stays only per Color rule 1. The sheet's background is the raised graphite level, `--raised` (confirmed 2026-10-18).
- **C5 Dark only:** kept, as a designer decision. Dark is Onrace's identity from the brand tone and the attributes, and every color rule and contrast check is built for it.
- **C6 Loading:** a subtle pulse on skeletons, still under reduced motion.
- **C7 Corners:** concentric only for elements inside bars. **Designer decision, 2026-10-19:** bar controls are all full capsules, iOS 26 style (radius = half the height): the search field, the Filters button and the List/Map control, with the segment concentric inside. Content (cards, chips, tiles, buttons outside bars) keeps 4/6px.

## Sources

- [`concept/concept.md`](concept/concept.md): the rules and every decision behind these values (Designer's taste, Hierarchy rules, Color rules, race card anatomy, Results list details, Map, Deferred to Lesson 7).
- [`concept/references.md`](concept/references.md): the references, the techniques taken and the anti-references, and the photo log.
- Values: [`tokens/tokens.css`](tokens/tokens.css) (and the map data [`ui/map-data.css`](ui/map-data.css)); components: [`components/`](components/README.md), bundled into [`components/index.css`](components/index.css); the showcase [`ui/kit.html`](ui/kit.html) and the shell [`ui/shell.html`](ui/shell.html); the inventory [`ui/inventory.md`](ui/inventory.md). Signed reasons for each token: the stand, [`concept/concept.html`](concept/concept.html).
