# Release Observation Workflow

## 1. Confirm Observation Scope

Collect:

- release version/tag/commit/PR/deployment ID
- environment, region, tenant, feature flag, or rollout cohort
- rollout window and current phase
- release owner, on-call, escalation path, and rollback authority
- expected success metrics from PRD, release notes, or readiness report

If rollback authority is unclear, report recommendations only and ask before acting.

## 2. Discover Evidence Sources

Use repo docs and available tools to find:

- deployment status, CI/CD runs, release notes, changelog, and commit diff
- dashboards, metrics, traces, logs, alerts, error tracking, uptime checks, and SLOs
- feature flag state, migration/backfill status, queue/backlog depth, job health, and cron status
- support tickets, issue reports, user feedback, analytics, and business metrics
- manual smoke checks or runbooks required by release docs

Name any missing credentials, dashboards, URLs, or systems that block observation.

## 3. Assess Health

Compare current signals to baseline or expected behavior:

- availability, latency, error rate, throughput, saturation, memory/CPU, cost, queue depth
- user workflow success, conversion, activation, or task completion signals
- security/auth anomalies, permission failures, data integrity, migration correctness
- logs/alerts/noise that suggest latent failure
- support/user reports and qualitative feedback

Use `UNKNOWN` rather than guessing when a signal is unavailable.

## 4. Decide Rollout State

Use these states:

- **HEALTHY** — required signals are available and within expected bounds.
- **WATCH** — no blocker yet, but signals are incomplete, noisy, or trending poorly.
- **BLOCKED** — rollout should not advance because a required signal is missing or failing.
- **ROLLBACK/ESCALATE RECOMMENDED** — evidence indicates user, data, security, availability, or cost risk.

Do not execute rollback/flag changes unless explicitly authorized.

## 5. Capture Follow-up Work

For each finding, decide whether to:

- create/triage a bug with `manage-github-issues`
- create product-learning PRD work with `create-interactive-prd`
- create technical debt/refactor work with `improve-code-health`
- update release/readiness gates if a missed signal should become mandatory
- open an incident/postmortem when impact warrants it

Prefer tracker-native relationships to connect follow-ups to the release, incident, PRD, or blocking issue.

## 6. Report

```markdown
## Release Observation Report

**Release**: {version/tag/deploy}
**Environment**: {env/cohort}
**Window**: {time}
**State**: HEALTHY | WATCH | BLOCKED | ROLLBACK/ESCALATE RECOMMENDED

### Signals Checked
| Signal | Source | Baseline/Expected | Current | Verdict |
| --- | --- | --- | --- | --- |

### User/Operator Feedback
- {feedback or none found}

### Blockers or Risks
- {issue, evidence, recommended action}

### Follow-up Work
| Item | Type | Relationship | Status |
| --- | --- | --- | --- |

### Recommendation
{continue rollout, pause, watch, rollback/escalate, or create follow-ups}
```
