"""Tests for scripts/validate.py — exercise real pass/fail paths.

Each test builds a minimal but realistic project tree in a temp dir, runs the
validator, and asserts on exit code / output. Stdlib-only; no network.
"""
from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

import pytest

SCRIPT = Path(__file__).resolve().parent / "scripts" / "validate.py"

MINIMAL_AGENTS = """\
# Agent Operating Contract
Read docs/INDEX.md first.
- Bootstrap: `python3 -m pip install -r requirements.txt`
- Fast validation: `python3 -m pytest -q`
- Full validation: `python3 -m pytest`
- Test: `python3 -m pytest`
- project-check: `python3 .agents/projectctl/validate.py .`
"""

GOOD_REQ = """\
# Requirements

### REQ-AUTH-001 — Magic-link login
**Status:** Accepted
**Priority:** Must
#### Acceptance criteria
- The link expires after the configured lifetime.
- The link cannot be redeemed more than once.
#### Verification
- TEST-AUTH-001
- TEST-AUTH-002
"""

GOOD_FEATURES = """\
# Features
| ID | Capability | Status | Requirements | Design | Implementation | Tests |
| --- | --- | --- | --- | --- | --- | --- |
| FTR-AUTH-001 | Magic auth | Implemented | REQ-AUTH-001 | docs/DESIGN.md#x | src/auth/ | tests/auth/ |
"""

COMMON_DOCS = {
    "README.md": "# Demo\n\nA real project body with enough words to be non-trivial.\n\n## Quickstart\nrun it.\n",
    "CLAUDE.md": "@AGENTS.md\n",
    "TODO.md": "# Active Work\n\n## Ready\n- [ ] first task\n\nsome body text exceeds trivial threshold comfortably here\n",
    "CONTRIBUTING.md": "# Contributing\n\nGuidance for contributors on how to work in this repo. Enough text to count.\n",
    "SECURITY.md": "# Security\n\nReporting policy text is here and is long enough to be non-trivial.\n",
    "docs/INDEX.md": "# Index\n\n| Q | Doc |\n| --- | --- |\n| What is it | ../README.md |\n| Agent rules | ../AGENTS.md |\n",
    "docs/REQUIREMENTS.md": GOOD_REQ,
    "docs/FEATURES.md": GOOD_FEATURES,
    "docs/DESIGN.md": "# Design\n\nUser journeys and state transitions described at length for the demo project.\n",
    "docs/BOUNDARIES.md": "# Boundaries\n\n- BOUNDARY-AUTH-001: auth checks are server-side only.\n- More invariant text to make the body comfortably non-trivial and clear.\n",
    "docs/ARCHITECTURE.md": "# Architecture\n\nAs-built system described in prose, components, stores, flows, and observability.\n",
    "docs/TESTING.md": "# Testing\n\n| Test ID | Scope | Verifies | Command |\n| --- | --- | --- | --- |\n| TEST-AUTH-001 | expires | REQ-AUTH-001 | pytest |\n| TEST-AUTH-002 | reuse | REQ-AUTH-001 | pytest |\n",
    "docs/GLOSSARY.md": "# Glossary\n\n| Term | Definition |\n| --- | --- |\n| tenant | an owning org |\n| session | auth context |\n",
    "docs/plans/README.md": "# Plans\n\nExecPlan format and lifecycle described here in enough detail to be non-trivial.\n",
}


def build_tree(tmp_path: Path, profile: str = "library", **overrides) -> Path:
    root = tmp_path / "proj"
    root.mkdir()
    (root / ".gitignore").write_text(".env\n")
    (root / "AGENTS.md").write_text(overrides.get("AGENTS.md", MINIMAL_AGENTS))
    (root / "project.yaml").write_text(
        overrides.get(
            "project.yaml",
            f"schema_version: 1\nprofile: {profile}\nname: demo\ndescription: demo project.\n",
        )
    )
    for rel, content in COMMON_DOCS.items():
        p = root / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(overrides.get(rel, content))
    decisions = root / "docs" / "decisions"
    decisions.mkdir(parents=True, exist_ok=True)
    (decisions / "README.md").write_text(
        overrides.get("docs/decisions/README.md",
                      "# Decisions\n\nWhere ADRs live and how they are formatted, explained here.\n")
    )
    (decisions / "ADR-0001-demo.md").write_text(
        overrides.get(
            "docs/decisions/ADR-0001-demo.md",
            "# ADR-0001 — Demo decision\n\n## Context\nsomething\n\n## Decision\nstdlib\n\n## Consequences\nsimple\n",
        )
    )
    return root


def run_validator(root: Path, profile: str = "library"):
    return subprocess.run(
        [sys.executable, str(SCRIPT), str(root), "--profile", profile],
        capture_output=True, text=True,
    )


def test_pass_on_complete_library(tmp_path):
    root = build_tree(tmp_path)
    r = run_validator(root, "library")
    assert r.returncode == 0, (r.returncode, r.stdout + r.stderr)


def test_fail_on_missing_agents(tmp_path):
    root = build_tree(tmp_path)
    (root / "AGENTS.md").unlink()
    r = run_validator(root, "library")
    assert r.returncode == 1
    assert "AGENTS.md" in r.stdout


def test_fail_on_duplicate_requirement_definition(tmp_path):
    root = build_tree(tmp_path)
    req = root / "docs" / "REQUIREMENTS.md"
    req.write_text(GOOD_REQ + "\n### REQ-AUTH-001 — Duplicate\n**Status:** Accepted\n#### Acceptance criteria\n- z\n#### Verification\n- TEST-AUTH-003\n")
    r = run_validator(root, "library")
    assert r.returncode == 1
    assert "REQ-AUTH-001 defined more than once" in r.stdout


def test_feature_reference_to_req_not_flagged_as_dup(tmp_path):
    # A REQ* referenced in FEATURES.md must NOT be flagged as a duplicate def.
    root = build_tree(tmp_path)
    r = run_validator(root, "library")
    assert r.returncode == 0
    assert "duplicate" not in r.stdout


def test_fail_on_committed_secret_env(tmp_path):
    root = build_tree(tmp_path)
    (root / ".env").write_text("API_KEY=sk-live-1234567890abcdef\n")
    r = run_validator(root, "library")
    assert r.returncode == 1
    assert "credentials" in r.stdout


def test_env_example_allowed(tmp_path):
    root = build_tree(tmp_path)
    (root / ".env.example").write_text("API_KEY=\nDB_URL=\n")
    r = run_validator(root, "library")
    assert r.returncode == 0
    assert "credentials" not in r.stdout


def test_usage_no_args(tmp_path):
    r = subprocess.run([sys.executable, str(SCRIPT)], capture_output=True, text=True)
    assert r.returncode == 2