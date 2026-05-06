---
name: fix-github-issue
description: |
  Fix GitHub issues end-to-end with selectable modes: standard fix, smoke-first reproduction, full review/self-fix, investigation-only, planning-only, or validation-only. Use when the user asks to fix, resolve, implement, investigate, plan, or validate a GitHub issue or issue number.
---

# Fix GitHub Issue

Use this skill for GitHub issue work. It consolidates standard fixing, smoke-first fixing, and full fix-plus-review into one workflow.

## Mode Selection

Read `references/workflow.md`, then choose:

- **standard**: classify → investigate/plan → implement → validate → report/PR.
- **smoke-first**: reproduce or create a failing check before implementation.
- **full-review**: standard + PR-style review lanes + self-fix + simplification.
- **investigate-only**, **plan-only**, **validate-only** when the user asks for a portion.

Default to **standard**. Use **smoke-first** for bugs, regressions, or unclear reproduction. Use **full-review** when the user asks for comprehensive rigor or the change is risky.

## Planning Gate

Investigation, planning, and validation-only modes must not edit source code. For coding modes, present the fix plan and wait for user approval before implementation unless the user has explicitly pre-authorized end-to-end fixing.
