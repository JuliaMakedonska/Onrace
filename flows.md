# User flows

Built from `sitemap.md` (Screens + Navigation sections) and `research/jtbd.md`. Every screen node below already exists in `sitemap.md` — no new screen was introduced while drawing these, so nothing needed adding back to the sitemap.

Shape convention, held consistent across all three diagrams:
- `["Screen Name"]` — a screen from `sitemap.md`
- `{"Question?"}` — a decision point
- `("State: ...")` — a loading/empty/error state, not its own screen
- `(("..."))` — a terminal: either a success exit or a dead end

Direction is picked per diagram for legibility, not held fixed at `TD`: Discovery below uses `flowchart LR` because "Race browse" is revisited from six different edges (entry, filter change, two dead-end retries, "back," and the no-branch of the final decision) — top-down forced those into crossing arcs; left-to-right resolves them into a clean horizontal fan with no logic change. Log Result and Retrieve Proof stay `TD` — neither revisits a single node anywhere near that often, so top-down already reads cleanly for them.

## Revision note (detail-level audit)

A pass against a stricter reference pattern found three gaps, now fixed everywhere they applied:

1. **Every genuine error state now offers an explicit retry decision, not just a dead end.** `ValidationError` (Flow 2) previously only looped back to the form with no "gives up" path modeled; `LinkError` (Flow 3) previously dead-ended immediately with no retry attempt, even though a broken link could be a transient failure. Both now branch through an explicit `{"Retry?"}`-style diamond, matching the pattern already used by `FetchError`/`AuthError`/`SubmitError`. Retry/give-up is now modeled as its own diamond decision everywhere, not just as two edges hanging off a rounded state node — this makes "does this error offer a real choice" visually unambiguous.
   - **Not applied to empty states** (`Empty`, `Empty2`): an empty result set isn't a failure to retry, it's a legitimate data state — the honest alternatives are "do something to fix it" (adjust filters / go log a result) or "leave," not "try the same fetch again." Kept as two direct edges, deliberately not a `Retry?` diamond.
