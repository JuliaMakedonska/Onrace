Source: Mobbin instead of Refero — Onrace is a mobile app and the research.md benchmarks are mobile products.

# Visual references

Lesson 6, step 1, 2026-10-13. Collected on Mobbin (`search_screens`, iOS first) for the two concept screens: **Race browse** (base, `-empty`, `-error`, `-loading`; filtered = base page with active chips) and **Results list** (base, `-empty`, `-error`, `-loading`). Map view is out of scope.

**What these references are for:** techniques to borrow, not a look to copy. One product is the base and two others each lend one or two techniques you can point at.

**How to read the values:**
- Mobbin has no style data, so every color here was read off a compressed screenshot preview. It's marked **[~]** (approximate) and is never an exact value.
- Every typeface is a guess from letterforms, marked **[?]**.
- A persona or job claim not traced to `research/personas.md` or `research/jtbd.md` is marked **[?]**.

**Guardrail (applies to everything below):** the artifact-page palette (the `#0b0c0e` / `#ff4d2e` family), `src/style.css` and the wireframe grays are not inputs for the product's look. Where a reference's own color falls into that family, it's flagged and not taken.

---

## 1. Which research.md products are on Mobbin

Searched in priority order: the HARD tier first, then the BENCHMARK's highest scorers on ownership credibility (Strava 23/40, LinkedIn certifications 23/40, Chess.com FIDE field 21/40), then other products research.md names.

| Product | research.md tier | On Mobbin? | Notes |
|---|---|---|---|
| RoxFit | HARD | **No** | iOS search by name returned only other apps (Runna, pliability, Fixtured, Alma, DAZN). Skipped. |
| RoxConnect | HARD | **No** | iOS search by name returned only unrelated apps. Skipped. |
| RoxMatchUp | HARD | **No** | iOS search by name returned only unrelated apps. Skipped. |
| ocrbase.com | HARD (web only) | **No** | Web search returned only unrelated apps. Skipped. |
| fitnessracingcalendar.com | HARD (web only) | **No** | Web search returned only unrelated apps. Skipped. |
| Strava | SOFT, and BENCHMARK 23/40 | **Yes (iOS)** | Used. |
| LinkedIn (certifications) | BENCHMARK 23/40 | **Yes (iOS)** | Used. |
| Chess.com (FIDE field) | BENCHMARK 21/40 | **No** | Two iOS queries returned Duolingo, Alan, Quizlet, Lyft and others. Skipped. |
| Letterboxd | BENCHMARK 17/40, ASPIRATIONAL | **Yes (iOS)** | Used. |
| AllTrails | ASPIRATIONAL | **Yes (iOS)** | Looked at, not picked as a style (§ 4). |
| IRONMAN | ASPIRATIONAL | **No** | iOS search returned Future Pro, Garmin Connect, Strava. Skipped. |
| Athlinks | SOFT (web) | **No** | Web search returned only unrelated apps. Skipped. |
| Goodreads, Parkrun, World Athletics, My Race Results, DUV, Race Roster | various | **Not searched** | Lower priority under this step's rule (HARD tier and top benchmark scorers first). Still open if more references are needed. |

