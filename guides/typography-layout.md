# Typography & layout

Clean means few sizes, few weights, and consistent edges. Deep dives: [better-typography](../references/vendor/jakubkrehel/better-typography/README.md), [better-layout](../references/vendor/jakubkrehel/better-layout/README.md), Craft's [typography](../references/vendor/gustavo-fior/articles/typography/) articles.

## Type

- **Font:** system UI stack (SF Pro on macOS) or Inter. One family for UI, optionally a mono for code.
- **Scale:** `12 · 13 · 14 · 16 · 20 · 24 · 32` px. App UI body is 14–16px. Chat and reading text is 16px.
- **Weights:** 400 and 500 for UI, 600 for headings. Nothing lighter than 400 below 18px.
- **Line-height:** UI body 1.5, long-form reading text 1.65–1.8 (Craft uses 1.8), UI labels 1.3–1.4, headings 1.1–1.2. Unitless values only.
- **Quiet headings:** in apps, headings stay small (16–20px, weight 500). Hierarchy comes from weight and muted color, not size. Big display type is for marketing heroes only.
- **Tracking:** tighten as size goes up, loosen as it goes down, and leave body text alone. Headings ≥ 24px get `-0.02em` (Inter's curve settles there). Small uppercase labels and pills get `+0.05em` to `+0.1em` (use `0.06em`).
- **Measure:** reading text is capped at ~65ch (chat column ≈ 680–760px).
- `text-wrap: balance` on headings, `pretty` on short descriptions, `tabular-nums` on any changing number.
- On `body`: `-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale;`. On macOS this stops light-on-dark text blooming half a weight heavier. Check any weight ≤ 300 after turning it on.
- Hierarchy comes from weight and color (text vs. text-muted) before size.

## Layout

- **4px grid.** Spacing steps `4 · 8 · 12 · 16 · 24 · 32 · 48 · 64`.
- **Group with space:** 8px inside a group, 16–24px between groups, 48px+ between sections.
- **Controls:** 36px height (compact), 40px (default), 44px (touch). Horizontal padding 12–16px.
- **Shared edges:** content and controls align to the same inline edges. Every stray edge adds noise.
- **App shell:** adapt sidebar width to labels, density, and available space; 260–280px is a starting point for a reading app, not a fixed rule. Constrain reading/forms; let data-heavy workspaces use available width. Keep top chrome quiet, adding translucency only when scrolling content needs separation.
- **Content bleeds, controls float:** backgrounds go edge to edge, while controls stay inside margins and safe areas.
- Logical properties (`padding-inline-start`), container queries for components, and breakpoints set where the content breaks.

## Spacing by relationship

Use the existing spacing scale to name four roles: page gutter, section separation, group gap and item gap. Keep a label or heading closer to its supporting content than to the next group. Do not give all sibling elements the same gap merely because they share a container.

For reading layouts, center the constrained column in the available content pane after accounting for navigation. For discovery grids, align media, title and description edges and preserve their grouping when columns collapse. For operational dashboards, keep useful density; large demonstration stages are not a model for ordinary metric cards.

On narrow screens, reduce columns and outer gutters before reducing body text. Keep deliberate internal padding and allow long labels to wrap where their full meaning matters. Check callout text against the surrounding reading edge even when its background extends outward.

Before delivery, compare one page introduction, one section boundary and one repeated component at desktop and narrow widths. Look for accidental double margins, detached labels, uneven card insets and headings that compete with content. Reference measurements and adaptation limits: [Animations.dev visual review](../references/sites/animations-dev.md#platform-visual-system-review).
