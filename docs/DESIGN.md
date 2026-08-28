---
document_id: design
status: current
owner: TKOResearch
---

# Design

How this standard behaves for its two users: a *human/agent scaffolder* and a
*machine* (CI).

## User journeys
- *Scaffold:* agent reads `SPEC.md`, copies `templates/` into a fresh
  `~/Projects/<name>/`, fills each doc for the project, runs the validator.
- *Validate:* user/CI runs `validate.py <root> --profile P`; reads a PASS/fail
  list; fixes failures; re-runs until clean.

## CLI semantics
- `validate.py <root> [--profile <P>]` — `<root>` is the project directory.
- Exit `0` = pass (warnings allowed), `1` = ≥1 failure, `2` = usage error.
- Output is `warning:`/`FAIL:` prefixed lines plus a `RESULT: …` summary line.
- Default profile `web-application` when `--profile` omitted but not valid:
  callers SHOULD pass an explicit profile.

## Error behavior
- Missing project root → `FAIL` line, exit 1.
- Unparsable `project.yaml` → warning (stdlib degradation), not a hard fail.
- A genuinely empty duplicate-definition or missing-file check is a hard fail.

## Domain concepts
- *Document role*: the one question a document answers.
- *Profile*: a named file-set + scope for the contract.
- *Control plane*: files whose modification can alter agent trust, requiring
  human review.
- *Definition vs reference*: an ID is a definition in its owner file; anywhere
  else it is a reference.