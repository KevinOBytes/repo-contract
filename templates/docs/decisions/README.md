# Decisions (`docs/decisions/`)

Architecture Decision Records (ADRs) live here, one file per decision:
`ADR-<NNNN>-<slug>.md`. They answer "why was this choice made?" — the one
question not answered elsewhere.

## Required ADR format
Status, Date, Deciders/Considers, Context, Decision, Consequences
(positive/negative/risks), Alternatives considered.

## Rules
- Number sequentially: `ADR-0001`, `ADR-0002`, … never reuse a number.
- An `Accepted` ADR participates in the authority ordering
  (`docs/BOUNDARIES.md` > `docs/REQUIREMENTS.md` > Accepted ADRs > …).
- Abandoned alternatives belong here, never in `ARCHITECTURE.md`.