# Security Policy

## Reporting a vulnerability

Private/prototype: report to the maintainer directly; do not file an issue for
an active vulnerability.

Public: describe the issue, affected version, and impact. Expect
acknowledgement and a fix timeline. Do not publicly disclose until a fix is
available.

## Scope
- In scope: this repository and the tooling it ships.
- Security-sensitive: `docs/BOUNDARIES.md`, `docs/SPEC.md`, `scripts/validate.py`
  (it inspects arbitrary project trees), anything touching the control plane.

## Remediation expectations
- Fixes land with a regression test.
- Secrets are rotated, never re-used.
- Security fixes take precedence over feature work.