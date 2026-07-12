---
name: create-prd-work-items
description: |
  Convert approved PRDs, technical designs, or feature specs into deduplicated, dependency-linked work items in GitHub Projects, GitHub Issues, or Jira across one or more repositories. Use when the user asks to split a PRD into stories, tasks, or epics; populate or update a project board; create implementation tickets; map cross-repo work; detect competing or duplicate items; set blocker, dependency, or parent-child relationships; or prioritize an implementation backlog before coding. Planning/tracker skill only; do not edit source code.
---

# Create PRD Work Items

Use this skill to turn approved requirements into tracker-native work that implementation agents can pick up safely.

## Boundary

This skill creates or updates planning artifacts and tracker items only. Do not edit source code. Ask before mutating GitHub/Jira unless the user explicitly authorized item creation or updates.

Prefer tracker relationships over labels or body text for dependency data. Labels/tags may describe area, type, repo, or lifecycle state, but they must not be the primary source of truth for `blocks`, `blocked by`, `parent`, `child`, `duplicate`, or `related` relationships.

## Runbook

1. Read `references/workflow.md`.
2. Confirm the PRD/spec/design input, target tracker URL, target org/repos, and posting permission.
3. Discover the tracker schema and supported relationship model before drafting items.
4. Read the PRD/spec/design completely and extract candidate epics, stories, tasks, spikes, and external dependencies.
5. Search existing project items and repo tickets for similar, duplicate, competing, or related work.
6. Update an existing item instead of creating a new one when it is the canonical match.
7. Draft small implementation-ready items with acceptance criteria, validation, repo/system ownership, and dependency relationships.
8. Prioritize by dependency graph: unblocked foundational items first, dependents later, external blockers visible.
9. Create/update/link items only after approval, then report the board state and next unblocked work.

## Handoff

After items exist, use `manage-delivery-board` to maintain blocked/unblocked state and `implement-prd-stories` to code the next unblocked item.

## Documentation Output

Write durable drafts and mutation reports under `docs/prd-work-items/` or a user-specified path under `docs/`. Never store generated documentation in agent-state directories such as `.agents/`, `.pi/`, `.codex/`, or `.claude/`.
