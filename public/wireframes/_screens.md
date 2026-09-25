# Screens — state scoping for every screen in `../sitemap.md`

*Pass 1 (below): the Discovery main flow. Pass 2 (after the Discovery summary table): the archive cluster and the infrastructure screens.*

## Pass 1 — Main flow (Main Job 1, Discovery, Primary persona)

Scope: only the screens that close **Main Job 1 — Discovery** for the Primary persona (The HYROX-First Hybrid Athlete) and sit on her main path to a race worth entering. Built from `../sitemap.md` (Screens, Navigation, Traceability sections) and `../flows.md` (the "Main Job 1 — Discovery" flow only).

Everything else was deliberately left out of this first pass. It's scoped further down, in **Pass 2 (2026-09-25)**: the archive cluster (Results list, Log result, Result detail) and the two `[INFRASTRUCTURE]` screens (Sign in / Sign up, Profile). Sign in / Sign up never appears on the Discovery path itself. Discovery "doesn't require an account at all" (`../sitemap.md` → Navigation § 1).

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


---

## Pass 2 — Archive cluster + infrastructure (2026-09-25)

Scope: every `../sitemap.md` screen Pass 1 left out. The states come from `../flows.md` → "Related Job 3 — Log a Result" and "Related Job 4 — Retrieve Proof", the only flows that draw these screens. Race picker (Flow 2's catalog branch), Sign up's email confirmation (Flow 4) and Profile (Flow 5) were added later on 2026-09-25, once those flows were drawn. File naming follows `_conventions.md` § 4: the base page, plus one file per ✓ state other than Success.

### Shared sample archive

Every archive screen uses the same four logged results, newest first, so Results list rows, Result detail pages and `?result=<slug>` links all agree. They're one Qualifying-Time Archivist's season. Berlin 3:12:48 is the Boston-qualifier-style proof that Related Job 4 is about. The races are real, with plausible past dates.

| slug | race_name | date | sport_type | finish_time | official_result_url (domain shown in the proof label) |
|---|---|---|---|---|---|
| `deka-strong-chicago-2026` | DEKA STRONG Chicago | 14 Mar 2026 | DEKA / functional fitness | 24:36 | `https://www.athlinks.com/event/deka-strong-chicago-2026/results` (athlinks.com) |
| `hyrox-london-2025` | HYROX London | 6 Dec 2025 | HYROX | 1:18:42 | `https://results.hyrox.com/season-8/london` (results.hyrox.com) |
| `valencia-half-2025` | Valencia Half Marathon | 26 Oct 2025 | Half marathon | 1:28:05 | `https://www.valenciaciudaddelrunning.com/en/half/results-2025/` (valenciaciudaddelrunning.com) |
| `berlin-marathon-2025` | Berlin Marathon | 21 Sep 2025 | Marathon | 3:12:48 | `https://berlin.r.mikatiming.com/2025/` (berlin.r.mikatiming.com) |

Every result shows its proof label as **"Self-reported · via <domain>"**, never "verified" or a checkmark (`../sitemap.md` → Entities → 4. Source-link proof).

---

## Results list ("my archive")

**Job it closes:** Related Job 4, retrieve proof ("pull that proof up quickly"). Also the entry point for Related Job 3 via its in-page **Log result** action. Main Job 2 is caveated (`../sitemap.md` → Screens).

**Where it sits in the flow:** the My Results tab, gated by "Signed in?", then `Loading: fetching logged results` → "Any results logged yet?". Tapping an entry goes to Result detail through its loading state. The **Log result** action (header, plus the empty state's call to action) opens Log result, and must work while the list is loading or has failed (`../flows.md`, Related Job 3 decisions).

**Chrome:** a top-level screen. It has the 3-tab bar with **My Results** current, and an iOS large title "My Results" with **Log result** in the header.

| State | Real? | Why |
|---|:---:|---|
| Empty | ✓ | `HasLogged` → "no" → `Empty: no results logged yet`. Exits: "goes to log one instead" (→ Log result, the empty state's call to action), or gives up (`DeadEnd4`, just leaving by a tab). |
| Error | ✓ | `Loading2` → "connection fails" → `FetchError2`, with `Retry?`: "yes" re-runs the fetch, "no" is `DeadEnd4`. |
| Loading | ✓ | `Loading2: fetching logged results`, on entry. |
| Success | — | No distinct endpoint. A populated list is normal browsing of the archive. |

Files: `results-list.html`, `-empty`, `-error`, `-loading`.

---

## Log result

**Job it closes:** Related Job 3, log a result with source proof.

**Where it sits in the flow:** opened from Results list's **Log result** action. The form's checks run in order: `official_result_url filled in?`, then `race_name/date/sport_type/finish_time all filled in?` `[?]`, then `Loading: saving result`, then `Submission succeeded?`. Success means a `results` row is saved, and the person lands back on Results list.

**Chrome:** a drill-down form, with no tab bar. The top bar has a back button on the left, the title **Log result** centred, and **Save** on the right (`_conventions.md` § 1, Forms). Revised 2026-09-25: the large title below the bar was dropped to save height at 390px. With a title in the bar, the back label is the parent's title, "‹ My Results", as iOS does, because "Back to My Results" won't fit beside a centred title (`_conventions.md` § 1, Back navigation).

**Catalog link (added 2026-09-25, `../flows.md` Flow 2 catalog branch):** above the race facts is a **Find in race catalog** row that opens Race picker. After a race is picked, the form shows it as a linked card: name, date and sport type, read-only, with "From the Onrace catalog" and an **Unlink** button. Race name, date and sport type are then no longer typed. Unlink turns them back into editable fields, pre-filled with the race's values. Only finish time and the official result link are always typed. The link travels as `catalog=<slug>` (a slug from the picker's sample catalog below), alongside the other values, through the error, loading and picker pages.

| State | Real? | Why |
|---|:---:|---|
| Empty | — | The blank form *is* the base page (`log-result.html`), the default view you arrive at. There's no empty-data state: nothing is fetched. |
| Error | ✓ | Three causes on one page (`_conventions.md` § 5): `?cause=link`, "source link is required" (the one field `../CLAUDE.md` marks required); `?cause=fields`, "required field missing" `[?]`; `?cause=submit`, "couldn't save the result" (was "link unreachable" until 2026-09-25; a client-side app can't check a timing site). Each has "fix and resubmit" (stay on the form) or giving up (`DeadEnd3`, back). |
| Loading | ✓ | `Submitting: saving result`. The form is visible but locked, and Save shows progress. |
| Success | — | The success is a data condition (the row exists), not a screen. The flow lands on Results list, which says what was saved. No `-success.html` (§ 5). |

Files: `log-result.html`, `-error`, `-loading`.

---

## Race picker (added 2026-09-25)

**Job it closes:** Related Job 3, log a result with source proof. It's a shortcut inside it: linking the result to a catalog race means race name, date and sport type are right and don't need typing. It reads the Discovery cluster's entity (Race listing) from inside the archive, read-only.

**Where it sits in the flow** (`../flows.md` → Flow 2, catalog branch): Log result → **Find in race catalog** → `Loading: fetching past catalog races` → Race picker. Selecting a race returns to Log result with it linked. Cancel returns to the form unchanged. An empty result or a failed load offers "type it in instead" (back to the form), because the catalog is optional.

**Chrome:** a modal sheet over Log result, not a drill-down. Choosing is a sub-task of the form, the iOS pattern for pickers. The top bar has **Cancel** on the left and the title "Find a race" centred, with no Save: selecting a row *is* the action. There's a search field under the bar. There's no tab bar.

**What it lists:** only *past* catalog races (`event_date` before today), newest first. You log a race you've run. The catalog keeps past editions for this reason (`../sitemap.md` → Entities → 1). Search matches name or city, runs on submit (the keyboard's Search key), and goes through the loading page like Race browse's filter changes. Each row shows name, date, a short sport tag and city/country. Tapping a row is the selection.

**Sample catalog (past editions):**

| slug | name | event_date | sport_type | city, country |
|---|---|---|---|---|
| `utmb-2026` | UTMB — Ultra-Trail du Mont-Blanc | 28 Aug 2026 | Ultra | Chamonix, France |
| `boston-marathon-2026` | Boston Marathon | 20 Apr 2026 | Marathon | Boston, USA |
| `deka-strong-chicago-2026` | DEKA STRONG Chicago | 14 Mar 2026 | DEKA / functional fitness | Chicago, USA |
| `hyrox-dallas-2026` | HYROX Dallas | 17 Jan 2026 | HYROX | Dallas, USA |
| `hyrox-london-2025` | HYROX London | 6 Dec 2025 | HYROX | London, UK |
| `valencia-half-2025` | Valencia Half Marathon | 26 Oct 2025 | Half marathon | Valencia, Spain |
| `berlin-marathon-2025` | Berlin Marathon | 21 Sep 2025 | Marathon | Berlin, Germany |
| `spartan-beast-killington-2025` | Spartan Race Beast — Killington | 13 Sep 2025 | OCR | Killington, USA |

The four archive results' slugs match their editions here, so a result logged from the catalog is the same race the archive already shows.

| State | Real? | Why |
|---|:---:|---|
| Empty | ✓ | `PickerMatches` → "no" → `Empty: no catalog race matches`. Exits: change the search, or "type it in instead" (back to the form, values kept). |
| Error | ✓ | `Error: could not load the race catalog`, with `Retry?`: yes reloads; no means "type it in instead". |
| Loading | ✓ | `Loading: fetching past catalog races`, on opening and on each search. |
| Success | — | Selecting a race returns to Log result. That's not an endpoint of the picker. |

Files: `race-picker.html` (`?q=` filters the list), `-empty`, `-error`, `-loading`.

---

## Result detail (proof view)

**Job it closes:** Related Job 4, "pull that proof up quickly". Secondary persona (Archivist) **only**: `jtbd.md` scores the Primary persona a sourced 1 here, so don't frame it around HYROX placement.

**Where it sits in the flow:** Results list, "taps a logged entry" → `DetailLoading2` → Result detail → "Source link still opens?". Success is that row's `official_result_url` opening.

**Chrome:** a drill-down screen, with no tab bar. Its top bar is "‹ Back to My Results". A sticky bottom action bar holds the one primary action, opening the official result, with the domain named in the label.

| State | Real? | Why |
|---|:---:|---|
| Empty | — | Only ever reached for a result that exists (tapped from the list). |
| Error | ✓ | Two causes on one page: by default `DetailError2`, "could not load result details" (`Retry?`: yes reloads, no is `DeadEnd4`); with `?cause=link`, `LinkError`, "couldn't open the source link" (reworded 2026-09-25: Onrace only knows the tab didn't open, not why) (`Try again?`: yes goes back to the detail, no is `DeadEnd5`). Same shape as Race detail's DetailError / RegLinkError. |
| Loading | ✓ | `DetailLoading2: fetching result details`. |
| Success | ✓ | `Success3`: the row's `official_result_url` opened, just now. This is the base page (§ 5). |

Files: `result-detail.html` (`?result=<slug>`, one of the four above), `-error`, `-loading`.

---

## Sign in / Sign up — `[INFRASTRUCTURE]`

**Job it closes:** none. It exists because accounts do (`../sitemap.md` → Entities → 5). It's the gate on the My Results and Profile tabs.

**Where it sits in the flow:** "Signed in?" → "no" → Sign in / Sign up. Then "submits credentials" → `Loading: signing in` → "Sign-in succeeded?". Yes lands on where the person was heading (`?next=`: Results list, or Profile). No goes to `Error: sign-in failed` → `Retry?`. "Closes without attempting" leads to `DeadEnd2`/`DeadEnd4`.

**Chrome:** a full-screen modal. **Close** is on the left of the top bar, with no tab bar and no Back (`_conventions.md` § 1, Gates). One screen toggles between **Sign in** and **Create account**. Fields: email and password. **Decided 2026-09-25:** email + password through Supabase Auth, with Confirm email on (`../sitemap.md` → Entities → 5). Create account doesn't sign anyone in: it leads to **Check inbox** (`../flows.md` → Flow 4).

| State | Real? | Why |
|---|:---:|---|
| Empty | — | The blank form is the base page. Nothing is fetched. |
| Error | ✓ | Three causes on one page: by default `AuthError`, "sign-in failed"; `?cause=signup`, "couldn't create the account" (Flow 4 `SignUpError`); `?cause=confirm`, "confirmation link expired or already used" (Flow 4 `ConfirmError`), whose exit is resending. Each has retry, or Close as giving up. |
| Loading | ✓ | `SigningIn` / `CreatingAccount`, the same page in either mode (`?mode=signup`). |
| Check inbox | ✓ | Flow 4 `CheckInbox`, added 2026-09-25. After Create account, or after signing in with an unconfirmed email (`?reason=unconfirmed`). It names the address, says what to do, and offers **Resend email** (with its own brief "Sending…" and a "Sent" line) and **Use a different email** (back to the form). A flow step waiting on the inbox, not one of the four standard states (`_conventions.md` § 4). Opening the email's link returns to the app signed in. The wireframe models that with `?confirmed=1` (a reviewer's switch standing in for the emailed link), which sets the session and lands on `next`. `&expired=1` with it takes the expired-link error instead. |
| Success | — | Lands on the `next` screen. That's not an endpoint of its own. |

Files: `sign-in-sign-up.html`, `-error`, `-loading`, `-check-inbox`.

---

## Profile — `[INFRASTRUCTURE]`

**Job it closes:** none (`../sitemap.md` → Entities → 5, and its reversal note). It shows whose account this is and lets the person leave it.

**Where it sits in the flow** (`../flows.md` → Flow 5, added 2026-09-25): the Profile tab → "Signed in?" → `Loading: fetching profile` → Profile. The tab goes to `profile-loading.html?run=1`, the same pattern as My Results. Signed out, the tab opens Sign in / Sign up with that as `next`.

**Chrome:** a top-level screen. It has the 3-tab bar with **Profile** current and an iOS large title "Profile". The page background is iOS grouped gray. It shows initials (photo deferred), then a grouped list of fields: **Name**, **Country**, **Language** `[?]` (a stored preference, with no localization, so the UI must not imply it translates anything), and the email from sign-in, read-only. **Sign out** sits in its own group at the end. Fields save as they change (iOS Settings convention), so there's no Save button.

**Sign out (Flow 5):** tapping **Sign out** opens an iOS confirm alert over Profile: title "Sign out of Onrace?", one line saying the results stay saved and signing back in brings them back, then **Cancel** and **Sign out**. It's real `<dialog>` markup in `profile.html`, opened by the button (a disclosure, `_conventions.md` § 1), not a separate page. Confirming clears the session and lands on Race browse. There's no loading or error on sign-out itself: it's a local sign-out and can't fail (`../flows.md` Flow 5 note).

| State | Real? | Why |
|---|:---:|---|
| Empty | — | A signed-in account always has itself to show. |
| Error | ✓ | Two causes on one page: by default `ProfileError`, "could not load your profile" (`Retry?`: yes reloads, no is leaving by a tab); `?cause=save`, `SaveError` — the profile loaded, and one field's change didn't save (inline on that row, the field back at its previous value, with "Try again"). |
| Loading | ✓ | `ProfileLoading: fetching profile`. Initials, rows and Sign out are gray placeholders; the tab bar works. |
| Success | — | Sign-out's outcome is landing on Race browse, not a Profile state. |

Files: `profile.html`, `-error`, `-loading`.

---

## Pass 2 summary

| Screen | Empty | Error | Loading | Success | Files |
|---|:---:|:---:|:---:|:---:|---|
| Results list | ✓ | ✓ | ✓ | — | 4 |
| Race picker | ✓ (no match) | ✓ | ✓ | — (returns to the form) | 4 |
| Log result | — (blank form = base) | ✓ ×3 causes | ✓ | — (lands on Results list) | 3 |
| Result detail | — | ✓ ×2 causes | ✓ | ✓ (base) | 3 |
| Sign in / Sign up | — (blank form = base) | ✓ ×3 causes | ✓ | — (lands on `next`); + Check inbox | 4 |
| Profile | — | ✓ ×2 causes | ✓ | — | 3 |