**Seen in results but not used:** Runna, pliability and Garmin Connect came up in name searches. research.md doesn't name them as competitors or benchmarks: Runna appears only as Strava's race-data source, Garmin only inside a RoxFit review. So they aren't substituted in. This includes Garmin Connect's "Verified Source" race list ([screen](https://mobbin.com/screens/25ab95f9-a80d-4bee-a01c-0e5d1dd67898)), which is close to our topic.

**The consequence:** no HARD-tier product is on Mobbin. Every reference below comes from a benchmark or aspirational product, and none is hybrid-racing branded. The brief's "in the spirit of HYROX/CrossFit" (`../CLAUDE.md` → Design / brand tone) has no visual reference here yet (§ 6).

---

## 2. Visual language per product

### Strava: light (a dark mode exists)

- **Home feed:** [ba77b254](https://mobbin.com/screens/ba77b254-e2a1-4de3-88f0-2667b828fede), [b3fba3c0](https://mobbin.com/screens/b3fba3c0-9ad3-4cc7-ac17-e6bd4d136813)
- **Activity detail:**
  - light: [125cbc4d](https://mobbin.com/screens/125cbc4d-55cc-4abc-82d0-4ff489ed616e)
  - the same screen in dark mode: [e691c172](https://mobbin.com/screens/e691c172-0756-44c2-a5a2-35ae7eed1269)
- **Event detail:** [f157cfb3](https://mobbin.com/screens/f157cfb3-2d58-4acd-a8f6-994d973fb678)

**Observed:**
- **Background:** white with pale-gray section bands ~#F2F2F2 [~]. Text is near-black ~#1A1A1A [~].
- **One saturated accent:** orange ~#FC5200 [~], on the active tab, PR badges, the date-tile band and primary pills. **It's in the forbidden `#ff4d2e` family, so Strava's color is not taken.**
- **Shapes:** cards have a ~12px radius [~] and a faint shadow. Buttons are fully rounded pills.
- **Type:** titles in a heavy grotesque sans, possibly a custom face [?]. Stats are set as a small gray label over a large bold number.
- **Density:** medium. Three stats to a row.
- **Dark mode:** near-black ~#121212 [~] with dark-gray cards ~#1E1E1E [~], and the accent unchanged.

### LinkedIn: light

- **Feed / search:** [fd47feea](https://mobbin.com/screens/fd47feea-bea4-4aff-ab5d-c371a2933da6)
- **Profile, activity:** [ed6c9c35](https://mobbin.com/screens/ed6c9c35-57a7-4c90-a61c-ca16bfb35a2b)
- **Profile, licenses and certifications:** [a26e38b8](https://mobbin.com/screens/a26e38b8-aee7-41eb-a0b0-4f023d37ec08)

**Observed:**
- **Background:** white, with warm-gray gaps between sections ~#F4F2EE [~]. Text is near-black ~#1F1F1F [~].
- **Accents:**
  - links and secondary buttons: blue ~#0A66C2 [~]
  - selected filter chips: dark green ~#01754F [~]
- **Shapes:** almost no cards. Sections are full-width blocks separated by the gray gaps, with hairline rules inside them.
- **Type:** a system-like sans, likely SF Pro on iOS [?]. Section titles ~20pt bold [~], body ~15pt [~], meta lines gray.
- **Density:** high and text-led.

### Letterboxd: dark

- **Diary:** [483648e0](https://mobbin.com/screens/483648e0-d2c3-47ed-9c05-384c4d078d49)
- **Activity:** [5b928f6a](https://mobbin.com/screens/5b928f6a-7415-491e-8974-b8b70a719d70)
- **Review detail:** [37003650](https://mobbin.com/screens/37003650-95a8-4b42-9c41-47a1e2ada51d)

**Observed:**
- **Background:** blue-tinted slate ~#14181C [~], with lighter slate row bands ~#20262D [~]. Text is pale blue-gray ~#DDE3EA [~], and meta is mid slate ~#8899AA [~].
- **Color on data only:** green ~#00E054 [~] for star ratings and orange ~#FF8000 [~] for the "liked" heart. The tab bar is slate with a blue active icon ~#40BCF4 [~]. The heart's orange is amber, not the forbidden `#ff4d2e`, but it's still not taken.
- **Shapes:** small radii ~4px [~] on posters and day boxes. Rows are flat, with hairline separators.
- **Type:** a grotesque sans, possibly Graphik [?]. Titles bold, the year in a lighter gray beside them.
- **Density:** high. About ten rows per screen on the diary.

### AllTrails: light

- **Explore list:** [d5b73a33](https://mobbin.com/screens/d5b73a33-8e08-475b-8865-65f73e9744ed), [cac26e0b](https://mobbin.com/screens/cac26e0b-990e-4dab-aa58-862598867b45)
- **Photo card with route:** [87814f39](https://mobbin.com/screens/87814f39-6c9a-437a-8192-056b6acecdce)

**Observed:**
- **Background:** white, with dark forest-green text accents ~#1F3A1F [~]. A lime-green floating "Map" pill ~#A6E07E [~].
- **Shapes:** large photo cards with a ~16–20px radius [~].
- **Type:** a geometric-leaning sans [?].
- **Layout:** one dot-separated meta line under each title ("★ 4.7 · Moderate · 3.00 mi").
- **Density:** low, photo-led.

**Light/dark tally:** three light (Strava, LinkedIn, AllTrails), one dark (Letterboxd), and Strava ships both. The brief asks for "dark, intense" (`../CLAUDE.md` → Design / brand tone), but most of these references are light-first, so light vs. dark stays open (§ 6).

---

## 3. Concrete patterns

### 3a. Race / event card with date and location (→ Race browse)

- **Strava, Browse Events** ([cb844353](https://mobbin.com/screens/cb844353-6828-40e9-9aff-bf37ffe1b302)) and **Club Events, Past tab** ([264079d8](https://mobbin.com/screens/264079d8-5540-4548-b539-429c1b34bc54)).
  - **Card:** white, ~12px radius [~].
  - **Date tile on the left:** a colored band with the short month ("Jun"), a large day number below it ("3"), and the weekday ("Wed") under that.
  - **Right side:** the event name in bold, then two gray meta lines (sport and venue, then attendees).
  - The date is read before the name.
- **AllTrails, Explore** ([d5b73a33](https://mobbin.com/screens/d5b73a33-8e08-475b-8865-65f73e9744ed)): a photo card, then the title, then one dot-separated meta line (place · difficulty · distance).

### 3b. Result with a source (→ Results list, Result detail)

- **LinkedIn, Licenses and certifications** ([a26e38b8](https://mobbin.com/screens/a26e38b8-aee7-41eb-a0b0-4f023d37ec08)):
  - each entry is the issuer's square logo, then the title in bold, the issuer, "Issued Sep 2020", and "Credential ID …" in gray
  - the proof is meta text under the claim, not a badge on it
- **LinkedIn, company Certifications and pledges** ([2e873a3b](https://mobbin.com/screens/2e873a3b-3ac8-4bca-b726-92de277571ed)): each item is an external-link glyph, the title in bold, and **the source domain on its own gray line underneath** ("blogs.microsoft.com"). This is the closest observed match to Onrace's "Self-reported · via \<domain\>".
- **Counter-example, not to borrow: LinkedIn Verifications** ([f8fa87dc](https://mobbin.com/screens/f8fa87dc-3036-493f-8cee-9475e12ed26a), [c0bd805c](https://mobbin.com/screens/c0bd805c-c3bd-4257-b10a-149bc9ebfd80)). It uses a shield badge on the avatar and the words "Verified by Persona". Onrace can't claim that (`../voice.md` → principle 1, "Claim only what Onrace can know"; `../research/research.md` → BENCHMARK → mechanism 2, "never a checkmark implying Onrace vouches for it").

### 3c. Empty state with a primary action (→ Results list `-empty`, Race browse `-empty`)

- **Strava, Club Events, no upcoming** ([b6641647](https://mobbin.com/screens/b6641647-d40e-49b3-a73a-56f2a11e5c98)):
  - layout: a small outline icon, then a bold title "No upcoming events right now", then one gray line, then a **filled** pill "Create an event"
  - all centred in the content area, with the tab bar still visible
- **Strava, Browse Events, filtered to nothing** ([0ebb31b2](https://mobbin.com/screens/0ebb31b2-336e-4b06-b298-bbdf271d5598)):
  - layout: no icon, then a bold title "No events found", then "Try adjusting your filters", then an **outlined** pill "Adjust Filters"
  - the filter controls stay visible above it
- **Counter-example, not to borrow: Letterboxd, No reviews** ([f64404c2](https://mobbin.com/screens/f64404c2-85aa-45ea-8ef1-bdf469344c95)). It has a gray title, a joke line and no action. That conflicts with `../voice.md` (Microcopy → empty state; no motivational lines) and with `../flows.md`, where the Results list empty state has a call to action.

---

## 4. Picked styles

Three styles: one base and two donors. AllTrails is documented above but not picked. Its strongest techniques are photo-led cards (Onrace has no race imagery, and content images are deferred in `../wireframes/_conventions.md` § 7) and the floating Map pill (map view is out of scope). Its one leftover technique, the dot-separated meta line, is already covered by Strava's card.

### Base: Strava

- **Why it's the base:**
  - It's tied for the top BENCHMARK score (23/40) and is the only sports product of the four.
  - It has screens for both of our concept screens: an event list and a performance record.
- **What "base" means here:** the structure and type hierarchy, **not the color**. Its orange is in the forbidden family and is dropped.
- **Light/dark:** light by default, with a dark mode that keeps the same structure ([e691c172](https://mobbin.com/screens/e691c172-0756-44c2-a5a2-35ae7eed1269)). That suggests the structure survives either theme decision.

| Technique (pointable) | Mobbin | Onrace screen | Persona worry / job it addresses |
|---|---|---|---|
| **The date tile leads the race card.** A fixed-width tile on the left (short month on a band, a large day number, the weekday), with the name and meta to its right. Card radius ~12px [~]. Keep the shape; the band color will be our own. | [cb844353](https://mobbin.com/screens/cb844353-6828-40e9-9aff-bf37ffe1b302) | Race browse cards | Primary persona: "see what's coming up … so that I can plan my season instead of finding out about races too late" (`../research/jtbd.md` → Related job 1). Reading the date first serves season planning. That it scans faster than a date inside the meta line is **[?]**. |
| **Stat typesetting: a small gray label above a large bold value.** "Moving Time / 4:07", in a 2–3 column grid, with the value about 1.5× the label's size [~]. | [125cbc4d](https://mobbin.com/screens/125cbc4d-55cc-4abc-82d0-4ff489ed616e) | Results list rows (finish time), Result detail | Qualifying-Time Archivist: "pull that proof up quickly" (`jtbd.md` → Related job 4). The finish time is the fact being proved, so it gets the largest type in the row. Primary persona's emotional job, "be recognized as what I actually am — a hybrid athlete" (`jtbd.md` → Emotional): performance figures set as the hero content. |
| **The empty state's button weight follows its cause.** A filled pill when the empty state's action creates something ("Create an event"). An outlined pill when it recovers from filtering ("Adjust Filters"). Both with a bold title and one plain line. | [b6641647](https://mobbin.com/screens/b6641647-d40e-49b3-a73a-56f2a11e5c98), [0ebb31b2](https://mobbin.com/screens/0ebb31b2-336e-4b06-b298-bbdf271d5598) | Results list `-empty` (filled **Log result**); Race browse `-empty` (outlined **Clear all filters**) | Archivist: "log the result … so that I have proof ready" (`jtbd.md` → Related job 3); the empty archive's one way forward is logging. Race browse `-empty`: `jtbd.md` → Hypothesis 7 **[?]** (a filter that lands on "no races match"). |

### Donor 1: LinkedIn (licenses and certifications)

- **Light/dark:** light.
- **Why picked:** it's the other 23/40 BENCHMARK scorer, and the one whose proof is an external link, the same shape as Onrace's trust model (`../CLAUDE.md` → Result trust model).

| Technique (pointable) | Mobbin | Onrace screen | Persona worry / job it addresses |
|---|---|---|---|
| **The source sits on its own line under the claim, as a gray domain with an external-link glyph, not as a badge.** The claim (title) is bold. The proof is a quieter meta line beneath it ("blogs.microsoft.com"). Nothing is pinned to the title or avatar. | [2e873a3b](https://mobbin.com/screens/2e873a3b-3ac8-4bca-b726-92de277571ed), [a26e38b8](https://mobbin.com/screens/a26e38b8-aee7-41eb-a0b0-4f023d37ec08) | Results list rows and Result detail: "Self-reported · via \<domain\>" | Primary persona's trust trigger: a product that "visibly labels 'self-reported + source-linked' would be *more transparent than what they're used to*" (`../research/personas.md` → Primary → Trust triggers). Archivist's trust trigger: Boston "accepts a link or certificate as sufficient proof" (`personas.md` → Secondary → Trust triggers). Social job: "I want the proof itself to stand on its own" (`jtbd.md` → Social). |
| **What not to take:** the shield badge and "Verified by Persona". | [f8fa87dc](https://mobbin.com/screens/f8fa87dc-3036-493f-8cee-9475e12ed26a) | n/a | `../voice.md` principle 1; `research.md` BENCHMARK mechanism 2. |

### Donor 2: Letterboxd (diary)

- **Light/dark:** dark. It's the only dark reference found among the named products.
- **Why picked:** its diary is a personal, date-ordered log of things you did, the closest analogue to Results list. It also shows how a dark UI can keep color on the data rather than the chrome.

| Technique (pointable) | Mobbin | Onrace screen | Persona worry / job it addresses |
|---|---|---|---|
| **Month-grouped log with a day box.** A full-width uppercase month band ("OCTOBER 2025") heads each group. Each row starts with a small bordered square holding the day number, then the title (bold) and the year (lighter), then one data line. Flat rows, hairline separators, ~4px radius [~] on the small elements. | [483648e0](https://mobbin.com/screens/483648e0-d2c3-47ed-9c05-384c4d078d49) | Results list (denser and calmer than Race browse's cards: the contrast this lesson is after) | Archivist: "pull that proof up quickly … without scrambling to find it" (`jtbd.md` → Related job 4). Grouping by month matches remembering a race by when it was. That people recall races by date is **[?]**. |
| **Color only on the data, never on the chrome.** The background, rows and type are neutral slate. Saturated color appears only on the ratings and the like-heart. Our equivalent: color lands on the finish time or sport tag, not on headers or bars. | [483648e0](https://mobbin.com/screens/483648e0-d2c3-47ed-9c05-384c4d078d49), [37003650](https://mobbin.com/screens/37003650-95a8-4b42-9c41-47a1e2ada51d) | Both screens, as a color rule | No persona source. **[?]** It's a technique for "dark, intense" (`../CLAUDE.md` brand tone) and `../voice.md` principle 3 ("the look carries the energy"), not an answer to a persona worry. |

---

## 5. What was checked

- **Sources read:**
  - `research/research.md`: the COMPETITORS tiers, the BENCHMARK table and mechanisms, and where Runna and Garmin are mentioned
  - `research/personas.md`: the Primary and both Secondary personas, their trust triggers and pains
  - `research/jtbd.md`: Related jobs 1–4, Emotional and Social jobs, Hypotheses 1–7
- **Searches:** the products in § 1, with platform iOS (web only for the web-only HARD products and Athlinks). For each product used, I read the returned previews before describing them, and kept only screens whose `app_name` matched the product.
- **Links:** every Mobbin link here is the `mobbin_url` the tool returned.

## 6. Still unknown

- **No HARD-tier visuals.** RoxFit, RoxConnect, RoxMatchUp, ocrbase and fitnessracingcalendar aren't on Mobbin. The closest-audience products have no visual reference. Their App Store or website screenshots would need another source; `research/screens/` may already hold some from the 2026-09-02 pass (not checked in this step).
- **Light vs. dark.** The brief says dark. Three of the four references are light-first, and the one dark reference (Letterboxd) is a film app. Not decided.
- **Exact values.** Every hex is [~] from compressed previews, and every typeface is [?]. Nothing here is a token.
- **Accent color.** The base's accent is ruled out by the guardrail, and the donors' accents (LinkedIn blue/green, Letterboxd green/orange) aren't taken. Onrace's accent is fully open.
- **Untested persona links.** Whether the date-first card or the month-grouped log actually help the personas is **[?]**. No user research exists (`personas.md`, opening note).
- **Products not searched:** Goodreads, Parkrun, World Athletics, My Race Results, DUV, Race Roster.
