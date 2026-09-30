#!/usr/bin/env python3
"""Check the my-ui library is consistent: valid tokens, indexes list every file, links resolve."""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LINK = re.compile(r"\]\(([^)#\s]+)\)")
errors, warnings = [], []


def check_links(md: Path):
    text = re.sub(r"```.*?```|`[^`]*`", "", md.read_text(encoding="utf-8"), flags=re.S)
    for target in LINK.findall(text):
        if "://" in target or target.startswith("mailto:"):
            continue
        if not (md.parent / target).exists():
            errors.append(f"{md.relative_to(ROOT)}: broken link -> {target}")


# SKILL.md frontmatter
skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
m = re.match(r"^---\n(.*?)\n---", skill, re.S)
if not m or not re.search(r"^name:\s*\S", m.group(1), re.M) or not re.search(r"^description:\s*\S", m.group(1), re.M):
    errors.append("SKILL.md: frontmatter needs name and description")

# tokens
try:
    tokens = json.loads((ROOT / "tokens/tokens.json").read_text(encoding="utf-8"))
    if "$status" in tokens:
        warnings.append("tokens/tokens.json: still placeholder values ($status present)")
except json.JSONDecodeError as e:
    errors.append(f"tokens/tokens.json: invalid JSON ({e})")

# every component folder is listed in components/index.md and has a README
comp_index = (ROOT / "components/index.md").read_text(encoding="utf-8")
for d in sorted((ROOT / "components").iterdir()):
    if d.is_dir() and not d.name.startswith("_"):
        if not (d / "README.md").exists():
            errors.append(f"components/{d.name}: missing README.md")
        if f"({d.name}/README.md)" not in comp_index:
            errors.append(f"components/index.md: missing entry for {d.name}")

# every playbook is listed
pb_index = (ROOT / "playbooks/index.md").read_text(encoding="utf-8")
for f in sorted((ROOT / "playbooks").glob("*.md")):
    if f.name != "index.md" and f"({f.name})" not in pb_index:
        errors.append(f"playbooks/index.md: missing entry for {f.name}")

# every reference image is mentioned in references/index.md
ref_index = (ROOT / "references/index.md").read_text(encoding="utf-8")
for f in sorted((ROOT / "references/images").glob("*")):
    if f.name != ".gitkeep" and f"images/{f.name}" not in ref_index:
        errors.append(f"references/index.md: image not captioned -> images/{f.name}")

for md in ROOT.rglob("*.md"):
    if ".git" not in md.parts:
        check_links(md)

for w in warnings:
    print(f"warn:  {w}")
for e in errors:
    print(f"error: {e}")
print("ok" if not errors else f"{len(errors)} error(s)")
sys.exit(1 if errors else 0)
