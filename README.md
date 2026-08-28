# repo-contract

A machine-validated **repository documentation contract** for agent-driven
projects: nine Markdown documents, each answering exactly one question, bound
together by a machine-readable manifest (`project.yaml`) and enforced by a
validator (`scripts/validate.py`).

The goal is not "every repo has the same eight Markdown files." It is that every
repo exposes a predictable, versioned, testable contract that humans and agents
can navigate, query, validate, and update through normal source control.
No tool is a substitute for a human review of the control plane — but a spec
alone doesn't stop agents from following docs that drifted out of context. This
repo makes adherence checkable.

## What this repo is

| Artifact | Purpose |
|---|---|
| `SPEC.md` | The normative description of the standard (why each doc exists, what must be in it, ID conventions, profiles). |
| `templates/` | Fill-in starter content for every document and decision/plan skeleton, keyed to the profiles. |
| `scripts/validate.py` | The validator: makes "complete and consistent" a testable property, not a promise. |
| `project.yaml` | This repo's own manifest — the contract applied to itself (dogfooding). |

## Quickstart

Scaffold a new project:

```bash
mkdir -p ~/Projects/newproj && cd ~/Projects/newproj
# create your documents from templates/, fill per SPEC.md, then:
python3 scripts/validate.py . --profile web-application
```

Validate an existing repo:

```bash
python3 scripts/validate.py /path/to/repo --profile service
```

Exit 0 = pass (warnings allowed). Exit 1 = one or more contract failures that
must be fixed before the docs are trustworthy.

## Profiles

Generate exactly the file set your project needs — do not cargo-cult optional
files. See `SPEC.md#profiles`.

- `library` — CLI / package / helper
- `service` — backend / API-only
- `web-application` — anything with a web UI
- `monorepo` — multi-package
- `regulated-system` — FDA/ISO/certification or compliance-bound

## Documentation

- `docs/INDEX.md` — this repo's question → document router.
- `docs/SPEC.md` — **the standard itself** (normative).
- `docs/BOUNDARIES.md` — hard constraints for working in this repo.
- `docs/REQUIREMENTS.md` — requirements for the standard's own tooling.
- `docs/ARCHITECTURE.md` — how the validator and templates fit together.
- `docs/TESTING.md` — how the contract is verified.
- `docs/decisions/` — ADRs for the standard's design choices.

## License

MIT. See `LICENSE`.