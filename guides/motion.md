# Motion

Motion in a soft UI is felt more than seen. It confirms that something happened and where it went. It's never there to show off. The values here are the house style. Where the upstream sources disagree, this file decides (see *Resolved conflicts*).

Deep dives: [emil-design-eng](../references/vendor/emilkowalski/emil-design-eng/README.md), [apple-design](../references/vendor/emilkowalski/apple-design/README.md), [better-ui animations](../references/vendor/jakubkrehel/better-ui/animations.md), [enter-exit](../references/vendor/jakubkrehel/better-ui/enter-exit.md).

## 1. Should it animate at all?

| How often the user sees it | Decision |
|---|---|
| 100+ times/day (shortcuts, command palette, sending a message, typing) | **No animation.** Instant. |
| Tens of times/day (hover, list navigation, tab switch) | Color/opacity only, ≤ 150ms, or nothing |
| Occasional (menus, popovers, dialogs, toasts, sheets) | Standard motion below |
| Rare (onboarding, empty states, success moments) | May stagger / add a little delight |

Keyboard-triggered actions never animate. Every animated change also needs a static cue (color, icon, label), so motion is never the only signal.

## 2. Values

```css
--ease-out:    cubic-bezier(0.23, 1, 0.32, 1);   /* enter, exit, press — default */
--ease-in-out: cubic-bezier(0.77, 0, 0.175, 1);  /* things moving across the screen */
--ease-drawer: cubic-bezier(0.32, 0.72, 0, 1);   /* sheets, drawers (iOS-like) */
```

| Element | Duration | Easing |
|---|---|---|
| Press feedback (`:active`) | 120ms | `--ease-out` |
| Hover color/background | 150ms | `ease` |
| Tooltip | 125ms (0ms once one is already open) | `--ease-out` |
| Dropdown, popover, select | 180ms | `--ease-out` |
| Dialog | 220ms in / 160ms out | `--ease-out` |
| Sheet / drawer | 300ms | `--ease-drawer` |
| Toast | 250ms | `--ease-out` |

**Never `ease-in`** for UI: it delays the first frames, the exact moment the user is watching. Exits are faster and quieter than enters.

Springs (Motion / Framer Motion) are for gestures and anything the user can grab: `{ type: "spring", duration: 0.35, bounce: 0 }`. Only use bounce (`0.15`) when the user's own flick carried momentum.

## 3. Recipes

**Press:** every pressable thing.
```css
.pressable { transition: transform 120ms var(--ease-out); }
.pressable:active { transform: scale(0.97); }
```

**Enter/exit for a popover or menu:** scale from the trigger, never from 0.
```css
.popover {
  transform-origin: var(--transform-origin, top);   /* trigger side; dialogs stay centered */
  transition: opacity 180ms var(--ease-out), transform 180ms var(--ease-out);
  @starting-style { opacity: 0; transform: scale(0.96); }
}
.popover[data-closing] { opacity: 0; transform: scale(0.98); transition-duration: 120ms; }
```

**Soft entrance (rare moments only):** opacity + small translate + blur, staggered by ~60ms per semantic chunk (title, text, actions).
```css
from { opacity: 0; transform: translateY(8px); filter: blur(4px); }
```

**Icon swap** (copy → check, send → stop): cross-fade with scale `0.25→1`, opacity `0→1`, blur `4px→0`. Keep both icons in the DOM.

**Crossfade that looks "doubled":** add `filter: blur(2px)` during the transition to merge the two states.

## 4. Rules

- Transition named properties only (`transition-property: transform, opacity`), never `all`.
- Animate only `transform`, `opacity`, `filter` (and `clip-path`). Never animate `width`/`height`/`top`/`margin`.
- Use CSS transitions for state changes (they can be interrupted), keyframes only for one-shot sequences, and springs for gestures.
- No enter animation on first page render (`AnimatePresence initial={false}`).
- Theme switch: disable all transitions for one frame so the page snaps instead of smearing.
- Hover effects only under `@media (hover: hover) and (pointer: fine)`.
- `prefers-reduced-motion: reduce` → keep opacity/color fades, drop movement and scale.

## Resolved conflicts

| Topic | Emil Kowalski | Jakub Krehel | House choice | Why |
|---|---|---|---|---|
| Press scale | `0.97` | `0.96` | **`0.97`** | Softer; the goal is barely-felt feedback |
| Standard curve | `cubic-bezier(0.23,1,0.32,1)` | `cubic-bezier(0.2,0,0,1)` | **Emil's** | Stronger front-load, so it feels instant |
| Stagger step | 30–80ms | ~100ms | **60ms** | Soft feel favors a quick cascade |
