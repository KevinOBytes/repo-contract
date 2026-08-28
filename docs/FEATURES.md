---
document_id: features
status: current
owner: TKOResearch
---

# Features

| ID          | Capability              | Status      | Requirements            | Design                     | Implementation            | Tests |
| ----------- | ----------------------- | ----------- | ----------------------- | -------------------------- | ------------------------- | ----- |
| FTR-STD-001 | Disjoint document roles | Implemented | REQ-STD-001             | docs/DESIGN.md#concepts    | docs/SPEC.md              | test_validator.py |
| FTR-STD-002 | Stable identifiers      | Implemented | REQ-STD-002             | docs/DESIGN.md#concepts    | docs/SPEC.md              | test_validator.py |
| FTR-STD-003 | Authority ordering     | Implemented | REQ-STD-003             | docs/SPEC.md §4            | docs/SPEC.md              | test_validator.py |
| FTR-STD-004 | Profiles                | Implemented | REQ-STD-004             | docs/SPEC.md §5.1          | templates/                | test_validator.py |
| FTR-TL-001  | Validator exit semantics| Implemented | REQ-TL-001              | docs/DESIGN.md#cli         | scripts/validate.py       | test_validator.py |
| FTR-TL-002  | ID ownership enforcement| Implemented | REQ-TL-002              | docs/DESIGN.md#concepts    | scripts/validate.py       | test_validator.py |
| FTR-TL-003  | Secret guard            | Implemented | REQ-TL-003              | docs/SPEC.md §10           | scripts/validate.py       | test_validator.py |
| FTR-CT-001  | Templates match spec    | Implemented | REQ-CT-001              | docs/SPEC.md §5            | templates/                | test_validator.py |