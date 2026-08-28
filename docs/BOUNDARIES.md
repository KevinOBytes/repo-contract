---
document_id: boundaries
status: current
owner: TKOResearch
last_reviewed: 2026-08-28
review_interval_days: 90
---

# Boundaries

ID convention `BOUNDARY-<AREA>-<NNN>`. Hard constraints for this repository and
for the standard it ships. This is the highest-authority file agents read.

## Product scope and non-goals
- BOUNDARY-SCOPE-001: This repo defines a documentation *contract* and the
  tooling/content that implement it. It does not scaffold application code.
- BOUNDARY-SCOPE-002: It is not a code quality linter; it validates document
  consistency only.

## Trust boundaries
- BOUNDARY-TRUST-001: `scripts/validate.py` reads only files under the given
  project root. It never writes outside it.

## Data boundaries
- BOUNDARY-DATA-001: The validator may read the project's doc tree and
  `project.yaml`; it may not read or log secrets outside the target repo.

## Dependency boundaries
- BOUNDARY-DEP-001: The validator runs on Python stdlib only; optional PyYAML
  may improve `project.yaml` parsing but must degrade gracefully when absent.
- BOUNDARY-DEP-002: No production dependency may be introduced into the
  validator without documenting the reason and updating SPEC §10.

## Control-plane boundaries
- BOUNDARY-CTL-001: `AGENTS.md`, `CLAUDE.md`, `project.yaml`,
  `docs/BOUNDARIES.md`, `docs/SPEC.md`, `templates/**`, and `.github/**` are
  control-plane paths; changes require explicit human review, not an AI
  reviewer alone.

## Consistency boundaries
- BOUNDARY-CONS-001: `templates/` and `scripts/validate.py` must remain
  mutually consistent with `docs/SPEC.md`. A change to one that invalidates the
  other is a control-plane change.

## Logging boundaries
- BOUNDARY-LOG-001: Never log tokens, credentials, or customer data. The
  validator reports file paths and check names only.

## Actions requiring explicit human approval
- Any change to `docs/SPEC.md` (the normative standard).
- Any change to `docs/BOUNDARIES.md` itself.
- Any change to the validator's exit semantics (`REQ-TL-001`).
- Any change to the control-plane path set (`project.yaml` →
  `protected_control_plane`).