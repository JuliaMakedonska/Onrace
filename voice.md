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
