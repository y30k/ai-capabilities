---
name: implement-prd-stories
description: |
  Implement an already reviewed and approved PRD by decomposing it into small,
  dependency-ordered, verifiable user stories and coding one story at a time with
  validation after each slice. Use when the user asks to implement a PRD, execute a
  PRD, build from requirements, implement PRD stories, or continue after reviewing a
  generated PRD. Requires explicit approval before source-code changes. Not for
  creating or revising PRDs; use create-interactive-prd for planning and requirements.
---

# Implement PRD Stories

Use this coding skill to turn an approved PRD into validated implementation slices.

## Boundary

This skill starts **after** planning/design/requirements review. If the PRD has not been reviewed or approved, summarize it and ask for explicit approval before editing source code. Do not rewrite requirements unless the user asks.

## Runbook

1. Read `references/workflow.md`.
2. Read the PRD completely, including non-goals, open questions, technical approach, implementation phases, and validation notes.
3. Create story tracking under `docs/prd-implementations/{prd-slug}/` when useful.
4. Present the story breakdown and validation plan, then wait for user approval before source-code edits.
5. Implement one small story at a time, validating after each story.
6. Stop and report if a story exposes a requirements conflict, unverified assumption, or scope expansion.

## Documentation Output

When writing plans, reports, PRDs, briefs, findings, story tracking, scratch notes, or other generated documentation, write them under the repository-root `docs/` directory, preferably `docs/implement-prd-stories/...` or the specific `docs/` path named in the workflow. Do not use `.agents/`, `.pi/`, `.codex/`, `.claude/`, or other agent-specific directories for generated documentation.
