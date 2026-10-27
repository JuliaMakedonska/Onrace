# Tokens audit: Lesson 8, step 1 (2026-10-27)

An audit of the kit's values before the refactor. **Nothing was changed or renamed:** this file only records what is there.

## What was read

- **Product values:**
  - `ui/kit.css`: its `:root`, the `@media (prefers-reduced-motion)` / `(prefers-reduced-transparency)` overrides and the Dynamic Type `@supports` block;
  - `ui/map.css`.
- **Every page that uses them:**
  - all 35 `wireframes/*.html` pages (10 screens with their states);
  - `ui/kit.html` and `ui/shell.html`;
  - `concept/concept.html` and `concept/first-screen.html`;
  - the review pages: `ui/review-*.html` (10) and `visuals/review-round3.html`.
  - Skipped: `wireframes/_wireframe/` (frozen) and `wireframes/index.html` (the viewer, with its own `<style>`, which links no kit file).
- **No inline values on the pages:** no product page has a `style=""` attribute or a `<style>` block, so every value reaches the screens through the two CSS files.
- **The docs layer is listed separately, not audited as tokens:** `ui/kit-doc.css`, `concept/stand.css` and `concept/specimens.css` (see "Docs layer" below).

## Counts

- **Tokens:**
  - 174 unique tokens: 144 in `kit.css` and 30 in `map.css`;
  - not counted as tokens: the component-local custom properties set per rule, `--ring-top`, `--ring-sides`, `--ring-bottom`, `--state-icon`, `--state-icon-color` and `--tab-icon` in `kit.css`, and `--x`, `--yf`, `--dy` and `--dy-abs` on each map pin;
  - 180 definitions, counting the reduced-motion, reduced-transparency and Dynamic Type overrides;
  - 1,314 `var()` uses across 2,284 declarations.
- **Unused tokens:** none are unused by everything. Five have no product use: `--font-mono`, `--stand-max`, `--stand-col-min` and `--space-9` (docs layer only), and `--radius-3` (the showcase frame only).

## How to read the table

- **Files:** the files where the token is defined or used (`kit.css`, `map.css`).
- **Where it is used:** the CSS property × the number of rules, with up to four selectors (`…` means more). "Aliased by" means another token is defined from this one.
- **Screens:** the wireframe screens whose markup the selectors match, plus the non-screen pages.
- **Docs:** uses in the docs layer.
- **Role(s):** what the token does in each place. Where a token plays more than one role, they're split by `;`, and a **bold** role is one that the findings below call out.

## The table (174 tokens)

