# build-component

Use when creating a new reusable component (not a one-off piece of a page).

1. Check `components/index.md` — if something close exists, extend it instead.
2. Copy `components/_template/` to `components/<kebab-name>/`.
3. Read `guides/feel.md`, plus `guides/motion.md` and `guides/surfaces.md`. Style only with variables from `tokens/tokens.css`. If a value is missing, propose a new token.
4. Cover states: default, hover, focus-visible, active, disabled, loading/empty where relevant, light + dark.
5. Accessibility: semantic element first, keyboard operable, visible focus ring, labels for icon-only controls, contrast ≥ 4.5:1 for text.
6. Fill in the README (purpose, props, usage, do/don't, tokens used).
7. Add the line to `components/index.md` and run `python scripts/validate.py`.
