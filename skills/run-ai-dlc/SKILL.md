---
name: run-ai-dlc
description: |
  Orchestrate an AI Development Life Cycle across repository skills: agent/workspace readiness, discovery, PRD creation, technical design, work-item decomposition, test strategy, dependency-aware implementation, review, PR review-comment remediation, production readiness, release, observation, and feedback. Use when the user asks for the order of skills, an end-to-end AI-DLC plan, lifecycle governance, stage gates, delivery workflow selection, or a review of where a task belongs in the AI-assisted development process.
---

# Run AI-DLC

Use this meta-skill to choose the right specialized skill and gate for each phase of AI-assisted software delivery.

## Boundary

This skill routes and governs work. It does not replace the detailed phase skills. Do not edit source code directly under this skill; hand off to the appropriate implementation, review, readiness, release, or operations skill.

## Runbook

1. Read `references/lifecycle.md`.
2. Identify the user's current lifecycle phase, artifacts, blockers, and desired outcome.
3. Check required gates before moving forward: approval, design readiness, tracker relationships, validation plan, unblocked work, review, review-comment remediation, readiness, release, and observation.
4. Recommend the next skill and the exact artifact/input it should consume.
5. If the user asks for an end-to-end plan, produce the ordered skill sequence with entry/exit criteria.
6. If a capability gap remains, use `skill-creator` or `create-agent-workflow` to create a durable skill/workflow rather than improvising repeatedly.

## Core Gates

- Do not code before requirements/design/work item approval unless the user explicitly requests a small direct fix.
- Do not create implementation tickets from unapproved or ambiguous requirements except in draft mode.
- Do not implement blocked work; use tracker relationships to find ready work.
- Do not merge or release without review, review-comment remediation when requested changes exist, and readiness gates appropriate to the change.
- Do not treat release as done until production/staging observation and follow-up capture are complete.

## Documentation Output

When writing plans, reports, PRDs, briefs, findings, story tracking, scratch notes, or other generated documentation, write them under the repository-root `docs/` directory, preferably `docs/ai-dlc/...` or the specific `docs/` path named in the workflow. Do not use `.agents/`, `.pi/`, `.codex/`, `.claude/`, or other agent-specific directories for generated documentation.
