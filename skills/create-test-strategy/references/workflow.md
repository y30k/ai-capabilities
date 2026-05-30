# Test Strategy Workflow

## 1. Confirm Scope

- Identify source requirements: PRD, technical design, project items, issue list, or release candidate.
- Identify target users, systems, repos, and environments.
- Confirm whether the output is a draft plan, an approved gate, or a backlog of test work.
- If requirements are unclear, ask instead of inventing acceptance criteria.

## 2. Discover Existing Validation

Inspect repo files before recommending tests:

- package/build/test scripts, CI workflows, Makefiles, task runners, Docker/compose files
- existing unit, integration, e2e, browser, contract, migration, load, accessibility, and security tests
- fixtures, factories, seed data, snapshots, mocks, service emulators, and test environments
- release docs, quality gates, coverage expectations, performance budgets, SLOs, and dashboards

Record exact commands and files. If a command needs secrets/services, name the prerequisite.

## 3. Build the Validation Matrix

Use this structure:

```markdown
# {Feature} Test Strategy

## Scope
- Sources: {PRD/design/items}
- Target repos/systems: {list}
- Gate status: draft | proposed | approved

## Existing Validation Inventory
- `{path}` — {command/test/fixture and relevance}

## Validation Matrix
| Requirement/Story | Risk | Acceptance Criteria | Test Level | Command/Method | Data/Env | Owner | Gate? |
| --- | --- | --- | --- | --- | --- | --- | --- |

## Nonfunctional Checks
| Area | Needed? | Check | Baseline/Budget | Notes |
| --- | --- | --- | --- | --- |

## Missing Harnesses or Blockers
- {missing data/env/tool/baseline/signoff} — {impact and proposed item}

## Recommended Story/Test Work
- {story or test task} — {dependency and validation value}
```

## 4. Choose Appropriate Test Levels

Favor the smallest reliable check that proves behavior:

- unit tests for pure logic, validation, parsing, formatting, reducers, and isolated utilities
- integration/contract tests for database, API, service, queue, CLI, and provider boundaries
- e2e/browser/manual checks for full user journeys and high-confidence UI flows
- migration/rollback checks for schema/data changes
- performance/load/bundle checks for hot paths, costly operations, and budgets
- accessibility checks for changed user-facing UI
- security/privacy checks for auth, authorization, secrets, tenancy, sensitive data, audit, and abuse cases
- observability checks for logs, metrics, traces, alerts, dashboards, and feature-flag visibility

Do not require slow end-to-end tests when a narrower check gives equal confidence. Do not accept only unit tests for cross-system risks.

## 5. Identify Work Items and Gates

- Mark which checks are mandatory gates for implementation, PR review, readiness, and post-release observation.
- If test infrastructure work is needed, create proposed items for `create-prd-work-items` instead of hiding it in prose.
- If a performance-sensitive change lacks a baseline, propose a baseline task and measurement method.
- If a gate is external or manual, document who/what must provide signoff.

## 6. Report and Handoff

End with:

```markdown
## Test Strategy Summary

**Recommended gate set**: {commands/manual checks}
**Blockers**: {none or list}
**New work items needed**: {none or list}
**Next**: Use `create-prd-work-items` to add validation tasks, then `implement-prd-stories` to implement unblocked items with these checks.
```
