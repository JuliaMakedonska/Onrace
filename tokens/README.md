# Tokens

Lesson 8: the kit's values as two levels of design tokens.

- **`tokens-audit.md`:** step 1, the audit of `ui/kit.css` and `ui/map.css`, with every token, its uses, its roles and the findings. It also holds step 2's mapping (old variable → new token) for steps 3–4.
- **`tokens.css`:** step 2 (2026-10-27).
  - **Primitives:** raw values with no roles in their names. Colors are named by hue and L*.
  - **Semantic:** the color roles, each a `var()` of a primitive.
  - No page links it yet. The kit switches to it in steps 3–4.
