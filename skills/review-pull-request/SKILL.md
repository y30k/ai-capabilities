---
name: review-pull-request
description: |
  Review pull requests with multiple paths: smart/adaptive review, comprehensive review, maintainer decision review, validation on main versus feature branch, and optional safe fix implementation. Use when the user asks to review a PR, validate a PR, check a pull request, synthesize review findings, or decide whether a PR is ready to merge. If the user asks to address existing reviewer comments, reply on PR threads, commit, and push fixes, use address-pr-review-comments instead.
---

# Review Pull Request

Use this skill for PR review and validation. It consolidates smart, comprehensive, maintainer, and validation-focused PR workflows.

## Mode Selection

Read `references/workflow.md`, then choose:

- **smart**: adaptive review; only run lanes warranted by risk.
- **comprehensive**: run all review lanes and synthesize findings.
- **maintainer**: review against project direction and make approve/request-changes/comment recommendation.
- **validation**: compare main/base vs feature behavior, including tests or reproduction.
- **fix-review-findings**: implement safe fixes from this review run if requested; use `address-pr-review-comments` when existing GitHub reviewer threads need replies, commits, and push updates.

## Handoff

Use `address-pr-review-comments` after reviewers request changes or leave threaded feedback that should be answered on GitHub before pushing a fix commit.

## Documentation Output

When writing plans, reports, PRDs, briefs, findings, story tracking, scratch notes, or other generated documentation, write them under the repository-root `docs/` directory, preferably `docs/review-pull-request/...` or the specific `docs/` path named in the workflow. Do not use `.agents/`, `.pi/`, `.codex/`, `.claude/`, or other agent-specific directories for generated documentation.
