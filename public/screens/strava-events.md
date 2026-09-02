# Strava — Events tab — screenshots captured (logged-in session)

Playwright (2026-09-02) confirmed the Events tab is unreachable by URL when logged out (`strava-home.png` — redirects to the marketing homepage, no "Events" entry in the public nav). Julia supplied real logged-in mobile screenshots on 2026-09-02 that close that gap: `strava events.PNG`, `strava races.PNG`, `strava event page.PNG`, `strava marathon page.PNG`, `strava marathon page scroll.PNG`, `strava run details.PNG`, `strava weekly run.PNG`.

## Navigation confirmed

Events lives at **Groups → Events** (tab bar: Home / Maps / Record / Groups / You), alongside sibling tabs **Challenges** and **Clubs** — races sit inside Strava's social/community section, not under the primary Home or Maps tabs. This matches the "bolted onto an existing social platform" framing already in `../research.md`'s deep-dive table.

## Two distinct event types live under one tab — this is new information

The Events tab actually surfaces two structurally different things, which the prior WebSearch-only research pass didn't distinguish:

1. **"Local Club Events"** (`strava weekly run.PNG`, `strava event page.PNG`) — recurring, club-hosted social meetups (e.g. "Weekly Run - Parc Drumul Taberei - West Side Running Club," every Thursday). Has `Sport` + `Format` fields (Format: **Social**), a host club card with member count and an "Admin" profile, a "Going" list with named attendees and **Follow** buttons, and a **Join** CTA. This is a social/community feature — attendee identities, follow relationships, recurring meetups — not a race-discovery feature at all.
2. **"Races"** (`strava races.PNG`, `strava marathon page.PNG`, `strava marathon page scroll.PNG`) — actual competitive race listings, sourced/branded via Runna ("558 Runna athletes racing"). This is the section actually comparable to Onrace's map.

## The Races section — real UI, not previously visible

`strava races.PNG` (the "View all" page) shows:
- A **search bar** plus **faceted filter chips**: Sport, Dates, Distance, Location, Elevation, and at least one more cut off in the screenshot (likely Terrain, matching the detail-page fields below) — i.e. Strava's Races browse is exactly the **faceted filter + browse pattern** described in `../research.md`'s "Race-discovery UX patterns" section, not a pure map or pure feed.
- Section headers **"Popular Races For You"** and **"Half Marathons"** — a hybrid of personalized recommendation ("For You") and distance-based curated grouping, horizontally scrollable card rails (not a map view anywhere in these screenshots — no map-based race browsing was observed, only list/card browsing plus filters).
- Race cards show cover photo, date badge, title, and (for Runna-sourced races) a "N Runna athletes racing" social-proof line with avatar stack.

## Race detail page — richer than expected

`strava marathon page.PNG` / `strava marathon page scroll.PNG` (Raiffeisen Bank Bucharest Marathon):
- Distance-variant chips (10km / Half Marathon / Marathon) — one event, multiple race options, selectable.
- Race Date, a long-form description ("AIMS certified..." with "See more"), then a **stats row**: Terrain (Road), Price (lei 105+), Elevation (Flat), **Temperature (22°C), Humidity (Moderate), Wind (Light)** — the weather fields are a genuinely novel addition neither ocrbase nor AllTrails' race-adjacent pages showed; likely modeled/forecast data tied to date+location rather than official race-provided info.
- An actual **route map with the course path drawn on it** and a **Save Route** bookmark action (route data reused from Strava's core Maps/routes feature, not race-specific).
- Two CTAs at the bottom: **"Register"** (external link icon — hands off to the official registration site, same pattern as Onrace's planned `registration_url` field) and **"Train with Runna"** (commercial cross-sell into Strava's paid training-plan product) — confirms Runna's role is both a data source *and* a monetization funnel, not just event metadata supply.

## Still not observed

- No map/pin-based race browsing anywhere in these screenshots — Strava's Races section appears to be list/card + filters only, unlike ocrbase/AllTrails' map-first browsing.
- No HYROX, DEKA, or functional-fitness listings in any screenshot — every race shown is running (10K/Half/Marathon). Doesn't rule out coverage elsewhere, but no evidence of it either; the prior finding ("currently running/cycling-centric, no signal it covers HYROX/DEKA") still holds, now with a concrete UI sample behind it rather than pure inference.
- Personal results/archive tied to a completed race — not captured; these screenshots are all pre-race discovery/registration flows.

## Relevance to Onrace

- Strava's filter set (Sport, Dates, Distance, Location, Elevation, Terrain) is close to a superset of Onrace's planned filters (region, date, sport type) — validates region/date/sport as the right minimum facet set, with distance/elevation as plausible v2 additions once real race data has that detail.
- The weather-stats row and drawn route map are a level of per-race richness Onrace won't attempt at MVP (out of scope, no route/elevation data in the `races` table) — useful as a "what a mature version of this could look like" reference, not an MVP target.
- The "Register" (external link) + "Train with Runna" (in-house upsell) button pairing is a clean model for how a link-out CTA can sit next to a product's own CTA without confusing which one leaves the app — worth the same visual distinction (e.g. filled vs. outline button) when Onrace pairs a race's `registration_url` link-out with any in-app action later.
