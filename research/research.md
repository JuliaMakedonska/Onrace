# Research

Living notes for Onrace's discovery phase. Updated 2026-09-02 with a first competitor/reference pass (desktop web research, no user interviews yet — see gaps below).

## Questions to answer

- Who are the actual early users (recreational vs. competitive hybrid athletes), and where do they currently track races/results today?
- What does the current landscape look like — HYROX's own site, Athlinks, DUV, RaceRoster, Strava, spreadsheets?
- What sport taxonomy do athletes actually use when they think of "hybrid races"? Confirms/refines the scope in `../CLAUDE.md`.
- What proof do elite races (Boston Marathon, HYROX Elite, etc.) actually require when athletes apply with a qualifying time? Format, fields, source requirements.
- What race data is realistically available to seed the initial catalog (dates, locations, official links)?

## COMPETITORS

Comparison matrix and market-pattern findings for the 5 competitors selected for closer review (2026-09-02): **ocrbase.com**, **RoxConnect**, **Strava** (Events tab), **Athlinks**, **AllTrails** — spanning the three competitive tiers from the original audit (HARD: same product/audience · SOFT: same task, different audience · ASPIRATIONAL: international benchmark).

### Comparison matrix

| Axis | ocrbase.com | RoxConnect | Strava (Events tab) | Athlinks | AllTrails |
|---|---|---|---|---|---|
| **Audience** | OCR/functional-fitness/trail/rucking racers broadly — hybrid-adjacent, not hybrid-branded | HYROX-specific hybrid athletes, beginner→elite, claims "+80 countries" (confirmed on-page stat) | Strava's existing broad run/cycling base, now shown races via the Events tab | Competitive endurance athletes broadly (running/tri/swim/cycling/adventure racing) | Outdoor enthusiasts (hiking/camping/trail running), broad skill range |
| **Product foundation** | Free web calendar, footer-credited "Made by Rebase Labs" | Native mobile app (iOS/Android) — App Store/Google Play badges shown on homepage | Mature social fitness platform (web+app); races live under Groups → Events | Web results database; footer links to "Life Time" and "ChronoTrack" | Web + mobile app; map-first trail directory |
| **Key mechanism** | Browse/filter races by format/date/country, map or list view | Create profile → filter/match with training partners → in-app chat | Search + faceted filters (Sport/Dates/Distance/Location/Elevation/Terrain) + a "Popular Races For You" personalized rail | Search/claim your name or bib in race results → build a personal race history | Search by location/filters → trail detail → record/save an activity |
| **Trust model** | None visible — listings read as self/community-submitted, no verification UI observed | Minimal — self-reported profile data, no verification UI observed | Race listings sourced from Runna, not self-reported by athletes; activity data is the athlete's own GPS-tracked activity | Results reportedly auto-matched from official timing feeds — **mechanism specifics data not confirmed** (no source link retained for this claim) | Community reviews + crowdsourced trail data; no personal-result verification concept observed |
| **Monetization** | No pricing/paid-tier UI observed anywhere on the site | Freemium: Free vs. ~$11.99/mo Premium (confirmed on-page pricing table) | Free Events tab observed; a paid tier reportedly gates training-analysis features — **price point data not confirmed** this pass | Free to athletes; B2B link to ChronoTrack observed in footer (monetization structure inferred from that link, not confirmed in detail) | Freemium positioning stated publicly — **specific gated features/price data not confirmed** this pass |
| **Sources** | [ocrbase.com](https://www.ocrbase.com/) · `screens/ocrbase.md` · `screens/ocrbase-home.png` | [roxconnect.com](https://roxconnect.com) · `screens/roxconnect.md` · `screens/roxconnect-home.png` | `screens/strava-events.md` (logged-in screenshots) · `screens/strava-home.png` (logged-out state) | [athlinks.com](https://www.athlinks.com/) · `screens/athlinks.md` · `screens/athlinks-home.png` | [alltrails.com](https://www.alltrails.com) · `screens/alltrails.md` · `screens/alltrails-explore-map.png` |

**Sourcing note:** every row above is backed by a live screenshot or the product's own public page (linked in the Sources row). Three specific claims carried over from an earlier WebSearch/WebFetch pass — Strava's Events tab being tied to a Runna acquisition, Strava's and AllTrails' exact paid-tier feature lists/prices, and Athlinks' timing-feed auto-match mechanism — no longer have a retained citation link, so they're marked **data not confirmed** above rather than re-asserted as fact.

### Three shared market patterns

1. **Freemium (or an adjacent B2B subsidy) is the default business model.** Confirmed for RoxConnect (on-page: Free / $11.99/mo) and inferred for Athlinks (footer link to ChronoTrack, its B2B timing arm). Strava's and AllTrails' paid-tier specifics are data not confirmed this pass, but both publicly present a free tier plus a paid subscription. Nobody charges for the core "find/log a race" job itself.
2. **Nobody uses a self-reported, required-source-link trust model.** Athlinks reportedly auto-matches from timing feeds (mechanism data not confirmed with a retained link); Strava's own activity data is GPS-tracked; ocrbase and RoxConnect listings/profiles carry no verification layer at all (confirmed — no claim flow or verification badge observed in either product's screenshots). Onrace's "the link is the evidence" approach is genuinely novel among this set.
3. **Discovery and archiving are always separate products, never natively unified.** RoxConnect discovers *partners* (confirmed — no race-browsing UI found in `screens/roxconnect.md`); ocrbase discovers *races only* (confirmed — no personal-archive feature observed); Athlinks archives *results only* (confirmed — search-first homepage, no map/browse UI, `screens/athlinks.md`); Strava's Events sits inside an existing activity-tracking product (confirmed, `screens/strava-events.md`). No competitor launched both halves as one coherent product.

