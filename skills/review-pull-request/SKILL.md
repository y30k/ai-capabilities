---
name: review-pull-request
description: |
  Review pull requests and merge requests for correctness, edge cases, tests, maintainability, compatibility, security, performance, and delivery risk; validate claimed behavior; synthesize evidence-backed findings; recommend merge posture when requested; and publish review feedback when authorized and tooling permits. Use for first-pass, comprehensive, maintainer, validation-focused, or merge-readiness review of a PR/MR. Treat a direct request to review an identified PR/MR as authorization to publish one review unless the user requests read-only or draft output. For remediation of existing GitHub review threads, use address-pr-review-comments instead.
---

# Review Pull Request

## Select Review Depth and Actions

Read `references/workflow.md`. Select one review depth: **smart** (default), **comprehensive**, **maintainer**, or **validation**. Separately select output and mutation behavior: return or draft findings, publish authorized feedback, or implement explicitly requested high-confidence findings from this review run.

## Review Output Default

Treat a direct request to review an identified PR/MR as authorization to publish one review when credentials and tooling allow, unless the user requests read-only, draft, or validation-only output. Prefer one top-level review comment with clear reasoning, impact, and requested changes; add inline comments only when provider tooling supports them and line mapping is reliable. Never publish duplicate or partial review content. If direct commenting fails, is unavailable, or would create noise, return the same review content in the agent response and state why it was not posted.

Use a normal comment review by default. Use formal approve/request-changes only when the user explicitly authorizes that formal decision; repository convention may inform the recommendation but never substitutes for authorization.

## Handoff

When changes are still local and no PR/MR exists, use `check-production-readiness` and then `submit-change-request` before review. Use `submit-change-request` directly when an existing PR/MR only needs CI/CD monitoring.

Use `address-pr-review-comments` after reviewers request changes or leave threaded feedback that should be answered on GitHub before pushing a fix commit.

## Documentation Output

Write durable review notes under `docs/review-pull-request/` or a user-specified path under `docs/`. Never store generated documentation in agent-state directories such as `.agents/`, `.pi/`, `.codex/`, or `.claude/`.
