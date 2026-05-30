# Address PR Review Comments Workflow

## 1. Discover PR Context

- Confirm PR number or URL. If missing, infer from the current branch with `gh pr status` or ask.
- Ensure the working tree is clean or protect unrelated local changes before checkout/editing.
- Fetch PR metadata:

```bash
PR="<number-or-url>"
gh pr view "$PR" --json number,title,url,headRefName,baseRefName,reviewDecision,isDraft,mergeStateStatus,comments,reviews,files,statusCheckRollup
```

- Check out the PR branch with `gh pr checkout "$PR"` unless already on the correct branch.

## 2. Fetch Review Threads

Prefer review-thread data over flattened comments so replies go to the right place.

```bash
OWNER="<owner>"
REPO="<repo>"
PR_NUMBER="<number>"
gh api graphql \
  -F owner="$OWNER" \
  -F repo="$REPO" \
  -F number="$PR_NUMBER" \
  -f query='query($owner:String!,$repo:String!,$number:Int!){ repository(owner:$owner,name:$repo){ pullRequest(number:$number){ reviewThreads(first:100){ nodes{ id isResolved isOutdated path line originalLine diffSide comments(first:50){ nodes{ id author{ login } body createdAt url } } } pageInfo{ hasNextPage endCursor } } } } }'
```

If there are more than 100 threads, paginate before triage. Also inspect top-level PR comments and review summaries because reviewers sometimes leave required changes outside threads.

## 3. Triage Every Comment

Create a compact table before editing:

| Thread/comment | Reviewer ask | Disposition | Planned change | Validation |
| --- | --- | --- | --- | --- |
| URL or thread ID | What must change | fix / answer / stale / duplicate / defer / blocked | File/symbol or response | Test/check/manual validation |

Rules:

- Treat unresolved `CHANGES_REQUESTED` feedback as blocking unless clearly stale or out of scope.
- Do not ignore outdated threads; verify whether the issue still exists.
- Merge duplicate comments into one code change but reply to each relevant thread.
- Ask the user before declining, deferring, or expanding scope beyond the PR.

## 4. Implement Safely

- Edit only files needed to satisfy approved review feedback.
- Keep changes smaller than a rewrite unless reviewers requested the rewrite.
- Preserve PR intent and avoid introducing unrelated cleanup.
- Track which files/lines correspond to each thread for accurate replies.

Stop and ask if:

- Feedback conflicts with requirements or other reviewer feedback.
- A requested fix needs product/design decisions.
- Validation failure implies broader scope.
- The branch needs a rebase, force-push, or destructive operation.

## 5. Validate

Run the smallest reliable validation first, then broader checks when relevant:

- Formatter/linter for touched files.
- Unit/integration tests related to changed behavior.
- Build/typecheck if API/type contracts changed.
- Manual or reproduction checks for UI/behavior comments.

Record exact commands and outcomes. If a check cannot run, explain why and what would be needed.

## 6. Reply Before Push

Reply on each original thread before pushing the commit. Use concise, factual language:

```text
Addressed locally by <specific change>. Validation: <command/result>. Pushing this in the next commit.
```

For answers without code changes:

```text
Good question — <answer>. I did not change code because <reason>. Validation/context: <evidence>.
```

For deferred or blocked feedback:

```text
I did not change this in this PR because <reason>. Suggested follow-up: <issue/task>, pending owner confirmation.
```

Post a thread reply with GitHub GraphQL:

```bash
THREAD_ID="<thread-id>"
REPLY_BODY="<reply body>"
gh api graphql \
  -F threadId="$THREAD_ID" \
  -f body="$REPLY_BODY" \
  -f query='mutation($threadId:ID!,$body:String!){ addPullRequestReviewThreadReply(input:{pullRequestReviewThreadId:$threadId,body:$body}){ comment{ id url } } }'
```

Use `gh pr comment <pr> --body '<summary>'` only for top-level feedback or a final summary that does not belong to a specific thread.

Do not mark threads resolved unless explicitly authorized. If authorized, only resolve threads after the fix or answer is complete and the reply has been posted.

## 7. Commit and Push

Before committing:

```bash
git status --short
git diff --check
git diff
```

Then commit only intended files:

```bash
git add <intended files>
git commit -m "fix: address PR review comments"
git push
```

If push fails because the branch moved, fetch and inspect before rebasing or merging. Never force-push without explicit authorization.

## 8. Final Report

Return:

- PR URL and pushed commit hash.
- Thread replies posted, with URLs if available.
- Files changed.
- Validation commands and results.
- Any unresolved, deferred, blocked, or user-decision items.
- Whether another review pass is recommended.
