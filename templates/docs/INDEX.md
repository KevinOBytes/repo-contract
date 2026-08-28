# Documentation Index

Every document answers one distinct question. Read the row for what you need.

| Question                                              | Document                          |
| ----------------------------------------------------- | --------------------------------- |
| What is this project, and how do I run it?            | `README.md`                       |
| How must an agent work in this repository?            | `AGENTS.md`                       |
| What must the product/system do?                      | `docs/REQUIREMENTS.md`            |
| What capabilities exist or are planned?               | `docs/FEATURES.md`                |
| How should the product/interface behave?              | `docs/DESIGN.md`                  |
| What must never be crossed or violated?               | `docs/BOUNDARIES.md`              |
| How is the current system actually built?             | `docs/ARCHITECTURE.md`            |
| Why was an architectural choice made?                 | `docs/decisions/*.md` (ADRs)      |
| How will a substantial change be executed?            | `docs/plans/active/*.md`          |
| What work is immediately pending?                     | `TODO.md` (generated view)        |
| How do we prove it works?                             | `docs/TESTING.md`                 |
| How is it deployed/observed/recovered?                | `docs/OPERATIONS.md`              |
| What are the abuse cases and failure modes?           | `docs/THREAT_MODEL.md`            |
| What do the terms mean?                               | `docs/GLOSSARY.md`                |

Searching for a change's impact: read `docs/BOUNDARIES.md` and
`docs/REQUIREMENTS.md` first; if you change how the product is built or behaves,
update the matching document in the same change.