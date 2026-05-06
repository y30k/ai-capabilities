---
name: release
description: |
  Prepare and cut a software release with gated validation: parse release intent, check repository state, run smoke tests, detect stack/version files, bump versions, draft changelog, request approval, commit/tag/create release, and handle optional package distribution. Use when the user asks to release, cut a release, ship, tag, publish, or prepare changelog and release notes.
---

# Release

Use this skill for release preparation and execution. Releases can affect users and external systems, so preserve approval gates.

Read `references/workflow.md` before changing versions, tags, branches, or published artifacts.

## Documentation Output

When writing plans, reports, PRDs, briefs, findings, story tracking, scratch notes, or other generated documentation, write them under the repository-root `docs/` directory, preferably `docs/release/...` or the specific `docs/` path named in the workflow. Do not use `.agents/`, `.pi/`, `.codex/`, `.claude/`, or other agent-specific directories for generated documentation.
