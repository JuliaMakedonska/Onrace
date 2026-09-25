# Sitemap

Draft. Built bottom-up from `research/jtbd.md`, `research/personas.md`, and `research/research.md` — entities before screens, per the working method: no screen or navigation should be proposed until the objects a person actually deals with are named and traced to a job.

## Entities

Entities 1–4 below are included because a specific job in `jtbd.md` produces or requires it. Entity 5 is the one exception, tagged **infrastructure**: no job requires it, but the existence of accounts does (see its reversal note). Entities with neither behind them are listed separately under **Under question**, not mixed in here. `[?]` marks a part of an entity that's assumed rather than sourced.

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

### 5. Athlete account — `[INFRASTRUCTURE]`, not job-sourced

The account a person signs into, and the minimal facts that say whose it is. Private to its owner, like Logged result. Never shown to anyone else (`../CLAUDE.md` → no social features).

**Fields/parts:**
- sign-in identity (email): already provided by Supabase Auth, not a new field
- name
- country
- language `[?]`: stored as a preference only. `../CLAUDE.md` plans no localization, so the field changes nothing in the UI yet. Don't design it as if it switches the app's language.
- *(photo: deferred, not excluded.)* Showing a photo means uploading and storing images, which needs Supabase Storage, and that isn't in the decided stack. For MVP the account shows the name's **initials** instead. Revisit once Storage is decided on.

**Deliberately not included:** bio, stats or results summaries, badges, customization, public visibility. There's no job for any of them, and most are the "profile page" conventions that `../CLAUDE.md` rules out (social features). `jtbd.md` Hypothesis 6 ("see my own range reflected back") stays unbuilt. This entity doesn't serve it.

**Why it exists (no job behind it):** accounts exist because Logged result is owner-only (`../CLAUDE.md` → RLS). A product with accounts has to show who is signed in and offer a way to sign out. Without that, a shared or borrowed device stays signed into someone else's archive, with no way to tell or to leave.

**Reversal (2026-09-25):** this entity used to sit under *Under question* as "Athlete account / identity `[?]`", concluding that "no job explicitly asks for a profile object with its own fields". Commit `03ed66f` (2026-09-24) reached the same verdict for a Profile screen (`jtbd.md` Hypothesis 6: "isn't [justified], by any job"). Both answered the question they asked correctly, but it was the wrong question for this kind of object. "Does a job need this?" is the test for product features. The test for infrastructure is the one that already justified Sign in / Sign up: **does the existence of auth require this to exist somewhere?** For account identity and sign-out, yes. The earlier verdict still holds for the *feature* version of a profile (stats, range, social surface). That stays out.

**Connects to:**
- **Logged result**: owns every result in one person's archive (row-level ownership)
- Sign in / Sign up and Profile (screens) read and write it

---

## Under question

Not included above because no job in `jtbd.md` produces or requires them directly — listed here so they aren't silently dropped, not because they're necessarily wrong.

- **Automated plausibility check / flag `[?]`** — proposed in `research.md` → BENCHMARK top-3 mechanism #3 and CONCLUSIONS gap 4 (dead-link detection, implausible-time flags, duplicate detection) as a trust-building mechanism. Not traced to any specific JTBD job — it's the researcher's proposed system behavior, not something a person's job produces or asks for. Would attach to Logged result / Source-link proof if built.
- **Saved season plan / itinerary `[?]`** — the Multi-Region Season Planner persona's job ("browse races spatially to decide where to travel/compete next") describes *browsing* behavior only; no job or data-model field in `../CLAUDE.md` describes saving, bookmarking, or persisting a shortlist. Flagged so it isn't assumed later without a job behind it.
- **Results map (a map of countries/locations where the user has competed) `[?]`** — a feature idea raised in this session, not sourced to any job in `jtbd.md`. Related Jobs 3–4 (logging a result with proof; retrieving proof for an application) are about producing and retrieving evidence, not about visualizing geographic spread of past results, and no other job describes wanting a spatial view of one's own history. Compelling on its own terms and worth validating later — plausibly a natural extension of the Qualifying-Time Archivist's job (a byproduct view of results already logged with location data), or a new hypothesis to add to `jtbd.md` if pursued — but currently not a confirmed requirement. Do not treat as an entity or design a screen for it until it's traced to a job the way the four entities above are.

