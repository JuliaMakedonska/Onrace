# Screens — Main flow (Main Job 1, Discovery, Primary persona)

Scope: only the screens that close **Main Job 1 — Discovery** for the Primary persona (The HYROX-First Hybrid Athlete) and sit on her main path to a race worth entering. Built from `../sitemap.md` (Screens, Navigation, Traceability sections) and `../flows.md` (the "Main Job 1 — Discovery" flow only).

Everything else — Log Result, Results list, Result detail, Sign in/Sign up — is deliberately left alone here. Sign in/Sign up in particular never appears on this path: per `../sitemap.md` → Navigation § 3, it's a contextual gate on Log Result / My Results only, and Discovery "doesn't require an account at all." These get picked up in Step 8.

Two screens qualify — the only two rows in `../sitemap.md`'s Traceability matrix checked for Main Job 1, and the only two screen nodes (`["..."]`) in `../flows.md`'s Discovery flowchart:

- **Race browse**
- **Race detail**

---

## Race browse

**Job it closes:** Main Job 1 — Discovery.
> "When I'm looking for hybrid races to enter, I want to see the full range of options — across countries, formats, and dates — instead of checking each source separately, so that I can compare them in one place." (`../research/jtbd.md` → Main Job 1)

Per `../sitemap.md`, Race browse also serves Related Job 1 (plan season by format) and Related Job 2 (choose races by location) — noted for context, but Main Job 1 is what puts it on this main path.

**Where it sits in the flow** (`../flows.md` → "Main Job 1 — Discovery"): the entry node. `App opens → Race browse` at 0 taps — per `../sitemap.md` → Navigation § 2, it's the default/home tab, "the one clean job gets the one screen that costs nothing to reach." It's also the most-revisited node in the diagram: filter changes loop back into it (`Browse → Loading → ... → Browse`), and it's the landing point after backing out of Race detail ("back / compares another race"). From here, tapping a race card or pin is the 1-tap transition into Race detail.

**States:**

| State | Real? | Why |
|---|:---:|---|
| Empty | ✓ | `HasResults` → "no" → `Empty("Empty: no races match current filters")`. A legitimate data state, not an error — resolved by adjusting filters or giving up (merges into `DeadEnd1`). |
| Error | ✓ | `Loading` → "connection fails" → `FetchError("Error: could not load races")`, with a `Retry?` diamond: "yes" retries the fetch (back to `Loading`), "no" gives up (merges into `DeadEnd1`). |
| Loading | ✓ | `Loading("Loading: fetching races")` — fires on entry and again on every filter change. |
| Success | — | No distinct "it worked" endpoint on this screen. Reaching `HasResults` → "yes" just re-displays `Browse` — normal browsing, not a terminal. The flow's actual `Success` node is scoped to Race detail (opening `registration_url`), not to browsing itself. |

---

## Race detail

**Job it closes:** Main Job 1 — Discovery.
> Per `../sitemap.md`: "Job: Main Job 1 (jtbd.md: '...so that I can compare them in one place' — viewing one listing's official_url/registration_url/description is how that comparison actually happens)."

> **Build note — race descriptions (2026-09-24) — done:** `race-detail.html` now carries all seven, copied verbatim from `f034acb` and checked against it. Original note kept below.
>
> **Build note — race descriptions (2026-09-24):** the prose `description` for each sample race used to sit on Race browse's cards and was removed from them when the cards were shortened. When `race-detail.html` is built, **take those descriptions from commit `f034acb`** (`git show f034acb:wireframes/race-browse.html`, the seven `<p class="description">` lines). Don't rewrite them from scratch: they're the existing, reviewed sample copy for these exact races. Race detail is also where the full `sport_type` value shows ("DEKA / functional fitness", not the card tag's short "DEKA").

This is where the job's own outcome clause — "so that I can compare them in one place" — actually resolves into a decision (`WantsToEnter` → "Worth entering?").

**Where it sits in the flow** (`../flows.md` → "Main Job 1 — Discovery"): reached from Race browse by "taps a race card or pin," 1 tap deep (`../sitemap.md` → Navigation § 2: "Total: 1 tap"). No independent entry point (`../sitemap.md` → Navigation § 3: contextual, "opened from within Race browse"). From here: `WantsToEnter` → "no" loops back to Race browse; "yes" leads into a registration-link check that ends the flow (`Success` or `DeadEnd6`).

**States:**

| State | Real? | Why |
|---|:---:|---|
| Empty | — | No empty scenario modeled — a race detail is only ever reached for a race that already exists (tapped from a populated Race browse result). `../flows.md` doesn't model this. |
| Error | ✓ | Two distinct causes: `DetailError("Error: could not load race details")` on load, with a `Retry?` diamond — "yes" retries the fetch, "no" gives up (merges into `DeadEnd1`); and `RegLinkError("Error: couldn't open registration link")` after deciding to enter, lighter-weight with no retry diamond (see `../flows.md`'s data-provenance note) — exits by going back to Race detail to try again later, or gives up into the distinct `DeadEnd6`. |
| Loading | ✓ | `DetailLoading("Loading: fetching race details")` on entry. |
| Success | ✓ | `Success(("Success: this race's registration_url opened — Onrace records nothing further"))` — the flow's one distinct "it worked" endpoint, reached via `WantsToEnter` → "yes" → `RegLinkCheck` → "yes." |

---

## Summary table

| Screen | Empty | Error | Loading | Success |
|---|---|---|---|---|
| Race browse | ✓ — no races match current filters after a successful query; exit is to adjust filters (loops back to Browse) or give up (merges into `DeadEnd1`) | ✓ — race-list fetch fails; `Retry?` exits to retrying the fetch or giving up (merges into `DeadEnd1`) | ✓ — fetching races; fires on initial entry and again on every region/date/sport filter change | — |
| Race detail | — | ✓ — either the race-detail fetch fails (`Retry?` exits to retrying or giving up into `DeadEnd1`), or, after deciding to enter, the registration link fails to open (exits to back-to-detail-and-retry-later, or giving up into the distinct `DeadEnd6`) | ✓ — fetching a specific race's details, triggered by tapping a card/pin from Race browse | ✓ — `registration_url` opens successfully after deciding the race is worth entering; exit is out to the external registration site, with nothing further recorded in Onrace |
