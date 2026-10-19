Source: Mobbin instead of Refero — Onrace is a mobile app and the research.md benchmarks are mobile products.

# Visual references

Lesson 6, step 1, 2026-10-13. Collected on Mobbin (`search_screens`, iOS first) for the two concept screens: **Race browse** (base, `-empty`, `-error`, `-loading`; filtered = base page with active chips) and **Results list** (base, `-empty`, `-error`, `-loading`). Map view is out of scope.

**What these references are for:** techniques to borrow, not a look to copy. One product is the base and two others each lend one or two techniques you can point at.

**How to read the values:**
- Mobbin has no style data, so every color here was read off a compressed screenshot preview. It's marked **[~]** (approximate) and is never an exact value.
- Every typeface is a guess from letterforms, marked **[?]**.
- A persona or job claim not traced to `research/personas.md` or `research/jtbd.md` is marked **[?]**.

**Guardrail (applies to everything below):** the artifact-page palette (the `#0b0c0e` / `#ff4d2e` family), `src/style.css` and the wireframe grays are not inputs for the product's look. The ban is on those specific values, not on any hue: whether Onrace uses orange, or any other color, is an open taste decision. Separately, a reference's signature brand color (Strava's orange, LinkedIn's blue) isn't taken, because it belongs to another brand.

**Scope label (Lesson 6, steps 5–6 forbid changing screen text and structure):** every technique in § 4 is marked
- **visual only**: applies within the existing markup, by CSS alone; or
- **structural**: adds, splits or regroups elements. Structural techniques are listed in § 4c, Deferred to Lesson 7.

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
| Letterboxd | BENCHMARK 17/40, ASPIRATIONAL | **Yes (iOS)** | Looked at, not picked as a style (§ 4). |
| AllTrails | ASPIRATIONAL | **Yes (iOS)** | Looked at, not picked as a style (§ 4). |
| IRONMAN | ASPIRATIONAL | **No** | iOS search returned Future Pro, Garmin Connect, Strava. Skipped. |
| Athlinks | SOFT (web) | **No** | Web search returned only unrelated apps. Skipped. |
| Goodreads, Parkrun, World Athletics, My Race Results, DUV, Race Roster | various | **Not searched** | Lower priority under this step's rule (HARD tier and top benchmark scorers first). Still open if more references are needed. |

