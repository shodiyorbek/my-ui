---
name: my-ui
description: "Shodiyorbek's UI library and design system for soft, clean, frictionless interfaces, like the ChatGPT macOS app, Linear or Raycast. It holds tokens, components, motion/surface/typography rules and captioned references. Use this skill for ANY frontend or UI work: building or styling a component, page, app shell, chat UI, landing page, dashboard, form, modal or menu; choosing colors, spacing, radius, shadows, fonts or animation timing; making something feel smoother, softer, cleaner, calmer, more polished or less cluttered; reviewing or polishing UI; or turning a screenshot or Figma frame into code. Also use it when the user wants to add, save or organize UI references, snippets, skills or notes into their library, even if they just paste a link and say \"save this\"."
---

# my-ui

This skill is the single source of truth for how this user's interfaces look, move and behave. The target feeling: **soft, clean, frictionless.** The interface gets out of the way, responds instantly, and never makes the user wait, re-type or guess. Think of the ChatGPT macOS app: neutral colors, low-contrast structure, generous rounded surfaces, motion you barely notice, zero-wait interaction.

Before inventing a color, spacing value, radius, duration or component API, look here first. The point of the library is that every agent's output looks like it came from the same hand.

## Start here

1. Read **[guides/feel.md](guides/feel.md)**. It defines "soft", gives the five laws and the hard→soft anti-pattern table. It's short, so read it every time you build UI.
2. Load **[tokens/tokens.css](tokens/tokens.css)** into the project, or map it into the Tailwind theme. Use only these variables. They're generated from `tokens/tokens.json`.
3. Read only the guide the task needs:

| Task involves… | Read |
|---|---|
| Any animation, transition, hover, press, open/close | [guides/motion.md](guides/motion.md) |
| Springs, drag, swipe, flick, sheets, toggles, layout morphs, Motion/SwiftUI/Reanimated spring params | [guides/springs.md](guides/springs.md) (+ `lib/spring.js`, `python scripts/spring.py`) |
| Colors, backgrounds, borders, shadows, radius, cards, glass/blur | [guides/surfaces.md](guides/surfaces.md) |
| Loading, forms, inputs, deleting, errors, empty states, keyboard | [guides/frictionless.md](guides/frictionless.md) |
| Fonts, text sizes, spacing, alignment, page structure | [guides/typography-layout.md](guides/typography-layout.md) |

4. Check **[components/index.md](components/index.md)**. Reuse or extend before writing new.
5. If a playbook in **[playbooks/index.md](playbooks/index.md)** matches the task, follow it.

Need more depth than a guide gives? The original source skills are in `references/vendor/` (see [references/index.md](references/index.md)). The guides are the house decisions, so when a vendor file disagrees with a guide, the guide wins.

## Non-negotiables

- **Tokens only.** No raw hex, px radius, shadow or duration in components. If a value is missing, propose a token instead of hard-coding one.
- **Neutral first, one filled primary per view.** Color is for meaning.
- **Space before lines.** Separate with space, then a tone shift, then a shadow ring. Borders only for dividers and focus.
- **Instant feedback, short motion.** Press feedback on pointer-down. UI motion ≤ 250ms with `--ease-out`. Actions users repeat constantly or trigger from the keyboard don't animate.
- **Springs for anything grabbable or reversible, critically damped by default.** Gestures use physics springs with the release velocity. Bounce only after a flick.
- **No friction.** Optimistic updates, undo instead of confirm, no layout shift, autofocus the obvious field.
- **Soft is not illegible.** Text ≥ 4.5:1 (the validator enforces this for token pairs), and a visible focus ring.
- **Every state:** hover, pressed, focus-visible, disabled, loading, empty, error, in light and dark.

## Adding to the library

When the user shares something to keep (a link, screenshot, snippet, skill, note), follow [workflows/ingest.md](workflows/ingest.md). If it contradicts a guide, show both and ask which wins. Don't pick silently.

After any change to this folder: `python scripts/build_tokens.py` (if tokens changed), then `python scripts/validate.py`, plus `node scripts/test-spring.mjs` if `lib/spring.js` changed.

## Other agents

This folder is plain markdown, JSON and CSS. `AGENTS.md` routes Codex, Cursor, Copilot, Gemini CLI and others here.