---

## Screens

Grouped by the two entity clusters from the Entities section above (Discovery = Race listing + Search/filter criteria; Archive = Logged result + Source-link proof), not by generic "site sections." Every screen is tagged with the `jtbd.md` job it serves; `[INFRASTRUCTURE]` marks a screen with no job behind it that exists because accounts do (renamed from `[ORPHAN]` on 2026-09-25: "orphan" read as "unjustified," but these screens are justified, by auth rather than by a job). Loading/empty/error states are noted inline as *states*, not listed as their own screens. An earlier draft modeled a distinct "Onrace — entry" screen to carry Main Job 2; that screen never actually existed as separate UI (Race browse is the real 0-tap landing screen, per Navigation → Depth below) and has been removed. Its rationale wasn't wrong, just misplaced — see Navigation § 1 for where it actually lives now (corrected 2026-09-17).

```
Onrace (app — not a separate screen or job-closing destination; Race browse is the
│        actual landing screen at 0 taps, see Navigation → Depth below. Main Job 2's
│        "one product" framing is closed at the nav level, not here — see
│        Navigation § 1, "Why Main Job 2 lives here, not on a screen.")
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
    │     (jtbd.md); + Main Job 2 (caveated, see Screens section intro note above).
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
    │     States (not separate screens): empty form · source-link-required
    │     validation error (official_result_url — the one field `../CLAUDE.md`'s
    │     data model explicitly marks required) · other-required-field
    │     validation error (race_name/date/sport_type/finish_time `[?]` —
    │     assumed required, not explicitly marked so in the data model; see
    │     flows.md, Flow "Related Job 3") · submit error (e.g. unreachable
    │     source link).
    │
    └── Result detail (proof view)
          Job: Related Job 4 — "pull that proof up quickly" (jtbd.md).
          Persona: Secondary — Archivist ONLY. jtbd.md scores this job a
          sourced **1** for the Primary persona — an actual disconfirmation,
          not just an absence of evidence — because HYROX Worlds qualification
          is placement-based, not proof-of-time. Do not design this screen
          around the Primary persona's framing (see personas.md/jtbd.md's own
          design-implication note).

Sign in / Sign up  [INFRASTRUCTURE]
  No job in jtbd.md calls for account creation or login. Exists because
  "Logged result" is owner-only per ../CLAUDE.md's data model, which means
  accounts exist (Entities → 5. Athlete account). Needed for both personas
  technically (to make ownership work), but not sourced to any stated job.

Profile  [INFRASTRUCTURE]  (added 2026-09-25)
  Shows whose account this is and lets the person leave it. Not job-sourced;
  exists because auth does (Entities → 5, incl. its reversal note).
  Contents, deliberately narrow: initials (photo deferred) · name · country
  · language [?] (stored preference, no localization yet) · Sign out.
  Nothing else: no bio, stats, customization, or public view.
  Entry: account button in the My Results navigation bar (Navigation § 1).
  Only reachable signed in, since My Results already gates on sign-in.
```

**Jobs with no screen of their own:** the Emotional job ("recognized as what I actually am — a hybrid athlete") and the Social job ("the proof itself to stand on its own") don't produce distinct screens — per `jtbd.md`, they describe how existing screens should read (tone/framing on Discovery; the self-reported-source-linked display convention on Result detail), not separate destinations. Not listed as screens or orphans for that reason.

**Not included:** a profile *feature* (stats, range reflected back, public page). `jtbd.md` Hypothesis 6 stays unbuilt, and Profile above is account infrastructure only. Also not included: a screen for the Results map idea flagged under Entities → Under question — it stays unbuilt until it's traced to a job.

---

## Navigation

Built only from the screens already named in the Screens section above. No new screen is introduced here, only how the existing ones are entered and reached. (Profile, added 2026-09-25, was added to the Screens section first. Its placement is decided below.)

### 1. Global navigation — 2 items (revised 2026-09-24)

