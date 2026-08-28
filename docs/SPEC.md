# SPEC — Repository Documentation Contract

**Status:** normative — the single source of truth for what this standard *is*.
**Version:** 1.0
**Owner:** TKOResearch / KevinOBytes

## 1. Purpose

A machine-validated contract that makes a repository's documentation
predictable, testable, and safe for autonomous agents to navigate, query, and
update. Every document answers exactly one question; the manifest
(`project.yaml`) makes the set machine-readable; the validator
(`scripts/validate.py`) enforces consistency. This prevents the failure mode
where overlapping Markdown files drift out of date while agents still treat them
as authoritative.

## 2. The conceptual model

| Question                                              | Canonical document            |
| ----------------------------------------------------- | ----------------------------- |
| What is this project, and how do I run it?            | `README.md`                   |
| How must an agent work in this repository?            | `AGENTS.md`                   |
| What must the product/system do?                      | `docs/REQUIREMENTS.md`        |
| What capabilities exist or are planned?               | `docs/FEATURES.md`            |
| How should the product or interface behave?           | `docs/DESIGN.md`              |
| What must never be crossed or violated?               | `docs/BOUNDARIES.md`          |
| How is the current system actually built?             | `docs/ARCHITECTURE.md`        |
| Why was a particular architectural choice made?       | `docs/decisions/*.md` (ADR)   |
| How will a substantial change be executed?            | `docs/plans/active/*.md`      |
| What work is immediately pending?                     | `TODO.md`                     |
| How do we prove it works?                             | `docs/TESTING.md`             |
| How is it deployed/observed/recovered?                | `docs/OPERATIONS.md`          |
| What are the abuse cases and failure modes?           | `docs/THREAT_MODEL.md`        |
| What do the terms mean?                               | `docs/GLOSSARY.md`            |

### 2.1 Semantic-role rules

- **REQUIREMENTS = WHAT.** Requirements state observable, required behavior.
  They never describe how it is implemented or how a user experiences a flow.
- **DESIGN = HOW the user experiences it.** Journeys, API semantics, state
  transitions, error behavior, domain concepts. Not the implementation.
- **ARCHITECTURE = HOW it is built (as-built).** Real components, data stores,
  flows, failure behavior. Abandoned alternatives go in ADRs, never here.
- **BOUNDARIES = what must never be violated.** Non-goals, trust/data/package/
  dependency/logging/migration/operational boundaries, actions requiring human
  approval. This is the highest-authority file agents read.
- **FEATURES = capability index.** Links to requirements, design section, and
  implementation path. It does NOT repeat requirement wording.
- **TODO.md = short-horizon view, generated from the canonical tracker**
  (GitHub Issues / Linear). Never authoritative for scope.

Overlap is the failure mode. If two documents describe the same behavior, one
of them is wrong — remove the duplicate, do not add a third.

## 3. Identifier conventions

IDs are stable, unique, and scoped by prefix. The validator enforces that an ID
may only be *defined* by the file owning its prefix (occurrences elsewhere are
legitimate references).

| Prefix    | Owned by                        | Format               |
| --------- | ------------------------------- | -------------------- |
| `REQ`     | `docs/REQUIREMENTS.md`          | `REQ-<AREA>-<NNN>`   |
| `FTR`     | `docs/FEATURES.md`              | `FTR-<AREA>-<NNN>`   |
| `BOUNDARY`| `docs/BOUNDARIES.md`            | `BOUNDARY-<AREA>-<NNN>` |
| `ADR`     | `docs/decisions/ADR-*.md`       | `ADR-<NNNN>`         |
| `TEST`    | `docs/TESTING.md`               | `TEST-<AREA>-<NNN>`  |

## 4. Authority ordering

When documents conflict, this ordering resolves the conflict:

```
BOUNDARIES > REQUIREMENTS > ADRs (status Accepted) > DESIGN > ARCHITECTURE > TODO
```

`TODO.md` is informational and never overrides a normative document.

## 5. Document requirements (per profile)

