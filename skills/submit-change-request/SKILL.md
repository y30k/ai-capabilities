---
name: submit-change-request
description: |
  Submit production-ready changes by committing the exact staged candidate, pushing a branch, creating or updating a pull request or merge request, and monitoring connected CI/CD; also support read-only CI monitoring and PR/MR title or body drafting. Use after check-production-readiness for an initial change request or fast track, or after validated review remediation or conflict resolution for an existing PR/MR update, when the user asks to commit, push, open or update a PR/MR, submit changes for review, draft a PR/MR, or watch CI/CD. Default to a PR/MR; push directly to the default branch only when the user explicitly requests fast track, bypass or skip PR/MR, or direct-to-main or default behavior.
---

# Submit Change Request

Use this skill to move a production-ready staged candidate into remote review and make connected automation explicit before PR review, release, or handoff.

Default to creating or updating a PR/MR. Use direct-to-default fast track only as an explicit exception.

## Boundary

This skill may stage focused existing-PR updates, commit, push, create or update PRs/MRs, request reviewers, set labels, and watch CI/CD only with user authorization. Do not merge PRs/MRs, deploy, approve production gates, cancel/retry expensive jobs, force-push, rewrite public history, or click manual approvals unless explicitly authorized.

Never infer fast track from generic phrases such as "push it", "submit it", "ship it", or "looks good". If the user has not explicitly requested bypassing PR/MR review or pushing directly to the default branch, use the PR/MR path or ask when the target remains ambiguous.

For `new-change-request`, require a current **READY** or **CONDITIONALLY READY** verdict from `check-production-readiness` for the exact staged candidate. Fast track requires **READY**; every gate that would otherwise remain pending must already have a named waiver reflected in that verdict. For `update-existing-change-request`, use the focused validation from review remediation or conflict resolution. If the update materially expands scope or risk, stop treating it as remediation and route it back to the appropriate implementation skill as a new candidate.

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
3. For **ci-monitor-only**: do not stage, commit, push, or create/update a PR/MR. Identify the existing PR/MR, branch, or commit, discover connected CI/CD, watch automation, report, and stop.
4. For **draft-only**: do not stage, commit, push, or create/update a PR/MR. Inspect context read-only as needed, draft the PR/MR title/body or command plan, report, and stop.
5. For `new-change-request` and `fast-track-direct-default`, require all intended changes to be already staged, recompute the source commit and staged tree ID, and compare both with readiness evidence; do not stage new candidate hunks here. For `update-existing-change-request`, inspect and stage only the focused, validated remediation or conflict-resolution changes.
6. Verify local validation for mutating submission modes. For an existing PR/MR update, run the focused checks required by review remediation or conflict resolution. If the update materially expands scope or risk, stop and route it back to the appropriate implementation skill as a new candidate.
7. Present the commit/submission plan and wait for approval unless the user has explicitly authorized this exact workflow in the current run.
8. Commit only intended changes using the repository's message conventions and issue references. For a new change request or fast track, verify the resulting commit tree equals the reviewed staged tree ID.
9. For normal PR/MR modes: push safely to the correct remote branch and create/update the PR/MR. For an existing PR/MR update, record the pre-update provider head, verify the pushed commit becomes the provider-reported updated head, and bind required CI/CD evidence to that exact head before progression.
10. For **fast-track-direct-default**: fetch the remote, verify the reviewed source commit was already aligned with the exact default branch and direct-push policy, confirm the exact commit to push, push without force, then watch default-branch CI/CD. If alignment requires merge, rebase, or branch updates, stop and rerun readiness on the resulting candidate.
11. For modes with automation monitoring (`new-change-request`, `update-existing-change-request`, `ci-monitor-only`, `fast-track-direct-default`), watch automation until it reaches a terminal state or an agreed timeout. Triage failures as product/test, flaky, infrastructure, missing-secret/access, manual-approval, or unknown.
12. Report the PR/MR URL or direct-push target, commits or N/A, validation or N/A, CI/CD status or N/A, blockers, and next recommended skill.

## Gates

- **Readiness gate**: `new-change-request` requires READY or CONDITIONALLY READY for the exact source commit and staged tree ID; `fast-track-direct-default` requires READY with every otherwise pending gate explicitly waived. Existing PR/MR updates require all affected focused gates, exact updated-head verification, and required automation on that head; material scope or risk expansion becomes a new candidate.
- **Submission gate**: for mutating submission modes, intended diff is understood, required readiness or focused validation evidence is current, commit exists, and either a PR/MR is created or updated or an explicitly requested fast-track commit is pushed to the default branch. For `ci-monitor-only` and `draft-only`, this gate is not applicable because those modes must not mutate repository or remote state.
- **Fast-track gate**: direct-to-default push is allowed only when explicit fast-track intent is present, the default branch is unambiguous, repository policy permits direct pushes, the commit tree matches the READY candidate, no unrelated changes are included, force-push is not needed, and every otherwise pending gate has an explicit named waiver.
- **Automation gate**: every required PR/MR or default-branch check for the exact submitted/updated head is passing or explicitly waived. A failed, blocked, timed-out, or unknown required check must be triaged with evidence and owner action, but does not pass the gate.

A failing or blocked automation gate does not mean the PR/MR must be deleted. It blocks progression to review or release until the next explicit action succeeds or receives an authorized waiver: fix and resubmit, retry with evidence, request credentials/manual approval, or hand off to an owner.

## Handoffs

- Use `review-pull-request` after the PR/MR exists and required automation is passing or explicitly waived.
- Use `address-pr-review-comments` after reviewers leave actionable threads.
- Use `resolve-merge-conflicts` when the branch cannot cleanly merge, rebase, or fast-forward to the default branch.
- Return to `develop-feature`, `implement-prd-stories`, or `fix-github-issue` when CI exposes code or test defects.
- Use `check-production-readiness` before a new change request or fast track when readiness evidence is absent or stale.
- Use `observe-release` after a fast-track direct push triggers a deployment or rollout.

## Documentation Output

Write durable submission drafts and reports under `docs/submit-change-request/` or a user-specified path under `docs/`. Never store generated documentation in agent-state directories such as `.agents/`, `.pi/`, `.codex/`, or `.claude/`.
