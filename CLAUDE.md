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
- `results` (personal per-user archive, owner-only via RLS): race_name/date/sport_type (optionally linked to a catalog race), finish_time, category, official_result_url (required), notes.

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
