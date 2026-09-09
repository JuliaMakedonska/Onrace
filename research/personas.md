# Personas

Built from `research.md` only (2026-09-02 competitor/reference pass — no interviews or surveys conducted, per `research.md` line 3 and its "User research" section, which reads: "_Not started — no interviews or surveys conducted yet._"). This document contains **no primary user research**, so every claim below is either:

- traced to a specific section of `research.md`, or
- marked **[?] HYPOTHESIS** — not sourced, not validated, included only because it's a reasonable inference worth testing.

Nothing here should be read as confirmed user behavior. Treat these as research-informed guesses to validate, not finished personas.

---

## Primary — "The HYROX-First Hybrid Athlete"

**Why primary:** this is the persona with the most, and the most varied, direct support in `research.md` — it's named across the Sport taxonomy findings, the COMPETITORS HARD tier, and the differentiation thesis in Findings → decisions, and it's the persona the product's own seeding priority is built around (`research.md` → Race data availability: "prioritize HYROX ... and DEKA ... first for MVP seeding"). No other persona in this set is corroborated by that many independent parts of the document.

**Context**
- Identifies as a "hybrid athlete" in the training-methodology sense — someone deliberately training strength + endurance together (Alex Viada, *The Hybrid Athlete*, 2013) — not someone who casually cross-trains. *(Sport taxonomy findings)*
- Treats HYROX as their anchor race format, with marathons/OCR/functional-fitness as adjacent interests — this is how the existing app ecosystem (RoxFit, HySim, RoxMatchUp, HYBRD, HybridAF) is structured around this audience. *(Sport taxonomy findings)*
- **[?] HYPOTHESIS** — likely overlaps with the user base of existing HYROX-specific apps (RoxConnect: "beginner→elite," RoxFit: "training-first framing," RoxMatchUp) rather than general fitness/endurance tools. *(COMPETITORS → HARD tier matrix)* — **flagged, not confirmed:** the matrix only describes who these products are *marketed to*; it contains no usage data, so "already lives inside" overstated a stated audience as an observed behavior. Reframed here as a plausible overlap to validate, not a fact about this persona's current app usage.

