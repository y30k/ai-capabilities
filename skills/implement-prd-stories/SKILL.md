---
name: implement-prd-stories
description: |
  Implement approved, unblocked PRD stories or tracker work items one slice at a time with validation after each slice. Use after `create-prd-work-items` or `manage-delivery-board` identifies dependency-ready GitHub Projects, GitHub Issues, Jira items, or approved local stories; when the user asks to code PRD stories, implement the next unblocked ticket, execute approved work items, or continue feature implementation from a delivery board. Requires explicit approval before source-code changes. Not for creating tracker items or decomposing PRDs into tickets; use `create-prd-work-items` for that.
---

# Implement PRD Stories

Use this coding skill to implement approved PRD work that is already small, owned, and unblocked.

## Boundary

This skill starts after requirements/design/story planning. Prefer consuming tracker-native work items created by `create-prd-work-items` and prioritized by `manage-delivery-board`.

If the user provides only a PRD with no approved story/work-item breakdown, do not silently decompose and code. Ask whether to use `create-prd-work-items` first, or create a temporary local story plan for this session and wait for approval before editing source code.

Do not implement blocked work. Dependency readiness must come from tracker relationships or an explicitly approved local dependency table, not labels or body prose alone.

## Runbook

1. Read `references/workflow.md`.
2. Identify the implementation source: tracker item, ready queue, approved local story list, or PRD fallback.
3. Verify the selected story is approved, unblocked, small enough, owned by this repo/system, and has acceptance criteria plus validation.
4. Present a focused implementation plan and wait for approval before source-code edits unless the user has already authorized coding this exact item.
5. Implement one story at a time, running its validation before moving on.
6. Stop if requirements conflict, blockers appear, validation fails in a way that changes scope, or the story depends on unfinished external work.
7. Update tracker/story status only when authorized, preserving links to commits, validation, blockers, and follow-up items.

## Documentation Output

When writing plans, reports, PRDs, briefs, findings, story tracking, scratch notes, or other generated documentation, write them under the repository-root `docs/` directory, preferably `docs/implement-prd-stories/...` or the specific `docs/` path named in the workflow. Do not use `.agents/`, `.pi/`, `.codex/`, `.claude/`, or other agent-specific directories for generated documentation.
