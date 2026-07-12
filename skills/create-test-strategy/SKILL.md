---
name: create-test-strategy
description: |
  Create acceptance, regression, integration, performance, accessibility, security, and release validation strategies from PRDs, technical designs, or work items. Use when the user asks for a test plan, QA strategy, validation matrix, acceptance criteria, coverage-gap analysis, story-level validation, nonfunctional test planning, or release-gate design. Planning only: inspect source and tests for evidence, write the strategy artifact, and do not add or modify tests or implementation files.
---

# Create Test Strategy

Use this skill to turn requirements and technical designs into a concrete validation plan that can guide story creation, implementation, review, and production readiness.

## Boundary

Treat this as a planning-only skill. Read source and test files to understand current coverage and commands, but do not add or modify tests, fixtures, configuration, or implementation. Route implementation to `implement-prd-stories`. Write durable plans under `docs/test-strategies/` unless the user provides another documentation path.

## Runbook

1. Read `references/workflow.md`.
2. Confirm the PRD/spec/design/work-item input and the target release or feature scope.
3. Discover existing test commands, CI gates, fixtures, environments, and quality bars from repo files.
4. Map each requirement/story/risk to observable acceptance criteria and the smallest reliable validation.
5. Include nonfunctional checks when relevant: performance, security, privacy, accessibility, reliability, migration/rollback, compatibility, and observability.
6. Identify missing test harnesses, data, environments, baselines, secrets, or manual signoffs.
7. Record proposed tracker items for non-trivial validation work; create them only in a subsequent `create-prd-work-items` run.
8. Present the validation matrix and ask for approval before treating it as a gate.

## Handoff

- Use the matrix while creating work items so each story has validation.
- Use `implement-prd-stories` to add or update tests as part of each unblocked story.
- Use `check-production-readiness` to verify the agreed gates before initial submission; use `review-pull-request` after the PR/MR exists.

## Documentation Output

Write supporting findings and review notes under `docs/test-strategies/` or another user-specified path under `docs/`. Never store generated documentation in agent-state directories such as `.agents/`, `.pi/`, `.codex/`, or `.claude/`.
