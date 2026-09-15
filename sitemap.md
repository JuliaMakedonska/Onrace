# Sitemap

Draft. Built bottom-up from `research/jtbd.md`, `research/personas.md`, and `research/research.md` — entities before screens, per the working method: no screen or navigation should be proposed until the objects a person actually deals with are named and traced to a job.

## Entities

Each entity below is included because a specific job in `jtbd.md` produces or requires it. Entities with no job behind them are listed separately under **Under question**, not mixed in here. `[?]` marks a part of an entity that's assumed rather than sourced.

---

### 1. Race listing

A single catalog entry for a race a hybrid athlete could enter.

**Fields/parts** (per `../CLAUDE.md` → `races` table, matched against the matrix in `jtbd.md`):
- name
- sport_type
- event_date
- city / region / country
- lat/lng
- official_url
- registration_url (link-out only — Onrace never handles the signup itself, per `../CLAUDE.md` → Explicitly out of scope)
- description

**Job:** Main Job 1 — Discovery (`jtbd.md`: "see the full range of options — across countries, formats, and dates... instead of checking each source separately"). Also serves Related Job 1 ("see what's coming up in the formats I actually care about") and Related Job 2 ("weigh them by where they are").

**Connects to:**
- **Search/filter criteria** — the set a race listing is matched against (region, date, sport_type)
- **Logged result** — a result can *optionally* link back to a race listing (`../CLAUDE.md` → `results` table: "race_name/date/sport_type, optionally linked to a catalog race")
- its own lat/lng is what a map view (a screen, not an entity) would plot — not treated as a separate entity here

---

### 2. Search / filter criteria

The set of facets a person narrows the race catalog by.

**Fields/parts** (per `../CLAUDE.md` MVP feature 1 and `research.md` → PATTERNS: "faceted filtering (region, date, sport type) layered on top" of the map):
- region
- date (range)
- sport_type

**Job:** Main Job 1 — Discovery, directly ("across countries, formats, and dates"). Also Related Job 1 (format-driven planning) and Related Job 2 (location-driven planning) — `jtbd.md` ties these two related jobs to filtering by sport_type and by region/location respectively.

