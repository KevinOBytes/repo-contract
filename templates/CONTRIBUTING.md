# Contributing

## Getting started
- {setup, toolchain, and how to run the app/tests}

## Development workflow
1. Read `docs/INDEX.md` and the documents governing your change.
2. Create an ExecPlan under `docs/plans/active/` for substantial changes
   (see `docs/plans/README.md`).
3. Make the smallest coherent change; update affected docs in the same change.
4. Run the full validation commands (see `AGENTS.md` → Commands).
5. Open a PR. If your change touches the control plane (`AGENTS.md`,
   `project.yaml`, `docs/BOUNDARIES.md`, `.agents/`), it needs explicit human
   review — an AI reviewer alone is not sufficient.

## Definition of done
Implementation + tests + documentation + migration/rollback addressed, and all
validation commands pass (`AGENTS.md` → Definition of done).

## Code standards
- {lint/format instructions}
- No secrets or credentials in code, commits, or logs.