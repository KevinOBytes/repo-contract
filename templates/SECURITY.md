# Security Policy

{Short policy for a personal/private project. Expand for public projects.}

## Reporting a vulnerability

For private/internal prototype: report privately to the owner (`{owner}`) — do
not file an issue for an active vulnerability.

For public projects: describe the issue, affected version, and impact; expect
an acknowledgement and a fix timeline. Do not publicly disclose until a fix is
available.

## Scope
- In scope: {this codebase}
- Security-sensitive: `docs/BOUNDARIES.md`, `docs/THREAT_MODEL.md`,
  authentication/authorization paths, anything touching secrets.

## Remediation expectations
- Fixes land with a regression test.
- Secrets are rotated, never re-used.
- Security fixes take precedence over feature work.