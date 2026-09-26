# Voice

How Onrace speaks. These principles govern every line in `microcopy.md`, and every new line gets checked against them.

**Context they're written for:** a hybrid athlete deciding whether a race is worth entering (`research/jtbd.md` → Main Job 1: "…so that I can compare them in one place"), and an athlete keeping official results they may later submit as proof for an elite race (`research/personas.md` → The Qualifying-Time Archivist: "Produce, on demand, a link or certificate from an official timing source as proof of a qualifying time"). In both, the product is useful only if it's believed. Credibility comes before cleverness.

**What they rest on:** desk research only: `CLAUDE.md`, `research/research.md` (including its Competitor language section, verbatim copy from RoxConnect, ocrbase, Athlinks and Strava, fetched 2026-09-26), `research/jtbd.md` and `research/personas.md`. No interviews exist yet (`research.md` → User research: "Not started"). So these are sourced rules, not user-validated ones. Where a principle leans on an inference rather than a sourced line, the explanation says so.

## Principles

### 1. Claim only what Onrace can know

**Rule:** Onrace never says more than it can check. A result is self-reported with a source link, never "verified", and a failure is described as what Onrace actually saw, not what it guesses happened on someone else's site.

**Example:**
> Self-reported · via results.hyrox.com
>
> Couldn't open the link. It didn't open in a new tab. Your browser may have blocked it.

**Counter-example:**
> ✓ Verified HYROX result
>
> The timing site is down. Try again later.

**Explanation:**
- `CLAUDE.md` → Result trust model: "Onrace does not verify it — the link itself is the evidence".
- `research.md` → BENCHMARK, mechanism #2: "Structurally label every result as self-reported + source-linked, never as 'verified'", and CONCLUSIONS gap 4: "the link is the evidence,' not 'Onrace verifies'".
- The counter-example's second line claims knowledge a static client can't have. `flows.md`'s link checks were reworded for exactly this reason (Main Job 1 → Endpoints, `DeadEnd6`: "Onrace can only know the link couldn't be opened, not that it's broken"; the same rewording was applied to Flow 3's source-link check on 2026-09-25).
- It differentiates because, per `research.md` → Competitor language → "Where they differ" #1, RoxConnect advertises "VERIFIED RACE PROFILES" and "verified race history", yet describes only "Link your official HYROX results directly from results.hyrox.com", a link presented as verification. Strava admits the gap only in its help center ("We know 33% isn't 100%"). For an athlete whose proof will be judged by an elite race, one overclaim discredits every other claim.

### 2. Point to the source, and let it vouch

