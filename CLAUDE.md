# Onrace — Product Brief

## Sources of truth

| What | Where | Changed by |
|---|---|---|
| **Look** (values and components) | `ui/kit.css` (`:root` for values, kit classes for components), shown in `ui/kit.html` | the "keep it" rule (UI assembly below) |
| **Words** (every product line) | `microcopy.md`, rendered in `voice.html` | `microcopy.md` first, then `scripts/build_voice_html.py` |
| **Structure** (screens and states) | `wireframes/*.html` | the page itself, carried to every screen that shares the component |
| **Decisions** (and why) | `concept/concept.md` | a dated entry per decision |

## What it is

Onrace is an interactive map of races for hybrid athletes, plus a personal archive of official race results with links to source. It brings together official hybrid competitions and marathons in one place so athletes can find upcoming races, and centrally store their official results — because registering for elite races (e.g. Boston Marathon) often requires proof of previous official results, which are typically scattered across different timing websites.

## Race scope

A **hybrid-athlete race calendar**, not a single race format. Catalog whatever races hybrid athletes actually train for and compete in: HYROX, DEKA/functional-fitness racing, marathons, half marathons, triathlons, ultras. The unifying thread is the audience (hybrid athletes), not that every race itself is a "hybrid format."

## Core features (MVP)

1. **Interactive map of races** — filterable by region, date, and sport type, plus a search by race name or city (added 2026-09-30, for finding a race you already know; `research/jtbd.md` → Hypothesis 7 `[?]`).
2. **Personal archive of official race results** — each entry links back to the official source (timing site) as proof.

## Target users

Both recreational and competitive/elite hybrid athletes, roughly equally.
- Discovery (map + filters) serves casual racers planning their season.
- The results archive with source links serves anyone who eventually needs official proof of a time (e.g. applying to Boston Marathon).

## People (persona & JTBD summary)

**Primary persona — The HYROX-First Hybrid Athlete.** Trains HYROX as an anchor format with marathons/OCR/functional-fitness as adjacent interests. Wants to find upcoming races across those formats and, more tentatively, keep results from all of them in one place. Full persona set (plus two secondary personas) and sourcing in `research/personas.md`.

**Two main jobs** (co-equal, not one main + related — see `research/jtbd.md`):
1. **Discovery** — see the full range of hybrid races across countries, formats, and dates instead of checking each source separately.
2. **Results archiving** — keep official race results, with source-link proof, in the same place discovery happens.

