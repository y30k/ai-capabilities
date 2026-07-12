---
name: manage-github-issues
description: |
  Create and triage individual GitHub issues and repository issue backlogs without implementing fixes: draft evidence-based bug reports, check duplicates, suggest labels and ownership, link related pull requests, and prepare stale-issue digests. Use when the user asks to file or report an issue, deduplicate or triage GitHub issues, or maintain an issue backlog. Use manage-delivery-board instead for project-board status, dependency relationships, blocked or unblocked analysis, or next-ready sequencing.
---

# Manage GitHub Issues

Use `fix-github-issue` when the user wants code changes. Use `create-prd-work-items` when the user wants an approved PRD split into dependency-linked GitHub or Jira implementation stories.

## Boundary

Keep code inspection and reproduction read-only; do not implement a fix. Confirm whether the run is read-only, draft-only, or authorized to mutate GitHub. Ask before creating, editing, labeling, commenting on, linking, closing, or reopening issues unless the user explicitly authorized those actions.

Read `references/workflow.md` and choose **create issue** or **triage backlog**. Use `manage-delivery-board` for board-level dependency sequencing and next-ready work.

## Documentation Output

Write requested issue drafts and triage reports under `docs/manage-github-issues/` or another user-specified path under `docs/`. Never store generated documentation in agent-state directories such as `.agents/`, `.pi/`, `.codex/`, or `.claude/`.
