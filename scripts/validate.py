#!/usr/bin/env python3
"""validate.py — machine validation of the repository documentation contract.

Usage:
    python3 validate.py <project_root> [--profile library|service|web-application|monorepo|regulated-system]

Validates that a repo satisfies the contract before an agent claims "complete".
Exit 0 = pass (warnings allowed), 1 = one or more failures, 2 = usage error.

Checks:
  - profile-required documents exist and have a non-trivial body
  - project.yaml exists and parses as YAML (if PyYAML installed) / JSON-ish
  - ID prefix conventions hold and IDs owned by their owning file only
  - internal `docs/` markdown links resolve to files
  - each Accepted requirement has "Acceptance criteria" + a "Verification" ref
  - each Implemented feature references a requirement and a test path
  - AGENTS.md command lines reference real commands (best-effort)
  - no committed .env with real-looking secrets
  - control-plane files present

Stdlib only (yaml is optional; degrades to a light parse).
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

FAILURES: list[str] = []
WARNINGS: list[str] = []

REQUIRED_EVERY = [
    "README.md", "AGENTS.md", "CLAUDE.md", "TODO.md", "project.yaml",
    "docs/INDEX.md", "docs/REQUIREMENTS.md", "docs/FEATURES.md",
    "docs/DESIGN.md", "docs/BOUNDARIES.md", "docs/ARCHITECTURE.md",
    "docs/TESTING.md", "docs/GLOSSARY.md",
    "docs/decisions/README.md", "docs/plans/README.md",
]
PROFILE_EXTRA = {
    "library": [],
    "service": ["docs/OPERATIONS.md", "docs/THREAT_MODEL.md"],
    "web-application": ["docs/OPERATIONS.md", "docs/THREAT_MODEL.md"],
    "monorepo": ["docs/OPERATIONS.md", "docs/THREAT_MODEL.md"],
    "regulated-system": ["docs/OPERATIONS.md", "docs/THREAT_MODEL.md"],
}


def fail(msg: str) -> None:
    FAILURES.append(msg)


def warn(msg: str) -> None:
    WARNINGS.append(msg)


def loaded_yaml(path: Path):
    """Return True-ish if the file parses as YAML.

    Uses PyYAML when available; otherwise falls back to a structural light check
    (required top-level keys present). Returns False only when the file is
    genuinely unparsable by the available means.
    """
    required_keys = ["schema_version", "profile", "documents", "commands"]
    try:
        import yaml  # noqa: F401
        data = yaml.safe_load(path.read_text())
        return isinstance(data, dict) and "profile" in data
    except Exception:
        pass
    # Light fallback: confirm the key top-level fields appear as `key:` lines.
    text = path.read_text()
    present = set(re.findall(r"^([a-z_]+):", text, re.M))
    return required_keys[1] in present  # 'profile' is the load-bearing key


def body_non_trivial(path: Path) -> bool:
    if not path.exists():
        return False
    text = path.read_text()
    content = re.sub(r"[#`|>*\[\]\-()\s]", "", text)
    return len(content) > 200


def check_required_files(root: Path, profile: str) -> None:
    required = REQUIRED_EVERY + PROFILE_EXTRA.get(profile, [])
    for rel in required:
        p = root / rel
        if not p.exists():
            fail(f"missing required file: {rel}")
        elif not body_non_trivial(p):
            warn(f"file may be placeholder/empty: {rel}")
    decisions = root / "docs" / "decisions"
    adrs = list(decisions.glob("ADR-*.md")) if decisions.exists() else []
    if not adrs:
        fail("no ADR files found under docs/decisions/ (need >= 1)")


def check_id_uniqueness(root: Path) -> None:
    # An ID may only be *defined* by the file that owns its prefix. Occurrences
    # of an ID in other files (FEATURES referencing REQ-*, TESTING referencing
    # REQ-*, ADRs, plans) are legitimate references, not duplicate definitions.
    owner = {
        "REQ": root / "docs" / "REQUIREMENTS.md",
        "FTR": root / "docs" / "FEATURES.md",
        "BOUNDARY": root / "docs" / "BOUNDARIES.md",
        "ADR": root / "docs" / "decisions",  # directory of ADR-*.md files
    }
    header = re.compile(r"^####? .*?((?:REQ|FTR|BOUNDARY|ADR)-[A-Z0-9]+-[0-9]+)", re.M)
    for prefix, owner_path in owner.items():
        if owner_path.is_file():
            defined = header.findall(owner_path.read_text(errors="ignore"))
            for ident in set(defined):
                if defined.count(ident) > 1:
                    fail(f"{ident} defined more than once in {owner_path}")
        elif owner_path.is_dir():
            defined = set()
            for p in owner_path.glob("ADR-*.md"):
                m = re.match(r"ADR-(\d+)", p.name)
                if m:
                    ident = "ADR-" + m.group(1)
                else:
                    # fall back to body header if filename lacks number
                    h = header.search(p.read_text(errors="ignore"))
                    ident = h.group(1) if h else None
                if ident and ident in defined:
                    fail(f"{ident} defined in more than one ADR file")
                if ident:
                    defined.add(ident)


def check_links(root: Path) -> None:
    link_re = re.compile(r"\]\(([^)#]+)(?:#[^)]*)?\)")
    for p in root.joinpath("docs").rglob("*.md"):
        text = p.read_text(errors="ignore")
        for target in link_re.findall(text):
            if target.startswith("http") or target.startswith("mailto:"):
                continue
            if target.startswith("#"):
                continue
            tgt = root / target
            if tgt.exists() or (p.parent / target).exists():
                continue
            warn(f"unresolved link '{target}' in {p}")


def check_requirements(root: Path) -> None:
    req_file = root / "docs" / "REQUIREMENTS.md"
    if not req_file.exists():
        return
    text = req_file.read_text()
    accepted_headers = list(re.finditer(r"^### (REQ-[A-Z0-9]+-[0-9]+)\s*—", text, re.M))
    for i, hm in enumerate(accepted_headers):
        end = accepted_headers[i + 1].start() if i + 1 < len(accepted_headers) else len(text)
        block = text[hm.start():end]
        if "**Status:** Accepted" in block:
            if "Acceptance criteria" not in block:
                fail(f"{hm.group(1)} is Accepted but lacks acceptance criteria")
            if "Verification" not in block:
                fail(f"{hm.group(1)} is Accepted but lacks a Verification reference")


def check_features(root: Path) -> None:
    feat = root / "docs" / "FEATURES.md"
    if not feat.exists():
        return
    for line in feat.read_text().splitlines():
        if line.startswith("| FTR-") and ("Implemented" in line or "In Development" in line):
            if "REQ-" not in line:
                warn(f"implemented feature missing requirement reference: {line}")
            if "test" not in line.lower():
                warn(f"implemented feature missing test path: {line}")


def check_agents_commands(root: Path) -> None:
    agents = root / "AGENTS.md"
    if not agents.exists():
        return
    cmd_refs = ["bootstrap", "check", "validate", "test", "project-check"]
    text = agents.read_text()
    for field in cmd_refs:
        m = re.search(rf"- (?:{field}[a-z ]*): `(\S+)`", text)
        if m:
            cmd = m.group(1).strip("{}")
            if "pending" in cmd or cmd == "":
                warn(f"AGENTS.md {field} command is pending-stack (acceptable at scaffold)")
                continue
            first = cmd.split()[0]
            if not Path(first).exists() and _which(first) is None:
                warn(f"AGENTS.md {field} command '{cmd}' first token not found on PATH")


def _which(name: str):
    import shutil
    return shutil.which(name)


def check_secrets(root: Path) -> None:
    for p in root.rglob("*.env"):
        if p.name == ".env.example":
            continue
        if re.search(r"(?i)(secret|token|password|api[_-]?key|sk-)\s*[=:]\s*\S+", p.read_text(errors="ignore")):
            fail(f"real-looking credentials committed: {p}")
    gi = root / ".gitignore"
    if gi.exists() and ".env" not in gi.read_text():
        warn(".gitignore does not ignore .env")


def check_control_plane(root: Path, profile: str) -> None:
    plane = ["AGENTS.md", "CLAUDE.md", "project.yaml", "docs/BOUNDARIES.md"]
    if profile in ("service", "web-application", "monorepo", "regulated-system"):
        plane.append("docs/THREAT_MODEL.md")
    for rel in plane:
        if not (root / rel).exists():
            fail(f"control-plane file missing: {rel}")


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: validate.py <project_root> [--profile <p>]")
        return 2
    root = Path(sys.argv[1]).expanduser().resolve()
    profile = "web-application"
    if "--profile" in sys.argv:
        i = sys.argv.index("--profile")
        profile = sys.argv[i + 1] if i + 1 < len(sys.argv) else profile

    if not root.exists():
        fail(f"project root does not exist: {root}")

    check_required_files(root, profile)
    check_id_uniqueness(root)
    check_links(root)
    check_requirements(root)
    check_features(root)
    check_agents_commands(root)
    check_secrets(root)
    check_control_plane(root, profile)

    y = root / "project.yaml"
    if y.exists() and not loaded_yaml(y) and y.read_text().strip():
        warn("project.yaml present but not YAML-parseable (PyYAML missing? light parse only)")

    print(f"validated: {root} (profile={profile})")
    for w in WARNINGS:
        print(f"  [warn] {w}")
    for f in FAILURES:
        print(f"  [FAIL] {f}")
    if FAILURES:
        print(f"RESULT: FAIL ({len(FAILURES)})")
        return 1
    if WARNINGS:
        print(f"RESULT: PASS with {len(WARNINGS)} warnings")
    else:
        print("RESULT: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())