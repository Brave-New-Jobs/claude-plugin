"""Package the whole plugin as a .zip for upload to Claude (chat / Cowork).

Claude's plugin uploader wants the plugin's CONTENTS at the archive root — so
`.claude-plugin/plugin.json` must sit at the top of the zip, NOT inside a
`bnj-employer/` folder. Zipping the directory from outside produces the second
shape and is rejected as not a valid plugin, which is the single most common way
this goes wrong.

`.zip` and not `.plugin`: the two extensions hold identical bytes, but the upload
dialog filters on `.zip`.

Excluded from the archive: the build scripts and the repo's own README, which are
for whoever maintains this, not for the person installing it. INSTALL.md is kept
— it is the fallback instructions if the plugin route is unavailable on their
plan.

    python build-plugin-zip.py [output-directory]
"""
from __future__ import annotations

import json
import pathlib
import sys
import zipfile

HERE = pathlib.Path(__file__).resolve().parent
OUT_NAME = "bnj-employer-plugin.zip"

# Everything the installed plugin needs, and nothing that only the maintainer
# needs. Directories are included whole.
INCLUDE = [".claude-plugin/plugin.json", ".mcp.json", "INSTALL.md"]
INCLUDE_DIRS = ["skills"]


def main() -> None:
    manifest = HERE / ".claude-plugin" / "plugin.json"
    if not manifest.is_file():
        sys.exit(f"no plugin manifest at {manifest}")
    name = json.loads(manifest.read_text(encoding="utf-8")).get("name", "?")

    out_dir = pathlib.Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else HERE / "dist"
    out_dir.mkdir(parents=True, exist_ok=True)
    out = out_dir / OUT_NAME

    members: list[pathlib.Path] = []
    for rel in INCLUDE:
        p = HERE / rel
        if not p.is_file():
            sys.exit(f"missing {rel}")
        members.append(p)
    for d in INCLUDE_DIRS:
        root = HERE / d
        if not root.is_dir():
            sys.exit(f"missing directory {d}/")
        members.extend(sorted(p for p in root.rglob("*") if p.is_file()))

    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
        for f in members:
            arcname = f.relative_to(HERE).as_posix()   # root-relative: no wrapper folder
            z.write(f, arcname)
            print(f"  + {arcname}")

    print(f"\nplugin '{name}' -> {out}  ({out.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
