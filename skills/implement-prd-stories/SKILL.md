---
name: implement-prd-stories
description: |
  Implement approved, unblocked PRD stories or tracker work items one slice at a time in the current repository, validate and stage each story's changes, and apply the tracker's real completion semantics: move to Done and propagate newly unblocked dependents to Ready only when current evidence satisfies Done, otherwise use an existing intermediate state or retain a truthful non-Done state until submission, merge, acceptance, or release requirements are met. Use after `create-prd-work-items` or `manage-delivery-board` identifies dependency-ready GitHub Projects, GitHub Issues, Jira items, or approved local stories; when the user asks to implement the next unblocked ticket, continue delivery from a board, advance ready work, or keep a PRD moving. Require explicit authorization before editing files or Git state in another repository. Not for creating tracker items or decomposing PRDs; use `create-prd-work-items`.
---

# Implement PRD Stories

Use this coding skill to implement approved PRD work that is already small, owned, and unblocked, while keeping the delivery board/story list moving with minimal user effort.

## Boundary

This skill starts after requirements/design/story planning. Prefer consuming tracker-native work items created by `create-prd-work-items` and prioritized by `manage-delivery-board`.

If the user provides only a PRD with no approved story/work-item breakdown, do not silently decompose and code. Ask whether to use `create-prd-work-items` first, or create a temporary local story plan for this session and wait for approval before editing source code.

Resolve and record the current Git repository root before planning. Keep all source, test, generated-file, documentation, and Git-index mutations inside that repository. Do not edit a sibling repository, nested independent repository, submodule, or other worktree unless the user explicitly authorizes that repository. Cross-repository tracker reads and routine Done/Ready status transitions required by the dependency sweep are tracker mutations, not authorization for cross-repository code or file changes.

Do not implement blocked work. Dependency readiness must come from tracker relationships or an explicitly approved local dependency table, not labels or body prose alone.

## Autonomy Policy

Treat explicit authorization to implement a selected story, ready queue, or PRD delivery board as authorization for this completion protocol without repeated prompts:

- make scoped technical changes and run validation only in the current repository
- select the next ready story when the user authorized a queue but did not name an item
- stage only the completed story's local changes while preserving unrelated working-tree and index state
- apply routine tracker transitions for the active story, including In Progress and the tracker-accurate completion transition; use Done only when current evidence satisfies its discovered definition, otherwise use an existing intermediate state or retain the current truthful non-Done state
- record validation, staged files, blockers, and follow-up evidence on the story when the tracker supports it
- after tracker-accurate Done is verified, inspect dependency-linked blocked stories across the tracking scope without filtering by owning repository, and move every now-unblocked story to Ready; never propagate readiness from an intermediate or retained non-Done state
- attempt bounded self-repair for validation failures caused by the current implementation
- continue with another ready story only when requested and only when its technical work belongs to the current repository or cross-repository implementation was explicitly authorized

These routine active-story and dependency-driven Done/Ready tracker transitions are part of implementation authorization. Ask for user input only when manual review is truly required: ambiguous requirements, scope changes, blocked dependencies, unavailable or ambiguous Done/Ready mappings, destructive or contentious tracker changes beyond these routine transitions, closing/deleting/reassigning unrelated work, technical edits outside the current repository, missing credentials/signoffs, validation failures that change scope or require weakening checks, production-impacting decisions, or any action that would commit, push, rewrite history, or bypass required review.

## Runbook

1. Read `references/workflow.md`.
2. Resolve the current repository root and snapshot its working tree and index before editing; if another repository was explicitly authorized, resolve and snapshot that named root before touching it.
3. Identify the implementation source: tracker item, ready queue, approved local story list, or PRD fallback.
4. Discover the tracker/local Done and Ready mappings, the evidence required for Done, any existing intermediate implementation status, and the relationship model before changing statuses.
5. Verify the selected story is approved, unblocked, small enough, technically owned by the current repository unless cross-repository implementation was explicitly authorized, and has acceptance criteria plus validation.
6. If implementation authorization for this exact story/queue/run already exists, proceed without another approval pause; otherwise present a focused plan and ask before source-code edits.
7. Move the active story to the appropriate in-progress status, then implement only that story in the current repository and run targeted plus broader required validation.
8. If validation fails from an implementation mistake, attempt a bounded repair; stop when the fix changes scope, blockers appear, or owner input is needed.
9. After validation passes, stage only the story's intended changes in each explicitly authorized repository touched and verify no story-owned hunk remains unstaged; do not commit or push.
10. Apply the discovered completion semantics and refetch to verify the transition. Move the active story to Done only when validated staged implementation satisfies the tracker's Done definition; otherwise move it to an existing Implemented/Ready for Review equivalent or retain its current truthful non-Done state, record the unmet Done condition, and do not claim Done or unblock dependents.
11. Only after tracker-accurate Done is verified, sweep dependency-linked blocked stories across the tracker, including items owned by other repositories. Move each to Ready only when every blocker and independent readiness gate is satisfied; refetch to verify each transition. If Done is still pending, skip the sweep and record the later owner/action that must finalize Done and readiness propagation. If any required Ready transition fails, preserve the staged Done story and stop before implementing another item. Do not edit those repositories.
12. For every technical repository touched, treat its source commit and staged index as a separate candidate and run `check-production-readiness` in that repository. If unrelated pre-existing staged entries remain anywhere, preserve them and ask how to separate or include them rather than misrepresenting an index. Record one verdict per repository, then use `submit-change-request` separately for each READY or CONDITIONALLY READY candidate.

## Documentation Output

Write durable implementation plans and story reports under `docs/implement-prd-stories/` or a user-specified path under `docs/`. Never store generated documentation in agent-state directories such as `.agents/`, `.pi/`, `.codex/`, or `.claude/`.
