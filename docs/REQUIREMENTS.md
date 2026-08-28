---
document_id: requirements
status: current
owner: TKOResearch
last_reviewed: 2026-08-28
review_interval_days: 90
---

# Requirements

High-level intent: define a machine-validated repository documentation
contract and provide tooling (`scripts/validate.py`) and content
(`templates/`) that make it reproducible. ID convention `REQ-<AREA>-<NNN>`.

## Standard

### REQ-STD-001 — Disjoint document roles
**Status:** Accepted
**Priority:** Must
**Feature:** FTR-STD-001

The standard shall assign exactly one semantic role to each canonical document
as listed in `docs/SPEC.md` §2.

#### Acceptance criteria
- The question→document table in SPEC §2 lists each document exactly once.
- Two documents do not describe the same question.

#### Verification
- `TEST-STD-001` (SPEC table = document set)

### REQ-STD-002 — Stable identifiers
**Status:** Accepted
**Priority:** Must
**Feature:** FTR-STD-002

The standard shall define a stable `PREFIX-AREA-NNN` identifier scheme,
documented in SPEC §3.

#### Acceptance criteria
- Each prefix is owned by exactly one file.
- An ID defined in its owner appears nowhere else as a definition.

#### Verification
- `TEST-STD-002`

### REQ-STD-003 — Authority ordering
**Status:** Accepted
**Priority:** Must
**Feature:** FTR-STD-003

The standard shall define an unambiguous authority ordering resolving document
conflicts.

#### Acceptance criteria
- SPEC §4 documents the ordering.
- `TODO.md` is never authoritative.

#### Verification
- `TEST-STD-003`

### REQ-STD-004 — Profiles
**Status:** Accepted
**Priority:** Should
**Feature:** FTR-STD-004

The standard shall define profiles (`library`, `service`, `web-application`,
`monorepo`, `regulated-system`) with per-profile file sets.

#### Acceptance criteria
- Each profile lists exactly the files it requires (SPEC §5.1).

#### Verification
- `TEST-STD-004`

## Tooling

### REQ-TL-001 — Validator exit semantics
**Status:** Accepted
**Priority:** Must
**Feature:** FTR-TL-001

`scripts/validate.py` shall exit `0` on pass and nonzero on any contract
failure, printing human-readable failure lines.

#### Acceptance criteria
- Exit 0 when all checks pass.
- Exit nonzero listing each check failure.

#### Verification
- `TEST-TL-001`, `TEST-TL-002`

### REQ-TL-002 — ID ownership enforcement
**Status:** Accepted
**Priority:** Must
**Feature:** FTR-TL-002

The validator shall treat an ID as a definition only in its owning file, and
report duplicate definitions.

#### Acceptance criteria
- A `REQ-*` referenced in `FEATURES.md` is not flagged.
- A `REQ-*` defined twice in `REQUIREMENTS.md` is flagged.

#### Verification
- `TEST-TL-003`, `TEST-TL-004`

### REQ-TL-003 — Secret guard
**Status:** Accepted
**Priority:** Must
**Feature:** FTR-TL-003

The validator shall fail on any committed `.env` (not `.env.example`)
containing real-looking credentials.

#### Acceptance criteria
- `.env.example` is allowed.
- `.env` with an `API_KEY=value` fails the check.

#### Verification
- `TEST-TL-005`

## Content

### REQ-CT-001 — Templates match spec
**Status:** Accepted
**Priority:** Must
**Feature:** FTR-CT-001

Every template in `templates/` shall reflect the structure and conventions the
validator enforces.

#### Acceptance criteria
- A scaffolded project built only from `templates/` passes validation (with
  minimal considered stubs replaced).
- No validator check lacks a corresponding SPEC guidance note.

#### Verification
- `TEST-CT-001`