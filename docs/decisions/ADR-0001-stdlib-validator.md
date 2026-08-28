# ADR-0001 — Stdlib-only Python validator

- Status: Accepted
- Date: 2026-08-28
- Deciders: TKOResearch / KevinOBytes
- Considers: maintainers

## Context

The validator must run anywhere — a CI runner, a contributor laptop, a
one-off Docker build — with zero install friction and no network fetch. A
dependency (e.g. PyYAML) would block validation on machines that don't have it.

## Decision

Implement `scripts/validate.py` on the Python standard library only. PyYAML
may improve `project.yaml` parsing when present but the tool MUST degrade
gracefully to a light parse when absent (warning, not failure). See
`BOUNDARY-DEP-001`.

## Consequences

- Positive: runs everywhere Python 3 is present; trivially testable with the
  stdlib `tempfile`/`subprocess` for fixtures.
- Negative: stricter/more-correct YAML is not guaranteed without PyYAML.
- Risks: silent config misread → mitigated by the warning and by the ID-check
  never depending on YAML semantics.
- Alternatives considered: full PyYAML dependency (rejected: install friction);
  a compiled binary (rejected: overkill for a stdlib CLI).