| Variable | Value | Files | Where it is used (property × selectors) | Screens | Docs | Role(s) |
|---|---|---|---|---|---|---|
| `--bg-bar` | `#0F1114` | kit.css, map.css | aliased by `--glass-bar`, `--map-water`; background ×1: `body:has(> .sheet > .phone-screen)` | 10 screens · kit.html, shell.html | docs ×3 | frame / void (behind the sheet); base of glass bar; map water |
| `--bg-0` | `#131518` | kit.css | aliased by `--glass-ground`; background ×3: `.onrace`, `.kit-frame`, `.kit-shell`; color ×1: `.onrace ::selection` | 10 screens · concept.html, first-screen.html, kit.html, shell.html | docs ×2 | page background; base of glass ground; kit stage; ::selection text |
| `--bg-1` | `#1D2024` | kit.css, map.css | aliased by `--map-land`; background ×9: `.race-search input, .phone-screen > form`, `.race-card`, `.result-card .card-link`, `.skeleton-card` … | 10 screens · concept.html, first-screen.html, kit.html, shell.html | docs ×2 | surface (cards, rows, search field, saved status, Sign out); map land |
| `--bg-2` | `#272B30` | kit.css | aliased by `--glass-sheet`; background ×14: `.filters-trigger, .state-action.secondar`, `.sport-tag`, `.chip`, `.race-card time` … | 9 screens · concept.html, first-screen.html, kit.html | docs ×4 | raised (secondary buttons, chips, date tile, segmented track, skeleton bars, pin labels, initials); base of glass sheet; **hover/pressed on rows** (`.row--check:active`, `a.row--nav:hover`, `.signout:hover`) |
| `--bg-3` | `#2C3035` | kit.css, map.css | aliased by `--map-lines`; background ×12: `.filters-trigger:hover, .state-action.se`, `.chip:hover`, `.view-btn[aria-pressed="true"]`, `.filters-trigger[aria-expanded="true"]` … | 10 screens · concept.html, first-screen.html, kit.html | docs ×2 | pressed/hover/open on raised controls; pressed card (from bg-1); rows group on the sheet; `.linked-race`; map lines |
| `--line` | `#31363C` | kit.css | border-bottom ×2: `.controls`, `.action-sheet .action-message`; border-left ×2: `.results-order`, `dialog.alert .alert-actions button + but`; border-top ×2: `.rows li + li::before`, `dialog.alert .alert-actions`; box-shadow ×2: `.kit-frame`, `.kit-shell` | 9 screens · concept.html, first-screen.html, kit.html | docs ×6 | hairline divider (lists, bars, alert buttons); kit frame outline |
| `--field-line` | `#686E75` | kit.css | box-shadow ×5: `.race-search input, .phone-screen > form`, `.view-btn[aria-pressed="true"]`, `.race-card:hover .card-link::after`, `.map-placeholder` …; scrollbar-color ×1: `.sheet, .phone-screen` | 10 screens · concept.html, first-screen.html, kit.html, shell.html | docs ×1 | input boundary; pressed segment outline; card hover ring; map frame; scrollbar |
| `--text-1` | `#F4F5F6` | kit.css | aliased by `--focus`, `--control-tint`; color ×50: `.onrace`, `.onrace h1`, `.filters-trigger, .state-action.secondar`, `.clear-all` …; background ×2: `.onrace ::selection`, `.map-pin::before` | 10 screens · concept.html, first-screen.html, kit.html, shell.html | docs ×16 | primary text; aliased as focus and control tint; ::selection fill; map pin dot |
| `--text-2` | `#A3A9B0` | kit.css | color ×39: `.clear-all:hover`, `.race-search input::placeholder, .phone-`, `.race-card time`, `.race-card .card-location` …; background ×7: `.chip span`, `.race-search::before, .phone-screen > fo`, `.map-pin::after`, `.result-card .card-meta::after` …; box-shadow ×1: `.race-search input:hover, .phone-screen `; --state-icon-color ×1: `.state-message, .state-msg` | 10 screens · concept.html, first-screen.html, kit.html, shell.html | docs ×16 | secondary text; placeholder; inactive tab; glyph fill (chip ×, search, disclosure, chevron); search hover boundary; map leader line; empty-state icon; link hover |
| `--text-disabled` | `#6B7178` | kit.css | color ×10: `.sort-toggle:disabled`, `fieldset:disabled :is(.row label, .row .`, `fieldset:disabled .row input::placeholde`, `fieldset:disabled .date-pill, fieldset:d` …; background ×1: `fieldset:disabled :is(.row:has(> select)` | 10 screens · concept.html, first-screen.html, kit.html, shell.html | docs ×4 | disabled control text and glyphs |
| `--chip-text` | `#BFC4CA` | kit.css | color ×1: `.sport-tag` | Race browse, Results list, Race picker · concept.html, first-screen.html, kit.html | docs ×1 | format chip label |
| `--accent` | `#F5B649` | kit.css | background ×2: `.state-action:not(.secondary)`, `.register-btn, .open-btn, .submit-btn`; color ×2: `.bottom-nav a[aria-current="page"]`, `.top-bar .save-btn, .top-bar .bar-action` | 10 screens · concept.html, first-screen.html, kit.html, shell.html | docs ×2 | **primary action fill; bar action text (Save); current tab** |
| `--accent-hover` | `#FFC46A` | kit.css | background ×2: `.state-action:not(.secondary):hover`, `.register-btn:hover, .open-btn:hover, .s`; color ×1: `.top-bar .save-btn:hover, .top-bar .bar-` | 10 screens · concept.html, kit.html, shell.html | docs ×2 | hover of the same three: primary fill, bar action, current tab |
| `--on-accent` | `#131518` | kit.css | color ×2: `.state-action:not(.secondary)`, `.register-btn, .open-btn, .submit-btn` | 8 screens · concept.html, kit.html | docs ×2 | text/icon on the primary fill |
| `--error` | `#EE8B84` | kit.css | aliased by `--invalid`, `--destructive`; background ×2: `.inline-error h2::before, .form-alert h2`, `.gate > section:has(> .inline-error + .s`; --state-icon-color ×1: `.state-message[role="alert"], .state-mes` | 10 screens · concept.html, kit.html | docs ×2 | error state icon; alert/form error icon; base of invalid and destructive |
| `--error-bg` | `#3A2F31` | kit.css | background ×1: `.inline-error, .form-alert` | Log result, Sign in, Reset password, New password · kit.html | docs ×2 | error surface (inline error, form alert) |
| `--focus` | `var(--text-1)` | kit.css | outline ×6: `.onrace :focus-visible`, `.race-search input:focus-visible, .phone`, `.race-card .card-link:focus-visible::aft`, `.date-pill:has(.date-value:focus-visible` … | 10 screens · concept.html, first-screen.html, kit.html, shell.html | docs ×2 | focus ring |
| `--invalid` | `var(--error)` | kit.css | --ring-sides ×2: `.rows li:has([aria-invalid="true"])`, `.rows li:has([aria-invalid="true"])`; --ring-top ×1: `.rows li:has([aria-invalid="true"])`; --ring-bottom ×1: `.rows li:has([aria-invalid="true"])` | Race browse, Log result, Sign in, Reset password, New password, Profile · kit.html |  | invalid field ring |
| `--destructive` | `var(--error)` | kit.css | color ×3: `.signout`, `dialog.alert #signout-confirm`, `.action-sheet .is-destructive` | Race detail, Log result, Result detail, Profile · kit.html |  | destructive action text (Sign out, its alert button, action sheet) |
| `--control-tint` | `var(--text-1)` | kit.css | background ×2: `.race-card:has(.card-link[aria-current="`, `.row--check input[type="checkbox"]`; accent-color ×1: `.onrace` | 10 screens · concept.html, first-screen.html, kit.html, shell.html |  | checkmark, checkbox, accent-color of system controls |
| `--glass-opacity` | `85%`; `100%` (reduced transparency) | kit.css | aliased by `--glass-bar`, `--glass-ground` | — |  | glass fill strength for bars |
| `--glass-opacity-sheet` | `90%`; `100%` (reduced transparency) | kit.css | aliased by `--glass-sheet` | — |  | glass fill strength for the sheet and alerts |
| `--glass-bar` | `color-mix(in srgb, var(--bg-bar) var(--glass-opa…` | kit.css | background ×2: `.bottom-nav`, `.action-bar` | Race browse, Race detail, Results list, Result detail, Profile · concept.html, first-screen.html, kit.html, shell.html |  | floating tab bar, action bar |
| `--glass-ground` | `color-mix(in srgb, var(--bg-0) var(--glass-opaci…` | kit.css | background ×4: `.phone-screen .controls`, `body:has(> .phone-screen)::before`, `.top-bar`, `.top-bar--large.is-collapsed` | 10 screens · concept.html, first-screen.html, kit.html, shell.html |  | bars over the page: controls bar, top bar, status-bar edge |
| `--glass-sheet` | `color-mix(in srgb, var(--bg-2) var(--glass-opaci…` | kit.css | background ×3: `.sheet`, `dialog.alert`, `.action-sheet .action-group, .action-she` | Race browse, Race detail, Log result, Result detail, Profile · kit.html |  | Filters sheet, alert, action sheet |
| `--glass-blur` | `20px`; `0px` (reduced transparency) | kit.css | -webkit-backdrop-filter ×9: `.bottom-nav`, `.phone-screen .controls`, `body:has(> .phone-screen)::before`, `.sheet` …; backdrop-filter ×9: `.bottom-nav`, `.phone-screen .controls`, `body:has(> .phone-screen)::before`, `.sheet` … | 10 screens · concept.html, first-screen.html, kit.html, shell.html |  | backdrop blur of every glass surface |
| `--glass-edge` | `rgba(244, 245, 246, 0.08)` | kit.css | box-shadow ×4: `body > .bottom-nav, .kit-tabbar > .botto`, `.sheet`, `dialog.alert`, `.action-sheet .action-group, .action-she`; border-bottom-color ×2: `.phone-screen .controls`, `.top-bar--large.is-collapsed`; border-bottom ×1: `.top-bar`; border-top ×1: `.action-bar` | 10 screens · concept.html, first-screen.html, kit.html, shell.html |  | rim of every glass surface (tab bar, sheet, alert, action sheet) |
| `--font-display` | `"Schibsted Grotesk", "Hanken Grotesk", sans-seri…` | kit.css | font-family ×4: `.onrace h1`, `.race-card time .day`, `.finish-time`, `.finish dd` | 10 screens · concept.html, first-screen.html, kit.html, shell.html | docs ×2 | display face: title, finish time, date day |
| `--font-text` | `"Hanken Grotesk", sans-serif` | kit.css | font-family ×31: `.onrace`, `.filters-trigger, .state-action`, `.clear-all`, `.sport-tag` … | 10 screens · concept.html, first-screen.html, kit.html, shell.html | docs ×4 | text face: everything else |
| `--font-mono` | `ui-monospace, "SF Mono", Menlo, monospace` |  | — | — | docs ×1 | docs layer only (stand code) |
| `--type-root` | `16`; `17` (iOS Dynamic Type) | kit.css | aliased by `--type-unit` | — |  | Dynamic Type base (16, 17 on iOS) |
| `--type-unit` | `calc(1rem / var(--type-root))` | kit.css | aliased by `--size-title`, `--size-time`, `--size-time-hero`, `--size-day`, `--size-item`, `--size-body`, `--size-meta`, `--size-proof`, `--size-label`, `--date-col` | — |  | unit that scales every size token |
| `--size-title` | `calc(34 * var(--type-unit))` | kit.css | font-size ×1: `.onrace h1`; height ×1: `.bar.h1` | 10 screens · concept.html, first-screen.html, kit.html, shell.html | docs ×1 | screen title (Large Title); title skeleton |
| `--size-time` | `calc(32 * var(--type-unit))` | kit.css | aliased by `--skel-time-h`; font-size ×2: `.finish-time`, `.finish dd` | Results list, Result detail · concept.html, kit.html | docs ×2 | finish time in rows and facts; time skeleton |
| `--size-time-hero` | `calc(56 * var(--type-unit))` | kit.css | font-size ×1: `.result .finish dd`; height ×1: `.result .bar.finish-bar` | Race browse, Race detail, Results list, Race picker, Result detail, Profile · concept.html, kit.html | docs ×1 | finish time leading Result detail |
| `--size-time-hero-cap` | `22vw` | kit.css | font-size ×1: `.result .finish dd` | Result detail · kit.html |  | cap so the hero time fits the width |
| `--size-day` | `calc(30 * var(--type-unit))` | kit.css | font-size ×2: `.race-card time .day`, `.initials` | Race browse, Race picker, Profile · concept.html, first-screen.html, kit.html | docs ×1 | date day; **also the initials** in Profile |
| `--size-item` | `calc(17 * var(--type-unit))` | kit.css | font-size ×14: `.race-card h2`, `.card-top h2`, `.state-message :is(h1, h2), .state-msg h`, `.top-bar` …; height ×1: `.result .bar.h1` | 10 screens · concept.html, first-screen.html, kit.html, shell.html | docs ×1 | item title (race name), bar titles, state headings |
| `--size-body` | `calc(15 * var(--type-unit))` | kit.css | font-size ×17: `.onrace`, `.filters-trigger, .state-action`, `.race-search input, .phone-screen > form`, `.date-pill` …; margin ×1: `.official p` | 10 screens · concept.html, first-screen.html, kit.html, shell.html | docs ×3 | body, buttons, search (15) |
| `--size-meta` | `calc(15 * var(--type-unit))` | kit.css | font-size ×25: `.clear-all`, `.race-card .card-location`, `.result-card .card-meta`, `.view-btn` …; margin-block ×3: `.sort-toggle`, `.form-alert .alert-link`, `.form-alert .alert-link`; padding-block ×2: `.forgot a`, `.form-alert .alert-link`; margin ×1: `.copy-link` | 10 screens · concept.html, first-screen.html, kit.html | docs ×5 | meta: location, counts, segment labels (15, same as body) |
| `--size-proof` | `calc(13 * var(--type-unit))` | kit.css | font-size ×11: `.chip`, `.race-card time`, `.proof-label`, `.map-placeholder` …; margin-block ×1: `.result-list .skeleton-card .bar.proof`; padding-block ×1: `.row-note a` | 10 screens · concept.html, first-screen.html, kit.html | docs ×6 | proof line, month/year, filter chip, map labels |
| `--size-label` | `calc(11 * var(--type-unit))` | kit.css | font-size ×4: `.sport-tag`, `.bottom-nav a`, `.map-placeholder > .map-pin`, `.group-heading` | Race browse, Results list, Race picker, Profile · concept.html, first-screen.html, kit.html, shell.html |  | format chip, tab label, group heading, pin label |
| `--weight-display` | `800` | kit.css | font-weight ×4: `.onrace h1`, `.race-card time .day`, `.finish-time`, `.finish dd` | 10 screens · concept.html, first-screen.html, kit.html, shell.html | docs ×2 | display weight |
| `--weight-strong` | `600` | kit.css | font-weight ×35: `.onrace strong, .onrace b`, `.filters-trigger, .state-action`, `.sport-tag`, `.chip` … | 10 screens · concept.html, first-screen.html, kit.html, shell.html | docs ×9 | labels, buttons, titles |
| `--weight-regular` | `400` | kit.css | font-weight ×2: `.clear-all`, `.linked-race .unlink-btn` | Race browse, Log result · concept.html, first-screen.html, kit.html | docs ×1 | plain text buttons (Clear all, Unlink) |
| `--leading-tight` | `1` | kit.css | line-height ×8: `.onrace h1`, `.filters-trigger, .state-action`, `.sport-tag`, `.chip` … | 10 screens · concept.html, first-screen.html, kit.html, shell.html | docs ×3 | one-line controls and display |
| `--leading-item` | `1.2` | kit.css | line-height ×12: `.race-card h2`, `.race-card time`, `.card-top h2`, `.state-message :is(h1, h2), .state-msg h` …; height ×1: `.result .bar.h1` | 10 screens · concept.html, first-screen.html, kit.html, shell.html |  | titles and two-line items |
| `--leading-body` | `1.45` | kit.css | margin-block ×4: `.sort-toggle`, `.result-list .skeleton-card .bar.proof`, `.form-alert .alert-link`, `.form-alert .alert-link`; margin ×2: `.official p`, `.copy-link`; line-height ×1: `.onrace`; padding-block ×1: `.form-alert .alert-link` | 10 screens · concept.html, first-screen.html, kit.html, shell.html | docs ×1 | running text; also used as a spacing unit (margin-block) |
| `--tracking-display` | `-0.03em` | kit.css | letter-spacing ×4: `.onrace h1`, `.race-card time .day`, `.finish-time`, `.finish dd` | 10 screens · concept.html, first-screen.html, kit.html, shell.html | docs ×2 | display tightening |
| `--tracking-label` | `0.07em` | kit.css | letter-spacing ×2: `.sport-tag`, `.group-heading` | Race browse, Results list, Race picker, Profile · concept.html, first-screen.html, kit.html |  | uppercase label spacing |
| `--radius-1` | `4px` | kit.css | border-radius ×7: `.sport-tag`, `.race-card .photo`, `.race-card .card-link`, `.race-card time` … | Race browse, Race detail, Results list, Race picker, Result detail, Sign in, Profile · concept.html, first-screen.html, kit.html | docs ×3 | inner radius: photo, chip, date tile, skeleton bar |
| `--radius-2` | `6px` | kit.css | border-radius ×19: `.filters-trigger, .state-action`, `.race-card`, `.race-card .card-link::after`, `.result-card .card-link` … | 10 screens · concept.html, first-screen.html, kit.html | docs ×3 | outer radius: card, button, field, row group |
| `--radius-3` | `12px` | kit.css | border-radius ×2: `.kit-frame`, `.kit-shell` | — · kit.html | docs ×2 | docs layer: kit frame and kit shell |
| `--radius-sheet` | `38px` | kit.css | border-radius ×4: `.sheet`, `.sheet`, `body:has(> .sheet > .phone-screen)::befo`, `body:has(> .sheet > .phone-screen)::befo` | 10 screens · kit.html, shell.html |  | native sheet top corners |
| `--radius-bar-control` | `calc(var(--target) / 2)` | kit.css | aliased by `--radius-bar-inner`; border-radius ×5: `.race-search input, .phone-screen > form`, `:is(.controls, .top-bar) .view-toggle`, `:is(.controls, .top-bar) .filters-trigge`, `.action-bar :is(.register-btn, .open-btn` … | 10 screens · concept.html, first-screen.html, kit.html, shell.html |  | capsule control in a bar |
| `--radius-bar-inner` | `calc(var(--radius-bar-control) - var(--space-1))` | kit.css | border-radius ×1: `:is(.controls, .top-bar) .view-btn` | 10 screens · concept.html, first-screen.html, kit.html, shell.html |  | segment inside a bar capsule |
| `--radius-filter-chip` | `calc(var(--filter-chip-height) / 2)` | kit.css | border-radius ×1: `.chip` | Race browse · concept.html, first-screen.html, kit.html |  | filter chip capsule |
| `--radius-alert` | `34px` | kit.css | border-radius ×2: `dialog.alert`, `.action-sheet .action-group, .action-she`; border-bottom-left-radius ×1: `dialog.alert .alert-actions button:first`; border-bottom-right-radius ×1: `dialog.alert .alert-actions button:last-` | Race detail, Log result, Result detail, Profile · kit.html |  | alert and action-sheet corners |
| `--radius-avatar` | `50%` | kit.css | border-radius ×2: `:is(button, .submit-btn)[aria-busy="true`, `.initials` | Sign in, New password, Profile · kit.html | docs ×1 | circle: initials; **also the busy spinner** |
| `--border` | `1px` | kit.css | box-shadow ×13: `.race-search input, .phone-screen > form`, `.race-search input:hover, .phone-screen `, `.view-btn[aria-pressed="true"]`, `.race-card:hover .card-link::after` …; text-decoration-thickness ×5: `.clear-all`, `.official a, .row-note a, .alert-link, .`, `.copy-link`, `.text-link` …; border-bottom ×3: `.controls`, `.top-bar`, `.action-sheet .action-message`; border-top ×3: `.action-bar`, `.rows li + li::before`, `dialog.alert .alert-actions`; transform ×2: `.filters-trigger:active, .state-action:a`, `.register-btn:active, .open-btn:active, `; border-left ×2: `.results-order`, `dialog.alert .alert-actions button + but`; left ×1: `.map-pin::after`; width ×1: `.map-pin::after`; padding-top ×1: `body:has(> .top-bar) > .phone-screen` | 10 screens · concept.html, first-screen.html, kit.html, shell.html | docs ×8 | hairline and boundary width |
| `--focus-ring` | `2px` | kit.css | outline ×6: `.onrace :focus-visible`, `.race-search input:focus-visible, .phone`, `.race-card .card-link:focus-visible::aft`, `.date-pill:has(.date-value:focus-visible` …; outline-offset ×6: `.onrace :focus-visible`, `.race-card .card-link:focus-visible::aft`, `.date-pill:has(.date-value:focus-visible`, `.row--check:has(input:focus-visible)` …; --ring-sides ×2: `.rows li:has([aria-invalid="true"])`, `.rows li:has([aria-invalid="true"])`; border ×1: `:is(button, .submit-btn)[aria-busy="true`; --ring-top ×1: `.rows li:has([aria-invalid="true"])`; --ring-bottom ×1: `.rows li:has([aria-invalid="true"])` | 10 screens · concept.html, first-screen.html, kit.html, shell.html | docs ×3 | focus outline width; **also the invalid ring width** |
| `--shadow-sheet` | `0 12px 32px -12px rgba(0, 0, 0, 0.6)` | kit.css | box-shadow ×4: `body > .bottom-nav, .kit-tabbar > .botto`, `.sheet`, `dialog.alert`, `.action-sheet .action-group, .action-she` | Race browse, Race detail, Results list, Log result, Result detail, Profile · concept.html, first-screen.html, kit.html, shell.html | docs ×1 | float shadow: tab bar, sheet, alert, action sheet |
| `--target` | `44px` | kit.css | aliased by `--radius-bar-control`, `--tap-pad`; min-height ×19: `.filters-trigger, .state-action`, `.clear-all`, `.race-search input, .phone-screen > form`, `.view-btn` …; height ×4: `.map-placeholder > .map-pin`, `body:has(> .sheet > .phone-screen)::befo`, `.action-bar .bar.button`, `.skel-signout .bar`; margin-block ×3: `.sort-toggle`, `.form-alert .alert-link`, `.form-alert .alert-link`; padding-block ×3: `.forgot a`, `.row-note a`, `.form-alert .alert-link`; margin ×2: `.official p`, `.copy-link`; top ×1: `.phone-screen .controls`; min-width ×1: `.map-placeholder > .map-pin`; padding-inline ×1: `.top-bar[data-collapse] .bar-title`; margin-bottom ×1: `.top-bar--large`; padding-top ×1: `body:has(> .top-bar) > .phone-screen` | 10 screens · concept.html, first-screen.html, kit.html, shell.html | docs ×3 | minimum tap target (44) |
| `--measure` | `65ch` | kit.css | max-width ×2: `.state-message p, .state-msg p`, `.gate > section:has(> .inline-error + .s` | 9 screens · concept.html, kit.html | docs ×1 | running-text line length |
| `--tap-pad` | `calc((var(--target) - var(--filter-chip-height))…` | kit.css | inset ×1: `.chip::after, .clear-all::after`; padding ×1: `.chips-row` | Race browse · concept.html, first-screen.html, kit.html |  | 32px chip → 44px tap area |
| `--hidden-size` | `1px` | kit.css | width ×1: `.onrace .visually-hidden`; height ×1: `.onrace .visually-hidden` | 10 screens · concept.html, first-screen.html, kit.html, shell.html |  | visually hidden text |
| `--chip-height` | `24px` | kit.css | height ×2: `.skeleton-card .bar.tag`, `.result-list .skeleton-card .bar.tag`; min-height ×1: `.sport-tag` | Race browse, Race detail, Results list, Race picker, Result detail, Profile · concept.html, first-screen.html, kit.html |  | format chip height; its skeleton |
| `--filter-chip-height` | `32px` | kit.css | aliased by `--radius-filter-chip`, `--tap-pad`; min-height ×1: `.chip` | Race browse · concept.html, first-screen.html, kit.html |  | filter chip height |
| `--space-1` | `4px` | kit.css | aliased by `--radius-bar-inner`; padding ×7: `.clear-all`, `.race-card time`, `.view-toggle`, `.bottom-nav a` …; margin ×6: `.race-card h2`, `.finish dt`, `.inline-error p, .form-alert p`, `.linked-fact` …; text-underline-offset ×5: `.clear-all`, `.official a, .row-note a, .alert-link, .`, `.copy-link`, `.text-link` …; gap ×5: `.chip`, `.race-card .card-location`, `.bottom-nav a`, `.sort-toggle` …; margin-bottom ×3: `.race-card .sport-tag`, `.skeleton-card .bar.photo`, `.skeleton-card .bar.location`; margin-left ×2: `.row:has(> select)::after`, `.row-note.is-error a`; inset ×1: `.view-btn::after`; padding-block ×1: `.rows .row--stacked input`; margin-right ×1: `.field-error::before, .row-note.is-error`; margin-top ×1: `.linked-race .unlink-btn` | 10 screens · concept.html, first-screen.html, kit.html, shell.html | docs ×7 | tight inner padding |
| `--space-2` | `8px` | kit.css | aliased by `--tabbar-gap`; margin ×14: `.saved-status`, `.race h2, .result h2`, `.result .proof p`, `.action-caption` …; gap ×13: `.filters-trigger, .state-action`, `:is(button, .submit-btn)[aria-busy="true`, `.row-note [data-saving]:not([hidden])`, `.result-card .card-link` …; padding ×13: `.sport-tag`, `.chip`, `.race-search input, .phone-screen > form`, `.race-card` …; margin-bottom ×6: `.state-message::before, .state-msg::befo`, `.gate > section:has(> .inline-error + .s`, `.bar.h2`, `.bar.line` …; inset ×5: `dialog.action-sheet`, `dialog.action-sheet`, `dialog.action-sheet`, `.kit-stage dialog.action-sheet` …; margin-top ×3: `.state-msg .submit-btn`, `.state-actions`, `.gate > section:has(> .inline-error + .s`; margin-left ×2: `.race-search input::-webkit-search-cance`, `.results-order`; margin-right ×2: `.saved-status::before`, `.inline-error h2::before, .form-alert h2`; min-height ×1: `.view-btn`; row-gap ×1: `.skeleton-card`; padding-left ×1: `.results-order`; top ×1: `body:has(> .sheet > .phone-screen)::befo`; padding-block ×1: `.rows .row--stacked`; margin-block ×1: `.form-alert .alert-link` | 10 screens · concept.html, first-screen.html, kit.html, shell.html | docs ×8 | small gaps; tab bar gap |
| `--space-3` | `12px` | kit.css | aliased by `--sheet-gap-top`; gap ×16: `.card-top`, `.result-card .card-meta`, `.controls`, `.control-row` …; padding ×15: `.chip`, `.phone-screen > form.search`, `.race-card .card-link`, `.race-card time` …; margin ×3: `.inline-error, .form-alert`, `.list-intro`, `.form-note, .sent-note`; column-gap ×2: `.race-card .card-link`, `.skeleton-card`; padding-bottom ×1: `.controls`; padding-right ×1: `.race-card:has(.card-link[aria-current="`; margin-bottom ×1: `.initials`; margin-left ×1: `.row:has(> select)::after`; min-height ×1: `.action-sheet button` | 10 screens · concept.html, first-screen.html, kit.html, shell.html | docs ×13 | row and control gaps; sheet gap |
| `--space-4` | `16px` | kit.css | aliased by `--tabbar-inset`; padding ×38: `.phone-screen > form.search`, `.race-search input, .phone-screen > form`, `.race-search input, .phone-screen > form`, `.result-card .card-link` …; margin ×9: `.saved-status`, `.race h1, .result h1`, `.finish`, `.race > picture > .photo` …; left ×4: `.race-search::before, .phone-screen > fo`, `.phone-screen > form.search::before`, `body:has(> .sheet > .phone-screen)::befo`, `.rows li + li::before`; padding-inline ×3: `.phone-screen :is(main, .screen-main) > `, `.phone-screen :is(main, .screen-main) > `, `.phone-screen .results-row`; margin-bottom ×3: `.race .bar.photo`, `.bar.h1`, `.bar.finish-bar`; right ×2: `.race-card:has(.card-link[aria-current="`, `body:has(> .sheet > .phone-screen)::befo`; gap ×2: `.facts`, `.skel-facts`; top ×1: `.map-placeholder > .map-pin` | 10 screens · concept.html, first-screen.html, kit.html, shell.html | docs ×9 | gutter, card padding; tab bar inset |
| `--space-5` | `20px` | kit.css | padding ×5: `.filters-trigger, .state-action`, `.race, .result`, `.register-btn, .open-btn, .submit-btn`, `.gate` …; margin ×5: `.gate .group`, `.text-link`, `.linked-race`, `.context` …; margin-bottom ×2: `.result h1`, `.result .bar.h1` | 10 screens · concept.html, first-screen.html, kit.html | docs ×3 | button padding, section padding |
| `--space-6` | `24px` | kit.css | aliased by `--fade-end`; padding ×6: `.state-message, .state-msg`, `.phone-screen > form.search ~ :is(main, `, `.sheet > .phone-screen > main`, `.sheet > form` …; margin ×6: `.sheet .group`, `.facts`, `.about p`, `.official p` …; margin-bottom ×2: `.skel-facts`, `.bar.line.end` | 10 screens · concept.html, first-screen.html, kit.html, shell.html | docs ×4 | empty-state padding; fade length |
| `--space-7` | `32px` | kit.css | padding ×3: `.race, .result`, `#log-form`, `.gate`; margin ×2: `.expiry-note`, `.group` | 8 screens · kit.html | docs ×1 | screen/form padding, group gap |
| `--space-8` | `48px` | kit.css | max-width ×1: `dialog.alert` | Race detail, Result detail, Profile · kit.html | docs ×2 | alert max-width margin |
| `--space-9` | `64px` |  | — | — | docs ×3 | unused by product (stand only) |
| `--date-col` | `calc(68 * var(--type-unit))` | kit.css | grid-template-columns ×2: `.race-card .card-link`, `.skeleton-card`; width ×1: `.race-card time` | Race browse, Results list, Race picker · concept.html, first-screen.html, kit.html |  | date column on the race card |
| `--photo-ratio` | `3 / 1` | kit.css | aspect-ratio ×4: `.race-card .photo`, `.skeleton-card .bar.photo`, `.race > picture > .photo`, `.race .bar.photo` | Race browse, Race detail, Results list, Race picker, Result detail, Profile · concept.html, first-screen.html, kit.html |  | 3:1 photo band |
| `--photo-filter` | `grayscale(1) contrast(1.12) brightness(0.85)` | kit.css | filter ×2: `.race-card .photo`, `.race > picture > .photo` | Race browse, Race detail, Race picker · concept.html, first-screen.html, kit.html |  | black-and-white photos |
| `--icon-s` | `15px` | kit.css | aliased by `--spinner-size`; width ×7: `.chip span`, `.race-card .card-location::before, .proo`, `.sort-toggle::after`, `.result-card .card-meta::after` …; height ×7: `.chip span`, `.race-card .card-location::before, .proo`, `.sort-toggle::after`, `.result-card .card-meta::after` … | 9 screens · concept.html, first-screen.html, kit.html | docs ×4 | small glyph (chip ×, location, proof, sort); spinner size |
| `--icon-m` | `18px` | kit.css | width ×5: `.race-search::before, .phone-screen > fo`, `.filters-trigger::before`, `.saved-status::before`, `.top-bar a.back::before` …; height ×5: `.race-search::before, .phone-screen > fo`, `.filters-trigger::before`, `.saved-status::before`, `.top-bar a.back::before` …; margin-top ×1: `.race-search::before, .phone-screen > fo`; padding ×1: `.race-search input, .phone-screen > form` | 10 screens · concept.html, first-screen.html, kit.html, shell.html | docs ×4 | field and button glyph |
| `--icon-l` | `26px` | kit.css | width ×3: `.race-card:has(.card-link[aria-current="`, `body > .bottom-nav a::before, .kit-tabba`, `.row--check input[type="checkbox"]`; height ×3: `.race-card:has(.card-link[aria-current="`, `body > .bottom-nav a::before, .kit-tabba`, `.row--check input[type="checkbox"]`; padding-right ×1: `.race-card:has(.card-link[aria-current="`; margin-top ×1: `.race-card:has(.card-link[aria-current="` | Race browse, Results list, Race picker, Profile · concept.html, first-screen.html, kit.html, shell.html | docs ×4 | tab icon, checkmark |
| `--icon-search` | `url(data:image/svg…)` | kit.css | --state-icon ×1: `.state-message, .state-msg` | Race browse, Race detail, Results list, Race picker, Result detail, New password, Profile · concept.html, kit.html |  | glyph mask |
| `--icon-search-field` | `url(data:image/svg…)` | kit.css | -webkit-mask ×1: `.race-search::before, .phone-screen > fo`; mask ×1: `.race-search::before, .phone-screen > fo` | 10 screens · concept.html, first-screen.html, kit.html, shell.html |  | glyph mask |
| `--icon-pin` | `url(data:image/svg…)` | kit.css | -webkit-mask ×1: `.race-card .card-location::before, .proo`; mask ×1: `.race-card .card-location::before, .proo` | Race browse, Results list, Race picker, Result detail · concept.html, first-screen.html, kit.html |  | glyph mask |
| `--icon-link` | `url(data:image/svg…)` | kit.css | -webkit-mask-image ×1: `.proof-label::before`; mask-image ×1: `.proof-label::before` | Results list, Result detail · concept.html, kit.html |  | glyph mask |
| `--icon-filters` | `url(data:image/svg…)` | kit.css | -webkit-mask ×1: `.filters-trigger::before`; mask ×1: `.filters-trigger::before` | Race browse · concept.html, first-screen.html, kit.html |  | glyph mask |
| `--icon-chevron` | `url(data:image/svg…)` | kit.css | -webkit-mask ×1: `.row:has(> select)::after`; mask ×1: `.row:has(> select)::after` | Race browse, Log result, Sign in, Reset password, New password, Profile · kit.html | docs ×2 | glyph mask |
| `--icon-error` | `url(data:image/svg…)` | kit.css | -webkit-mask ×2: `.inline-error h2::before, .form-alert h2`, `.gate > section:has(> .inline-error + .s`; mask ×2: `.inline-error h2::before, .form-alert h2`, `.gate > section:has(> .inline-error + .s`; --state-icon ×1: `.state-message[role="alert"], .state-mes` | 10 screens · concept.html, kit.html |  | glyph mask |
| `--icon-check` | `url(data:image/svg…)` | kit.css | -webkit-mask ×2: `.race-card:has(.card-link[aria-current="`, `.row--check input[type="checkbox"]`; mask ×2: `.race-card:has(.card-link[aria-current="`, `.row--check input[type="checkbox"]` | Race browse, Results list, Race picker · concept.html, first-screen.html, kit.html |  | glyph mask |
| `--icon-saved` | `url(data:image/svg…)` | kit.css | -webkit-mask ×1: `.saved-status::before`; mask ×1: `.saved-status::before` | Results list · kit.html |  | glyph mask |
| `--icon-compass` | `url(data:image/svg…)` | kit.css | --tab-icon ×1: `.bottom-nav a[href*="race-browse"]` | Race browse, Results list, Profile · concept.html, first-screen.html, kit.html, shell.html |  | glyph mask |
| `--icon-stopwatch` | `url(data:image/svg…)` | kit.css | --tab-icon ×1: `.bottom-nav a[href*="results-list"]` | Race browse, Results list, Profile · concept.html, first-screen.html, kit.html, shell.html |  | glyph mask |
| `--icon-user` | `url(data:image/svg…)` | kit.css | --tab-icon ×1: `.bottom-nav a[href*="profile"]` | Race browse, Results list, Profile · concept.html, first-screen.html, kit.html, shell.html |  | glyph mask |
| `--icon-close` | `url(data:image/svg…)` | kit.css | -webkit-mask ×1: `.chip span`; mask ×1: `.chip span` | Race browse · concept.html, first-screen.html, kit.html |  | glyph mask |
| `--icon-back` | `url(data:image/svg…)` | kit.css | -webkit-mask ×1: `.top-bar a.back::before`; mask ×1: `.top-bar a.back::before` | 10 screens · kit.html, shell.html |  | glyph mask |
| `--icon-disclosure` | `url(data:image/svg…)` | kit.css | -webkit-mask ×2: `.result-card .card-meta::after`, `.row--nav::after`; mask ×2: `.result-card .card-meta::after`, `.row--nav::after` | Race browse, Results list, Log result, Race picker · concept.html, first-screen.html, kit.html |  | glyph mask |
| `--icon-archive` | `url(data:image/svg…)` | kit.css | --state-icon ×1: `.state-message--archive:not([role="alert` | Results list, Profile · concept.html, kit.html |  | glyph mask |
| `--icon-sort` | `url(data:image/svg…)` | kit.css | -webkit-mask ×1: `.sort-toggle::after`; mask ×1: `.sort-toggle::after` | Race browse · kit.html |  | glyph mask |
| `--icon-state` | `48px` | kit.css | width ×2: `.state-message::before, .state-msg::befo`, `.gate > section:has(> .inline-error + .s`; height ×2: `.state-message::before, .state-msg::befo`, `.gate > section:has(> .inline-error + .s` | 9 screens · concept.html, kit.html |  | empty/error state icon |
| `--skel-pulse-dim` | `0.55` | kit.css | opacity ×1: `50%` | — |  | skeleton pulse low point |
| `--dur-pulse` | `1600ms` | kit.css | animation ×1: `.bar, .initials.skel, .map-placeholder[a` | Race browse, Race detail, Results list, Race picker, Result detail, Profile · concept.html, kit.html |  | skeleton pulse length |
| `--skel-line` | `12px` | kit.css | height ×12: `.results-count .bar.count`, `.skeleton-card .bar.location`, `.result-list .skeleton-card .bar.date`, `.result-list .skeleton-card .bar.proof` …; margin-block ×1: `.result-list .skeleton-card .bar.proof` | 10 screens · concept.html, first-screen.html, kit.html |  | skeleton bar size |
| `--skel-title` | `16px` | kit.css | height ×4: `.skeleton-card .bar.title`, `.result-list .skeleton-card .bar.title`, `.bar.h2`, `.bar.name` | Race browse, Race detail, Results list, Race picker, Result detail, Profile · concept.html, kit.html |  | skeleton bar size |
| `--skel-title-w` | `70%` | kit.css | width ×3: `.skeleton-card .bar.title`, `.bar.h1`, `.action-bar .bar.caption` | Race browse, Race detail, Results list, Race picker, Result detail, Profile · concept.html, kit.html |  | skeleton bar size |
| `--skel-tag-w` | `64px` | kit.css | width ×4: `.skeleton-card .bar.tag`, `.result-list .skeleton-card .bar.tag`, `.bar.label`, `.bar.heading`; grid-template-columns ×1: `.skel-facts` | Race browse, Race detail, Results list, Race picker, Result detail, Profile · concept.html, kit.html |  | skeleton bar size |
| `--skel-loc-w` | `45%` | kit.css | width ×4: `.skeleton-card .bar.location`, `.skel-facts .bar:nth-child(even)`, `.bar.line.end`, `.bar.email` | Race browse, Race detail, Results list, Race picker, Result detail, Profile · concept.html, kit.html |  | skeleton bar size |
| `--skel-count-w` | `140px` | kit.css | width ×2: `.results-count .bar.count`, `.bar.h2` | Race browse, Race detail, Results list, Race picker, Result detail, Profile · concept.html, first-screen.html, kit.html |  | skeleton bar size |
| `--skel-row-title-w` | `55%` | kit.css | width ×3: `.result-list .skeleton-card .bar.title`, `.bar.line.short`, `.bar.name` | Race browse, Race detail, Results list, Race picker, Result detail, Profile · concept.html, kit.html |  | skeleton bar size |
| `--skel-time-w` | `96px` | kit.css | width ×2: `.result-list .skeleton-card .bar.time`, `.bar.finish-bar` | Race browse, Race detail, Results list, Race picker, Result detail, Profile · concept.html, kit.html |  | skeleton bar size |
| `--skel-time-h` | `var(--size-time)` | kit.css | height ×2: `.result-list .skeleton-card .bar.time`, `.bar.finish-bar` | Race browse, Race detail, Results list, Race picker, Result detail, Profile · concept.html, kit.html |  | skeleton bar size |
| `--skel-date-w` | `72px` | kit.css | width ×2: `.result-list .skeleton-card .bar.date`, `.row .bar.value` | 10 screens · concept.html, kit.html |  | skeleton bar size |
| `--skel-proof-w` | `62%` | kit.css | width ×2: `.result-list .skeleton-card .bar.proof`, `.bar.link` | Race browse, Race detail, Results list, Race picker, Result detail, Profile · concept.html, kit.html |  | skeleton bar size |
| `--screen-w` | `390px` | kit.css | max-width ×4: `body:has(> .phone-screen)`, `body:has(> .sheet > .phone-screen)`, `.kit-frame`, `.kit-shell`; inset ×1: `dialog.action-sheet` | 10 screens · kit.html, shell.html |  | iPhone width (390); kit frame width |
| `--tabbar-h` | `64px` | kit.css | aliased by `--radius-tabbar`, `--tabbar-clear`; height ×2: `body > .bottom-nav, .kit-tabbar > .botto`, `.kit-tabbar` | Race browse, Results list, Profile · concept.html, first-screen.html, kit.html, shell.html |  | tab bar height |
| `--tabbar-inset` | `var(--space-4)` | kit.css | left ×1: `body > .bottom-nav, .kit-tabbar > .botto`; right ×1: `body > .bottom-nav, .kit-tabbar > .botto` | Race browse, Results list, Profile · concept.html, first-screen.html, kit.html, shell.html |  | tab bar side inset |
| `--tabbar-gap` | `var(--space-2)` | kit.css | aliased by `--tabbar-clear`; bottom ×1: `body > .bottom-nav, .kit-tabbar > .botto`; height ×1: `.kit-tabbar` | Race browse, Results list, Profile · concept.html, first-screen.html, kit.html, shell.html |  | tab bar gap to the bottom |
| `--radius-tabbar` | `calc(var(--tabbar-h) / 2)` | kit.css | border-radius ×1: `body > .bottom-nav, .kit-tabbar > .botto` | Race browse, Results list, Profile · concept.html, first-screen.html, kit.html, shell.html |  | tab bar capsule |
| `--tabbar-clear` | `calc(var(--tabbar-h) + var(--tabbar-gap) + var(-…` | kit.css | padding-bottom ×1: `.phone-screen` | 10 screens · kit.html, shell.html |  | scroll clearance above the tab bar |
| `--scrim` | `rgba(0, 0, 0, 0.6)` | kit.css | background ×7: `.sheet-backdrop`, `body:has(> .sheet > .phone-screen)`, `body:has(> .sheet > .phone-screen)`, `body:has(> .sheet > .phone-screen)::befo` … | 10 screens · kit.html, shell.html |  | dimming behind sheet, alert, action sheet |
| `--sheet-gap-top` | `var(--space-3)` | kit.css | aliased by `--sheet-large`; top ×1: `body:has(> .sheet > .phone-screen)::befo`; margin-top ×1: `body > .sheet:has(> .phone-screen)` | 10 screens · kit.html, shell.html |  | large detent gap |
| `--z-under` | `-1` | kit.css | z-index ×1: `.map-placeholder::before, .map-placehold` | Race browse · kit.html |  | layer: behind its own box (map land, borders) |
| `--z-lift` | `1` | kit.css | z-index ×2: `.map-placeholder > *`, `.top-bar :is(a, button)` | 10 screens · kit.html, shell.html |  | layer: above siblings (map contents, bar buttons) |
| `--z-float` | `2` | kit.css | z-index ×3: `.phone-screen .controls`, `.map-placeholder > .map-pin`, `.top-bar` | 10 screens · concept.html, first-screen.html, kit.html, shell.html |  | layer: sticky controls bar, top bar, map pins |
| `--z-bar` | `3` | kit.css | z-index ×4: `.phone-screen > .action-bar`, `body > .bottom-nav, .kit-tabbar > .botto`, `.top-bar--large`, `body > .top-bar` | 10 screens · concept.html, first-screen.html, kit.html, shell.html |  | layer: tab bar, action bar, large top bar |
| `--z-edge` | `4` | kit.css | z-index ×1: `body:has(> .phone-screen)::before` | 10 screens · kit.html, shell.html |  | layer: status-bar scroll edge |
| `--z-scrim` | `5` | kit.css | z-index ×1: `.sheet-backdrop` | Race browse · kit.html |  | layer: scrim |
| `--z-sheet` | `6` | kit.css | z-index ×3: `.sheet`, `.kit-stage dialog.alert`, `.kit-stage dialog.action-sheet` | Race browse, Race detail, Log result, Result detail, Profile · kit.html |  | layer: sheet, alert, action sheet |
| `--sheet-large` | `calc(100% - var(--safe-top) - var(--sheet-gap-to…` | kit.css | height ×1: `.sheet` | Race browse, Log result · kit.html |  | sheet height at large detent |
| `--dur-sheet` | `250ms`; `0ms` (reduced motion) | kit.css | transition ×2: `.sheet-backdrop`, `.sheet` | Race browse, Log result · kit.html |  | sheet slide |
| `--safe-top` | `env(safe-area-inset-top, 0px)` | kit.css | aliased by `--sheet-large`; padding ×2: `.phone-screen header:not(.top-bar)`, `.top-bar`; top ×2: `.phone-screen .controls`, `body:has(> .sheet > .phone-screen)::befo`; height ×1: `body:has(> .phone-screen)::before`; margin-top ×1: `body > .sheet:has(> .phone-screen)`; min-height ×1: `.top-bar`; margin-bottom ×1: `.top-bar--large`; padding-top ×1: `body:has(> .top-bar) > .phone-screen` | 10 screens · concept.html, first-screen.html, kit.html, shell.html |  | top safe area |
| `--safe-bottom` | `env(safe-area-inset-bottom, 0px)` | kit.css | aliased by `--tabbar-clear`; padding ×4: `.phone-screen > form.search ~ :is(main, `, `.sheet > .phone-screen > main`, `.sheet > form`, `.action-bar`; bottom ×1: `body > .bottom-nav, .kit-tabbar > .botto`; inset ×1: `dialog.action-sheet` | 10 screens · concept.html, first-screen.html, kit.html, shell.html |  | bottom safe area |
| `--fade-end` | `linear-gradient(to right, #000 calc(100% - var(-…` | kit.css | -webkit-mask-image ×1: `.chips-row`; mask-image ×1: `.chips-row` | Race browse · concept.html, first-screen.html, kit.html |  | mask fading the chips row end |
| `--stand-max` | `1152px` |  | — | — | docs ×1 | docs layer only (stand width) |
| `--stand-col-min` | `320px` |  | — | — | docs ×1 | docs layer only (stand column) |
| `--avatar-size` | `80px` | kit.css | width ×1: `.initials`; height ×1: `.initials` | Profile · kit.html |  | initials circle size |
| `--alert-width` | `270px` | kit.css | width ×1: `dialog.alert` | Race detail, Result detail, Profile · kit.html |  | alert width (iOS 270) |
| `--kit-stage-h` | `600px` | kit.css | height ×2: `.kit-stage`, `.kit-shell` | — · kit.html |  | kit stage height (showcase only) |
| `--ease-out` | `cubic-bezier(0.2, 0.8, 0.2, 1)` | kit.css | transition ×12: `.filters-trigger, .state-action`, `.filters-trigger, .state-action`, `.chip`, `.sheet-backdrop` … | 10 screens · concept.html, first-screen.html, kit.html, shell.html | docs ×2 | state transitions, sheet |
| `--dur-fast` | `160ms`; `0ms` (reduced motion) | kit.css | transition ×10: `.filters-trigger, .state-action`, `.filters-trigger, .state-action`, `.chip`, `.top-bar[data-collapse] .bar-title` … | 10 screens · concept.html, first-screen.html, kit.html, shell.html | docs ×2 | state transitions |
| `--ease-in-out` | `cubic-bezier(0.45, 0, 0.55, 1)` | kit.css | animation ×1: `.bar, .initials.skel, .map-placeholder[a` | Race browse, Race detail, Results list, Race picker, Result detail, Profile · concept.html, kit.html |  | skeleton pulse |
| `--dur-spin` | `800ms` | kit.css | animation ×1: `:is(button, .submit-btn)[aria-busy="true` | Sign in, New password, Profile · kit.html | docs ×1 | spinner turn |
| `--spinner-size` | `var(--icon-s)` | kit.css | width ×1: `:is(button, .submit-btn)[aria-busy="true`; height ×1: `:is(button, .submit-btn)[aria-busy="true` | Sign in, New password, Profile · kit.html | docs ×2 | busy spinner |
| `--map-pin-dot` | `10px` | kit.css | height ×2: `.map-pin::before`, `.map-pin::after`; transform ×1: `.map-placeholder > .map-pin`; width ×1: `.map-pin::before` | Race browse · kit.html |  | pin dot size |
| `--map-water` | `var(--bg-bar)` | kit.css | background ×1: `.map-placeholder`; box-shadow ×1: `.map-pin::before` | Race browse · kit.html |  | map water; pin dot ring |
| `--map-land` | `var(--bg-1)` | kit.css | background ×1: `.map-placeholder::before` | Race browse · kit.html |  | map land |
| `--map-lines` | `var(--bg-3)` | kit.css | background ×1: `.map-placeholder::after` | Race browse · kit.html |  | coastlines and borders |
| `--pin-h` | `22px` | kit.css, map.css | height ×2: `.map-pin > span`, `.map-pin::after`; transform ×1: `.map-placeholder > .map-pin`; top ×1: `.map-pin[data-pin="berlin-marathon"]::af`; bottom ×1: `.map-pin[data-pin="utmb"]::after, .map-p` | Race browse · kit.html |  | pin label height |
| `--pin-gap` | `6px` | kit.css | transform ×1: `.map-placeholder > .map-pin` | Race browse · kit.html |  | shortest leader line |
| `--pin-berlin-marathon-dy` | `-52px` | map.css | --dy ×1: `.map-pin[data-pin="berlin-marathon"]` | Race browse · kit.html |  | pin label offset |
| `--pin-hyrox-london-dy` | `-28px` | map.css | --dy ×1: `.map-pin[data-pin="hyrox-london"]` | Race browse · kit.html |  | pin label offset |
| `--pin-utmb-dy` | `30px` | map.css | --dy ×1: `.map-pin[data-pin="utmb"]` | Race browse · kit.html |  | pin label offset |
| `--pin-deka-strong-chicago-dy` | `-30px` | map.css | --dy ×1: `.map-pin[data-pin="deka-strong-chicago"]` | Race browse · kit.html |  | pin label offset |
| `--pin-spartan-beast-killington-dy` | `-56px` | map.css | --dy ×1: `.map-pin[data-pin="spartan-beast-killing` | Race browse · kit.html |  | pin label offset |
| `--pin-boston-marathon-dy` | `28px` | map.css | --dy ×1: `.map-pin[data-pin="boston-marathon"]` | Race browse · kit.html |  | pin label offset |
| `--pin-hyrox-dallas-dy` | `28px` | map.css | --dy ×1: `.map-pin[data-pin="hyrox-dallas"]` | Race browse · kit.html |  | pin label offset |
| `--map-ratio` | `1.79600` | kit.css | top ×1: `.map-placeholder > .map-pin` | Race browse · kit.html |  | map height ÷ width |
| `--map-land-mask` | `url(data:image/svg…)` | kit.css | -webkit-mask-image ×1: `.map-placeholder::before`; mask-image ×1: `.map-placeholder::before` | Race browse · kit.html |  | land shape |
| `--map-lines-mask` | `url(data:image/svg…)` | kit.css | -webkit-mask-image ×1: `.map-placeholder::after`; mask-image ×1: `.map-placeholder::after` | Race browse · kit.html |  | borders shape |
| `--pin-berlin-marathon-x` | `91.411%` | map.css | --x ×1: `.map-pin[data-pin="berlin-marathon"]` | Race browse · kit.html |  | pin longitude (x) |
| `--pin-berlin-marathon-yf` | `0.4414` | map.css | --yf ×1: `.map-pin[data-pin="berlin-marathon"]` | Race browse · kit.html |  | pin latitude (y fraction) |
| `--pin-hyrox-london-x` | `81.387%` | map.css | --x ×1: `.map-pin[data-pin="hyrox-london"]` | Race browse · kit.html |  | pin longitude (x) |
| `--pin-hyrox-london-yf` | `0.4481` | map.css | --yf ×1: `.map-pin[data-pin="hyrox-london"]` | Race browse · kit.html |  | pin latitude (y fraction) |
| `--pin-utmb-x` | `86.570%` | map.css | --x ×1: `.map-pin[data-pin="utmb"]` | Race browse · kit.html |  | pin longitude (x) |
| `--pin-utmb-yf` | `0.4831` | map.css | --yf ×1: `.map-pin[data-pin="utmb"]` | Race browse · kit.html |  | pin latitude (y fraction) |
| `--pin-hyrox-dallas-x` | `9.780%` | map.css | --x ×1: `.map-pin[data-pin="hyrox-dallas"]` | Race browse · kit.html |  | pin longitude (x) |
| `--pin-hyrox-dallas-yf` | `0.5536` | map.css | --yf ×1: `.map-pin[data-pin="hyrox-dallas"]` | Race browse · kit.html |  | pin latitude (y fraction) |
| `--pin-deka-strong-chicago-x` | `16.570%` | map.css | --x ×1: `.map-pin[data-pin="deka-strong-chicago"]` | Race browse · kit.html |  | pin longitude (x) |
| `--pin-deka-strong-chicago-yf` | `0.5063` | map.css | --yf ×1: `.map-pin[data-pin="deka-strong-chicago"]` | Race browse · kit.html |  | pin latitude (y fraction) |
| `--pin-spartan-beast-killington-x` | `27.545%` | map.css | --x ×1: `.map-pin[data-pin="spartan-beast-killing` | Race browse · kit.html |  | pin longitude (x) |
| `--pin-spartan-beast-killington-yf` | `0.4965` | map.css | --yf ×1: `.map-pin[data-pin="spartan-beast-killing` | Race browse · kit.html |  | pin latitude (y fraction) |
| `--pin-boston-marathon-x` | `28.845%` | map.css | --x ×1: `.map-pin[data-pin="boston-marathon"]` | Race browse · kit.html |  | pin longitude (x) |
| `--pin-boston-marathon-yf` | `0.5036` | map.css | --yf ×1: `.map-pin[data-pin="boston-marathon"]` | Race browse · kit.html |  | pin latitude (y fraction) |

