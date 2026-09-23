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
| Error | ✓ | `Loading` → "connection fails" → `FetchError("Error: could not load races")`, with a `Retry?` diamond. |
| Loading | ✓ | `Loading("Loading: fetching races")` — fires on entry and again on every filter change. |
| Success | — | No distinct "it worked" endpoint on this screen. Reaching `HasResults` → "yes" just re-displays `Browse` — normal browsing, not a terminal. The flow's actual `Success` node is scoped to Race detail (opening `registration_url`), not to browsing itself. |

---

## Race detail

**Job it closes:** Main Job 1 — Discovery.
> Per `../sitemap.md`: "Job: Main Job 1 (jtbd.md: '...so that I can compare them in one place' — viewing one listing's official_url/registration_url/description is how that comparison actually happens)."

This is where the job's own outcome clause — "so that I can compare them in one place" — actually resolves into a decision (`WantsToEnter` → "Worth entering?").

**Where it sits in the flow** (`../flows.md` → "Main Job 1 — Discovery"): reached from Race browse by "taps a race card or pin," 1 tap deep (`../sitemap.md` → Navigation § 2: "Total: 1 tap"). No independent entry point (`../sitemap.md` → Navigation § 3: contextual, "opened from within Race browse"). From here: `WantsToEnter` → "no" loops back to Race browse; "yes" leads into a registration-link check that ends the flow (`Success` or `DeadEnd6`).

**States:**

| State | Real? | Why |
|---|:---:|---|
| Empty | — | No empty scenario modeled — a race detail is only ever reached for a race that already exists (tapped from a populated Race browse result). `../flows.md` doesn't model this. |
| Error | ✓ | Two distinct error states: `DetailError("Error: could not load race details")` (with a `Retry?` diamond) on load, and `RegLinkError("Error: couldn't open registration link")` (lighter-weight, no retry diamond — see `../flows.md`'s data-provenance note) after deciding to enter. |
| Loading | ✓ | `DetailLoading("Loading: fetching race details")` on entry. |
| Success | ✓ | `Success(("Success: this race's registration_url opened — Onrace records nothing further"))` — the flow's one distinct "it worked" endpoint, reached via `WantsToEnter` → "yes" → `RegLinkCheck` → "yes." |

---

## Summary table

| Screen | Empty | Error | Loading | Success |
|---|:---:|:---:|:---:|:---:|
| Race browse | ✓ | ✓ | ✓ | — |
| Race detail | — | ✓ | ✓ | ✓ |