**Connects to:** Race listing (the collection it's applied against).

---

### 3. Logged result

A personal, owner-only archive entry recording a race a person has actually completed.

**Fields/parts** (per `../CLAUDE.md` → `results` table, after the `category`/`notes` cut documented in `jtbd.md` → "Feature-candidates to cut"):
- race_name
- date
- sport_type
- optional link to a Race listing
- finish_time
- official_result_url (**required** — not optional)

**Job:** Related Job 3 — "When I finish a race, I want to log the result along with where it came from, so that I have proof ready without having to redo the work later" (toward Main Job 2 — Results archiving). Sourced to the Qualifying-Time Archivist persona specifically, not the primary persona (`jtbd.md` matrix: Related Job 3 scores 3 for the Archivist, only a caveated 2, general/non-specific, for the primary persona).

**Connects to:**
- **Race listing** — optional link
- **Source-link proof** — the required official_result_url is what makes this entry usable as evidence (see below)
- the archive owner (see Athlete account, under question) via row-level ownership — no separate "archive" entity exists beyond "logged results filtered to one owner"

---

### 4. Source-link proof

The external evidence attached to a logged result — called out as its own entity here (rather than folded silently into Logged result's field list) because `research.md` treats it as the product's core trust mechanism, not an incidental field.

**Fields/parts:**
- official_result_url (the mandatory link itself — same field as on Logged result; this entity is that field plus its *display treatment*, not a separately stored object)
- display label showing the source, e.g. "self-reported, via [domain of official_result_url]" — never a checkmark or "verified" badge (`research.md` → BENCHMARK, mechanism #2: "Structurally label every result as self-reported + source-linked, never as 'verified'")

**Job:** Related Job 3 (logging with proof) and Related Job 4 — "When an elite race asks me to prove a past result, I want to pull that proof up quickly, so that I can apply without scrambling to find it." Both trace to the Qualifying-Time Archivist persona and to `research.md` → Proof-of-result findings (Boston Marathon's accepted-proof types).

**Connects to:** Logged result (it's attached to exactly one).

---

## Under question

Not included above because no job in `jtbd.md` produces or requires them directly — listed here so they aren't silently dropped, not because they're necessarily wrong.

- **Athlete account / identity `[?]`** — assumed necessary for "owner-only via RLS" per-user archives (`../CLAUDE.md` → Data model) and for the emotional job ("recognized as what I actually am — a hybrid athlete," `jtbd.md` → Emotional and social jobs). But no job explicitly asks for a profile object with its own fields (name, avatar, etc.) — everything sourced so far only requires *ownership*, not a profile. Needs a fields decision only if a future job requires one.
- **Automated plausibility check / flag `[?]`** — proposed in `research.md` → BENCHMARK top-3 mechanism #3 and CONCLUSIONS gap 4 (dead-link detection, implausible-time flags, duplicate detection) as a trust-building mechanism. Not traced to any specific JTBD job — it's the researcher's proposed system behavior, not something a person's job produces or asks for. Would attach to Logged result / Source-link proof if built.
- **Saved season plan / itinerary `[?]`** — the Multi-Region Season Planner persona's job ("browse races spatially to decide where to travel/compete next") describes *browsing* behavior only; no job or data-model field in `../CLAUDE.md` describes saving, bookmarking, or persisting a shortlist. Flagged so it isn't assumed later without a job behind it.
- **Results map (a map of countries/locations where the user has competed) `[?]`** — a feature idea raised in this session, not sourced to any job in `jtbd.md`. Related Jobs 3–4 (logging a result with proof; retrieving proof for an application) are about producing and retrieving evidence, not about visualizing geographic spread of past results, and no other job describes wanting a spatial view of one's own history. Compelling on its own terms and worth validating later — plausibly a natural extension of the Qualifying-Time Archivist's job (a byproduct view of results already logged with location data), or a new hypothesis to add to `jtbd.md` if pursued — but currently not a confirmed requirement. Do not treat as an entity or design a screen for it until it's traced to a job the way the four entities above are.

---

## Screens

Grouped by the two entity clusters from the Entities section above (Discovery = Race listing + Search/filter criteria; Archive = Logged result + Source-link proof), not by generic "site sections." Every screen is tagged with the `jtbd.md` job it serves; `[ORPHAN]` marks a screen with no job behind it. Loading/empty/error states are noted inline as *states*, not listed as their own screens.

```
Onrace — entry point (Main Job 2 — jtbd.md: "I want that in one product, so that I'm
│                      not maintaining two separate habits or tools"
│                      — CAVEAT: scores only a caveated 2 for Primary, `[?]`
│                      unscored for the Archivist, per jtbd.md's JTBD × Persona matrix.
│                      Included because the entry point is where "one product" is
│                      actually experienced, not because this job is strongly evidenced.)
│                      → Primary: weak/inferred. Secondary (Archivist): unconfirmed [?].
│                      Secondary (Season Planner): not evidenced for this screen.
│
├── Discovery  [object: Race listing + Search/filter criteria]
│   │
│   ├── Race browse (map + list)
│   │     Job: Main Job 1 — "see the full range of options — across countries,
│   │     formats, and dates — instead of checking each source separately"
│   │     (jtbd.md); + Related Job 1 (plan season by format); + Related Job 2
│   │     (choose races by location).
│   │     Persona: Primary (core) + Secondary — Season Planner (core, Related Job 2).
│   │     States (not separate screens): loading · no races match current
│   │     filters · fetch error.
│   │
│   └── Race detail
│         Job: Main Job 1 (jtbd.md: "...so that I can compare them in one
│         place" — viewing one listing's official_url/registration_url/
│         description is how that comparison actually happens).
│         Persona: Primary + Secondary — Season Planner.
│
└── My Results (Archive)  [object: Logged result + Source-link proof]
    │
    ├── Results list ("my archive")
    │     Job: Related Job 4 — retrieve proof for an elite-race application
    │     (jtbd.md); + Main Job 2 (caveated, see entry-point note above).
    │     Persona: Secondary — Archivist (core, Related Job 4 scores a clean 3).
    │     Primary: weak/caveated only (Main Job 2 = 2 for Primary).
    │
    ├── Log result
    │     Job: Related Job 3 — "log the result along with where it came from,
    │     so that I have proof ready without having to redo the work later"
    │     (jtbd.md).
    │     Persona: Secondary — Archivist (core, scores 3). Primary: weak/general
    │     only — jtbd.md's matrix explicitly labels the Primary-persona cell here
    │     "2 (weak/general)," i.e. generic trust-mechanism reasoning, not
    │     persona-specific evidence.
    │     States (not separate screens): empty form · submit error (e.g.
    │     unreachable source link).
    │
    └── Result detail (proof view)
          Job: Related Job 4 — "pull that proof up quickly" (jtbd.md).
          Persona: Secondary — Archivist ONLY. jtbd.md scores this job a
          sourced **1** for the Primary persona — an actual disconfirmation,
          not just an absence of evidence — because HYROX Worlds qualification
          is placement-based, not proof-of-time. Do not design this screen
          around the Primary persona's framing (see personas.md/jtbd.md's own
          design-implication note).

Sign in / Sign up  [ORPHAN]
  No job in jtbd.md calls for account creation or login. Included here only
  because "Logged result" is owner-only per ../CLAUDE.md's data model, and
  the underlying "Athlete account" entity itself was already flagged `[?]`
  under question in this file's Entities section — this screen inherits that
  same lack of sourcing. Needed for both personas technically (to make
  ownership work), but not sourced to any stated job.
```

**Jobs with no screen of their own:** the Emotional job ("recognized as what I actually am — a hybrid athlete") and the Social job ("the proof itself to stand on its own") don't produce distinct screens — per `jtbd.md`, they describe how existing screens should read (tone/framing on Discovery; the self-reported-source-linked display convention on Result detail), not separate destinations. Not listed as screens or orphans for that reason.

**Not included:** a screen for the Results map idea flagged under Entities → Under question — it stays unbuilt until it's traced to a job.

---

*Depth kept minimal deliberately — additional levels (e.g. within Log result, within Race detail) are Step 3, not this pass.*
