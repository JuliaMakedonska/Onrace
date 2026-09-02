# Research

Living notes for Onrace's discovery phase. Updated 2026-09-02 with a first competitor/reference pass (desktop web research, no user interviews yet — see gaps below).

## Questions to answer

- Who are the actual early users (recreational vs. competitive hybrid athletes), and where do they currently track races/results today?
- What does the current landscape look like — HYROX's own site, Athlinks, DUV, RaceRoster, Strava, spreadsheets?
- What sport taxonomy do athletes actually use when they think of "hybrid races"? Confirms/refines the scope in `../CLAUDE.md`.
- What proof do elite races (Boston Marathon, HYROX Elite, etc.) actually require when athletes apply with a qualifying time? Format, fields, source requirements.
- What race data is realistically available to seed the initial catalog (dates, locations, official links)?

## COMPETITORS

Comparison matrix and market-pattern findings for all **15 competitors** identified in the original audit (2026-09-02), across the three competitive tiers (HARD: same product/audience · SOFT: same task, different audience · ASPIRATIONAL: international benchmark). The first 5 — **ocrbase.com**, **RoxConnect**, **Strava** (Events tab), **Athlinks**, **AllTrails** — got an initial closer review; the remaining 10 were reviewed to the same depth in a follow-up pass. Split into three tables by tier for readability.

### Comparison matrix — HARD tier (same product, same audience)

