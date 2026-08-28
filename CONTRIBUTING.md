# Contributing

## Getting started
- Requires Python 3 (stdlib only for the validator).
- `python3 -m pytest -q` runs the validator's test suite.

## Development workflow
1. Read `docs/INDEX.md` and the documents governing your change.
2. Create an ExecPlan under `docs/plans/active/` for substantial changes (see
   `docs/plans/README.md`).
3. Make the smallest coherent change; update affected docs in the same change.
4. Run full validation: `python3 -m pytest -q && python3 scripts/validate.py . --profile library`
5. Open a PR. Control-plane changes (`AGENTS.md`, `project.yaml`,
   `docs/BOUNDARIES.md`, `docs/SPEC.md`, `templates/`) need explicit human
   review.

## Definition of done
Implementation + tests + documentation all present, all validation commands
pass, and any spec change is mirrored in both `templates/` and
`scripts/validate.py`.