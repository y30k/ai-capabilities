---
name: observe-release
description: |
  Verify post-release or post-deployment health, rollout safety, SLOs, logs, metrics, dashboards, feature flags, incidents, rollback criteria, user feedback, and follow-up work. Use after a release, deploy, feature-flag rollout, migration, or production change; when the user asks to monitor a release, validate production behavior, decide whether to continue/rollback, or turn production learnings into issues/PRDs. Do not make destructive production changes without explicit authorization.
---

# Observe Release

Use this skill after release execution to close the loop between shipped software, production signals, and the backlog.

## Boundary

This skill reads release artifacts, deployment state, observability signals, dashboards, logs, metrics, alerts, feedback, and trackers. Do not rollback, change feature flags, alter infrastructure, or create tracker items unless the user explicitly authorizes that action.

If the release has not been prepared or cut, use `release` first. If the candidate has not passed readiness, use `check-production-readiness` first.

## Runbook

1. Read `references/workflow.md`.
2. Confirm the release/tag/deploy, production or staging environment, rollout window, owner, and rollback authority.
3. Discover the expected success metrics, SLOs, dashboards, alerts, logs, feature flags, and user/operator checks.
4. Compare current signals against pre-release baselines, budgets, or agreed expectations.
5. Decide whether the rollout is healthy, watch-only, blocked, or rollback/escalation recommended.
6. Capture incidents, regressions, missing telemetry, user feedback, and follow-up work.
7. Create or update tracker items only after approval, preserving links to release artifacts and evidence.

## Handoff

- Use `manage-github-issues` for follow-up bugs or triage.
- Use `create-interactive-prd` for significant product learnings that need requirements.
- Use `improve-code-health` for maintainability issues discovered during rollout.
- Use `release` for hotfixes or rollback releases.

## Documentation Output

When writing plans, reports, PRDs, briefs, findings, story tracking, scratch notes, or other generated documentation, write them under the repository-root `docs/` directory, preferably `docs/release-observations/...` or the specific `docs/` path named in the workflow. Do not use `.agents/`, `.pi/`, `.codex/`, `.claude/`, or other agent-specific directories for generated documentation.
