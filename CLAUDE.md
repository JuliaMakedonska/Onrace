# Onrace — Product Brief

## What it is

Onrace is an interactive map of races for hybrid athletes, plus a personal archive of official race results with links to source. It brings together official hybrid competitions and marathons in one place so athletes can find upcoming races, and centrally store their official results — because registering for elite races (e.g. Boston Marathon) often requires proof of previous official results, which are typically scattered across different timing websites.

## Race scope

A **hybrid-athlete race calendar**, not a single race format. Catalog whatever races hybrid athletes actually train for and compete in: HYROX, DEKA/functional-fitness racing, marathons, half marathons, triathlons, ultras. The unifying thread is the audience (hybrid athletes), not that every race itself is a "hybrid format."

## Core features (MVP)

1. **Interactive map of races** — filterable by region, date, and sport type.
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
- **Map**: Leaflet + OpenStreetMap tiles (free, no API key required).
- **Race data**: manually curated/seeded, no scraping in MVP.

## Data model (high-level)

- `races` (public catalog): name, sport_type, event_date, city/region/country, lat/lng, official_url, registration_url, description.
- `results` (personal per-user archive, owner-only via RLS): race_name/date/sport_type (optionally linked to a catalog race), finish_time, official_result_url (required).
  - `category` and `notes` — removed — no job maps to this; reconsider if the archiving job proves more central after validation.

## Information architecture (high-level)

- **Top-level sitemap**: Discovery (Race browse, Race detail) and My Results/Archive (Results list, Log result, Result detail), plus a contextual Sign in/Sign up gate that closes no job of its own — surfaces only when an unauthenticated person taps My Results (which also gates the Log result action inside it). Full detail: `sitemap.md`; rendered view: `ia.html`.
- **Main flow**: Discovery — app opens → Race browse (0 taps, the default/home tab) → Race detail (1 tap) → opens `registration_url` externally. The one job in the whole JTBD matrix that needs no caveats for the primary persona. Full flow diagram, plus Log Result and Retrieve Proof: `flows.md`.
- **Global navigation**: 2 tabs — Discover (Race browse), My Results (Results list). **Log result** is the primary action button inside My Results (header + empty state), not a tab: tabs are destinations, actions are buttons. Revised 2026-09-24 from 3 tabs (Discover / Log Result / My Results); costs Log result +1 tap (1 → 2). Full reasoning, with the superseded 3-item version kept for the record: `sitemap.md` → Navigation § 1–2.
- **Tap-depth to the main job**: 1 tap from app launch to a specific race worth entering, under the 3-tap ceiling.

## Repo / infra already set up

- GitHub: https://github.com/JuliaMakedonska/Onrace (public — required for GitHub Pages on the free plan).
- Live: https://juliamakedonska.github.io/Onrace/
- Auto-deploys via GitHub Actions on every push to `main`.

## Open gaps (not blocking MVP, noted for later)

- Supabase project not yet created — needed before backend work begins.
- No differentiation/competitor analysis done yet.
- Platform is web-only/responsive for now, no native mobile app planned.

## Status

Pre-implementation. Repo holds the Vite scaffold, the deploy pipeline, and the design-process folder structure (`research/`, `wireframes/`, `concept/`, `tokens/`, `components/`, `design-system/`, `handoff/` — see `README.md` for what each holds). No product code or design work has been produced yet.
