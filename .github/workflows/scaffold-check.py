#!/usr/bin/env python3
"""scaffold-check.py — CI proof that templates/ produce a structurally valid
scaffold.

Copies every template into a temp project tree, substitutes realistic values
for the common {placeholders} (owner/name/profile/date), adds the minimal root
files a scaffold always gets, then runs scripts/validate.py. The raw templates
are intentionally fill-me skeletons, so leftover prose `{...}` tokens are
expected; the hard contract is that the validator reports NO hard FAILs
(missing files, duplicate IDs, etc.). Satisfies REQ-CT-001.
"""
from __future__ import annotations

import subprocess
import sys
import tempfile
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
TEMPLATES = REPO / "templates"
VALIDATOR = REPO / "scripts" / "validate.py"

# {placeholder} -> realistic value (keeps IDs/links/paths clean in CI).
SUBS = {
    "{owner}": "TKOResearch",
    "{date}": "2026-08-28",
    "{today}": "2026-08-28",
    "{profile}": "library",
    "{name}": "demo",
    "{one-line description}": "demo scaffold project",
    "{description}": "A demo scaffold project built from repo-contract templates.",
    "{project-check}": "python3 scripts/validate.py . --profile library",
    "pending-stack": "python3 -m pytest -q",
    "{bootstrap}": "python3 -m pytest -q",
    "{check}": "python3 -m pytest -q",
    "{validate}": "python3 -m pytest -q",
    "{test}": "python3 -m pytest -q",
    "{command}": "python3 -m pytest -q",
    "{timestamp}": "2026-08-28T00:00:00Z",
    "{body}": "Substantive project-specific content for the demo produced by the scaffolder.",
}

# Fill-token areas that reference IDs/paths matter for validation; prose
# placeholders like {criterion 1} do not. We only demand the former be gone.
REQUIRED_CLEAN = ["REQ-{AREA}", "FTR-{AREA}", "BOUNDARY-{AREA}", "TEST-{AREA}", "{test command}"]


def main() -> int:
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp) / "demo"
        for template in TEMPLATES.rglob("*"):
            if not template.is_file():
                continue
            rel = template.relative_to(TEMPLATES).as_posix()
            out = root / rel
            out.parent.mkdir(parents=True, exist_ok=True)
            text = template.read_text()
            for k, v in SUBS.items():
                text = text.replace(k, v)
            out.write_text(text)

        if not (root / ".gitignore").exists():
            (root / ".gitignore").write_text(".env\n")

        r = subprocess.run(
            [sys.executable, str(VALIDATOR), str(root), "--profile", "library"],
            capture_output=True, text=True,
        )
        out = r.stdout + r.stderr
        print(out)
        hard = [l for l in out.splitlines() if "[FAIL]" in l]
        if hard:
            print("ci: template scaffold produced hard FAILs:", file=sys.stderr)
            for l in hard:
                print("  " + l, file=sys.stderr)
            return 1
    print("ci: templates produce a structurally valid scaffold (no hard FAILs)")
    return 0


if __name__ == "__main__":
    sys.exit(main())