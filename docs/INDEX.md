# Documentation Index

Every document answers one distinct question. Read the row for what you need.

| Question                                              | Document                            |
| ----------------------------------------------------- | ----------------------------------- |
| What is this project, and how do I run it?            | `../README.md`                      |
| How must an agent work in this repository?            | `../AGENTS.md`                      |
| What is the normative standard itself?                | `SPEC.md`                           |
| What must the standard/tooling do?                    | `REQUIREMENTS.md`                   |
| What capabilities exist or are planned?               | `FEATURES.md`                       |
| How should the tools/docs behave?                     | `DESIGN.md`                         |
| What must never be crossed or violated?               | `BOUNDARIES.md`                     |
| How is the current system actually built?             | `ARCHITECTURE.md`                   |
| Why was an architectural choice made?                 | `decisions/*.md` (ADRs)             |
| How will a substantial change be executed?            | `plans/active/*.md`                 |
| What work is immediately pending?                     | `../TODO.md` (generated view)       |
| How do we prove it works?                             | `TESTING.md`                        |
| What do the terms mean?                               | `GLOSSARY.md`                       |

Searching for a change's impact: read `BOUNDARIES.md` and `SPEC.md` first; if
you change what the standard is or how the tooling behaves, update the matching
document in the same change.