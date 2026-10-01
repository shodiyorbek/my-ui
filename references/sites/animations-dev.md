# Animations.dev: course reading and demo review

Reviewed 2026-10-01 through the user's authenticated browser. Read the explanatory material across all 45 core lesson pages and the four interview transcripts. This is a text-and-demo review, **not every video watched end-to-end or every exercise completed**. No course code, transcripts, videos, assets, or paid skill packages are reproduced in this library.

## Coverage

| Module | Lesson pages read | Coverage |
|---|---:|---|
| [Animation theory](https://animations.dev/learn/animation-theory/intro) | 10 | Purpose, easing, springs, taste, prototyping, practical tips and judgement |
| [CSS animations](https://animations.dev/learn/css-animations/the-beauty-of-css-animations) | 5 | Transforms, transitions, keyframes and clipping |
| [Framer Motion](https://animations.dev/learn/framer-motion/why-framer-motion) | 9 | Basics and component walkthrough prose, hooks, graph and public iteration |
| [Good vs great](https://animations.dev/learn/good-vs-great-animations/the-big-little-details) | 4 | Details, performance, accessibility and future APIs |
| [Family drawer](https://animations.dev/learn/family-drawer/the-analysis) | 4 | Analysis, geometry, crossfade and finishing |
| [Dynamic Island](https://animations.dev/learn/dynamic-island/the-design) | 4 | Design, ring, timer and morph |
| [Navigation menu](https://animations.dev/learn/navigation-menu/know-your-tools) | 3 | Primitive choice, animation and closing discussion |
| [Hero illustration](https://animations.dev/learn/hero-illustration/svg-introduction) | 6 | SVG, strokes, rotation, click, clock and polish |

Also read [Vocabulary](https://animations.dev/learn/vocabulary), [Animations as Proof of Care](https://animations.dev/learn/bonuses/animations-as-proof-of-care), and the interview transcripts for [Henry Heffernan](https://animations.dev/learn/interviews/henry-heffernan), [Mariana Castilho](https://animations.dev/learn/interviews/mariana-castilho), [Lochie Axon](https://animations.dev/learn/interviews/lochie-axon), and [Dennis Brotzky](https://animations.dev/learn/interviews/dennis-brotzky). Inspected the Skills page and Vault listing; their packages and every linked Vault item were not reviewed.

## Interaction and playback evidence

- Multi-step demo: exercised Continue and Back, including a quick reversal. This was a spot check, not full keyboard or screen-reader verification.
- Dynamic Island: live Ring and Timer controls responded. An embedded editor preview separately failed with a class-extension runtime error in `ring.js`; its code was not verified as runnable.
- Family drawer: opened the polished demo. Dismissal behavior was not verified.
- Navigation: exercised menu triggers; the inspection did not establish the complete hover, focus and dismissal sequence.
- Manual Play successfully started the GT Standard clip and the main Basics player; English captions were available for the latter. Initial player error messages therefore do not establish that all media is unavailable. Neither playback check establishes full video coverage.
- Code blocks were consulted selectively. Solutions and exercises were not implemented or graded, and lesson completion controls were not intentionally used.

## What enters the skill

The original synthesis in [choreograph-motion](../../playbooks/choreograph-motion.md) covers motion intent, interruption, shared geometry, sequence ownership and production checks. Existing [motion guidance](../../guides/motion.md) covers stable hit regions, realistic performance and reduced motion. The interview readings reinforce prototyping in the actual medium, directing attention toward content, and separating personal taste from functional defects.

Keep existing house timings and restrained product behavior. Expressive illustration and marketing examples are contextual demonstrations, not defaults for frequent POS actions. Library APIs, acceleration, licensing and browser support can change: consult current official documentation before implementing older examples. A visual trick involving duplicated layers must retain one accessible interactive control; a placeholder does not replace a label.

These are selective application notes, not a replacement for the course. Remaining coverage is full video viewing, exercise implementation, exhaustive source-code review and the linked Vault collection.

## Platform visual system review

Measured 2026-10-01 from rendered DOM and inspected screenshots at 1138×988 desktop and 390×844 mobile. Covered the course overview, theory lesson, video lesson, navigation walkthrough, interview listing, Vault listing, Skills page and Vocabulary. Mobile spot checks covered the overview, lesson and Vocabulary. These are representative shared templates, not an exhaustive audit of every route and interaction. The authenticated homepage redirected to the course overview, so the public marketing layout was not assessed.

### Measured examples

| Role | Observed desktop treatment | Responsive observation |
|---|---|---|
| Overview grid | 24px outer gutters, three approximately 347px columns with 24px gaps | One 358px column inside 16px gutters at 390px |
| Lesson shell | Approximately 260px sidebar; 700px reading column centered in remaining space; content wrapper 92px top and 48px inline padding | Sidebar absent from reading view; 16px gutters, 358px reading width; Lessons link in header |
| Lesson type | Inter; title 20/28px at weight 500; body 16/26.4px; paragraph margins generally 12px | Body size and line-height retained |
| Gallery heading | Vocabulary, Interviews and Skills use 36/40px headings; Vocabulary weight 600, tracking −1.8px | Vocabulary retains 36px heading in the checked viewport |
| Card grouping | Overview media-to-title 16px; title-to-description 4px; titles 15/22.5px; descriptions 15/24px | Cards stack without shrinking text |
| Vocabulary cards | Two 535px columns separated by 20px; 20px text inset; titles 15/22.5px, descriptions 14/22.4px with 4px separation | One 358px column; 20px text inset retained |
| Skills reading page | 700px centered column; 80px before major section headings, 16px paragraph spacing; 17/27.2px explanatory text | Not measured on mobile |

Values are observations of these pages, not a recovered global token system. The 20px card inset and 80px editorial gap are reference-specific; existing house spacing tokens remain authoritative.

### Surface and hierarchy observations

The lesson body uses warm near-black `rgb(17,17,16)` with white primary text. Vocabulary cards use `rgb(13,13,13)`, 16px corners and muted description text `rgb(181,179,173)`. Their subtle visible boundary is not a conventional CSS border on the measured article; use the resulting separation as inspiration rather than assuming an implementation. Small labels, weight changes and surface changes establish hierarchy without coloring every section. Bright demo canvases visually isolate the example from dark course navigation.

The sidebar uses compact 14px labels and measured 32px lesson rows. Long names truncate. These are desktop density observations, not recommended touch-target sizes or a reason to hide essential labels in an operational app. Some lesson captions measure 12/16px; preserve the skill's readability and contrast requirements when adapting them. No full contrast, keyboard or screen-reader audit was performed.

### Application recipe

- Establish separate page, section, group and item spacing roles. Make related text visibly closer than adjacent groups. Audit the relationships, not just whether every number is divisible by four.
- Choose width by task: constrained prose/forms, flexible operational tables, responsive discovery grids. Center a reading column within the usable pane after navigation is accounted for.
- Keep text edges aligned across headings, descriptions and controls. A callout background can extend beyond the reading edge while its text remains aligned.
- Give demonstrations enough space to show motion without clipping. Do not transfer their empty stage height to routine dashboard cards.
- Keep body text legible on small screens; reduce columns and outer gutters before reducing font size. Preserve component inset and clear separation between groups.
- Reserve large heading treatments for page introductions. Use quieter section and card headings; do not reproduce every observed size as a new token.
- Map surface and text roles into the product's existing themes. The lesson is tonal hierarchy, not mandatory dark mode, white demo panels, exact colors or negative tracking.

Implementation guidance: [typography and layout](../../guides/typography-layout.md).