**Current structure:** a 2-tab bottom bar — **Discover** → Race browse, **My Results** → Results list. **Log result** is no longer a tab; it's the primary action button inside My Results (in the Results list header, and as the empty state's call to action).

| Item → screen | Job behind it | Persona |
|---|---|---|
| **Discover** → Race browse | Main Job 1 — Discovery (`jtbd.md`) | Primary (core) + Secondary — Season Planner |
| **My Results** → Results list | Related Job 4 — "pull that proof up quickly" (`jtbd.md`); also home of Related Job 3's entry point, via the in-page **Log result** action | Secondary — Archivist (core); Primary weak/caveated only |

**Why 2 tabs + an in-page action (the reasoning that replaced the 3-item version below):** the problem with the 3-item bar was a *destination/action mismatch*, not tap count. A tab bar is for switching between places; actions go in the screen's own toolbar or buttons (Apple HIG's tab bar guidance: tabs are for navigation, not for starting tasks). Discover and My Results are places — you go there to look at a set of things. "Log Result" was an action (start a form that creates one new Logged result) sitting between two places as if it were one. And that action writes to the exact collection My Results shows, so its natural home is inside that place, next to the list it adds to — not a separate location of its own.

The trigger-difference argument below is still true — Related Jobs 3 and 4 *are* triggered at different moments (right after a race vs. later, on demand). But a difference in *when* a job happens doesn't make it a different *place*: both jobs act on the same object (Logged result) in the same archive. Different triggers justify two clear entry points, not two tabs — and the in-page primary action is that second entry point.

**The cost, stated honestly** (see § 2 for the numbers): Related Job 3 goes from 1 tap to 2. That was the reason commit `03ed66f` kept 3 tabs: Related Job 3 is the one job sourced as urgency-triggered ("right after finishing a race," `jtbd.md`). Accepted, not dismissed: the "urgency" is hours-to-days after a race, not seconds, and the extra tap is small next to the form itself (race, date, sport type, finish time, plus finding and pasting `official_result_url`). **[?] HYPOTHESIS:** that people expect to find "log a result" inside My Results, and that logging is rare enough (a few times a season) that it doesn't need a permanent slot. Neither is backed by user research — check both in the first usability test of the My Results flow.

**Main Job 2 is served better by this, not worse:** with only two tabs, Discover and My Results are now the *entire* global nav — the "one product, two co-equal halves" framing below is now literally what the bar shows.

#### Superseded — original 3-item reasoning (kept for the record, no longer the structure)

*Superseded 2026-09-24 by the 2-item structure above. Kept here, not deleted, because commit `03ed66f` explicitly re-affirmed it earlier the same day; the reversal should be traceable, not silent. Its reasoning about triggers is still correct — what changed is the conclusion drawn from it (see "Why 2 tabs + an in-page action" above).*

`jtbd.md`'s own framing ("Why two main jobs, not one main + related") justifies co-equal top-level status by *trigger*, not by feature symmetry: Discovery is triggered by planning ahead, Archiving by "the opposite moment — after competing." That same trigger-difference logic, applied one level down, also separates the two Archive-cluster sub-jobs from each other — Related Job 3 (log right after finishing a race) and Related Job 4 (retrieve proof later, on demand) are triggered at different moments too. That's the basis for 3 global items, not 2 or 4 *(superseded — see above)*:

| Item → screen | Job behind it | Persona |
|---|---|---|
| **Discover** → Race browse | Main Job 1 — Discovery: "see the full range of options... instead of checking each source separately" (`jtbd.md`) | Primary (core) + Secondary — Season Planner |
| **Log Result** → Log result | Related Job 3 — "log the result along with where it came from... proof ready without having to redo the work later," triggered right after finishing a race (`jtbd.md`) | Secondary — Archivist (core); Primary only weak/general (matrix: "2, weak/general") |
| **My Results** → Results list | Related Job 4 — "pull that proof up quickly" when an elite race asks for it, triggered later, on demand (`jtbd.md`) | Secondary — Archivist (core); Primary weak/caveated only (Main Job 2 = 2) |

