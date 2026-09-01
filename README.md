# Onrace

An interactive map of races for hybrid athletes, plus a personal archive of official race results with links to source.

Full product brief: [`CLAUDE.md`](./CLAUDE.md). Live app: https://juliamakedonska.github.io/Onrace/

## Repo structure

This is a living index — update it as folders fill up or their purpose shifts.

| Path | Purpose | Status |
|---|---|---|
| [`research/`](./research/research.md) | Discovery notes: competitor/reference audit, user research, findings → decisions | Skeleton only |
| `research/screens/` | Reference screenshots gathered during research | Empty |
| [`wireframes/`](./wireframes/README.md) | Low-fidelity layout explorations for core screens | Empty |
| [`concept/`](./concept/README.md) | Visual direction exploration — moodboards, style tiles | Empty |
| [`tokens/`](./tokens/README.md) | Design tokens (color, type, spacing, radius, elevation) | Empty |
| [`components/`](./components/README.md) | Reusable UI component specs | Empty |
| [`design-system/`](./design-system/README.md) | Assembled tokens + components as a documented system | Empty |
| [`handoff/`](./handoff/README.md) | Dev-ready specs/assets for implementation | Empty |
| `src/` | App source code (currently the unmodified Vite scaffold) | Placeholder |
| `.github/workflows/` | CI: auto-deploys `main` to GitHub Pages | Working |

Intended flow: `research/` → `wireframes/` → `concept/` → `tokens/` → `components/` → `design-system/` → `handoff/` → implementation in `src/`.

## Tech stack

React + Vite · Supabase (Postgres + Auth) · Leaflet + OpenStreetMap · deployed to GitHub Pages via GitHub Actions.

## Status

Pre-implementation — see [`CLAUDE.md`](./CLAUDE.md) for the full brief, scope, and open gaps.
