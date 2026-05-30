---
name: develop-feature
description: |
  Develop software features from an approved idea, existing plan/spec, or app brief
  through implementation, validation, and optional PR preparation. Use when the user
  asks to build, implement, execute a plan, turn an idea into a PR, or create an
  application with iterative validation. Not for creating PRDs or requirements; use
  create-interactive-prd. Not for implementing approved PRDs; use implement-prd-stories.
---

# Develop Feature

Use this coding skill for feature work from an approved idea, plan, spec, or app brief through validated implementation. For approved PRDs that need durable story tracking, use `create-technical-design`, `create-test-strategy`, and `create-prd-work-items` before `implement-prd-stories`.

## Boundary

This skill may create lightweight implementation plans, but those plans are a gate before coding. If the agent creates or materially changes a plan, present it to the user and wait for approval before editing source code.

## Path Selection

Read `references/workflow.md`, then choose the smallest useful path:

- **idea-to-PR**: idea → lightweight implementation plan → approval gate → implementation → validation → PR.
- **plan-to-PR**: existing approved plan/spec → implementation → validation → PR.
- **PRD-to-tracked-delivery**: approved PRD → `create-technical-design` → `create-test-strategy` → `create-prd-work-items` → `manage-delivery-board` → `implement-prd-stories`.
- **implement-only**: user explicitly asks to implement an already-understood plan without PR ceremony.
- **guided PIV**: user wants human-in-the-loop plan, implementation, validation, feedback.
- **adversarial build**: new app or large feature benefits from builder/reviewer repair loops.

## Core Rule

Do not skip gates or validation. At minimum run relevant tests or explain why they cannot run.

## Documentation Output

When writing plans, reports, PRDs, briefs, findings, story tracking, scratch notes, or other generated documentation, write them under the repository-root `docs/` directory, preferably `docs/develop-feature/...` or the specific `docs/` path named in the workflow. Do not use `.agents/`, `.pi/`, `.codex/`, `.claude/`, or other agent-specific directories for generated documentation.
