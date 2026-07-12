---
name: run-ai-dlc
description: |
  Orchestrate and govern multi-phase AI-assisted software delivery by selecting repository skills, checking stage gates, and defining lifecycle entry and exit criteria. Use when the user asks for an end-to-end AI-DLC plan, the order or selection of delivery skills, lifecycle governance, stage-gate review, delivery workflow selection, or where work belongs in the development lifecycle. Do not use this meta-skill to execute a single implementation, tracker, review, release, or operations phase.
---

# Run AI-DLC

Use this meta-skill to choose the right specialized skill and gate for each phase of AI-assisted software delivery.

## Boundary

This skill routes and governs work. It does not replace the detailed phase skills. Do not edit source code directly under this skill; hand off to the appropriate implementation, review, readiness, release, or operations skill.

## Runbook

1. Read `references/lifecycle.md`.
2. Identify the user's current lifecycle phase, artifacts, blockers, and desired outcome.
3. Check required gates before moving forward: approval, design readiness, tracker relationships, validation plan, unblocked work, implementation validation and tracked-story staging/tracker-accurate completion/readiness propagation, production readiness, change-request submission, CI/CD automation, review, review-comment remediation, integration, release, and observation.
4. Recommend the next skill and the exact artifact/input it should consume.
5. If the user asks for an end-to-end plan, produce the ordered skill sequence with entry/exit criteria.
6. If a capability gap remains, use `skill-creator` or `create-agent-workflow` to create a durable skill/workflow rather than improvising repeatedly.

## Gate Behavior

Enforce the entry and exit gates in `references/lifecycle.md`. Stop at the first unmet gate, name the missing evidence or approval, and route execution to the owning phase skill. Proceed through an exception only when the user explicitly authorizes it and the lifecycle output records the exception and risk.

## Documentation Output

Write durable lifecycle plans under `docs/ai-dlc/` or a user-specified path under `docs/`. Never store generated documentation in agent-state directories such as `.agents/`, `.pi/`, `.codex/`, or `.claude/`.
