# Wireframe conventions

Applies to every screen wireframed for Onrace, starting with the two screens scoped in `_screens.md` (Race browse, Race detail) and carried forward as later steps expand to the rest of `sitemap.md`. Nothing here draws a screen — this is the ruleset the drawing steps follow.

---

## 1. Fidelity

Structure, hierarchy, and zones only.

- **Grayscale only** — no color. Zones and emphasis are shown with grayscale value (black/white/gray fills or borders), not hue.
- **No fonts** — no typeface choices, no custom font sizing beyond what's needed to show a heading/body/label hierarchy generically (e.g., relative weight or size steps, not a chosen type scale).
- **No branding** — no logo, no product name treated as a wordmark, no Onrace visual identity (`../CLAUDE.md`'s "Bold & competitive" brand tone is explicitly deferred, not applied here).
- **No images** — no photos, illustrations, or icons standing in for future artwork. A map is represented as a labeled placeholder region (e.g., a boxed area labeled "map"), not a rendered map.
- **Every screen file is bare phone content, not a mini-site.** `wireframes/<name>.html` contains only the screen itself (390px-wide, `height: 100%`, internally scrolling) — no nav tree, no captions, no device-frame border. That chrome lives exactly once, in `index.html` (§ 6), which puts the bare file inside its own dark device-mockup frame via `<iframe>`. Opening a screen file directly still works and still reads as phone-width, just without index.html's outer bezel. Nothing inside the file — a drawer, the bottom nav — is ever allowed to render outside the file's own bounds (`overflow: hidden` on `<body>`, `position: relative` as the anchor for the drawer/backdrop's `position: absolute`).
- **Global nav is a bottom tab bar, not top tabs.** Onrace's real in-app 3-item global nav (`../sitemap.md` → Navigation § 1: Discover / Log Result / My Results) is fixed to the bottom edge of the screen — the standard mobile placement for a persistent global nav — not styled as browser-style horizontal tabs at the top. It sits outside the scrolling content (so it doesn't scroll away) but still inside the screen file's own bounds. No icons yet (§ 7) — just the correct bar shape and bottom position; the current tab is marked the same way as any other current-page indicator in this file (inverted fill).
- **Zone separation is spacing, not boxing.** A visible gap between zones is enough to group them — a border/box wrapper around a zone is added only when nothing inside that zone is already self-evidently one unit (no zone in the current screens needs this: a button, a line of text, or a set of already-bordered items don't get a second, redundant border around them). Borders are reserved for elements doing real structural work — separating one race card from the next, framing the List/Map toggle buttons, marking the drawer's edge against the content behind it — never as decorative wrapping. Padding inside any element scales with that element's own content (a one-line counter is not padded like a multi-field card).
- **Working disclosure patterns** — anything hidden by default (filters, secondary panels, alternate views of the same data) gets real, working interaction, not a static illustration of the collapsed/expanded state: a bottom-sheet/drawer overlay triggered by a button for content that replaces the screen's attention (e.g. a filter form), or a real toggle that swaps which panel is visible for two representations of one result set (e.g. map vs. list, per `../sitemap.md`'s "Race browse (map + list)"). See § 2 for how this is implemented.

This is a deliberate low-fidelity pass: the goal is to validate structure and content against the jobs in `../research/jtbd.md`, not to preview the finished UI.

## 2. Markup

Semantic HTML, not nested `<div>` soup.

- Use `<header>`, `<nav>`, `<main>`, `<section>`, `<article>`, `<form>`, `<button>` for their actual roles — a race card is an `<article>`, the filter set is a `<form>`, the 3-item global nav (`../sitemap.md` → Navigation § 1) is a `<nav>`.
- `<div>`/`<span>` are allowed only where no semantic element fits (e.g., a pure layout wrapper with no independent meaning) — never as the default choice.
- Each wireframe is a standalone, valid HTML page (`<html>`, `<head>`, `<body>`) — no build step, no framework, viewable by opening the file directly.
- **Light vanilla `<script>` is allowed** when a zone's real behavior requires it — opening/closing a bottom-sheet drawer, swapping which view panel is visible — so the wireframe demonstrates actual interaction structure, not just a picture of one state. No framework, no build step, no external library, and JS is used only to toggle real HTML (a `hidden` attribute, an `aria-pressed`/`aria-expanded` state, a CSS class already defined for the transition) — never to fake content that should be real markup.
- **Sourcing/rationale annotations are invisible in the rendered page.** Which job a zone closes, where it sits in `../flows.md`, or why a default was chosen (e.g. why a view defaults to List over Map) is recorded as an HTML comment immediately above that zone's markup (`<!-- ZONE: ... -->`) — never as on-page text. The rendered wireframe shows only the real interface (headings, buttons, labels, content); the traceability is still in the file for anyone reading source or `view-source:`, it just doesn't compete with the UI for visual attention. A screen's job/flow-position summary lives in `index.html`'s heading above the device mockup (§ 6) — one line, outside the screen file entirely, not duplicated per file.

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

## 6. `index.html`: the wireframe-browsing shell

One page owns all the wireframe-browsing chrome — the nav tree and the device-mockup frame — so individual screen files (§ 1) can stay bare. `index.html` is **dark-themed**, matching the rest of the project's rendered docs (`../public/research.html`, `../public/personas.html`, `../public/ia.html`, `../public/workspace.html`) — same CSS variables (`--bg`, `--bg-elev`, `--bg-elev-2`, `--border`, `--text`, `--text-dim`, `--text-faint`, `--accent`, `--accent-dim`, `--radius`), same values. This is the one deliberate exception to § 1's grayscale rule: it's the *shell*, not the product wireframe — the actual screen content rendered inside the device mockup stays grayscale, unchanged, per § 1.

- **Layout**: `<div class="layout">` — a CSS grid, `grid-template-columns: 240px 1fr`, not flex — with `<aside class="sidebar">` (dark, `position: sticky`, own scroll) as one column and `<div class="content-col">` as the other. Grid guarantees the two stay separate, bounded regions at any window width.
- **Device mockup**: `.content-col` holds a fixed-size box (~410×864px, capped by viewport height) styled with the dark palette, centered in the available space, containing one `<iframe>` that fills it and points at the current bare screen file. The iframe's own native scrollbar is the "internal scroll" — nothing here re-implements scrolling.
- **Tree nav, pulled only from sourced documents, nothing invented** (same rules as the nav this replaced, now reskinned dark and made interactive):
  - Top-level groups are `../sitemap.md`'s own Screens-section clusters — Discovery, My Results (Archive) — plus Sign in/Sign up as an ungrouped top-level item, exactly where `../sitemap.md`'s own ASCII tree places it (outside both clusters, an `[ORPHAN]`).
  - Each screen is a node whose `data-frame` is its base `<name>.html` (§ 4/§ 5 — the base file is always the default/"success" view).
  - State children (`Empty` / `Error` / `Loading` / `Success`) are added **only** for a screen that has an actual `_screens.md` state table, and **only** for the states that table marks ✓ — e.g. Race browse gets Empty/Error/Loading (its Success is "—", no child); Race detail gets Error/Loading/Success (its Success child points at the same `race-detail.html` as the screen node — no separate file — and it gets no Empty child, "—"). A screen with no `_screens.md` table yet (Results list, Log result, Result detail, as of this pass) is a plain leaf link with no state children — add them only once that screen gets its own `_screens.md` pass.
  - Indentation is nested `<ul>`/`<li>` only — group → screen → state, three levels.
- **Switching screens**: clicking a tree link is real, working interaction (light vanilla JS, § 2) — it sets the iframe's `src` to the link's `data-frame`, moves `aria-current="page"` to that link, and updates the heading above the mockup. No full page reload, no framework.
- Sourcing/rationale for the nav's own structure lives in an HTML comment above it (per § 2's rule), not as on-page text.

## 7. Deferred to a later pass

Explicitly out of scope until a later step:

- Color (including the eventual dark, high-energy brand palette per `../CLAUDE.md` → Design/brand tone)
- Fonts / typography
- Shadows, elevation, or other visual depth cues
- Icons
- Any other finished-UI polish

---

*Next: `race-browse.html` (bare screen) and `index.html` (dark shell + nav tree + device mockup) are built. Still to draw: `race-browse-empty.html` / `race-browse-error.html` / `race-browse-loading.html` and `race-detail.html` / `race-detail-error.html` / `race-detail-loading.html`, per `_screens.md`'s state table and these conventions — each new file is bare (§ 1) and just needs a `data-frame` node added to `index.html`'s existing tree (§ 6).*
