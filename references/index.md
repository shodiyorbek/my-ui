# References

Captioned sources. Format per entry: **name**, link, *take* (what to copy), *ignore* (what not to), tags.

## Skills (copied into `vendor/`, MIT-licensed, licenses kept)

The house guides in `../guides/` distill these. Open the originals when you need the full reasoning or more recipes.

- **emil-design-eng** by Emil Kowalski ([source](https://github.com/emilkowalski/skills/tree/main/skills/emil-design-eng), [local](vendor/emilkowalski/emil-design-eng/README.md)). *Take:* the animation decision framework (frequency → purpose → easing → duration), custom easing curves, press scale, origin-aware popovers, clip-path techniques, gesture/drag details, Sonner principles. *Ignore:* the "Initial Response" greeting. tags: motion, polish, components
- **apple-design** by Emil Kowalski ([source](https://github.com/emilkowalski/skills/tree/main/skills/apple-design), [local](vendor/emilkowalski/apple-design/README.md)). *Take:* the fluid-interface physics (interruptibility, velocity handoff, momentum projection, rubber-banding), springs, translucent materials, optical typography. This is the closest source for the "macOS app softness". *Ignore:* the "Initial Response" greeting. tags: motion, gestures, materials, apple
- **better-ui** by Jakub Krehel ([source](https://github.com/jakubkrehel/skills/tree/main/skills/better-ui), [local](vendor/jakubkrehel/better-ui/README.md)). *Take:* concentric radius, shadow-as-border recipes, image outlines, icon transitions, optical alignment. tags: surfaces, polish, icons
- **better-typography**, **better-layout**, **better-colors**, **better-accessibility** by Jakub Krehel ([source](https://github.com/jakubkrehel/skills), [local](vendor/jakubkrehel/)). *Take:* type scale and wrapping rules, grouping with space, semantic color tokens and ramps, focus/hit-area/reduced-motion rules. tags: type, layout, color, a11y

- **craft-design-engineering** and archived Craft articles by Gustavo Fior ([source](https://github.com/gustavo-fior/craft), [skill](vendor/gustavo-fior/craft-design-engineering/README.md), [articles](vendor/gustavo-fior/articles/), [license](vendor/gustavo-fior/LICENSE.md)). **Provenance checked 2026-10-01:** the [live homepage](https://craft.gustavofior.com/) says unpublished repository articles are AI placeholders. The archive is not a collection of ~35 verified published essays. *Take:* published guidance on [nested radius](https://craft.gustavofior.com/nested-border-radius), [hover restraint](https://craft.gustavofior.com/hover-restraint), and [tabular numbers](https://craft.gustavofior.com/tabular-numbers), checked in the latest study. *Ignore:* unpublished draft claims unless independently verified; `<Demo />` tags require live widgets. Existing house decisions stand on their own reasoning and other cited sources, not on placeholder authority. tags: provenance, surfaces, motion, type


Copied from commits `emilkowalski/skills@d16ebe6`, `jakubkrehel/skills@267330e` and `gustavo-fior/craft@e0d176e`. Nested `SKILL.md` files were renamed to `README.md` so agents don't load them as separate, competing skills.

## Sites

**User preference, reaffirmed 2026-10-01:** Bencho and Craft are preferred aesthetic references. See the [fresh observations and application recipe](sites/bencho-and-craft-analysis.md#2026-10-01-refresh) before the historical measurements below. Approval of the aesthetic does not mean every component or accessibility choice is approved.

- **bencho.dev** (https://bencho.dev/). A gallery of interactive UI blocks. Measured in the user's browser; full data in [sites/bencho-and-craft-analysis.md](sites/bencho-and-craft-analysis.md). *Take:* cards defined only by a translucent text-color wash (6% light / 9% dark, no border, no shadow) → our `--color-wash`; press faster than release (90ms / 260ms) → our 100ms / 200ms; press amount scaled by size (.985 text, .96 icons); a frosted scrim (page color 78% + `blur(22px)`) → our `--color-scrim`; glass only once content scrolls under it; modals that morph out of the clicked card (380ms, side panel +60ms); concentric 22/4/18 menus; odometer digit counters. *Ignore:* the 90+ overshoot/bounce curves, hover-only titles and actions (invisible on touch), failing muted-text contrast (≈2.5:1 light), the pure `#000` dark mode, the header with no backing, slow deep links. tags: gallery, surfaces, press, modal
- **Gustavo Fior: Craft** (https://craft.gustavofior.com/). Published design articles with interactive demonstrations; many other entries are marked “Soon”. Open it to *feel* a value before changing it. Measured in the user's browser (full data in [sites/bencho-and-craft-analysis.md](sites/bencho-and-craft-analysis.md)): bg `#fafafa` / dark `#0f0f0f`, text `#171717`, muted `#737373`, no borders anywhere (only the layered ring shadow), quiet headings (16–18px/500), article body 14px with 1.8 leading, Redaction serif logo + Inter + JetBrains Mono. *Take:* shadow system, instant hover, the clip-path segmented thumb (→ `components/segmented`), 0.97 press, patient-then-instant tooltips. *Ignore:* many disabled "Soon" cards, 10–12px text, instant hover on big cards so faint it feels dead, `<html>` background left transparent (against its own article), and the Optical Alignment article's text, which says the play icon moves left while its code (correctly) moves it right. tags: gallery, motion, north-star

## Products (feel benchmarks)

- **ChatGPT macOS app.** *Take:* the overall feel: neutral palette, tone-shift sidebar, big rounded composer, whitespace between messages, streaming output, hover-revealed message actions, no-wait sending. *Ignore:* nothing specific. This is the north star for "soft & frictionless". tags: chat, app-shell, north-star

## Original composition studies

See [annotated studies](composition-studies.md) for rationale and anti-patterns. Original diagrams, not captured product screenshots or user-approved designs.

- **Conversation workspace** ([diagram](images/conversation-study.svg)). *Take:* A narrow reading measure keeps long answers comfortable. *Ignore:* illustrative dimensions and sample content. tags: composition, teaching
- **Operational inventory** ([diagram](images/operations-study.svg)). *Take:* Route links describe locations; an underline marks selection. *Ignore:* illustrative dimensions and sample content. tags: composition, teaching
- **Independent settings forms** ([diagram](images/settings-study.svg)). *Take:* Fields stay readable rather than stretching across the page. *Ignore:* illustrative dimensions and sample content. tags: composition, teaching
- **Product landing page** ([diagram](images/marketing-study.svg)). *Take:* The headline explains value before decorative content. *Ignore:* illustrative dimensions and sample content. tags: composition, teaching
- **Empty results and recoverable errors** ([diagram](images/empty-error-study.svg)). *Take:* No matching results is different from having no records. *Ignore:* illustrative dimensions and sample content. tags: composition, teaching
- **Destination links versus mode switches** ([diagram](images/pattern-choice-study.svg)). *Take:* Use links for stock, movements, and drafts destinations. *Ignore:* illustrative dimensions and sample content. tags: composition, teaching

## Control design

- [Modern controls research](modern-controls.md) — official Radix, Base UI, React Aria, and WAI-ARIA sources with take/adapt notes. Reviewed 2026-10-01.

## Animation learning

- **Animations.dev by Emil Kowalski** — [course reading and demo review](sites/animations-dev.md), reviewed 2026-10-01 with authenticated access. *Take:* purposeful motion, interruption handling, shared geometry, sequence ownership, realistic performance checks, and reduced-motion alternatives. Also includes a [platform visual review](sites/animations-dev.md#platform-visual-system-review) of spacing, typography, surfaces and responsive templates. Written material reviewed across 45 core lessons and four interview transcripts; videos and exercises are not fully completed. *Ignore:* treating example timings as universal or older library implementation details as current guarantees. tags: motion, performance, accessibility
