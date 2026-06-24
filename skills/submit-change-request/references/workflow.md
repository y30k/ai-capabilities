# Change Request Submission Workflow

## Table of Contents

1. [Confirm Scope and Authorization](#1-confirm-scope-and-authorization)
2. [Select Mode](#2-select-mode)
3. [Discover Repository and Provider Conventions](#3-discover-repository-and-provider-conventions)
4. [Audit Candidate Hygiene](#4-audit-candidate-hygiene)
5. [Verify Pre-submit Validation](#5-verify-pre-submit-validation)
6. [Commit Safely](#6-commit-safely)
7. [Normal PR/MR Submission](#7-normal-prmr-submission)
8. [Fast-track Direct-to-Default Submission](#8-fast-track-direct-to-default-submission)
9. [Discover Connected CI/CD](#9-discover-connected-cicd)
10. [Monitor and Triage Automation](#10-monitor-and-triage-automation)
11. [Report](#11-report)

## 1. Confirm Scope and Authorization

Collect:

- requested mode: new change request, existing PR/MR update, CI-monitor-only, draft-only, or explicit fast track
- repository, remote, default/base branch, head branch, and target provider
- related issue, story, PRD, design, release, incident, or review-remediation context
- whether the PR/MR should be draft/WIP or ready for review
- requested reviewers, labels, assignees, milestone, project fields, and notification expectations
- maximum CI/CD watch time and whether safe retries are authorized

Ask before mutating repository or remote state unless the user explicitly requested the exact commit/push/create/watch workflow.

## 2. Select Mode

Default to PR/MR submission. Choose direct-to-default fast track only when the user explicitly asks for it in git context.

Fast-track trigger phrases include:

- "fast track" or "fast-track this"
- "bypass PR", "skip PR", "skip pull request", "skip MR", or "no merge request"
- "push directly to main/default/master/trunk"
- "commit straight to main/default/master/trunk"
- "land directly on the default branch"

Do **not** treat generic phrases like "push it", "ship it", "submit it", "looks good", or "get it out" as fast-track authorization by themselves. If the intent could mean either "open/update a PR" or "push to default", ask.

## 3. Discover Repository and Provider Conventions

Use local repo files and available tools to determine:

- default/base branch and remote URL/provider
- branch naming, commit message, signing, DCO, changelog, generated-file, and PR/MR template conventions
- required pre-submit commands from docs, package scripts, task runners, Makefiles, CI configs, and contribution guides
- PR/MR creation tool: `gh`, `glab`, provider API/MCP, web URL, or repo-specific CLI
- required review rules, branch protections, CODEOWNERS, approval requirements, labels, projects, and linked issue keywords
- whether direct pushes to the default branch are allowed, protected, or organization-forbidden

If provider, default branch, or base branch is unclear, stop and ask rather than creating or fast-tracking against the wrong target.

## 4. Audit Candidate Hygiene

Inspect:

- `git status --short`
- unstaged and staged diffs
- current branch and upstream
- commits ahead/behind base or remote branch
- untracked/generated artifacts
- secrets, debug logs, temporary flags, commented-out code, local-only paths, and unrelated edits

Stage only intended files. If unrelated changes exist, leave them unstaged or ask whether to split them. If the branch is behind base and integration is required, fetch and use the repo's preferred merge/rebase strategy; route conflicts to `resolve-merge-conflicts`.

For fast track, be stricter: no unrelated changes, no unknown generated artifacts, and no ambiguous commit set may be pushed to the default branch.

## 5. Verify Pre-submit Validation

Run the smallest repo-appropriate local gate set before submission when possible:

- tests, lint, typecheck, format/check, build, package, docs, migrations, generated artifacts, snapshots, accessibility, security, or performance commands that apply to the changed scope
- targeted reproduction or smoke checks for bug fixes
- UI screenshots/recordings or visual/a11y evidence when relevant

If validation cannot run because of missing services, secrets, hardware, time, or credentials, disclose the blocked gate in the PR/MR body. Use draft/WIP if the missing gate is material.

For fast track, do not rely on "CI will catch it" for known local failures. Either fix first, get an explicit named waiver for the skipped/failed gate, or refuse fast track and use the PR/MR path.

## 6. Commit Safely

Prefer one logical commit unless the repository expects a different structure. Use the repo's message convention and include issue/story references when appropriate.

Before committing:

1. Show the files to be committed and validation summary.
2. Confirm commit message and target branch when ambiguity remains.
3. Run `git diff --cached` or equivalent inspection for the staged candidate.

Do not amend or squash existing public commits, rewrite branch history, or commit unrelated files without explicit authorization.

## 7. Normal PR/MR Submission

Push to the intended remote branch and set upstream when needed. If the branch already exists remotely:

- fetch first when remote state may have changed
- avoid overwriting collaborators' work
- use normal push by default
- use `--force-with-lease` only after explicit authorization and a clear reason

If push fails because of non-fast-forward, permission, branch protection, hooks, LFS, signing, or secret scanning, report the exact blocker and recommended next action.

Create or update the PR/MR using the repository's template when present. Include:

```markdown
## Summary
- {what changed}

## Linked Work
- Closes/Fixes/Refs {issue/story/PRD/design}

## Validation
- [x] `{command}` — {result}
- [ ] {blocked command/signoff} — {why blocked, owner}

## Risk and Rollback
- Risk: {low/medium/high and why}
- Rollback: {revert, flag disable, config rollback, migration rollback, package rollback, or N/A}

## Notes for Reviewers
- {areas to inspect, screenshots, logs, CI links, known follow-ups}
```

Attach screenshots, recordings, benchmark output, or log excerpts when they materially help review. Mark as draft/WIP when local validation is incomplete, scope is intentionally partial, or the user requests draft mode.

## 8. Fast-track Direct-to-Default Submission

Use this path only after explicit fast-track authorization. It bypasses PR/MR review and pushes directly to the default branch.

Required checks before direct push:

- explicit fast-track wording is present in the current user request or confirmed by the user
- the default branch is known from repo/provider data, not guessed
- direct default-branch push is allowed by repo/org policy and does not require bypassing protections
- local checkout is up to date with the remote default branch, preferably via fetch plus fast-forward update
- intended commit set is exact and reviewable locally
- validation passed, or each skipped/failed gate has an explicit named waiver
- no force-push, history rewrite, protected-environment approval, or production deployment approval is needed

Preferred safe flow:

1. Fetch remote state: `git fetch --prune <remote>`.
2. Identify default branch from provider metadata or remote HEAD, e.g. `origin/main`.
3. Prefer applying and committing the final diff on an up-to-date local default branch (`git pull --ff-only`).
4. If changes were developed on a feature branch, do not blindly push `HEAD:<default>`. First prove the outgoing commit set is exactly intended; cherry-pick or recreate the commit on the updated default branch when safer.
5. Rerun relevant validation after the final commit exists on the updated default branch, when practical.
6. Present a final fast-track confirmation containing remote, default branch, commit SHA(s), changed files, validation, push command, rollback plan, and CI/CD to watch.
7. Push without force to the default branch.
8. Monitor default-branch automation for the pushed commit.

If direct push is rejected by branch protection, hooks, permissions, or secret scanning, do not try to bypass it. Report the blocker and ask whether to fall back to the PR/MR path.

## 9. Discover Connected CI/CD

Treat the provider's required checks, branch protection, merge widget, or default-branch status checks as the primary source of truth, then enrich from repo configuration and external status links.

Look for:

- GitHub Actions: `.github/workflows/`, check suites, required status checks, environments
- GitLab CI: `.gitlab-ci.yml`, child pipelines, merge request pipelines, branch pipelines, environments
- Jenkins: `Jenkinsfile`, multibranch jobs, commit statuses, PR comments, Blue Ocean/job URLs
- Buildkite: `.buildkite/`, commit statuses, annotations
- CircleCI: `.circleci/config.yml`, PR checks, branch workflows
- Azure Pipelines: `azure-pipelines.yml`, branch policies, checks
- Drone/Woodpecker/TeamCity/Travis/other systems through status contexts, comments, badges, or repo docs
- security, code scanning, dependency, coverage, preview deploy, visual regression, and manual approval checks

If a system is mentioned in repo docs but not visible from available credentials, report it as an external/unknown gate rather than assuming it passed.

## 10. Monitor and Triage Automation

Poll with reasonable backoff until all required checks reach a terminal state, the user-specified watch window expires, or an action is required.

Use these statuses:

- **PASSING** — all required checks passed; optional checks are passing or non-blocking.
- **FAILED** — at least one required check failed.
- **BLOCKED** — missing secrets, permissions, runners, manual approvals, external systems, or ambiguous required gates prevent completion.
- **PENDING/TIMEOUT** — checks are still running after the agreed watch window.
- **UNKNOWN** — CI source of truth cannot be queried.

Failure triage:

- **Product/test failure**: inspect logs, reproduce locally if practical, then route back to the implementation skill to fix and resubmit.
- **Formatting/lint/type failure**: fix within scope when authorized, run local check, commit/push update, and monitor again.
- **Generated artifact or snapshot drift**: regenerate only if repo policy and review context support it; otherwise investigate stale expectations.
- **Flaky failure**: retry only when repo policy or user approval allows it; capture evidence and avoid repeated blind reruns.
- **Infrastructure/quota/runner failure**: report owner, failing system, log URL, and retry/escalation recommendation.
- **Missing secret/access/manual approval**: identify the needed credential, environment, owner, and whether the PR/MR or default-branch update must wait.
- **Security/code scanning failure**: do not bypass; inspect finding and route to fix or owner decision.

Do not click deploy approvals, protected-environment approvals, or production promotions unless explicitly authorized.

## 11. Report

```markdown
## Change Request Submission Report

**Mode**: new-change-request | update-existing-change-request | ci-monitor-only | draft-only | fast-track-direct-default
**PR/MR**: {url, N/A for fast track, or not created}
**Direct push target**: {remote/default branch or N/A}
**Base → Head**: {base} ← {branch or commit}
**Commit(s)**: {sha(s)}
**Local validation**: {commands and results or blocked/waived gates}
**Automation state**: PASSING | FAILED | BLOCKED | PENDING/TIMEOUT | UNKNOWN

### CI/CD Checks
| Check | System | Status | Evidence/URL | Required? | Notes |
| --- | --- | --- | --- | --- | --- |

### Blockers or Follow-ups
- {blocker, owner/action, next skill}

### Next Step
Use `{skill}` because {reason}.
```
