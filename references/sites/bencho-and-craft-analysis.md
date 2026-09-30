# Design reference analysis: bencho.dev + craft.gustavofior.com

Captured 2026-09-30 by the Claude Chrome extension in the user's browser, using `getComputedStyle` and each site's CSS. Values marked *measured* come from the site; *estimated* ones are judged from screenshots. What the library adopted from this is in `../index.md` and the `guides/` *Resolved conflicts* tables.

**Bottom line:** Craft is the closer match to "soft, clean, frictionless". Bencho is softer and more tactile but overuses bounce. Take Bencho's surfaces and press physics. Take Craft's restraint and its shadow system.

---

## 1. bencho.dev

### Browsed
Homepage (48-card masonry grid) with hovers; clicked like, dragged the image compare, opened the account menu; switched dark→light; opened 4 block-detail modals and changed their controls; opened the Sounds page.

### Colors (measured)

| Token | Light | Dark |
|---|---|---|
| Page bg `--bg` | `#fff` | `#000` |
| Surface / -2 / -3 | `#f7f7f6` / `#f1f1f0` / `#ecebe7` | `#0f0f0f` / `#181818` / `#202020` |
| Card fill `.bench-card` | `rgba(23,24,26,.06)`, no border | `rgba(255,255,255,.09)` |
| Menu/popover | `#fff` | `color-mix(ink 9%, bg)` ≈ `#171717` |
| Text `--ink` | `#17181a` | `#fff` |
| Muted `--ink-2…5` | `#3c3b37` `#5c5b56` `#6f6e68` `#85847e` | `#b4b4b4` `#9a9a9a` `#828282` `#6b6b6b` |
| Hero subtitle | `#a3a29c` | `#6b6b6b` |
| Hairline `--rule` | `#17181a29` | not checked |
| Accents | focus `#2231dd`, pick `#0d99ff`, ok `#15803d` | pick `#3aa9ff`, ok `#34d17a` |

Light-mode grays are warm (slightly yellow).

### Typography (measured)
Inter only (300–700). H1 40px/500/1.06, −0.022em. Big number 33px/500/1.0, −0.03em. Body 15px/400/1.5. Nav, chips, menu rows 14px/500. Buttons and small text 12.5–13.5px. `-webkit-font-smoothing: antialiased`; counters use `tabular-nums`.

### Spacing (measured)
Page padding `92px 20px 24px`. Masonry with 12px gaps, full-bleed. Hero subtitle max ~454px. Header 72px. Modal max 1000×640, inset 24, 12px gap, 300px side panel with 18px padding. Menu 240px wide, 4px padding, 44px rows with `0 16px` padding. Chips 32px tall, `0 14px` padding.

### Radius (measured)
Cards and modal panels 28. Menu 22 → rows 18 (concentric with 4px padding). Inner demo surfaces 18. Input 14. Slider bars 10. Pills, chips, segmented controls and round buttons 999px (162 uses). Images ~18–20 (estimated).

### Shadows and borders (measured)
- Cards: no shadow and no border, only the translucent fill.
- Menu: `0 0 0 1px rgba(ink,.06)`.
- Search pill after scrolling (glass): `rgba(elev,.74)`, `blur(8px) saturate(160%)`, ring `.06` plus `0 2px 10px rgba(shadow,.06)`.
- Modal side panel: `1px solid rgba(ink,.07)`, `rgba(elev,.86)`, `blur(14px) saturate(150%)`.
- Scrim: `color-mix(in srgb, var(--bg) 78%, transparent)` with `blur(22px) saturate(130%)`.
- Focus ring: `0 0 0 2px var(--bg), 0 0 0 4px rgba(ink,.35)`.

### Motion (measured)

**Curves:** `cubic-bezier(0.22,1,0.36,1)` ×59; overshoot `(0.24,1.34,0.38,1)` ×23; `(0.3,0.9,0.4,1)` ×19; more overshoots up to y=1.6.

**Durations:** 160ms (×103), 200, 260, 140, 220, 320.

| Interaction | Values |
|---|---|
| Nav link | color .16s; press scale .985 over .12s |
| Icon button hover | circle behind it goes opacity 0→1, scale .86→1 over .26s with overshoot; icon 1.04 |
| Icon button press | scale .96 with **90ms** duration on `:active`; release uses the normal 260ms |
| Small buttons | press .92–.95 |
| Card hover | label bar: opacity .2s + translateY 4→0 over .26s |
| Chips | bg and color .16s |
| Segmented control | bg and color .18s, no sliding thumb |
| Modal | card→modal shared-element morph over 380ms `(.33,.55,.2,1)`; scrim .26s; side panel translate 10px + opacity .24s, delayed 60ms; controls fade in after 40% |
| Like | keyframe scale .6→1.28→1 over 520ms; particles 620ms; odometer digits |
| Label input | SVG outline notch via `stroke-dashoffset` .32s |
| Notify button | width .46s with overshoot; text crossfade .2s |

Reduced motion is handled (scale removed, durations 1ms).

### Dark mode
The default. Pure `#000` bg; card wash .06→.09; muted grays become neutral; glass weaker; shadows darker.