**Top-3 MVP-core jobs** (only #1 is cleanly "important to the primary persona"; #2–3 rest on market whitespace + a strongly-evidenced secondary persona instead — see `research/jtbd.md` → JTBD × Persona matrix for why):
1. Discovery (above).
2. Log a race result with required source-link proof, **and retrieve it later for an elite-race application.** These are one committed job, not two: logging a result you can never pull back up isn't a functioning feature, so retrieval was always implied by committing to logging — the original list just didn't name the retrieval half explicitly. (Corrected 2026-09-17 to match `sitemap.md`/`flows.md`, which had already fully designed retrieval as its own screen and flow — the design docs were right, this summary list was incomplete.)
3. Results archiving combined with discovery, across formats.

Much of this is still `[?]`-flagged hypothesis, not confirmed by real users — see `research/personas.md` and `research/jtbd.md` for exactly which parts.

## Geographic scope

Global from day one — races seeded from multiple countries/continents, filters support international regions.

## Result trust model

Self-reported with a **required source link**. The user enters their own result and pastes a link to the official timing site as proof; Onrace does not verify it — the link itself is the evidence, mirroring what elite races already require of applicants.

## Business model

Free for now, no monetization plan. Not designing for ads or paywalls at this stage.

## Design / brand tone

Bold & competitive — high-energy, athletic, performance-driven visual identity (dark, intense, bold typography), in the spirit of HYROX/CrossFit branding.

## Explicitly out of scope for MVP

- **Social features** — no following, comments, activity feeds, leaderboards, or public sharing of results.
- **Race registration/payment handling** — Onrace links out to official registration pages only, never handles signups or payments itself.
- **Training plans/coaching content**.
- **Admin/CMS for race data** — races added directly via SQL for now, no admin UI.

## Target timeline

MVP by **2026-11-01** (2 months from brief date, 2026-09-01).

## Tech stack (decided)

- **Frontend**: React + Vite, deployed as a static site via the existing GitHub Actions → GitHub Pages pipeline.
- **Backend**: Supabase (Postgres DB + Auth), accessed client-side via the anon key with Row Level Security — no custom server needed.
- **Auth method (decided 2026-09-25)**: email + password via Supabase Auth, with **Confirm email left on** (Supabase's default): Create account sends a confirmation email, and opening its link signs the person in. Sign-out is local to the device (`signOut({ scope: 'local' })`). No magic links or social sign-in in MVP. Password reset: "Forgot password?" on Sign in → Reset password (email, then "check your inbox") → the emailed link opens New password → back on Sign in with the new password (`flows.md` → Flow 6). Minimum password length 8 `[?]` (a Supabase project setting; default 6).
- **Map**: Leaflet + OpenStreetMap tiles (free, no API key required).
- **Race data**: manually curated/seeded, no scraping in MVP.

## Data model (high-level)

- `races` (public catalog): name, sport_type, event_date, city/region/country, lat/lng, official_url, registration_url, description. One row per *edition*; past editions stay (Race browse shows upcoming ones, Log result's Race picker shows past ones for linking a result).
- `results` (personal per-user archive, owner-only via RLS): race_name/date/sport_type (optionally linked to a catalog race), finish_time, official_result_url (required).
  - `category` and `notes` — removed — no job maps to this; reconsider if the archiving job proves more central after validation.
- `profiles` (one per account, owner-only via RLS; infrastructure, not job-sourced — added 2026-09-25): name, country, language `[?]` (stored preference only; no localization planned). Email comes from Supabase Auth. Photo deferred (would need Supabase Storage, not in the stack yet); initials shown instead. No bio/stats/public fields.

## Information architecture (high-level)

- **Top-level sitemap**: Discovery (Race browse, Race detail) and Results/Archive (Results list, Log result, Race picker — an optional screen pushed from Log result, "‹ Log result" back (a modal until 2026-10-24), to link a past catalog race, Result detail), plus `[INFRASTRUCTURE]` screens that close no job of their own but exist because accounts do (Reset password and New password, Flow 6, sit under the Sign in gate; the two main ones are described here): a contextual Sign in/Sign up gate — surfaces only when an unauthenticated person taps Results (which also gates the Log result action inside it) — and Profile (initials, name, country, language, Sign out), a global tab (added 2026-09-25; reverses the earlier "no job supports Profile" verdict — see `sitemap.md` → Entities → 5). Signed out, the Profile tab opens the same Sign in/Sign up gate as Results. Full detail: `sitemap.md`; rendered view: `ia.html`.
- **Main flow**: Discovery — app opens → Race browse (0 taps, the default/home tab) → Race detail (1 tap) → opens `registration_url` externally. The one job in the whole JTBD matrix that needs no caveats for the primary persona. Full flow diagram, plus Log Result and Retrieve Proof: `flows.md`.
- **Global navigation**: 3 tabs — Discover (Race browse), Results (Results list; "My Results" until the markup pass, 2026-10-23), Profile (Profile). Revised 2026-09-25: Profile became a tab for 1-tap consistency and the familiar Account-tab convention, accepting an auth entry point on every top-level screen, Discover included (Discover itself still gates nothing). This replaces a same-day account button inside Results, kept as superseded. Profile is 1 tap from any top-level screen (2 from Race detail, which has no tab bar); Sign out is 2. **Log result** stays the primary action button inside Results (header + empty state), not a tab: tabs are destinations, actions are buttons (revised 2026-09-24 from the Discover / Log Result / Results bar; costs Log result +1 tap, 1 → 2). Full reasoning, with both superseded versions kept for the record: `sitemap.md` → Navigation § 1–2.
- **Tap-depth to the main job**: 1 tap from app launch to a specific race worth entering, under the 3-tap ceiling.

## Repo / infra already set up

- GitHub: https://github.com/JuliaMakedonska/Onrace (public — required for GitHub Pages on the free plan).
- Live: https://juliamakedonska.github.io/Onrace/
- Auto-deploys via GitHub Actions on every push to `main`.

## Open gaps (not blocking MVP, noted for later)

- Supabase project not yet created — needed before backend work begins.
- No differentiation/competitor analysis done yet.
- Platform is web-only/responsive for now, no native mobile app planned.

## Wireframes

Low-fidelity, grayscale, iOS-structured HTML wireframes for **every screen in `sitemap.md`**, in `wireframes/` (mirrored to `public/wireframes/` for GitHub Pages; keep both in sync). Browse them at https://juliamakedonska.github.io/Onrace/wireframes/: an iPhone frame, the screen tree on the left, and zone notes for the current screen on the right.

- **Screens (10):** Race browse, Race detail (Discovery); Results list, Log result, Race picker, Result detail (archive); Sign in / Sign up, Reset password, New password, Profile (`[INFRASTRUCTURE]`). 35 pages in total: each screen's base page plus one page per real state (`-empty` / `-error` / `-loading`, and two named inbox waits, `-check-inbox`).
- **The rules:** `wireframes/_conventions.md` covers fidelity, soft-gray tokens and radii, iOS system chrome, 3-tab bar vs drill-down vs modal, forms, gates, pickers and alerts, linking along `flows.md` only, state in the URL, the sessionStorage auth session, and test switches.
- **The scope:** `wireframes/_screens.md` has, for every screen, its states (with ✓ or — and the reason) and the shared sample data.
- **Live flows:** every primary action is a real link along `flows.md`'s six flows. System decisions are real checks, and failure branches use reviewer switches (`&fail=1`, `&empty=1`, `?confirmed=1`, …).
- **Review:** `wireframes/_critique.md` holds the 2026-09-25 review: 8 defects found and fixed (dead ends first), with everything else checked clean.
- **Deferred:** color, brand typography, content icons and finished-UI polish (`_conventions.md` § 7).
- **Wireframe / Design toggle (2026-10-18):** the viewer shows either the working page (**Design**, the default: `wireframes/`, updated in place through Lessons 6–7) or its frozen snapshot (**Wireframe**: `wireframes/_wireframe/`, the 35 pages byte-for-byte at commit `7347c27`, the end of Lesson 5 before any painting). The mode is in the URL: `#race-browse?mode=wireframe`, or in the workspace `#04/race-browse?mode=wireframe`. **The snapshot is frozen history, not a copy to maintain:** never edit it, never link it to `ui/kit.css`, and keep it out of the build checks, the inventory and step 7 (`_conventions.md` § 6, `wireframes/_wireframe/README.md`).

## Voice

How Onrace speaks, decided 2026-09-26 to 2026-09-30 and applied to every wireframe screen.

- **`voice.md`** is the rulebook, in precedence order: **Forbidden** (absolute) > **Dictionary** (one concept, one word) > **Microcopy** (the shape of each element type: button, heading, field, empty, error, loading, success, dangerous action) > **Principles** (the why).
- **The five principles**, each grounded in `research/` and the competitor copy scan (`research/research.md` → Competitor language):
  1. Claim only what Onrace can know. A result is "Self-reported · via \<domain\>", never "verified".
  2. Point to the source and let it vouch.
  3. Plain words; the look carries the energy.
  4. Every format by its own name.
  5. No crowd in the copy.
- **Key terms:**
  - things: results archive (label: Results), result, finish time, official result link / official result, race catalog, account (label: Profile), email, confirmation link / reset link, race date.
  - actions: Log result, Register (races only), Create account, Sign in / Sign out, Send a new link (only where the tap sends), Reset password again, Cancel (leave a task), Dismiss (hide a message), Try again, Clear all filters.
  - back buttons name the destination screen.
- **Never:** "all in one place", crush / legendary, motivational lines, hype numbers, community or crowd words, "verified", a minimizing "just", exclamation marks, emoji in system messages, "successfully", Oops-style errors.
- **`microcopy.md`** is the source of truth for every product line: 534 rows with the screen, zone, Before / After, Why, type, states, source, and flags. It separates our copy from catalog data, reference data, user-written text (`race_name`, `finish_time`, `official_result_url`, name, email, search text; never rewritten) and wireframe annotations. It was last checked against all 35 pages on 2026-09-30, with zero mismatches.
- **Rendered view:** `voice.html` (live at https://juliamakedonska.github.io/Onrace/voice.html) shows the principles, Dictionary, Forbidden list, Microcopy rules, and all `microcopy.md` lines, searchable and collapsed by screen. It's generated by `scripts/build_voice_html.py` (writes both `voice.html` and `public/voice.html`); re-run it after changing either `.md`.
- **Closed (markup pass, 2026-10-23):** short buttons ("Try again", the nav-bar "Save", "Dismiss") carry their full accessible names (`voice.md` → Button; `microcopy.md` rows 535–545).

## Concept

The visual concept, Lesson 6 (2026-10-13 to 2026-10-15). Direction A, **Podium**: graphite ground `#131518`, one scarce sodium-amber accent `#F5B649`, Schibsted Grotesk 800 (title, finish time, date day) + Hanken Grotesk 400/600 (everything else), radii 4/6 in content (12 on the stand panels; since step 3b the Filters sheet takes the native sheet radius, 38 [?], and bar controls are capsules), Solar bold icons, black-and-white race photos.

- **Where it lives (`concept/`):**
  - `concept.md`: the rules and every decision.
  - `references.md`: references and the photo log.
  - `concept.html`: the stand, live at https://juliamakedonska.github.io/Onrace/concept/concept.html. Its own layout is `stand.css`.
  - The values and components moved to the kit in Lesson 7 step 3a (2026-10-18): `concept/tokens.css` and `concept/components.css` are now `ui/kit.css`, and `concept/map.css` is now `ui/map.css` (see UI assembly below).
  - Build scripts: `scripts/concept/build_stand.py` runs the checks, writes the stand, stamps the pages that link the kit and mirrors the stand, the kit and the map to `public/`; `scripts/concept/build_map.py` regenerates the map block in `ui/map.css`.
  - Mirror: `concept/` pages and CSS → `public/concept/`.
- **The rules:**
  - Values only from tokens: pages and `ui/kit.css`'s classes hold no raw values (the map pins' inline `left`/`top` went in the markup pass, 2026-10-23).
  - Every token is signed on the stand with its reason, and the build stops if one isn't.
  - Fonts load from each page's `<head>`, not from CSS.
  - Color rules 1–3 (`concept.md` → Color rules) are checked by `build_stand.py` on every build: 1 accent placement, 2 no success color on results, 3a depth of dark. Each stops the build when broken. So does any contrast pair below AA (81 pairs since the kit). So does any horizontal overflow: `scripts/check_overflow.mjs` (2026-10-24) opens every wireframe state in headless Chrome at 390 and 320 wide, Race browse with 0–5 active filters, and fails if anything reaches past the screen edge or scrolls sideways (the chips row excepted), if a one-line control (Sort, Filters, List/Map, chips, Clear all filters) wraps, or if a font didn't load (it serves the pages over local HTTP and measures after `document.fonts.ready`).
  - **3b** (amber vs HYROX yellow) is reported, not blocking: the amber is a **designer override** of 3b (2026-10-14), valid for this exact hex only.
- **Screens in Podium:** Race browse (`race-browse.html` + `-empty`, `-error`, `-loading`) and Results list (`results-list.html` + the same three). They link `ui/kit.css` (Race browse also `ui/map.css`) and keep the wireframes' text and structure. **Since Lesson 7 step 5 (2026-10-22), all 10 screens are on the kit:** Race detail (Discovery, with the card's photo band on top, a designer decision), then the Archive and Infrastructure groups (`concept.md` → Step 5). Every markup change listed in `concept.md` → Deferred to Lesson 7 (markup) and Gap triage → Markup pass still waits for the markup pass.
- **Checked:** step 7 (2026-10-15) found 9 defects against `concept.md` and `/impeccable audit`: 8 fixed, 1 detector false positive (`concept.md` → Step 7 check).

## UI assembly

Lesson 7 (2026-10-18 to 2026-10-25): every screen assembled from one kit, in native iOS. `DESIGN.md` (repo root) is the design system documented from the code, not from intentions; `concept/concept.md` → Native iOS records every step and decision. Overview page: `public/ui-overview.html` (workspace #07), generated by `scripts/build_ui_overview.py` from the repo files.

**Where the kit lives (`ui/`, mirrored to `public/ui/` by `build_stand.py`):**
- **`ui/kit.css`:** the one source of truth. Every token in `:root` (flat; two-level tokens are Lesson 8) and every component class, with no raw values in the classes. Each component is defined once and nothing in it goes unused by the screens.
- **`ui/map.css`:** the static map's data: its tokens, the Natural Earth masks, and each pin's place keyed on `data-pin`. Linked by the Race browse pages (not render-blocking) and the showcase.
- **`ui/shell.html`:** the shell, the large-title header and the floating tab bar.
- **`ui/kit.html`:** the showcase, every inventory component in its states, with the screens' own text (live: https://juliamakedonska.github.io/Onrace/ui/kit.html). The specimens are hand-written; `scripts/build_kit_showcase.py` (run by the build) arranges them by role under a sticky nav and writes each one's facts (classes, the screens that use it, its native iOS counterpart) from `ui/inventory.md` → Showcase map.
- **`ui/inventory.md`:** every component of the 10 screens, with its screens, states, photo, HIG link and gaps.
- **Stand-only values** live outside the kit: `concept/specimens.css` (the `.btn` family, status messages, the success and warning tokens), `concept/stand.css`, `concept/first-screen.css`.

**Visuals (`visuals/`):** Onrace's own black-and-white race photos (generated, checked for text and logos, retouched locally), each pre-cropped to its 3:1 band at 684 and 1026 px in AVIF, WebP and JPEG with `srcset`. How they were made, checked and exported: `visuals/README.md`. Mirrored to `public/visuals/` by the build.

**The rules:**
- **Every screen links the kit** (`ui/kit.css`, plus `ui/map.css` on Race browse) and has no style block, no inline style and no class the kit doesn't define. **Nothing new on a screen:** a new component or variant goes into the kit and the showcase first.
- **"Keep it" rule (2026-10-25):** when I say "keep it" (залишаємо) about a visual change, update the kit (`ui/kit.css` and the showcase `ui/kit.html`), sign the reason in `DESIGN.md`, and carry any markup change to every screen where the component appears.
- **Native iOS rule (designer, 2026-10-18):** every element with a native iOS counterpart follows Apple's [Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines) for anatomy, metrics and behavior; Podium supplies only the look. The component-to-HIG table (e.g. [Tab bars](https://developer.apple.com/design/human-interface-guidelines/tab-bars), [Sheets](https://developer.apple.com/design/human-interface-guidelines/sheets), [Alerts](https://developer.apple.com/design/human-interface-guidelines/alerts), [Segmented controls](https://developer.apple.com/design/human-interface-guidelines/segmented-controls), [Lists and tables](https://developer.apple.com/design/human-interface-guidelines/lists-and-tables)) and the decided conflicts C1–C7 are in `DESIGN.md` → Native iOS. Glass, sheet and alert radii are **provisional [?]** (Apple's iOS 26 kit wasn't read).
- **The build checks** (`python3 scripts/concept/build_stand.py`), listed below; any failure stops the build.

**Checks that stop the build** (`build_stand.py`, `check_overflow.mjs`, `check_kit.py`):

1. Color rule 1: the accent only where you act or where you are (`ACCENT_OK`).
2. Color rule 2: no success color on results; on the stand's markup, no result carries a success mark and the proof line states its source.
3. Color rule 3a: the depth of dark, background levels in even steps.
4. Contrast: every text pair at WCAG AA, glass against its worst case behind it.
5. Signed tokens: every token in `ui/kit.css`, `ui/map.css` and the stand's files has a row on the stand with its reason.
6. Overflow: every wireframe state at 390, at 320 and at 390 with 200% text (Race browse with 0–5 filters, the sheet, the map, the alerts): nothing past the screen edge, nothing scrolling sideways but the chips row.
7. One line: Sort, Filters, List/Map, the filter chips and Clear all filters never wrap.
8. Fonts: every family and weight a page renders text in has loaded, so the real fonts are measured.
9. Scripts and styles: no page script throws, and every deferred stylesheet applies.
10. The showcase against the inventory: every inventory component has a Showcase map row, a specimen and every state it lists (`scripts/check_kit.py`).
11. The showcase's words: every word in a specimen is in `microcopy.md` (`scripts/check_kit.py`).

- **Accessible names start with the visible label** (WCAG 2.5.3); text changes go through `microcopy.md` first, then `scripts/build_voice_html.py`.
- **The record:** `concept.md` → Native iOS, step by step (3a, 3b, 5, Consolidation, the markup passes, Overflow fix, Step 6, Step 7). Before/after of each step: `ui/review-3b.html`, `ui/review-step5.html`, `ui/review-markup.html`, `ui/review-markup-2.html`, `ui/review-overflow.html`, `ui/review-step6.html`, `ui/review-step7.html`, and the lesson pages and showcase restructure (2026-10-26): `ui/review-lessons.html`; the photos' round 3: `visuals/review-round3.html`.
- **Lesson pages:** the 06 and 07 overviews share one template, `scripts/lesson_page.py` ("Lesson N of 12", the dates, the sources of truth, a stats strip read from the repo, the stage nav, what we saw and decided, a decision register from `concept.md`, and what's open mapped to the lesson that takes it); `build_stand.py` rebuilds both after the kit.

**Wireframe / Design toggle:** the viewer (`wireframes/index.html`) shows each screen as it is now (**Design**, `wireframes/`) or as the frozen Lesson 5 snapshot (**Wireframe**, `wireframes/_wireframe/`, `#race-browse?mode=wireframe`). The snapshot is history: never edit it, never link it to the kit, and keep it out of the build checks (see Wireframes above).

## Status

Pre-implementation. The IA (`sitemap.md`, `flows.md`, `ia.html`), the full wireframe set, the visual concept and the UI assembly (Lesson 7, above: all 10 screens on one kit, native iOS, the critique and the final check closed with no open defect) are done. No product code yet: `src/` is still the Vite scaffold. Next: Lesson 8, design tokens (`tokens/`), then `components/`, `design-system/`, `handoff/`.
