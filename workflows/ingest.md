# Ingest: adding material to the library

Use this whenever the user hands over something to keep — a link, screenshot, code snippet, component, a skill/prompt they wrote elsewhere, a note, a Figma frame, a color palette. The goal is that after ingesting, the item is findable by any agent from an index, and nothing contradicts anything else.

## 1. Classify

| It is… | It goes to |
|---|---|
| Colors, spacing, fonts, radius, shadows, motion values | `tokens/tokens.json`, then `python scripts/build_tokens.py` |
| Reusable UI code (button, card, modal…) | `components/<kebab-name>/` (copy `components/_template/`) |
| Inspiration: screenshot, site link, Dribbble shot, Figma frame | `references/` + entry in `references/index.md` |
| Someone else's skill / design guideline (e.g. from skills.sh or GitHub) | Copy it (with its LICENSE) into `references/vendor/<author>/`, renaming `SKILL.md` to `README.md`. Merge its decisions into the matching `guides/*.md`, and record disagreements in that guide's *Resolved conflicts* table |
| A principle about how the UI should look, move or behave | The matching `guides/*.md` |
| A procedure / prompt / "skill" for doing a UI task | `playbooks/<kebab-name>.md` + entry in `playbooks/index.md` |
| A rule or preference ("never use pure black", "8px grid") | The file it governs: token rule → `tokens/README.md`, component rule → that component's README, global rule → `SKILL.md` Rules |

If something fits two places, split it: the values go to tokens, the procedure to a playbook, and they link to each other.

## 2. Dedupe

Search the library for the same thing before adding (`grep -ri` on the name, colors, key phrases). If it overlaps:
- Same thing, better version → replace the old one and note it in the commit message.
- Conflicting guidance → do not silently pick one. Show the user both and ask which wins.

## 3. Place and caption

- References: save images to `references/images/<kebab-name>.<ext>`. For each entry, write **what to take from it** (e.g. "the card density and the muted border — not the colors"). An uncaptioned image is nearly useless to an agent.
- Playbooks: start with one line saying when to use it, then steps. Strip anything tied to a specific old project unless it's a reusable lesson.
- Components: fill in the README template (purpose, props, usage, do/don't, which tokens it uses).

## 4. Update indexes

Every new file gets a line in its folder's `index.md`. The indexes are how agents find things without reading everything.

## 5. Validate

```bash
python scripts/validate.py
```

Fix anything it reports, then commit with a message describing what was added.
