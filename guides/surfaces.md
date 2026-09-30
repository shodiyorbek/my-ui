# Surfaces, color, depth

How to get the clean, soft look without it turning into grey mush. Deep dives: [better-ui surfaces](../references/vendor/jakubkrehel/better-ui/surfaces.md), [better-colors](../references/vendor/jakubkrehel/better-colors/README.md), [apple-design materials](../references/vendor/emilkowalski/apple-design/README.md).

## Color

- **Neutral first.** One neutral ramp does 95% of the work. The accent is optional. The default primary action is an inverted neutral (`--color-primary` = near-black in light mode, near-white in dark).
- **Semantic tokens only.** Components use `--color-bg`, `--color-surface`, `--color-text-muted`…, never hex or primitives. The values are in `tokens/tokens.json`.
- **Soften the ends.** Background isn't pure white in every region, and text isn't pure black. Dark mode is a dark gray (`#212121`-ish), not `#000`.
- **One filled primary per view.** Peers are neutral (ghost or subtle).
- **Muted ≠ illegible.** Secondary text still has to reach 4.5:1 on the surface it actually sits on. Measure it, don't guess.

## Layering (how regions separate)

Use this order, and stop at the first one that works:
1. **Space.** Group gaps ≥ 2× the gaps inside a group.
2. **Tone shift.** Sidebar `--color-bg-subtle`, main `--color-bg`, raised input `--color-surface`.
3. **Shadow ring.** `--shadow-ring` (a 1px transparent-black ring plus a soft lift). This replaces borders on cards, inputs, buttons and menus.
4. **Border.** Only for structural dividers (table rows, hairline separators) and focus/selected states.

## Radius

- Scale: `sm 8` · `md 12` · `lg 16` · `xl 24` · `full`. Small controls use `md`, cards and composers `lg`–`xl`, and chips and single-line inputs can go `full`.
- **Concentric:** outer radius = inner radius + padding. A `12px` button inside an `8px`-padded container → container radius `20px`. Past 24px of padding, choose each radius independently.

## Depth & elevation

| Level | Use | Token |
|---|---|---|
| 0 | Page, sidebar | none |
| 1 | Cards, inputs, composer | `--shadow-ring` |
| 2 | Menus, popovers, tooltips | `--shadow-float` |
| 3 | Dialogs, sheets | `--shadow-overlay` + scrim `--color-scrim` |

In dark mode, shadows mostly disappear. Rely on the ring (`oklch(1 0 0 / 0.08)`) and a lighter surface tone for elevation.

**Translucent chrome** (sticky headers, toolbars): `background: color-mix(in oklab, var(--color-bg) 72%, transparent); backdrop-filter: blur(20px) saturate(180%);`. Instead of a hard border, fade the edge where content scrolls under it. Never stack translucent on translucent. Respect `prefers-reduced-transparency`.

## Details

- Images get `outline: 1px solid oklch(0 0 0 / 0.1); outline-offset: -1px` (white/0.1 in dark), never a tinted gray.
- Icons use `currentColor`, with 1.5px stroke next to regular text and 2px next to semibold. One icon set per product.
- Icon + text buttons: 2px less padding on the icon side. Play triangles are nudged 1–2px right.
- Focus: a visible 2px ring with offset, drawn in `--color-focus`. Soft doesn't mean invisible focus.
