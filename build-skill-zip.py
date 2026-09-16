"""Package the Odoo sync skill as a .zip for upload to Claude Desktop / claude.ai.

Claude wants ONE complete skill folder per zip — the directory, with SKILL.md and
anything beside it — not a bare SKILL.md.

Written with `zipfile` rather than PowerShell's Compress-Archive on purpose:
Compress-Archive writes Windows backslashes into the entry names, which several
readers treat as a single oddly-named file at the root instead of a folder.
`zipfile` writes forward slashes, which is what the format actually specifies.

    python build-skill-zip.py [output-directory]
"""
from __future__ import annotations

import pathlib
import sys
import zipfile

HERE = pathlib.Path(__file__).resolve().parent
SKILL_DIR = HERE / "skills" / "bnj-odoo-sync"
OUT_NAME = "bnj-odoo-sync-skill.zip"


def main() -> None:
    if not (SKILL_DIR / "SKILL.md").is_file():
        sys.exit(f"no SKILL.md under {SKILL_DIR}")

    out_dir = pathlib.Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else HERE / "dist"
    out_dir.mkdir(parents=True, exist_ok=True)
    out = out_dir / OUT_NAME

    files = sorted(p for p in SKILL_DIR.rglob("*") if p.is_file())
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
        for f in files:
            # Entry names are relative to the skill folder's PARENT, so the zip
            # opens as `bnj-odoo-sync/SKILL.md` — the folder Claude looks for.
            arcname = f.relative_to(SKILL_DIR.parent).as_posix()
            z.write(f, arcname)
            print(f"  + {arcname}")

    print(f"\n{out}  ({out.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
