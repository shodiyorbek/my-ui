# Motion

Motion in a soft UI is felt more than seen. It confirms that something happened and where it went, and never shows off. The values here are the house style. Where the upstream sources disagree, this file decides (see *Resolved conflicts*).

Deep dives: [emil-design-eng](../references/vendor/emilkowalski/emil-design-eng/README.md), [apple-design](../references/vendor/emilkowalski/apple-design/README.md), [better-ui animations](../references/vendor/jakubkrehel/better-ui/animations.md), and Craft's articles in [`references/vendor/gustavo-fior/articles/motion/`](../references/vendor/gustavo-fior/articles/motion/) (live demos at craft.gustavofior.com).

## 1. Should it animate at all?

| How often the user sees it | Decision |
|---|---|
| 100+ times/day (shortcuts, command palette, sending a message, toggling a sidebar by key) | **No animation.** Instant. |
| Tens of times/day (hovering nav/list/menu items, list navigation, tab switch) | **Instant** highlight. No transition on hover backgrounds you sweep across. |
| Occasional (menus, popovers, dialogs, toasts, sheets) | Standard motion below |
| Rare (onboarding, empty states, success moments) | May stagger or add a little delight |

Decide by frequency and intent, not by input device. Every animated change also needs a static cue (color, icon, label), so motion is never the only signal.

## 2. Values

```css
--ease-out:    cubic-bezier(0.23, 1, 0.32, 1);   /* enter, press: the default */
--ease-in-out: cubic-bezier(0.77, 0, 0.175, 1);  /* things moving across the screen */
--ease-drawer: cubic-bezier(0.32, 0.72, 0, 1);   /* sheets, drawers (iOS-like) */
--ease-spring: linear(…);                         /* CSS spring with a small overshoot, for playful toggles only */
```

| Element | Enter | Exit | Easing |
|---|---|---|---|
| Press feedback (`:active`) | 100ms | 100ms | `--ease-out` |
| Hover on list/nav/menu items | instant | instant | none |
| Hover on a standalone button | ≤ 150ms color/opacity | same | `ease` |
| Tooltip | first one waits 400–700ms, then fades in over 125ms. Neighbours open instantly with no animation | 0–100ms | `--ease-out` |
| Dropdown, popover, select | 180ms | 90–120ms | `--ease-out` |
| Dialog | 220ms | 120ms | `--ease-out` |
| Toast | 240ms | 120ms, fade + blur, no travel | `--ease-out` |
| Sheet / drawer | 300ms | 200ms | `--ease-drawer` |
| List item removed | n/a | 160ms: fade + collapse height so rows below slide up | `--ease-out` |

**Exits run at about half the enter duration.** The user is done with the thing, so don't make them watch it leave. **Never use `ease-in` on entrances.** It delays the first frames, which is exactly when the user is watching.

Springs (Motion / Framer Motion) are for gestures and anything the user can grab or flick back and forth (switches, sidebars, drag handles): `{ type: "spring", duration: 0.3, bounce: 0 }`, or `{ stiffness: 300, damping: 30 }`. Only add bounce (`0.15`) when the user's own flick carried momentum.

## 3. Recipes

**Press:** anything pressable (buttons, cards, rows, chips).
```css
.pressable { transition: transform 100ms var(--ease-out); }
.pressable:active { transform: scale(0.97); }   /* large cards: 0.98 */
```

**Popover / menu:** scale from the trigger, never from 0.
```css
.popover {
  transform-origin: var(--transform-origin, top center);   /* dialogs stay centered */
  transition: opacity 180ms var(--ease-out), transform 180ms var(--ease-out);
  @starting-style { opacity: 0; transform: scale(0.95); }
}
.popover[data-closed] { opacity: 0; transform: scale(0.95); transition-duration: 120ms; }
```

**Exit (toast, notice):** fade with a touch of blur, no travel, half the time.
```css
.toast[data-closing] { opacity: 0; filter: blur(2px); transition: opacity 120ms var(--ease-out), filter 120ms var(--ease-out); }
```

**Stagger (rare entrances only):** `opacity 0→1`, `translateY(8px)→0`, 360ms `--ease-out`, **40ms** between items. Cap the total so the last item starts within ~300ms of the first (step = 300ms ÷ count). Only stagger visible rows. Never block clicks while items fade in.

**Icon swap** (copy→check, send→stop): cross-fade with scale `0.25→1`, opacity `0→1`, blur `4px→0`, spring `{ duration: 0.3, bounce: 0 }`. Keep both icons in the DOM, one absolutely positioned. For related shapes (hamburger→X), move the lines instead.

**Crossfade that looks "doubled":** add `filter: blur(2px)` during the transition to merge the two states.

## 4. Rules

- Transition named properties only (`transition-property: transform, opacity`), never `all`. Keep press timing separate from hover color timing.
- Animate only `transform`, `opacity`, `filter`, `clip-path`. The one exception is collapsing a removed list row's height, and that stays short (160ms).
- Use CSS **transitions** for toggles (they retarget mid-flight), **keyframes** only for one-shot, uninterruptible things like spinners, and **springs** for gestures.
- No enter animation on first page render (`AnimatePresence initial={false}`).
- Theme switch: disable all transitions for one frame so the page snaps instead of smearing.
- Hover effects only under `@media (hover: hover) and (pointer: fine)`.
- `prefers-reduced-motion: reduce`: keep opacity and color fades, drop movement and scale.

## 5. Sound (optional)

Only use sound for completed actions where the user's eyes may be elsewhere (sent, copied, saved, upload done, a calm error). Never on typing, scrolling, menus or navigation, or anything that can fire twice in a second. Keep it very quiet (gain ≈ 0.05–0.1), always paired with a visual change, and provide an obvious, remembered mute. See [interface-sfx](../references/vendor/gustavo-fior/articles/sound/interface-sfx.mdx).

## Resolved conflicts

| Topic | Emil Kowalski | Jakub Krehel | Gustavo Fior | House choice | Why |
|---|---|---|---|---|---|
| Press scale | `0.97` | `0.96` | `0.97` (`0.98` for large surfaces) | **`0.97`, `0.98` large** | Two of three agree, and it's the softer option |
| Press duration | 100–160ms | n/a | ~100ms | **100ms** | Matches Apple's value too. Longer lags behind the finger |
| Standard curve | `cubic-bezier(0.23,1,0.32,1)` | `cubic-bezier(0.2,0,0,1)` | `cubic-bezier(0.23,1,0.32,1)` | **`0.23,1,0.32,1`** | Two of three agree, and it feels instant |
| Stagger step | 30–80ms | ~100ms | 30–60ms (40ms in code), cap ~300ms total | **40ms, capped at 300ms total** | Gustavo's cap solves the long-list problem |
| Exit easing | never ease-in | ease-out | ease-in is OK for exits | **ease-out** | One curve is simpler, and at 120ms the difference is invisible |
| Hover transition | reduce or remove | ≤ 150ms | instant | **instant on list/menu/nav, ≤ 150ms on standalone buttons** | Sweeping across items must never lag the pointer |
