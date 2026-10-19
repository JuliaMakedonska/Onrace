# Onrace — Product Brief

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

- **Top-level sitemap**: Discovery (Race browse, Race detail) and My Results/Archive (Results list, Log result, Race picker — an optional modal from Log result to link a past catalog race, Result detail), plus `[INFRASTRUCTURE]` screens that close no job of their own but exist because accounts do (Reset password and New password, Flow 6, sit under the Sign in gate; the two main ones are described here): a contextual Sign in/Sign up gate — surfaces only when an unauthenticated person taps My Results (which also gates the Log result action inside it) — and Profile (initials, name, country, language, Sign out), a global tab (added 2026-09-25; reverses the earlier "no job supports Profile" verdict — see `sitemap.md` → Entities → 5). Signed out, the Profile tab opens the same Sign in/Sign up gate as My Results. Full detail: `sitemap.md`; rendered view: `ia.html`.
- **Main flow**: Discovery — app opens → Race browse (0 taps, the default/home tab) → Race detail (1 tap) → opens `registration_url` externally. The one job in the whole JTBD matrix that needs no caveats for the primary persona. Full flow diagram, plus Log Result and Retrieve Proof: `flows.md`.
- **Global navigation**: 3 tabs — Discover (Race browse), My Results (Results list), Profile (Profile). Revised 2026-09-25: Profile became a tab for 1-tap consistency and the familiar Account-tab convention, accepting an auth entry point on every top-level screen, Discover included (Discover itself still gates nothing). This replaces a same-day account button inside My Results, kept as superseded. Profile is 1 tap from any top-level screen (2 from Race detail, which has no tab bar); Sign out is 2. **Log result** stays the primary action button inside My Results (header + empty state), not a tab: tabs are destinations, actions are buttons (revised 2026-09-24 from the Discover / Log Result / My Results bar; costs Log result +1 tap, 1 → 2). Full reasoning, with both superseded versions kept for the record: `sitemap.md` → Navigation § 1–2.
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
  - things: results archive (label: My Results), result, finish time, official result link / official result, race catalog, account (label: Profile), email, confirmation link / reset link, race date.
  - actions: Log result, Register (races only), Create account, Sign in / Sign out, Send a new link (only where the tap sends), Reset password again, Cancel (leave a task), Dismiss (hide a message), Try again, Clear all filters.
  - back buttons name the destination screen.
