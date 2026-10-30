# Tokens

Lesson 8: the kit's values as two levels of design tokens.

- **`tokens-audit.md`:** step 1, the audit of `ui/kit.css` and `ui/map.css`, with every token, its uses, its roles and the findings. It also holds step 2's mapping (old variable → new token) for steps 3–4.
- **`tokens.css`:** step 2 (2026-10-27).
  - **Primitives:** raw values with no roles in their names. Colors are named by hue and L*.
  - **Semantic:** the color roles, each a `var()` of a primitive.
  - Since step 4 (2026-10-28) every page that shows the product links it, then `components/index.css`. `ui/kit.css` and `ui/map.css` are gone.
  - Hex values live only here: `DESIGN.md`'s frontmatter values and `.impeccable/design.json` are generated from it (`scripts/build_design_sidecar.py`).
- **`theme.js`** and the light block (step 5, 2026-10-30, the theme stress test): `tokens.css` ends with `:root[data-theme="light"]`, which overrides semantic roles only. `theme.js`, in each page's `<head>`, sets `data-theme="light"` from `?theme=light` and keeps it for the tab, so a state change keeps it. Onrace stays dark-only (C5) until the designer decides. The contrast of every role pair in both themes is a generated comment at the end of `tokens.css` (`scripts/concept/build_stand.py`).
