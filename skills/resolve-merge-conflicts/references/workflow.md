# Merge Conflict Resolution Workflow

## 1. Inspect State

- Run `git status`.
- Identify conflicted files and operation type: merge, rebase, cherry-pick, or PR sync.
- Determine base, ours, and theirs when possible.

## 2. Understand Intent

For each conflict:

- Read surrounding code, not only conflict markers.
- Inspect recent commits or PR context if available.
- Decide whether to keep ours, theirs, or combine.
- Avoid deleting behavior without evidence.

## 3. Resolve

- Edit conflicts manually.
- Remove all conflict markers.
- Preserve formatting and project conventions.
- Keep unrelated changes out.

## 4. Validate

Run targeted tests, typecheck, lint, or build. At minimum run syntax checks for edited files if project checks are unavailable.

## 5. Report

List resolved files, decisions made, validation results, and any remaining manual steps such as `git rebase --continue`.
