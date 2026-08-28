---
document_id: threat_model
status: current
owner: security
last_reviewed: {date}
review_interval_days: 90
---

# Threat Model

Pairs with `docs/BOUNDARIES.md`: boundaries define constraints, this file maps
abuse cases and failures onto them.

## Assets & impact
- {asset} — {value}, worst-case impact if compromised/lost.

## Trust boundaries and entry points
- {each trust boundary from BOUNDARIES.md, and the entry points that cross it}

## Threat actors
- {who is attacking, their capability and goals}

## Threats
| ID        | Threat                         | Entry/asset      | Mitigation                       | Boundary       |
| --------- | ------------------------------ | ---------------- | -------------------------------- | -------------- |
| THREAT-001 | {threat statement}             | {vector}         | {control}                        | BOUNDARY-*-NNN |

## Failure modes (non-adversarial)
- {issues, crash, stale state, dependency failure} and how they degrade safely.

## Residual risk
- {what is knowingly accepted, and why}.