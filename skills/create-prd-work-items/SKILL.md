---
name: create-prd-work-items
description: |
  Convert approved PRDs, technical designs, or feature specs into deduplicated, dependency-linked GitHub Projects, GitHub Issues, or Jira work items across one or more repositories. Use when the user asks to split a PRD into stories/tasks/epics, populate or update a project board, create implementation tickets, map cross-repo work, detect competing or duplicate items, set blockers/dependencies/parent-child relationships, or prioritize an implementation backlog before coding. Planning/tracker skill only; do not edit source code.
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

## Example Request Shape

```text
Use docs/PRODUCT_REQUIREMENTS.md to build stories for this repo in https://github.com/orgs/kextant/projects/1/views/1. Use labels/tags only for implementation area across github.com/kextant repos. Add to similar existing items instead of creating duplicates. Identify dependencies using tracker relationships, not labels or prose, and prioritize unblocked work first.
```

## Handoff

After items exist, use `manage-delivery-board` to maintain blocked/unblocked state and `implement-prd-stories` to code the next unblocked item.

## Documentation Output

When writing plans, reports, PRDs, briefs, findings, story tracking, scratch notes, or other generated documentation, write them under the repository-root `docs/` directory, preferably `docs/prd-work-items/...` or the specific `docs/` path named in the workflow. Do not use `.agents/`, `.pi/`, `.codex/`, `.claude/`, or other agent-specific directories for generated documentation.
