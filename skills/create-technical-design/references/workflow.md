# Technical Design Workflow

## 1. Confirm Handoff

- Identify the PRD/spec path, pasted requirements, or issue set.
- Confirm the PRD/spec is approved enough to design. If not, summarize the gap and ask for approval or route to `create-interactive-prd`.
- Identify target repos, deployment surfaces, users/operators, and the desired design artifact path.
- State that no source code will be changed during design.

## 2. Ground in the Codebase

Read real files before technical claims. Inspect the relevant:

- current implementation paths, public APIs, commands, jobs, components, and configuration
- data models, schemas, migrations, contracts, events, queues, and integrations
- tests, fixtures, CI gates, deploy/release docs, feature flags, and observability hooks
- security, auth, permissions, privacy, tenancy, secrets, and audit boundaries when touched

Capture findings with exact paths and symbols. Use `TBD — needs research` for unknowns; do not invent architecture.

## 3. Analyze Options

For each viable option, compare:

- implementation scope and compatibility with existing patterns
- migration/backfill/rollback complexity
- user/operator risk, security/privacy risk, performance/cost risk
- cross-repo or external dependencies
- testability and observability

Prefer the smallest reversible design that satisfies must-have requirements and preserves existing contracts.

## 4. Write the Design

Use this structure unless the repo has its own template:

```markdown
# {Feature} Technical Design

## Inputs
- PRD/spec: {path or ref}
- Target repos/systems: {list}
- Approval state: {state}

## Summary
{one-paragraph design}

## Codebase Findings
- `{path}` — {verified finding}

## Decisions
| Decision | Choice | Alternatives | Rationale | Reversible? |
| --- | --- | --- | --- | --- |

## Proposed Architecture
{components, flows, boundaries, diagrams-as-text if useful}

## API, Data, and Contract Changes
- API/command/event/schema: {change}
- Compatibility: {backward/forward compatibility notes}
- Migration/backfill: {plan or none}

## Security, Privacy, and Permissions
{authz, data handling, tenancy, secrets, audit, abuse cases}

## Performance and Reliability
{latency, throughput, caching, failure modes, retries, queues, resource/cost impact}

## Rollout, Rollback, and Observability
{feature flags, deployment sequencing, metrics, logs, alerts, dashboards, rollback trigger}

## Validation Strategy
{unit/integration/e2e/manual/performance/security/accessibility checks}

## Dependencies and Story Seeds
| Seed | Repo/System | Depends On | Notes |
| --- | --- | --- | --- |

## Risks and Open Questions
- {risk/question} — {owner or next action}
```

## 5. Gate and Handoff

- Verify every technical reference exists or is marked TBD.
- Separate blocked decisions from implementation-ready decisions.
- Ask the user to approve the design before creating tracker items or coding.
- Recommend `create-test-strategy` for detailed validation planning before `create-prd-work-items` creates story/ticket validation fields.
