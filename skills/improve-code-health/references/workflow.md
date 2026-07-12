# Code Health Workflow

## 1. Scope

Clarify target area, allowed behavior changes, validation commands, and risk tolerance.

## 2. Baseline

- Inspect project structure and dependency boundaries.
- Identify tests and commands that prove behavior.
- Capture current failures before changing code.

## 3. Architecture Sweep Path

1. Find complexity hotspots, duplicated patterns, dead code, leaky abstractions, and unclear boundaries.
2. Read representative files before judging.
3. Prioritize changes by user value, risk, and reversibility.
4. Produce a prioritized plan with scope, non-goals, risks, and validation for each phase. Stop without any repository edit—including documentation—unless implementation or a durable report artifact is explicitly authorized.

## 4. Safe Refactor Path

1. Define the behavior, interfaces, and checks the slice must preserve.
2. Choose one small, approved refactor slice.
3. Add characterization coverage first when existing tests do not protect affected behavior.
4. Make mechanical changes before semantic changes; do not mix behavior changes into the slice.
5. Run targeted validation after each slice, then required broader checks and inspect the final diff.
6. Stop and report unexpected failures or scope changes; do not weaken checks to obtain a pass.

## 5. Stage an Implemented Refactor When Authorized

Before a readiness handoff, obtain staging authorization unless the user already requested staging or candidate preparation. Snapshot `git status --short`, working-tree diffs, and cached diffs; present an exact path/hunk allowlist; and stop on overlap or unrelated pre-staged content unless an isolation plan is approved. Stage only intended refactor hunks, inspect both cached and unstaged views, run `git diff --cached --check`, and verify no intended hunk remains unstaged or unrelated hunk was absorbed. Do not commit or push.

## 6. Report

Include changed files, complexity removed, behavior preserved, validation results, and follow-up opportunities. Before initial PR/MR submission, hand off to `check-production-readiness` only when the implemented refactor is staged and verified; otherwise return the exact staging plan. Use `submit-change-request` only after readiness.