### What makes it soft
1. Cards defined by translucent fill (ink at 6%), with no border or shadow.
2. Concentric radii everywhere (22/4/18).
3. Hover circles scale up from .86 behind icons.
4. Press is faster than release (90ms in, 260ms out).
5. Press amounts are small and scale with size (.985 text, .96 icons, .92–.95 tiny).
6. Glass appears only once you scroll.
7. The scrim tints and blurs instead of darkening.
8. The modal grows from the card that opened it.
9. Secondary info appears on hover.
10. Digit-wheel numbers with tabular-nums.

### Avoid
- Overshoot everywhere (90+ curves).
- Hover-only discovery, which hides things from touch users.
- Muted text failing contrast (≈3.9:1 dark, ≈2.5:1 light).
- Header with no backing over scrolling content.
- Slow deep links (3–5s placeholder).
- Pure `#000` dark background.
- A sponsored card in the grid, and a hero pill that clips its text.

### Items opened
Like, Image compare, Label input (`/blocks/label-input`), Liquid toggle (`/blocks/liq-toggle`), Notify (`/blocks/toasts`), the Sounds page. The settings panel uses pill segmented controls (36px tall, 2px padding, 32px buttons) and 44px drag-anywhere slider bars with `cursor: ew-resize`.

---

## 2. craft.gustavofior.com

### Colors (measured)

| Token | Light | Dark |
|---|---|---|
| Page bg | `#fafafa` | `#0f0f0f` |
| Card / popover | `#fff` | `#171616` |
| Text | `#171717` | `#ecedec` |
| Muted text | `#737373` | `#929292` |
| Muted / accent fill | `#f2f2f2` / `#f0f0f0` | `#1e1f1e` / `#272627` |
| Border / input | `#e5e5e5` | white at .10 / .15 |
| Ring | `#a1a1a1` | `#737272` |
| Destructive | `#e40014` | `#ff6467` |

No brand color. The "Soon" badge uses sky at 10%.

### Typography (measured)
Logo in Redaction serif at 16px. Inter for UI. Article H1 18px/500, H2 16px/500. Article body 14px / **1.8** in muted. Index body 14/20. Card title 13px/500, description 12px. Sidebar 12px. Badge 10px. JetBrains Mono for inline code at 0.8em.

### Layout (measured)
Content column 576px. Header padding `26px 32px`. Card grid 2 × 280px with a 16px gap. Menu demo: 4px padding, 32px items.

### Radius (measured)
Token 10px. Cards 18. Code blocks and menus 14 → items 10 (concentric). Buttons, segmented controls, badges full. Tooltip 18. Inline code 3.

### Shadows (measured)
No borders anywhere. `--custom-shadow`:
- Light: `0 0 0 1px #0000000f, 0 1px 2px -1px #0000000f, 0 2px 4px #0000000a`
- Dark: `inset 0 1px 0 #ffffff08, inset 0 0 0 1px #ffffff08, 0 0 0 1px #0000001a, 0 2px 2px #0000001a, 0 4px 4px #0000001a, 0 8px 8px #0000001a`

### Motion (measured)

| Interaction | Values |
|---|---|
| Sidebar links | color .2s |
| Icon buttons | .15s; `active:scale-[0.97]` |
| Gallery card hover | **no transition**; bg to card/80 (barely visible) |
| Segmented control | **clip-path thumb**: a second copy of the labels in the active color, clipped with `inset(2px 2px 2px Xpx round 9999px)`, `transition: clip-path .25s ease` |
| Tooltip | 150ms, fade + zoom-in-95 + 8px slide from the trigger side, `origin-(--transform-origin)`, instant for neighbours |

5 reduced-motion rules.

### Dark mode
Toggle cycles system → light → dark. Charcoal `#0f0f0f`, cards one step lighter, 6-layer shadow with a 3% white inset top edge.

### What makes it soft
Layered ring shadow instead of borders; dark cards catch light at the top; instant hover; clip-path segmented thumb; 0.97 press; concentric radii; inset image outlines; quiet type scale (headings 16–18px/500, body 1.8 leading); patient-then-instant tooltips; noise on colored fields.

### Avoid
- Many disabled "Soon" placeholders.
- Very small text (10–12px).
- The Optical Alignment article's text says the play icon moves left while its code moves it right; the code is correct.
- `<html>` background left transparent, against its own article.
- One missed click (not reproduced).
- Instant hover on large cards is so faint it feels dead.

### Items opened
Tabular Numbers, Nested Border Radius, Hover Restraint, Image Outlines, Noise, Optical Alignment, HTML Background, GOATs.

---

## Common patterns
1. No hard borders: translucent fills (Bencho) or a 1px ring shadow (Craft).
2. Colors derived from the text color at low alpha, so one rule works in both themes.
3. Concentric radii (22/4/18, 14/4/10) and pills for every chip, toggle and icon button.
4. Small press feedback: .96–.985, and .92–.95 on tiny controls. Press snaps in 90ms and releases slower.
5. Short durations of 150–260ms. 380–460ms only for spatial changes.
6. Curves `(0.22,1,0.36,1)` / `(0.23,1,0.32,1)`. Leave out Bencho's overshoots.
7. Pill segmented controls with a 2px inset. The clip-path version is the smoothest.
8. Muted text does the hierarchy work; headings stay at 16–18px/500.
9. Inter, antialiased, tabular numbers.
10. Reduced motion is respected on both sites.
11. Instant hover; animation goes on press and on open/close.
