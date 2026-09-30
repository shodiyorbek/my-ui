# The feel: soft, clean, frictionless

The target is the feeling of apps like the ChatGPT macOS app, Linear, Things or Raycast. The interface gets out of the way, responds before you finish thinking, and never makes you wait, re-type or hunt. "Soft" isn't a style you add on top. It's what's left once you remove every hard edge, harsh contrast, jolt and unnecessary step.

The ChatGPT description below comes from how the app looks. It isn't a measured spec, so treat its specific values as approximations.

## What makes an app like the ChatGPT desktop app feel soft

- **Almost no color.** Neutral grays, near-black text, white or near-black backgrounds. The primary action is often just an inverted neutral (a black button in light mode, white in dark), not a brand color. Color is kept for meaning.
- **Low-contrast structure.** Sidebar vs. content is separated by a slight shift in background tone, not a line. Borders, where they exist, are faint (≈5–10% black).
- **Generous, rounded surfaces.** The composer is a big rounded container (pill-like on a single line, a large-radius card when it grows). Nested elements follow concentric radii.
- **One focal point per view.** Everything else is quiet: muted secondary text, icon-only toolbar controls that fade in on hover.
- **Space instead of dividers.** Messages are separated by whitespace, not boxes and rules.
- **Motion you barely notice.** Things appear with a short fade/translate. Nothing bounces, and nothing animates on actions you repeat all day.
- **Zero-wait interaction.** Your message appears instantly, responses stream in, the input stays focused and remembers drafts. Nothing jumps as content loads.

## The five laws

1. **Softness = low contrast between neighbours, high contrast for content.** Surfaces, borders and chrome sit close in tone to each other. Text and the one primary action carry the contrast. Never make body text soft: it must still pass 4.5:1.
2. **Remove before you add.** Before adding a border, a divider, a color or an animation, try space, a tone shift, or nothing. See [surfaces.md](surfaces.md).
3. **Respond instantly, animate briefly.** Feedback on pointer-down. UI motion ≤ 250ms, ease-out, no bounce. Repeated actions get no animation. See [motion.md](motion.md).
4. **Never make the user wait, re-do or guess.** See [frictionless.md](frictionless.md).
5. **Details compound.** Concentric radii, optical alignment, tabular numbers, balanced headings. Nobody notices one of them, but everyone notices when they're all missing.

## Anti-patterns (the "hard" UI checklist)

| Hard | Soft |
|---|---|
| `border: 1px solid #ccc` around every card | Tone shift or `--shadow-ring` (see surfaces) |
| Brand-colored everything | Neutral UI, one filled primary per view |
| Pure `#000` text on pure `#fff` | `--color-text` on `--color-bg` (slightly softened both ends) |
| Dividers between every list row | 8px gaps within groups, 16px+ between groups |
| 300–500ms animations, bouncy springs | 150–250ms ease-out, `bounce: 0`; exits at half the time |
| Hover backgrounds that fade in as you sweep a list | Instant highlight |
| White flash when overscrolling a dark page | `html` background set to the theme token |
| Hard cut-off at the edge of a scroll area | Edge-aware scroll fade |
| Black 50% scrim behind dialogs | Frosted scrim: page color at ~78% + blur |
| Glass header even at the top of the page | Flat at the top; glass only once content scrolls under it |
| Modal that pops in from nowhere | Modal that grows from the card that opened it |
| Modal "Are you sure?" confirmations | Do it, then offer Undo |
| Spinner that replaces content | Skeleton or optimistic content in place |
| Hover-only affordances on touch | Gate hover with `@media (hover: hover)` |
| Dense, cramped controls | 36–40px control height, 44px touch targets |
| 4 font sizes and 3 weights in one card | 2 sizes, 2 weights max per component |
