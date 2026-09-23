# Wireframe conventions

Applies to every screen wireframed for Onrace, starting with the two screens scoped in `_screens.md` (Race browse, Race detail) and carried forward as later steps expand to the rest of `sitemap.md`. Nothing here draws a screen — this is the ruleset the drawing steps follow.

---

## 1. Fidelity

Structure, hierarchy, and zones only.

- **Grayscale only** — no color. Zones and emphasis are shown with grayscale value (black/white/gray fills or borders), not hue.
- **No fonts** — no typeface choices, no custom font sizing beyond what's needed to show a heading/body/label hierarchy generically (e.g., relative weight or size steps, not a chosen type scale).
- **No branding** — no logo, no product name treated as a wordmark, no Onrace visual identity (`../CLAUDE.md`'s "Bold & competitive" brand tone is explicitly deferred, not applied here).
- **No images** — no photos, illustrations, or icons standing in for future artwork. A map is represented as a labeled placeholder region (e.g., a boxed area labeled "map"), not a rendered map.

This is a deliberate low-fidelity pass: the goal is to validate structure and content against the jobs in `../research/jtbd.md`, not to preview the finished UI.

## 2. Markup

Semantic HTML, not nested `<div>` soup.

- Use `<header>`, `<nav>`, `<main>`, `<section>`, `<article>`, `<form>`, `<button>` for their actual roles — a race card is an `<article>`, the filter set is a `<form>`, the 3-item global nav (`../sitemap.md` → Navigation § 1) is a `<nav>`.
- `<div>`/`<span>` are allowed only where no semantic element fits (e.g., a pure layout wrapper with no independent meaning) — never as the default choice.
- Each wireframe is a standalone, valid HTML page (`<html>`, `<head>`, `<body>`) — no build step, no framework, viewable by opening the file directly.

## 3. Text

Real domain text, not lorem ipsum.

- Race listings use plausible real-world race names, sport types, and locations drawn from Onrace's actual scope (`../CLAUDE.md` → Race scope: HYROX, DEKA/functional-fitness, marathons, half marathons, triathlons, ultras) — e.g. "HYROX London," "Boston Marathon," not "Race Name 1."
- Form fields, filters, and detail fields use their real field names and plausible real values per `../sitemap.md`'s Entities section (`race_name`, `sport_type`, `event_date`, `city/region/country`, `official_url`, `registration_url`, `finish_time`, `official_result_url`) — not generic "Label" / "Value" filler.
- Error/empty/loading copy is written as real, specific microcopy matching the state's actual cause in `../flows.md` (e.g. "No races match your current filters," not "Empty state" or "Lorem ipsum dolor").

## 4. File naming

- One HTML file per screen, kebab-case, Latin script, matching the screen's name in `../sitemap.md`: `wireframes/<name>.html`.
  - Example: **Race browse** → `wireframes/race-browse.html`; **Race detail** → `wireframes/race-detail.html`.
- One additional file per *real, non-default* state on that screen: `wireframes/<name>-<state>.html`, where `<state>` is one of `empty`, `error`, `loading` (see § 5 for why `success` isn't a suffix).
  - Example: `wireframes/race-browse-empty.html`, `wireframes/race-browse-error.html`, `wireframes/race-browse-loading.html`.
- Which state files actually get created is decided per screen by `_screens.md`'s state table, not assumed uniform across screens — a screen only gets a `-<state>.html` file for a state marked ✓ there. (Race detail, for instance, gets no `-empty.html` — `_screens.md` marks Empty "—" for that screen: a race detail is only ever reached for a race that already exists.)

## 5. States

Each state is its own page — same structure, different content — not one page with hidden/toggled variants.

- **The base page (`<name>.html`) is the success state.** Per `_screens.md`'s own rule ("only where there's a distinct 'it worked' screen/endpoint"), there's no separate `-success.html` file: the base wireframe *is* the populated, working view of the screen — races listed on Race browse, a race's full detail plus a working registration link on Race detail. A screen with no distinct success endpoint (Race browse, per `_screens.md`) still uses its base page as the default/populated view; it just isn't a job-closing terminal in `../flows.md`'s sense.
- `empty`, `error`, and `loading` each get their own file, built only where `_screens.md` marks that state ✓ for that screen.
- All state pages for a given screen share the same structure and zones as the base page (§ 1–2) — a state page changes what's rendered inside those zones (e.g. a message in place of the race list, a spinner placeholder in place of content), not the page's layout or semantic skeleton.
- Where `../flows.md` distinguishes two causes of the same state on one screen (e.g. Race detail's `DetailError` vs. `RegLinkError`, both "error"), that distinction is handled as different copy within one `-error.html` page, not as separate files — the file-naming grain is state, not cause.

## 6. Deferred to a later pass

Explicitly out of scope until a later step:

- Color (including the eventual dark, high-energy brand palette per `../CLAUDE.md` → Design/brand tone)
- Fonts / typography
- Shadows, elevation, or other visual depth cues
- Icons
- Any other finished-UI polish

---

*Next: draw `race-browse.html` / `race-browse-empty.html` / `race-browse-error.html` / `race-browse-loading.html` and `race-detail.html` / `race-detail-error.html` / `race-detail-loading.html`, per `_screens.md`'s state table and these conventions.*
