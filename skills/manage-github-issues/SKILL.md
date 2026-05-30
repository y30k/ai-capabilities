---
name: manage-github-issues
description: |
  Manage GitHub issues without implementing fixes: create high-quality issues from bug reports, reproduce problems when possible, deduplicate against existing issues, label and triage open issues, link related PRs, and prepare stale-item digests. Use when the user asks to file an issue, report a bug, triage issues, dedupe issues, or maintain the issue backlog.
---

# Manage GitHub Issues

Use this skill for issue creation and triage. Use `fix-github-issue` when the user wants code changes. Use `create-prd-work-items` instead when the user wants an approved PRD split into dependency-linked GitHub/Jira implementation stories.

Read `references/workflow.md` and choose **create issue** or **triage backlog**. For board-level dependency sequencing and next-ready work, use `manage-delivery-board`.

## Documentation Output

When writing plans, reports, PRDs, briefs, findings, story tracking, scratch notes, or other generated documentation, write them under the repository-root `docs/` directory, preferably `docs/manage-github-issues/...` or the specific `docs/` path named in the workflow. Do not use `.agents/`, `.pi/`, `.codex/`, `.claude/`, or other agent-specific directories for generated documentation.
