# my-ui

Personal UI library packaged as an agent skill. It teaches agents to build **soft, clean, frictionless** interfaces (think the ChatGPT macOS app). Entry point: [`SKILL.md`](SKILL.md). Live demo: open `examples/demo.html`.

## Install

One command, for any agent (Claude Code, Cursor, Codex, Copilot, Gemini CLI, …):

```bash
npx skills add shodiyorbek/my-ui          # this project
npx skills add shodiyorbek/my-ui -g       # all projects (user-level)
npx skills add shodiyorbek/my-ui -a claude-code   # only for Claude Code
```

Update later with `npx skills update my-ui`.

Other ways:

- **Claude.ai / Claude app:** upload the packaged `my-ui.skill` (Settings → Capabilities → Skills).
- **Manual:** `git clone https://github.com/shodiyorbek/my-ui ~/.claude/skills/my-ui`.
- **Agents working inside this repo** read `AGENTS.md`, which routes them to `SKILL.md`.

Keep one clone as the master copy and `git pull` elsewhere, so copies don't drift apart.

## Adding things

Tell your agent "add this to my-ui" and give it the item. It follows [`workflows/ingest.md`](workflows/ingest.md). Check with `python scripts/validate.py`.

## Credits

`references/vendor/` contains MIT-licensed skills by [Emil Kowalski](https://github.com/emilkowalski/skills), [Jakub Krehel](https://github.com/jakubkrehel/skills) and [Gustavo Fior](https://github.com/gustavo-fior/craft), with their licenses.