**Rule:** every result, race and outbound action names where its truth lives (the official timing site, the organiser's site), and the copy sends people there rather than asking them to take Onrace's word.

**Example:**
> Open official result on berlin.r.mikatiming.com
>
> Register on hyrox.com. Sign-up and payment happen there.

**Counter-example:**
> View proof
>
> Register now

**Explanation:**
- `research/jtbd.md` → Social job: "When I log a result with no one around to vouch for me, I want the proof itself to stand on its own".
- `research.md` → Proof-of-result findings: Boston accepts "an official race result, a digital results platform, or a verified certificate from the timing company". The authority is the timing company, so the copy names it.
- `CLAUDE.md` → Out of scope: "Onrace links out to official registration pages only, never handles signups or payments". The domain in the label makes that visible before the tap, and "Register now" hides it.
- Competitor language → "Where they differ" #2: only Athlinks points back to "the official website's results", and only inside a help article. No competitor puts the source in the interface itself.

### 3. Plain words; the look carries the energy

**Rule:** say the fact and the next step, calmly. No superlatives, no crush/conquer/legend, no hype numbers, no exclamation marks, no "all in one place".

**Example:**
> 7 upcoming races
>
> Couldn't load races. Check your connection and try again. Your filters will stay as they are.

**Counter-example:**
> Your next epic challenge awaits! 🔥
>
> Crush your next race. All your races, all in one place.

**Explanation:**
- `CLAUDE.md` → Design / brand tone: "Bold & competitive — high-energy, athletic, performance-driven **visual identity** (dark, intense, bold typography)". The brief puts the energy in the visual identity. It says nothing about hyped words, so the bold look isn't a licence for loud copy.
- Competitor language → "Where they all sound the same" #1, #2 and #4: all four already say "all in one place" (Athlinks: "All of Your Results in One Place"; Strava: "Everything you need, all in one place"), crush and legend lines ("crush your next event", "Become legendary"), and big numbers ("+499,900 Active competitors", "over 100 million active people"). RoxConnect's numbers even disagree with each other (80, 30+, 195+ countries), which shows how hype numbers erode trust.
- *Inference, flagged:* no research shows athletes distrust hype. The rule rests on the two jobs above (a decision, and a proof), where a claim that sounds inflated costs credibility, and on the fact that sounding like everyone else can't set Onrace apart.

### 4. Every format, by its own name

**Rule:** speak to one athlete across formats, and name each race and format exactly: HYROX, DEKA, Marathon, the race's own name. Never shrink it to one sport, and never blur it into generic fitness words like "activity", "workout" or "event".

**Example:**
> HYROX London · 6 Dec 2026 · London, UK
>
> Log result: Race name · Sport type · Finish time

**Counter-example:**
> Find your next HYROX
>
> Log an activity

**Explanation:**
- `research/jtbd.md` → Emotional job: "be recognized as what I actually am — a hybrid athlete — so that the tools I use reflect my training identity instead of forcing me into a single-sport box" (sourced to `research.md` → Sport taxonomy findings: "'hybrid athlete' describes the audience, not a race format").
- `research.md` → Findings → decisions: Onrace's whitespace is "cross-format discovery + archive (HYROX, DEKA, marathons, triathlons, ultras together)".
- Competitor language, "What it calls things": RoxConnect is "Built for the HYROX community". Strava's object is an "activity", "effort" or "segment", with no race result at all. ocrbase calls everything an "event". Onrace's current copy already says "race" everywhere and never "event" (`microcopy.md` → Searched for and not found), and this principle keeps it that way.

### 5. No crowd in the copy

**Rule:** a result is kept for the athlete and made credible by its source, so the copy never points at followers, sharing, cheers, rivals, leaderboards or "the community".

**Example:**
> Your results stay saved. Sign back in anytime to see them.
>
> Keep your official race results here, each with a link to the timing site that published it.

**Counter-example:**
> Share your PR with the community!
>
> See how you stack up against your rivals.

**Explanation:**
- `CLAUDE.md` → Explicitly out of scope: "Social features — no following, comments, activity feeds, leaderboards, or public sharing of results". Copy that invites sharing promises a feature that doesn't exist.
- `research.md` → BENCHMARK, "One mechanism that won't work: peer/social visibility": "there's no audience positioned to notice or contest a fabricated result". Credibility has to come from the source link (principle 2), not from an audience.
- Competitor language → "Where they all sound the same" #3: RoxConnect ("…crush your next event — together"), Athlinks ("Connect With Friends and Rivals", "sharing your successes") and Strava ("Community-Powered Motivation", "the social network for those who strive") all sell the crowd. ocrbase doesn't, but it has no archive to sell.

## Considered and not adopted

These three weren't adopted because nothing in the sources supports them.

- **"Energetic and motivating, to match the bold brand."** The brand-tone line is about visual identity (principle 3), and no research finding asks for motivational copy. It's also the category's default voice, so it wouldn't set Onrace apart.
- **"Warm, witty, a bit irreverent" (Strava's "A no BS network").** There's no evidence the audience wants this. It also works against principle 1 in the moments that matter most (errors, proof), where a joke reads as not taking the result seriously.
- **"Coach-like encouragement" (PRs, goals, "push yourself").** Training content is out of scope (`CLAUDE.md` → Explicitly out of scope: "Training plans/coaching content"). Personal-best language also implies a judgement of the athlete's performance, which Onrace doesn't make.

## Where current copy already conflicts

This is a pointer only. Nothing is rewritten here, and the flags live in `microcopy.md`.

- **Principle 3:** the Sign in context lines say "…with their source links, in one place". "In one place" is the category's stock phrase.
- **Principle 3 (tone):** microcopy flag **V1**, the minimizer "just" ("it just isn't confirmed yet").
- **Principle 2:** flag **T2**, where the proof link has seven names. Naming the source consistently is part of letting it vouch.
- **Principle 1:** no conflicts found. No current line says "verified" (only "Onrace doesn't verify results"). "Official" only ever names the source's own page ("Official result", "Official race website"), and the error copy already says only what the browser can detect.

## Dictionary

One concept, one word. Every discrepancy flagged in `microcopy.md` (T1–T6, A1–A5, C1–C4) is resolved below. When a line is written or rewritten, the word comes from this table, and the struck-out words don't reappear. The reasons use the research's own language. Where a choice rests on iOS convention rather than research, it says so.

### Things (nouns)

| Concept | Use | Not | Why | Resolves |
|---|---|---|---|---|
| The collection of someone's results | **results archive** | ~~archive~~ (alone), ~~logged results~~, ~~your official race results~~ (as a name) | The product is "a personal archive of official race results" (`CLAUDE.md` → What it is), and the job is "Results archiving" (`jtbd.md` → Main Job 2). "Results archive" says both what's kept and why. "Logged results" names the act, not the place. Counts read "4 results", not "4 logged results". | T1 |
| …the tab and screen that show it | **My Results** | — | The nav label, fixed in `sitemap.md` → Navigation § 1. It names the place in the tab bar. Running copy says "results archive" ("Sign in to see your results archive"). The two don't compete: one is a label, the other a description. | T1 |
| One logged race | **result** | ~~entry~~, ~~submission~~, ~~record~~, ~~time~~ (for the whole thing), ~~activity~~ | `CLAUDE.md` → `results` table, and Boston's own wording: "an official race result" (`research.md` → Proof-of-result findings). "Proof of a past time" becomes "proof of a past result". | T3 |
| The number on it | **finish time** | ~~time~~ (alone), ~~PR~~ | The field (`finish_time`, `CLAUDE.md`). **qualifying time** is allowed only when naming what an elite race asks for. It's the Archivist's own phrase ("proof of a qualifying time", `personas.md`). | T3 |
| The link a person pastes as proof | **official result link** | ~~source link~~, ~~result link~~, ~~timing page~~, ~~your proof~~ (as a name) | `CLAUDE.md` → trust model: "a link to the official timing site as proof"; the field is `official_result_url`. "Official result" is what Boston accepts, so this is the word an elite race will recognise. "Proof" stays as the *reason* ("it's the proof elite races ask for"), not as the object's name. | T2 |
| The page that link opens | **official result** | ~~timing page~~, ~~result page~~ | The same Boston phrase: the thing opened is the official result itself ("Open official result on berlin.r.mikatiming.com"). | T2 |
| The website behind it | its **domain** (results.hyrox.com); generically, **official timing site** | ~~timing site~~ (without "official"), ~~the source~~ | Principle 2: name where the truth lives. "Official timing site" is `CLAUDE.md`'s own phrase, used only when there's no domain to name (e.g. the Log result helper). | T2 |
| The set of races Onrace curates | **race catalog** | ~~Onrace catalog~~, ~~catalog race~~, ~~the catalog~~ (alone), ~~listing~~ | `CLAUDE.md` → Data model: "`races` (public catalog)". "Race" in front says what's in it, and saying "Onrace" in Onrace's own UI adds nothing. One item is still "a race" ("Find a race", "No race in the race catalog matches…"). "Listing" is IA-doc language (`sitemap.md` → Race listing), not interface language. | T4 |
| A race | **race** | ~~event~~, ~~competition~~, ~~listing~~ | Already consistent (`microcopy.md` → Searched for and not found). It's the audience's word ("find hybrid races to enter", `jtbd.md` → Main Job 1). Competitors' "event" (ocrbase) and "activity" (Strava) are what principle 4 rules out. | — |
| What someone signs in to | **account** | ~~profile~~ (in running copy) | `CLAUDE.md` / `sitemap.md` → Entities 5, "Athlete account": the thing that exists because of auth. "Create an account to set up your profile" becomes "Create an account to start your results archive", or "…to see your account". | T5 |
| …the tab and screen that show it | **Profile** | — | The nav label (`sitemap.md` → Navigation § 1), same pattern as My Results: a label, not a synonym. | T5 |
| What someone types to sign in | **email** | ~~address~~, ~~email address~~ | `CLAUDE.md` → Auth method: "email + password". One word everywhere: "We'll send a link to confirm your email", not "…your address". | T6 |
| What the email contains | **confirmation link** (sign-up) / **reset link** (password) | ~~email~~ as the thing you resend, ~~the link we sent~~ when the type matters | `flows.md` Flows 4 and 6 name the objects this way. The link is the thing the person acts on, and the email is only how it travels. So "Resend email" becomes "Send a new link" (see A1). | T6 |
| When a race happens | **race date** | ~~date~~ (alone, as a field label) | The race's `event_date`, and the person's own phrase on Log result ("Add the date you raced"). On Race detail and Result detail, the label becomes "Race date" as well. The Filters range keeps its structure as "Race date: From / To". | C1 |

### Actions (buttons and links)

| Action | Use | Not | Why | Resolves |
|---|---|---|---|---|
| Get a fresh emailed link (confirmation or reset) | **Send a new link** | ~~Resend email~~, ~~Resend link~~, ~~Request a new link~~, ~~send a new one~~ | One action, one label, on all four surfaces (sign-up Check inbox, reset Check inbox, expired confirmation, expired reset). "New" is the accurate word: each link "works once" (`flows.md` Flows 4 and 6), so a person needs a new link, not the old email again. | A1 |
| Create an Onrace account | **Create account** | ~~Sign up~~, ~~Register~~ | Already the button and toggle label. "Sign up" stays a doc name only (`sitemap.md` → "Sign in / Sign up") and never appears in the UI. | A2 |
| Enter a race, on the organiser's site | **Register** ("Register on hyrox.com"), and **registration** | ~~sign-up~~, ~~sign up~~ | `CLAUDE.md` → `registration_url`, and "Race registration/payment handling" is out of scope. Registering is the organiser's word for entering a race. "Sign-up and payment happen there" becomes "Registration and payment happen there". Then "sign up" never means two things. | A2 |
| Sign in / out | **Sign in**, **Sign out** | ~~Log in~~, ~~Log out~~, ~~Login~~ | Already consistent. "Log" is reserved for results ("Log result"), so it never means signing in. | — |
| Record a new result | **Log result** / "Log your first result" | ~~Add result~~, ~~Submit~~ | `jtbd.md` → Related Job 3: "log the result along with where it came from". | — |
| Leave a task or modal without changing anything | **Cancel** | ~~Close~~ | iOS convention (not research): Cancel means "nothing I started here is kept". It covers the Sign in modal, Race picker, Filters sheet and sign-out alert. "Close" goes. | A3 |
| Hide a message you've read | **Dismiss** | ~~Close~~, ~~OK~~ | The inline alerts (registration link, official result link) aren't tasks, so Cancel would be wrong. One word for "I've seen this". | A3 |
| Go back one screen | **‹ \<parent screen's title\>** — "‹ Discover", "‹ My Results", "‹ Sign in" | ~~Back to races~~, ~~Back to My Results~~ | iOS convention: the back button names where it goes, using the same word as that screen's title or tab, so the label always matches where you land. Replaces the two-rule compromise in `wireframes/_conventions.md` § 1 (the rule changes in the rewrite pass). | A4 |
| Remove every active filter | **Clear all filters** | ~~Clear all~~ | The longer label is unambiguous wherever it appears (chips bar, empty state). "Clear all" next to chips could read as clearing the search or the list. | A5 |
| Retry a failed load | **Try again** | ~~Retry~~, ~~Reload~~ | Already consistent across every error. | — |

### Consistency rules

| Rule | Decision | Why | Resolves |
|---|---|---|---|
| Expiry wording | One sentence, everywhere a link can expire: **"Each link works once and expires after a while."** An expired-link heading is "This link has expired", naming the link type if needed ("This reset link has expired"). What the screen reader hears matches what's shown: "Sent. Check your inbox again." in both. | Three wordings of one fact read as three different rules. `flows.md` Flows 4 and 6 state the rule once ("expire and work once"). | C2 |
| Apostrophes | **Curly ’** in all product copy. | Typographic, not research: it's the platform's own text style, and it takes one decision to end 13 vs 32 inconsistent lines. | C3 |
| Required vs optional | **Mark what's optional, not what's required.** Every Log result field is needed, so none gets a "Required" tag. The one optional control, "Find in race catalog", keeps its "Optional" note, and the official result link's helper says *why* it's needed. | Drops the self-contradiction (a "Required" tag on one field under "Every field is needed"). The link keeps its weight through its explanation, which is what `research.md` → BENCHMARK mechanism #1 cares about: the link is mandatory, and people understand why. | C4 |

### Allowed and not allowed at a glance

- **Allowed:** race · race catalog · race date · sport type · result · finish time · qualifying time (elite-race context only) · results archive · official result link · official result · official timing site / \<domain\> · log (a result) · register / registration (races only) · account · email · confirmation link · reset link · Create account · Sign in · Sign out · Send a new link · Cancel · Dismiss · Try again · Clear all filters · My Results / Profile / Discover (as labels).
- **Not allowed:** event · competition · listing · entry · submission · record · activity · workout · effort · archive (alone) · logged results · source link · result link · timing page · timing site (without "official") · proof (as the link's name) · address · email address · the catalog / Onrace catalog / catalog race · profile (in running copy) · sign up / signup / sign-up (anywhere in the UI) · log in / login · Close · Back to … · Resend … · Request a new link · Clear all (alone) · Required (as a tag) · verified · PR / personal best.

## Forbidden

What Onrace never writes, whoever is writing and however the line is squeezed for space. Each "before" is either a real line from the current copy (`microcopy.md`) or the competitor pattern it echoes (`research.md` → Competitor language). The "after" follows the Dictionary.

| Never write | Why | Before | After |
|---|---|---|---|
| **"all in one place" / "in one place" / "in one spot"** | Every competitor's stock promise (Athlinks "All of Your Results in One Place", Strava "Everything you need, all in one place"). Principle 3: it can't set Onrace apart, and it says nothing specific. | "Sign in to keep your official race results, with their source links, in one place." (current Sign in line) | "Sign in to see your results archive: each result with its official result link." |
| **crush · conquer · legendary · epic · beast mode** | The category's hype register (RoxConnect "crush your next event", Strava "Become legendary", Athlinks "conquer new goals"). Principle 3. | "Crush your next race." | "7 upcoming races" |
| **Motivational second person**: "your next X starts here", "push yourself", "you've got this" | Competitor pattern #5 (ocrbase "Your next race starts here", Strava "Push yourself further"). Training and coaching are out of scope (`CLAUDE.md`). | "Your next race starts here." | "Discover" (the screen title), then the races |
| **Hype numbers**: counts used as social proof ("+499,900 athletes", "every 19 seconds") | Competitor pattern #4. RoxConnect's own counts contradict each other (80, 30+, 195+ countries), and a number used to impress invites exactly that doubt. Counts are allowed only as plain facts about the list on screen. | "Join 100,000+ hybrid athletes!" | "7 upcoming races" |
| **Community and crowd words**: community, friends, rivals, followers, share, cheers, leaderboard | Principle 5. Social features are out of scope (`CLAUDE.md`), and peer visibility "won't work" here (`research.md` → BENCHMARK). | "Share your result with the community!" | "Saved: Berlin Marathon" |
| **verified / ✓** about a result | Principle 1 (`CLAUDE.md`: "Onrace does not verify it"). The competitor scan's clearest warning is RoxConnect's "VERIFIED RACE PROFILES" for what is only a link. | "✓ Verified result" | "Self-reported · via results.hyrox.com" |
| **"just"** as a minimizer (flag V1) | It shrinks the person's problem instead of explaining it, and a stuck account isn't a small thing to the person it happened to. | "Your account is still there, it just isn't confirmed yet." (current) | "Your account is still there. It isn't confirmed yet." |
| **Exclamation marks** | Principle 3: the facts carry the weight. A "!" on an error reads as alarm, and on a success it reads as salesmanship. Neither helps someone assembling proof for an elite race. | "Password changed!" | "Password changed. Sign in with your new password." (current) |
| **Emoji in system messages** (errors, confirmations, status, empty states) | Principle 3. Emoji add tone the facts don't need, and screen readers read them aloud ("fire, party popper"). | "No races found 😕" | "No races match your current filters" (current) |
| **"successfully"** | Redundant: the message that something happened *is* the success. "Saved" already says it worked. It also pads a line that should be scannable. | "Your result was saved successfully." | "Saved: Berlin Marathon" (current) |
| **Oops / Whoops / Uh-oh / "Something went wrong"** | The AI-and-app cliché error. It says nothing about what happened or what to do next, which is the opposite of principle 1. | "Oops! Something went wrong." | "Couldn’t load races. Check your connection and try again." (current, with a curly apostrophe) |

**Not forbidden, for the record:** "official" (it names the source's own page, not Onrace's judgement), "proof" (as the reason a link is needed), and plain counts of what's on screen ("4 results"). These are allowed because they state facts. The words above are forbidden because they make claims.

## Microcopy

Rules by element type. Each rule has one Onrace example (written to the Dictionary above) and a "not" example. A **Check** line shows the rule was tested against the Principles, Dictionary and Forbidden list. Where two of them pulled in different directions, the resolution is written into the rule.

The states these rules cover are the ones `wireframes/_screens.md` scopes for every screen: base, empty, error, loading, success, plus the two check-inbox waits.

### Button

**Rule:** an action verb plus what it acts on, naming the result of the tap, and it must make sense read alone, out of context (a screen reader's list of buttons, a skimmed screen). Where the platform keeps the visible label short (a nav-bar "Save", a retry inside an error block), the **accessible name** carries the full phrase.

| Onrace example | Not |
|---|---|
| **Register on hyrox.com** · **Log result** · **Send a new link** · **Save new password** · **Find in race catalog** · **Clear all filters** | ~~OK~~ · ~~Next~~ · ~~Submit~~ · ~~Continue~~ · ~~Yes~~ · ~~Click here~~ · ~~Register now~~ |

- **Short visible label, full accessible name:** "Try again" inside "Couldn’t load races" is announced as "Try loading races again". The nav-bar "Save" beside "Log result" is announced as "Save result". "Dismiss" is announced as "Dismiss this message".
- **Check:**
  - Principle 2: a button that leaves Onrace names its destination ("Register on hyrox.com", "Open official result on berlin.r.mikatiming.com").
  - Dictionary: verbs are the chosen ones (Log, Register, Send a new link, Cancel, Dismiss, Try again).
  - The read-alone test is why the Dictionary keeps "Try again" only with an accessible name, and picks "Clear all filters" over "Clear all".

### Screen heading

**Rule:** say what this place *is*, in Dictionary terms: the screen's name, or the one race or result it shows. It's never a greeting, a mood or a promise.

| Onrace example | Not |
|---|---|
| **Discover** · **My Results** · **Log result** · **Find a race** · **Reset password** · on a detail screen, the item itself: **HYROX London**, **Berlin Marathon** | ~~Welcome back!~~ · ~~Your dashboard~~ · ~~Let’s log a race~~ · ~~Your next race starts here~~ |

- **Check:**
  - The heading is also the back label on the next screen down (`_conventions.md` § 1, Dictionary A4), so it has to be the place's stable name ("‹ My Results" only works if the screen is called My Results).
  - Principle 3 and Forbidden rule out greetings and motivational lines (ocrbase's "Your next race starts here").

### Form field

**Rule:** the **label** says what to enter, the **hint** says how (format, or where to find it), and the **validation error** says exactly what to fix, in one sentence, next to the field. A **placeholder** is an example marked "e.g.", never a real-looking value and never a stand-in for the label.

| Part | Onrace example | Not |
|---|---|---|
| Label | **Official result link** · **Finish time** · **Race date** | ~~Source link~~ · ~~Time~~ · ~~Date~~ |
| Hint | "Paste the link from the official timing site. Elite races ask for exactly this." · "Hours:minutes:seconds, exactly as the official results show it." | ~~Enter a valid URL~~ · ~~Required~~ |
| Error | "Add your finish time, e.g. 3:12:48." · "Use at least 8 characters." | ~~Invalid input~~ · ~~This field is required~~ · ~~You forgot the finish time~~ |
| Placeholder | "e.g. 3:12:48" · "e.g. Berlin Marathon" | ~~https://berlin.r.mikatiming.com/2025/~~ (reads as filled in, flag P2) |

- **Required vs optional:** mark only what's optional ("Optional", on Find in race catalog). Required fields carry no tag, and the hint explains why a field matters (Dictionary, C4).
- **Check:**
  - The labels come from the Dictionary (official result link, race date, finish time).
  - The hint and error say *why* the link is needed, which is principle 2's "let the source vouch".
  - Errors follow the Error rule below: no blame, the fix stated as an instruction.

### Empty state

**Rule:** say why it's empty (which is often nothing wrong), then offer the action that fills it. Name the real reason: filters, a search, nothing logged yet. Don't imply a fault.

| Onrace example | Not |
|---|---|
| "**No races match your current filters.** Remove a filter above, or try a wider date range." · [**Clear all filters**] [**Loosen filters**] | ~~Nothing here yet 😕~~ · ~~No data~~ · ~~Oops, no results!~~ |
| "**No results in your results archive yet.** Each result you log keeps its official result link, ready when an elite race asks for proof." · [**Log your first result**] | ~~Start your journey!~~ · ~~Your archive is empty~~ (no next step) |

- **Check:**
  - Principle 1: the reason given is the one Onrace knows (the filters, the empty archive).
  - The Archivist's job gives the empty archive its reason to fill ("proof of a qualifying time", `personas.md`).
  - Forbidden: no emoji, no "Oops", no hype.
  - Dictionary: "results archive", "official result link".

### Error

**Rule:** three parts, in order: **what happened**, **why** (as far as Onrace can know), and **what to do next**. Never blame the person reading it, even when the cause is on their side (a missing field, a mistyped email). State the fix as an instruction, not as their mistake. When Onrace can't know the cause, it gives the likely ones as possibilities ("may"), never as fact.

| Onrace example | Not |
|---|---|
| "**Couldn’t open the link.** It didn’t open in a new tab; your browser may have blocked it. Try again, or come back to this race later." | ~~The timing site is down.~~ (a claim Onrace can’t check) |
| "**Couldn’t sign you in.** The email or password didn’t match, or the connection dropped. Check both and try again." | ~~You entered the wrong password.~~ · ~~Invalid credentials.~~ |
| "**Too many requests.** Onrace limits how often a reset link can be sent. Wait a minute, then send a new link." | ~~Oops! Something went wrong.~~ · ~~Error 429~~ |
| Field-level: "Add the official result link. It’s the proof this result is yours." | ~~You didn’t add a link!~~ |

- **Check:**
  - Principle 1 decides what goes in the "why" part. `flows.md`'s link checks were reworded for the same reason, and the "may" framing is the honest form when there are several possible causes.
  - Forbidden: no Oops, no exclamation marks, no "successfully".
  - Dictionary: "Couldn’t" with a curly apostrophe (C3), "Send a new link" (A1), "email" (T6).

### Loading

**Rule:** say nothing, or name what's loading. Use a skeleton or placeholder in place of the content, and a short status line for screen readers ("Loading races…"). In a button, the verb moves into the present tense: Save becomes Saving…. There's no filler, no cheer, and no invented progress.

| Onrace example | Not |
|---|---|
| (skeleton cards) + screen-reader status "Loading races…" · button **Saving…** · **Sending…** · **Signing in…** | ~~Hang tight!~~ · ~~Good things take time…~~ · ~~Almost there! 87%~~ · ~~Please wait~~ |

- **Check:**
  - Principle 1: no fake percentages, because Onrace doesn't know them.
  - Principle 3: silence or a noun, no cheer.
  - The present-tense button keeps the Button rule's verb, so the label still says what's happening.

### Success

**Rule:** state the fact, and the next step if there is one. No celebration: the result of the tap is the confirmation.

| Onrace example | Not |
|---|---|
| "**Saved: Berlin Marathon**" (on My Results, the result now in the list) · "**Password changed.** Sign in with your new password." · "**We sent a link to maya.rossi@example.com.** Open it on this device to finish creating your account." | ~~Result saved successfully!~~ · ~~Congratulations! 🎉~~ · ~~You’re all set!~~ · ~~Great job, champion~~ |

- **Check:**
  - Forbidden: "successfully", exclamation marks, emoji.
  - Principle 5: no "share it" follow-up.
  - Principle 1: Check inbox says "We sent a link" only on sign-up, where Onrace knows it did. On reset it says "If an account exists for …", because Supabase doesn't reveal whether one does (`flows.md` Flow 6).

### Dangerous action

**Rule:** before the tap, say what will happen, and whether it can be undone. If it can't, say so plainly. If it can, say how to get back. Either way the confirm button repeats the action's verb, not "Yes" or "OK", and Cancel is the safe default.

| Onrace example | Not |
|---|---|
| Alert: "**Sign out of Onrace?** Your results stay saved. Sign back in anytime to see them." · [**Cancel**] [**Sign out**] | ~~Are you sure?~~ · [~~Yes~~] [~~No~~] · ~~This can’t be undone~~ (it can: signing back in restores everything) |
| Template for an irreversible action (none in MVP; editing or deleting a result is an accepted gap, `research.md` → CONCLUSIONS gap 7): "**Delete your Berlin Marathon result?** This can’t be undone. The official result on berlin.r.mikatiming.com isn’t affected." · [**Cancel**] [**Delete result**] | ~~Delete?~~ · [~~OK~~] |

- **Check:**
  - Principle 1 decides the undo sentence. "Can't be undone" appears only when it's true, which is why Sign out gets the reassuring version.
  - Principle 2 names what's outside Onrace and untouched (the official result).
  - Dictionary: Cancel (A3), "results", "official result".
  - Button rule: the verb repeats the action ("Sign out", "Delete result").

---

`voice.md` is complete: Principles → Dictionary → Forbidden → Microcopy. From here on, every line of Onrace copy is written by it, and checked against `microcopy.md`. When they disagree: the **Forbidden** list is absolute, the **Dictionary** decides the word, the **Microcopy** rules decide the shape of the line, and the **Principles** settle anything the other three don't cover.
