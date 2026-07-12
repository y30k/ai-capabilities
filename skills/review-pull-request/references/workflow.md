# Pull Request Review Workflow

## Table of Contents

1. [Fetch Context](#1-fetch-context)
2. [Select Review Depth and Actions](#2-select-review-depth-and-actions)
3. [Review Lanes](#3-review-lanes)
4. [Validation Mode](#4-validation-mode)
5. [Synthesize Findings](#5-synthesize-findings)
6. [Publish Review Comments by Default](#6-publish-review-comments-by-default)
7. [Optional Fixes](#7-optional-fixes)
8. [Output](#8-output)

## 1. Fetch Context

- Identify PR/MR number, URL, or branch. If no PR/MR exists yet, hand the staged candidate to `check-production-readiness`, then `submit-change-request`.
- Read title, body, linked issues, changed files, diff, checks, comments, review threads, and project rules.
- Check current review state and whether comments have already been posted by this agent to avoid duplicates.
- Understand explicit scope and non-goals before flagging missing features.

Useful GitHub CLI context commands:

```bash
gh pr view "$PR" --json number,title,url,headRefName,baseRefName,author,isDraft,mergeStateStatus,reviewDecision,body,comments,reviews,files,statusCheckRollup
```

Use equivalent GitLab, Bitbucket, Azure DevOps, or other code-review-provider tools when GitHub is not the host.

## 2. Select Review Depth and Actions

Choose one review depth:

| Depth | Use when | Lanes |
| --- | --- | --- |
| smart | default | scope + risk classification + selected lanes |
| comprehensive | user asks for full or deep review | all lanes |
| maintainer | merge decision needed | direction, scope, user impact, review posture |
| validation | prove behavior changed correctly | base vs feature checks |

Choose actions separately:

| Action | Use when |
| --- | --- |
| return or draft findings | user requests read-only, draft, or validation-only output |
| publish review | a direct review request identifies the PR/MR and publication is not excluded |
| fix current-run findings | user explicitly requests high-confidence fixes from this review run |
| address existing GitHub threads | hand off to `address-pr-review-comments` to process unresolved threads, post traceable replies, push fixes, and resolve fully addressed feedback |

Output target default:

1. Post review feedback to the PR/MR itself when a PR/MR is identified and credentials/tooling allow it.
2. Fall back to the agent response when provider access, credentials, line mapping, repository policy, or user instructions prevent posting.
3. If posting fails, preserve the exact review body in the final response and include the failure reason.

Treat a direct request to review an identified PR/MR as authorization for one coherent review publication unless the user requests read-only, draft, or validation-only output. Never infer authorization to approve, request changes formally, edit code, or post multiple partial reviews from credentials alone.

Use a top-level review comment by default. Use inline comments only when line-level mapping is reliable and there are few focused findings. Use formal approve/request-changes only when the user explicitly authorizes that formal decision; repository convention may guide the proposed action but does not authorize it.

## 3. Review Lanes

Run the relevant lanes:

- Correctness and edge cases.
- Error handling and failure modes.
- Test coverage and test quality.
- Comment and documentation quality.
- UX/API compatibility and migration risk.
- Security/privacy/performance when relevant.
- CI/CD, deployment, release, and rollback impact when relevant.
- Scope creep and simplification.

Review only the PR/MR scope unless a broader issue is necessary to explain a finding.

## 4. Validation Mode

When validating behavior:

1. Determine the claimed fix or feature.
2. Check base/main for old behavior if practical.
3. Check feature branch for new behavior.
4. Run E2E/manual reproduction only if environment supports it.
5. Clearly separate verified facts from assumptions.

Record exact commands, branch/commit, and pass/fail/blocked outcomes.

## 5. Synthesize Findings

Group findings by severity:

- **Blocking**: must fix before merge.
- **Important**: should fix soon or before release, but may not block merge depending on owner risk tolerance.
- **Nit/optional**: small cleanup or clarity improvement; not merge-blocking.
- **Questions**: need author clarification.

Every actionable finding should include:

- what should change
- why it matters
- evidence from the diff, file/line, command output, or repo behavior
- suggested fix direction when clear

Avoid vague comments such as "consider improving this" without explaining impact.

## 6. Publish Review Comments by Default

Prepare one review body with this structure:

```markdown
## PR Review

**Decision**: approve | comment | request changes

### Findings

1. **{Severity}: {short title}**
   - Location: `{path}:{line}` or `{file/area}`
   - Issue: {what is wrong}
   - Why it matters: {risk/impact}
   - Suggested change: {specific direction}

### Validation
- `{command}` — {pass/fail/not run and why}

### Notes
- {assumptions, non-blocking observations, or follow-up}
```

Posting rules:

- Prefer `gh pr review <pr> --comment --body-file <file>` for a top-level GitHub review comment.
- Use `--request-changes` only when the user explicitly authorizes submitting a formal changes-requested review and clear blocking findings remain. Maintainer-decision mode or a merge recommendation alone produces a comment/recommendation, not authorization for this mutation.
- Use `--approve` only when the user explicitly authorizes submitting a formal approval and no blocking findings remain.
- For GitLab/other providers, use the provider CLI/API equivalent for a merge request note/review.
- Do not post duplicate comments. If an equivalent review body was already posted, update locally and report instead of spamming.
- Do not publish secrets, private logs, or sensitive vulnerability details; summarize safely and use the repository's private security process when appropriate.

If posting is unavailable or fails, return the review body in the agent response with:

```markdown
Could not post directly to the PR/MR because: {reason}. Review content follows.
```

## 7. Optional Fixes

If asked to fix findings from this review run:

- Implement only high-confidence, in-scope fixes.
- Do not rewrite the PR unnecessarily.
- Rerun focused validation and summarize remaining findings.
- Use `submit-change-request` to commit, push, and monitor the update; passing or explicitly waived updated required CI/CD completes readiness confirmation without a separate final production-readiness phase.

If asked to address existing GitHub review comments or reply to reviewer threads before pushing, use `address-pr-review-comments` instead.

## 8. Output

Return a concise final response with:

- PR/MR URL.
- Whether review comments were posted to the PR/MR; include the comment/review URL if available.
- Review decision and finding counts by severity.
- Validation commands and results.
- If posting failed, the full review body and the failure reason.
- Suggested next skill: `address-pr-review-comments`, `submit-change-request`, or no action.
