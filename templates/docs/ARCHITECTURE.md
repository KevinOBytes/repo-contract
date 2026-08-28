---
document_id: architecture
status: current
owner: {owner}
last_reviewed: {date}
review_interval_days: 90
---

# Architecture (as-built)

Describes what IS implemented. Abandoned alternatives belong in ADRs, not here.

- System context: {the system and its actors/external systems}
- Components / containers: {diagram ref + prose; `docs/diagrams/containers.mmd`}
- Runtime topology: {processes, deploy targets, networking}
- Data stores and ownership: {databases, tables, who owns each}
- External dependencies: {services, libraries with rationale}
- Authentication and authorization flow: {how identity flows through}
- Data flows: {primary request and background-job flows}
- Background jobs: {cadence, idempotency, failure handling}
- Caching: {layers, invalidation, consistency guarantees}
- Deployment environments: {dev/staging/prod differences}
- Failure behavior: {what degrades, what fails closed}
- Observability: {metrics/logs/traces; alerting}
- Recovery and rollback: {restore, replay, rollback steps}
- Known technical debt: {honest list, linked to TODO items}