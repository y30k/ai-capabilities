---
name: review-pull-request
description: |
  Review pull requests/merge requests with adaptive, comprehensive, maintainer-decision, validation, and optional safe-fix paths. Use when the user asks to review a PR/MR, validate a PR/MR, check a pull request, synthesize review findings, decide whether a PR is ready to merge, or leave review feedback. By default, when a PR/MR target and credentials are available, publish clear review comments on the PR/MR itself with reasoning, impact, and requested changes; fall back to returning the review in the agent response when direct commenting is unavailable. If the user asks to address existing reviewer comments, reply on PR threads, commit, and push fixes, use address-pr-review-comments instead.
---

# Review Pull Request

Use this skill for PR/MR review and validation. It consolidates smart, comprehensive, maintainer, validation-focused, review-comment publishing, and safe fix workflows.

## Mode Selection

Read `references/workflow.md`, then choose:

- **smart**: adaptive review; only run lanes warranted by risk.
- **comprehensive**: run all review lanes and synthesize findings.
- **maintainer**: review against project direction and make approve/request-changes/comment recommendation.
- **validation**: compare main/base vs feature behavior, including tests or reproduction.
- **publish-review-comments**: default output behavior; post clear findings to the PR/MR itself when possible, otherwise return them in the agent response.
- **fix-review-findings**: implement safe fixes from this review run if requested; use `address-pr-review-comments` when existing GitHub reviewer threads need replies, commits, and push updates.

## Review Output Default

Default to publishing review feedback on the PR/MR itself when a PR/MR is identified and credentials/tooling allow it. Prefer a top-level review comment with clear reasoning, impact, and requested changes; add inline comments only when provider tooling supports them and the line mapping is reliable. If direct commenting fails, is unavailable, or would create noisy duplicates, return the same review content in the agent response and say why it was not posted.

Use a normal comment review by default. Use formal approve/request-changes only when the user asks for a maintainer decision or the repository workflow clearly expects that action.

## Handoff

Use `submit-change-request` first when changes are still local, no PR/MR exists, or PR-connected CI/CD needs to be created or monitored before review.

Use `address-pr-review-comments` after reviewers request changes or leave threaded feedback that should be answered on GitHub before pushing a fix commit.

## Documentation Output

When writing plans, reports, PRDs, briefs, findings, story tracking, scratch notes, or other generated documentation, write them under the repository-root `docs/` directory, preferably `docs/review-pull-request/...` or the specific `docs/` path named in the workflow. Do not use `.agents/`, `.pi/`, `.codex/`, `.claude/`, or other agent-specific directories for generated documentation.
