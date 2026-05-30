# Implement PRD Stories Workflow

## 1. Confirm Implementation Source

Accept these sources, in priority order:

1. A specific GitHub/Jira tracker item with relationship data.
2. A ready queue from `manage-delivery-board`.
3. Approved work items from `create-prd-work-items`.
4. An approved local story list under `docs/`.
5. A PRD fallback only when the user explicitly asks for temporary local planning.

For tracker sources, fetch the current item state before coding. For local stories, read the story table and source PRD/design.

If the only input is an approved PRD, ask: "Do you want me to use `create-prd-work-items` to create durable tracker stories first, or draft a local temporary story plan for this session?" Stop until the user chooses.

## 2. Verify Readiness

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

## 3. Build Focused Implementation Plan

For the selected story, read the source PRD/design/work item and relevant code. Present:

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

Ask for approval before source-code edits unless already granted for this exact story.

## 4. Implement One Story

1. Re-read relevant code and tests.
2. Make the smallest change that satisfies the story.
3. Add/update tests when appropriate for the story's validation plan.
4. Run targeted validation first.
5. Run broader required checks if the story affects shared contracts, schemas, build paths, or risky behavior.
6. Mark the story `pass`, `blocked`, or `failed` with evidence.

Do not continue to another story after a failed validation unless the user asks for a repair attempt or the next story is independent and safe.

## 5. Scope and Blocker Control

Stop and ask before:

- implementing a blocked or dependent item
- changing requirements, non-goals, or acceptance criteria
- broad refactors not required by the story
- touching another repo/system not authorized for this run
- weakening validation to make the story pass
- creating new tracker items without approval

If implementation discovers missing dependency work, record the blocker and route to `create-prd-work-items` or `manage-delivery-board`.

## 6. Tracker/Story Updates

When authorized, update the tracker or local story file:

- status/result
- validation commands and outcomes
- linked branch/commit/PR if available
- newly discovered blockers using tracker-native relationships
- follow-up items for out-of-scope work

Do not encode new blockers only as labels if relationship links are available.

## 7. Final Report

```markdown
## PRD Story Implementation Report

**Source**: {tracker/project/PRD/local plan}
**Story completed**: {ref/title}
**Status**: pass | blocked | failed

### Changed Files
- `{path}` — {summary}

### Validation Summary
- `{command}` — {pass/fail/not run and why}

### Tracker Updates
- {items/relationships/statuses updated or not authorized}

### Remaining Work or Risks
- {open blockers, follow-ups, next ready item if known}
```