2. **Every distinct network-dependent step now has its own loading state**, instead of reusing one generic node or skipping the state entirely: added `DetailLoading` (Flow 1, opening a race), `SigningIn`/`SigningIn2` (Flows 2 and 3, sign-in was previously modeled as instant while form submission wasn't), and `DetailLoading2` (Flow 3, opening a specific logged result). Re-fetching the race list on a filter change still correctly reuses `Loading` — that's the same operation repeating, not a different step being conflated with it.
3. **Dead ends re-examined for genuine distinctness**, not just left as originally drawn:
   - Flow 1's `DeadEnd1` already merged "empty results" and "fetch error" give-ups into one outcome; the new `DetailError`'s give-up path merges into it too, and its label was broadened slightly ("leaves without *deciding on*" rather than "*finding*" a race) so it honestly covers all three causes.
   - Flow 3's new `DetailError2` give-up merges into `DeadEnd4` for the same reason — same downstream outcome ("no proof in hand, deadline at risk"), whatever the internal cause.
   - Kept **separate**, on purpose, after considering the merge: Flow 2's `DeadEnd2` (auth failure) vs. `DeadEnd3` (save failure, now also covering the validation-error give-up) — different root causes with different real fixes (an auth problem vs. a forms/data problem). And Flow 3's `DeadEnd4` (can't reach the archive at all) vs. `DeadEnd5` (reached it, but the evidence itself is dead) — the second is a categorically different, more specific gap (points at the missing edit/re-link feature already flagged in the Navigation section's "Deep: none yet"), not a rewording of the first.

## Revision note (Discovery layout)

The Discovery diagram's top-down layout was visually tangled — arrows crossing around "Race browse," and the three retry/give-up paths converging on one dead-end node from awkward angles. Rendered four candidates (`TD`/`LR` × merged/split dead end) and compared them directly before choosing: switching only the direction to `flowchart LR`, with the dead-end node left exactly as merged, resolved both problems — same nodes, same edges, same single dead-end outcome, just laid out left-to-right instead of top-down. Splitting the dead end into three nodes was rejected even though it also read cleanly, because it would have reversed the merge decision from the audit above for a purely cosmetic reason, duplicating one outcome into three identical-meaning circles.

## Revision note (post-critique fixes, 2026-09-17)

A rigorous critique against this file and `sitemap.md` found further gaps, fixed here:

1. **Flow 3's logged-results fetch (`Loading2`) had no failure branch** — the one network step in the whole document without one. Added `FetchError2`/`Retry?`, mirroring Flow 1's `Loading`/`FetchError` pattern, merging its give-up edge into `DeadEnd4`.
2. **Both auth gates (Flow 2, Flow 3) had no way to back out before attempting sign-in** — the only modeled exits were through a failed attempt. Added a direct "closes without attempting" edge from `SignIn`/`SignIn2` into `DeadEnd2`/`DeadEnd4` respectively.
3. **Flow 2's form validation only checked `official_result_url`**, even though `race_name`, `date`, `sport_type`, and `finish_time` are equally required by `../CLAUDE.md`'s data model. Generalized `HasLink` into `HasRequired` ("All required fields filled in?"), reusing the existing `ValidationError`/`ValidationRetry` pattern rather than adding new nodes.
4. **Flow 1's `registration_url` had no failure handling**, unlike `official_result_url`'s treatment in Flow 3. Added a lightweight, lower-stakes check (`RegLinkCheck` → error → back-edge to Race detail) — deliberately without a `Retry?` diamond, since this is an outbound link to someone else's site, not Onrace's own trust mechanism.
5. **`DeadEnd5`** (source link dead even after retry, Flow 3) **is left as-is by decision** — see the note at that dead end below. Closing it would require an edit/re-link capability not backed by any job in `jtbd.md`; logged as a post-MVP backlog item rather than built speculatively.

## Revision note (fresh-session corrections, 2026-09-17)

A fresh-session review of the prior pass's *reasoning*, not just its diagrams, caught two mischaracterizations:

1. **`registration_url`'s lighter treatment was justified on the wrong grounds.** The prior note framed it as "not Onrace's own trust mechanism" — true, but not the actual reason for lighter handling. The real reason is data provenance: `registration_url` is Onrace's own curated, manually-seeded catalog data (`../CLAUDE.md` → Race data), so it's low rot risk; `official_result_url` is an arbitrary user-submitted link, high rot risk. Reasoning corrected in Flow 1's notes below. Separately, the broken-registration-link give-up path now has its own distinct terminal, `DeadEnd6`, rather than any risk of reading as the same outcome as `DeadEnd1` — this person already decided the race was worth entering; the failure is an external link rotting *after* that decision, not indecision, and merging the two would misrepresent what happened.
2. **Flow 2's required-field check over-generalized.** The prior pass folded `official_result_url` and `race_name`/`date`/`sport_type`/`finish_time` into one "all required fields filled in?" check with one generic error label. That flattened a real distinction: `../CLAUDE.md`'s data model only explicitly marks `official_result_url` as required — the other fields are just listed, not stated as required. Split back into two checks: the original source-link check (unflagged, since it's actually sourced) and a second, explicitly `[?]`-flagged check for the other fields, each with its own specific error label instead of one generic "required fields missing" message.

(A third correction — relocating rather than deleting the "Onrace — entry" screen's underlying rationale — applies to `sitemap.md` only; see that file's Navigation § 1.)

## Revision note (success-endpoint precision, 2026-09-17)

Audited every flow's `Success` endpoint against one question: is it a verifiable condition, or a vague destination like "lands on X screen"? Found two gaps and one asymmetry worth stating outright:

1. **Flow 2 (Log Result) had no `Success` terminal at all** — `SubmitOK`'s "yes" edge just landed on the `ResultsList` screen node, exactly the "lands on X screen" vagueness this check was looking for. Added an explicit `Success2` terminal stating the actual condition: a `results` row now exists for this user with `official_result_url` populated (the one field `../CLAUDE.md` requires), plus the other fields per this flow's `[?]`-flagged check.
2. **Flow 3 (Retrieve Proof)'s `Success3` said "ready to submit to the elite race"** — not verifiable by Onrace, since whether a given application accepts the proof isn't knowable here. Tightened to the condition the flow actually confirms: this specific row's `official_result_url` opened successfully just now.
3. **Flow 1 (Discovery)'s `Success` was already reasonably specific** (names the exact field, `registration_url`), but its prose now says explicitly what it lacks compared to the other two: an Onrace-side data-model record. Opening `registration_url` changes nothing in Onrace's own data — completion happens entirely on an external site, outside Onrace's visibility, unlike the other two endpoints, which are both about a `results` row's confirmed state.

---
## Revision note (Flow 2 entry point, 2026-09-24)

Global navigation went from 3 tabs to 2 (`sitemap.md` → Navigation § 1, revised 2026-09-24): **Log result** is no longer a tab, it's the primary action button inside My Results. Flow 2 now reflects that; everything from the Log result form onward is unchanged.

1. **Entry moved:** `Start2` is now "Global nav: taps My Results," not "taps Log Result." The sign-in gate (`AuthCheck` and everything under it) is unchanged, but it now fires on the My Results tab, and a successful sign-in lands on **Results list**, not directly on the form.
2. **One new step, `ResultsList` → `FindsAction`:** reaching the form now takes a tap on the in-page **Log result** action (header button, or the empty state's call to action). Flagged `[?]`, because it rests on `sitemap.md`'s own unvalidated hypothesis that people will look for logging inside My Results.
3. **One new dead end, `DeadEnd7`** ("reached My Results, never found Log result") `[?]`. Kept separate from `DeadEnd2` (never got signed in) and `DeadEnd3` (forms/data failure) under this document's own rule of merging dead ends only when the root cause and fix are the same. The root cause here is how easy the action is to find, and the fix is prominence/placement in the UI — neither auth nor submission.
4. **Deliberately not added:** the Results list's own fetch (`Loading2` / `FetchError2`) is not copied into Flow 2. That fetch is Flow 3's job. The Log result action is part of the screen's header, not of the loaded list, so it must stay usable while the list is loading or has failed. That's a design constraint on Results list, recorded here so Flow 2 doesn't inherit Flow 3's fetch failure.

---

## Main Job 1 — Discovery (Primary persona — The HYROX-First Hybrid Athlete)

> "See the full range of options — across countries, formats, and dates — instead of checking each source separately... so that I can compare them in one place." (`jtbd.md`)

```mermaid
flowchart LR
    Start(("App opens")) --> Browse["Race browse"]
    Browse --> Loading("Loading: fetching races")
    Loading --> HasResults{"Any races match current filters?"}
    HasResults -->|"no"| Empty("Empty: no races match current filters")
    Empty -->|"adjusts filters"| Browse
    Empty -->|"gives up"| DeadEnd1(("Dead end: leaves without deciding on a race"))
    HasResults -->|"yes"| Browse
    Loading -->|"connection fails"| FetchError("Error: could not load races")
    FetchError --> FetchRetry{"Retry?"}
    FetchRetry -->|"yes"| Loading
    FetchRetry -->|"no"| DeadEnd1
    Browse -->|"changes region/date/sport filters"| Loading
    Browse -->|"taps a race card or pin"| DetailLoading("Loading: fetching race details")
    DetailLoading -->|"loads successfully"| Detail["Race detail"]
    DetailLoading -->|"connection fails"| DetailError("Error: could not load race details")
    DetailError --> DetailRetry{"Retry?"}
    DetailRetry -->|"yes"| DetailLoading
    DetailRetry -->|"no"| DeadEnd1
    Detail -->|"back / compares another race"| Browse
    Detail --> WantsToEnter{"Worth entering?"}
    WantsToEnter -->|"yes"| RegLinkCheck{"Registration link opens?"}
    RegLinkCheck -->|"yes"| Success(("Success: this race's registration_url opened — Onrace records nothing further"))
    RegLinkCheck -->|"no"| RegLinkError("Error: couldn't open registration link")
    RegLinkError -->|"back to race detail, tries again later"| Detail
    RegLinkError -->|"gives up"| DeadEnd6(("Dead end: decided to enter, but the registration link is broken"))
    WantsToEnter -->|"no"| Browse
```

**Decisions:**
- *Any races match current filters?* — branches between showing results and the empty state.
- *Retry?* (after a race-list fetch fails) — genuine choice between trying the same fetch again or giving up.
- *Retry?* (after a race-detail fetch fails) — same choice, one level down, for opening a specific race.
- *Worth entering?* — on Race detail, this is where the job's own "so that I can compare them in one place" actually resolves into a decision.
- *Registration link opens?* (added — Race detail previously assumed opening `registration_url` always succeeds) — checked at lighter weight than the Retrieve Proof flow's equivalent check on `official_result_url`: no retry diamond, just two direct edges (mirroring how `Empty`/`Empty2` are already handled elsewhere in this document — a legitimate outcome gets two edges, not a formal retry loop). The lighter weight is about data provenance, not job/trust-mechanism importance: `registration_url` is Onrace's own curated, manually-seeded catalog data (`../CLAUDE.md` → Race data: "manually curated/seeded, no scraping in MVP"), so Onrace controls when it's entered and it's low rot risk. `official_result_url` is an arbitrary link a user pastes in themselves, with no curation at all — genuinely higher rot risk, which is why it gets the heavier, retry-capable treatment in Flow 3.

**States:**
- Loading: fetching races (the list).
- Loading: fetching race details (a single race — its own step, no longer skipped or folded into the list's loading state).
- Empty: no races match the current filters.
- Error: could not load races (list fetch/connection failure).
- Error: could not load race details (detail fetch/connection failure).
- Error: couldn't open registration link (added — lighter-weight than the source-link failure in the Retrieve Proof flow, per the data-provenance reasoning above; no retry loop — a direct back-edge to Race detail, or a distinct give-up outcome, `DeadEnd6`, kept separate from `DeadEnd1`).

**Endpoints:**
- **Success:** the race's `registration_url` has opened in the browser — that's the entire condition. Per `../CLAUDE.md`, Onrace only ever links out, never handles registration, so no Onrace-side record (no row, no flag, nothing in the data model) is created or changed by this. Unlike the other two flows' success endpoints, this one isn't verifiable from Onrace's own data — the job's completion happens entirely on the registration site, outside Onrace's visibility.
- **Dead ends:** two, kept distinct on purpose.
  - *Leaves without deciding on a race* (`DeadEnd1`) — one merged outcome reachable from three different causes (gives up on an empty result, gives up after a failed list fetch, gives up after a failed detail fetch). All three leave the primary persona in the same place: no race decided on, job unresolved. Kept as a single node rather than three, since the *cause* is already visible from which edge leads in, and the *outcome* genuinely doesn't differ.
  - *Decided to enter, but the registration link is broken* (`DeadEnd6`) — kept separate from `DeadEnd1` on purpose, even though both are give-up outcomes. This person already made the decision the job's own "so that I can compare them in one place" resolves into — the failure here is a broken external link discovered *after* deciding, not indecision or an earlier fetch failure. Folding it into `DeadEnd1` would misrepresent what actually happened.

---

## Related Job 3 — Log a Result with Source Proof (Secondary persona — The Qualifying-Time Archivist)

> "When I finish a race, I want to log the result along with where it came from, so that I have proof ready without having to redo the work later." (`jtbd.md`)

```mermaid
flowchart TD
    Start2(("Global nav: taps My Results")) --> AuthCheck{"Signed in?"}
    AuthCheck -->|"no"| SignIn["Sign in / Sign up"]
    SignIn -->|"submits credentials"| SigningIn("Loading: signing in")
    SignIn -->|"closes without attempting"| DeadEnd2
    SigningIn --> AuthResult{"Sign-in succeeded?"}
    AuthResult -->|"no"| AuthError("Error: sign-in failed")
    AuthError --> AuthRetry{"Retry?"}
    AuthRetry -->|"yes"| SignIn
    AuthRetry -->|"no"| DeadEnd2(("Dead end: leaves without logging the result"))
    AuthResult -->|"yes"| ResultsList["Results list (my archive)"]
    AuthCheck -->|"yes"| ResultsList
    ResultsList --> FindsAction{"Finds and taps Log result? (header button, or empty state's call to action) [?]"}
    FindsAction -->|"yes"| LogForm["Log result"]
    FindsAction -->|"no"| DeadEnd7(("Dead end: reached My Results, never found Log result [?]"))
    LogForm --> HasLink{"official_result_url filled in?"}
    HasLink -->|"no"| ValidationError("Error: source link is required")
    ValidationError --> ValidationRetry{"Fix and resubmit?"}
    ValidationRetry -->|"yes"| LogForm
    ValidationRetry -->|"no"| DeadEnd3(("Dead end: no result saved, proof lost for later"))
    HasLink -->|"yes"| HasOtherRequired{"race_name/date/sport_type/finish_time all filled in? [?]"}
    HasOtherRequired -->|"no"| OtherFieldError("Error: required field missing (race_name / date / sport_type / finish_time) [?]")
    OtherFieldError --> OtherFieldRetry{"Fix and resubmit?"}
    OtherFieldRetry -->|"yes"| LogForm
    OtherFieldRetry -->|"no"| DeadEnd3
    HasOtherRequired -->|"yes"| Submitting("Loading: saving result")
    Submitting --> SubmitOK{"Submission succeeded?"}
    SubmitOK -->|"no — link unreachable"| SubmitError("Error: link unreachable, submission failed")
    SubmitError --> SubmitRetry{"Retry?"}
    SubmitRetry -->|"yes"| LogForm
    SubmitRetry -->|"no"| DeadEnd3
    SubmitOK -->|"yes"| Success2(("Success: results row saved for this user — official_result_url populated (required)"))
```

**Decisions:**
- *Signed in?* — Logged results are owner-only per `../CLAUDE.md`'s RLS model, so the My Results tab gates into Sign in / Sign up if not signed in, per the Navigation section's contextual-gate design. Since 2026-09-24 this gate sits on the My Results tab rather than on a Log Result tab; Log result lives inside My Results, so one gate covers both archive jobs.
- *Finds and taps Log result?* `[?]` — added 2026-09-24 with the 2-tab nav. The form is now one in-page action away from Results list (header button, or the empty state's call to action), not a tab. Flagged: that people look for logging inside My Results is `sitemap.md` → Navigation § 1's unvalidated hypothesis. The action must not depend on the list having loaded (see the 2026-09-24 revision note).
- *Sign-in succeeded?*
- *Retry?* (after a failed sign-in) — previously just an edge label; now an explicit diamond, same as every other error in this flow.
- *official_result_url filled in?* — enforces the required-source-link trust model (`../CLAUDE.md` → Result trust model) before the form can be submitted at all. This is the one field `../CLAUDE.md`'s data model explicitly marks "(required)."
- *race_name/date/sport_type/finish_time all filled in?* `[?]` — added as a second, separate check, deliberately flagged. Unlike `official_result_url`, `../CLAUDE.md`'s data model doesn't actually say these fields are required — it just lists them (`race_name/date/sport_type ..., finish_time, official_result_url (required)`). Modeled here as an assumed requirement (a result with no finish time or date is hard to imagine as useful) and flagged `[?]`, per this document set's own convention for assumed-not-sourced parts (see `sitemap.md`'s Entities section), not presented as settled fact. Previously this had no modeled validation at all — a blank `finish_time` would have silently surfaced as "link unreachable" via `SubmitError`, which was never accurate.
- *Fix and resubmit?* (after the source-link validation fails) — previously this error only looped back to the form with no give-up path at all; now it's a real choice, same as the other errors in this flow.
- *Fix and resubmit?* (after the other-required-fields validation fails) `[?]` — same retry-or-give-up choice, one level down; inherits the same `[?]` status as the check above it.
- *Submission succeeded?*
- *Retry?* (after a failed submission)

**States:**
- Loading: signing in (previously missing — sign-in was drawn as instant even though form submission, an equivalent network call, already had its own loading state).
- Error: sign-in failed.
- Error: source link is required (client-side validation, before submission).
- Error: required field missing (race_name / date / sport_type / finish_time) `[?]` (client-side validation, before submission — flagged, since these aren't explicitly marked required in `../CLAUDE.md`'s data model the way `official_result_url` is).
- Loading: saving result.
- Error: link unreachable / submission failed.

**Endpoints:**
- **Success:** tightened from "lands in Results list" (a screen, not a condition) to the actual verifiable state: a new row now exists in `results`, owned by this user via RLS, with `official_result_url` populated — the one field `../CLAUDE.md`'s data model explicitly requires — and, per this flow's `[?]`-flagged validation, `race_name`, `date`, `sport_type`, and `finish_time` populated too (though that requirement is only assumed here, not confirmed at the schema level — see the `[?]` on `HasOtherRequired` above). That row is what now appears on Results list ("my archive") and is what the next flow below retrieves.
- **Dead ends:** three, kept distinct on purpose.
  - *Leaves without logging the result* — reachable from a failed sign-in (after exhausting retries) or from closing the Sign in / Sign up screen without attempting at all (added — previously the only modeled exit from that screen was through a failed attempt). Root cause: never got signed in.
  - *No result saved, proof lost for later* — reachable from the source-link validation failing, the other-required-fields validation failing `[?]`, or the save itself failing. Root cause: a forms/data problem, once already past sign-in. These two were considered for merging into one "nothing happened" dead end but kept apart because they point at different real fixes (fix auth vs. fix the submission path), unlike the validation/submission pair inside the second node, which really is the same failure surfaced at two different moments.
  - *Reached My Results, never found Log result* `[?]` (added 2026-09-24) — signed in fine, on the right screen, but never took the in-page action. Root cause: the action wasn't findable enough. Real fix: its placement/prominence on Results list. That's a different fix from both dead ends above, so it isn't merged into either. Flagged because whether this happens at all is untested.

---

## Related Job 4 — Retrieve Proof for an Elite-Race Application (Secondary persona — The Qualifying-Time Archivist)

> "When an elite race asks me to prove a past result, I want to pull that proof up quickly, so that I can apply without scrambling to find it." (`jtbd.md`)

```mermaid
flowchart TD
    Start3(("Global nav: taps My Results")) --> AuthCheck2{"Signed in?"}
    AuthCheck2 -->|"no"| SignIn2["Sign in / Sign up"]
    SignIn2 -->|"submits credentials"| SigningIn2("Loading: signing in")
    SignIn2 -->|"closes without attempting"| DeadEnd4
    SigningIn2 --> AuthResult2{"Sign-in succeeded?"}
    AuthResult2 -->|"no"| AuthError2("Error: sign-in failed")
    AuthError2 --> AuthRetry2{"Retry?"}
    AuthRetry2 -->|"yes"| SignIn2
    AuthRetry2 -->|"no"| DeadEnd4(("Dead end: leaves without proof, application deadline at risk"))
    AuthResult2 -->|"yes"| ResultsList2["Results list (my archive)"]
    AuthCheck2 -->|"yes"| ResultsList2
    ResultsList2 --> Loading2("Loading: fetching logged results")
    Loading2 --> HasLogged{"Any results logged yet?"}
    HasLogged -->|"no"| Empty2("Empty: no results logged yet")
    Empty2 -->|"goes to log one instead"| LogForm2["Log result"]
    Empty2 -->|"gives up"| DeadEnd4
    HasLogged -->|"yes"| ResultsList2
    Loading2 -->|"connection fails"| FetchError2("Error: could not load logged results")
    FetchError2 --> FetchRetry2{"Retry?"}
    FetchRetry2 -->|"yes"| Loading2
    FetchRetry2 -->|"no"| DeadEnd4
    ResultsList2 -->|"taps a logged entry"| DetailLoading2("Loading: fetching result details")
    DetailLoading2 -->|"loads successfully"| ResultDetail["Result detail (proof view)"]
    DetailLoading2 -->|"connection fails"| DetailError2("Error: could not load result details")
    DetailError2 --> DetailRetry2{"Retry?"}
    DetailRetry2 -->|"yes"| DetailLoading2
    DetailRetry2 -->|"no"| DeadEnd4
    ResultDetail --> LinkWorks{"Source link still opens?"}
    LinkWorks -->|"yes"| Success3(("Success: this results row's official_result_url opened successfully, just now"))
    LinkWorks -->|"no"| LinkError("Error: source link unreachable")
    LinkError --> LinkRetry{"Try again?"}
    LinkRetry -->|"yes"| ResultDetail
    LinkRetry -->|"no"| DeadEnd5(("Dead end: proof inaccessible, nothing in-app to correct it"))
```

**Decisions:**
- *Signed in?* — same owner-only gate as the Log Result flow.
- *Sign-in succeeded?*
- *Retry?* (after a failed sign-in)
- *Retry?* (after a failed fetch of the logged-results list — added; this was the one network fetch in the whole document that previously had no paired failure branch, unlike every other fetch here).
- *Any results logged yet?* — branches between the archive and an empty state.
- *Retry?* (after a failed fetch of a specific result's details — previously this step wasn't modeled at all; opening a result was drawn as instant).
- *Source link still opens?* — the moment the "the link is the evidence" trust model (`../CLAUDE.md` → Result trust model) actually gets tested by an outside party.
- *Try again?* (after the source link fails to open) — previously this dead-ended immediately with no retry attempt, even though the failure could be transient (a flaky timing-site server, not necessarily a truly dead link).

**States:**
- Loading: signing in (previously missing, same gap as Flow 2).
- Error: sign-in failed.
- Loading: fetching logged results.
- Error: could not load logged results (added — previously this fetch had no failure branch at all, unlike every other fetch in this document).
- Empty: no results logged yet.
- Loading: fetching result details (previously missing — a specific result's detail fetch was collapsed into an instant transition).
- Error: could not load result details.
- Error: source link unreachable.

**Endpoints:**
- **Success:** tightened from "ready to submit to the elite race" — not something Onrace can actually verify, since whether a specific application accepts the proof isn't knowable from here — to the condition the flow itself confirms: the selected `results` row's `official_result_url`, the required proof link per `../CLAUDE.md`'s Result trust model, opened successfully in this session. What happens after that — whether the race accepts it — is outside Onrace's scope by design: Onrace's job ends at confirming the link is live, since the product's trust model is "self-reported, source-linked," not "Onrace verifies" (`research.md` → CONCLUSIONS gap 4).
- **Dead ends:** two, kept distinct on purpose.
  - *Leaves without proof, application deadline at risk* — one merged outcome reachable from five causes: a failed sign-in, closing the Sign in / Sign up screen without attempting at all (added), an empty archive (nothing was ever logged), a failed fetch of the logged-results list (added), or a failed fetch of a specific result's details. All five share the same downstream reality — no proof in hand, right when it's needed — so they're one node, not five.
  - *Proof inaccessible, nothing in-app to correct it* — kept separate from the node above on purpose. This one is reached only after everything else worked (signed in, archive has entries, the specific result loaded fine) and the source link itself turns out to be dead even after a retry. That's a materially different, more specific problem — the evidence itself has rotted — pointing at a real, currently-missing product gap (an edit/re-link flow for a logged result), which ties directly to the Navigation section's honest "Deep: none yet" note.
    - **Decision (2026-09-17): left as a known, accepted MVP gap.** Closing it (an edit/re-link capability for a logged result) would be new scope not backed by any job in `jtbd.md` — no job asks to *correct* a logged result, only to log one (Related Job 3) and retrieve one (Related Job 4). Tracked here as a post-MVP backlog item rather than built speculatively; revisit if a "fix a stale result" job is ever sourced.
