# Maintainer Standup Workflow

## 1. Gather Context

Use available tools only:

- `git status --short`, current branch, recent commits.
- Open PRs, review requests, failing checks, merge conflicts.
- Open issues, new comments, stale or high-priority items.
- Local maintainer notes if the project has them.

If `gh` or network access is unavailable, report the limitation and summarize local git state.

## 2. Synthesize

Prioritize by urgency and maintainer leverage:

1. Broken main, failing release, security, or data-loss risk.
2. PRs blocked on maintainer review.
3. Issues with fresh user impact.
4. Stale work needing nudge/closure.
5. Background cleanup.

## 3. Output

```markdown
# Maintainer Standup — {date}

## Top Priorities
1. {action} — {why now}

## Pull Requests
- {PR}: {status, blocker, recommended action}

## Issues
- {issue}: {status, recommended action}

## Local Repository
- Branch/status summary
- Uncommitted changes if any

## Suggested Next Actions
- [ ] {highest leverage action}
```

Optionally persist the brief under `.agents/maintainer-standup/briefs/` if the user wants history.
