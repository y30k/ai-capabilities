# Address PR Review Comments Workflow

## Table of Contents

1. [Discover PR Context](#1-discover-pr-context)
2. [Build an Unresolved-Thread Worklist](#2-build-an-unresolved-thread-worklist)
3. [Triage Every Unresolved Comment](#3-triage-every-unresolved-comment)
4. [Implement Safely](#4-implement-safely)
5. [Validate](#5-validate)
6. [Commit Locally Before Replying](#6-commit-locally-before-replying)
7. [Reply on Still-Unresolved Threads](#7-reply-on-still-unresolved-threads)
8. [Push](#8-push)
9. [Resolve Fully Addressed Threads](#9-resolve-fully-addressed-threads)
10. [Final Report](#10-final-report)

## 1. Discover PR Context

- Confirm PR number or URL. If missing, infer from the current branch with `gh pr status` or ask.
- Ensure the working tree is clean or protect unrelated local changes before checkout/editing.
- Fetch PR metadata:

```bash
PR="<number-or-url>"
gh pr view "$PR" --json number,title,url,headRefName,headRefOid,headRepository,headRepositoryOwner,baseRefName,reviewDecision,isDraft,mergeStateStatus,comments,reviews,files,statusCheckRollup
```

- Record the PR head repository owner/name, head ref, and provider-reported head OID. Identify the local remote whose URL matches that head repository; do not assume the configured upstream is the PR target.
- Discover any repository or organization policy that explicitly requires a confirmation checkpoint for commits, replies, normal PR-head pushes, or thread resolution. Do not invent a checkpoint when no such policy is present.
- Check out the PR branch with `gh pr checkout "$PR"` unless already on the correct branch.
- Treat the direct request to address review feedback as authorization for the default end-to-end sequence: scoped edits, validation, staging, commit, replies, normal non-force push to the existing PR head, and resolution of eligible threads. Do not add a confirmation pause unless the user requested one or repository/organization policy requires it.

## 2. Build an Unresolved-Thread Worklist

Prefer review-thread data over flattened comments so replies and resolution target the original discussion. GitHub returns both resolved and unresolved threads, so fetch every page for transport but immediately filter to `isResolved == false`. Resolved thread IDs must never enter the triage or implementation worklist.

```bash
OWNER="<owner>"
REPO="<repo>"
PR_NUMBER="<number>"
PAGE_JSON="$(gh api graphql \
  -F owner="$OWNER" \
  -F repo="$REPO" \
  -F number="$PR_NUMBER" \
  -f query='query($owner:String!,$repo:String!,$number:Int!){ repository(owner:$owner,name:$repo){ pullRequest(number:$number){ reviewThreads(first:100){ nodes{ id isResolved isOutdated viewerCanReply viewerCanResolve path line originalLine diffSide comments(first:100){ nodes{ id author{ login } body createdAt url } pageInfo{ hasNextPage endCursor } } } pageInfo{ hasNextPage endCursor } } } } }')"
jq -c '.data.repository.pullRequest.reviewThreads.nodes[] | select(.isResolved == false)' <<<"$PAGE_JSON"
jq '[.data.repository.pullRequest.reviewThreads.nodes[] | select(.isResolved == true)] | length' <<<"$PAGE_JSON"
jq -r '.data.repository.pullRequest.reviewThreads.pageInfo' <<<"$PAGE_JSON"
```

If the review-thread `pageInfo.hasNextPage` is true, rerun the query with an `$after: String` variable, pass `-F after="$END_CURSOR"`, and change the field to `reviewThreads(first:100, after:$after)`. Filter each page before combining it, continue until `hasNextPage` is false, and deduplicate by thread ID.

Before triage, fetch every comment in each unresolved worklist thread. When its nested `comments.pageInfo.hasNextPage` is true, continue that connection independently until false and deduplicate comment IDs:

```bash
THREAD_ID="<unresolved-thread-node-id>"
AFTER="<comments-end-cursor>"
COMMENTS_PAGE="$(gh api graphql \
  -F threadId="$THREAD_ID" \
  -F after="$AFTER" \
  -f query='query($threadId:ID!,$after:String){ node(id:$threadId){ ... on PullRequestReviewThread { id isResolved comments(first:100,after:$after){ nodes{ id author{ login } body createdAt url } pageInfo{ hasNextPage endCursor } } } } }')"
```

Do not decide disposition or resolution eligibility until the full unresolved-thread conversation, including its latest reviewer follow-ups, has been read. Record its latest comment ID with the worklist row. Record only the count of excluded resolved threads for the final report; do not reply to, implement changes for, or reopen them.

Recheck every worklist thread immediately before implementation, again before replying, and again before resolution:

```bash
THREAD_ID="<thread-node-id>"
gh api graphql \
  -F threadId="$THREAD_ID" \
  -f query='query($threadId:ID!){ node(id:$threadId){ ... on PullRequestReviewThread { id isResolved viewerCanReply viewerCanResolve path line comments(last:1){ nodes{ id url } } } } }'
```

If the query fails or does not return a boolean `isResolved`, do not act on the thread; report its state as unknown. If the returned latest comment ID differs from the worklist snapshot, fetch the new conversation, update the plan and validation as needed, and retriage before acting. If `isResolved` is true at any recheck, remove the thread from the active worklist and perform no reply or resolution mutation. If `viewerCanReply` or `viewerCanResolve` is false for an action the plan requires, leave the thread unresolved and report the permission blocker. If code was already prepared solely for that thread, stop and decide whether it remains independently justified before keeping it.

Build a separate non-thread worklist from independently actionable top-level PR comments and review summaries. Record source type, ID/URL, author, concern, current response state, and whether it duplicates a review thread. Do not use summary text to resurrect or duplicate a concern whose review thread is already resolved. Non-thread feedback has no review-thread resolution state: never pass it to `resolveReviewThread`, and report resolution as N/A.

## 3. Triage Every Unresolved Comment

Create a compact table from the unresolved-thread worklist before editing:

| Unresolved thread | Reviewer ask | Disposition | Planned change or answer and why | Validation | Resolution condition |
| --- | --- | --- | --- | --- | --- |
| URL and thread ID | Concise original concern | fix / answer / stale / duplicate / defer / blocked | File/symbol or response rationale | Test/check/manual evidence | push required / reply sufficient / leave unresolved |

Create a parallel table for actionable non-thread feedback:

| Comment/review | Reviewer ask | Disposition | Planned change or answer and why | Validation | Response plan |
| --- | --- | --- | --- | --- | --- |
| URL and ID | Concise original concern | fix / answer / stale / duplicate / defer / blocked | File/symbol or response rationale | Test/check/manual evidence | top-level response URL or pending |

Rules:

- Treat unresolved `CHANGES_REQUESTED` feedback as blocking unless clearly stale or out of scope.
- Do not ignore outdated but unresolved threads; verify against current code whether the issue still exists.
- Merge duplicate comments into one code change, but preserve one worklist row and one reply for every unresolved thread.
- Ask the user before declining, deferring, or expanding scope beyond the PR.
- Never create a row for a resolved thread. If a resolved thread contains useful context, use it only as historical evidence and do not act on it.

## 4. Implement Safely

- Edit only files needed to satisfy triaged in-scope review feedback.
- Keep changes smaller than a rewrite unless reviewers requested the rewrite.
- Preserve PR intent and avoid introducing unrelated cleanup.
- Track the original concern, affected files/symbols, implementation decision, rationale, validation evidence, and commit for each unresolved thread so its reply is independently auditable.

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

Record exact commands and outcomes. If a check cannot run, explain why and what would be needed. For review-driven fixes, this focused validation plus passing or explicitly waived updated required CI/CD is the readiness confirmation; do not run a separate final production-readiness phase.

Before committing or calling GitHub mutations, record one action plan containing the exact intended files, commit plan, still-unresolved thread IDs, actionable non-thread IDs/URLs, reply/response summary per item, explicit PR-head push target, and threads expected to become resolution-eligible. A direct request to address review comments authorizes commit, reply, normal push, and resolution by default, so present the plan for traceability and continue without waiting. Stop before sections 6–9 only when the user explicitly requested read-only, local-only, draft replies, or an approval checkpoint; repository or organization policy requires approval; or a destructive/exceptional action such as force-push, history rewrite, protection bypass, production mutation, review dismissal, or material scope expansion is needed.

## 6. Commit Locally Before Replying

When code changed, create the local commit before posting review-thread replies so each code-fix reply can cite a concrete short SHA. Do not push yet.

Before committing, snapshot and inspect both worktree and index:

```bash
git status --short
git diff --check
git diff
git diff --cached --name-only
git diff --cached
```

Stage the intended allowlist, then inspect the index again. If any unrelated pre-staged path or hunk remains, stop and obtain an isolation plan; a normal `git commit` commits the whole index.

```bash
git add -- path/to/file another/path
git diff --cached --name-only
git diff --cached
# Proceed only when the cached diff exactly matches the recorded commit allowlist.
git commit -m "fix: address PR review comments"
FULL_SHA="$(git rev-parse HEAD)"
SHORT_SHA="$(git rev-parse --short HEAD)"
```

When multiple comments are fixed by one commit, reuse the same short SHA. Keep the corresponding full SHA for ancestry verification. When multiple commits are needed, map each unresolved thread to both forms. For answer-only or verified-stale feedback, state why no code commit applies. For a duplicate, cite the canonical thread and its commit when one exists. Deferred or blocked feedback remains unresolved and must say why.

## 7. Reply on Still-Unresolved Threads

Recheck `isResolved` and `viewerCanReply` immediately before each reply. If the thread is now resolved, skip it without posting. If reply permission is unavailable, leave it unresolved and report the blocker. Otherwise reply on the original thread before pushing, and make the reply independently traceable. A reply that only says "done", "fixed", or gives a commit SHA is insufficient.

For a code fix:

```text
Disposition: Addressed — code fix
Original concern: <concise restatement of the reviewer ask>
What changed: <specific behavior and affected file/symbol>
Why this addresses it: <reason the implementation satisfies the concern and relevant trade-off>
Commit: <local-short-sha> (local at reply time; resolution requires verified push)
Validation: `<exact command>` — PASS (<relevant result>)
```

For an answer-only or verified-stale thread:

```text
Disposition: Addressed — answer | verified stale
Original concern: <concise restatement>
Answer / current state: <specific explanation>
Why no code change is needed: <reason supported by current code, requirement, or evidence>
Commit: N/A — no code change
Evidence: <file/symbol, command/result, issue/design link, or other concrete support>
```

For a duplicate:

```text
Disposition: Addressed — duplicate
Original concern: <concise restatement>
Canonical handling: <thread URL and what changed or was answered there>
Why this covers this thread: <specific overlap>
Commit: <short-sha or N/A>
Validation: <command/result or canonical evidence>
```

For deferred, blocked, disputed, or partial feedback:

```text
Disposition: Not addressed — deferred | blocked | disputed | partial
Original concern: <concise restatement>
Why it remains open: <specific reason>
Follow-up / owner action: <issue, decision, credential, or next step>
Resolution: Leaving this thread unresolved.
```

Post the reply and capture its ID and URL:

```bash
THREAD_ID="<thread-id>"
REPLY_BODY="<reply body>"
gh api graphql \
  -F threadId="$THREAD_ID" \
  -f body="$REPLY_BODY" \
  -f query='mutation($threadId:ID!,$body:String!){ addPullRequestReviewThreadReply(input:{pullRequestReviewThreadId:$threadId,body:$body}){ comment{ id url } } }'
```

After a successful thread reply, refresh the thread and compare all comment IDs added since the pre-reply snapshot. If the only new ID is the returned reply ID, make it the new snapshot. If any reviewer or bot comment also appeared, read it and retriage before push or resolution. This prevents your own reply from masking a concurrent follow-up.

For each actionable non-thread worklist item, post a mapped top-level response that links the original comment/review URL and uses the same disposition, what/why, commit, and validation fields as thread replies. Capture the response URL. A coherent summary may cover multiple items only when it maps each original URL/ID separately.

Use `gh pr comment <pr> --body '<summary>'` for these non-thread responses or a final summary. Do not resolve any thread in this section; non-thread items always have resolution N/A.

## 8. Push

After all required thread and non-thread responses are posted, push explicitly to the recorded PR head repository/ref:

```bash
HEAD_REMOTE="<remote-matching-pr-head-repository>"
HEAD_REF="<provider-reported-head-ref>"
git push "$HEAD_REMOTE" "HEAD:refs/heads/$HEAD_REF"
```

Refetch PR metadata and verify the provider-reported PR head, not merely the configured upstream. The provider head OID should equal local `HEAD`; if a concurrent commit is intentionally accepted, fetch the exact head ref and prove every cited commit is its ancestor before resolving:

```bash
PR_HEAD_OID="$(gh pr view "$PR" --json headRefOid --jq '.headRefOid')"
test "$(git rev-parse HEAD)" = "$PR_HEAD_OID"
CITED_SHA="<full-sha-corresponding-to-the-short-sha-in-the-reply>"
git merge-base --is-ancestor "$CITED_SHA" "$PR_HEAD_OID"
```

If push fails because the branch moved, fetch and inspect before any authorized rebase or merge. Never force-push without explicit authorization. If reconciliation rewrites a cited SHA, rerun affected validation and post a corrective response for every affected worklist item: recheck unresolved thread state and reply there, or link the original non-thread item from a mapped top-level response. Do this before any resolution:

```text
Tracking update: branch reconciliation rewrote the local commit cited above.
Pushed commit: <new-short-sha> (supersedes <old-short-sha>)
What changed and why: <specific outcome and rationale>
Validation: `<exact command>` — PASS (<relevant result>)
```

Apply the same post-reply refresh and concurrent-follow-up check from section 7 to every corrective thread reply, and capture every corrective non-thread response URL. Leave code-fix threads and duplicates that depend on commits unresolved until the push succeeds, every cited or superseding SHA is present on the PR branch, and any needed corrective reply is posted successfully without masking a newer comment.

If no code changes were needed, skip commit/push. Complete answer-only or verified-stale replies may proceed to resolution; deferred, blocked, disputed, and partial threads may not.

## 9. Resolve Fully Addressed Threads

Resolve an active worklist thread only when its current state is still unresolved, `viewerCanResolve` is true, its reply was posted successfully, and its disposition meets one of these conditions:

- **fix** — the change passed focused validation, and every SHA cited in its reply is present on the pushed PR branch or has a corrective reply naming the verified pushed replacement;
- **answer** — the reply fully answers the concern with concrete evidence;
- **stale** — current code or requirements prove the concern no longer applies, and the reply explains that evidence;
- **duplicate** — the reply links the canonical addressed thread, and any shared fix is pushed.

Never resolve deferred, blocked, disputed, partial, failed-validation, failed-reply, or failed-push threads. Recheck `isResolved` immediately before mutation; if another actor already resolved it, record an already-resolved no-op rather than mutating or claiming credit.

Resolve one eligible thread at a time and verify the returned state:

```bash
THREAD_ID="<thread-node-id>"
gh api graphql \
  -F threadId="$THREAD_ID" \
  -f query='mutation($threadId:ID!){ resolveReviewThread(input:{threadId:$threadId}){ thread{ id isResolved } } }'
```

Treat a missing thread, API error, or `isResolved != true` response as a failed resolution. Leave it in the unresolved report with the exact error and recovery action; do not claim success from mutation intent alone.

## 10. Final Report

Return the PR URL, verified PR head repository/ref/OID, and pushed commit hash or short SHA(s), or note that no code commit was needed. Include this per-thread ledger:

| Original thread | Reviewer and concern | Disposition | What changed or was answered, and why | Location | Commit | Validation/evidence | Reply | Verified resolution |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| URL + thread ID | `@reviewer` — concise ask | fix / answer / stale / duplicate / deferred / blocked | Specific outcome and rationale | File/symbol or N/A | Verified pushed SHA, superseding SHA, or N/A with reason | Exact command/result or evidence | Reply URL(s) | resolved / unresolved + reason / skipped-already-resolved / N/A |

Include a separate non-thread ledger:

| Original comment/review | Reviewer and concern | Disposition | What changed or was answered, and why | Commit | Validation/evidence | Response URL | Resolution |
| --- | --- | --- | --- | --- | --- | --- | --- |
| URL + ID | `@reviewer` — concise ask | fix / answer / stale / duplicate / deferred / blocked | Specific outcome and rationale | Verified pushed SHA or N/A | Exact command/result or evidence | URL or failure | N/A |

Also include:

- Count of resolved threads excluded before triage and any threads skipped because they became resolved during the run; do not claim those as addressed by this run.
- Files changed and exact validation commands/results.
- Current CI/CD status if available, or a `submit-change-request` handoff for update/CI monitoring.
- Every thread intentionally left unresolved, with its blocker, owner action, and next step.
- Whether another review pass is recommended.
