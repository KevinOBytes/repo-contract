---
document_id: testing
status: current
owner: TKOResearch
---

# Testing

Strategy: the validator is tested with pytest fixtures that build real (minimal)
project trees in a temp dir and assert on exit codes and output.

## Mapping
| Test ID        | Scope                              | Verifies            | Command              |
| -------------- | ---------------------------------- | ------------------- | -------------------- |
| TEST-STD-001   | SPEC table ↔ document set          | REQ-STD-001         | `python3 -m pytest`  |
| TEST-STD-002   | ID prefix ownership                | REQ-STD-002         | `python3 -m pytest`  |
| TEST-STD-003   | authority ordering present in SPEC | REQ-STD-003         | `python3 -m pytest`  |
| TEST-STD-004   | profile file-set completeness      | REQ-STD-004         | `python3 -m pytest`  |
| TEST-TL-001    | validator exit 0 on clean tree     | REQ-TL-001          | `python3 -m pytest`  |
| TEST-TL-002    | validator exit 1 on broken tree    | REQ-TL-001          | `python3 -m pytest`  |
| TEST-TL-003    | REQ ref in FEATURES not flagged    | REQ-TL-002          | `python3 -m pytest`  |
| TEST-TL-004    | duplicate REQ def flagged          | REQ-TL-002          | `python3 -m pytest`  |
| TEST-TL-005    | `.env` secret fails, `.env.example` ok | REQ-TL-003      | `python3 -m pytest`  |
| TEST-CT-001    | templates-only scaffold passes     | REQ-CT-001          | `python3 -m pytest`  |

## Acceptance gate
`python3 -m pytest -q && python3 scripts/validate.py . --profile library` must
pass before marking work complete.