---
name: address-pr-review-comments
description: |
  Address existing GitHub pull request review feedback end-to-end: build a worklist from unresolved threads only, recheck thread state before acting, triage each concern, implement approved fixes, validate and commit changes, post evidence-rich replies explaining what was addressed and why, push the PR branch, resolve fully addressed threads, and report anything still unresolved. Use when the user asks to handle reviewer comments, respond to PR review threads, fix requested changes from a review, resolve addressed feedback, or remediate an existing changes-requested review. Use review-pull-request for a first-pass review and submit-change-request for branch updates not driven by existing review feedback.
---

# Address PR Review Comments

## Boundary

Treat a request to address review comments as authorization for scoped local edits and validation. Commit, post thread replies, push, and resolve addressed threads only when the user also requests or approves those actions. Before the first commit or remote mutation, present one action plan listing the still-unresolved thread IDs, commit, replies, push target, and threads eligible for resolution; obtain any missing authorization once. Include resolution in the default plan, and after approval do not ask again for each eligible thread. Without approval, stop after validated local edits and return draft replies plus a `submit-change-request` handoff. Always ask before destructive changes, force-pushes, branch rewrites, production changes, or dismissing reviews.

Never address a thread whose current `isResolved` state is true. Exclude resolved threads before triage, and recheck state before implementation, reply, and resolution so concurrent reviewer actions become no-op skips rather than duplicate work.

Do not use this skill for first-pass PR review; use `review-pull-request`. Do not use it for merge conflicts; use `resolve-merge-conflicts`.

## Procedure

Read and follow `references/workflow.md`. After authorization is confirmed, preserve its mutation sequence: commit locally, reply on each still-unresolved original thread, push code fixes, resolve each fully addressed thread, then verify resolution.

- Treat focused validation plus passing or explicitly waived updated required CI/CD as the readiness confirmation for review remediation; do not invoke a separate final production-readiness phase.
- In every reply, state the disposition, original concern, what changed or was answered, why that addresses the concern, affected file or symbol when applicable, relevant local commit short SHA or why none applies, and exact validation evidence.
- Resolve fix threads only after validation, reply, successful push, and proof that each reply-cited SHA is on the PR branch; if reconciliation rewrites a SHA, post a corrective reply naming the pushed replacement first. Resolve answer-only, verified-stale, or duplicate threads only after the explanatory reply is complete. Leave deferred, blocked, disputed, partial, failed-validation, failed-reply, and failed-push threads unresolved.
- Do not claim a push or resolution succeeded before verifying it.

## Documentation Output

Write durable plans, findings, and response reports under `docs/address-pr-review-comments/` or a user-specified path under `docs/`. Never store generated documentation in agent-state directories such as `.agents/`, `.pi/`, `.codex/`, or `.claude/`.
