# AI Development Life Cycle Skill Map

## Phase Order

| Phase | Purpose | Primary Skill | Exit Gate |
| --- | --- | --- | --- |
| 0. Agent/workspace readiness | Verify tools, repo safety, and agent behavior | `agent-smoke-test` | Tooling and guardrails understood |
| 1. Discovery and PRD | Define problem, users, evidence, scope, and success | `create-interactive-prd` | Validated PRD approved by user |
| 2. Technical design | Convert approved requirements into architecture and contracts | `create-technical-design` | Design approved; open questions isolated |
| 3. Test strategy | Map requirements and risks to validation gates | `create-test-strategy` | Validation matrix/gates approved |
| 4. Work-item decomposition | Create deduped, dependency-linked tracker items with validation | `create-prd-work-items` | Items exist or draft is approved; relationships verified |
| 5. Delivery board readiness | Identify unblocked, implementation-ready work | `manage-delivery-board` | Next-ready queue has no unresolved blockers |
| 6. Implementation | Code one approved, unblocked slice at a time; for tracked PRD stories, stay in the current repo, stage validated changes, mark Done, and refresh dependent Ready states across repositories | `implement-prd-stories`, `develop-feature`, or `fix-github-issue` | Slice passes validation; tracked story changes are staged, Done is verified, and cross-repository dependency readiness is refreshed |
| 7. Production readiness | Run a fail-closed review of the exact staged change before external submission | `check-production-readiness` | READY, or CONDITIONALLY READY with only named normal-submission-created automation pending |
| 8. Change request submission | Commit, push, create/update PR/MR, or explicitly fast-track to default, and watch connected CI/CD | `submit-change-request` | PR/MR exists, or explicit fast-track direct-to-default push is complete; required automation passed or is explicitly waived |
| 9. PR review | Review risk, behavior, tests, and maintainability; post clear PR/MR feedback when possible | `review-pull-request` | Findings posted or documented and dispositioned |
| 10. PR review remediation | Process only unresolved threads; address approved feedback; reply with what changed and why plus commit/evidence; resolve fully addressed threads | `address-pr-review-comments`, `submit-change-request` | Fixes are validated and bound to the verified updated PR/MR head; addressed threads are resolved; required automation for that exact head passed or is explicitly waived |
| 11. Integration hygiene | Resolve branch/rebase/merge conflicts, rerun all affected validation, and refresh existing-PR automation | `resolve-merge-conflicts`, `submit-change-request` | Resolution is bound to the verified updated PR/MR head; required automation for that exact head passed or is explicitly waived |
| 12. Release | Perform version, changelog, tag, publish, and release mechanics with release-specific integrity checks | `release` | Release artifact/deploy complete |
| 13. Observe rollout | Verify production/staging health and capture learnings | `observe-release` | Healthy/watch/block/rollback decision recorded |
| 14. Feedback and maintenance | Feed issues, tech debt, and product learnings back into backlog | `maintainer-standup`, `manage-github-issues`, `improve-code-health` | Follow-up items triaged |

## Support Skills

- `create-agent-workflow` — create reusable process when a recurring gap is not skill-specific.
- `skill-creator` — create or update a durable skill for repeated specialized work.
- `review-pull-request` optional fix action — implement safe findings from the current review run when thread replies are not required.
- `design-polished-web-ui` — specialty implementation and validation skill for polished responsive web UI.
- `remotion-generate` — specialty implementation skill for Remotion video projects.

## Common Routing

### New feature idea

`create-interactive-prd` → `create-technical-design` → `create-test-strategy` → `create-prd-work-items` → `manage-delivery-board` → `implement-prd-stories` → `check-production-readiness` → `submit-change-request` → `review-pull-request` → `address-pr-review-comments` if reviewers request changes → `submit-change-request` to monitor updated CI when needed → `resolve-merge-conflicts` if needed → `submit-change-request` to refresh integration CI when needed → `release` → `observe-release`.

### Existing issue or bug

`fix-github-issue` in smoke-first mode when reproduction is unclear → `check-production-readiness` → `submit-change-request` → `review-pull-request` → `address-pr-review-comments` if reviewers request changes → `submit-change-request` to monitor updated CI when needed → `release`/`observe-release` when shipping.

### Small approved change

`develop-feature` or `fix-github-issue` → validation → `check-production-readiness` → `submit-change-request` → `review-pull-request` → `address-pr-review-comments` if reviewers request changes.

### Backlog and project maintenance

- Use `maintainer-standup` for a broad, read-only repository health briefing.
- Use `manage-delivery-board` for project-board dependencies, blocked or unblocked analysis, and next-ready sequencing.
- Use `manage-github-issues` for individual issue creation or repository issue-backlog triage.
- Use `create-prd-work-items` only to decompose an approved PRD into implementation work.

### Refactor or technical debt

`improve-code-health` → `create-test-strategy` if validation is weak → `develop-feature` or `implement-prd-stories` for approved changes → `check-production-readiness` → `submit-change-request` → review and remediation.

### Polished web UI

`design-polished-web-ui` for scoped UI implementation or polish → `check-production-readiness` → `submit-change-request` → `review-pull-request` → release when production-bound.

## Gate Checklist

Before moving phases, verify:

- **PRD gate**: problem, users, success, non-goals, and technical claims are documented and approved.
- **Design gate**: contracts, data, migration, rollout, rollback, observability, security/privacy, and risks are addressed.
- **Test strategy gate**: requirements and risks map to acceptance criteria, commands, data, environments, and nonfunctional checks.
- **Tracker gate**: work items are deduped, owned by repo/system, small enough, linked with relationships, and include validation.
- **Readiness gate**: next item has no unresolved blocker relationships and has acceptance criteria plus validation.
- **Implementation gate**: each slice validates before moving on; a tracked PRD story also has all story-owned changes staged, a verified Done transition, and a verified cross-repository sweep that moves every newly unblocked dependent to Ready.
- **Production gate**: the exact staged candidate has no unresolved P0/P1/P2 issue; mandatory pre-submission build/test/security/performance gates pass; any feature-branch-push or PR/MR-created automation is named for `submit-change-request`.
- **Change request gate**: a current READY/CONDITIONALLY READY verdict covers the initial source commit and staged tree, with READY required for fast track; the resulting commit tree matches, is pushed, and has a PR/MR unless explicit fast-track direct-to-default was requested and completed; required CI/CD checks are passing or explicitly waived. Failed, blocked, timed-out, or unknown required checks are triaged but block progression.
- **Review gate**: findings are documented and dispositioned by owner.
- **Review remediation gate**: only unresolved threads enter the worklist; addressed threads have traceable replies and verified resolution; all affected validation passes on the provider-verified exact updated PR/MR head; and required automation for that same head passes or is explicitly waived.
- **Integration gate**: conflicts are resolved, all affected validation is rerun, the resolution is bound to the verified updated PR/MR head, and required automation for that exact head passes or is explicitly waived.
- **Observation gate**: release health and follow-up work are recorded.

## Gap Handling

If none of the existing skills match the needed phase, do not bury new process in ad hoc chat. Use:

1. `create-agent-workflow` for a reusable but non-skill-specific runbook.
2. `skill-creator` for a new specialized skill with triggers, workflow, gates, and references.