---

## Findings

### 1. Value drift: one role, different values

1. **Hover and pressed fills step by different amounts.**
   - A raised control (bg-2) goes one level up to **bg-3** on hover, pressed or open: `.filters-trigger:hover`, `.chip:hover`, `.secondary-btn:hover`, `.filters-trigger[aria-expanded]`, `.view-btn[aria-pressed]`, `.map-pin:hover > span`, the alert and action-sheet buttons on hover.
   - A row on a surface (bg-1) goes one level up to **bg-2**: `.row--check:active`, `a.row--nav[href]:hover`, `.signout:hover`.
   - A card on a surface (bg-1) jumps two levels to **bg-3**: `.race-card:has(.card-link:active)`, `.result-card .card-link:active`.
   - So "pressed" means +1 level on rows and +2 on cards. There's no pressed or hover token: each rule picks a level by hand.
2. **The chip family has three heights:**
   - `--chip-height` 24 (format chip, `.sport-tag`);
   - `--filter-chip-height` 32 (filter chip, `.chip`);
   - `--pin-h` 22 (map pin label, styled like a chip: bg-2, `--size-label`).
   - These are three components, so the gap may be intended. It's recorded because the pin label reads as the same small tag as the format chip, at 22 against 24.
3. **Body and meta have the same size, under two names.**
   - `--size-body` and `--size-meta` are both `calc(15 * var(--type-unit))`. Meta was 14 until C3 raised it.
   - Every element sized 15 has to choose one of the two names, and nothing distinguishes them.