**Jobs**
- Find upcoming HYROX (and adjacent-format) races to enter. *(Sport taxonomy findings; COMPETITORS HARD tier)*
- **[?] HYPOTHESIS** — track results across HYROX plus other formats they dabble in (marathons, OCR, functional fitness), in one place. Not directly evidenced — inferred from the fact that no competitor reviewed does this combination across formats (`research.md` → Three shared market patterns #3, CONCLUSIONS gap 6), which is stated as a *market gap Onrace could fill*, not as a job this persona has explicitly reported wanting done.

**Pains**
- Existing tools split the job in two: something discovers races *or* something archives results, never both, and every current cross-format combination in this space is single-sport-only (RoxFit and RoxMatchUp both do discovery+archive, but HYROX-only). *(Three shared market patterns #3; CONCLUSIONS gap 6)*
- No single official source covers HYROX + DEKA + marathons + triathlons + ultras together — even the research process itself had to hand-curate from separate calendars (hyrox.com, spartan.com/en/deka, etc.) rather than pull from one place. *(Race data availability)*

**Trust triggers**
- What could convince them: a source-link requirement that mirrors what they already do elsewhere in this niche — RoxFit's results claim to come from RoxFit's "own analyzed-race database" rather than self-report, and RoxConnect/ocrbase carry no verification layer at all, so a product that visibly labels "self-reported + source-linked" would be *more transparent than what they're used to*, not less. *(COMPETITORS HARD tier trust-model row; BENCHMARK → mechanism #2)*
- What could scare them off: **[?] HYPOTHESIS** — with no social/peer layer (Onrace's archive isn't a feed — no following, comments, or public sharing), there's no one in-app who'd notice or vouch for a fabricated result, which the document itself flags as a mechanism that "won't work" here for anyone, not just this persona. *(BENCHMARK → "One mechanism that won't work: peer/social visibility")* — this is presented as a designed-around limitation in the doc, not as a fear this persona has actually expressed.

**Mood quote**
> "Illustrative only — not sourced from any real athlete. No interview or quote data exists in `research.md`."
> *(placeholder, not a finding)* — "I already live in three different HYROX apps just to plan my season and remember what I ran."

---

## Secondary — "The Qualifying-Time Archivist"

**Context**
- Training toward or applying for an elite race that gates entry on a submitted official time — Boston Marathon is the named, sourced example. *(Proof-of-result findings)*
- **[?] HYPOTHESIS** — this persona's results currently live scattered across multiple timing-company sites, forcing them to hunt one down when an application deadline arrives. `research.md` does **not** state this directly (that specific "scattered across timing sites" framing appears in `../CLAUDE.md`, not in `research.md`); the closest thing `research.md` offers is that Boston accepts "an official race result, a digital results platform, or a verified certificate from the timing company" as proof — which implies plural possible sources, but doesn't itself describe an individual athlete's fragmentation problem.

**Jobs**
- Produce, on demand, a link or certificate from an official timing source as proof of a qualifying time for race entry. *(Proof-of-result findings)*

**Pains**
- **[?] HYPOTHESIS** — no confirmed pain point in `research.md` for this persona specifically. The document validates that elite races *require* this kind of proof; it does not report how painful today's process of assembling it actually is for anyone.

**Trust triggers**
- What convinces them: Boston Marathon itself doesn't require a verified/audited result — it accepts a link or certificate as sufficient proof, which directly validates that Onrace's "the link is the evidence" model mirrors real elite-race practice rather than inventing a novel, unfamiliar standard. *(Proof-of-result findings; Findings → decisions: "Trust model validated")*
- What scares them off: **[?] HYPOTHESIS** — a mandatory source-link field, at the moment of logging a result, may cause some submission drop-off, though the document explicitly frames this as an unvalidated hypothesis, not a finding: "friction will be measurable but survivable ... but the net effect is likely fewer results logged per user, not zero adoption." *(CONCLUSIONS gap 1 — explicitly labeled a hypothesis in the source document itself)*
- Note: HYROX World Championships qualification is placement-based, not submitted-time-based — so this persona's specific job (submit a time as proof) does **not** generalize to HYROX; it's a marathon-shaped job, evidenced only for that format. *(Proof-of-result findings)*

**Mood quote**
> Illustrative only, not sourced — "I have my Boston-qualifying time somewhere, I just need to remember which site has the certificate."

---

## Secondary — "The Multi-Region Season Planner"

**Context**
- Someone for whom geography is a primary axis of choosing what to race next — either recreational ("what can I travel to") or competitive (building a multi-region racing calendar). *(PATTERNS section)*
- Caveat on sourcing: this framing in `research.md` itself leans on `../CLAUDE.md`'s stated audience/global-scope assumptions rather than on independent evidence gathered in the research pass — the document says the map is "the documented plan, not a competing option" and cites CLAUDE.md as the reason geography matters, not a user finding. *(PATTERNS, "It's the documented plan, not a competing option")*

**Jobs**
- Browse races spatially to decide where to travel/compete next, rather than searching with a known date/sport already in mind. *(PATTERNS)*

**Pains**
- **[?] HYPOTHESIS** — `research.md` poses, but never answers, "where do athletes currently track races/results today — HYROX's own site, Athlinks, DUV, RaceRoster, Strava, spreadsheets?" as an open question. This implies possible tool-fragmentation pain for this persona, but the document is explicit that this is an unanswered question, not a confirmed pain point. *(Questions to answer, item 1)*

**Trust triggers**
- **[?] HYPOTHESIS** — no trust-related evidence specific to this persona exists in `research.md`. The document's map-vs-filter reasoning is about product-pattern fit (matching ocrbase's and AllTrails' map/filter UI shapes), not about what builds or erodes this persona's trust.

**Mood quote**
> Illustrative only, not sourced — "I want to see everything on a map and figure out which trip is worth planning around."

---

## Honest gaps

- No persona above is built from an actual interview, survey, review-mining pass, or usage log — `research.md` confirms none of these exist yet (line 3, "User research" section).
- Any "pain" or "trust trigger" not tied to a specific named section above should be read as a hypothesis to test, not a fact about real people.
- The document's own proposed next low-cost step — reading App Store reviews for RoxFit/RoxMatchUp/HYBRD/HybridAF — has **not** been done. That pass would be the first source of anything closer to a real, sourced mood quote or pain point. *(User research section; Next steps item 2)*

---

## Design implication: the archiving *sub-jobs* fit a different persona than Discovery does

`jtbd.md`'s JTBD × Persona matrix shows Discovery and the concrete archiving sub-jobs don't map to the same persona — stated precisely, since an earlier draft of this note blurred two different matrix rows together:

- **Discovery (Main Job 1)** maps most strongly to the **Primary** persona (The HYROX-First Hybrid Athlete) — scores a clean, well-sourced 3.
- **Logging a result with proof, and retrieving it for an elite-race application (Related Jobs 3–4)** map most strongly to the **Secondary** persona (The Qualifying-Time Archivist) — these score 3 for the Archivist, but only a caveated 2, a sourced 1, or `[?]` for the Primary persona. (Notably: retrieving proof for an elite-race application scores a sourced **1** for the Primary persona, since HYROX Worlds qualification is explicitly placement-based, not proof-of-time — see Proof-of-result findings in `research.md`.)

**Not the same claim as "Main Job 2 maps to the Archivist."** Main Job 2 (the compound job of wanting discovery + archiving combined in one product) scores **2** for the Primary persona and **`[?]`** (unscored, not lower) for the Archivist — so that row doesn't itself support handing the whole archiving *job* to the Archivist persona. The evidence for the handoff lives specifically in the two concrete sub-jobs (logging, retrieving), not in the combined-product framing. (Also worth weighing: the Archivist's 3s here come from the same `research.md` section — Proof-of-result findings — that this persona was originally built from, so they corroborate the persona's own definition more than they independently confirm it.)

This doesn't change which persona is primary — that's independently justified by the discovery-side evidence in `research.md`, not by these jobs. But it's a design implication worth carrying into wireframes: **the concrete acts of logging and retrieving a result should be designed around the Qualifying-Time Archivist's situation, not the HYROX-First Hybrid Athlete's.** Building those specific screens by asking "what would the primary persona want here" is the wrong lens, per the evidence — they exist to serve the secondary persona's job, and should be shaped by their context (proving a past official time for an elite-race application), not filtered through the primary persona's HYROX-anchored framing. See the matching note in `jtbd.md`.
