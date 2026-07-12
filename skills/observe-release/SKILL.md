---
name: observe-release
description: |
  Observe a completed or in-progress release, deployment, feature-flag rollout, migration, or production change by comparing required health signals with baselines and recommending whether to continue, pause, roll back, or escalate. Use when the user asks to monitor rollout health, validate production behavior, inspect SLOs, logs, metrics, alerts, or feedback, or capture evidence-backed follow-up work. Operate read-only by default and require explicit authorization for production or tracker mutations.
---

# Observe Release

Use this skill after release execution to close the loop between shipped software, production signals, and the backlog.

## Boundary

Operate read-only by default and use least-privilege queries. Do not run state-changing smoke checks, acknowledge alerts, rollback, change feature flags or infrastructure, rerun jobs, or create or update tracker items without explicit action-specific authorization. Redact secrets and personal or sensitive data from reports. If a required check can mutate production, mark it blocked and ask before running it.

If the release has not been prepared or cut, use `release` first. If the released source lacks pre-submission production-readiness evidence, record that lifecycle gap and escalate it; do not pretend a retrospective readiness pass can protect an already shipped change.

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

Write durable observation reports under `docs/release-observations/` or a user-specified path under `docs/`. Never store generated documentation in agent-state directories such as `.agents/`, `.pi/`, `.codex/`, or `.claude/`.
