# Change Request Submission Workflow

## Table of Contents

1. [Confirm Scope and Authorization](#1-confirm-scope-and-authorization)
2. [Select Mode](#2-select-mode)
3. [Discover Repository and Provider Conventions](#3-discover-repository-and-provider-conventions)
4. [Audit Candidate Hygiene](#4-audit-candidate-hygiene)
5. [Verify Readiness or Focused Update Validation](#5-verify-readiness-or-focused-update-validation)
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
- current production-readiness verdict and exact candidate identity for a new change request or fast track
- for an existing PR/MR update, provider head repository/ref and pre-update head OID
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

Mode routing:

| Mode | Mutates repository or remote? | Commit/push/create behavior |
| --- | --- | --- |
| `new-change-request` | Yes | Commit the already-staged reviewed candidate, push branch, create PR/MR, and monitor CI/CD. |
| `update-existing-change-request` | Yes | May stage/commit focused validated changes, push existing branch, update PR/MR, and monitor CI/CD. |
| `fast-track-direct-default` | Yes | Commit the already-staged READY candidate and push directly to default only after explicit fast-track gates pass. |
| `ci-monitor-only` | No | Skip staging, commits, pushes, and PR/MR creation/update; only inspect existing PR/MR/branch/commit status and monitor CI/CD. |
| `draft-only` | No | Skip staging, commits, pushes, and PR/MR creation/update; only prepare title/body or command plan. |

After selecting `ci-monitor-only`, skip all commit and submission sections and use only CI/CD discovery, monitoring, and reporting. After selecting `draft-only`, skip every mutation and CI-monitoring step, but use the repository template and section 7 body structure to produce the requested draft and report.

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

For `ci-monitor-only`, do not stage or alter files; inspect only enough to identify the PR/MR, branch, commit, and relevant automation.

For `draft-only`, inspect diffs and context read-only when useful for drafting; do not stage, commit, push, or create/update the PR/MR.

For `new-change-request` and `fast-track-direct-default`, do not stage new candidate content. Require every intended hunk to be already staged, recompute `git rev-parse HEAD` and `git write-tree`, and compare both values with the readiness handoff. If the source commit or tree ID differs, stop and return to `check-production-readiness`.

For `update-existing-change-request`, stage only the focused, validated review-remediation or conflict-resolution files. If scope or risk materially expands, stop treating the update as remediation and route it to the appropriate implementation skill as a new candidate.

If a new-change-request or fast-track branch needs merge/rebase integration that would change the reviewed candidate, stop and perform that work before rerunning readiness. For an existing PR/MR update, use the repository's preferred integration strategy, route conflicts to `resolve-merge-conflicts`, and retain focused validation evidence. For fast track, also require READY, no unrelated changes or unknown generated artifacts, and an unambiguous commit set.

## 5. Verify Readiness or Focused Update Validation

For `new-change-request`:

- require READY or CONDITIONALLY READY from `check-production-readiness`
- verify the source commit and staged tree ID match the readiness handoff
- copy named feature-branch-push and PR/MR-created automation into the submission and monitoring plan
- permit draft/WIP only when the user requested it and the candidate is READY or CONDITIONALLY READY; actual readiness blockers return to phase 7

For `fast-track-direct-default`:

- require READY for the exact source commit and staged tree ID; explicitly waive every gate that would otherwise remain pending
- do not rely on post-push CI to catch a known local failure
- refuse fast track when readiness is stale, failed, or ambiguous

For `update-existing-change-request`, identify and run every affected test, lint, typecheck, build, reproduction, visual, integration, or security gate required by the review remediation or conflict resolution; do not choose only the cheapest check. Record the pre-update provider head OID and require the update commit, required automation, and final evidence to bind to the provider-reported updated head. If scope or risk materially expands, stop and route the work back to the appropriate implementation skill as a new candidate.

For `ci-monitor-only`, local validation is out of scope unless the user requests it. For `draft-only`, include known evidence but do not mutate repository state. Mark production readiness and candidate identity `NOT RUN / N/A`, add an unchecked `check-production-readiness` prerequisite, and state that the draft does not authorize or satisfy submission.

## 6. Commit Safely

Use this section only for mutating submission modes: `new-change-request`, `update-existing-change-request`, and `fast-track-direct-default`. Skip it entirely for `ci-monitor-only` and `draft-only`.

Prefer one logical commit unless the repository expects a different structure. Use the repo's message convention and include issue/story references when appropriate.

Before committing:

1. Show the files to be committed and validation summary.
2. Confirm commit message and target branch when ambiguity remains.
3. Run `git diff --cached` or equivalent inspection for the staged candidate.
4. For a new change request or fast track, recompute and compare the candidate identity:

```bash
source_commit="$(git rev-parse HEAD)"
candidate_tree="$(git write-tree)"
# Compare both values with the production-readiness handoff before committing.
```

After committing a new change request or fast track, verify the commit tree is unchanged from the reviewed candidate:

```bash
test "$(git rev-parse 'HEAD^{tree}')" = "$candidate_tree"
```

Do not amend or squash existing public commits, rewrite branch history, or commit unrelated files without explicit authorization.

## 7. Normal PR/MR Submission

Perform the push, create, and update steps in this section only for `new-change-request` and `update-existing-change-request`. In `draft-only`, skip all mutations but use the repository template and body structure below to produce the requested title, body, or command plan.

Push to the intended remote branch and set upstream when needed. If the branch already exists remotely:

- fetch first when remote state may have changed
- avoid overwriting collaborators' work
- use normal push by default
- use `--force-with-lease` only after explicit authorization and a clear reason

If push fails because of non-fast-forward, permission, branch protection, hooks, LFS, signing, or secret scanning, report the exact blocker and recommended next action.

For `update-existing-change-request`, push explicitly to the provider-reported PR/MR head repository/ref rather than trusting a stale upstream. Refetch provider metadata after push and require the expected update commit to equal the updated head. If a concurrent commit changes the provider head, fetch/check out that exact head, rerun every affected remediation or integration gate on it, refetch provider metadata, and require the head OID to remain unchanged before proceeding. Record that exact validated OID as the automation commit and do not accept statuses from the pre-update head or an ancestor-only validation.

Create or update the PR/MR using the repository's template when present. Include:

```markdown
## Summary
- {what changed}

## Linked Work
- Closes/Fixes/Refs {issue/story/PRD/design}

## Production Readiness and Validation
- Verdict: READY | CONDITIONALLY READY | focused existing-PR update | NOT RUN (draft-only)
- Candidate: {source commit + staged tree ID, pre-update → verified updated provider head OID for focused update, or N/A for draft-only}
- [x] `{command}` — {result}
- [ ] `check-production-readiness` — {required before submission when draft-only}
- [ ] `{normal-submission-created check}` — {trigger, why pending, monitoring owner}

## Risk and Rollback
- Risk: {low/medium/high and why}
- Rollback: {revert, flag disable, config rollback, migration rollback, package rollback, or N/A}

## Notes for Reviewers
- {areas to inspect, screenshots, logs, CI links, known follow-ups}
```

Attach screenshots, recordings, benchmark output, or log excerpts when they materially help review. An actual `new-change-request` may be marked draft/WIP only when the user requests it and the candidate already satisfies the READY or CONDITIONALLY READY entry gate; incomplete validation or intentionally partial scope returns to production readiness instead. A `draft-only` document must say it is preparatory and cannot be submitted until readiness runs.

## 8. Fast-track Direct-to-Default Submission

Use this path only after explicit fast-track authorization. It bypasses PR/MR review and pushes directly to the default branch.

Required checks before direct push:

- explicit fast-track wording is present in the current user request or confirmed by the user
- the default branch is known from repo/provider data, not guessed
- direct default-branch push is allowed by repo/org policy and does not require bypassing protections
- the reviewed source commit equals the fetched remote default-branch tip; no merge, rebase, pull, cherry-pick, or branch update is needed
- intended commit tree exactly matches the READY candidate
- production readiness returned READY, with every otherwise pending gate explicitly waived
- no force-push, history rewrite, protected-environment approval, or production deployment approval is needed

Preferred safe flow:

1. Fetch remote state: `git fetch --prune <remote>`.
2. Identify the default branch from provider metadata or remote HEAD, e.g. `origin/main`.
3. Verify the source commit recorded by readiness equals the fetched remote default-branch tip. If not, stop; integrate first and rerun readiness on the resulting candidate.
4. Verify the committed tree equals the staged tree ID recorded by readiness.
5. Present a final fast-track confirmation containing remote, default branch, commit SHA, changed files, validation, waivers, push command, rollback plan, and CI/CD to watch.
6. Push that commit without force to the default branch.
7. Monitor default-branch automation for the pushed commit.

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

Poll with reasonable backoff until all required checks for the exact submitted or updated head OID reach a terminal state, the user-specified watch window expires, or an action is required. Reject stale check results attached only to a pre-update commit.

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
**Production readiness**: READY | CONDITIONALLY READY | focused existing-PR update | N/A
**Candidate identity**: {source commit + staged tree ID, or pre-update → verified updated provider head OID for focused update}
**Local validation**: {commands and results or blocked/waived gates}
**Automation state**: PASSING | FAILED | BLOCKED | PENDING/TIMEOUT | UNKNOWN | N/A

### CI/CD Checks
| Check | System | Head OID | Status | Evidence/URL | Required? | Notes |
| --- | --- | --- | --- | --- | --- |

### Blockers or Follow-ups
- {blocker, owner/action, next skill}

### Next Step
Use `{skill}` because {reason}.
```
