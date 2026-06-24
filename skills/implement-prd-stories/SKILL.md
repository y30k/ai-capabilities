---
name: implement-prd-stories
description: |
  Implement approved, unblocked PRD stories or tracker work items one slice at a time with validation, routine story-status progression, and post-completion blocked-story readiness sweeps. Use after `create-prd-work-items` or `manage-delivery-board` identifies dependency-ready GitHub Projects, GitHub Issues, Jira items, or approved local stories; when the user asks to code PRD stories, implement the next unblocked ticket, continue feature implementation from a delivery board, advance ready work, or keep a PRD moving. Requires implementation authorization for the run, then minimizes repeated user prompts unless requirements, blockers, validation failures, destructive actions, cross-repo scope, or owner decisions require manual review. Not for creating tracker items or decomposing PRDs into tickets; use `create-prd-work-items` for that.
---

# Implement PRD Stories

Use this coding skill to implement approved PRD work that is already small, owned, and unblocked, while keeping the delivery board/story list moving with minimal user effort.

## Boundary

This skill starts after requirements/design/story planning. Prefer consuming tracker-native work items created by `create-prd-work-items` and prioritized by `manage-delivery-board`.

If the user provides only a PRD with no approved story/work-item breakdown, do not silently decompose and code. Ask whether to use `create-prd-work-items` first, or create a temporary local story plan for this session and wait for approval before editing source code.

Do not implement blocked work. Dependency readiness must come from tracker relationships or an explicitly approved local dependency table, not labels or body prose alone.

## Autonomy Policy

Treat explicit authorization to implement a selected story, ready queue, or PRD delivery board as authorization to perform routine, non-destructive delivery actions for that run:

- select the next ready story when the user did not name a specific item
- move the active story through ordinary statuses such as Ready → In Progress → Validation/Review/Done according to the board schema
- record validation evidence, changed files, blockers, and follow-up notes on the story
- attempt bounded self-repair for validation failures caused by the current implementation
- after a story completes, review blocked stories in the same PRD/epic/project and move any now-unblocked items to Ready according to tracker-native relationships
- continue to the next ready story when the user asked to continue the feature/PRD queue, until no ready work remains or a manual-review trigger appears

Ask for user input only when manual review is truly required: ambiguous requirements, scope changes, blocked dependencies, destructive tracker changes, closing/deleting/reassigning contentious work, cross-repo work not authorized for this run, missing credentials/signoffs, validation failures that change scope or require weakening checks, production-impacting decisions, or any action that would rewrite history or bypass required review.

## Runbook

1. Read `references/workflow.md`.
2. Identify the implementation source: tracker item, ready queue, approved local story list, or PRD fallback.
3. Discover the tracker/local status schema and relationship model before changing statuses.
4. Verify the selected story is approved, unblocked, small enough, owned by this repo/system, and has acceptance criteria plus validation.
5. If implementation authorization for this exact story/queue/run already exists, proceed without another approval pause; otherwise present a focused plan and ask before source-code edits.
6. Move the active story to the appropriate in-progress status when the workflow supports it.
7. Implement one story at a time, running targeted validation and then broader required checks when warranted.
8. If validation fails from an implementation mistake, attempt a bounded repair; stop only when the fix changes scope, blockers appear, or owner input is needed.
9. Update the story with status, validation evidence, changed files, blockers, and links. Mark Done only when the story's definition of done is met; otherwise use the repo's implemented/ready-for-review status.
10. After completion, perform a blocked-story readiness sweep: re-check blocked items tied to the same PRD/epic/project and move items to Ready when all tracker-native blockers are done/closed/accepted/waived.
11. When validated work is ready for remote review, hand off to `submit-change-request` for commit/push/PR/MR creation and CI/CD monitoring.

## Documentation Output

When writing plans, reports, PRDs, briefs, findings, story tracking, scratch notes, or other generated documentation, write them under the repository-root `docs/` directory, preferably `docs/implement-prd-stories/...` or the specific `docs/` path named in the workflow. Do not use `.agents/`, `.pi/`, `.codex/`, `.claude/`, or other agent-specific directories for generated documentation.
