#!/usr/bin/env python3
"""Generate tokens/tokens.css (CSS variables, light + dark) from tokens/tokens.json. Never edit tokens.css by hand."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC, OUT = ROOT / "tokens/tokens.json", ROOT / "tokens/tokens.css"


def render() -> str:
    t = json.loads(SRC.read_text(encoding="utf-8"))
    light, dark = [], []
    for group, values in t.items():
        if group.startswith("$"):
            continue
        for name, v in values.items():
            var = f"--{group}-{name}"
            if isinstance(v, dict):
                light.append(f"  {var}: {v['light']};")
                dark.append(f"  {var}: {v['dark']};")
            else:
                light.append(f"  {var}: {v};")
    dark_block = "\n".join(dark)
    return (
        "/* Generated from tokens.json by scripts/build_tokens.py. Do not edit. */\n"
        ":root {\n  color-scheme: light dark;\n" + "\n".join(light) + "\n}\n\n"
        "@media (prefers-color-scheme: dark) {\n  :root:not([data-theme=\"light\"]) {\n"
        + "\n".join("  " + l for l in dark) + "\n  }\n}\n\n"
        ":root[data-theme=\"dark\"] {\n" + dark_block + "\n}\n"
    )


if __name__ == "__main__":
    OUT.write_text(render(), encoding="utf-8")
    print(f"wrote {OUT.relative_to(ROOT)}")