| File                    | Profile set           | Minimum content                                   |
| ----------------------- | --------------------- | ------------------------------------------------- |
| `README.md`             | all                   | what it is, how to run it, status                 |
| `AGENTS.md`             | all                   | project, authority order, workflow, hard rules, commands, DoD |
| `CLAUDE.md`             | all                   | `@AGENTS.md` import (+ Claude notes)              |
| `TODO.md`               | all                   | generated active-work view                        |
| `project.yaml`          | all                   | schema_version, profile, documents, commands, plan_required, protected_control_plane |
| `docs/INDEX.md`         | all                   | question → document table                         |
| `docs/REQUIREMENTS.md`  | all                   | `REQ-*` blocks with Status/Priority/AC/Verification |
| `docs/FEATURES.md`      | all                   | `FTR-*` rows linking to reqs, design, impl, tests |
| `docs/DESIGN.md`        | all                   | journeys, API semantics, state, errors, concepts  |
| `docs/BOUNDARIES.md`    | all                   | `BOUNDARY-*` invariants                            |
| `docs/ARCHITECTURE.md`  | all                   | as-built system                                   |
| `docs/TESTING.md`       | all                   | strategy mapped to `REQ-*`                        |
| `docs/GLOSSARY.md`      | all                   | shared domain terms                               |
| `docs/decisions/`       | all (≥1 ADR)          | ADR entries (Status/Context/Decision/Consequences)|
| `docs/plans/`           | all                   | ExecPlan format + active/completed dirs           |
| `docs/OPERATIONS.md`    | service, web-application, monorepo, regulated-system | deploy, observe, recover, rollback |
| `docs/THREAT_MODEL.md`  | service, web-application, monorepo, regulated-system | assets, trust boundaries, threats, failure modes |
| `CONTRIBUTING.md`       | service+, monorepo, regulated-system | dev workflow, DoD                   |
| `SECURITY.md`           | service+, monorepo, regulated-system | vulnerability reporting policy     |
| `.env.example`          | web-application       | schema only, no real secrets                     |
| nested `AGENTS.md`      | monorepo              | per-package deltas only                          |
| `BASELINE.md`           | regulated-system      | validation evidence, approval checklist          |

### 5.1 Profiles

| Profile            | Default when                          |
| ------------------ | ------------------------------------- |
| `library`          | CLI, package, helper                  |
| `service`          | backend / API-only                    |
| `web-application`  | anything with a web UI                |
| `monorepo`         | multi-package                         |
| `regulated-system` | FDA/ISO/certification or compliance-bound |

## 6. Requirements framing

- `Status` ∈ {Draft, Accepted, Superseded}. Only Accepted requirements carry
  weight.
- `Priority` ∈ {Must, Should, Could}. "Must"/"shall" mean something.
- Every Accepted requirement SHALL have a distinct ID, acceptance criteria,
  and a verification reference (test ID or method).

## 7. ADR format

Each ADR: `Status`, `Date`, `Deciders/Considers`, `Context`, `Decision`,
`Consequences` (positive/negative/risks), `Alternatives considered`.

## 8. ExecPlan format

Required for: cross-package changes, migrations, public API changes, auth/az
changes, new subsystems. Each plan: Status, Owner, Started, Requirements,
Boundaries, Scope, Background, numbered Plan steps with completion criteria,
Rollback, Risks/mitigations, Test plan. Live while in flight under
`docs/plans/active/`; moved to `completed/` when done.

## 9. The manifest (`project.yaml`)

Fields: `schema_version`, `profile`, `name`, `description`, `documents`
(path + authority + optional id_prefix per document), `commands`
(bootstrap/check/test/validate/project-check), `plan_required` (paths +
change_types), `protected_control_plane` (paths requiring human review).
The validator reads these fields; every read field MUST be documented here.

## 10. Machine validation

`scripts/validate.py <root> [--profile P]` checks (exit 0 pass / 1 fail):

1. Profile-required documents exist and have a non-trivial body.
2. `project.yaml` exists and parses.
3. ID-prefix ownership is respected; no ID defined twice.
4. Internal Markdown links under `docs/` resolve.
5. Every Accepted requirement has acceptance criteria + verification.
6. Implemented/in-development features reference a requirement and a test path.
7. AGENTS.md command tokens exist (best-effort PATH check).
8. No committed `.env` containing real-looking credentials.
9. Control-plane files present.

## 11. Control plane

Changes to the control plane — `AGENTS.md`, `CLAUDE.md`, `project.yaml`,
`docs/BOUNDARIES.md`, threatened precepts in `SPEC.md`, `.agents/`, GitHub
workflows, secrets — are "control-plane changes" requiring explicit human
review; an AI reviewer alone is not sufficient. Rationale: a careless or
malicious change can modify the very instructions an agent trusts.

## 12. Non-goals

- NOT a replacement for a code scaffolding tool (pairs with one).
- NOT a code-standards linter; it validates documentation consistency only.
- NOT a substitute for human review of control-plane or security changes.
- NOT an automatic "real-time capable" or "airworthy/fail-safe" claim
  generator — see fleet safety-language rules below.

## 13. Safety language

For embedded/control systems: never claim "flight safe", "airworthy",
"certified", "production safe", or "fail-safe" based on simulation or docs
alone. Allowed: "research prototype", "simulator verified", "tested under
defined scenarios", "control allocation prototype". Claims require an actual
verification program.