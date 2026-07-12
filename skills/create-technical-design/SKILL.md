---
name: create-technical-design
description: |
  Create implementation-ready technical designs, architecture plans, ADRs, interface contracts, rollout and observability plans, and risk reviews from approved PRDs or feature specs. Use after PRD approval and before creating work items or coding; when the user asks for a technical design, architecture spec, design doc, ADR, feasibility refinement, API or data-model design, migration plan, implementation plan, or technical handoff. Planning only: read source, configuration, schemas, and tests for evidence; write or update only the requested design artifact, and never edit implementation files or implement the feature.
---

# Create Technical Design

Use this skill to bridge approved product requirements to implementation-ready technical plans that can be decomposed into work items.

## Boundary

Treat this as a planning and documentation skill. Read code, configuration, schemas, tests, and deployment docs to verify claims, but modify only the requested design artifact; do not edit source, configuration, schema, migration, or test files or implement features. Write durable design artifacts under `docs/technical-designs/` unless the user provides another documentation path.

If the product problem or requirements are not approved, use `create-interactive-prd` first. If the user already has approved tickets and wants coding, use `implement-prd-stories` instead.

## Runbook

1. Read `references/workflow.md`.
2. Confirm the input PRD/spec, approval state, target repositories, and output path.
3. Ground the design in the codebase by reading actual files before making technical claims.
4. Compare viable options and choose the smallest safe design that satisfies the PRD.
5. Document contracts, data changes, migrations, rollout, rollback, observability, security/privacy, and validation implications.
6. Call out dependencies, blocked decisions, spikes, and story seeds for downstream planning.
7. Present the design for approval before work-item creation or implementation.

## Handoff

After approval, recommend:

1. `create-test-strategy` to create a validation matrix and story-level gate plan.
2. `create-prd-work-items` to create dependency-linked GitHub/Jira stories with validation.
3. `implement-prd-stories` only for unblocked, implementation-ready work items.

## Documentation Output

Write supporting findings and review notes under `docs/technical-designs/` or another user-specified path under `docs/`. Never store generated documentation in agent-state directories such as `.agents/`, `.pi/`, `.codex/`, or `.claude/`.
