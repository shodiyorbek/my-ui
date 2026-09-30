# my-ui

Personal UI library packaged as an agent skill. It teaches agents to build **soft, clean, frictionless** interfaces (think the ChatGPT macOS app). Entry point: [`SKILL.md`](SKILL.md). Live demo: open `examples/demo.html`.

## Install

- **Claude Code (all projects):** `git clone <this-repo> ~/.claude/skills/my-ui`
- **Claude Code (one project):** clone or submodule into `<project>/.claude/skills/my-ui`
- **Claude.ai / Claude app:** upload the packaged `my-ui.skill` (Settings → Capabilities → Skills)
- **Other agents (Codex, Cursor, Copilot, Gemini CLI):** add this repo to the workspace; they read `AGENTS.md`, which routes to `SKILL.md`

Keep one clone as the master copy and `git pull` elsewhere, so copies don't drift apart.

## Adding things

Tell your agent "add this to my-ui" and give it the item. It follows [`workflows/ingest.md`](workflows/ingest.md). Check with `python scripts/validate.py`.

## Credits

`references/vendor/` contains MIT-licensed skills by [Emil Kowalski](https://github.com/emilkowalski/skills), [Jakub Krehel](https://github.com/jakubkrehel/skills) and [Gustavo Fior](https://github.com/gustavo-fior/craft), with their licenses.
