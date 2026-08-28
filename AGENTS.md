# Agent Operating Contract

## Project

`repo-contract` is a machine-validated documentation standard for agent-driven
software projects. It defines nine Markdown documents with non-overlapping
semantic roles, a machine-readable manifest (`project.yaml`), and a validator
(`scripts/validate.py`). This repository both *describes* the standard
(`docs/SPEC.md`) and *implements* its tooling (`scripts/`) and example content
(`templates/`).

## Authority and reading order

1. `docs/BOUNDARIES.md` defines hard constraints — never cross them.
2. `docs/REQUIREMENTS.md` defines required behavior of the standard/tooling.
3. `docs/decisions/` contains accepted technical decisions (ADRs).
4. `docs/ARCHITECTURE.md` describes the current implementation.
5. `docs/DESIGN.md` defines how tools/docs should behave.
6. `docs/SPEC.md` is the normative spec — the single source of truth for what
   the standard *is*.
7. `TODO.md` is informational and never overrides the documents above.

Read `docs/INDEX.md` first for the mapping of question → document. Keep this
AGENTS.md a lean router: authority ordering, hard rules, workflow, commands.
The full "every file and what it's used for" table lives in `docs/INDEX.md` and
is loaded on demand, NOT inlined here — a long AGENTS.md dilutes adherence and
burns the context budget on every task.

## Required workflow

1. Read `docs/INDEX.md` and the documents applicable to the change.
2. Identify the relevant requirement / spec IDs.
3. Create an ExecPlan under `docs/plans/active/` for cross-package changes,
   public API changes (validator CLI), or new subsystems.
4. Make the smallest coherent change.
5. Run the required validation commands below.
6. Update affected documentation in the same change.
7. Report tests run, remaining risks, and unresolved assumptions.

## Hard rules

- Never weaken an invariant in `docs/BOUNDARIES.md` merely to make a test pass.
- Never change the semantic role of a document in `docs/SPEC.md` without an ADR.
- `templates/` and `scripts/validate.py` must stay mutually consistent: every
  check the validator enforces must correspond to guidance in `SPEC.md`, and
  every field in `project.yaml` the validator reads must be documented.
- Never claim completion unless the validation commands pass.

## Commands

- Bootstrap: `python3 -m pytest -q` (test of the validator against fixtures)
- Fast validation: `python3 scripts/validate.py . --profile library`
- Full validation: `python3 -m pytest -q && python3 scripts/validate.py . --profile library`
- Test: `python3 -m pytest -q`
- Docs contract validation: `python3 scripts/validate.py . --profile library`

## Definition of done

A change is complete only when implementation, tests, documentation, and the
validator's own checks all pass, and any spec change is reflected in both the
templates and the validator.