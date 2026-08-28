---
document_id: testing
status: current
owner: {owner}
---

# Testing

Strategy mapped to requirements. Each `ACCEPTED` requirement in
`docs/REQUIREMENTS.md` must be verifiable by at least one test reference.

## Test pyramid / layers
- {unit / integration / e2e strategy, per component}

## Mapping
| Test ID        | Scope                                | Verifies            | Command                  |
| -------------- | ------------------------------------ | ------------------- | ------------------------ |
| TEST-{A}-001   | {what it exercises}                  | REQ-{A}-001         | `{test command}`         |
| TEST-{A}-002   | {what it exercises}                  | REQ-{A}-002         | `{test command}`         |

## Property / invariant tests relevant to boundaries
- {each BOUNDARY-* worth guard-railing, and how it's tested}

## Fixtures and isolation
- {test DB, mocks, network isolation rules}

## Acceptance gate
- {exact command(s) that must pass before "complete" is claimed}