### Three differences

1. **Scale and maturity vary enormously.** Athlinks (Life Time Fitness-linked per its footer) and Strava (an established platform, `screens/strava-home.png`) versus ocrbase's and RoxConnect's small-team footprint (ocrbase's "Made by Rebase Labs" footer credit is confirmed; exact company size for either is data not confirmed). Onrace starts at the small end of this spectrum.
2. **"Race discovery" is solved via at least four different product shapes.** Pure calendar browsing (ocrbase, confirmed screenshot), partner-matching wrapped around events (RoxConnect, confirmed screenshot), filters + a personalized rail bolted onto a social app (Strava, confirmed `screens/strava-events.md`), and a claimed-results database with no discovery layer at all (Athlinks, confirmed screenshot). None matches Onrace's planned map-first, cross-format approach exactly.
3. **Revenue structure differs by category.** Direct consumer subscription (RoxConnect confirmed; Strava/AllTrails publicly positioned as freemium but specifics data not confirmed) vs. B2B-subsidizes-free-consumer-product (Athlinks, ChronoTrack footer link) vs. no visible monetization (ocrbase, confirmed — no pricing UI anywhere on the site). CLAUDE.md's "no monetization plan" puts Onrace in the same bucket as the least-resourced competitor here.

## BENCHMARK

**Question:** which lightweight mechanisms should Onrace's MVP borrow to make self-reported result *ownership* credible, given there's no manual verification team? Benchmarked against 5 products that handle self-reported/unverified ownership claims well in their own niche, scored 1–5 on 8 criteria (identity persistence, falsification cost, independent cross-reference, peer/social visibility, automatable plausibility checks, stakes-appropriate rigor, dispute/correction mechanism, source-artifact requirement).

| Criterion | Goodreads | Letterboxd | Strava (manual entry) | LinkedIn certifications | Chess.com FIDE field |
|---|---|---|---|---|---|
| Identity persistence | 3 | 3 | 4 | 5 | 3 |
| Falsification cost | 1 | 1 | 2 | 2 | 1 |
| Independent cross-reference | 1 | 1 | 1 | 3 | 5 |
| Peer/social visibility | 2 | 3 | 4 | 4 | 3 |
| Automatable plausibility checks | 1 | 1 | 3 | 2 | 1 |
| Stakes-appropriate rigor | 5 | 5 | 5 | 2 | 4 |
| Dispute/correction mechanism | 2 | 2 | 3 | 2 | 2 |
| Source-artifact requirement | 1 | 1 | 1 | 3 | 2 |
| **Total (/40)** | **16** | **17** | **23** | **23** | **21** |

Sources: [Goodreads Reading Challenge](https://www.goodreads.com/group/show/58421-2026-reading-challenge) · [Letterboxd diary feature](https://letterboxd.zendesk.com/hc/en-us/articles/15178773269263) · [Letterboxd FAQ](https://letterboxd.com/about/faq/) · [Strava Help: Virtual Trainer Activities](https://support.strava.com/en-us/articles/15401857-virtual-trainer-activities-on-strava) · [Strava Help: Segment Leaderboard Guidelines](https://support.strava.com/en-us/articles/15401921-segment-leaderboard-guidelines) · [How to add certifications on LinkedIn](https://socialrails.com/blog/how-to-add-certifications-to-linkedin) · [Chess.com forum: FIDE ratings verification](https://www.chess.com/forum/view/general/are-fide-ratings-on-the-profiles-verified-by-chess-com)

### Top 3 mechanisms for Onrace's MVP

1. **Make the source link mandatory, not optional, at submission.** LinkedIn scores well on identity persistence (5/5) but only 3/5 on source-artifact requirement, because its Credential URL field is *optional* — most users skip a step that isn't required ([source](https://socialrails.com/blog/how-to-add-certifications-to-linkedin)). Onrace's brief already plans a required link (`../CLAUDE.md` → Result trust model); this is direct evidence not to soften that in implementation.
2. **Structurally label every result as self-reported + source-linked, never as "verified."** Strava wins the table (23/40) largely via **structural segregation**, not verification — manual entries are excluded from leaderboards by rule, not judged case-by-case ([source](https://support.strava.com/en-us/articles/15401857-virtual-trainer-activities-on-strava)). A UI convention — always show "via [domain of official_result_url]," never a checkmark implying Onrace vouches for it — borrows the same mechanism at zero admin cost.
3. **Add automatable plausibility checks at submission time.** This is the one criterion every product in the table scored weakly on (1–3 out of 5, see table above) — a cheap opportunity to do better than all five references simultaneously: reject a dead/unreachable link, flag implausible finish times for a given sport/distance, flag exact duplicate race+time combinations submitted by different accounts.

### One mechanism that won't work: peer/social visibility

Letterboxd (3/5 on this criterion) and Strava (4/5) both lean on a critical mass of peers who know the claimant's real skill level to organically catch false claims — Strava's kudos/comments culture and Letterboxd's active review community. Onrace's results archive is explicitly *not* a social feed (`../CLAUDE.md`: no following, comments, or public sharing of results in MVP). With no followers and a thin launch user base, there's no audience positioned to notice or contest a fabricated result — "let the crowd police it" isn't viable here, so mechanisms 1–3 above have to substitute for the social layer this pattern actually depends on.

## PATTERNS

**Chosen pattern: map-first spatial exploration**, with faceted filtering (region, date, sport type) layered on top as its companion, not a separate feature.

This isn't a speculative pick — it's already decided in `../CLAUDE.md`: MVP feature 1 reads "Interactive map of races — filterable by region, date, and sport type," and the Tech stack section has already locked in Leaflet + OpenStreetMap as the map layer. Three reasons it fits:

1. **It's the documented plan, not a competing option.** `../CLAUDE.md` names the map explicitly as MVP feature 1, and the Leaflet + OSM tech-stack decision is already made, not open.
2. **The audience is geography-driven by design.** `../CLAUDE.md` commits to global scope from day one; both recreational athletes ("what can I travel to") and competitive athletes (multi-region racing calendars) make geography a primary decision axis — matching how ocrbase's map (`screens/ocrbase-events-map.png`) and AllTrails' `/explore` (`screens/alltrails-explore-map.png`) both center location-based browsing for a comparable "choose one of many options" task.
3. **The scale-breakdown risk doesn't apply yet.** A map without clustering gets cluttered at high pin density, but MVP data is hand-seeded via SQL (`../CLAUDE.md`: no admin/CMS, races added directly via SQL) — realistically tens to low hundreds of races, well inside the range where ocrbase's and AllTrails' maps (both confirmed via screenshot) stay legible without clustering logic.

Against the alternatives: faceted filter + browse alone is the closest runner-up — `../CLAUDE.md`'s own feature line already licenses it as the map's companion (list toggle or synced panel, matching both ocrbase's and AllTrails' pattern, confirmed via screenshot) for an athlete who already knows their date/sport constraints rather than browsing by location. A personalized recommendation feed doesn't fit: it needs behavioral history Onrace won't have at a cold-start launch, and no ranking pipeline is budgeted in the Supabase-only stack (`../CLAUDE.md` → Tech stack).

## CONCLUSIONS

For each open gap surfaced by the analysis above, a hypothesis and the section it follows from. None of these are validated with real user/usage data yet.

1. **Gap:** no competitor in the COMPETITORS matrix requires a mandatory source link the way Onrace will — will this cause submission drop-off? **Hypothesis:** friction will be measurable but survivable, because the target audience already produces official result links for other purposes (e.g. Boston Marathon qualifying-time proof — see "Proof-of-result findings" below); the extra step is small relative to a motivation that already exists, but the net effect is likely fewer results logged per user, not zero adoption. **Follows from:** COMPETITORS.
2. **Gap:** every HYROX-specific competitor found monetizes via consumer subscription (RoxConnect confirmed; RoxFit/RoxMatchUp asserted in the original audit), while Onrace's brief states no monetization plan. **Hypothesis:** "no monetization" is workable through MVP validation but not indefinitely — if Onrace needs revenue later, the two structures every funded competitor in this category actually uses (consumer subscription like RoxConnect, or B2B/organizer-subsidy like Athlinks×ChronoTrack) are the realistic options, not a novel third model. **Follows from:** COMPETITORS.
3. **Gap:** whether Strava's Events tab will expand beyond running/cycling into HYROX/DEKA territory, turning a SOFT competitor into a HARD one. **Hypothesis:** low probability inside Onrace's 2026-11-01 MVP window — every race sampled in `screens/strava-events.md` (2026-09-02, logged-in screenshots) was running-only (10K/Half/Marathon), and expansion would need a new data partnership, not just a UI change. Data not confirmed beyond this one screenshot pass — worth a periodic recheck, not a blocking risk. **Follows from:** COMPETITORS.
4. **Gap:** are automatable plausibility checks (dead-link detection, implausible-time flags, duplicate detection) a sufficient substitute for the peer-visibility mechanism ruled out for MVP? **Hypothesis:** sufficient to catch crude fabrications (impossible times, dead links, exact duplicates) but not a real-but-mismatched link (someone else's genuine result, wrong owner) — an acceptable residual risk given Onrace's trust model is explicitly "the link is the evidence," not "Onrace verifies" (`../CLAUDE.md` → Result trust model), so this is a known, deliberate limit, not a hidden gap. **Follows from:** BENCHMARK.
5. **Gap:** the MVP map-UI implementation choice (List/Map toggle vs. AllTrails-style split-pane) isn't decided, and no clustering plan exists for when the seed catalog outgrows "tens to low hundreds" of races. **Hypothesis:** toggle-first (ocrbase's pattern, `screens/ocrbase-events-map.png`) is the right MVP choice given the 2-month timeline and small seed catalog, with split-pane and clustering deferred to a v2 once real usage — not assumption — shows whether users hit that friction. Data not confirmed against Onrace's actual eventual catalog size. **Follows from:** PATTERNS.

## User research

_Not started — no interviews or surveys conducted yet._ Given the app ecosystem found above (RoxFit, RoxMatchUp, HybridAF, HYBRD), a cheap next step would be reading their App Store reviews for recurring complaints (a form of low-cost qualitative research) before committing to primary interviews.

## Sport taxonomy findings

- "Hybrid athlete" is a training-methodology term (formally systematized by Alex Viada, *The Hybrid Athlete*, 2013): someone deliberately training strength + endurance together, not casually cross-training. This matches the brief's framing — confirms "hybrid athlete" describes the **audience**, not a race format, exactly as `../CLAUDE.md` already states.
- The existing app ecosystem (RoxFit, HySim, RoxMatchUp, HYBRD, HybridAF) treats **HYROX as the anchor format** for this audience, with marathons/OCR/functional-fitness as adjacent interests — supports keeping HYROX as the flagship format in seed data even though scope is broader.
- ocrbase's own taxonomy — "Obstacle Course Racing, Fitness Racing, Trail Running, Hiking, Rucking" — is a useful reference model for `sport_type` values, though Onrace's brief-defined scope (HYROX, DEKA/functional-fitness, marathons/halves, triathlons, ultras) is closer to what hybrid athletes specifically compete in than OCR/rucking is.

## Proof-of-result findings (trust model validation)

- **Boston Marathon**: accepts "an official race result, a digital results platform, or a verified certificate from the timing company" as proof — i.e., a link/certificate from an official timing source, not a self-attested time. This directly validates Onrace's "required source link" trust model (`../CLAUDE.md` → Result trust model) as mirroring real elite-race practice, as the brief already assumed.
- **HYROX World Championships**: qualification is **placement-based** (top finishers at a Major/Last-Chance Qualifier), not a submitted-time threshold — no analogous "proof of time" submission flow exists for HYROX the way it does for Boston. This means the Boston-style example in the brief holds for marathons but doesn't generalize to HYROX; worth softening the brief's framing slightly to "e.g., Boston Marathon" rather than implying all elite hybrid-race entry works this way. Not blocking — the self-reported-link trust model still stands on its own merits (archival + portability) independent of whether every race requires it for entry.

## Race data availability (seeding)

Confirmed sources with structured, scrapable-by-hand event info for manual seeding:
- **hyrox.com/find-my-race** — dates, cities, official registration links.
- **spartan.com/en/deka** — DEKA FIT calendar, 2026 dates/cities confirmed for multiple US regions.
- **ocrbase.com** — community-submitted multi-format events (OCR/fitness racing/trail), could be a reference list to cross-check against, not a data source to scrape wholesale (respect their own aggregation effort/ToS — hand-curate from primary sources instead).
- Marathon majors (Boston, etc.) and DUV (ultras) have official calendars/databases but are lower priority than HYROX/DEKA for an MVP seed set aimed at the hybrid-athlete audience specifically.

**Gap**: no single source covers HYROX + DEKA + marathons + triathlons + ultras together — confirms manual curation (as already decided in `../CLAUDE.md`) is the only realistic MVP approach; no shortcut scrape target exists.

## Findings → decisions

- **Differentiation thesis confirmed**: the map+archive *combination* is the whitespace, not either half alone (see COMPETITORS above). Worth stating explicitly wherever Onrace's positioning gets written up next (concept/, or a future pitch doc).
- **Trust model validated**: required-source-link matches real elite-race verification practice (Boston). No change needed to `../CLAUDE.md`.
- **Suggested brief tweak**: soften the Boston Marathon example so it doesn't imply all elite hybrid races gate entry on submitted times — HYROX Worlds is placement-based, not time-based. Low priority, cosmetic.
- **Seed-data starting point**: prioritize HYROX (hyrox.com) and DEKA (spartan.com/en/deka) official calendars first for MVP seeding — they're the most hybrid-audience-specific and have the cleanest official sources; layer in a smaller set of major marathons/triathlons/ultras afterward rather than trying to cover all five sport types equally at launch.
- **Open, not yet decided**: whether to track Strava's new Events tab as a competitive risk if it expands beyond running/cycling into HYROX/DEKA territory — see CONCLUSIONS gap 3; revisit later, not blocking MVP.

## Next steps

1. ~~Capture reference screenshots into `screens/` for the products in the table above~~ — done 2026-09-02; Strava Events tab specifically closed via Julia's logged-in mobile screenshots (see `screens/strava-events.md`). Remaining gap: account-gated personal views on Athlinks (claimed-results history) and AllTrails ("Completed" log) still need a logged-in test account to capture.
2. Low-cost qualitative pass: skim App Store reviews for RoxFit/RoxMatchUp/HYBRD/HybridAF for recurring user complaints, before deciding whether primary interviews are worth the time given the 2-month MVP timeline.
3. Once taxonomy + differentiation thesis feel solid, move into `../wireframes/`.