4. **The radii are spread across eight tokens with two scales.**
   - Content uses fixed px: `--radius-1` 4, `--radius-2` 6, `--radius-3` 12.
   - iOS shapes use other values: `--radius-sheet` 38, `--radius-alert` 34, and the capsules `--radius-bar-control`, `--radius-filter-chip` and `--radius-tabbar`, each written as height ÷ 2.
   - `--radius-avatar` is 50%.
   - All three capsule tokens express the same role: a capsule is half its own height.
5. **Two tokens serve a role they weren't named for.**
   - `--focus-ring` (2px) is the focus outline width, and it's also the width of the invalid ring (the `.rows li:has([aria-invalid])` ring sides).
   - `--leading-body` (1.45) is a line height, and it's also a vertical spacing unit (`margin-block` on `.sort-toggle`, `.form-alert .alert-link` and two skeleton bars).
6. **The display size is shared by two different things.** `--size-day` (30) sizes the race card's date day and also the Profile initials. An avatar letter and a date figure are different roles that happen to share a size.

### 2. One variable, several roles

Each row below is one token. A token that's aliased lists its alias's roles too.

| Variable | Roles it plays | Where |
|---|---|---|
| `--accent` | (a) **primary action fill** | `.state-action:not(.secondary)`, `.register-btn`, `.open-btn`, `.submit-btn` (background) |
| | (b) **action in a bar** (text, no fill) | `.top-bar .save-btn`, `.top-bar .bar-action` (Save, Log result, Apply filters) |
| | (c) **current place** | `.bottom-nav a[aria-current="page"]` (the current tab) |
| `--accent-hover` | the hover of (a), (b) and (c) | the same selectors with `:hover` |
| `--error` | (a) **error icon** | `.inline-error h2::before`, `.form-alert h2::before`, the gate error icon |
| | (b) **invalid** ring (as `--invalid`) | `.rows li:has([aria-invalid="true"])` ring top and sides |
| | (c) **destructive** action text (as `--destructive`) | `.signout`, `dialog.alert #signout-confirm`, `.action-sheet .is-destructive` |
| `--text-1` | (a) **primary text** | about 50 color rules: titles, body, finish times, secondary-button labels |
| | (b) **focus** ring (as `--focus`) | `:focus-visible` outlines (6 rules) |
| | (c) **control tint** (as `--control-tint`) | the checkmark (`.race-card:has(.card-link[aria-current])`), `.row--check input[type="checkbox"]`, `accent-color` |
| | (d) selection fill | `.onrace ::selection` (background) |
| | (e) map pin dot | `.map-pin::before` (background) |
| `--text-2` | (a) **secondary text** | meta, location, proof line, month and year |
| | (b) placeholder | `.race-search input::placeholder` |
| | (c) inactive tab | `.bottom-nav a` |
| | (d) glyph fill | `.chip span` (×), the search magnifier, disclosure chevrons, the select chevron, the location and proof icons |
| | (e) **boundary on hover** | `.race-search input:hover` (the field's ring, normally `--field-line`) |
| | (f) map leader line | `.map-pin::after` |
| | (g) empty or error state icon | `.state-message::before` |
| | (h) link hover | `.clear-all:hover` |
| `--bg-0` | (a) **page background** | `.onrace`, `.kit-frame`, `.kit-shell` |
| | (b) glass base (as `--glass-ground`) | the controls bar, the top bar, the status-bar edge |
| | (c) selection text | `.onrace ::selection` (color) |
| | (d) **on-accent** has the same hex | `--on-accent: #131518` is written raw, not `var(--bg-0)` |
| `--bg-1` | (a) **surface** | `.race-card`, `.result-card .card-link`, the search field, `.rows`, `.saved-status`, `.signout`, the receded Results edge, `.skeleton-card` |
| | (b) map land (as `--map-land`) | `.map-placeholder::before` |
| `--bg-2` | (a) **raised** | secondary buttons, `.sport-tag`, `.chip`, the date tile, the segmented track, skeleton `.bar`, pin labels, `.initials` |
| | (b) glass base (as `--glass-sheet`) | the sheet, the alert, the action sheet |
| | (c) **hover or pressed on rows** | `.row--check:active`, `a.row--nav[href]:hover`, `.signout:hover` |
| `--bg-3` | (a) **hover, pressed or open on raised controls** | see Drift 1 |
| | (b) **pressed card** (from bg-1, +2) | `.race-card:active`, `.result-card .card-link:active` |
| | (c) **a group raised on a sheet or form** | `.sheet .rows`, `.linked-race` |
| | (d) map lines (as `--map-lines`) | `.map-placeholder::after` |
| `--bg-bar` | (a) frame and void | `body:has(> .sheet > .phone-screen)` (behind the sheet) |
| | (b) glass base (as `--glass-bar`) | the tab bar, the action bar |
| | (c) map water (as `--map-water`) | `.map-placeholder`, the ring of `.map-pin::before` |
| `--line` | (a) hairline divider | `.controls`, `.rows li + li::before`, `.results-order`, the alert buttons, the action-sheet message |
| | (b) showcase frame outline | `.kit-frame`, `.kit-shell` |
| `--field-line` | (a) **input boundary** | the search field, rows with inputs |
| | (b) selected segment outline | `.view-btn[aria-pressed="true"]` |
| | (c) card hover ring | `.race-card:hover .card-link::after` |
| | (d) map frame | `.map-placeholder` |
| | (e) scrollbar | `scrollbar-color` on `.sheet` and `.phone-screen` |
| `--glass-edge` | the rim of every glass surface | the tab bar, sheet, alert and action sheet (one role, four components) |
| `--shadow-sheet` | the float shadow, also on the tab bar | the tab bar, sheet, alert and action sheet (its name says "sheet" but it isn't limited to one) |
| `--icon-s` | a small glyph; also the spinner size (as `--spinner-size`) | |
| `--radius-avatar` (50%) | the initials circle; also the busy spinner | `:is(button, .submit-btn)[aria-busy="true"]::after` |
| `--space-6` | spacing; also the fade length (in `--fade-end`) | |

**Names that sound like a role but cover more than one:**
- `--accent` covers action, bar action and current place.
- `--error` covers error, invalid and destructive.
- `--text-2` covers text, glyph, boundary and line.
- `--bg-2` covers a raised level, row hover and a glass base.
- `--bg-3` covers pressed, pressed card, a group on a sheet and map lines.
- `--shadow-sheet` covers more than the sheet.
- `--field-line` is used beyond fields: a segment outline, a card hover ring, the map frame and the scrollbar.

### 3. Values bypassing variables

**In product class rules: none of substance.** The only literals are keywords and layout math:
- keywords: `none`, `transparent`, `currentColor`, `inherit`;
- opacity `0` and `1`;
- `font-size: 0` on `.chip span` (it hides the text and keeps the glyph);
- `letter-spacing: normal` (kit.css lines 674 and 1101);
- the centering transforms `-50%` in `.map-placeholder > .map-pin` and `.map-pin::before`;
- `100vw` in the inset of `dialog.action-sheet`.

**Raw values inside token definitions that repeat another token:**

| Token | Raw value | What it repeats |
|---|---|---|
| `--on-accent` | `#131518` | the hex of `--bg-0` |
| `--glass-edge` | `rgba(244, 245, 246, 0.08)` | `--text-1` (#F4F5F6) at 8%, written as rgba |
| `--shadow-sheet` | `… rgba(0, 0, 0, 0.6)` | the same color as `--scrim` |
| `--fade-end` | `#000` | a mask's opaque stop (not a color role; noted for completeness) |
| `--scrim` | `rgba(0, 0, 0, 0.6)` | pure black, which color rule 3a keeps off backgrounds; allowed here because it's a dimming layer, not a level |

**Outside the CSS, the same values are written a second time:**
- `DESIGN.md` frontmatter repeats every color hex and the three glass formulas;
- `.impeccable/design.json` is generated from DESIGN.md.
- Either one drifts if `kit.css` changes and they aren't regenerated.

**In the kit file, but not product:**
- `ui/kit.css` holds the showcase scaffolding classes `.kit-frame`, `.kit-frame--flush`, `.kit-shell`, `.kit-stage` and `.kit-tabbar`.
- It also holds the tokens only they use: `--radius-3` and `--kit-stage-h`.
- They're product-file classes that serve only `ui/kit.html` and `ui/shell.html`.

## Docs layer (not audited as tokens)

| File | Defines | Reads from the kit |
|---|---|---|
| `ui/kit-doc.css` | 13 `--d-*` tokens (the artifact style: `--d-bg`, `--d-elev`, `--d-elev-2`, `--d-border`, `--d-text`, `--d-dim`, `--d-faint`, `--d-accent`, `--d-accent-dim`, `--d-radius`, `--d-font`, `--d-mono`, `--d-side`) | nothing (its own values) |
| `concept/stand.css` | `--phone-width` | `--space-*`, `--radius-3`, `--stand-max`, `--stand-col-min`, `--font-mono`, type, color |
| `concept/specimens.css` | `--success`, `--success-bg`, `--warning`, `--warning-bg`, `--warning-line` (stand specimens only; rule 2 keeps success off the product) | `--accent`, `--on-accent`, `--bg-*`, type, `--target` |

**Kit tokens that only the docs layer uses:**
- `--font-mono`, `--stand-max`, `--stand-col-min` and `--space-9` (stand and doc);
- `--radius-3` and `--kit-stage-h` (the showcase scaffolding in `kit.css`).

## Candidate semantic color roles

These are read from the usages above and DESIGN.md's names. They're candidates for review, not decisions.

| Candidate role | Today | Read from |
|---|---|---|
| **Frame** (behind everything, void behind the sheet) | `--bg-bar` | `body:has(> .sheet …)`; DESIGN.md "the frame, darker than the page" |
| **Page background** | `--bg-0` | `.onrace`; DESIGN.md "Graphite Ground" |
| **Surface** (card, row group, field) | `--bg-1` | `.race-card`, `.result-card .card-link`, `.rows`, search field, `.saved-status` |
| **Raised** (control on a surface: secondary button, chip, date tile, track, avatar) | `--bg-2` | `.secondary-btn`, `.chip`, `.sport-tag`, `.view-toggle`, `.initials` |
| **Pressed / hover / open** | `--bg-3` (controls), `--bg-2` (rows) | Drift 1; one role, two values today |
| **Group on a sheet** (one level above the sheet) | `--bg-3` | `.sheet .rows`, `.linked-race` |
| **Skeleton** | `--bg-2` | `.bar`, `.initials.skel` |
| **Glass bar** | `--glass-bar` (bg-bar base) | tab bar, action bar |
| **Glass ground** | `--glass-ground` (bg-0 base) | controls bar, top bar, status edge |
| **Glass sheet** | `--glass-sheet` (bg-2 base) | sheet, alert, action sheet |
| **Glass rim** | `--glass-edge` | every glass surface |
| **Scrim** | `--scrim` | sheet backdrop, alert, action sheet |
| **Float shadow** | `--shadow-sheet` | tab bar, sheet, alert, action sheet |
| **Primary text** | `--text-1` | titles, body, finish times; DESIGN.md "Chalk" |
| **Secondary text** | `--text-2` | meta, location, proof, placeholder; DESIGN.md "Ash" |
| **Disabled text** | `--text-disabled` | `:disabled` controls |
| **Glyph** (small icons, chevrons, disclosure) | `--text-2` | `.chip span`, search, disclosure, select chevron |
| **Action** (primary fill) | `--accent` | `.register-btn`, `.open-btn`, `.submit-btn`, `.state-action`; DESIGN.md "Sodium Amber" |
| **On action** | `--on-accent` | text on the primary fill |
| **Action in a bar** (text only) | `--accent` | `.save-btn`, `.bar-action` |
| **Action hover** | `--accent-hover` | the three above, on hover |
| **Current place** | `--accent` | the current tab |
| **Inactive place** | `--text-2` | `.bottom-nav a` |
| **Error** | `--error` | error icons; DESIGN.md "Soft Coral" |
| **Error surface** | `--error-bg` | `.inline-error`, `.form-alert` |
| **Invalid** | `--invalid` → `--error` | invalid row ring |
| **Danger / destructive** | `--destructive` → `--error` | Sign out, its alert, action sheet |
| **Focus** | `--focus` → `--text-1` | `:focus-visible` |
| **Control tint** (checkmarks, switches) | `--control-tint` → `--text-1` | checkbox, card checkmark |
| **Hairline** (decorative divider) | `--line` | lists, bars, alert buttons; DESIGN.md "Hairline" |
| **Boundary** (an input's edge, 3:1) | `--field-line` | inputs, segment outline, card hover ring; DESIGN.md "Field Line" |
| **Boundary hover** | `--text-2` | `.race-search input:hover` |
| **Chip label** | `--chip-text` | `.sport-tag` |
| **Selection** | `--text-1` on `--bg-0`, inverted | `::selection` |

## Colors used in exactly one file and one class (or one rule)

| Variable | Value | File | The one place |
|---|---|---|---|
| `--map-water` | `var(--bg-bar)` | map.css → kit.css | `.map-placeholder` (and the ring of `.map-pin::before`, the same map) |
| `--map-land` | `var(--bg-1)` | map.css → kit.css | `.map-placeholder::before` |
| `--map-lines` | `var(--bg-3)` | map.css → kit.css | `.map-placeholder::after` |
| `--chip-text` | `#BFC4CA` | kit.css | `.sport-tag` |
| `--error-bg` | `#3A2F31` | kit.css | `.inline-error, .form-alert` (one rule) |
| `--on-accent` | `#131518` | kit.css | the primary fill's text (2 rules, one role) |
| `--text-disabled` | `#6B7178` | kit.css | `:disabled` states only (10 rules, one role) |

## What reads these files (and breaks when `ui/kit.css` is removed)

**Pages that link `ui/kit.css`** (each one also has a `public/` mirror; 52 pages in `public/` link it):
- `wireframes/`: all 35 pages. The 4 `race-browse*` pages also link `ui/map.css`.
- `ui/kit.html`, which also links `map.css` and `kit-doc.css`, and `ui/shell.html`.
- `concept/concept.html` (the stand, which also links `map.css`, `specimens.css` and `stand.css`) and `concept/first-screen.html`.
- Review pages:
  - `ui/review-3b.html`, `review-step5.html`, `review-markup.html`, `review-markup-2.html`, `review-overflow.html`, `review-step6.html`, `review-step7.html` (also `map.css`), `review-lessons.html`, `review-overviews.html`, `review-kit-sheet.html`;
  - `visuals/review-round3.html`.
- `public/concept-overview.html` and `public/ui-overview.html` embed the stand and the kit, and name `kit.css` in their text.

**Scripts:**

| Script | What it reads or does |
|---|---|
| `scripts/concept/build_stand.py` | `KIT` and `TOK` (every `:root` of `kit.css`, `map.css`, `specimens.css` and `stand.css`), `tok()`, `CSS_RULES` / `selectors_using()` for color rules 1 and 2 and the 3a usage check, `glass_parts()` (parses the `color-mix(…)` of the glass tokens), `SCRIM_A` (parses `rgba(0, 0, 0, a)` from `--scrim`), `CSS_V` (hashes `kit.css`, `kit-doc.css`, `map.css`, `stand.css` and `specimens.css` to stamp `?v=` on every page's link), writes the stand's own `<link href="../ui/kit.css">`, mirrors `ui/kit.css` and the others to `public/`, and runs every check below |
| `scripts/build_kit_showcase.py` | writes `ui/kit.html`'s layout; links and names `kit.css` in its intro |
| `scripts/check_kit.py` | reads `ui/kit.html`, `ui/inventory.md` and `microcopy.md`, not `kit.css`; it breaks only if the showcase's `kit-item` and `kit-label` markup changes |
| `scripts/check_overflow.mjs` | loads every kit-styled page; `ONE_LINE` names the kit classes `.sort-toggle`, `.filters-trigger`, `.controls .view-btn`, `.chips-row .chip` and `.clear-all`; `FONTS` names the kit's two families; the 200% pass depends on `--type-unit` being `1rem ÷ 16` |
| `scripts/build_design_sidecar.py` | reads the motion values from `kit.css` with `kit(name)` (`--dur-*`, `--ease-*`) |
| `scripts/lesson_page.py` | `repo_stats` counts the tokens in `kit.css` and `map.css`; `SOURCES` names `ui/kit.css` |
| `scripts/build_concept_overview.py` | `TOK` and `N_TOKENS` from `kit.css` and `map.css` |
| `scripts/build_ui_overview.py` | names `ui/kit.css` in the FLOW table and the stats ("kit tokens in ui/kit.css and ui/map.css") |
| `scripts/concept/build_map.py` | writes the generated map block of `ui/map.css` (its colors are aliases of kit tokens) |
| impeccable detector | checks against DESIGN.md (frontmatter hexes) |

## Build checks that name a variable

| Check | Where (build_stand.py) | Variables named |
|---|---|---|
| **Color rule 1**: accent placement | `selectors_using('accent', 'accent-hover')` against `ACCENT_OK` | `--accent`, `--accent-hover`; the allowed selectors are `.btn--primary`, `.state-action:not(.secondary)`, `.register-btn`, `.open-btn`, `.submit-btn`, `.top-bar .save-btn`, `.top-bar .bar-action`, `.bottom-nav a[aria-current="page"]` and the `.swatch--accent*` swatches |
| **Color rule 2**: no success on results | `selectors_using('success', 'success-bg')` against `SUCCESS_OK` | `--success`, `--success-bg` (specimens.css) |
| **Color rule 3a**: depth of dark | `BG_LEVELS` | `--bg-bar`, `--bg-0`, `--bg-1`, `--bg-2`, `--bg-3` (L\* range, chroma and step) |
| **Rule 3a, usage** | a regex on `background: var(--(field-)?line(-sheet)?)` | `--line`, `--field-line` (never a fill; `.sheet-handle` exempt) |
| **Rule 3b**: amber vs HYROX yellow (reported) | `tok('accent')` against `HYROX_REFS`; `RULE_3B_OVERRIDE` | `--accent`; the override holds for the exact hex `#F5B649` only |
| **Contrast PAIRS (109)** | `PAIRS` | `--accent`, `--accent-hover`, `--bg-0` … `--bg-3`, `--bg-bar`, `--chip-text`, `--control-tint`, `--destructive`, `--error`, `--error-bg`, `--field-line`, `--focus`, `--invalid`, `--line`, `--on-accent`, `--success`, `--success-bg`, `--text-1`, `--text-2`, `--text-disabled`, `--warning`, `--warning-bg` |
| **Glass contrast (GLASS_PAIRS, 16)** | `GLASS`, `glass_parts`, `WORST`, `UNDER` | text: `--text-1`, `--text-2`, `--accent`, `--control-tint`, `--destructive`; over `--glass-bar`, `--glass-ground`, `--glass-sheet` (and through them `--bg-bar`, `--bg-0`, `--bg-2`, `--glass-opacity`, `--glass-opacity-sheet`); `WORST = tok('text-1')`; `--scrim` |
| **Signed tokens (180)** | `_defined` vs the stand page | every `:root` token of `kit.css`, `map.css`, `specimens.css` and `stand.css` must appear on the stand; the stand's tables name them in `METRICS`, `SKEL`, `MAP_TRS`, `ICON_PLAN`, `TYPE_CLASS` and the color table |
| **check_overflow** | `scripts/check_overflow.mjs` | no variable names; it depends on the kit's classes and the `--type-unit` math (above) |
| **check_kit** | `scripts/check_kit.py` | no variable names |

**A rename breaks each of these by name.** Renaming `--accent`, `--bg-*`, `--text-*`, `--error`, `--line`, `--field-line`, the glass tokens or `--scrim` needs the same rename in `build_stand.py`: in `PAIRS`, `GLASS_PAIRS`, `BG_LEVELS`, the rule 1 and 2 `selectors_using` calls, the rule 3a regex, `RULE_3B_OVERRIDE`, and the `glass_parts` and `SCRIM_A` parsers (both expect today's exact value format). It also needs the rename in DESIGN.md's frontmatter and its sidecar.
