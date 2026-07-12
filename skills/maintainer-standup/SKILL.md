---
name: maintainer-standup
description: |
  Prepare a concise, read-only maintainer briefing from local git and available GitHub context, covering recent commits, pull requests, checks, issues, review priorities, stale work, repository state, and suggested next actions. Use when a maintainer asks for a morning briefing, project status digest, review queue summary, or repository health snapshot. Use manage-delivery-board for dependency-aware project sequencing and manage-github-issues for tracker mutations.
---

# Maintainer Standup

Generate a concise, prioritized maintainer briefing without changing repository or tracker state.

Read `references/workflow.md`, confirm the repository and observation window, gather available local and GitHub context, and distinguish unavailable data from checked-empty results. Route dependency sequencing to `manage-delivery-board`, issue mutations to `manage-github-issues`, and code changes to the appropriate implementation skill.

## Documentation Output

Persist requested briefing history under `docs/maintainer-standup/briefs/` or another user-specified path under `docs/`. Never store generated documentation in agent-state directories such as `.agents/`, `.pi/`, `.codex/`, or `.claude/`.
