# Agent Operating Contract

## Project

{one paragraph: what <NAME> is, what it does, in what domain, for whom. State
plainly whether it is a research prototype / internal tool / shipped product.}

## Authority and reading order

1. `docs/BOUNDARIES.md` defines hard constraints — never cross them.
2. `docs/REQUIREMENTS.md` defines required behavior.
3. `docs/decisions/` contains accepted technical decisions (ADRs).
4. `docs/ARCHITECTURE.md` describes the current (as-built) implementation.
5. `docs/DESIGN.md` defines product and interaction behavior.
6. `TODO.md` is informational and never overrides the documents above.

Read `docs/INDEX.md` first for the mapping of question → document. Keep this
AGENTS.md a lean router: authority ordering, hard rules, workflow, commands.
The full "every file and what it's used for" table lives in `docs/INDEX.md` and
is loaded on demand, NOT inlined here — a long AGENTS.md dilutes adherence and
burns the context budget on every task.

## Required workflow

1. Read `docs/INDEX.md` and the documents applicable to the change.
2. Identify the relevant requirement IDs (`REQ-*`).
3. Create an ExecPlan under `docs/plans/active/` for cross-package changes,
   migrations, public API changes, authentication/authorization changes, or
   new subsystems.
4. Make the smallest coherent change.
5. Run the required validation commands below.
6. Update affected documentation in the same change.
7. Report tests run, remaining risks, and unresolved assumptions.

## Hard rules

- Never weaken an invariant in `docs/BOUNDARIES.md` merely to make a test pass.
- Never introduce a production dependency without documenting the reason.
- Never modify generated files directly.
- Never expose secrets, credentials, tokens, or customer data in logs.
- Never claim completion unless the required validation commands pass.

## Commands

- Bootstrap: `{bootstrap}`
- Fast validation: `{check}`
- Full validation: `{validate}`
- Test: `{test}`
- Docs contract validation: `{project-check}`

## Definition of done

A change is complete only when implementation, tests, documentation, migration
behavior, and rollback implications are addressed.