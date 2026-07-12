---
name: resolve-merge-conflicts
description: |
  Resolve Git conflicts safely by identifying the in-progress operation, inspecting base, ours, theirs, and surrounding history, preserving intended behavior, resolving and staging conflicted paths, validating the result, and reporting whether the operation is ready to continue. Use when a merge, rebase, cherry-pick, revert, pull, or pull request reports conflicts, unmerged paths, or conflict markers. Use submit-change-request after resolution when the user wants the result committed, pushed, or submitted.
---

# Resolve Merge Conflicts

Read and follow `references/workflow.md`. Inspect the existing operation before editing. Do not initiate, abort, continue, skip, or force an operation unless that action was already requested or separately authorized. Preserve unrelated working-tree changes and route commit, push, or submission work to `submit-change-request`.

## Documentation Output

Write durable conflict-resolution reports under `docs/resolve-merge-conflicts/` or a user-specified path under `docs/`. Never store generated documentation in agent-state directories such as `.agents/`, `.pi/`, `.codex/`, or `.claude/`.
