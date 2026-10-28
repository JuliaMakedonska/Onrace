# Components

Lesson 8, step 3 (2026-10-27): the kit's component classes, one file per component, on the two token levels in `../tokens/tokens.css`. The classes, the markup they style and the states they cover (hover, pressed, focus, disabled) are exactly those of `ui/kit.css`. Nothing new was added; new states come in Lesson 9.

## What a page links

```html
<link rel="stylesheet" href="../tokens/tokens.css">       <!-- primitives + semantic color roles -->
<link rel="stylesheet" href="../components/index.css">    <!-- every component, one file, generated -->
<!-- Race browse and the showcase only, not render-blocking: -->
<link rel="preload" as="style" href="../ui/map-data.css" onload="this.onload=null;this.rel='stylesheet'">
```

`index.css` is **generated**: edit the component files, then run `python3 scripts/build_components.py` (`scripts/concept/build_stand.py` runs it first on every build). It's one bundled file, so a page makes one request instead of an `@import` chain.

**Who links it (since step 4, 2026-10-28):** every page that shows the product: the 35 screens, `ui/kit.html` (the showcase), `ui/shell.html`, the stand and `concept/first-screen.html`, and the review pages (for the page's base styles). `ui/kit.css` is gone: `scripts/check_kit.py` fails if a screen, the showcase or the shell links anything else, and `scripts/check_links.py` fails if any page links a missing file.

## The cascade order

The bundle keeps today's cascade exactly.

- **The order key.** `ui/kit.css` didn't keep each component in one place: a component's hover sits next to a screen's layout, skeletons appear in three places, and so on. So every component file holds its rules in **blocks**, and each block starts with an order line:

  ```css
  /* order 0180 */
  ```

- **The bundle.** It takes every block of every file and sorts by that number. The numbers are the order of `ui/kit.css` before the split: 107 blocks from 401 rules, numbered 0010 to 1070 in steps of 10. A rule added later can take a free number between two blocks without renumbering.
- **How it was checked.** With comments and whitespace stripped, `index.css` has exactly the rule text of `ui/kit.css`, in the same order (2026-10-27). The only differences:
  - every color token goes through a semantic role (the step 2 mapping in `../tokens/tokens-audit.md`);
  - `.kit-tabbar > .bottom-nav` is gone from the tab bar's two rules.
- **One file, several blocks.** A component with several blocks in its file is the cost of keeping the cascade exact. Collapsing them into one block is a cascade change, so it needs the comparison run again.

## The rules (checked by `scripts/build_components.py`; a failure stops the build)

- **Color only through a semantic role** from `tokens.css` (`--surface`, `--text-secondary`, `--accent-fill` …). No component reads a color primitive (`--graphite-*`, `--amber-*`, `--coral-*`, `--black`, `--alpha-*`).
- **Geometry from primitives directly:** radius, spacing, size, type size, duration, z-index (`--radius-2`, `--space-4`, `--size-item`, `--dur-fast`, `--z-sheet`). Non-color tokens have no semantic level, as decided in step 2.
- **Everything through `var()`.** No hex, px value or font name in a declaration. Keywords (`none`, `transparent`, `currentColor`, `inherit`) and layout math (`-50%`, `100vw`, `1fr`) are fine.
- **No text outside an order block** except the file's header comment, and no two blocks share a number.

## The files

There are 56 files. Each is named after its component in `ui/inventory.md` (kebab-case), apart from two that aren't inventory components:
- `base.css`: the page root every screen sets (`.onrace`), with box sizing, type, focus, selection and links.
- `screen.css`: the phone screen's frame and scroll areas (`ui/shell.html`), and the list and map panels.

**Where a rule names more than one component,** it went to the file whose look it defines. The shared part of a few looks sits in one file:
- the buttons' common base is in `primary-button.css`;
- the text-link look shared by `.official a`, `.row-note a`, `.alert-link` and `.forgot a` is in `text-link.css`;
- the error icon shared by `.inline-error`, `.field-error` and `.row-note.is-error` is in `inline-error.css`.

**Not here:**
- **The map's data** (Natural Earth masks, the map's ratio, each pin's place) is in `ui/map-data.css`, written by `scripts/concept/build_map.py`; the map's six design tokens (dot, label height and gap, water, land, lines) are in `tokens.css`. Only the pages that show the static map link it.
- **The showcase's stages** (`.kit-frame`, `.kit-stage`, `.kit-shell`, `.kit-tabbar`) are documentation: they're in `ui/kit-doc.css`. The tab bar specimens are small screens in frames, so the bar is the body's child, as on a screen, and no product selector names the showcase.
