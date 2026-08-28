---
document_id: architecture
status: current
owner: TKOResearch
---

# Architecture (as-built)

## System context
`repo-contract` is a library-style repo: it ships a spec, starter templates,
and a stdlib-Python validator that agents/humans run against a project root.
It has no server, no network dependencies, no runtime topology to deploy.

## Components
- `docs/SPEC.md` — the normative standard.
- `templates/` — fill-in starter content keyed to profiles.
- `scripts/validate.py` — the validator (single-file CLI, stdlib only).
- `test_validator.py` — pytest fixtures exercising the validator's pass/fail
  paths.
- `project.yaml` — the repo's own manifest (dogfooding the standard).

## Data flow
1. Agent/user scaffolds a project from `templates/` (fill per `SPEC.md`).
2. Agent/user runs `python3 scripts/validate.py <root> --profile <P>`.
3. Validator reads `project.yaml` + the Markdown tree, emits check results,
   exits 0/1.

## Failure behavior
- Returns a human-readable failure per check; never halts mid-file on a single
  error — it collects all failures then reports.
- Degrades gracefully if PyYAML is absent (light manifest parse only).

## Observability
None needed for a CLI; its "observability" is its structured stdout and exit
code, consumed by CI.

## Recovery / rollback
No persistent state; the repo is the artifact. Rollback = revert a commit.