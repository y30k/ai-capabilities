---
name: create-technical-design
description: |
  Create implementation-ready technical designs, architecture plans, ADRs, interface contracts, rollout/observability plans, and risk reviews from approved PRDs or feature specs. Use after PRD approval and before creating work items or coding; when the user asks for a technical design, architecture spec, design doc, ADR, feasibility refinement, API/data model design, migration plan, implementation plan, or technical handoff. Planning only; no source-code edits unless the user explicitly asks to update documentation.
---

# Create Technical Design

Use this skill to bridge approved product requirements to implementation-ready technical plans that can be decomposed into work items.

## Boundary

This is a planning and documentation skill. Read code, configs, schemas, tests, and deployment docs to verify claims, but do not edit source code or implement features. Write durable design artifacts under `docs/technical-designs/` unless the user provides another path.

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

When writing plans, reports, PRDs, briefs, findings, story tracking, scratch notes, or other generated documentation, write them under the repository-root `docs/` directory, preferably `docs/technical-designs/...` or the specific `docs/` path named in the workflow. Do not use `.agents/`, `.pi/`, `.codex/`, `.claude/`, or other agent-specific directories for generated documentation.
