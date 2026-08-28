---
document_id: design
status: current
owner: {owner}
---

# Design

How the product/interface behaves (not how it is built — that is
`ARCHITECTURE.md`; not what it must do — that is `REQUIREMENTS.md`).

## User journeys
- {primary journey, step by step}

## API semantics
- {endpoints/operations, request/response shape, idempotency, error codes}

## State transitions
- {allowed states and transitions, who may trigger them, failure paths}

## Error behavior
- {how errors surface; fail-closed rules; retry semantics}

## Accessibility / usability behavior
- {keyboard, contrast, reduced-motion, localization}

## Domain concepts
- {the nouns and verbs of the domain and how they relate}

## Design principles and trade-offs
- {principles, and what this design consciously accepts in exchange}