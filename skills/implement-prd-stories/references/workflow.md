# Implement PRD Stories Workflow

## Table of Contents

1. [Confirm Implementation Source and Autonomy](#1-confirm-implementation-source-and-autonomy)
2. [Discover Status Schema and Relationships](#2-discover-status-schema-and-relationships)
3. [Select Ready Work](#3-select-ready-work)
4. [Verify Readiness](#4-verify-readiness)
5. [Plan Without Unnecessary Pauses](#5-plan-without-unnecessary-pauses)
6. [Progress Story Status](#6-progress-story-status)
7. [Implement and Validate One Story](#7-implement-and-validate-one-story)
8. [Complete the Story](#8-complete-the-story)
9. [Blocked-Story Readiness Sweep](#9-blocked-story-readiness-sweep)
10. [Continue or Hand Off](#10-continue-or-hand-off)
11. [Report](#11-report)

## 1. Confirm Implementation Source and Autonomy

Accept these sources, in priority order:

1. A specific GitHub/Jira tracker item with relationship data.
2. A ready queue from `manage-delivery-board`.
3. Approved work items from `create-prd-work-items`.
4. An approved local story list under `docs/`.
5. A PRD fallback only when the user explicitly asks for temporary local planning.

For tracker sources, fetch the current item state before coding. For local stories, read the story table and source PRD/design.

If the only input is an approved PRD, ask: "Do you want me to use `create-prd-work-items` to create durable tracker stories first, or draft a local temporary story plan for this session?" Stop until the user chooses.

Treat requests like "continue implementing the PRD", "work through the ready stories", "implement the next unblocked ticket", or "keep making progress" as authorization to proceed through routine implementation/status/update loops without asking after every stage. Ask only when the manual-review triggers in this workflow appear.

## 2. Discover Status Schema and Relationships

Before changing tracker/local state, determine:

- status field names and allowed values
- which statuses mean backlog, blocked, ready, in progress, validation, review/submission, done/accepted, or released
- whether Done requires code validation only, PR/MR merge, release, or product-owner acceptance
- relationship types for blocks/blocked-by, parent/child, duplicate, related, dependency, or Jira links
- whether comments, audit fields, project fields, labels, milestones, or assignees are expected when statuses change

Do not invent statuses. Map to the closest existing workflow status. If the board has no clear Ready/In Progress/Done semantics, ask or use a local report instead of mutating tracker state.

## 3. Select Ready Work

If the user named a specific item, verify that item first. Otherwise select the highest-priority ready item from the queue using this order:

1. Unblocked foundational work that unlocks downstream stories.
2. Risk-reducing or contract/schema/API work before dependent UI/integration work.
3. Small independent stories with clear validation.
4. Work already assigned to this repo/system and current branch context.

Before declaring that no ready work exists, run the blocked-story readiness sweep in section 9; a completed dependency may have made additional work ready.

## 4. Verify Readiness

A story is ready only when:

- it is approved for implementation
- it is not blocked by any open tracker relationship or local dependency
- the owning repo/system matches the current task or the user explicitly asks for cross-repo work
- acceptance criteria are observable and testable
- validation commands/checks are known or a practical fallback is agreed
- required design/PRD context is linked or available
- external services, secrets, environments, or signoffs needed for the story are available or not required

Do not treat labels/tags or prose mentions as sufficient blocker truth when tracker relationships exist.

If readiness is unclear, use `manage-delivery-board` or ask the user instead of coding.

## 5. Plan Without Unnecessary Pauses

For the selected story, read the source PRD/design/work item and relevant code. Keep a focused plan in the conversation or a `docs/implement-prd-stories/...` note when useful:

```markdown
## Implementation Plan

**Story**: {tracker ref or local ID}
**Why ready**: {relationship/dependency evidence}
**Scope**: {one-slice summary}
**Files likely touched**: {paths}
**Acceptance criteria**: {criteria}
**Validation**: {commands/manual checks}
**Out of scope**: {non-goals and related blocked work}
```

If the user already authorized this exact story, ready queue, or PRD implementation run, do not pause for another approval unless the plan changes scope or introduces a manual-review trigger. If authorization is missing, ask before source-code edits.

Manual review is required before:

- implementing a blocked or dependent item
- changing requirements, non-goals, acceptance criteria, or story scope
- broad refactors not required by the story
- touching another repo/system not authorized for this run
- weakening, deleting, or bypassing validation to make the story pass
- creating new tracker items or changing contentious ownership/priority without approval
- closing, deleting, reassigning, or resolving contentious tracker items
- using credentials, external services, paid resources, production systems, or signoffs not already authorized
- continuing after a failure whose repair would change scope or create product/owner decisions

## 6. Progress Story Status

Stage progression is part of this skill, not optional cleanup.

When tracker/local mutations are authorized for the run:

1. Move the selected story from Ready/To Do to In Progress/Doing/Active before source-code edits when the workflow supports it.
2. Add a short note when helpful: implementation started, branch if known, and intended validation.
3. During validation, use the board's Validation/Review/Ready for Review status only if that status exists and matches repo convention.
4. On pass, move to Done only if the story definition of done is satisfied. If Done requires PR/MR merge, release, or owner acceptance, move to Implemented/Ready for Review/Validation Passed instead.
5. On blocked or failed, set Blocked/Failed only with evidence and exact next action.

For local story files, update the local status table and preserve dates, evidence, and dependency notes.

## 7. Implement and Validate One Story

1. Re-read relevant code and tests.
2. Make the smallest change that satisfies the story.
3. Add/update tests when appropriate for the story's validation plan.
4. Run targeted validation first.
5. Run broader required checks if the story affects shared contracts, schemas, build paths, permissions, performance-sensitive paths, or risky behavior.
6. If validation fails because of an implementation mistake, attempt a bounded self-repair and rerun validation.
7. Mark the story `pass`, `blocked`, or `failed` with evidence.

Do not continue to another story after failed validation unless the next story is independent and safe, or the user requested continuous progress and the failure is recorded as blocked/failed without contaminating the next item.

## 8. Complete the Story

When validation passes:

- update status according to the discovered schema
- record validation commands and outcomes
- list changed files and behavior summary
- link branch/commit/PR/MR if available
- record any discovered follow-ups without expanding the current scope
- preserve newly discovered blockers using tracker-native relationships when the target item already exists and relationship updates are authorized

Do not encode blockers only as labels if relationship links are available.

If `submit-change-request` is needed to create a PR/MR before Done is allowed, mark the story as Implemented/Ready for Review and hand off rather than pretending it is Done.

## 9. Blocked-Story Readiness Sweep

After each completed/implemented story, review blocked work tied to the same PRD, epic, parent issue, project, milestone, or local story group.

For each blocked story:

1. Fetch current relationship state.
2. List every blocker relationship or local dependency.
3. Mark each blocker as satisfied only when it is done/closed/accepted/merged/released according to its own definition, or explicitly waived.
4. Confirm the candidate story still has clear acceptance criteria, owner repo/system, design/test links, and available required environments/secrets/signoffs.
5. If all blockers are satisfied and the story is otherwise ready, move it from Blocked to Ready/To Do/Next according to the board schema.
6. Add a concise comment or local note: what unblocked it, which blockers were satisfied, and validation/design context to use next.
7. Leave still-blocked stories blocked with the exact remaining blockers and needed action.

Do not remove historical dependency relationships unless the tracker convention requires it. Prefer adding a readiness comment/status update over deleting useful dependency history.

If readiness updates require owner judgment, contentious priority changes, cross-team reassignment, or new work-item creation, record proposed updates and ask instead of mutating.

## 10. Continue or Hand Off

After the blocked-story sweep:

- If the user asked for one story only, stop after the report and name the next ready item if known.
- If the user asked to continue the feature/PRD queue and another ready story exists, select the next ready story and loop from section 4 without another approval pause.
- If no ready work remains, report blocked items and the smallest action that would unblock progress.
- When validated work is ready for remote review, use `submit-change-request` for commit/push/PR/MR creation and CI/CD monitoring.
- Use `manage-delivery-board` when board state is too ambiguous to safely update or select next work.
- Use `create-prd-work-items` when missing dependency work needs durable tracker items.

## 11. Report

```markdown
## PRD Story Implementation Report

**Source**: {tracker/project/PRD/local plan}
**Story completed**: {ref/title}
**Status**: pass | blocked | failed | implemented-ready-for-review | done

### Changed Files
- `{path}` — {summary}

### Validation Summary
- `{command}` — {pass/fail/not run and why}

### Story Stage Updates
| Story | From | To | Evidence |
| --- | --- | --- | --- |

### Blocked-Story Readiness Sweep
| Story | Previous blockers | Current status | Action taken |
| --- | --- | --- | --- |

### Tracker Updates
- {items/relationships/statuses updated or not authorized}

### Remaining Work or Risks
- {open blockers, follow-ups, next ready item if known}

### Next Step
- {continue with next story, use submit-change-request, use manage-delivery-board, ask owner, etc.}
```
