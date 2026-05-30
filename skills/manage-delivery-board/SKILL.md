---
name: manage-delivery-board
description: |
  Inspect, maintain, and prioritize GitHub Projects, GitHub Issues, or Jira delivery boards for AI-assisted development. Use when the user asks for blocked/unblocked work, next-ready story selection, dependency cleanup, duplicate detection, stale item triage, cross-repo delivery sequencing, sprint/project board hygiene, or implementation handoff. Tracker/planning skill only; do not edit source code.
---

# Manage Delivery Board

Use this skill to keep implementation work ordered by real tracker relationships so agents code only work that is ready.

## Boundary

This skill reads and updates trackers, not source code. Ask before mutating GitHub/Jira unless the user explicitly authorizes board updates. Use `implement-prd-stories` when the user asks to code a ready item.

Dependency readiness must come from tracker-native relationships or an explicitly approved relationship field. Do not infer blockers solely from labels, tags, or body prose unless the user accepts that fallback for the run.

## Runbook

1. Read `references/workflow.md`.
2. Confirm the target board/project/filter, target repos, and whether updates are allowed.
3. Discover fields, statuses, item types, and relationship/link capabilities.
4. Fetch current items and normalize status, owner, repo/system, priority, relationships, and validation readiness.
5. Detect blocked items, unblocked ready items, missing relationships, duplicate/competing items, stale work, cycles, and unclear acceptance criteria.
6. Recommend or apply safe board updates after approval.
7. Produce a next-ready queue for `implement-prd-stories`, including item refs, blockers, acceptance criteria, and validation commands.

## Handoff

Use this skill before implementation sessions, maintainer standups, or sprint planning. Then invoke `implement-prd-stories` with the top unblocked item or queue.

## Documentation Output

When writing plans, reports, PRDs, briefs, findings, story tracking, scratch notes, or other generated documentation, write them under the repository-root `docs/` directory, preferably `docs/delivery-board/...` or the specific `docs/` path named in the workflow. Do not use `.agents/`, `.pi/`, `.codex/`, `.claude/`, or other agent-specific directories for generated documentation.
