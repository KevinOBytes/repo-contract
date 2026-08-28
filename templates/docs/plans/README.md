# Execution Plans (`docs/plans/`)

An ExecPlan is required for: cross-package changes, database migrations, public
API changes, authentication/authorization changes, new subsystems, or any work
that spans multiple documents/repositories. A checklist item in `TODO.md` is
not a substitute — substantial work gets a real plan.

## Lifecycle

1. Author the plan in `active/<name>.md` before starting the work.
2. Keep it a LIVING document — update status/scoping as reality diverges.
3. When complete, move it to `completed/<name>.md` and check off the
   associated `TODO.md` items.

## Required structure

```markdown
# <Title>

- Status: Draft | Active | Complete | Abandoned
- Owner: {owner}
- Started: {date}
- Requirements: REQ-{AREA}-NNN [REQ-{AREA}-NNN]
- Boundaries: BOUNDARY-{AREA}-NNN

## Scope
What is included, and explicitly what is NOT (non-goals).

## Background
Why this change; the problem it solves.

## Plan
Numbered execution steps, each ending with a checkable completion criterion.

## Rollback
How to undo; what is irreversible. Must satisfy BOUNDARY-MIG-*.

## Risks and mitigations
Highest-risk steps + how each is de-risked / detected.

## Test plan
Commands and expectations that prove completion (link tests to REQ-*).
```