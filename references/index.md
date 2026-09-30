# References

Captioned sources. Format per entry: **name**, link, *take* (what to copy), *ignore* (what not to), tags.

## Skills (copied into `vendor/`, MIT-licensed, licenses kept)

The house guides in `../guides/` distill these. Open the originals when you need the full reasoning or more recipes.

- **emil-design-eng** by Emil Kowalski ([source](https://github.com/emilkowalski/skills/tree/main/skills/emil-design-eng), [local](vendor/emilkowalski/emil-design-eng/README.md)). *Take:* the animation decision framework (frequency → purpose → easing → duration), custom easing curves, press scale, origin-aware popovers, clip-path techniques, gesture/drag details, Sonner principles. *Ignore:* the "Initial Response" greeting. tags: motion, polish, components
- **apple-design** by Emil Kowalski ([source](https://github.com/emilkowalski/skills/tree/main/skills/apple-design), [local](vendor/emilkowalski/apple-design/README.md)). *Take:* the fluid-interface physics (interruptibility, velocity handoff, momentum projection, rubber-banding), springs, translucent materials, optical typography. This is the closest source for the "macOS app softness". *Ignore:* the "Initial Response" greeting. tags: motion, gestures, materials, apple
- **better-ui** by Jakub Krehel ([source](https://github.com/jakubkrehel/skills/tree/main/skills/better-ui), [local](vendor/jakubkrehel/better-ui/README.md)). *Take:* concentric radius, shadow-as-border recipes, image outlines, icon transitions, optical alignment. tags: surfaces, polish, icons
- **better-typography**, **better-layout**, **better-colors**, **better-accessibility** by Jakub Krehel ([source](https://github.com/jakubkrehel/skills), [local](vendor/jakubkrehel/)). *Take:* type scale and wrapping rules, grouping with space, semantic color tokens and ramps, focus/hit-area/reduced-motion rules. tags: type, layout, color, a11y

- **craft-design-engineering** + all Craft articles by Gustavo Fior ([source](https://github.com/gustavo-fior/craft), [skill](vendor/gustavo-fior/craft-design-engineering/README.md), [articles](vendor/gustavo-fior/articles/), [license](vendor/gustavo-fior/LICENSE.md)). Install upstream with `npx skills add gustavo-fior/craft`. *Take:* the ~35 articles in `articles/<section>/*.mdx`, which cover more than the 7 concepts the packaged skill indexes: button press, easings, exit animations, scale entrances, stagger with a total cap, interruptibility, icon morph, hover restraint, shadows-not-borders (including the dark-mode inset-highlight recipe now in our tokens), nested radius, scroll fades, squircles, hit areas, html background, noise, letter-spacing, font smoothing, tabular numbers, interface sound, and craft essays (taste, novelty budget, timelessness). *Ignore:* the `<Demo />` tags, which are interactive widgets that only work on the live site. tags: motion, surfaces, type, sound, polish

Copied from commits `emilkowalski/skills@d16ebe6`, `jakubkrehel/skills@267330e` and `gustavo-fior/craft@e0d176e`. Nested `SKILL.md` files were renamed to `README.md` so agents don't load them as separate, competing skills.

## Sites

- **bencho.dev** (https://bencho.dev/). *Take:* TODO, not captioned yet. This site couldn't be fetched when it was added. Ask the user what they like about it. tags: TODO
- **Gustavo Fior: Craft** (https://craft.gustavofior.com/). The live version of the articles above. Every concept has an interactive demo, so open it to *feel* a value before changing it. The site's own look (from its source `globals.css`, not seen in a browser): neutral oklch grays (bg `oklch(0.985 0 0)`, text `oklch(0.205 0 0)`, dark bg `oklch(0.17 0 0)`), Inter for UI + Redaction serif for display + JetBrains Mono, `--ease-snappy: cubic-bezier(0.23,1,0.32,1)`, a CSS `linear()` spring, and three-layer shadows instead of borders. *Take:* the neutral palette discipline, the serif-display + Inter pairing for editorial pages. tags: gallery, motion, north-star

## Products (feel benchmarks)

- **ChatGPT macOS app.** *Take:* the overall feel: neutral palette, tone-shift sidebar, big rounded composer, whitespace between messages, streaming output, hover-revealed message actions, no-wait sending. *Ignore:* nothing specific. This is the north star for "soft & frictionless". tags: chat, app-shell, north-star
