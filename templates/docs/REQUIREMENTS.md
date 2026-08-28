---
document_id: requirements
status: current
owner: {owner}
last_reviewed: {date}
review_interval_days: 90
---

# Requirements

High-level intent: {one short paragraph on product/system purpose.}

ID convention: `REQ-<AREA>-<NNN>`. `Status` ∈ Accepted | Draft | Superseded.
`Priority` ∈ Must | Should | Could. "Must"/"shall" carry real weight: every
Accepted requirement has acceptance criteria AND a verification method.

## {Area one, e.g. Authentication}

### REQ-{AREA}-001 — {Title}

**Status:** Accepted
**Priority:** Must
**Feature:** FTR-{AREA}-001

The system shall {observable required behavior}.

#### Acceptance criteria
- {criterion 1, testable and specific}
- {criterion 2}

#### Verification
- `TEST-{AREA}-00N` (see `docs/TESTING.md`)
- {E2E / unit / integration hook}

## {Area two, e.g. Data}

### REQ-{AREA}-002 — {Title}

...repeat for every real requirement. Do not bloat — capture what must be true.