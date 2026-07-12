---
name: address-pr-review-comments
description: |
  Address existing GitHub pull request review feedback end-to-end: build a worklist from unresolved threads only, recheck thread state before acting, triage each concern, implement in-scope fixes, validate, stage, commit, post evidence-rich replies, push the PR branch, resolve fully addressed threads, and report anything still unresolved. Treat a direct request to address PR comments as authorization for this default non-force workflow without approval pauses unless the user or repository policy explicitly requires a checkpoint. Use when the user asks to handle reviewer comments, respond to PR review threads, fix requested changes from a review, resolve addressed feedback, or remediate an existing changes-requested review. Use review-pull-request for a first-pass review and submit-change-request for branch updates not driven by existing review feedback.
---

# Address PR Review Comments

## Boundary

Treat a direct request to address, handle, fix, or resolve PR review comments as authorization for the complete default workflow: scoped edits, validation, index-safe staging, commit, traceable replies, a normal non-force push to the existing PR head branch, resolution of fully addressed threads, and verification. Build and record one action plan listing the still-unresolved thread IDs, intended files, commit, replies, push target, and resolution-eligible threads, but proceed without waiting for another approval.

Pause only when the user explicitly requests read-only, draft-reply, local-only, or approval-checkpoint behavior; repository or organization policy requires approval; or the next action is destructive or exceptional. Always ask before force-pushes, branch rewrites, production changes, dismissing reviews, bypassing protections, materially expanding scope, or declining, deferring, or disputing feedback that needs an owner decision. If such a checkpoint applies, stop before the gated action while preserving validated local work.

Never address a thread whose current `isResolved` state is true. Exclude resolved threads before triage, and recheck state before implementation, reply, and resolution so concurrent reviewer actions become no-op skips rather than duplicate work.

Do not use this skill for first-pass PR review; use `review-pull-request`. Do not use it for merge conflicts; use `resolve-merge-conflicts`.

## Procedure

Read and follow `references/workflow.md`. Unless an explicit approval checkpoint applies, the direct request supplies authorization. Preserve the mutation sequence: commit locally, reply on each still-unresolved original thread, push code fixes, resolve each fully addressed thread, then verify resolution.

- Treat focused validation plus passing or explicitly waived updated required CI/CD as the readiness confirmation for review remediation; do not invoke a separate final production-readiness phase.
- In every reply, state the disposition, original concern, what changed or was answered, why that addresses the concern, affected file or symbol when applicable, relevant local commit short SHA or why none applies, and exact validation evidence.
- Resolve fix threads only after validation, reply, successful push, and proof that each reply-cited SHA is on the PR branch; if reconciliation rewrites a SHA, post a corrective reply naming the pushed replacement first. Resolve answer-only, verified-stale, or duplicate threads only after the explanatory reply is complete. Leave deferred, blocked, disputed, partial, failed-validation, failed-reply, and failed-push threads unresolved.
- Do not claim a push or resolution succeeded before verifying it.

## Documentation Output

Write durable plans, findings, and response reports under `docs/address-pr-review-comments/` or a user-specified path under `docs/`. Never store generated documentation in agent-state directories such as `.agents/`, `.pi/`, `.codex/`, or `.claude/`.
