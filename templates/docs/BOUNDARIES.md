---
document_id: boundaries
status: current
owner: {owner}
last_reviewed: {date}
review_interval_days: 90
---

# Boundaries

ID convention: `BOUNDARY-<AREA>-<NNN>`. This is the highest-authority file
agents read. Statements here are hard constraints — do not weaken one to make
a test pass or a feature easier.

## Product scope and non-goals
- BOUNDARY-SCOPE-001: {in scope}
- BOUNDARY-SCOPE-002: {explicit non-goal}

## Trust boundaries
- BOUNDARY-TRUST-001: {where untrusted input crosses into trusted state}

## Data classification boundaries
- BOUNDARY-DATA-001: {what data is sensitive, how it must be handled}

## Authentication and authorization invariants
- BOUNDARY-AUTH-001: {must hold; e.g. server-side enforcement only}

## Package and import boundaries
- BOUNDARY-PKG-001: {direction of allowed dependencies, e.g. domain may not
  depend on application}

## Allowed and prohibited dependencies
- BOUNDARY-DEP-001: {prohibited categories}
- BOUNDARY-DEP-002: {allowlist rationale}

## External-service boundaries
- BOUNDARY-EXT-001: {which external services may be contacted, and how}

## Logging and telemetry boundaries
- BOUNDARY-LOG-001: {never log secrets/tokens/PII}

## Migration and backward-compatibility boundaries
- BOUNDARY-MIG-001: {compat guarantees, rollback posture}

## Operational boundaries
- BOUNDARY-OPS-001: {deploy/run constraints, approval gates}

## Actions requiring explicit human approval
- {list: prod migrations, auth changes, control-plane edits, external-svc
  additions, dependency changes}