- **Never:** "all in one place", crush / legendary, motivational lines, hype numbers, community or crowd words, "verified", a minimizing "just", exclamation marks, emoji in system messages, "successfully", Oops-style errors.
- **`microcopy.md`** is the source of truth for every product line: 534 rows with the screen, zone, Before / After, Why, type, states, source, and flags. It separates our copy from catalog data, reference data, user-written text (`race_name`, `finish_time`, `official_result_url`, name, email, search text; never rewritten) and wireframe annotations. It was last checked against all 35 pages on 2026-09-30, with zero mismatches.
- **Rendered view:** `voice.html` (live at https://juliamakedonska.github.io/Onrace/voice.html) shows the principles, Dictionary, Forbidden list, Microcopy rules, and all `microcopy.md` lines, searchable and collapsed by screen. It's generated by `scripts/build_voice_html.py` (writes both `voice.html` and `public/voice.html`); re-run it after changing either `.md`.
- **Known gap:** short buttons ("Try again", the nav-bar "Save", "Dismiss") still need full accessible names. That's a dedicated markup pass (`voice.md` → Button; `wireframes/_critique.md` #10).

## Concept

The visual concept, Lesson 6 (2026-10-13 to 2026-10-15). Direction A, **Podium**: graphite ground `#131518`, one scarce sodium-amber accent `#F5B649`, Schibsted Grotesk 800 (title, finish time, date day) + Hanken Grotesk 400/600 (everything else), radii 4/6 in content (12 on the stand panels; since step 3b the Filters sheet takes the native sheet radius, 38 [?], and bar controls are capsules), Solar bold icons, black-and-white race photos.

- **Where it lives (`concept/`):**
  - `concept.md`: the rules and every decision.
  - `references.md`: references and the photo log.
  - `concept.html`: the stand, live at https://juliamakedonska.github.io/Onrace/concept/concept.html. Its own layout is `stand.css`.
  - The values and components moved to the kit in Lesson 7 step 3a (2026-10-18): `concept/tokens.css` and `concept/components.css` are now `ui/kit.css`, and `concept/map.css` is now `ui/map.css` (see UI kit below).
  - Build scripts: `scripts/concept/build_stand.py` runs the checks, writes the stand, stamps the pages that link the kit and mirrors the stand, the kit and the map to `public/`; `scripts/concept/build_map.py` regenerates the map block in `ui/map.css`.
  - Mirror: `concept/` pages and CSS → `public/concept/`.
- **The rules:**
  - Values only from tokens: pages and `ui/kit.css`'s classes hold no raw values. The one exception is the map pins' inline `left`/`top` (deferred to Lesson 7).
  - Every token is signed on the stand with its reason, and the build stops if one isn't.
  - Fonts load from each page's `<head>`, not from CSS.
  - Color rules 1–3 (`concept.md` → Color rules) are checked by `build_stand.py` on every build: 1 accent placement, 2 no success color on results, 3a depth of dark. Each stops the build when broken. So does any contrast pair below AA (81 pairs since the kit).
  - **3b** (amber vs HYROX yellow) is reported, not blocking: the amber is a **designer override** of 3b (2026-10-14), valid for this exact hex only.
- **Screens in Podium:** Race browse (`race-browse.html` + `-empty`, `-error`, `-loading`) and Results list (`results-list.html` + the same three). They link `ui/kit.css` (Race browse also `ui/map.css`) and keep the wireframes' text and structure. **The other 8 screens stay grayscale until Lesson 7**, as does every markup change listed in `concept.md` → Deferred to Lesson 7 (markup).
- **Checked:** step 7 (2026-10-15) found 9 defects against `concept.md` and `/impeccable audit`: 8 fixed, 1 detector false positive (`concept.md` → Step 7 check).

## UI kit

Lesson 7 (2026-10-18). `DESIGN.md` (repo root) is the design system documented from the two painted screens; `concept/concept.md` follows the screens. `concept.md` → Native iOS holds the HIG rule, the decided HIG-vs-Podium conflicts (C1–C7), and the 33 gaps triaged into kit, markup pass and out of scope.

- **`ui/inventory.md`:** every component of all 10 screens, with its screens, states, photo, HIG link and gaps.
- **`ui/kit.css`:** the one source of truth. Every variable in `:root` (flat; two-level tokens are Lesson 8) and every component class, with no values in the classes. Grayscale screens' components are in it too, styled from DESIGN.md, though those screens don't link it yet.
- **`ui/map.css`:** the static map's data (tokens and Natural Earth masks), linked by the Race browse pages and the kit showcase only.
- **`ui/shell.html`:** the shell (large-title header and tab bar), no status bar.
- **`ui/kit.html`:** the showcase, every inventory component in its states, live at https://juliamakedonska.github.io/Onrace/ui/kit.html.
- **Step 3a** extracted the kit exactly as the screens look. The 8 Podium pages are byte-identical before and after at 390×844 (12 states).
- **Kit feedback + step 3b (2026-10-19):** initials a circle, Save amber on Log result, destructive Sign out, coral invalid ring; then the native iOS pass (Kit (CSS) gaps + C1, C3, C4, C6, C7): glass bars and sheet, floating tab bar, HIG type sizes, Dynamic Type units, skeleton pulse, busy spinner, disclosure, pressed states. Glass blur, rim, margins and the sheet radius are **provisional [?]** (Apple's iOS 26 kit wasn't read). 3b review (same day): all bar controls full capsules (search, Filters, List/Map; C7), glass action bar, result-row chevron on the meta row (times and proof lines don't move), empty/error states as one ContentUnavailableView-style component. `.impeccable/design.json` is generated from DESIGN.md by `scripts/build_design_sidecar.py`. Record: `concept.md` → Step 3b, Step 3b review. Before/after of every painted state: `ui/review-3b.html`.
- **Mirror:** `ui/` → `public/ui/` (`build_stand.py` does it).

## Status

Pre-implementation. The IA (`sitemap.md`, `flows.md`, `ia.html`), the full low-fidelity wireframe set and the visual concept (above) are done. No product code yet: `src/` is still the Vite scaffold. Next: Lesson 7 (markup), then `tokens/`, `components/`, `design-system/`, `handoff/`.