**Why Main Job 2 lives here, not on a screen (relocated 2026-09-17):** an earlier draft of this document modeled a distinct "Onrace — entry" screen to carry Main Job 2 (jtbd.md: "I want that in one product, so that I'm not maintaining two separate habits or tools"), reasoning that "the entry point is where 'one product' is actually experienced." That screen didn't hold up — Race browse is the actual 0-tap landing screen (see Depth, below), not a separate entry point — so it was removed from the Screens tree and the Traceability matrix. But the reasoning itself was sound, just aimed at the wrong artifact: it's *this nav structure* — Discover and My Results sitting as co-equal, always-visible items in one global nav (originally two of three; since 2026-09-24, the only two), rather than two separate apps or tabs a person has to consciously switch mental models between — that's where "one product" is actually experienced. That's what the Traceability matrix's Main Job 2 checkmarks on Race browse and Results list are really pointing at.

**Deliberately excluded from global nav:** Sign in/Sign up. It's an `[INFRASTRUCTURE]` screen (tagged `[ORPHAN]` until 2026-09-25) — no job in `jtbd.md` calls for it — and Discovery (the strongest, cleanest-sourced job in the whole matrix) doesn't require an account at all. Giving it a permanent global slot would spend one of a handful of nav items (2, as of 2026-09-24) on a screen with no job behind it, and would put an auth wall in front of users whose only goal is Discovery. It surfaces contextually instead (see below).

**Profile: not a tab either (decided 2026-09-25).** Profile is reached from an **account button (initials) in the My Results navigation bar**, beside the Log result action, not from a third tab. Same discipline as the Log result decision, applied test by test:
1. **Destination or action?** A destination: you go there to see your account. So unlike Log result, it passes the "tabs are places" test. That's necessary for a tab, not sufficient.
2. **How often?** Tabs are for places people return to every session. Profile is visited rarely: to check whose account this is, change a preference, or sign out. Log result was already judged too infrequent for a tab, and Profile is less frequent still.
3. **Job-sourcing.** Same test that kept Sign in / Sign up out of the bar: a permanent slot shouldn't go to a screen with no job behind it. A third tab would bring back the 3-item bar removed on 2026-09-24, with the new slot going to the one item that closes no job.
4. **Signed-out state.** As a tab, it would need either a second sign-in gate or a designed signed-out Profile. Inside My Results it sits behind the gate that's already there, so no new gate. Discover still needs no account.
5. **Ownership.** The account matters because it owns the archive, so its entry point sits in the archive's own header. This follows the iOS convention of an account button in the large-title bar when the tab bar is reserved for main destinations (e.g. the App Store).

**Rejected alternative:** the same account button on Discover's header too (1 tap from launch). It would put an auth entry point on the one screen designed to need no account. **The cost of the chosen placement:** someone who uses only Discover and wants to change a preference has to go through My Results. **[?] HYPOTHESIS:** that people look for their account inside My Results. Not backed by user research; check it in the same first usability test as Log result's placement.

### 2. Depth to the primary persona's core job

**Target:** Main Job 1 — Discovery, for the Primary persona (The HYROX-First Hybrid Athlete) — reaching a race worth entering.

- **App launch → Race browse: 0 taps.** Discover is set as the default/home tab, not just a nav item — justified because `jtbd.md`'s own conclusion names Main Job 1 as the one job in the whole matrix with "no caveats needed... satisfies both halves of the filter without qualification" (clean primary-persona importance + the strongest market gap). The one clean job gets the one screen that costs nothing to reach.
- **Race browse → Race detail: 1 tap.** Tapping a race card/pin is where the job's own "so that I can compare them in one place" (`jtbd.md`) actually resolves into a specific decision (view official_url/registration_url and decide to enter).

**Total: 1 tap** to go from opening the app to viewing a specific race worth entering — under the 3-tap ceiling, so no restructuring is needed. The tradeoff of defaulting to Discover: the Archive screens are never zero-tap — the Archivist persona always spends at least 1 tap to reach their core screens, and an unauthenticated user meets the Sign in/Sign up gate on the way (see below). That's an intentional bias toward the persona and job with the cleanest evidence (`jtbd.md`'s Tier 1 pick), at a small, bounded cost to the two jobs justified on weaker, Tier-2 grounds. Main Job 1's path is unchanged by the 2-tab revision.

