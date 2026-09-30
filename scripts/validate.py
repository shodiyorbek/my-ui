#!/usr/bin/env python3
"""Check the my-ui library is consistent: valid tokens, indexes list every file, links resolve."""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
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

# tokens: valid JSON, tokens.css regenerated, readable text contrast
def luminance(hex_color):
    h = hex_color.lstrip("#")[:6]
    c = [int(h[i:i + 2], 16) / 255 for i in (0, 2, 4)]
    c = [x / 12.92 if x <= 0.03928 else ((x + 0.055) / 1.055) ** 2.4 for x in c]
    return 0.2126 * c[0] + 0.7152 * c[1] + 0.0722 * c[2]


def contrast(a, b):
    la, lb = sorted((luminance(a), luminance(b)), reverse=True)
    return (la + 0.05) / (lb + 0.05)


try:
    tokens = json.loads((ROOT / "tokens/tokens.json").read_text(encoding="utf-8"))
    from build_tokens import render
    css = ROOT / "tokens/tokens.css"
    if not css.exists() or css.read_text(encoding="utf-8") != render():
        errors.append("tokens/tokens.css: out of date, run python scripts/build_tokens.py")
    colors = tokens.get("color", {})
    for fg in ("text", "text-muted", "accent", "danger", "success"):
        for bg in ("bg", "bg-subtle", "surface", "surface-hover"):
            for mode in ("light", "dark"):
                if fg in colors and bg in colors:
                    ratio = contrast(colors[fg][mode], colors[bg][mode])
                    if ratio < 4.5:
                        errors.append(f"tokens: {fg} on {bg} ({mode}) is {ratio:.2f}:1, needs 4.5:1")
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