| Axis | ocrbase.com | RoxConnect | RoxMatchUp | fitnessracingcalendar.com | RoxFit |
|---|---|---|---|---|---|
| **Audience** | OCR/functional-fitness/trail/rucking racers broadly — hybrid-adjacent, not hybrid-branded | HYROX-specific hybrid athletes, beginner→elite, claims "+80 countries" (confirmed on-page stat) | Hybrid/HYROX athletes, event organizers, and spectators (per its own App Store description) | Hybrid-race athletes — confirmed scope is "the UK and US, with more countries coming soon" (on-page tagline) | HYROX/hybrid athletes, training-first framing |
| **Product foundation** | Free web calendar, footer-credited "Made by Rebase Labs" | Native mobile app (iOS/Android) — App Store/Google Play badges shown on homepage | iOS app (iPad-designed) on Bubble.io (no-code); single developer credited (Hugues Dormoy) | Free web calendar, multi-format | Native iOS/Android app; footer credits "ROXFIT Limited" (registered company) |
| **Key mechanism** | Browse/filter races by format/date/country, map or list view | Create profile → filter/match with training partners → in-app chat | Browse HYROX/hybrid events → chat-based partner matching → classifieds (tickets/partners) → rolling 1-year ATP-style leaderboard | Filter (category/country/month) + flat list of event cards with starting price + "Book now"/"Sold out" CTA; free organizer submission | Discover & track races (list, live splits/rankings) + AI workout builder (HYPE) + race-day pacing plan (PACEME) + smartwatch sync + "Analyse Every Race" results/comparison |
| **Trust model** | None visible — listings read as self/community-submitted, no verification UI observed | Minimal — self-reported profile data, no verification UI observed | Self-reported profile/performance data; leaderboard claims "verified performances" — **mechanism data not confirmed** | None visible — no verification UI observed | Results appear pulled from RoxFit's own analyzed-race database rather than self-reported — **mechanism data not confirmed** |
| **Monetization** | No pricing/paid-tier UI observed anywhere on the site | Freemium: Free vs. ~$11.99/mo Premium (confirmed on-page pricing table) | Free + in-app purchases (RoxCoins micro-transactions to unlock contacts/boost listings) | No pricing/paid-tier UI observed; whether "Book now" is link-out or in-house checkout is **data not confirmed** | Free app; a new "Ultra" tier is in development (waitlist only) — **pricing data not confirmed** |
| **Sources** | [ocrbase.com](https://www.ocrbase.com/) · `screens/ocrbase.md` | [roxconnect.com](https://roxconnect.com) · `screens/roxconnect.md` | [App Store listing](https://apps.apple.com/ch/app/roxmatchup/id6743001913) · `screens/roxmatchup.md` — web app **access restricted** (login wall) | [fitnessracingcalendar.com](https://www.fitnessracingcalendar.com/) · `screens/fitnessracingcalendar.md` | [roxfit.app](https://roxfit.app/) · `screens/roxfit.md` |

### Comparison matrix — SOFT tier (same task, different audience)

| Axis | Strava (Events tab) | Athlinks | My Race Results | DUV Ultra Marathon Statistics | Race Roster |
|---|---|---|---|---|---|
| **Audience** | Strava's existing broad run/cycling base, now shown races via the Events tab | Competitive endurance athletes broadly (running/tri/swim/cycling/adventure racing) | General endurance athletes (running/tri/swim/cycling/multisport) wanting a dedicated race-only log — not hybrid-branded | Ultra-runners specifically (single-sport) | Race organizers, timers, fundraising coordinators (B2B) — not athlete-facing |
| **Product foundation** | Mature social fitness platform (web+app); races live under Groups → Events | Web results database; footer links to "Life Time" and "ChronoTrack" | Free web+iOS+Android app; footer reads "© 2025," a year stale at capture time | Free web database run by Deutsche Ultramarathon-Vereinigung e.V. (German nonprofit), all-volunteer team | Established company; confirmed offices in Sarasota, FL (USA) and London, ON (Canada) |
| **Key mechanism** | Search + faceted filters (Sport/Dates/Distance/Location/Elevation/Terrain) + a "Popular Races For You" personalized rail | Search/claim your name or bib in race results → build a personal race history | Manual entry, GPX import, or OCR-scan-a-screenshot to log a race; on-page counters read "0 Athletes · 0 Races Tracked · 0 Total Miles" at capture time | Race directors email results (Excel/text) to DUV → linked athlete↔event pages → auto-generated rankings for eligible events | Registration + fundraising + timing + virtual events + CRM + onsite check-in sold to organizers; athletes only arrive to complete a registration someone else set up |
| **Trust model** | Race listings sourced from Runna, not self-reported by athletes; activity data is the athlete's own GPS-tracked activity | Results reportedly auto-matched from official timing feeds — **mechanism specifics data not confirmed** | Purely self-reported (manual/GPX/OCR) — no required official source link, no auto-match | Director-submitted, not self-reported by athletes; corrections via contact form | N/A — not a results/ownership product |
| **Monetization** | Free Events tab observed; a paid tier reportedly gates training-analysis features — **price point data not confirmed** | Free to athletes; B2B link to ChronoTrack observed in footer | Freemium: free tier is unlimited race logging/search/timeline/PR tracking; subscription unlocks OCR import, interactive maps, advanced analytics, data export (confirmed on-page) | None observed — an unsold "Advertise here!" banner placeholder is the only monetization UI | B2B SaaS ("Request a demo" / "Let's talk") — pricing specifics **data not confirmed** |
| **Sources** | `screens/strava-events.md` (logged-in screenshots) · `screens/strava-home.png` (logged-out state) | [athlinks.com](https://www.athlinks.com/) · `screens/athlinks.md` | [myraceresults.app](https://www.myraceresults.app/) · `screens/myraceresults.md` | [statistik.d-u-v.org](https://statistik.d-u-v.org/) · `screens/duv.md` | [raceroster.com](https://raceroster.com/) · `screens/raceroster.md` |

### Comparison matrix — ASPIRATIONAL tier (international benchmarks)

| Axis | Parkrun | AllTrails | World Athletics | IRONMAN | Letterboxd |
|---|---|---|---|---|---|
| **Audience** | **Access restricted this pass** — data not confirmed | Outdoor enthusiasts (hiking/camping/trail running), broad skill range | Elite/competitive track & field and road-running athletes globally; the sport's governing body | Triathletes globally, beginner to Pro Series | Film enthusiasts broadly (cross-domain benchmark, not sports) |
| **Product foundation** | **Access restricted** — both `parkrun.com` and `parkrun.org.uk` returned an HTTP 405 "Human Verification" bot check; WebFetch hit the same wall | Web + mobile app; map-first trail directory | Official federation platform; news/media-led homepage with a Stats section beneath it | Established global race-series operator + retail Shop; personalization once signed in ("Hi IRONFAN!") | Established social platform — "3,938,638,123 films watched" logged at capture time (confirmed on-page) |
| **Key mechanism** | **Data not confirmed this session** — previously understood as barcode/token-scan timing, not self-reported; unverified this pass | Search by location/filters → trail detail → record/save an activity | Deep faceted filters (age category, timing method, wind reading, area/country, season, gender, event) over Toplists/Records/Rankings; a dedicated "Send Competition Results" nav item confirms organizer/official submission | "All Races" page = world map with **clustered pin counts** (161 matches total, confirmed on-screen) + a full faceted filter bar (race type/date/region/country/registration/course type) + text search | Self-log watched films → rate (5-star with halves) → write/share reviews → follow members → diary + curated lists/watchlist (all confirmed exact on-page copy) |
| **Trust model** | Data not confirmed this session | Community reviews + crowdsourced trail data; no personal-result verification concept observed | Federation-verified, official-timing-based — the highest-trust-signal reference point in the full set, via a mechanism not replicable at Onrace's scale | N/A for results in what was captured (a race-discovery/registration page, not a results archive) | Purely self-reported, no verification of any kind — high engagement (likes, follower graph) substitutes for it |
| **Monetization** | Data not confirmed this session | Freemium positioning stated publicly — **specific gated features/price data not confirmed** this pass | Sponsorship (Seiko "World Athletics Partner" badge, confirmed on-page) + merchandise Shop, not consumer subscription | Race registration fees (implied by "Registration Now Open" CTAs) + merchandise Shop — exact figures **data not confirmed** | Freemium — "Pro" subscription referenced inline and in nav |
| **Sources** | `screens/parkrun.md` · `screens/parkrun-blocked.png` — **access restricted** | [alltrails.com](https://www.alltrails.com) · `screens/alltrails.md` | [worldathletics.org](https://worldathletics.org/) · `screens/worldathletics.md` | [ironman.com](https://www.ironman.com/) · `screens/ironman.md` | [letterboxd.com](https://letterboxd.com/) · `screens/letterboxd.md` |

**Sourcing note:** every cell above is backed by a live screenshot, the product's own public page, or (for RoxMatchUp) its App Store listing — all linked in each table's Sources row. A handful of claims are marked **data not confirmed** where no citation was retained or a mechanism was implied but not directly verifiable (Strava's Runna-acquisition framing and paid-tier price, AllTrails' and Race Roster's exact pricing, Athlinks' and RoxFit's result-matching mechanisms). **Parkrun is marked access restricted**, not guessed: both `parkrun.com` and `parkrun.org.uk` returned an HTTP 405 bot-verification wall via both Playwright and WebFetch, and no bypass was attempted.

### Three shared market patterns

1. **Freemium (or an adjacent B2B subsidy) is the default business model.** Confirmed for RoxConnect (on-page: Free / $11.99/mo) and inferred for Athlinks (footer link to ChronoTrack, its B2B timing arm). Strava's and AllTrails' paid-tier specifics are data not confirmed this pass, but both publicly present a free tier plus a paid subscription. Nobody charges for the core "find/log a race" job itself.
2. **Nobody uses a self-reported, required-source-link trust model.** Athlinks reportedly auto-matches from timing feeds (mechanism data not confirmed with a retained link); Strava's own activity data is GPS-tracked; ocrbase and RoxConnect listings/profiles carry no verification layer at all (confirmed — no claim flow or verification badge observed in either product's screenshots). Onrace's "the link is the evidence" approach is genuinely novel among this set.
3. **Discovery and archiving are usually separate products — with two single-sport exceptions.** RoxConnect discovers *partners* (confirmed — no race-browsing UI found in `screens/roxconnect.md`); ocrbase discovers *races only* (confirmed — no personal-archive feature observed); Athlinks archives *results only* (confirmed — search-first homepage, no map/browse UI, `screens/athlinks.md`); Strava's Events sits inside an existing activity-tracking product (confirmed, `screens/strava-events.md`). But RoxFit ("Discover & Track Races" plus "Analyse Every Race," confirmed `screens/roxfit.md`) and RoxMatchUp (event discovery plus a rolling leaderboard, confirmed `screens/roxmatchup.md`) do combine both halves — scoped entirely to HYROX. No competitor combines both halves **across formats** the way Onrace plans to — see CONCLUSIONS gap 6.

### Three differences

1. **Scale and maturity vary enormously.** Athlinks (Life Time Fitness-linked per its footer) and Strava (an established platform, `screens/strava-home.png`) versus ocrbase's and RoxConnect's small-team footprint (ocrbase's "Made by Rebase Labs" footer credit is confirmed; exact company size for either is data not confirmed). Onrace starts at the small end of this spectrum.
2. **"Race discovery" is solved via at least four different product shapes.** Pure calendar browsing (ocrbase, confirmed screenshot), partner-matching wrapped around events (RoxConnect, confirmed screenshot), filters + a personalized rail bolted onto a social app (Strava, confirmed `screens/strava-events.md`), and a claimed-results database with no discovery layer at all (Athlinks, confirmed screenshot). None matches Onrace's planned map-first, cross-format approach exactly.
3. **Revenue structure differs by category.** Direct consumer subscription (RoxConnect confirmed; Strava/AllTrails publicly positioned as freemium but specifics data not confirmed) vs. B2B-subsidizes-free-consumer-product (Athlinks, ChronoTrack footer link) vs. no visible monetization (ocrbase, confirmed — no pricing UI anywhere on the site). CLAUDE.md's "no monetization plan" puts Onrace in the same bucket as the least-resourced competitor here.

## BENCHMARK

**Question:** which lightweight mechanisms should Onrace's MVP borrow to make self-reported result *ownership* credible, given there's no manual verification team? Benchmarked against 5 products that handle self-reported/unverified ownership claims well in their own niche, scored 1–5 on 8 criteria.

**Score anchors** — what a 1 and a 5 look like on each criterion:

- **Identity persistence** — 1 = anonymous/throwaway identity, free to discard and remake; 5 = tied to a durable, hard-to-fake real or professional identity.
- **Falsification cost** — 1 = as easy to fake as typing a sentence; 5 = faking it takes roughly as much effort as actually doing the real thing.
- **Independent cross-reference** — 1 = no external record exists to check the claim against; 5 = a public, independently-run database anyone can search to confirm it.
- **Peer/social visibility** — 1 = no one else ever sees the claim; 5 = surfaced directly to people with the specific knowledge to catch a lie.
- **Automatable plausibility checks** — 1 = any input is accepted, no rule-based check at all; 5 = obviously implausible claims are auto-rejected with no human reviewer needed.
- **Stakes-appropriate rigor** — 1 = verification effort is badly mismatched to what a false claim would gain someone; 5 = the built-in trust-signal is well-calibrated to the actual stakes of lying.
- **Dispute/correction mechanism** — 1 = no way to flag or fix a wrong/fraudulent entry after the fact; 5 = a lightweight, self-serve way to correct or contest a claim.
- **Source-artifact requirement** — 1 = a free-text claim is accepted on its own, nothing else required; 5 = an external, independently-hosted artifact (a link or document) is mandatory before the claim is accepted.

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
3. **The scale-breakdown risk doesn't apply yet — and there's now a concrete threshold to watch.** A map without clustering gets cluttered at high pin density, but MVP data is hand-seeded via SQL (`../CLAUDE.md`: no admin/CMS, races added directly via SQL) — realistically tens to low hundreds of races, the same range where ocrbase's and AllTrails' maps (both confirmed via screenshot) stay legible without clustering logic. IRONMAN's own "All Races" map needs clustering at 161 races globally (confirmed on-screen, `screens/ironman.md` / `screens/ironman-races.png`) — real evidence that low hundreds is roughly where clustering stops being optional, not just a theoretical ceiling.

Against the alternatives: faceted filter + browse alone is the closest runner-up — `../CLAUDE.md`'s own feature line already licenses it as the map's companion (list toggle or synced panel, matching both ocrbase's and AllTrails' pattern, confirmed via screenshot) for an athlete who already knows their date/sport constraints rather than browsing by location. A personalized recommendation feed doesn't fit: it needs behavioral history Onrace won't have at a cold-start launch, and no ranking pipeline is budgeted in the Supabase-only stack (`../CLAUDE.md` → Tech stack).

## CONCLUSIONS

For each open gap surfaced by the analysis above, a hypothesis and the section it follows from. None of these are validated with real user/usage data yet.

1. **Gap:** no competitor in the COMPETITORS matrix requires a mandatory source link the way Onrace will — will this cause submission drop-off? **Hypothesis:** friction will be measurable but survivable, because the target audience already produces official result links for other purposes (e.g. Boston Marathon qualifying-time proof — see "Proof-of-result findings" below); the extra step is small relative to a motivation that already exists, but the net effect is likely fewer results logged per user, not zero adoption. **Follows from:** COMPETITORS.
2. **Gap:** HYROX-specific competitors' monetization is more varied than the original audit assumed — RoxConnect confirmed subscription (~$11.99/mo), but a closer look shows RoxFit is a free app with an unpriced "Ultra" tier still in waitlist and RoxMatchUp is free with microtransactions (RoxCoins), not a subscription (`screens/roxfit.md`, `screens/roxmatchup.md`) — while Onrace's brief states no monetization plan at all. **Hypothesis:** "no monetization" is workable through MVP validation but not indefinitely — if revenue is needed later, the realistic options are a direct consumer model (subscription like RoxConnect, or micro-transactions like RoxMatchUp) or a B2B/organizer-subsidy model (like Athlinks×ChronoTrack) — there's no single obvious category default to fall back on, so this is a genuinely open design choice, not a foregone one. **Follows from:** COMPETITORS.
3. **Gap:** whether Strava's Events tab will expand beyond running/cycling into HYROX/DEKA territory, turning a SOFT competitor into a HARD one. **Hypothesis:** low probability inside Onrace's 2026-11-01 MVP window — every race sampled in `screens/strava-events.md` (2026-09-02, logged-in screenshots) was running-only (10K/Half/Marathon), and expansion would need a new data partnership, not just a UI change. Data not confirmed beyond this one screenshot pass — worth a periodic recheck, not a blocking risk. **Follows from:** COMPETITORS.
4. **Gap:** are automatable plausibility checks (dead-link detection, implausible-time flags, duplicate detection) a sufficient substitute for the peer-visibility mechanism ruled out for MVP? **Hypothesis:** sufficient to catch crude fabrications (impossible times, dead links, exact duplicates) but not a real-but-mismatched link (someone else's genuine result, wrong owner) — an acceptable residual risk given Onrace's trust model is explicitly "the link is the evidence," not "Onrace verifies" (`../CLAUDE.md` → Result trust model), so this is a known, deliberate limit, not a hidden gap. **Follows from:** BENCHMARK.
5. **Gap:** the MVP map-UI implementation choice (List/Map toggle vs. AllTrails-style split-pane) isn't decided, and no clustering plan exists for when the seed catalog outgrows "tens to low hundreds" of races. **Hypothesis:** toggle-first (ocrbase's pattern, `screens/ocrbase-events-map.png`) is the right MVP choice given the 2-month timeline and small seed catalog, with split-pane and clustering deferred to a v2 once real usage — not assumption — shows whether users hit that friction. Data not confirmed against Onrace's actual eventual catalog size. **Follows from:** PATTERNS.
6. **Gap:** RoxFit and RoxMatchUp already combine race discovery and a personal results/leaderboard view in one HYROX-specific app (`screens/roxfit.md`, `screens/roxmatchup.md`) — is the map+archive combination still genuine whitespace for Onrace? **Hypothesis:** yes, but narrower than first stated — both existing combinations are single-sport (HYROX only); no competitor reviewed across all 15 combines discovery and archive **across** HYROX + DEKA + marathons + triathlons + ultras together. Onrace's differentiation claim should be restated as cross-format breadth combined with the archive, not the discovery+archive combination alone, which two competitors already have at smaller scope. **Follows from:** COMPETITORS.

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

- **Differentiation thesis refined, not overturned**: RoxFit and RoxMatchUp (see COMPETITORS → HARD tier, `screens/roxfit.md`, `screens/roxmatchup.md`) already combine race discovery and a personal results/leaderboard view — but both are HYROX-only. Onrace's actual whitespace is narrower than first stated: **cross-format** discovery + archive (HYROX, DEKA, marathons, triathlons, ultras together), not the discovery+archive combination alone. Worth stating this more precisely wherever Onrace's positioning gets written up next (concept/, or a future pitch doc) — see CONCLUSIONS gap 6.
- **Trust model validated**: required-source-link matches real elite-race verification practice (Boston). No change needed to `../CLAUDE.md`.
- **Suggested brief tweak**: soften the Boston Marathon example so it doesn't imply all elite hybrid races gate entry on submitted times — HYROX Worlds is placement-based, not time-based. Low priority, cosmetic.
- **Seed-data starting point**: prioritize HYROX (hyrox.com) and DEKA (spartan.com/en/deka) official calendars first for MVP seeding — they're the most hybrid-audience-specific and have the cleanest official sources; layer in a smaller set of major marathons/triathlons/ultras afterward rather than trying to cover all five sport types equally at launch.
- **Open, not yet decided**: whether to track Strava's new Events tab as a competitive risk if it expands beyond running/cycling into HYROX/DEKA territory — see CONCLUSIONS gap 3; revisit later, not blocking MVP.

## Next steps

1. ~~Capture reference screenshots into `screens/` for the products in the table above~~ — done 2026-09-02; Strava Events tab specifically closed via Julia's logged-in mobile screenshots (see `screens/strava-events.md`). Remaining gap: account-gated personal views on Athlinks (claimed-results history) and AllTrails ("Completed" log) still need a logged-in test account to capture.
2. Low-cost qualitative pass: skim App Store reviews for RoxFit/RoxMatchUp/HYBRD/HybridAF for recurring user complaints, before deciding whether primary interviews are worth the time given the 2-month MVP timeline.
3. Once taxonomy + differentiation thesis feel solid, move into `../wireframes/`.