**Seen in results but not used:** Runna, pliability and Garmin Connect came up in name searches. research.md doesn't name them as competitors or benchmarks: Runna appears only as Strava's race-data source, Garmin only inside a RoxFit review. So they aren't substituted in. This includes Garmin Connect's "Verified Source" race list ([screen](https://mobbin.com/screens/25ab95f9-a80d-4bee-a01c-0e5d1dd67898)), which is close to our topic.

**The consequence:** no HARD-tier product is on Mobbin. Every Mobbin reference below comes from a benchmark or aspirational product, and none is hybrid-racing branded. The HARD tier is covered instead from the Lesson 1 screenshots in `../research/screens/` (§ 4b).

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
- **One saturated accent:** orange ~#FC5200 [~], on the active tab, PR badges, the date-tile band and primary pills. **Not taken: it's Strava's signature brand color.** The reason is that it belongs to another brand, not that orange is banned; whether Onrace uses any orange is an open taste decision.
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
- **Color on data only:** green ~#00E054 [~] for star ratings and orange ~#FF8000 [~] for the "liked" heart. The tab bar is slate with a blue active icon ~#40BCF4 [~]. These are Letterboxd's own brand colors, so they aren't taken.
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

Two styles: one base and one donor, plus one hybrid-racing source from the Lesson 1 screenshots (§ 4b). Letterboxd is documented below as not picked. AllTrails is documented above but not picked. Its strongest techniques are photo-led cards (Onrace has no race imagery, and content images are deferred in `../wireframes/_conventions.md` § 7) and the floating Map pill (map view is out of scope). Its one leftover technique, the dot-separated meta line, is already covered by Strava's card.

### Base: Strava

- **Why it's the base:**
  - It's tied for the top BENCHMARK score (23/40) and is the only sports product of the four.
  - It has screens for both of our concept screens: an event list and a performance record.
- **What "base" means here:** the structure and type hierarchy, **not the color**. Its orange is Strava's signature brand color, so it isn't carried over. Onrace may still use an orange of its own; that's an open taste decision.
- **Light/dark:** light by default, with a dark mode that keeps the same structure ([e691c172](https://mobbin.com/screens/e691c172-0756-44c2-a5a2-35ae7eed1269)). That suggests the structure survives either theme decision.

| Technique (pointable) | Scope | Mobbin | Onrace screen | Persona worry / job it addresses |
|---|---|---|---|---|
| **The date leads the race card, in its own left column.** Strava sets a fixed-width tile on the left, with the name and meta to its right. Card radius ~12px [~]. | **Visual only (reduced form).** Checked `wireframes/race-browse.html`: each card already holds the date, as one `<time>` ("27 Sep 2026") inside `<p class="card-meta">` after the sport tag. CSS alone can pull that `<time>` into a left column (`display: contents` on `.card-meta`, a grid on `.card-link`) and let it wrap in a narrow box, with the first line ("27") set larger via `::first-line` **[?]** (untested). Strava's full tile isn't possible this way: there's no weekday in the markup, and the month isn't its own element, so it can't get its own band. Those parts are in § 4c. | [cb844353](https://mobbin.com/screens/cb844353-6828-40e9-9aff-bf37ffe1b302) | Race browse cards | Primary persona: "see what's coming up … so that I can plan my season instead of finding out about races too late" (`../research/jtbd.md` → Related job 1). Reading the date first serves season planning. That it scans faster than a date inside the meta line is **[?]**. |
| **The finish time is the row's largest, boldest figure.** Strava sets its stat values about 1.5× the size of their labels [~], bold. | **Visual only.** Checked `wireframes/results-list.html`: `<span class="finish-time">` already sits in `.card-top` next to the race name, so its size and weight are CSS. Strava's gray label above the value ("Moving Time") has no equivalent element in the row, so that part is structural (§ 4c). | [125cbc4d](https://mobbin.com/screens/125cbc4d-55cc-4abc-82d0-4ff489ed616e) | Results list rows (finish time) | Qualifying-Time Archivist: "pull that proof up quickly" (`jtbd.md` → Related job 4). The finish time is the fact being proved, so it gets the largest type in the row. Primary persona's emotional job, "be recognized as what I actually am — a hybrid athlete" (`jtbd.md` → Emotional): performance figures set as the hero content. |
| **The empty state's button weight follows its cause.** A filled pill when the empty state's action creates something ("Create an event"). An outlined pill when it recovers from filtering ("Adjust Filters"). Both with a bold title and one plain line. | **Visual only.** The markup already makes the distinction: `results-list-empty.html` has `<a class="state-action">` ("Log your first result"), and `race-browse-empty.html` has `<button class="state-action secondary">` ("Clear all filters"). Only the styling changes. | [b6641647](https://mobbin.com/screens/b6641647-d40e-49b3-a73a-56f2a11e5c98), [0ebb31b2](https://mobbin.com/screens/0ebb31b2-336e-4b06-b298-bbdf271d5598) | Results list `-empty` (filled **Log your first result**); Race browse `-empty` (outlined **Clear all filters**) | Archivist: "log the result … so that I have proof ready" (`jtbd.md` → Related job 3); the empty archive's one way forward is logging. Race browse `-empty`: `jtbd.md` → Hypothesis 7 **[?]** (a filter that lands on "no races match"). |

### Donor: LinkedIn (licenses and certifications), source-line logic only

- **Light/dark:** light.
- **Why picked:** it's the other 23/40 BENCHMARK scorer, and the one whose proof is an external link, the same shape as Onrace's trust model (`../CLAUDE.md` → Result trust model).
- **What's taken: the logic of the source line only, not its styling.** The designer finds LinkedIn's look corporate and dated (`concept.md` → Designer's taste). So its gray, its type and its link glyph aren't carried over; only the arrangement is: the proof as its own quieter line under the claim, not a badge.

| Technique (pointable) | Scope | Mobbin | Onrace screen | Persona worry / job it addresses |
|---|---|---|---|---|
| **The source sits on its own line under the claim, not as a badge** (logic only). LinkedIn shows it as a gray domain with an external-link glyph; that styling isn't taken. The claim (title) is bold. The proof is a quieter meta line beneath it ("blogs.microsoft.com"). Nothing is pinned to the title or avatar. | **Visual only.** `results-list.html` already has `<p class="proof-label">` on its own line under the meta line. The external-link glyph is visual only if drawn with CSS `::before`; adding an SVG element would be structural. | [2e873a3b](https://mobbin.com/screens/2e873a3b-3ac8-4bca-b726-92de277571ed), [a26e38b8](https://mobbin.com/screens/a26e38b8-aee7-41eb-a0b0-4f023d37ec08) | Results list rows and Result detail: "Self-reported · via \<domain\>" | Primary persona's trust trigger: a product that "visibly labels 'self-reported + source-linked' would be *more transparent than what they're used to*" (`../research/personas.md` → Primary → Trust triggers). Archivist's trust trigger: Boston "accepts a link or certificate as sufficient proof" (`personas.md` → Secondary → Trust triggers). Social job: "I want the proof itself to stand on its own" (`jtbd.md` → Social). |
| **What not to take:** the shield badge and "Verified by Persona". | n/a | [f8fa87dc](https://mobbin.com/screens/f8fa87dc-3036-493f-8cee-9475e12ed26a) | n/a | `../voice.md` principle 1; `research.md` BENCHMARK mechanism 2. |

### Documented, not picked: Letterboxd (diary)

- **Light/dark:** dark.
- **Why not picked:** "Designer finds the diary unclear: dense dark list where it's not obvious what matters." (`concept.md` → Designer's taste.)
- **Its techniques, kept for the record only (not used in Lesson 6 or deferred to Lesson 7):**
  - **Color only on the data, never on the chrome.** The background, rows and type are neutral slate; saturated color appears only on the ratings and the like-heart. Would have been visual only. [483648e0](https://mobbin.com/screens/483648e0-d2c3-47ed-9c05-384c4d078d49), [37003650](https://mobbin.com/screens/37003650-95a8-4b42-9c41-47a1e2ada51d). No persona source **[?]**.
  - **Month-grouped log with a day box.** A full-width uppercase month band ("OCTOBER 2025") heads each group. Each row starts with a small bordered square holding the day number, then the title (bold) and the year (lighter), then one data line. Flat rows, hairline separators, ~4px radius [~]. Would have been structural: it adds month headers and needs the day as its own element. [483648e0](https://mobbin.com/screens/483648e0-d2c3-47ed-9c05-384c4d078d49). Served the Archivist's "pull that proof up quickly" (`jtbd.md` → Related job 4); recall by date is **[?]**.

### 4b. Hybrid-racing products (Lesson 1 screenshots, not Mobbin)

None of the HARD tier is on Mobbin (§ 1), but `../research/screens/` holds screenshots of all five from the 2026-09-02 pass.

**What these screenshots are:** mostly marketing websites and App Store listings, not the apps themselves.
- RoxFit and RoxConnect show their apps only as phone mockups on their websites.
- RoxMatchUp's App Store screenshots are the only real in-app UI in the set.
- ocrbase and fitnessracingcalendar are web products, so their pages are the product.

| Product | Screenshot | Light/dark | Color amount | Type character |
|---|---|---|---|---|
| RoxFit | `../research/screens/roxfit-how-it-works.png`, `../research/screens/roxfit-home.png` | **Dark.** Near-black ~#0F0F0D [~] with an olive-yellow glow. The app mockups are dark gray ~#1C1C1C [~] cards. | **One loud accent, small areas.** Yellow ~#FFE600 [~] only on the selected pill and the small uppercase eyebrow labels ("PACEME", "ON YOUR WRIST"). The "Ultra" waitlist page swaps this for violet ~#9B8CF2 [~]. | Heavy geometric sans for headlines, tight [?]. The wordmark is condensed, letterspaced capitals [?]. The eyebrows are small, wide-tracked uppercase. |
| RoxConnect | `../research/screens/roxconnect-home.png` | **Dark.** Pure black ~#000000 [~], with dark-gray ~#0E0E0E [~] cards. | **Almost none.** White and gray type, white pill buttons. Orange appears only inside the app mockups, on small controls. | Neutral grotesque, Inter-like [?]. Big bold headlines, light gray body. |
| RoxMatchUp | `../research/screens/roxmatchup-appstore.png` | **Dark.** Slate ~#2D303C [~]. | **Medium.** Yellow ~#F5DF3A [~] on titles, outlined buttons and tags, and the chat bubbles. | Bold rounded sans for screen titles [?]. Dense, small body text. |
| fitnessracingcalendar.com | `../research/screens/fitnessracingcalendar-home.png` | **Light page, dark card heads.** Warm off-white ~#F5F4EF [~]. Each card has a near-black head ~#171712 [~] over a white body. | **One accent, used a lot.** Lime ~#C8F03C [~] on every card's format chip and "Book now" button, plus olive-green links ~#5A7A00 [~]. "Sold out" is a pink chip ~#FDE2E2 [~] with red text. | Heavy, slightly condensed display grotesque for card titles [?]. The format chip is small, bold, wide-tracked uppercase ("DEKA FIT", "WILD HYBRID"). The body is a plain grotesque [?]. |
| ocrbase.com | `../research/screens/ocrbase-events-list.png`, `../research/screens/ocrbase-home.png` | **Light.** White, with a gray header ~#ECEFF0 [~]. | **Low.** Teal ~#1ABC9C [~] links (underlined race titles), gray tag chips. | Generic web sans, Inter-like [?]. Reads as a default framework theme, not a brand. |

**Tally:** three dark (RoxFit, RoxConnect, RoxMatchUp) and two light (fitnessracingcalendar, ocrbase), though fitnessracingcalendar puts a dark head on every card. Across all five, color is one accent on small, high-signal elements, not a palette.

**Technique taken: the format as a small uppercase chip with a high-contrast fill.** Seen in fitnessracingcalendar's card chips ("DEKA FIT") and RoxFit's eyebrows.

- **Scope: visual only.** Every Race browse card and Results list row already has `<span class="sport-tag">` (HYROX, DEKA, Marathon …). Uppercase, letterspacing and fill are CSS (`text-transform`); the text in the markup doesn't change.
- **Open question [?]:** whether CSS uppercase sits well with `../voice.md` principle 4, "Every format by its own name". The name is unchanged, but "Half marathon" would render as "HALF MARATHON".
- **Persona worry:** the Primary persona's "see what's coming up in the formats I actually care about" (`../research/jtbd.md` → Related job 1), so the format reads at a glance. Also the Emotional job, "recognized as what I actually am — a hybrid athlete" (`jtbd.md` → Emotional), since the format chip is the most hybrid-racing-native element in this set. That it reads as "for hybrid athletes" to real users is **[?]**.

**Anti-reference: what we don't take.**
- **Big-number stat strips.** RoxConnect's "+499,900 active competitors globally / +80 countries". These are hype numbers and crowd words, both on `../voice.md`'s Forbidden list.
- **Pure black plus one hot accent.** RoxConnect's look, and the fastest route back to the banned artifact-page values (`#0b0c0e` / `#ff4d2e`) by habit. If Onrace goes dark, its values have to be chosen fresh, not drifted into.
- **Price and booking state on the card.** fitnessracingcalendar's "From £80", "Book now" and pink "Sold out". Onrace has no price data and links out to register only (`../CLAUDE.md` → Out of scope).
- **The tag-soup format list.** ocrbase's gray chips ("DEKA MILE - Affiliate", "DEKA STRONG - Affiliate") repeat in every row, so no chip stands out.
- **Marketing-tone card copy** ("Salt Lake City, are you ready?"). That's catalog data, not ours, but it shows how quickly a race card turns into hype.

### 4c. Deferred to Lesson 7 (structural)

Lesson 6 steps 5–6 forbid changing screen text and structure, so these wait.

| Technique | From | Why it's structural | Onrace screen |
|---|---|---|---|
| **The full date tile:** the month on its own colored band, plus a weekday line. | Strava, [cb844353](https://mobbin.com/screens/cb844353-6828-40e9-9aff-bf37ffe1b302) | It splits the single `<time>` into month and day elements, and adds weekday text that isn't in the markup. | Race browse cards |
| **A gray label above the finish time** ("Finish time"). | Strava, [125cbc4d](https://mobbin.com/screens/125cbc4d-55cc-4abc-82d0-4ff489ed616e) | Adds a label element (and text) the Results list row doesn't have. | Results list rows |
| **A dark card head** holding the format chip and title, over a light body with the date and location. | fitnessracingcalendar, `../research/screens/fitnessracingcalendar-home.png` | It regroups the card: in `race-browse.html` the sport tag sits in `.card-meta` beside the date, not with the title. | Race browse cards |

---

## 5. What was checked

- **Sources read:**
  - `research/research.md`: the COMPETITORS tiers, the BENCHMARK table and mechanisms, and where Runna and Garmin are mentioned
  - `research/personas.md`: the Primary and both Secondary personas, their trust triggers and pains
  - `research/jtbd.md`: Related jobs 1–4, Emotional and Social jobs, Hypotheses 1–7
- **Searches:** the products in § 1, with platform iOS (web only for the web-only HARD products and Athlinks). For each product used, I read the returned previews before describing them, and kept only screens whose `app_name` matched the product.
- **Links:** every Mobbin link here is the `mobbin_url` the tool returned.
- **Hybrid-racing screenshots (§ 4b):** viewed `roxfit-home.png`, `roxfit-how-it-works.png`, `roxconnect-home.png`, `roxmatchup-appstore.png`, `fitnessracingcalendar-home.png` (whole page plus a cropped section of cards) and `ocrbase-events-list.png` in `research/screens/`, alongside each product's `.md` note there.
- **Scope labels (§ 4):** checked against the current markup of `wireframes/race-browse.html` (race card), `wireframes/results-list.html` (result row), `wireframes/results-list-empty.html` and `wireframes/race-browse-empty.html` (state actions).

## 6. Still unknown

- **HARD-tier app UI.** The HARD tier is covered only by marketing sites, App Store screenshots and web pages (§ 4b), all from 2026-09-02. The real in-app UI of RoxFit and RoxConnect hasn't been seen beyond website mockups.
- **Visual-only techniques untested.** The reduced date column (`display: contents`, `::first-line`) is **[?]** until it's tried in the wireframe CSS.
- **Light vs. dark: decided, dark.** It's the designer's decision (see `concept.md` → Designer's taste), not inherited from the brief or the artifact pages. For the record: three of the four Mobbin references are light-first, and three of the five hybrid-racing products (§ 4b) are dark.
- **Exact values.** Every hex is [~] from compressed previews, and every typeface is [?]. Nothing here is a token.
- **Accent color.** None of the references' brand accents are taken (Strava orange, LinkedIn blue/green, Letterboxd green/orange, and in § 4b RoxFit yellow and fitnessracingcalendar lime). Only the specific artifact-page values are banned, so Onrace's accent, orange included, is an open taste decision.
- **Untested persona links.** Whether the date-first card actually helps the personas is **[?]**. No user research exists (`personas.md`, opening note).
- **Products not searched:** Goodreads, Parkrun, World Athletics, My Race Results, DUV, Race Roster.

---

## 7. Photos

Lesson 6, step 3, 2026-10-13. These photos demonstrate each direction's card in `directions.html`. They aren't product content. Every photo below was downloaded and looked at before it was used, and each one is free under the Unsplash License (no Unsplash+). The page loads them from `images.unsplash.com` at `?w=900&q=75&fm=jpg`, and all three loaded in the browser check.

**Scope reminder (step 5):** neither `wireframes/race-browse.html` nor `wireframes/results-list.html` has an image placeholder. Race cards and result rows are text only (`_conventions.md` § 1, "No images"), and the one placeholder region is Race browse's `.map-placeholder`, which is the map view and out of scope. So in step 5 these photos have no slot to fill, and adding one would be structural (§ 4c).

### Used in `directions.html`

| Direction | Subject | Photographer | Unsplash page | Image URL |
|---|---|---|---|---|
| 1 · Chalk on rubber | A row of athletes leaning on loaded sleds at the start line of an indoor fitness race, with the crowd behind the barriers. Functional-fitness racing. Shown in grayscale. | Leona Lee | https://unsplash.com/photos/athletes-compete-by-pushing-weighted-sleds-indoors-xGzdmd5lB6I | https://images.unsplash.com/photo-1743993414654-0be2b73a9620 |
| 2 · Format colors | A racer in a headband runs up a steep wooden obstacle wall on an outdoor course, motion-blurred. OCR. | Nikita Pishchugin | https://unsplash.com/photos/man-climbing-a-wooden-obstacle-during-a-race-yNUBSKvl5d8 | https://images.unsplash.com/photo-1776938023428-60ddf175a2d1 |
| 3 · Floodlight | A trail runner with a hydration vest on a mountain path, with glaciated peaks behind. Trail / ultra. Paired with the UTMB card, but the location isn't confirmed by the source. | Brian Metzler | https://unsplash.com/photos/man-in-white-shirt-and-blue-shorts-running-on-brown-ground-between-green-grass-during-daytime-nmWQ2SKvj5M | https://images.unsplash.com/photo-1498581444814-7e44d2fbe0e2 |

### Added 2026-10-13 for Direction A's Race browse preview (every card has a photo)

| Card | Subject | Photographer | Unsplash page | Image URL |
|---|---|---|---|---|
| Berlin Marathon | Runners filling a tree-lined city avenue during a road race, seen from above. The city isn't identified, so the photo is illustrative, not Berlin. | Mārtiņš Zemlickis | https://unsplash.com/photos/people-running-on-road-during-daytime-NPFu4GfFZ7E | https://images.unsplash.com/photo-1452626038306-9aae5e071dd3 |
| HYROX London | Same sled-push start line as Direction 1 above. | Leona Lee | https://unsplash.com/photos/athletes-compete-by-pushing-weighted-sleds-indoors-xGzdmd5lB6I | https://images.unsplash.com/photo-1743993414654-0be2b73a9620 |
| HYROX Dallas | An athlete pushing a sled down a HYROX lane, with a HYROX-branded barrier. Listed below as not used in step 3; used here because it's a HYROX race's own card. | Mathieu Improvisato | https://unsplash.com/photos/athletes-compete-in-a-hyrox-race-event-v4P_DDrpRsk | https://images.unsplash.com/photo-1757147517623-ee9a76c9ead2 |
| Boston Marathon | Road-race runners wearing race bibs, legs and shoes mid-stride. The city isn't identified, so the photo is illustrative. | Miguel A Amutio | https://unsplash.com/photos/people-running-on-gray-asphalt-road-during-daytime-QDv-uBc-poY | https://images.unsplash.com/photo-1613936360976-8f35cf0e5461 |

Also downloaded and viewed, not used: a close-up of runners' legs on a road race (Miguel A Amutio, https://unsplash.com/photos/people-running-on-gray-asphalt-road-during-daytime-Y0woUmyxGrw), and a motion-blurred runner's legs (Pierre-Antoine Franck, https://unsplash.com/photos/runners-in-motion-during-a-race-W2pBsQaT6FQ). Both were too abstract to place a race.

### Step 5: the photos on Race browse (`wireframes/race-browse.html`), 2026-10-14

Each card has a photo inside it (the race card anatomy in `concept.md`), shown black and white at 3:1. Each crop was checked at 390 wide. `alt=""`: the photos are illustrative, and the card's title already names the race inside the same link.

| Card | Photo | Photographer | Unsplash page | Image | Crop at 3:1 |
|---|---|---|---|---|---|
| Berlin Marathon | City road race seen from above (illustrative; not Berlin) | Mārtiņš Zemlickis | https://unsplash.com/photos/people-running-on-road-during-daytime-NPFu4GfFZ7E | `photo-1452626038306-9aae5e071dd3` | `photo--mid`: the runners fill the band |
| HYROX London | Sled-push start line | Leona Lee | https://unsplash.com/photos/athletes-compete-by-pushing-weighted-sleds-indoors-xGzdmd5lB6I | `photo-1743993414654-0be2b73a9620` | `photo--low`: the athletes on the sleds |
| HYROX Dallas | Athlete pushing a sled in a HYROX lane | Mathieu Improvisato | https://unsplash.com/photos/athletes-compete-in-a-hyrox-race-event-v4P_DDrpRsk | `photo-1757147517623-ee9a76c9ead2` | `photo--mid`: the athlete and the lane |
| DEKA STRONG Chicago | **New.** An athlete on an air bike at a functional-fitness competition, a judge beside her (Copa Sur, no HYROX branding) | Jose Valenzuela | https://unsplash.com/photos/athletes-cycle-intensely-during-a-competition-with-judges-watching-rHDNRphQqIk | `photo-1778346612273-93520f4b7918` | `photo--lower` (74%, changed 2026-10-14): the athlete's back, the air bike and the judge. The other event's "COPA SUR" banner is out of frame; the athlete's head is cropped. At 70% the banner's edge still shows |
| Boston Marathon | Road-race runners wearing bibs (illustrative; not Boston) | Miguel A Amutio | https://unsplash.com/photos/people-running-on-gray-asphalt-road-during-daytime-QDv-uBc-poY | `photo-1613936360976-8f35cf0e5461` | `photo--high` (top edge): the bibs; `--mid` showed only legs |
| Spartan Race Beast — Killington | Racer running up an obstacle wall | Nikita Pishchugin | https://unsplash.com/photos/man-climbing-a-wooden-obstacle-during-a-race-yNUBSKvl5d8 | `photo-1776938023428-60ddf175a2d1` | `photo--center`: head to thighs; `--mid` cut off the head |
| UTMB — Ultra-Trail du Mont-Blanc | Trail runner, glaciated peaks behind (*replaced 2026-10-20 by a generated photo, see Step 4 below*) | Brian Metzler | https://unsplash.com/photos/man-in-white-shirt-and-blue-shorts-running-on-brown-ground-between-green-grass-during-daytime-nmWQ2SKvj5M | `photo-1498581444814-7e44d2fbe0e2` | `photo--mid`: the runner and the mountains |

**Viewed and rejected for DEKA** (both show HYROX equipment or come from a HYROX event, and on a DEKA card they would give it HYROX's look, against attribute 3):
- athletes preparing for a fitness competition, under a HYROX wall-ball station (Mathieu Improvisato): https://unsplash.com/photos/athletes-preparing-for-a-fitness-competition-seOGJ4ZOOew
- "Athletes competing in a fitness competition with weights and equipment", captioned Hyrox Hong Kong 2025 (Leona Lee): https://unsplash.com/photos/athletes-competing-in-a-fitness-competition-with-weights-and-equipment-5ADpBLL3240. Ruled out from its page caption; not downloaded.

### Step 4: our own visuals (Lesson 7, 2026-10-20)

**Generated, not photographed.** Our own photos are generated with ChatGPT image generation: illustrations of each format, **not taken at the named race**. A UTMB card's photo shows a trail ultra on a glaciated ridge, not UTMB itself. The alt text stays as it is (`alt=""`): the photos are illustrative, and the card's title already names the race inside the same link. Tool, workflow, the style block, the 7 scene prompts and the check of each file: `visuals/README.md`.

**Checked 2026-10-20:** 1 of 7 passed. The other six show clothing logos (swooshes), bib numbers or printed text at full size. They aren't used and wait in `visuals/incoming/` for a regenerate with the text fix.

| Card | Photo | Source | File | Crop at 3:1 |
|---|---|---|---|---|
| UTMB — Ultra-Trail du Mont-Blanc | **Replaced.** A single trail runner on a rocky ridge, snow-capped peaks and a glacier behind (generated; not UTMB) | ChatGPT image generation, scene `trail-ultra-ridge-1` | `visuals/trail-ultra-ridge-1.jpg` | `photo--low` (50% 72%, re-checked): the runner centered in the band; `--mid` left her low in the frame |

Berlin Marathon, HYROX London, HYROX Dallas, DEKA STRONG Chicago, Boston Marathon and Spartan Race Beast — Killington keep their Unsplash photos (Step 5 table above) until their generated images pass. `directions.html` and `directions-round-1.html` keep their Unsplash photos as history.

### Downloaded, not used

| Subject | Photographer | Unsplash page | Why not used |
|---|---|---|---|
| A HYROX sled-push lane, with a HYROX-branded barrier and roxzone behind | Mathieu Improvisato | https://unsplash.com/photos/athletes-compete-in-a-hyrox-race-event-v4P_DDrpRsk | On topic, but the HYROX branding fills the frame and would make one format set the look (attribute 3). |
| Runners from behind on an indoor HYROX run lane, with Red Bull and HYROX branding | Mathieu Improvisato | https://unsplash.com/photos/athletes-running-in-an-indoor-race-event-Nqfj4YYMXVc | Same reason: brand-heavy, and it reads as a crowd (`voice.md` principle 5). |
| A racer on a rope climb over water, shot through a blurred foreground | Nikita Pishchugin | https://unsplash.com/photos/person-rappelling-down-a-rope-over-water-W50GgZvvPa8 | OCR, but the subject is small and the frame is dominated by blur. |
| Athletes preparing for a fitness competition | Mathieu Improvisato | https://unsplash.com/photos/athletes-preparing-for-a-fitness-competition-seOGJ4ZOOew | Downloaded as a backup but not opened, so its subject is only Unsplash's alt text. |
| A man on a trail | Eddy Billard | https://unsplash.com/photos/man-on-trail-iXU_zV0S62o | Downloaded as a backup but not opened, so its subject is only Unsplash's alt text. |
