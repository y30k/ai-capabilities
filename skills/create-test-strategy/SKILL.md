---
name: create-test-strategy
description: |
  Create acceptance, regression, integration, performance, accessibility, security, and release validation strategies from PRDs, technical designs, or work items. Use when the user asks for a test plan, QA strategy, validation matrix, acceptance criteria, coverage gaps, story-level validation, nonfunctional test planning, or release gate design before or during implementation. Planning skill; do not edit source code unless explicitly asked to add tests.
---

# Create Test Strategy

Use this skill to turn requirements and technical designs into a concrete validation plan that can guide story creation, implementation, review, and production readiness.

## Boundary

This is primarily a planning skill. Read source and test files to understand current coverage and commands, but do not add or modify tests unless the user explicitly asks for implementation. Write durable plans under `docs/test-strategies/` unless the user provides another path.

## Runbook

1. Read `references/workflow.md`.
2. Confirm the PRD/spec/design/work-item input and the target release or feature scope.
3. Discover existing test commands, CI gates, fixtures, environments, and quality bars from repo files.
4. Map each requirement/story/risk to observable acceptance criteria and the smallest reliable validation.
5. Include nonfunctional checks when relevant: performance, security, privacy, accessibility, reliability, migration/rollback, compatibility, and observability.
6. Identify missing test harnesses, data, environments, baselines, secrets, or manual signoffs.
7. Recommend new or updated tracker items via `create-prd-work-items` when validation work is non-trivial.
8. Present the validation matrix and ask for approval before treating it as a gate.

## Handoff

- Use the matrix while creating work items so each story has validation.
- Use `implement-prd-stories` to add or update tests as part of each unblocked story.
- Use `review-pull-request` and `check-production-readiness` to verify the agreed gates before merge/release.

## Documentation Output

When writing plans, reports, PRDs, briefs, findings, story tracking, scratch notes, or other generated documentation, write them under the repository-root `docs/` directory, preferably `docs/test-strategies/...` or the specific `docs/` path named in the workflow. Do not use `.agents/`, `.pi/`, `.codex/`, `.claude/`, or other agent-specific directories for generated documentation.
