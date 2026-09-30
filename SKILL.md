---
name: my-ui
description: "Shodiyorbek's personal UI library and design system — tokens, components, visual references, and UI playbooks in one place. Use this skill for ANY frontend/UI work for this user: building or styling a component, page, screen, landing page, dashboard or form; picking colors, spacing, typography, radius or shadows; reviewing or polishing UI; turning a screenshot, Figma frame or reference into code; or when the user says \"my ui\", \"my style\", \"my components\", \"my design system\". Also use it when the user wants to add, save, import or organize UI references, snippets, skills or notes into their library — even if they just paste a link or image and say \"save this\"."
---

# my-ui

This skill is the single source of truth for how this user's UIs look and are built. Everything lives in this folder; nothing important should live anywhere else. If you find yourself inventing a color, spacing value or component API, stop and look here first — the whole point of the library is that every agent produces UI that looks like it came from the same hand.

## Map

| Path | What's there | Read it when |
|---|---|---|
| `tokens/tokens.json` | Colors, spacing, type scale, radius, shadows, motion | Before writing any styles |
| `components/<name>/` | One folder per component: source + `README.md` (props, usage, do/don't) | Building UI that needs that component |
| `components/index.md` | List of every component with a one-line purpose | Deciding whether a component already exists |
| `references/index.md` | Captioned inspiration: screenshots, links, and *what to take from each* | Designing something new or matching a vibe |
| `playbooks/` | Task procedures (e.g. build a component, review UI). Index in `playbooks/index.md` | The task matches a playbook |
| `workflows/ingest.md` | How to add new material to the library | The user wants to save/add/import something |
| `scripts/validate.py` | Checks indexes and links are consistent | After changing anything in this folder |

Read only what the task needs. The indexes exist so you don't have to open every file.

## How to use it

**Building UI**
1. Read `tokens/tokens.json`. Use tokens by name (CSS variables / Tailwind theme keys), never raw hex or px values. If a needed value is missing, say so and propose adding a token rather than hard-coding one — an ad-hoc value is how a library slowly stops being consistent.
2. Check `components/index.md`. Reuse or extend an existing component before writing a new one.
3. If a playbook in `playbooks/index.md` matches the task, follow it.
4. If the look is open-ended, skim `references/index.md` for relevant entries and say which ones you drew from.

**Adding to the library** — follow `workflows/ingest.md`. Short version: classify → dedupe → place → caption → update the index → run the validator.

**Reviewing UI** — use `playbooks/review-ui.md` if present, checking against tokens and component READMEs.

## Rules

- **One source of truth.** Each fact lives in exactly one file; other files link to it. Duplicated guidance drifts and then agents get contradictory instructions.
- **Tokens first.** Components consume tokens; pages consume components.
- **Empty is honest.** If a section is still a placeholder (marked `TODO`), tell the user rather than pretending the library has an opinion it doesn't have yet.
- **Keep this file short.** Details go in the folders above; this file is a router.

## Using this skill outside Claude

This folder is plain markdown + JSON, so any agent can use it. `AGENTS.md` at the root points non-Claude agents (Codex, Cursor, Copilot, Gemini CLI, etc.) to this file.
