---
name: address-pr-review-comments
description: |
  Address pull request review comments end-to-end: fetch unresolved GitHub PR review threads and comments, triage each reviewer concern, implement approved fixes on the PR branch, validate changes, reply on the original review threads with dispositions before pushing, commit, push, and summarize remaining follow-up. Use when the user asks to handle PR review comments, respond to reviewer threads, fix requested changes, resolve review feedback, or update a PR after code review.
---

# Address PR Review Comments

Use this coding/review-response skill when a PR already has reviewer comments and the user wants the agent to address them, reply on the threads, and push an update.

## Boundary

This skill may edit source code, commit, push, and post GitHub comments only with user authorization. If the user asks only to analyze review feedback, stop after the triage plan. If the user asks to address comments, treat that as authorization to implement fixes, but still ask before destructive changes, force-pushes, branch rewrites, production changes, or dismissing/marking threads resolved.

Do not use this skill for first-pass PR review; use `review-pull-request`. Do not use it for merge conflicts; use `resolve-merge-conflicts`.

## Runbook

1. Read `references/workflow.md`.
2. Identify the PR, repository, base branch, head branch, review state, checks, and current local git state.
3. Fetch unresolved review threads, top-level PR comments, review summaries, and requested-changes reviews using GitHub CLI/API or available GitHub tools.
4. Build a thread-by-thread triage table: actionable fix, question/clarification, duplicate, already fixed/stale, out of scope, or needs owner decision.
5. Present the plan and wait for approval unless the user already explicitly requested implementation of the exact PR feedback.
6. Check out the PR branch and implement only high-confidence, in-scope fixes tied to the review comments.
7. Run targeted validation and any relevant required checks; stop if validation fails or feedback changes scope.
8. Reply on each original review thread before pushing the commit, with concise disposition and validation evidence. Use a top-level PR comment only for non-thread feedback or a final summary.
9. Commit only the intended changes, push to the PR branch, then report pushed commit, validation, thread replies, and remaining unresolved items.

## Required Reply Discipline

- Reply to the original review thread whenever the feedback came from a thread.
- Mention whether the issue was fixed locally, answered without code change, deferred with reason, or blocked.
- Include validation evidence when available.
- Do not claim a fix was pushed before the push succeeds; say it is addressed locally and being pushed in the next commit.
- Do not mark threads resolved unless the user explicitly authorizes it and the fix/answer is complete.

## Documentation Output

When writing plans, reports, PRDs, briefs, findings, story tracking, scratch notes, or other generated documentation, write them under the repository-root `docs/` directory, preferably `docs/address-pr-review-comments/...` or the specific `docs/` path named in the workflow. Do not use `.agents/`, `.pi/`, `.codex/`, `.claude/`, or other agent-specific directories for generated documentation.
