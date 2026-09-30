# Tokens

`tokens.json` is the only place raw design values live. `tokens.css` is generated from it by `python scripts/build_tokens.py`. Never edit the CSS by hand; the validator fails if it's out of date.

Every variable is `--<group>-<name>`: `--color-text-muted`, `--space-4`, `--radius-lg`, `--shadow-ring`, `--ease-out`, `--duration-fast`.

- **Plain CSS:** import `tokens.css` once at the app root.
- **Tailwind v4:** import `tokens.css`, then in `@theme` map e.g. `--color-bg: var(--color-bg);`, `--radius-lg: var(--radius-lg);`, or use arbitrary values like `bg-(--color-surface)`.
- **Tailwind v3:** in `theme.extend`, set `colors: { bg: 'var(--color-bg)', … }` and so on.
- **Dark mode:** follows the OS by default. `data-theme="light|dark"` on `<html>` forces a theme.

## Rules

- Components use **semantic** color roles only (`text-muted`, `surface-hover`), never a value picked because it looks right.
- `text-faint` is under 4.5:1 on purpose. Use it only for disabled and decorative text, never for information.
- The validator checks `text`, `text-muted`, `accent`, `danger` and `success` against `bg`, `bg-subtle`, `surface` and `surface-hover` in both themes, and requires 4.5:1.
- Adding a role: add it to `tokens.json` with both light and dark values, rebuild, validate.
