# References

Captioned sources. Format per entry: **name**, link, *take* (what to copy), *ignore* (what not to), tags.

## Skills (copied into `vendor/`, MIT-licensed, licenses kept)

The house guides in `../guides/` distill these. Open the originals when you need the full reasoning or more recipes.

- **emil-design-eng** by Emil Kowalski ([source](https://github.com/emilkowalski/skills/tree/main/skills/emil-design-eng), [local](vendor/emilkowalski/emil-design-eng/README.md)). *Take:* the animation decision framework (frequency → purpose → easing → duration), custom easing curves, press scale, origin-aware popovers, clip-path techniques, gesture/drag details, Sonner principles. *Ignore:* the "Initial Response" greeting. tags: motion, polish, components
- **apple-design** by Emil Kowalski ([source](https://github.com/emilkowalski/skills/tree/main/skills/apple-design), [local](vendor/emilkowalski/apple-design/README.md)). *Take:* the fluid-interface physics (interruptibility, velocity handoff, momentum projection, rubber-banding), springs, translucent materials, optical typography. This is the closest source for the "macOS app softness". *Ignore:* the "Initial Response" greeting. tags: motion, gestures, materials, apple
- **better-ui** by Jakub Krehel ([source](https://github.com/jakubkrehel/skills/tree/main/skills/better-ui), [local](vendor/jakubkrehel/better-ui/README.md)). *Take:* concentric radius, shadow-as-border recipes, image outlines, icon transitions, optical alignment. tags: surfaces, polish, icons
- **better-typography**, **better-layout**, **better-colors**, **better-accessibility** by Jakub Krehel ([source](https://github.com/jakubkrehel/skills), [local](vendor/jakubkrehel/)). *Take:* type scale and wrapping rules, grouping with space, semantic color tokens and ramps, focus/hit-area/reduced-motion rules. tags: type, layout, color, a11y

Copied from commits `emilkowalski/skills@d16ebe6` and `jakubkrehel/skills@267330e`. Nested `SKILL.md` files were renamed to `README.md` so agents don't load them as separate, competing skills.

## Sites

- **bencho.dev** (https://bencho.dev/). *Take:* TODO, not captioned yet. This site couldn't be fetched when it was added. Ask the user what they like about it. tags: TODO
- **Gustavo Fior: Craft** (https://craft.gustavofior.com/). *Take:* TODO, not captioned yet. This site couldn't be fetched when it was added. Ask the user what they like about it. tags: TODO

## Products (feel benchmarks)

- **ChatGPT macOS app.** *Take:* the overall feel: neutral palette, tone-shift sidebar, big rounded composer, whitespace between messages, streaming output, hover-revealed message actions, no-wait sending. *Ignore:* nothing specific. This is the north star for "soft & frictionless". tags: chat, app-shell, north-star
