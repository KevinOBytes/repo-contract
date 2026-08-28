---
document_id: features
status: current
owner: {owner}
---

# Features

Capability index, not a second copy of requirements. Each feature links to its
requirements, its design section, and its implementation path. Generation is
intended from `REQUIREMENTS.md` + source, so entries stay one-line.

| ID            | Capability           | Status       | Requirements             | Design                             | Implementation | Tests          |
| ------------- | -------------------- | ------------ | ------------------------ | ---------------------------------- | -------------- | -------------- |
| FTR-{A}-001   | {name}               | Planned      | REQ-{A}-001, REQ-{A}-002 | `docs/DESIGN.md#section`           | `src/{path}/`   | `tests/{path}/`|
| FTR-{A}-002   | {name}               | Implemented  | REQ-{A}-003              | `docs/DESIGN.md#section`           | `src/{path}/`   | `tests/{path}/`|

Status ∈ Planned | Backlog | In Development | Implemented | Deprecated.
`Implemented` requires a requirement reference AND a test pointer.