---
name: release
description: |
  Prepare or execute software releases with release-mechanics-specific validation and action-specific approval gates. Use when the user asks to plan or cut a versioned release, hotfix, prerelease, tag, hosted release, changelog or release notes, or package publication. Discover repository conventions, verify version and tag uniqueness, and require separate authorization before commits, pushes, hosted releases, or registry publishing.
---

# Release

## Boundary

Treat release planning and drafting as read-only. Approval of a version or release notes does not authorize file edits, commits, tags, pushes, hosted releases, or package publication. Verify the release source already passed pre-submission production readiness and either completed its PR/MR review, remediation, integration, and required CI/CD or followed an explicitly authorized fast-track path; do not rerun a separate full production-readiness phase. Read `references/workflow.md`, present an action manifest, and perform only the separately approved actions. Never overwrite an existing tag, force-push, or blindly retry an ambiguous publish.

After the release or deployment completes, use `observe-release` to verify rollout health and capture follow-up work.

## Documentation Output

Write durable release plans and reports under `docs/release/` or a user-specified path under `docs/`. Never store generated documentation in agent-state directories such as `.agents/`, `.pi/`, `.codex/`, or `.claude/`.
