# Pull Request Review Workflow

## 1. Fetch Context

- Identify PR number/branch.
- Read title, body, linked issues, changed files, diff, checks, comments, and project rules.
- Understand explicit scope and non-goals before flagging missing features.

## 2. Select Mode

| Mode | Use when | Lanes |
| --- | --- | --- |
| smart | default | scope + risk classification + selected lanes |
| comprehensive | user asks full/deep review | all lanes |
| maintainer | merge decision needed | direction, scope, user impact, review posture |
| validation | prove behavior changed correctly | base vs feature checks |
| fix-review-findings | user wants fixes from this review run | implement high-confidence findings without required thread replies |
| address existing review comments | user wants reviewer threads addressed, replied to, committed, and pushed | hand off to `address-pr-review-comments` |

## 3. Review Lanes

Run the relevant lanes:

- Correctness and edge cases.
- Error handling and failure modes.
- Test coverage and test quality.
- Comment and documentation quality.
- UX/API compatibility and migration risk.
- Security/privacy/performance when relevant.
- Scope creep and simplification.

## 4. Validation Mode

When validating behavior:

1. Determine the claimed fix or feature.
2. Check base/main for old behavior if practical.
3. Check feature branch for new behavior.
4. Run E2E/manual reproduction only if environment supports it.
5. Clearly separate verified facts from assumptions.

## 5. Synthesize

Group findings by severity:

- **Blocking**: must fix before merge.
- **Important**: should fix soon.
- **Nit/optional**: not merge-blocking.
- **Questions**: need author clarification.

## 6. Optional Fixes

If asked to fix findings from this review run:

- Implement only high-confidence, in-scope fixes.
- Do not rewrite the PR unnecessarily.
- Rerun validation and summarize remaining findings.

If asked to address existing GitHub review comments or reply to reviewer threads before pushing, use `address-pr-review-comments` instead.

## 7. Output

Return review decision, findings, evidence, changed files if fixes were made, validation results, and suggested PR comment.
