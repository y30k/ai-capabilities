# Delivery Board Management Workflow

## 1. Confirm Scope

- Identify the board/project URL, Jira board/project, repo set, milestone/sprint, labels/components, or saved filter.
- Confirm whether the user wants a read-only report, proposed updates, or authorized mutations.
- Confirm the relationship source of truth: tracker issue links/sub-issues/project relationship fields/Jira links.

If relationship data cannot be read, report that readiness is uncertain and ask whether to continue with a fallback.

## 2. Discover Board Schema

For GitHub:

- Check `gh auth status`.
- Identify project owner, number, fields, item types, views, and current items.
- Inspect target repos for linked issues/PRs, issue templates, labels, milestones, and relationship support.

For Jira:

- Identify project keys, boards, sprints, issue types, statuses, priorities, components, versions, and link types.

For any tracker, capture which fields mean status, priority, repo/system, type, assignee, milestone, and relationship.

## 3. Normalize Items

Create an internal table:

```markdown
| Item | Repo/System | Type | Status | Assignee | Priority | Blocked By | Blocks | Validation Ready? | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
```

An item is implementation-ready only when:

- all blocker relationships point to done/closed/accepted items or waived external dependencies
- acceptance criteria are testable
- owning repo/system is clear
- required design/test inputs are linked or embedded
- required environment/secrets/manual signoffs are available or not needed
- no competing canonical item is unresolved

## 4. Audit the Board

Look for:

- blocked items without blocker relationships
- items marked ready but blocked by open dependencies
- cycles in `blocks`/`blocked by` links
- duplicate or competing items
- cross-repo dependencies missing target repo ownership
- stale in-progress items, abandoned PRs, or missing assignees
- stories too large for one implementation slice
- missing validation, acceptance criteria, or PRD/design links
- labels pretending to be dependency truth

## 5. Prioritize Next Work

Build a next-ready queue:

1. Unblocked foundational items that unblock the most downstream work.
2. Risk-reducing spikes with dependent implementation waiting.
3. Contract/schema/API work before UI or integration dependents.
4. Small independent items that can complete without increasing merge conflict risk.
5. Work with known validation commands before work with missing gates.

Do not recommend coding blocked items. If every item is blocked, recommend the smallest action to remove a blocker.

## 6. Apply Updates Safely

Before mutations, show proposed changes and wait unless authorized.

Safe updates include:

- status corrections based on closed/open relationships
- adding missing tracker-native links
- moving duplicates to canonical items
- adding missing PRD/design/test links to item bodies
- setting repo/system/type/priority fields
- adding comments that explain decisions or ask owners for missing info

Do not close, delete, or reassign contentious work without explicit approval.

## 7. Report

```markdown
## Delivery Board Review

**Board**: {url/filter}
**Mode**: read-only | proposed updates | updated

### Next Unblocked Work
| Rank | Item | Repo/System | Why Ready | Validation | Downstream Unblocked |
| --- | --- | --- | --- | --- | --- |

### Blocked Work
| Item | Blocked By | Needed Action |
| --- | --- | --- |

### Hygiene Findings
- {duplicate, missing relationship, stale item, cycle, unclear AC}

### Handoff to Implementation
Use `implement-prd-stories` on: {item/ref or queue}
```
