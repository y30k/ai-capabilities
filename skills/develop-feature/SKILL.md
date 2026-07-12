---
name: develop-feature
description: |
  Implement software features from an idea, approved plan or specification, or app brief through plan-gated coding, validation, and optional PR/MR handoff. Use when the user asks to build a feature or application, implement or execute a plan, turn an idea into validated code, or work through iterative plan-implement-validate cycles. After implementation validation, use check-production-readiness before submit-change-request handles commit, push, PR/MR, or CI/CD operations. Not for creating requirements or PRDs; use create-interactive-prd. Not for delivering approved PRD stories from a tracked queue; use implement-prd-stories.
---

# Develop Feature

Use this coding skill for feature work from an approved idea, plan, spec, or app brief through validated implementation. For approved PRDs that need durable story tracking, use `create-technical-design`, `create-test-strategy`, and `create-prd-work-items` before `implement-prd-stories`.

## Boundary

This skill may create lightweight implementation plans, but those plans are a gate before coding. If the agent creates or materially changes a plan, present it to the user and wait for approval before editing source code.

Treat implementation authorization as permission for scoped local, non-destructive edits and validation only. Staging is a separate Git-index mutation: before a readiness handoff, obtain authorization for an exact, index-safe staging plan unless the user already asked to stage or prepare the submission candidate. Ask before destructive changes, cross-repository work, credentials or production services, weakening checks, or commit/push/PR/MR operations; hand remote submission work to `submit-change-request`.

## Path Selection

Read `references/workflow.md`, then choose the smallest useful path:

- **idea-to-PR**: idea → lightweight implementation plan → approval gate → implementation → validation → authorized index-safe staging → `check-production-readiness` → `submit-change-request`.
- **plan-to-PR**: existing approved plan/spec → implementation → validation → authorized index-safe staging → `check-production-readiness` → `submit-change-request`.
- **PRD-to-tracked-delivery**: approved PRD → `create-technical-design` → `create-test-strategy` → `create-prd-work-items` → `manage-delivery-board` → `implement-prd-stories`.
- **implement-only**: user explicitly asks to implement an already-understood plan without PR ceremony.
- **guided PIV**: user wants human-in-the-loop plan, implementation, validation, feedback.
- **adversarial build**: new app or large feature benefits from builder/reviewer repair loops.

## Core Rule

Do not skip approval gates. Before reporting completion, verify each acceptance criterion, run the most relevant targeted tests plus required broader checks, and inspect the final diff. If a check cannot run, record the command, reason, and remaining uncertainty.

## Documentation Output

Write durable plans and validation notes under `docs/develop-feature/` or a user-specified path under `docs/`. Never store generated documentation in agent-state directories such as `.agents/`, `.pi/`, `.codex/`, or `.claude/`.
