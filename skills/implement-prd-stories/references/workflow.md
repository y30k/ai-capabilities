# Implement PRD Stories Workflow

## 1. Confirm Handoff

- Identify the PRD path or pasted PRD content.
- Read the PRD fully.
- Check whether the user has explicitly approved it for implementation.
- If approval is missing, summarize the PRD and ask: "Do you approve implementing this PRD as written?" Stop until the user answers.

## 2. Extract Implementation Inputs

Extract and preserve:

- Problem and proposed solution.
- Key hypothesis and success metrics.
- Non-goals and out-of-scope items.
- Must/should/could/won't capabilities.
- Technical approach and verified file references.
- Implementation phases, dependencies, and open questions.
- Validation notes and any `TBD — needs research` items.

If an open question changes implementation scope, ask the user before coding.

## 3. Create Story Breakdown

Create small stories that can each be completed in one implementation slice.

Good story size examples:

- Add or modify one schema field plus focused tests.
- Add one utility or service function plus tests.
- Extend one API endpoint or command path.
- Add one UI component state or integration.
- Wire an existing component to a new data field.

Avoid stories like "build the whole feature" or "add authentication"; split them by dependency.

Story fields:

```markdown
| ID | Title | Acceptance Criteria | Depends On | Validation |
| --- | --- | --- | --- | --- |
| US-001 | {small slice} | {pass/fail criteria} | - | {test/check} |
```

## 4. Approval Gate

Present the story breakdown, planned file areas, validation commands, and known risks. Ask for approval before source-code edits.

Proceed only when the user confirms. If they request changes, update the story breakdown first.

## 5. Implement One Story at a Time

For each story:

1. Re-read the relevant PRD section and existing code.
2. Implement the smallest change that satisfies the story.
3. Run the story's validation command or the closest practical check.
4. Mark the story `pass`, `fail`, or `blocked` with notes.
5. Continue to the next dependency-ready story only if validation is acceptable.

## 6. Scope Control

Stop and ask the user before:

- Adding capabilities not in the PRD.
- Changing non-goals.
- Making broad refactors not required by the story.
- Proceeding when validation contradicts the PRD.
- Implementing a story with unresolved `TBD` requirements.

## 7. Final Report

```markdown
## PRD Implementation Report

**PRD**: {path}
**Stories completed**: {n}/{total}

| Story | Status | Validation | Notes |
| --- | --- | --- | --- |
| US-001 | pass/fail/blocked | {command/result} | {notes} |

### Changed Files
- `{path}` — {summary}

### Validation Summary
- {commands and outcomes}

### Remaining Work or Risks
- {open items}
```
