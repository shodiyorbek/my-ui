---
name: my-ui
description: "Build, redesign, or review polished web and app interfaces using Shodiyorbek's calm, content-focused design system. Use for page composition, UI components, interaction design, responsive styling, and organizing UI references in this library. Adapt to the product and existing design system; backend-only work does not need this skill."
---

# my-ui

Create calm, content-focused interfaces with clear hierarchy, comfortable typography, predictable controls, and thoughtful feedback. ChatGPT-like restraint is a feeling benchmark, not a requirement to copy its layout or brand. Adapt composition to the user's task.

The user's instructions and the product's functional requirements take precedence. Preserve working behavior, real data, and existing accessibility. Use the house style as a default; map it into an established project design system rather than replacing that system wholesale.

## Start here

1. Read **[guides/feel.md](guides/feel.md)**. It defines "soft", gives the five laws and the hard→soft anti-pattern table. It's short, so read it every time you build UI.
2. For a page or workflow, read [page composition](guides/page-composition.md) and the relevant section of [pattern selection](guides/pattern-selection.md). Inspect the existing routes, shared components, and real content first. For a small component edit, skip unrelated page guidance.
3. Reuse the project's semantic tokens. For a new system, load [tokens/tokens.css](tokens/tokens.css) or map it into the theme. Extend tokens deliberately when a needed role is missing; avoid a parallel palette.
4. Read only the guide the task needs:

| Task involves… | Read |
|---|---|
| Any animation, transition, hover, press, open/close | [guides/motion.md](guides/motion.md) |
| Springs, drag, swipe, flick, sheets, toggles, layout morphs, Motion/SwiftUI/Reanimated spring params | [guides/springs.md](guides/springs.md) (+ `lib/spring.js`, `python scripts/spring.py`) |
| Colors, backgrounds, borders, shadows, radius, cards, glass/blur | [guides/surfaces.md](guides/surfaces.md) |
| Loading, forms, inputs, deleting, errors, empty states, keyboard | [guides/frictionless.md](guides/frictionless.md) |
| Fonts, text sizes, spacing, alignment, page structure | [guides/typography-layout.md](guides/typography-layout.md) |

5. Check **[components/index.md](components/index.md)**. Reuse or extend before writing new.
6. If a playbook in **[playbooks/index.md](playbooks/index.md)** matches the task, follow it.

Need more depth than a guide gives? The original source skills are in `references/vendor/` (see [references/index.md](references/index.md)). The guides are the house decisions, so when a vendor file disagrees with a guide, the guide wins.

For composition examples, consult the [six annotated reference studies](references/composition-studies.md). They are original teaching diagrams, not product screenshots or user-approved designs. Before finishing a UI implementation, use [review-ui](playbooks/review-ui.md) to inspect the rendered result and key interactions.

## Working defaults

- **Semantic tokens.** Reuse or map existing tokens; add a shared token for a missing visual role. Keep literal values in token definitions or genuinely one-off geometry, not scattered styling.
- **Neutral first, one dominant action per task or independent section.** Color is for meaning.
- **Space before lines.** Separate with space, then a tone shift, then a shadow ring. Use subtle borders when they clarify inputs, dense tables, or boundaries; do not make softness obscure structure.
- **Instant feedback, short motion.** Press feedback on pointer-down. UI motion ≤ 250ms with `--ease-out`. Actions users repeat constantly or trigger from the keyboard don't animate.
- **Springs for anything grabbable or reversible, critically damped by default.** Gestures use physics springs with the release velocity. Bounce only after a flick.
- **Thoughtful feedback.** Preserve non-sensitive input, prevent layout shifts, and show progress. Use optimistic updates only when failure can safely roll back. Confirm irreversible actions; do not announce success before the server accepts security, payment, or stock-posting changes.
- **Soft is not illegible.** Text ≥ 4.5:1 (the validator enforces this for token pairs), and a visible focus ring.
- **Relevant states:** default, hover, pressed, focus-visible, disabled, loading, empty, error, and success. Check each supported theme; do not add dark mode to a product solely to satisfy this skill.

## Adding to the library

When the user shares something to keep (a link, screenshot, snippet, skill, note), follow [workflows/ingest.md](workflows/ingest.md). If it contradicts a guide, show both and ask which wins. Don't pick silently.

After any change to this folder: `python scripts/build_tokens.py` (if tokens changed), then `python scripts/validate.py`, plus `node scripts/test-spring.mjs` if `lib/spring.js` changed.

## Other agents

This folder is plain markdown, JSON and CSS. `AGENTS.md` routes Codex, Cursor, Copilot, Gemini CLI and others here.
