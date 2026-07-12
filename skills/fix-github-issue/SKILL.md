---
name: fix-github-issue
description: |
  Fix or assess GitHub issues with standard, smoke-first, full-review, investigation-only, planning-only, and validation-only modes. Use when the user supplies a GitHub issue URL, owner/repository#number reference, or repository-context issue number and asks to fix, resolve, implement, reproduce, investigate, plan, or validate it.
---

# Fix GitHub Issue

Use this skill for GitHub issue work. It consolidates standard fixing, smoke-first fixing, and full fix-plus-review into one workflow.

## Mode Selection

Read `references/workflow.md`, then choose:

- **standard**: classify → investigate/plan → implement → validate → authorized index-safe staging → `check-production-readiness` → `submit-change-request` handoff.
- **smoke-first**: reproduce or create a failing check before implementation.
- **full-review**: standard + PR-style review lanes + self-fix + simplification.
- **investigate-only**, **plan-only**, **validate-only** when the user asks for a portion.

Default to **standard**. Use **smoke-first** for bugs, regressions, or unclear reproduction. Use **full-review** when the user asks for comprehensive rigor or the change is risky.

## Planning Gate

Investigation, planning, and validation-only modes must not edit source code. For coding modes, present the fix plan and wait for user approval before implementation unless the user has explicitly pre-authorized end-to-end fixing.

Authorization to fix an issue permits scoped local edits and validation in the verified issue repository, not posting comments, changing issue state, staging, committing, pushing, opening or updating a PR/MR, using production systems, or other destructive or remote actions unless separately requested. Before readiness, obtain authorization for exact, index-safe staging unless the user already asked to stage or prepare the candidate. Draft remote outputs, and hand off to `check-production-readiness` only after the candidate is staged and verified.

## Documentation Output

Write durable findings, plans, and validation notes under `docs/github-issues/{issue}/` or a user-specified path under `docs/`. Never store generated documentation in agent-state directories such as `.agents/`, `.pi/`, `.codex/`, or `.claude/`.
