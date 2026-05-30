---
name: maintainer-standup
description: |
  Prepare a maintainer standup briefing for a repository: git status, recent commits, pull requests, issues, review priorities, stale work, and suggested next actions. Use when a maintainer wants a morning briefing, project status digest, review queue summary, or repository health snapshot. Works without model-specific variants.
---

# Maintainer Standup

Use this skill to generate a concise maintainer briefing. It replaces model-specific standup variants with one portable workflow.

Read `references/workflow.md`, gather available repository/GitHub context, and produce a prioritized digest. Use `manage-delivery-board` when the standup needs dependency-aware blocked/unblocked project-board sequencing.

## Documentation Output

When writing plans, reports, PRDs, briefs, findings, story tracking, scratch notes, or other generated documentation, write them under the repository-root `docs/` directory, preferably `docs/maintainer-standup/...` or the specific `docs/` path named in the workflow. Do not use `.agents/`, `.pi/`, `.codex/`, `.claude/`, or other agent-specific directories for generated documentation.
