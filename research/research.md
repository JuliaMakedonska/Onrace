# Research

Living notes for Onrace's discovery phase. Updated 2026-09-02 with a first competitor/reference pass (desktop web research, no user interviews yet — see gaps below).

## Questions to answer

- Who are the actual early users (recreational vs. competitive hybrid athletes), and where do they currently track races/results today?
- What does the current landscape look like — HYROX's own site, Athlinks, DUV, RaceRoster, Strava, spreadsheets?
- What sport taxonomy do athletes actually use when they think of "hybrid races"? Confirms/refines the scope in `../CLAUDE.md`.
- What proof do elite races (Boston Marathon, HYROX Elite, etc.) actually require when athletes apply with a qualifying time? Format, fields, source requirements.
- What race data is realistically available to seed the initial catalog (dates, locations, official links)?

## Competitor / reference audit

_Screenshots captured 2026-09-02 for the 5 deep-dive competitors below — see `screens/README.md` and the Visual observations section further down. Table notes below are from live-site/WebFetch review._

| Product | What it is | Race discovery | Personal results archive | Notes vs. Onrace |
|---|---|---|---|---|
| [hyrox.com/find-my-race](https://hyrox.com/find-my-race/) | Official HYROX event calendar | List, single format (HYROX only), registration links | No | Owns its own format only; won't ever list marathons/DEKA/etc. |
| [Athlinks](https://www.athlinks.com/) | Legacy endurance-results database | No map; result search by name/bib | Yes — claims results, "rivals" comparisons, training log | Huge historical archive (10 yrs, running/tri/swim/cycling/adventure racing) but **no HYROX/DEKA/functional-fitness coverage**, no map-based discovery, dated UX. Results are auto-matched from timing feeds, not self-reported with a source link. |
| [DUV Ultra Marathon Statistics](https://statistik.d-u-v.org/) | Ultra-running results & rankings database | Event list, not a map | Yes, but ultra-running only | Race directors push results via file upload; not self-reported by athletes. Ultra-only scope. |
| [RaceRoster](https://raceroster.com/) | Registration/timing SaaS for race organizers | N/A (B2B tool, not athlete-facing discovery) | Results shown per-event, not personal cross-race archive | Not a competitor — it's infrastructure organizers use; Onrace could eventually link out to RaceRoster event pages as `official_url`. |
| **Strava Events tab** (new, 2026 — via Runna acquisition) | Race discovery inside Strava, matched to sport/location | Yes — filters by distance, date, location, sport, elevation, temperature | No (Strava has activities, not an official-result archive with source links) | **Most significant new entrant.** Currently running/cycling-centric (Runna's base); no signal yet it covers HYROX/DEKA/functional fitness. Worth re-checking scope periodically — if Strava expands into hybrid-format races, it competes directly on the discovery half. |
| **ocrbase.com** | Community-run OCR/fitness-race calendar | Yes — list + map toggle, filters by organizer, format (OCR, Fitness Racing, Trail, Hiking, Rucking), date, country | No | **Closest direct competitor to Onrace's map half.** Multi-format like Onrace's scope, free community event submission (Google Form), but no personal archive, no results/proof concept at all. Validates that "aggregate calendar across hybrid-adjacent formats" is a real, wanted product shape. |
| [fitnessracingcalendar.com](https://www.fitnessracingcalendar.com/) | Fitness-race calendar (DEKA-focused page seen) | List with country/month/distance filters, upcoming/past toggle | Possibly (a "past events" toggle exists) but appears to just be historical event listings, not personal-athlete results | Narrower and less polished than ocrbase; single-format pages per race series. |
| **My Race Results** (app) | Personal race-result logging app | No | Yes — this is its whole purpose: log finish times, dates, locations, notes across running/marathon/tri/cycling/swim/multisport; has OCR-scan-a-screenshot import | **Closest direct competitor to Onrace's archive half.** Not hybrid-athlete branded, no HYROX/DEKA-specific framing, and results aren't tied to a required official source link — self-reported free text instead of Onrace's "link is the evidence" trust model. |
| **RoxFit / RoxMatchUp / RoxConnect** (hybrid-athlete app ecosystem) | Training + event-discovery + partner-matching apps built specifically for the HYROX/hybrid community | RoxMatchUp centralizes/discovers HYROX + hybrid events | RoxFit lets users share results/achievements (social, not archival-with-proof) | Validates strong existing demand from this exact audience for HYROX-adjacent tooling — but fragmented across several single-purpose apps rather than one map + archive product. |

**Takeaway:** No competitor currently combines (a) a cross-format map covering HYROX/DEKA/marathons/etc. together with (b) a personal, source-linked results archive. ocrbase is closest on the map half; My Race Results is closest on the archive half. Onrace's actual whitespace is the *combination*, not either piece alone — worth stating explicitly as the differentiation thesis once `research/findings → decisions` gets fleshed out further.

### Competitor grouping — HARD / SOFT / ASPIRATIONAL

**HARD — same product, same audience, our market** (hybrid-athlete race discovery/archive apps)

| Company | Why HARD | What to learn from it |
|---|---|---|
| **RoxMatchUp** | Event-discovery app built explicitly for HYROX + hybrid events — same audience, same core job (find your next race), our exact niche. | How narrow, community-sized apps frame "hybrid event" scope; validates that a dedicated discovery app for this audience is viable at small scale. |
| **RoxConnect** | Also hybrid-athlete-specific; lists events with date/location/price/distance, same audience. | It layers a social/partner-matching angle onto event discovery — a reminder that this audience values training-partner-finding, a possible future feature, not core to MVP but worth noting. |
| **ocrbase.com** | Multi-format (OCR/fitness racing/trail/rucking) map+list calendar; audience overlaps heavily with hybrid athletes even without the branding. Closest thing to Onrace's map half that exists today. | Its filter model (organizer, format, date, country) and list/map toggle are a concrete UI reference; also study its free community-submission flow as a possible future alternative to pure manual seeding. |
| **fitnessracingcalendar.com** | Functional-fitness-race calendar (DEKA-focused), same underlying niche and task. | Shows what a *minimal, single-format* version of the map half looks like — useful as a "what not to under-build" floor, since it's narrower/less polished than ocrbase. |
| **RoxFit** | Training + result-sharing app purpose-built for hybrid athletes/HYROX — same audience, adjacent product (training-first, race-secondary). | How it frames "share your result" socially rather than archivally — Onrace should study this to make sure the archive reads as *personal proof record*, not a social feed, per the brief's explicit no-social-features scope. |

**SOFT — different product, same underlying task** (finding/choosing a race, or archiving results, for a broader endurance audience)

| Company | Why SOFT | What to learn from it |
|---|---|---|
| **Strava** (new Events tab, via Runna) | Solves race discovery for a much broader run/cycling audience, not hybrid-specific — same task, different product and audience. | Most important one to watch: a well-resourced, high-distribution player just entered race discovery. Study how it matches races to athletes (sport/location/distance) — and keep checking whether it expands into HYROX/DEKA, which would turn this into a HARD competitor. |
| **Athlinks** | Endurance results database (running/tri/swim/cycling) — same "archive your race history" task, different audience (not hybrid-specific) and no discovery/map. | Legacy UX to avoid: dated, no map, results auto-matched from timing feeds rather than self-reported+linked. Good negative example of what happens without a map/archive combo. |
| **My Race Results** (app) | Personal race-log app for a general multisport audience — solves Onrace's archive half exactly, just not for this audience and without the required-source-link trust model. | Its OCR-scan-a-screenshot import for logging a result is a genuinely useful pattern to consider for Onrace's result-entry flow, to reduce friction versus manual field entry. |
| **DUV Ultra Marathon Statistics** | Same task (find races, see results) for ultra-runners specifically — one of Onrace's five target sport types, but as a single-sport tool, not hybrid-athlete framed. | Reference for what serious statistical/ranking depth looks like in one sport vertical — a reminder of how much deeper a single-sport competitor can go than a cross-format MVP will at launch; don't try to out-feature it on ultras specifically. |
| **RaceRoster** | Registration/timing SaaS — athletes use it as part of the same "choose and enter a race" journey, but it's organizer-facing infrastructure, not athlete-facing discovery. | Its event pages are a likely target for Onrace's `official_url`/`registration_url` fields — worth knowing its URL structure when seeding data and linking out. |

**ASPIRATIONAL — international benchmarks in race-discovery/results**

| Company | Why ASPIRATIONAL | What to learn from it |
|---|---|---|
| **Parkrun** | Global (23 countries, 2,000+ locations) endurance-event network with a famously simple, permanent personal results history page tied to every event attended. | Benchmark for how clean and low-friction a personal result/history page can be — Onrace's results archive UI should aim for this level of simplicity, not Athlinks' clutter. |
| **AllTrails** | International benchmark for map-based activity discovery: rich filters, a synced "Completed" activity log with map view, reviews/photos — adjacent outdoor-activity vertical, not racing, but the exact discovery+personal-log shape Onrace is building. | Its map-view "Completed" log (toggle between map and list of what you've done) is close to a template for how Onrace could visually unify the race map and personal results archive as one coherent product, not two disconnected sections. |
| **World Athletics** (official results/records database) | Global governing-body benchmark for what an "official, verified result" data model and presentation look like at the highest level of trust. | Reference for how to *signal* authority/verification in a results UI (badges, source attribution, certification language) even though Onrace's model is self-reported-with-link rather than governing-body-verified. |
| **IRONMAN** (global event footprint + IRONMAN Tracker) | ~190 events worldwide across five brands with official real-time results/tracking — international benchmark for triathlon, one of Onrace's five target sports, at global scale. | How it presents official results/splits with strong trust signals tied to bib numbers — a model for what "official source" should look and feel like when Onrace links out to it. |
| **Letterboxd** | Cross-domain benchmark (film logging, not sports) for "a personal archive of things you've experienced, each entry backed by a citation/reference" — proves the archive-as-identity pattern works well outside sports. | Its diary/log UX (chronological personal history, minimal but satisfying to fill in) is a good reference for making Onrace's results archive feel like a rewarding personal record, not a chore form. |

### Deep-dive comparison — 5 selected competitors

Selected across the three groups above for a closer read: **ocrbase.com**, **RoxConnect** (HARD), **Strava — Events tab**, **Athlinks** (SOFT), **AllTrails** (ASPIRATIONAL). Table below gathered via WebFetch/WebSearch; live screenshots were captured in a follow-up pass (2026-09-02, Playwright MCP) — see the Visual observations section below and `screens/`.

| Axis | ocrbase.com | RoxConnect | Strava (Events tab) | Athlinks | AllTrails |
|---|---|---|---|---|---|
| **Audience** | OCR/functional-fitness/trail/rucking racers broadly — hybrid-adjacent, not hybrid-branded | HYROX-specific hybrid athletes, beginner→elite, claims 80 countries | Strava's existing broad run/cycling base, now shown races via the 2026 Runna acquisition | Competitive endurance athletes broadly (running/tri/swim/cycling/adventure racing) | Outdoor enthusiasts (hiking/camping/trail running), broad skill range |
| **Product foundation** | Free, community-run web calendar (Rebase Labs, small UK company); map+list, event submission via Google Form | Native mobile app (iOS/Android); social/matching platform layered on event data | Mature social fitness platform (web+app) with race discovery bolted on via acquisition | Web results database owned by Life Time Fitness / ChronoTrack, paired with a B2B timing/registration business (Athlinks Services) | Web + mobile app; map-first trail directory built on crowdsourced + official park content |
| **Key mechanism** | Browse/filter races by format/date/country, map or list view, no account needed to browse | Create profile → filter/match with training partners → in-app chat → coordinate around an event | Personalized activity feed/kudos, now plus a matched Events tab (sport/location/date/distance) surfacing races | Search/claim your name or bib in race results → build a personal race history → compare to "rivals" | Search by location/filters → trail detail → record/save an activity → share to community |
| **Trust** | None explicit — listings read as self/community-submitted, no verification layer | Minimal — mostly self-reported profile data; "official event integration" for event details only | Effort/activity data is the athlete's own GPS-tracked activity (not third-party verified); race listings sourced from Runna's database, not self-reported | Results auto-matched to a claimed profile from official timing feeds (ChronoTrack, etc.) — no self-report, no source-link requirement | Community reviews + crowdsourced trail data blended with official park data; no personal-result verification concept at all (not a results product) |
| **Monetization** | Unclear / likely none yet — small early-stage company, no visible paid tier, free to list an event | Freemium: free tier (5 msgs/mo) vs. Premium ~$11.99/mo (unlimited messaging, advanced filters) | Freemium: the Events tab itself is free for everyone; paid tier ($9.99–11.99/mo) gates *training-analysis* features (segments, HR zones, route builder) — race discovery is not paywalled | Free to athletes; monetized B2B via Athlinks Services/ChronoTrack (timing & registration sold to race organizers) | Freemium: free browsing; Plus/Peak subscription gates route-building, offline maps, printable maps; no ads |

#### Three shared market patterns

1. **Freemium (or an adjacent B2B subsidy) is the default business model** — RoxConnect, Strava, and AllTrails all keep core discovery/browsing free and gate advanced features behind a subscription; Athlinks instead monetizes organizers (ChronoTrack) rather than athletes. Nobody charges for the core "find/log a race" job itself.
2. **Nobody uses a self-reported, required-source-link trust model** — trust is either automated (Athlinks' timing-feed auto-match, Strava's own GPS data) or effectively absent (ocrbase's unverified listings, RoxConnect's self-reported profiles). Onrace's "the link is the evidence" approach is genuinely novel among this set, not an established pattern to lean on.
3. **Discovery and archiving are always separate products, never natively unified** — RoxConnect discovers *partners*, ocrbase discovers *races only*, Athlinks archives *results only*, Strava bolted discovery onto an existing activity-tracking product. Nobody launched with both halves as one coherent product — reinforces the whitespace finding from the grouping section above.

#### Three differences

1. **Scale and maturity vary enormously** — Strava and Athlinks are large, backed platforms (Athlinks owned by Life Time Fitness; Strava a category leader) with acquired/legacy data assets, versus ocrbase/RoxConnect being small, niche, likely single-founder-scale tools. Onrace starts at the small end of this spectrum.
2. **"Race discovery" is being solved via at least four different product shapes** — pure calendar browsing (ocrbase), partner-matching wrapped around events (RoxConnect), a social feed with discovery bolted on (Strava), and a claimed-results database with no discovery layer at all (Athlinks). None matches Onrace's planned map-first, cross-format approach exactly.
3. **Revenue structure differs by category** — direct consumer subscription (RoxConnect, Strava, AllTrails) vs. B2B-subsidizes-free-consumer-product (Athlinks) vs. no clear monetization (ocrbase). Onrace's brief currently states no monetization plan, which puts it in the same bucket as the least-resourced competitor here (ocrbase) — worth being deliberate about, not just default.

#### Three open questions for the PM

1. Since no competitor requires a source link the way Onrace will, is there a real risk that this becomes submission friction (versus Athlinks' zero-effort auto-claim or a free-text entry model)? Worth validating whether target users actually retain/can find an official results link months after a race, before locking the requirement in as-is.
2. Every HYROX-specific competitor found (RoxConnect, RoxFit, RoxMatchUp) monetizes via consumer subscription — does Onrace intend to eventually monetize on the same axis, or lean toward Athlinks' B2B-subsidy model (e.g., timing/registration partnerships) instead? The brief says "no monetization plan for now," but this table suggests the category's revenue mostly comes from one of these two structures — worth a deliberate future call rather than leaving it fully open.
3. Strava entering race discovery for free, bundled into an already-dominant platform, is a distribution threat no small independent product can outspend. Should Onrace's strategy explicitly commit to the hybrid-format-breadth + verified-archive niche rather than ever competing with Strava on general race discovery — and if Strava extends into HYROX/DEKA coverage, does that change the answer?

### Visual observations (screenshot pass, 2026-09-02)

Live browser capture (Playwright MCP) of the 5 deep-dive competitors, closing the gap flagged in the previous pass. Full notes per product are in `screens/*.md`; screenshots in `screens/*.png`. Four findings worth calling out here:

1. **Two real map/list UI patterns exist, not just one.** ocrbase uses a **List/Map toggle** (map replaces the list, clustered pin counts like "78" per region). AllTrails uses a **true split-pane** (scrollable card list synced live to the map viewport, pins show a distance badge instead of a plain marker or count). Toggle is cheaper to build; split-pane is the more polished target. Given Onrace's MVP dataset will start small (hand-curated HYROX/DEKA seed set, not hundreds of pins), clustering isn't needed yet either way — worth deciding List/Map-toggle-first for MVP and treating AllTrails' split-pane as a v2 target, not a launch requirement.
2. **RoxConnect's dark/black/high-contrast marketing site is a concrete visual match for the brief's "bold & competitive" brand tone** (`../CLAUDE.md`) — this validates that choice against a real product this exact audience already uses, not just a stated preference. Also visually confirmed RoxConnect's pricing ($0 free / $11.99/mo premium), matching the figure already in the deep-dive table.
3. **Athlinks' staleness is now directly visible, not just inferred.** Its homepage "What's Happening" section is labeled "(COMING SOON)" but still displays a sample countdown card for a 2017 Miami Marathon — live evidence of an unmaintained legacy product, and a concrete example of what to avoid (shipping placeholder/stale content instead of an honest empty state).
4. **Strava's Events tab is confirmed genuinely unreachable outside the app** — navigating directly to `strava.com/events` redirects to the logged-out marketing homepage, and that homepage's public nav (Activities/Features/Maps/Challenges/Subscription) has no Events entry at all. Reinforces that Strava's race-discovery threat is currently invisible to anyone not already deep in the app — good for near-term competitive risk, but means Onrace can't easily keep tabs on how that feature evolves without a logged-in test account.

## User research

_Not started — no interviews or surveys conducted yet._ Given the app ecosystem found above (RoxFit, RoxMatchUp, HybridAF, HYBRD), a cheap next step would be reading their App Store reviews for recurring complaints (a form of low-cost qualitative research) before committing to primary interviews.

## Sport taxonomy findings

- "Hybrid athlete" is a training-methodology term (formally systematized by Alex Viada, *The Hybrid Athlete*, 2013): someone deliberately training strength + endurance together, not casually cross-training. This matches the brief's framing — confirms "hybrid athlete" describes the **audience**, not a race format, exactly as `../CLAUDE.md` already states.
- The existing app ecosystem (RoxFit, HySim, RoxMatchUp, HYBRD, HybridAF) treats **HYROX as the anchor format** for this audience, with marathons/OCR/functional-fitness as adjacent interests — supports keeping HYROX as the flagship format in seed data even though scope is broader.
- ocrbase's own taxonomy — "Obstacle Course Racing, Fitness Racing, Trail Running, Hiking, Rucking" — is a useful reference model for `sport_type` values, though Onrace's brief-defined scope (HYROX, DEKA/functional-fitness, marathons/halves, triathlons, ultras) is closer to what hybrid athletes specifically compete in than OCR/rucking is.

## Proof-of-result findings (trust model validation)

- **Boston Marathon**: accepts "an official race result, a digital results platform, or a verified certificate from the timing company" as proof — i.e., a link/certificate from an official timing source, not a self-attested time. This directly validates Onrace's "required source link" trust model (`../CLAUDE.md` → Result trust model) as mirroring real elite-race practice, as the brief already assumed.
- **HYROX World Championships**: qualification is **placement-based** (top finishers at a Major/Last-Chance Qualifier), not a submitted-time threshold — no analogous "proof of time" submission flow exists for HYROX the way it does for Boston. This means the Boston-style example in the brief holds for marathons but doesn't generalize to HYROX; worth softening the brief's framing slightly to "e.g., Boston Marathon" rather than implying all elite hybrid-race entry works this way. Not blocking — the self-reported-link trust model still stands on its own merits (archival + portability) independent of whether every race requires it for entry.

## Ownership-credibility deep dive (narrowed from "trust")

The competitor matrix (see grouping/deep-dive above) framed the open question as platform-level "trust." On reflection that's too broad: a linked official result is only ever as credible as its official source — Onrace doesn't need to *be* trusted as a verifier. The actual open problem is narrower: **credible self-reported ownership** — how confident can anyone be that a linked result truly belongs to the person claiming it, given Onrace has no verification pipeline in MVP?

### Evaluation criteria (1–5, higher = more ownership-credibility achievable without a manual verification team)

1. **Identity persistence** — is the claim bound to a durable, hard-to-recreate identity (real-name/professional/reputational stakes) rather than an anonymous or throwaway one?
2. **Falsification cost** — how much effort does faking the claim take relative to actually doing the thing?
3. **Independent cross-reference availability** — does an external, independently-hosted record exist that anyone (not just the platform) could check the claim against?
4. **Peer/social visibility** — is the claim exposed to people with the specific knowledge to notice and contest a lie?
5. **Automatable plausibility checks** — can obviously implausible claims be caught by simple rules (duplicates, format/domain checks, sanity bounds) with no human reviewer?
6. **Stakes-appropriate rigor** — does the amount of built-in trust-signal roughly match how much a false claim would actually gain the person (a low-stakes claim needing little rigor is *good* design, not a gap)?
7. **Dispute/correction mechanism** — is there a lightweight, non-admin way to flag, self-correct, or challenge a claim after the fact?
8. **Source-artifact requirement** — does making the claim require attaching an external, independently-hosted artifact (a link, not just free text) as a precondition?

### Products that handle self-reported ownership well, in their own niche

- **Goodreads reading log** — users self-mark books "read," no verification; near-zero incentive to lie makes the near-zero rigor appropriate. ([Goodreads Reading Challenge](https://www.goodreads.com/group/show/58421-2026-reading-challenge))
- **Letterboxd diary** — self-logged watched films with optional review/rating, publicly visible to followers; an active review culture adds mild social scrutiny beyond Goodreads' quieter shelves. ([Letterboxd diary feature](https://letterboxd.zendesk.com/hc/en-us/articles/15178773269263), [Letterboxd FAQ](https://letterboxd.com/about/faq/))
- **Strava manual activity entries** — activities entered without GPS data are structurally segregated: they're excluded from challenge and segment leaderboards by design, unlike GPS-tracked efforts, which Strava's own algorithms can flag for implausible data. ([Strava Help: Virtual Trainer Activities](https://support.strava.com/en-us/articles/15401857-virtual-trainer-activities-on-strava), [Strava Help: Segment Leaderboard Guidelines](https://support.strava.com/en-us/articles/15401921-segment-leaderboard-guidelines))
- **LinkedIn certifications** — self-added with optional Credential ID + Credential URL fields linking back to the issuer; LinkedIn doesn't verify the fields itself, but a filled-in URL lets any viewer click through and check. ([How to add certifications on LinkedIn](https://socialrails.com/blog/how-to-add-certifications-to-linkedin)) — high-stakes professional claims but only *optional* external verification, a known weak point.
- **Chess.com FIDE OTB rating field** — users self-enter their over-the-board FIDE rating into a profile field; Chess.com does not verify it for regular players (only titled players' credentials are checked), but FIDE itself runs a fully public, independently searchable ratings database anyone can cross-check the claim against. ([Chess.com forum: "Are FIDE Ratings on the profiles verified by Chess.com?"](https://www.chess.com/forum/view/general/are-fide-ratings-on-the-profiles-verified-by-chess-com))

### Scoring table

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

Reading the table: Goodreads and Letterboxd score low almost everywhere *except* stakes-appropriate rigor — they're not weak designs, they're correctly-calibrated designs for a low-stakes claim. Strava and LinkedIn score highest but for opposite reasons — Strava wins by **structurally downgrading** a low-verifiability claim type (segregation, not verification), while LinkedIn wins by **identity + optional linkage** but is undermined by making the one mechanism that would actually help (the Credential URL) optional. Chess.com is the strongest case of "independent cross-reference exists but isn't required" — the FIDE database is a perfect check nobody is forced to use.

### Three lightweight mechanisms worth bringing into Onrace's MVP

1. **Make the source link mandatory, not optional, at the point of submission.** LinkedIn's certification field proves the failure mode of leaving this optional — most users skip a step that isn't required, even when it would substantially raise credibility. Onrace's brief already plans a required link; this comparison is a concrete reason not to soften that in implementation, no admin needed since it's a form-validation rule.
2. **Structurally label every result as self-reported + source-linked, never as "verified."** Borrowed from Strava's manual-vs-GPS segregation: the trust signal comes from *how the claim is categorized and displayed*, not from a review step. A simple UI convention (e.g., always showing "via [domain of official_result_url]" next to a result, never a checkmark/badge implying Onrace vouches for it) sets correct expectations with zero ongoing admin cost.
3. **Add automatable plausibility checks at submission time.** No human reviewer needed: reject a dead/unreachable link, flag implausible finish times for a given sport/distance, and flag exact duplicate race+time combinations submitted by different accounts. This is the one criterion (#5) every self-reported product in the table scored weakly on — a cheap opportunity for Onrace to do better than all five references simultaneously.

### One mechanism that won't work for Onrace's MVP: peer/social visibility

Letterboxd's engaged review community and Strava's kudos/comments culture both lean on **a critical mass of peers who know the claimant's real skill level** to organically catch false claims. Onrace's results archive is explicitly *not* a social feed — per `../CLAUDE.md`, social features, following, and public sharing of results are out of scope for MVP. With no followers, no comments, and (at launch) a thin user base, there's no audience positioned to notice or contest a fabricated result the way a training partner would on Strava. Importing "let the crowd police it" isn't viable here; the mandatory-link, labeling, and automatable-checks mechanisms above have to substitute for the social layer this pattern actually depends on.

## Race-discovery UX patterns

The key task for the map half of Onrace: finding a suitable race among many available hybrid competitions and marathons. Five fundamentally different UX patterns solve this kind of "find one good option among many" problem — not variations of one approach, but distinct interaction models.

### The five patterns

**1. Faceted filter + browse**
*How it works:* user picks values on independent axes (region, date, sport type, distance) that progressively narrow a result set; results render as a list or grid.
*Where used:* ocrbase.com, AllTrails' side panel, Zillow, Airbnb's filter bar.
*When it fits:* large catalog, discrete well-defined attributes, user already knows roughly what they want on 1–3 axes.
*When it breaks down:* user doesn't know which axes matter yet ("show me something interesting"); filters over-narrow to zero results with no fallback; catalog too small for filtering to save real effort.

**2. Personalized/algorithmic recommendation feed**
*How it works:* system ranks and surfaces items using the user's history/behavior/profile, no explicit query required — user scrolls a feed the system assembled.
*Where used:* Strava's Events tab (matched by sport/location/distance history), Netflix, Spotify Discover Weekly.
*When it fits:* platform has accumulated behavioral data; decision is low-stakes/frequent enough that passive suggestion beats active search; users want to be shown rather than to look.
*When it breaks down:* cold start — no history yet means no signal; opaque ranking undermines trust for a high-stakes, infrequent decision (choosing one race to train toward); requires an ongoing ranking pipeline to build and maintain.

**3. Search-by-query (text search / autocomplete)**
*How it works:* free-text box, user types what they're looking for, system matches/ranks against a query.
*Where used:* Google, Athlinks' homepage ("Enter an athlete name"), most e-commerce search bars.
*When it fits:* user already has a specific target in mind (a race name, a city) — fast for someone who knows exactly what they want.
*When it breaks down:* useless for exploratory browsing ("what's out there in my region this fall") — it assumes the query rather than generating it; vocabulary/typo mismatch; no good way to express "near me, sometime in the next 3 months, any sport."

**4. Curated/editorial lists (collections)**
*How it works:* a human editor groups items by theme or occasion ("Best beginner-friendly hybrid races in Europe," "Fall marathon picks") — the user browses judgment, not raw data.
*Where used:* Wirecutter, travel-guide "best of" posts, IRONMAN's featured-races carousel.
*When it fits:* catalog is large/undifferentiated and users benefit from expert framing; there's ongoing editorial capacity; trust/authority is part of the value.
*When it breaks down:* doesn't scale to comprehensive coverage; goes stale fast; requires continuous manual upkeep; fails users with a specific need outside whatever angle was curated.

**5. Map-first spatial exploration**
*How it works:* a pan/zoom map is the primary surface; markers represent races, discovery happens by moving through geography rather than filtering or querying.
*Where used:* AllTrails' `/explore` (see `screens/alltrails.md`), Airbnb's map view, Google Maps "things to do nearby," ocrbase's map toggle (see `screens/ocrbase.md`).
*When it fits:* geography is a primary decision axis (traveling athletes, "what's near me"), visual/spatial thinking, supports serendipity.
*When it breaks down:* doesn't scale globally without clustering; hard to layer multiple non-spatial facets (date + sport + distance) onto a map without clutter; weak when the user cares more about *when* than *where*; cramped on small screens.

### Fit against `../CLAUDE.md`

**Best fit: Map-first spatial exploration (5).**
1. Not speculative — CLAUDE.md's MVP feature 1 literally reads "Interactive map of races — filterable by region, date, and sport type," and the tech stack section has already locked in Leaflet + OpenStreetMap as the map layer. This pattern is the decided plan, not a competing option.
2. The audience is geography-driven by design: global scope from day one, both recreational athletes planning "what can I travel to" and competitive athletes building a multi-region racing calendar — geography is a primary axis for this specific decision, exactly matching map-first's fit condition.
3. The scale-breakdown risk (map clutter without clustering) doesn't apply yet — MVP data is hand-seeded via SQL, likely tens to low hundreds of races, well within the range where a map stays legible with no clustering logic needed (validated against ocrbase/AllTrails in the Visual observations section above).

**Second-best, under condition X = the athlete already has firm constraints (a specific date window and/or sport type) rather than browsing by location: Faceted filter + browse (1).**
Once someone knows "HYROX, October, anywhere in Western Europe," panning a map to find pins is slower than a filtered list — this is exactly why both ocrbase and AllTrails (see Visual observations above) pair their map with a list/filter alternative rather than shipping map-only. CLAUDE.md's own feature line already licenses this — "filterable by region, date, and sport type" is filter language layered onto the map, not a separate feature — so building faceted filtering as the map's companion (list toggle or synced panel) is a natural extension, not a scope add.

**Doesn't fit: Personalized/algorithmic recommendation feed (2).**
It requires exactly what Onrace won't have at launch: behavioral history to rank against. A brand-new product with a hand-seeded catalog has a hard cold-start problem — there's no usage data for months. It also needs an ongoing ranking pipeline the stack doesn't budget for (Supabase + client-side anon key, no ML/backend layer), and it optimizes for passive engagement-time in a product explicitly not designed as a feed or social loop (per CLAUDE.md's "no social features" and free/no-ads scope) — the opposite of a free, no-monetization utility meant to get someone to a decision and out to registration.

## Race data availability (seeding)

Confirmed sources with structured, scrapable-by-hand event info for manual seeding:
- **hyrox.com/find-my-race** — dates, cities, official registration links.
- **spartan.com/en/deka** — DEKA FIT calendar, 2026 dates/cities confirmed for multiple US regions.
- **ocrbase.com** — community-submitted multi-format events (OCR/fitness racing/trail), could be a reference list to cross-check against, not a data source to scrape wholesale (respect their own aggregation effort/ToS — hand-curate from primary sources instead).
- Marathon majors (Boston, etc.) and DUV (ultras) have official calendars/databases but are lower priority than HYROX/DEKA for an MVP seed set aimed at the hybrid-athlete audience specifically.

**Gap**: no single source covers HYROX + DEKA + marathons + triathlons + ultras together — confirms manual curation (as already decided in `../CLAUDE.md`) is the only realistic MVP approach; no shortcut scrape target exists.

## Findings → decisions

- **Differentiation thesis confirmed**: the map+archive *combination* is the whitespace, not either half alone (see competitor table takeaway). Worth stating explicitly wherever Onrace's positioning gets written up next (concept/, or a future pitch doc).
- **Trust model validated**: required-source-link matches real elite-race verification practice (Boston). No change needed to `../CLAUDE.md`.
- **Suggested brief tweak**: soften the Boston Marathon example so it doesn't imply all elite hybrid races gate entry on submitted times — HYROX Worlds is placement-based, not time-based. Low priority, cosmetic.
- **Seed-data starting point**: prioritize HYROX (hyrox.com) and DEKA (spartan.com/en/deka) official calendars first for MVP seeding — they're the most hybrid-audience-specific and have the cleanest official sources; layer in a smaller set of major marathons/triathlons/ultras afterward rather than trying to cover all five sport types equally at launch.
- **Open, not yet decided**: whether to track Strava's new Events tab as a competitive risk if it expands beyond running/cycling into HYROX/DEKA territory — revisit later, not blocking MVP.

## Next steps

1. ~~Capture reference screenshots into `screens/` for the products in the table above~~ — done 2026-09-02 (see Visual observations above). Remaining gap: account-gated personal views (Athlinks claimed-results history, AllTrails "Completed" log, Strava Events tab) need a logged-in test account to capture.
2. Low-cost qualitative pass: skim App Store reviews for RoxFit/RoxMatchUp/HYBRD/HybridAF for recurring user complaints, before deciding whether primary interviews are worth the time given the 2-month MVP timeline.
3. Once taxonomy + differentiation thesis feel solid, move into `../wireframes/`.
