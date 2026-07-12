# GitHub Issue Fix Workflow

## 1. Identify the Issue and Repository

- Extract the issue number and owner/repository from a URL or qualified reference; for a bare number, use the current repository only.
- Resolve the current Git root and canonical remote identity with `git rev-parse --show-toplevel` plus provider/remote metadata.
- If ambiguous and `gh` is available, search open issues only in the verified repository.
- Fetch title, body, labels, comments, state, URL, author, and repository identity.
- Compare the issue repository with the current checkout before planning edits. On mismatch, stop and ask the user to switch to the correct checkout or explicitly authorize a named cross-repository implementation path; never apply another repository's issue to the current codebase by default.

## 2. Classify

Classify as bug, feature, enhancement, refactor, chore, documentation, or question. Explain why.

## 3. Choose Mode

| Mode | Best for | Extra work |
| --- | --- | --- |
| standard | most issues | normal validation |
| smoke-first | bugs/regressions | reproduce or failing test before fix |
| full-review | risky changes | review lanes, self-fix, simplification |
| investigate-only | unclear issue | no code changes |
| plan-only | implementation deferred | plan artifact only |
| validate-only | user has a fix | run checks and inspect diff |

## 4. Research and Investigate

- Search the codebase for relevant files, APIs, tests, schemas, and docs.
- Read actual files before making technical claims.
- For bugs, identify expected vs actual behavior and likely root cause.
- For features/enhancements, identify existing patterns to extend.
- Capture findings under `docs/github-issues/{issue}/` when useful.

## 5. Plan

Write a concise plan with:

- Goal and non-goals.
- Files likely to change.
- Test/validation strategy.
- Risks and rollback notes.

Present the plan and wait for user approval before source-code edits unless the user explicitly pre-authorized end-to-end fixing. Ask before proceeding if scope is ambiguous, destructive, or much larger than the issue suggests.

For `investigate-only`, `plan-only`, and `validate-only` modes, stop here or after validation and do not implement.

For **smoke-first** mode, reproduce the reported behavior or add a focused regression test before editing, run it, and confirm it fails for the expected reason. After the fix, rerun the same check and require it to pass. If reproduction is impossible, record why and obtain agreement on a substitute validation signal.

## 6. Implement

- Prefer minimal changes that address the issue.
- Follow existing project patterns.
- Add or update a focused regression test for changed behavior. If automation is infeasible, record why and perform a concrete manual or reproduction check.
- Keep unrelated cleanup out of scope.

## 7. Validate

Run the issue reproduction or regression check, relevant targeted tests, and required broader typecheck, lint, build, or integration checks. Verify the issue acceptance criteria and inspect the final diff. If a check cannot run, report the command, reason, and remaining uncertainty.

## 8. Optional Full Review

For full-review mode, review the resulting diff across lanes:

- Correctness and edge cases.
- Error handling and user-facing failures.
- Test coverage.
- Comments and documentation quality.
- Scope creep and simplification opportunities.

Fix high-confidence findings within the approved issue scope, rerun affected validation, and report scope-changing findings instead of applying them.

## 9. Stage the Candidate When Authorized

For coding modes that will continue to production readiness, obtain explicit staging authorization unless the user already requested staging or candidate preparation. Snapshot `git status --short`, working-tree diffs, and cached diffs first. Present an intended file/hunk allowlist; stop on staged/unstaged overlap or unrelated pre-staged content unless an isolation plan is approved. Stage only intended hunks, inspect cached and unstaged views again, run `git diff --cached --check`, and verify no intended hunk remains unstaged and no unrelated hunk was absorbed. Do not commit or push.

Without staging authorization, return a validated local fix and exact staging plan; do not invoke `check-production-readiness` or call the work an exact staged candidate.

## 10. Report

Return:

- Issue number and summary.
- Root cause or implementation approach.
- Changed files.
- Validation results.
- Remaining risks.
- Production-readiness handoff only when the candidate was staged and verified; otherwise the pending staging plan. Then include the requested PR/MR title/body, issue comment draft, or `submit-change-request` handoff when applicable.
