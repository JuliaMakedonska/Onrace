# Onrace

An interactive map of races for hybrid athletes, plus a personal archive of official race results with links to source.

Full product brief: [`CLAUDE.md`](./CLAUDE.md). Live app: https://juliamakedonska.github.io/Onrace/

## Repo structure

This is a living index — update it as folders fill up or their purpose shifts.

| Path | Purpose | Status |
|---|---|---|
| [`research/`](./research/research.md) | Discovery notes: competitor/reference audit, findings → decisions | Drafted |
| ↳ People | [`personas.md`](./research/personas.md) (3 personas) + [`jtbd.md`](./research/jtbd.md) (jobs to be done, JTBD × persona matrix) | Drafted from desktop research; primary interviews not started |
| `research/screens/` | Reference screenshots gathered during research | Empty |
| [`sitemap.md`](./sitemap.md) | Information architecture: entities, screens (tagged by job), navigation, job-traceability matrix | Drafted |
| [`flows.md`](./flows.md) | User flows (Mermaid): three job flows (Discovery, Log Result, Retrieve Proof) and three infrastructure flows (Sign up with email confirmation, Profile and sign out, Password reset), with every decision/state/endpoint reasoned out | Drafted |
| ↳ Rendered view | [`ia.html`](./ia.html) — the sitemap tree, all six flow diagrams (three job flows, three infrastructure), and the traceability matrix as one page | Drafted |
| [`microcopy.md`](./microcopy.md) | Every interface line from the wireframes in one table (screen, zone, line, type), with inconsistencies flagged, becoming the source of truth for product copy | Transcribed, flags open |
| [`wireframes/`](./wireframes/README.md) | Low-fidelity, grayscale, iOS-structured wireframes for every sitemap screen and state, linked along the flows | Done: 10 screens, 35 pages ([live](https://juliamakedonska.github.io/Onrace/wireframes/)) |
| [`concept/`](./concept/README.md) | Visual direction exploration — moodboards, style tiles | Empty |
| [`tokens/`](./tokens/README.md) | Design tokens (color, type, spacing, radius, elevation) | Empty |
| [`components/`](./components/README.md) | Reusable UI component specs | Empty |
| [`design-system/`](./design-system/README.md) | Assembled tokens + components as a documented system | Empty |
| [`handoff/`](./handoff/README.md) | Dev-ready specs/assets for implementation | Empty |
| `src/` | App source code (currently the unmodified Vite scaffold) | Placeholder |
| `.github/workflows/` | CI: auto-deploys `main` to GitHub Pages | Working |

Intended flow: `research/` → `sitemap.md`/`flows.md` (IA) → `wireframes/` → `concept/` → `tokens/` → `components/` → `design-system/` → `handoff/` → implementation in `src/`.

## Wireframes

[`wireframes/`](./wireframes/README.md) holds the full low-fidelity set: 10 screens, 35 pages, one per real state. Browse them live at https://juliamakedonska.github.io/Onrace/wireframes/: an iPhone frame, the screen tree on the left, and zone notes on the right.

| File | What it is |
|---|---|
| [`index.html`](./wireframes/index.html) | The browsing shell: device frame, screen tree, zone notes |
| [`_conventions.md`](./wireframes/_conventions.md) | The contract every page follows: fidelity, tokens, iOS chrome, linking, states, test switches |
| [`_screens.md`](./wireframes/_screens.md) | Per-screen state scoping (✓ or — with reasons) and shared sample data |
| [`_critique.md`](./wireframes/_critique.md) | The 2026-09-25 review: defects found and fixed, and what was checked clean |

The pages are wired along `flows.md`'s six flows (sign-in gate, catalog link, email confirmation, sign-out, password reset), so every path can be clicked through. Color, brand type and content icons are deferred to `concept/`.

## Tech stack

React + Vite · Supabase (Postgres + Auth) · Leaflet + OpenStreetMap · deployed to GitHub Pages via GitHub Actions.

## Status

Pre-implementation. IA and wireframes are done; product code hasn't started. See [`CLAUDE.md`](./CLAUDE.md) for the full brief, scope, and open gaps.
