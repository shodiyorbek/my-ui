# Springs

A spring doesn't play a fixed animation. It pulls a value toward a target, like a physical object. That gives you three things tweens (duration + easing curve) can't: it can be **interrupted and reversed mid-flight without a jump**, it **carries the user's velocity** from a drag into the animation, and it **settles naturally** instead of stopping on a timer. Those three properties are most of what makes the ChatGPT macOS app and iOS feel fluid.

**Springs are not bounce.** Every house default is *critically damped* (damping ratio 1): it arrives as fast as possible with zero overshoot. Bounce is allowed in exactly one case (see *When to add bounce*).

Sources: [apple-design](../references/vendor/emilkowalski/apple-design/README.md) §3–6 (Apple's *Designing Fluid Interfaces*), [emil-design-eng](../references/vendor/emilkowalski/emil-design-eng/README.md) *Spring Animations*, Craft's [interruptibility](../references/vendor/gustavo-fior/articles/motion/interruptibility.mdx) and [icon-morph](../references/vendor/gustavo-fior/articles/motion/icon-morph.mdx). The Motion conversions below were verified against the `motion@13.4.6` source.

## 1. Spring or tween?

| Situation | Use | Why |
|---|---|---|
| Anything the user drags, flicks or swipes (sheets, drawers, carousels, swipe-to-dismiss, sliders, reorder) | **Spring, physics params + release velocity** | Only springs continue the gesture's momentum |
| Anything that can be toggled back and forth quickly (switches, sidebars, accordions, segmented thumbs, expand/collapse) | **Spring** | Reverses smoothly mid-flight |
| Layout changes and shared-element morphs (item moves, list reorders, card → modal) | **Spring** (`smooth`) | Retargets cleanly when layout changes again mid-animation |
| Icon swaps (copy → check) | **Spring** `bounce: 0`, ~0.3s | Snap without wobble |
| Simple enter/exit of popovers, tooltips, toasts, dialogs | **Tween** (`--ease-out`, 150–250ms) or a CSS spring token | Fixed, short, rarely interrupted, and cheaper on the main thread |
| Hover, color, opacity-only changes | **Tween or instant** | Nothing to carry. Springs add nothing here |
| Loading spinners, progress, marquees | **Linear keyframes** | Constant motion |
| Keyboard-triggered, 100+/day actions | **Nothing** | Instant beats any animation |

## 2. The two numbers

Think in Apple's terms. They're the easiest to reason about:

- **Damping ratio** controls overshoot. `1.0` means no bounce (the house default). `0.85` gives a ~1% overshoot you feel more than see. Below `0.7` it reads as bouncy, which is out of style for this library.
- **Response** is roughly how long it takes to get there, in seconds (one undamped period). Lower is snappier. It is **not** the total duration: a spring's settle time comes out of the physics (≈1.5× response for damping 1).

## 3. House presets

These are defined once in `tokens/tokens.json` → `spring`, and generated into `tokens.css` as CSS easings.

| Preset | Damping | Response | Settles | Use |
|---|---|---|---|---|
| `snappy` | 1.0 | 0.30s | 441ms | Switches, toggles, small state changes, icon swaps |
| `smooth` | 1.0 | 0.40s | 588ms | **Default.** Popovers, panels, sidebar, layout shifts, card→modal morph |
| `gentle` | 1.0 | 0.55s | 809ms | Large surfaces opened by click (sheets, full-page transitions) |
| `flick` | 0.85 | 0.40s | 558ms | Only after a drag/flick released with momentum. ~1% overshoot |

The same preset in every API. Run `python scripts/spring.py <damping> <response>` for any other values:

| API | `smooth` (1.0 / 0.4s) |
|---|---|
| Motion, **physics** (use for gestures) | `{ type: "spring", stiffness: 247, damping: 31.4, mass: 1 }` |
| Motion, time-based | `{ type: "spring", visualDuration: 0.333, bounce: 0 }` |
| SwiftUI | `.spring(response: 0.4, dampingFraction: 1.0)` |
| React Native Reanimated | `withSpring(v, { stiffness: 247, damping: 31.4, mass: 1 })` |
| CSS | `transition: transform var(--spring-smooth-duration) var(--spring-smooth)` |
| No library (JS) | `mySpring.createSpring({ preset: "smooth" })` from `lib/spring.js` |

Conversions: `stiffness = (2π / response)²`, `damping = 2 × ratio × √stiffness`, Motion `visualDuration = response / 1.2` and `bounce = 1 − ratio`.

## 4. The gotcha: time-based springs drop velocity

In Motion, a spring defined by **`visualDuration`/`duration` + `bounce` ignores the velocity it's handed.** The source says so: *"Time-defined springs ignore inherited velocity."* That's fine for click-triggered animations, but it silently kills the momentum handoff that makes a flicked sheet feel real.

**Rule: anything released from a gesture uses the physics form (`stiffness`/`damping`) with the release velocity.**

```jsx
// Motion: drag a sheet, release, and it continues at the finger's speed
<motion.div
  drag="y"
  dragConstraints={{ top: 0, bottom: 0 }}
  dragElastic={0.2}                                   // rubber-band past the bounds
  dragTransition={{ bounceStiffness: 247, bounceDamping: 31.4 }}
  onDragEnd={(e, info) => {
    const projected = info.offset.y + project(info.velocity.y);   // where the flick would land
    const target = nearestSnapPoint(projected);
    animate(y, target, { type: "spring", stiffness: 247, damping: 26.7, velocity: info.velocity.y }); // flick preset
  }}
/>
```

## 5. The fluid-gesture recipe

This comes from Apple's *Designing Fluid Interfaces*. `lib/spring.js` implements every piece without dependencies, and `examples/springs.html` is a working sheet built with it.

1. **Respond on pointer-down.** Stop any running animation at its *current* position (`spring.set(spring.value)`), never snap to the target.
2. **Track 1:1** during the drag, keeping the grab offset. Use `setPointerCapture`. Past a boundary, apply `rubberband()` instead of a hard stop.
3. **Measure release velocity** from the last ~100ms of pointer samples (`velocityTracker()`).
4. **Project** where the flick would come to rest: `current + project(velocity)`. Choose the snap point nearest the *projection*, not the release point. That's what lets a small, quick flick throw a sheet closed.
5. **Hand off velocity**: `spring.to(target, { velocity, preset: "flick" })`. There's no seam between finger and animation.
6. **Stay grabbable**: if the user touches it again mid-flight, go back to step 1.

## 6. CSS springs (no JS)

`tokens.css` exposes each preset as a `linear()` easing plus its matching duration. They must be used together:

```css
.switch-thumb { transition: transform var(--spring-snappy-duration) var(--spring-snappy); }
.sidebar      { transition: transform var(--spring-smooth-duration) var(--spring-smooth); }
```

- CSS springs get the *curve* of a spring but not its physics. When interrupted, a transition restarts from the current position with zero velocity. That's fine for clicks and toggles, but not good enough for gestures.
- All critically damped presets share one curve shape; only the duration differs. That's physics, not a bug.
- `linear()` is supported in all current browsers. Older browsers ignore the declaration and fall back to `ease`, which is acceptable.

## 7. When to add bounce

Only when **the user's own motion carried momentum into it**: a flick released, a card thrown, a drag let go past a snap point. Then use `flick` (0.85). The overshoot is the physical echo of their throw, so it reads as right.

Never add bounce to things that simply appear (menus, dialogs, toasts, tooltips), to hover, or to anything keyboard-triggered. On a menu that fades in, overshoot reads as a toy. That's the measured failure of bencho.dev, which has 90+ overshoot curves.

**Decorative exception:** mouse-follow effects (tilt cards, cursor followers) may use a soft, bouncy spring (Emil's `stiffness: 100, damping: 10`, ratio 0.5), because they have no functional meaning. Never use it on functional UI.

## 8. Rules

- Animate `transform` and `opacity` with springs, never `width`/`height`/`top`. For layout changes use FLIP (Motion `layout`, `layoutId`).
- **Never block input while a spring settles.** The tail of a critically damped spring is long and imperceptible. The UI is interactive the moment the gesture ends.
- Decompose 2D motion into independent X and Y springs, each with its own velocity.
- With `prefers-reduced-motion: reduce`, jump to the target (`lib/spring.js` does this automatically) or cross-fade opacity. No travel, no scale, no overshoot.
- Keep one preset per interaction type across the product. Consistent physics is what makes surfaces feel like one material.

## Resolved conflicts

| Topic | Source says | House choice | Why |
|---|---|---|---|
| Craft's `--ease-spring` token | a CSS `linear()` spring with **16% overshoot** | **Removed**; replaced by generated, critically damped presets | 16% overshoot on UI breaks "no bounce" |
| Craft interruptibility demo | `stiffness: 300, damping: 30` (ratio 0.87) | Covered by `flick` (0.85) for gestures; `snappy` for toggles | Toggles are click-driven, so no momentum means no overshoot |
| Emil, mouse-follow | `stiffness: 100, damping: 10` (ratio 0.5) | Decorative use only | Too bouncy for functional UI |
| Apple drawer | damping 0.8, response 0.3 | `flick` 0.85 / 0.4 | Slightly calmer to match the soft style; still carries momentum |
| Jakub, icon transitions | `{ duration: 0.3, bounce: 0 }` | Kept as is (≈ `snappy`) | Already critically damped |
