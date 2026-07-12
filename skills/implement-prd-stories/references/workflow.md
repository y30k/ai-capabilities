# Implement PRD Stories Workflow

## Table of Contents

1. [Confirm Repository, Source, and Autonomy](#1-confirm-repository-source-and-autonomy)
2. [Discover Status Schema and Relationships](#2-discover-status-schema-and-relationships)
3. [Select Ready Work](#3-select-ready-work)
4. [Verify Readiness](#4-verify-readiness)
5. [Plan Without Unnecessary Pauses](#5-plan-without-unnecessary-pauses)
6. [Progress Story Status](#6-progress-story-status)
7. [Implement and Validate One Story](#7-implement-and-validate-one-story)
8. [Stage and Apply the Completion Status](#8-stage-and-apply-the-completion-status)
9. [Cross-Repository Blocked-Story Readiness Sweep](#9-cross-repository-blocked-story-readiness-sweep)
10. [Continue or Hand Off](#10-continue-or-hand-off)
11. [Report](#11-report)

## 1. Confirm Repository, Source, and Autonomy

Accept these sources, in priority order:

1. A specific GitHub/Jira tracker item with relationship data.
2. A ready queue from `manage-delivery-board`.
3. Approved work items from `create-prd-work-items`.
4. An approved local story list under `docs/`.
5. A PRD fallback only when the user explicitly asks for temporary local planning.

Resolve the current repository root and snapshot its state before selecting work. If no Git root exists, stop because the required local-staging contract cannot be satisfied:

```bash
REPO_ROOT="$(git rev-parse --show-toplevel)"
cd "$REPO_ROOT"
git status --short
git diff --name-only
git diff --cached --name-only
git ls-files --stage
git diff --cached --binary --full-index
git write-tree
```

Treat this root as the only authorized technical mutation boundary by default. If the user explicitly names another repository for technical changes, resolve and snapshot that root too and add only that named root to the authorized set. Do not edit files, run mutating Git commands, create worktrees, or stage changes in any other repository, nested independent repository, submodule, or sibling checkout. Reading tracker data and changing dependency-driven tracker statuses across repository ownership is allowed by this workflow and does not authorize code changes there.

For tracker sources, fetch the current item state before coding. For local stories, read the story table and source PRD/design. Confirm the active story's owning repository maps to the current root; if it does not, stop and ask for explicit cross-repository implementation authorization or a repository change.

If the only input is an approved PRD, ask: "Do you want me to use `create-prd-work-items` to create durable tracker stories first, or draft a local temporary story plan for this session?" Stop until the user chooses.

Treat requests such as "continue implementing the PRD" or "implement the next unblocked ticket" as authorization for scoped implementation in the current repository, local staging, the active story's routine In Progress and tracker-accurate completion transitions, and dependency-driven Ready transitions only after Done is genuinely satisfied. Do not infer authorization to commit, push, submit remotely, or edit another repository.

## 2. Discover Status Schema and Relationships

Before changing tracker/local state, determine:

- status field names, transition IDs, and allowed values
- the exact statuses that represent Blocked, Ready, In Progress, and Done, including semantic equivalents such as To Do/Next or Closed/Completed
- the evidence the tracker requires for Done: validated implementation, submission, merge, owner acceptance, release, or another explicit condition
- any existing intermediate status such as Implemented, Validation Passed, or Ready for Review
- whether an issue-only tracker represents Done by closing the issue with a completed reason and what evidence permits that closure
- relationship types for blocks/blocked-by, parent/child, duplicate, related, dependency, or Jira links
- the active delivery scope and how reverse dependencies are queried across repositories
- whether comments, audit fields, project fields, labels, milestones, or assignees are expected when statuses change

For this skill, local technical implementation means the acceptance criteria pass, required validation passes, and all story-owned changes are staged locally. Tracker truth remains authoritative: move the active story to the discovered Done-equivalent only when that evidence satisfies the tracker's actual Done definition. If Done additionally requires submission, merge, owner acceptance, release, or another later event, move to an existing intermediate Implemented/Validation Passed/Ready for Review equivalent or retain the current truthful non-Done state when no such status exists. Record the unmet Done condition and later owner/action, and do not close the item or treat it as satisfied dependency evidence. If the tracker has no unambiguous Done or Ready mapping, cannot preserve a truthful non-Done state, forbids the accurate transition, or requires an owner-only decision, stop and surface the schema conflict rather than inventing a status or claiming completion.

Do not invent statuses or represent dependency truth only with labels/body prose when tracker-native relationships exist. Refetch every changed item to verify its resulting status.

## 3. Select Ready Work

If the user named a specific item, verify that item first. Otherwise honor the ready queue's explicit priority or order, but select technical work only when its owning repository is the current repository unless cross-repository implementation was explicitly authorized. When priority is absent or tied, use these tie-breakers:

1. Unblocked foundational work that unlocks downstream stories.
2. Risk-reducing or contract/schema/API work before dependent UI/integration work.
3. Small independent stories with clear validation.
4. Work already assigned to this repo/system and current branch context.

Before declaring that no ready work exists during initial selection, refresh the queue and dependency state read-only or use `manage-delivery-board`; section 9 is reserved for propagation after this run verifies an active story as Done. A cross-repository item may be reported Ready without becoming eligible for implementation in the current run.

## 4. Verify Readiness

A story is ready only when:

- it is approved for implementation
- it is not blocked by any open tracker relationship or local dependency
- the owning repository maps to the current repository root, or the user explicitly authorizes technical changes in the other named repository
- acceptance criteria are observable and testable
- validation commands/checks are known or a practical fallback is agreed
- required design/PRD context is linked or available
- external services, secrets, environments, or signoffs needed for the story are available or not required

Do not treat labels/tags or prose mentions as sufficient blocker truth when tracker relationships exist.

If readiness or repository ownership is unclear, use `manage-delivery-board` or ask the user instead of coding. Never treat permission to update a cross-repository story's tracker status as permission to implement that story outside the current repository.

## 5. Plan Without Unnecessary Pauses

For the selected story, read the source PRD/design/work item and relevant code. Keep a focused plan in the conversation or a `docs/implement-prd-stories/...` note when useful:

```markdown
## Implementation Plan

**Story**: {tracker ref or local ID}
**Current repository root**: {absolute root and remote identity}
**Explicitly authorized additional technical roots**: {none or named roots + authorization}
**Tracker scope**: {project/board/epic/dependency graph across repositories}
**Status mapping**: {Blocked / Ready / In Progress / Done equivalents, Done evidence contract, and intermediate or retained non-Done fallback}
**Why ready**: {relationship/dependency evidence}
**Scope**: {one-slice summary}
**Files likely touched**: {paths inside the current root or explicitly authorized additional roots}
**Pre-existing worktree/index state**: {unrelated state to preserve}
**Acceptance criteria**: {criteria}
**Validation**: {commands/manual checks}
**Staging plan**: {story-owned files/hunks only}
**Out of scope**: {all non-authorized repository edits, non-goals, and related blocked work}
```

If the user already authorized this exact story, ready queue, or PRD implementation run, do not pause for another approval unless the plan changes scope or introduces a manual-review trigger. If authorization is missing, ask before source-code edits.

Manual review is required before:

- implementing a blocked or dependent item
- changing requirements, non-goals, acceptance criteria, or story scope
- broad refactors not required by the story
- editing files, Git state, worktrees, submodules, or generated artifacts in another repository not explicitly authorized for technical changes
- weakening, deleting, or bypassing validation to make the story pass
- creating new tracker items or changing contentious ownership/priority without approval
- closing, deleting, reassigning, or resolving unrelated/contentious tracker items beyond the active story's tracker-accurate completion transition
- using credentials, external services, paid resources, production systems, or signoffs not already authorized
- continuing after a failure whose repair would change scope or create product/owner decisions

## 6. Progress Story Status

Status progression is part of the implementation contract, not optional cleanup. Implementation authorization includes routine transitions for the active story and dependency-driven Ready transitions discovered in section 9.

1. Move the selected story from Ready/To Do to In Progress/Doing/Active before source-code edits when the workflow supports it; refetch to verify.
2. Add a short implementation-started note when the tracker convention expects one, including the current repository/branch and intended validation.
3. Do not move the story to Done during intermediate validation. Section 8 owns the tracker-accurate completion transition after validation and staging succeed.
4. On blocked or failed work, set the appropriate Blocked/Failed equivalent only with evidence and an exact next action; do not stage incomplete changes as a completed story or run the unblocking sweep.

For approved local story tables in the current repository, apply equivalent status updates in that file and include them in the story's staged changes. A local status file in another repository remains outside the mutation boundary unless explicitly authorized.

## 7. Implement and Validate One Story

1. Re-read relevant code and tests inside the recorded repository root.
2. Make the smallest change that satisfies the story. Before every file write or generated output, ensure its resolved path remains inside the current root or an explicitly authorized additional root and does not enter any other nested independent repository or submodule.
3. Add or update tests for changed behavior; if automation is infeasible, document why and define a concrete manual check.
4. Run targeted validation first and map results to every acceptance criterion.
5. Run broader required checks when shared contracts, schemas, builds, permissions, performance-sensitive paths, or risky behavior are affected.
6. Inspect the final unstaged and staged diffs against the initial snapshot; separate story-owned hunks from unrelated pre-existing work.
7. For implementation-caused failures, repair only within the authorized story scope and rerun affected checks; otherwise stop for manual review.
8. Classify the technical outcome as `pass`, `blocked`, or `failed` with acceptance and command evidence. Only `pass` proceeds to staging and the tracker-accurate completion transition.

Do not continue to another story after failed validation unless the next story is independent, belongs to the current repository, and the user requested continuous progress. Preserve failed work separately so it cannot contaminate the next story's staged completion evidence.

## 8. Stage and Apply the Completion Status

A story is locally implemented when its acceptance criteria and required validation pass and its intended repository changes are staged. Whether that evidence also makes the tracker item Done depends on the status semantics discovered in section 2. Use this order:

1. In each authorized repository actually touched, inventory the story-owned files and hunks against its pre-implementation snapshot. Exclude unrelated pre-existing changes. If any story path already contains pre-existing staged content, stop and obtain an explicit separation plan before staging; do not attempt to prove preservation by comparing serialized patch bytes after modifying the same index blob.
2. Stage only story-owned files or hunks. Use path-limited staging when a file is story-only; use interactive or patch-based index staging when story and unrelated unstaged hunks share a file.
3. Inspect the staged story diff and run the staged-diff hygiene check in each touched authorized repository:

```bash
git diff --cached --check
git diff --cached --name-only
git diff --cached --stat
```

4. Verify every intended story hunk is staged and no unrelated hunk was newly added to the index. Compare `git ls-files --stage` mode/blob entries for every unrelated pre-existing staged path with the baseline and inspect cached patches for ownership; do not require byte-identical serialized diff text, whose context can change. Record the resulting staged tree ID.
5. Apply the completion transition discovered in section 2:
   - If validated staged implementation satisfies the tracker's Done definition, move the active item to Done. For an issue-only tracker, close it as completed only when the discovered closure contract permits closure on this evidence.
   - If Done requires submission, merge, owner acceptance, release, or another unmet event, move the item to an existing Implemented/Validation Passed/Ready for Review equivalent. If no such status exists, retain its current truthful non-Done state. Record the unmet Done condition and the later owner/action that must finalize Done; do not close the item.
6. Attach the repository, staged-file list, acceptance results, validation evidence, and completion rationale when supported. Refetch the item and verify the exact intended status. If a local story table in the current repository is the tracker, update only that status/evidence hunk, stage it, and repeat the staged-diff checks.
7. Record follow-ups without expanding scope. Preserve dependency relationships; do not delete historical blocker links merely because local implementation passed.

Do not commit or push. If story-owned changes cannot be isolated and staged, or if the accurate status mutation/refetch fails, report `technical-pass/staging-failed` or `technical-pass/status-transition-failed`; do not claim the intended status or run the dependency-unblocking sweep. If an intermediate or retained non-Done status is verified, report `implemented-pending-done`, skip section 9, and hand off through readiness and submission while recording that Done finalization and dependency propagation remain pending. Only a verified tracker-accurate Done state permits section 9.

## 9. Cross-Repository Blocked-Story Readiness Sweep

Run this sweep only after the active story's tracker-accurate Done status is verified; an Implemented, Validation Passed, Ready for Review, submitted, or merely merged state is insufficient unless the discovered Done contract explicitly equates that state with Done. Enumerate blocked stories across the active tracker/delivery scope, not merely the current repository or the completed item's forward links, then identify every item whose readiness may have changed because its blocker set includes the newly Done story. Check reverse `blocks` relationships, `blocked by` links, Jira dependency links, parent/child gates, and blocked items in the active PRD/epic/project. Do not filter candidates by repository; a story owned by another repository must still be evaluated and moved to Ready when eligible.

For each candidate blocked story:

1. Fetch its current status, owning repository/system, complete tracker-native blocker set, and non-dependency readiness gates.
2. Mark a blocker satisfied only when its current tracker state satisfies that item's discovered Done/Closed/Accepted contract or it has an explicit recorded waiver. An intermediate implementation status is not satisfied dependency evidence. The newly completed story is one satisfied blocker, not proof that all blockers are satisfied.
3. Confirm no independent readiness blocker remains: acceptance criteria are actionable, owner repository/system is known, required design/test inputs exist, and required environments, secrets, or signoffs are available or not needed.
4. If every blocker and readiness gate is satisfied, move the story from Blocked to the discovered Ready-equivalent even when its owning repository differs from the current repository.
5. Refetch the story and verify Ready. When supported, add concise evidence naming the completed dependency and the remaining satisfied/waived blocker set. If the active tracker is a local file in an authorized repository, stage only each verified Ready status/evidence hunk and rerun the staged-diff checks.
6. Leave every ineligible story Blocked and report its exact remaining blocker or readiness gap. Do not change its priority, assignee, scope, or repository ownership merely to make it ready.

Cross-repository tracker status mutation is required here; cross-repository file, branch, worktree, index, commit, or source mutation is forbidden without explicit authorization. If the tracker record is a local file stored only in another repository, report that it requires cross-repository file authorization rather than editing it silently.

Do not remove historical dependency relationships unless tracker policy explicitly requires it. If any required Ready transition fails or cannot be verified, preserve the active story's staged changes and verified tracker-accurate Done state, report the exact item, repository, attempted mapping, and permission/schema error, and stop the run. Do not claim the item was unblocked or implement another story until the sweep succeeds or an owner resolves the tracker failure.

## 10. Continue or Hand Off

After the cross-repository blocked-story sweep, continue only when every required Ready transition was verified or no item qualified for transition:

- If the user asked for one story only, stop after the report and name every newly Ready item relevant to the delivery graph.
- If the user asked to continue the feature/PRD queue, select another Ready story without another approval pause only when its technical owner is the current repository. A story moved to Ready in another repository must be reported and skipped until the user explicitly authorizes technical work there or starts a run in that repository.
- If no implementable current-repository work remains, report blocked items, newly Ready cross-repository items, and the smallest next action.
- Treat each technical repository touched as a separate candidate with its own source commit, staged tree ID, complete index, readiness run, and submission handoff. Invoke `check-production-readiness` separately in every touched root. If unrelated pre-existing staged entries remain in a root, preserve them and stop for a separation/inclusion decision rather than misrepresenting that index; do not unstage them silently. Record one verdict per repository and use `submit-change-request` separately after each READY or CONDITIONALLY READY result.
- Use `manage-delivery-board` when relationship or status state is too ambiguous to transition safely.
- Use `create-prd-work-items` when missing dependency work needs durable tracker items.

## 11. Report

```markdown
## PRD Story Implementation Report

**Source**: {tracker/project/PRD/local plan}
**Current repository**: {absolute root and remote identity}
**Story implemented**: {ref/title}
**Technical outcome**: done | implemented-pending-done | blocked | failed | technical-pass/staging-failed | technical-pass/status-transition-failed
**Completion-status verification**: {refetched status, why it is accurate, unmet Done condition/later owner when applicable, or failure}

### Staged Story Changes
| Path/hunk | Story purpose | Staged verification |
| --- | --- | --- |

- Pre-existing index state preserved: {yes/no + explanation}
- Unstaged story-owned hunks remaining: {none or exact list}
- Changes made outside current repository: {none, or explicitly authorized repo and evidence}

### Validation Summary
- `{command}` — {pass/fail/not run and why}

### Active Story Status
| Story | Repository | From | To | Verification |
| --- | --- | --- | --- | --- |

### Cross-Repository Blocked-Story Readiness Sweep
| Story | Owning repository | Previous blockers | Remaining blockers/gates | From → To | Verification/action |
| --- | --- | --- | --- | --- | --- |

### Per-Repository Readiness Handoff
| Repository root | Source commit | Staged tree ID | Candidate files | Readiness verdict/handoff |
| --- | --- | --- | --- | --- |

### Tracker Problems
- {failed status transitions, permission/schema issues, or none}

### Remaining Work or Risks
- {open blockers, follow-ups, newly Ready cross-repository items, next implementable current-repository item}

### Next Step
- {continue in current repo, request cross-repo implementation authorization, use check-production-readiness then submit-change-request, use manage-delivery-board, ask owner, etc.}
```
