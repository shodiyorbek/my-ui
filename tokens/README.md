# Tokens

`tokens.json` is the only place raw design values live. Components and pages reference tokens by name.

- CSS: expose as variables, e.g. `--color-primary`, `--space-4`, `--radius-md`.
- Tailwind: map them into `theme.extend` so classes like `bg-primary` and `p-4` resolve to tokens.
- Colors have `light` and `dark` values; always handle both.

## Rules

<!-- Add token-level rules here, e.g. "4px base grid", "never pure black text". -->
- TODO: add your rules.
