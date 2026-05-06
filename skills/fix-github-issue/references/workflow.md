# GitHub Issue Fix Workflow

## 1. Identify the Issue

- Extract the issue number from the user request.
- If ambiguous and `gh` is available, search open issues.
- Fetch title, body, labels, comments, state, URL, and author.

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
- Capture findings under `.agents/artifacts/fix-github-issue/{issue}/` when useful.

## 5. Plan

Write a concise plan with:

- Goal and non-goals.
- Files likely to change.
- Test/validation strategy.
- Risks and rollback notes.

Present the plan and wait for user approval before source-code edits unless the user explicitly pre-authorized end-to-end fixing. Ask before proceeding if scope is ambiguous, destructive, or much larger than the issue suggests.

For `investigate-only`, `plan-only`, and `validate-only` modes, stop here or after validation and do not implement.

## 6. Implement

- Prefer minimal changes that address the issue.
- Follow existing project patterns.
- Add or update tests when practical.
- Keep unrelated cleanup out of scope.

## 7. Validate

Run the most relevant checks, such as typecheck, lint, unit tests, reproduction scripts, or targeted manual verification. If a check cannot run, explain why and what remains unverified.

## 8. Optional Full Review

For full-review mode, review the resulting diff across lanes:

- Correctness and edge cases.
- Error handling and user-facing failures.
- Test coverage.
- Comments and documentation quality.
- Scope creep and simplification opportunities.

Fix high-confidence findings, rerun validation, and simplify changed code where possible.

## 9. Report

Return:

- Issue number and summary.
- Root cause or implementation approach.
- Changed files.
- Validation results.
- Remaining risks.
- PR body or issue comment if requested.
