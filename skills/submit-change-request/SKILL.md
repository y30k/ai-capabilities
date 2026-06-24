---
name: submit-change-request
description: |
  Commit validated changes, push a branch, create or update a pull request/merge request, and monitor connected CI/CD until checks pass, fail, or block. Use after implementation, review remediation, merge-conflict resolution, or any branch update when the user asks to commit, push, open a PR/MR, create a pull request, submit changes for review, or watch CI/CD across GitHub Actions, GitLab CI, Jenkins, Buildkite, CircleCI, Azure Pipelines, or similar systems. By default create or update a PR/MR; use the non-default direct-to-default fast-track path only when the user explicitly says fast track, bypass/skip PR, push directly to main/default, commit straight to main, or an equivalent git-context phrase.
---

# Submit Change Request

Use this skill to move validated local changes from a working tree into a remote review/submission state and to make connected automation explicit before review, readiness, release, or handoff.

Default to creating or updating a PR/MR. Use direct-to-default fast track only as an explicit exception.

## Boundary

This skill may stage files, commit, push, create or update PRs/MRs, request reviewers, set labels, and watch CI/CD only with user authorization. Do not merge PRs/MRs, deploy, approve production gates, cancel/retry expensive jobs, force-push, rewrite public history, or click manual approvals unless explicitly authorized.

Never infer fast track from generic phrases like "push it", "submit it", "ship it", or "looks good" unless the surrounding git context clearly means bypassing PR/MR review. If fast-track intent is ambiguous, ask whether the user means direct push to the default branch.

Do not use this skill to implement the feature itself; use `develop-feature`, `implement-prd-stories`, or `fix-github-issue`. Do not use it for PR review content; use `review-pull-request`. Use `address-pr-review-comments` when reviewer threads need replies and code changes.

## Modes

Read `references/workflow.md`, then choose the smallest safe mode:

- **new-change-request**: commit intended local changes, push a branch, create a PR/MR, then watch connected CI/CD. This is the default.
- **update-existing-change-request**: commit and push additional changes to an existing PR/MR, then watch checks.
- **ci-monitor-only**: monitor checks for an existing PR/MR or pushed branch without changing code.
- **draft-only**: prepare a PR/MR title/body or command plan without committing, pushing, or creating anything.
- **fast-track-direct-default**: non-default emergency/trivial path; commit intended changes and push directly to the repository default branch without creating a PR/MR. Use only when the user explicitly requests fast track, bypass/skip PR/MR, direct-to-main/default, or an equivalent git-context phrase.

## Runbook

1. Identify the repository, remote provider, default/base branch, head branch, related issue/story/PRD, and whether a PR/MR already exists.
2. Select the mode. Default to PR/MR submission unless explicit fast-track wording is present.
3. Inspect local git state and intended diff. Separate unrelated edits, detect secrets/debug residue, and confirm all intended changes are staged or ready to stage.
4. Verify local validation. Run missing pre-submit checks when practical, or record why the PR/MR must be draft/WIP or why fast track is blocked.
5. Present the commit/submission plan and wait for approval unless the user has explicitly authorized this exact workflow in the current run.
6. Commit only intended changes using the repository's message conventions and issue references.
7. For normal PR/MR modes: push safely to the correct remote branch, create or update the PR/MR, then discover and watch PR/MR-connected CI/CD.
8. For **fast-track-direct-default**: fetch the remote, verify the exact default branch and direct-push policy, update the local default branch safely, confirm the exact commit(s) to push, push to the default branch without force, then watch default-branch CI/CD for the pushed commit.
9. Watch automation until it reaches a terminal state or an agreed timeout. Triage failures as product/test, flaky, infrastructure, missing-secret/access, manual-approval, or unknown.
10. Report the PR/MR URL or direct-push target, commits, validation, CI/CD status, blockers, and next recommended skill.

## Gates

- **Submission gate**: intended diff is understood, local validation is passing or explicitly disclosed, commit exists, and either a PR/MR is created/updated or an explicitly requested fast-track commit is pushed to the default branch.
- **Fast-track gate**: direct-to-default push is allowed only when explicit fast-track intent is present, the default branch is unambiguous, repository policy permits direct pushes, the pushed commit set is exactly intended, no unrelated changes are included, force-push is not needed, and validation is passing or explicitly waived with named risk.
- **Automation gate**: every required PR/MR or default-branch check is passing, explicitly waived, or named as failed/blocked with evidence and owner action.

A failing or blocked automation gate does not automatically mean the submission should be abandoned. It means the next action must be explicit: fix and resubmit, retry with evidence, request credentials/manual approval, or hand off to an owner.

## Handoffs

- Use `review-pull-request` after the PR/MR exists and required automation is passing or triaged.
- Use `address-pr-review-comments` after reviewers leave actionable threads.
- Use `resolve-merge-conflicts` when the branch cannot cleanly merge, rebase, or fast-forward to the default branch.
- Return to `develop-feature`, `implement-prd-stories`, or `fix-github-issue` when CI exposes code or test defects.
- Use `check-production-readiness` for staged release candidates after review/submission gates are satisfied, or after fast-track direct push when the change is production-bound.
- Use `observe-release` after a fast-track direct push triggers a deployment or rollout.

## Documentation Output

When writing plans, reports, PRDs, briefs, findings, story tracking, scratch notes, or other generated documentation, write them under the repository-root `docs/` directory, preferably `docs/submit-change-request/...` or the specific `docs/` path named in the workflow. Do not use `.agents/`, `.pi/`, `.codex/`, `.claude/`, or other agent-specific directories for generated documentation.