**Related Job 3 (log a result) — tap depth before vs. after the 2-tab revision (2026-09-24):**

| Path to the Log result form | 3 tabs (before) | 2 tabs + in-page action (now) | Change |
|---|---|---|---|
| From app launch, signed in | 1 — tap **Log Result** tab | 2 — tap **My Results** tab → tap **Log result** button | **+1 tap** (1 → 2) |
| From app launch, signed out | 1 tap + sign-in gate → form | 1 tap + sign-in gate → Results list → 1 tap → form (2 taps + gate) | **+1 tap**; the gate count is the same (one gate either way) |
| Already on My Results | 1 — tap **Log Result** tab | 1 — tap **Log result** button | no change |
| First-time user, empty archive | 1 — tap **Log Result** tab | 2 — tap **My Results** → empty state's **Log your first result** | **+1 tap**, and lands on an empty state that explains what the archive is for, before asking for input |

So the real cost is exactly **one extra tap from anywhere outside My Results** — 2 taps total, still under the 3-tap ceiling. No path gets worse by more than that, and none gains a second gate. The sign-in gate now fires one step earlier (on the My Results tab, not on the Log action), which also means a signed-out person sees *why* they're signing in (their archive) before they're asked to. Related Job 4 (retrieve proof) is unchanged: 1 tap to My Results, then 1 tap into a Result detail.

**Profile and Sign out: tap depth (added 2026-09-25):**

| Path | Taps | Notes |
|---|---|---|
| App launch → Profile, signed in | 2: **My Results** tab → account button | under the 3-tap ceiling |
| App launch → Profile, signed out | 1 tap + sign-in gate → Results list → 1 tap (2 taps + gate) | the same single gate as the archive; no new one |
| App launch → Sign out | 3: … → Profile → **Sign out** | at the ceiling, acceptable for the rarest action in the app |
| Already on My Results → Profile | 1 | |

### 3. Global / contextual / deep

- **Global (always visible — the 2-item nav bar, since 2026-09-24):**
  - Discover (Race browse)
  - My Results (Results list)
  - *(Formerly also Log Result — now an in-page action, below. See § 1.)*

- **In-page primary action (a button on a screen, not a nav item):**
  - **Log result** — the primary button in the Results list header, and the call to action in its empty state. Opens the Log result screen.

