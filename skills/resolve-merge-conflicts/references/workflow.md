# Merge Conflict Resolution Workflow

## 1. Inspect State

- Run `git status --short` and `git diff --name-only --diff-filter=U`; inspect `git ls-files -u` when stage entries are needed.
- Identify whether a merge, rebase, cherry-pick, revert, or pull is in progress before editing or running another Git operation.
- Inspect base, stage-2, and stage-3 versions with `git show :1:<path>`, `git show :2:<path>`, and `git show :3:<path>` when available. Verify what `ours` and `theirs` mean for the current operation; their intuitive branch meaning can reverse during rebase.
- Record unrelated staged, unstaged, and untracked files and leave them untouched.

## 2. Understand Intent

For each conflict:

- Read surrounding code, not only conflict markers.
- Inspect recent commits or PR context if available.
- Decide whether to keep ours, theirs, or combine.
- Avoid deleting behavior without evidence.

## 3. Resolve and Stage

- Resolve text conflicts manually and remove conflict markers.
- Handle rename/rename, delete/modify, mode, submodule, generated-file, and binary conflicts according to repository policy; do not treat them as ordinary text merges.
- Stage only each resolved path with `git add <path>` or record an intentional deletion with `git rm <path>`.
- Re-run `git diff --name-only --diff-filter=U` and `git ls-files -u`; do not declare resolution while either reports unmerged entries.
- Inspect the staged resolution with `git diff --cached` and keep unrelated changes out.

## 4. Validate

Run targeted tests plus applicable typecheck, lint, build, or syntax checks. Run `git diff --cached --check` against the staged resolution, plus `git diff --check` when unstaged changes remain, and inspect both staged and unstaged diffs. For multi-step rebases or cherry-picks, expect later commits to conflict again and repeat this workflow after each authorized continuation.

## 5. Report or Continue

List resolved paths, per-conflict decisions and evidence, validation commands and results, remaining unrelated changes, and the exact operation state. Continue or abort the merge, rebase, cherry-pick, or revert only when already authorized; otherwise report the precise next command for the user.
