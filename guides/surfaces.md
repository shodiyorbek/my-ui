# Surfaces, color, depth

How to get the clean, soft look without it turning into grey mush. Deep dives: [better-ui surfaces](../references/vendor/jakubkrehel/better-ui/surfaces.md), Craft's [color](../references/vendor/gustavo-fior/articles/color/) and [layout](../references/vendor/gustavo-fior/articles/layout/) articles, [better-colors](../references/vendor/jakubkrehel/better-colors/README.md), [apple-design materials](../references/vendor/emilkowalski/apple-design/README.md).

## Color

- **Neutral first.** One neutral ramp does 95% of the work. The accent is optional. The default primary action is an inverted neutral (`--color-primary` = near-black in light mode, near-white in dark).
- **Semantic tokens only.** Components use `--color-bg`, `--color-surface`, `--color-text-muted`…, never hex or primitives. The values are in `tokens/tokens.json`.
- **Soften the ends.** Background isn't pure white in every region, and text isn't pure black. Dark mode is a charcoal (`#0f0f0f`–`#212121`), never `#000`. Pure black was measured on bencho.dev and it's the harshest thing on that site.
- **One dominant action per task or independent section.** Supporting actions are quieter (ghost or subtle); independent forms may each have a primary.
- **Muted ≠ illegible.** Secondary text still has to reach 4.5:1 on the surface it actually sits on. Measure it, don't guess.

## Layering (how regions separate)

Use this order, and stop at the first one that works:
1. **Space.** Group gaps ≥ 2× the gaps inside a group.
2. **Tone shift.** Sidebar `--color-bg-subtle`, main `--color-bg`, raised input `--color-surface`.
3. **Wash or ring.** Either a **wash**, `--color-wash` (the text color at ~6%, translucent, with no edge at all; bencho.dev's cards), for items that sit *on* a surface (grid cards, chips, user message bubbles). Or a **ring**, `--shadow-ring` (1px transparent ring plus a soft lift; Craft), for things that float *above* it (inputs, composer, menus, standalone cards). Both are derived from the text color at low alpha, so they work on any background and in both themes.
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
| 3 | Dialogs, sheets | `--shadow-overlay` + scrim `--color-scrim` with `backdrop-filter: blur(20px) saturate(130%)` |

**Build every level from the same first two layers** (the 1px ring and the tight contact shadow), then add softer, wider layers for height. That's what makes levels read as the same material at different heights. No layer should be consciously visible: if you can see the shadow, it's too strong.

**Dark mode:** a dark shadow on a dark page is invisible, so the edge comes from light. The dark tokens use a faint inset white ring plus a 1px inset top highlight (light catching the top edge), with dark outer layers kept for separation. Primary buttons get `--shadow-primary`, which gives the filled button a crisp edge in both themes.

**Scrims frost, they don't darken.** The scrim is the page color at ~78% plus a blur, so the page behind a dialog looks frosted rather than blacked out.

**Translucent chrome** (sticky headers, toolbars): only turn glass on once content actually scrolls under it; at the top it's flat. Then use `background: color-mix(in oklab, var(--color-bg) 72%, transparent); backdrop-filter: blur(20px) saturate(180%);`. Instead of a hard border, fade the edge where content scrolls under it. Never stack translucent on translucent. Respect `prefers-reduced-transparency`.

## Details

- **Paint the canvas:** set `background-color: var(--color-bg)` on `html`, not just on a wrapper, so overscroll never flashes white in dark mode. Keep `<meta name="theme-color">` in sync with the theme.
- **Scroll fades instead of hard edges:** a scroll container fades its content out at the edge that can still scroll, using `mask-image: linear-gradient(to bottom, transparent, black 2.5rem, black calc(100% - 2.5rem), transparent)`. Only fade a side that has more content (track it on scroll). Hide the scrollbar on horizontal chip/tab rows and let the fade do its job.
- **Squircles (progressive enhancement):** on large radii (avatars, app icons, big cards) add `corner-shape: squircle` (≈ `superellipse(2)`) next to the same `border-radius`. Browsers without support keep the round corner, so it's safe.
- **Noise (optional):** on large flat color fields that show banding (a colored hero or card), overlay SVG `feTurbulence` grain at ~8% opacity with `mix-blend-mode: overlay` inside an `isolation: isolate` container. Tile it on big areas for performance. Never on plain neutral UI.
- Images get `outline: 1px solid oklch(0 0 0 / 0.1); outline-offset: -1px` (white/0.1 in dark), never a tinted gray.
- Icons use `currentColor`, with 1.5px stroke next to regular text and 2px next to semibold. One icon set per product.
- Icon + text buttons: 2px less padding on the icon side. Play triangles are nudged 1–2px right.
- Focus: a visible 2px ring with offset, drawn in `--color-focus`. Soft doesn't mean invisible focus.