- **Contextual (appears in-flow, reached by drilling into something, not from the nav bar):**
  - **Race detail** — opened from within Race browse (tap a card/pin); no independent entry point.
  - **Log result** — opened from within My Results via the Log result action above; no longer a global destination of its own.
  - **Result detail (proof view)** — opened from within My Results (tap a logged entry); Secondary–Archivist only, per Step 2's persona note.
  - **Profile**: opened from the account button in the My Results navigation bar; no independent entry point. Signed-in only (see § 1).
  - **Sign in / Sign up** — surfaces only when an unauthenticated person taps My Results (owner-only per `../CLAUDE.md`'s RLS model — and since Log result now lives inside My Results, that one tap gates both archive jobs); never interrupts Discover, since that job needs no account. This is a gate triggered by an action, not a destination someone navigates to on its own — hence contextual, not global. *(Before 2026-09-24 it was reachable from two of the three nav items, Log Result and My Results.)*

- **Deep (rare, buried actions):**
  - **Sign out**: a button on Profile, 3 taps from launch. The first real entry here (2026-09-25). This bucket used to say signing out wasn't in the screen list, and that absence is exactly the gap Profile closes (Entities → 5).
  - Editing or deleting a logged result, and any further account settings, still aren't in the screen list, so they're still not invented here.

---

*Depth kept minimal deliberately — additional levels (e.g. within Log result, within Race detail) are Step 3, not this pass.*

---

## Traceability

Rows = every job in `jtbd.md` (main, related, emotional, and social — the five unsourced items under `jtbd.md` → Hypotheses are excluded, since they're explicitly "not backed by `research.md`," a different category from what's asked here). Columns = every screen in the Screens section above. A ✓ means the screen actually participates in *closing* that job, not merely that it's adjacent to the topic.

| Job (`jtbd.md`) | Race browse | Race detail | Results list | Log result | Result detail | Sign in / Sign up | Profile |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Main Job 1 — Discovery | ✓ | ✓ | | | | | |
| Main Job 2 — Results archiving (combined) | ✓ | | ✓ | | | | |
| Related Job 1 — plan season by format | ✓ | | | | | | |
| Related Job 2 — choose races by location | ✓ | | | | | | |
| Related Job 3 — log a result with proof | | | ✓ | ✓ | | | |
| Related Job 4 — retrieve proof for an application | | | ✓ | | ✓ | | |
| Emotional — recognized as a hybrid athlete | ✓ | | | | | | |
| Social — proof stands on its own | | | ✓ | ✓ | ✓ | | |

**Notes on the two `✓` rows that aren't a dedicated interaction:** Emotional and Social don't have a screen built specifically for them — per the Screens section's own "Jobs with no screen of their own" note, they're closed by *how* an existing screen reads, not by a separate destination. Emotional is closed by Race browse's cross-format framing (seeing HYROX/DEKA/marathons/etc. together as one "hybrid athlete" catalog, not siloed by sport). Social is closed by the required-link-at-entry and self-reported-labeling conventions (`research.md` → BENCHMARK mechanisms #1–2) actually being implemented on Log result, Results list, and Result detail. These are legitimate closes, not padding — but they're framing-level, not task-level, unlike every other ✓ in the matrix.

**Correction (2026-09-17):** an earlier draft of this matrix included an `Onrace (entry)` column, treating app launch as its own screen that closed Main Job 2. That contradicted the Navigation section's own claim that Race browse is the 0-tap landing screen — there is no separate entry screen to close a job. The column has been removed (see also the Screens section's opening note and the corrected tree above); Main Job 2's coverage is unaffected, since Race browse and Results list were already checked independently of it. The removed screen's rationale — why Main Job 2 matters at the IA level at all — wasn't discarded, just relocated to Navigation § 1.

### Orphan screens (column with no ✓)

*"Orphan" here still means what it means in a traceability matrix: a column with no ✓. The screens that have one are tagged `[INFRASTRUCTURE]` in the Screens section (renamed from `[ORPHAN]`, 2026-09-25), because an empty column isn't a defect for a screen that exists to support auth.*

**Sign in / Sign up**: zero checks. Tagged `[INFRASTRUCTURE]` in the Screens section: no job in `jtbd.md` calls for account creation or login on its own.

**Resolution: attach to existing, not delete or add.** This screen isn't dead weight — it's required because Logged result is owner-only per `../CLAUDE.md`'s RLS model — but it shouldn't be scored as if it closes a job of its own, and it shouldn't be promoted to a first-class, job-justified destination either. The Navigation section already made the correct call here without naming it as such: Sign in / Sign up is classified as **contextual**, a gate triggered only when an unauthenticated person attempts Log Result (Related Job 3) or My Results (Related Job 4), never a standalone stop. That's the resolution — it's attached to those two jobs' flows as an enabling step, not counted as closing them itself. No change needed beyond stating this explicitly here.

**Profile**: zero checks, and the same resolution. It exists because accounts do (Entities → 5), and it's attached to the archive as that account's home and its only sign-out point. It isn't scored as closing a job. It's contextual in My Results, not a global item (Navigation § 1). Its reversal of the 2026-09-24 "no job supports Profile" verdict is documented at Entities → 5, not here, because it changes *why* the screen exists, not what it closes.

### Orphan jobs (row with no ✓)

**None.** Every job in `jtbd.md` traces to at least one screen once the Emotional and Social jobs' framing-level closes (above) are counted honestly rather than left unmapped. This isn't a forced result — the two jobs that could easily have gone unmapped (Emotional, Social) were only checked because the Screens section and the Entities section's Source-link proof mechanisms had *already* documented exactly where each one lives; nothing was invented here to avoid an empty row.

**Goal met: no empty row or column, without inventing a screen or stretching a job's meaning to force a match.**
