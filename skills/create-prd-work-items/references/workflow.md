# PRD Work Item Creation Workflow

## 1. Confirm Inputs

Collect:

- PRD/spec path or pasted content.
- Optional technical design and test strategy paths.
- Tracker target: GitHub Project URL, org/user project number, Jira board/project, or explicit repo issue tracker.
- Target organization and repositories, including cross-repo dependencies.
- Permission mode: `draft-only`, `ask-before-posting`, or `authorized-to-post`.

If the PRD is not approved or still has scope-changing open questions, stop and ask whether to proceed with draft-only planning.

## 2. Discover Tracker Capabilities

Do not assume fields or relationship support. Inspect them first.

For GitHub:

- Check auth: `gh auth status`.
- Identify owner, project number, and project fields from the URL.
- Inspect project fields and current items, for example with `gh project view` and `gh project item-list` when available.
- Search target repos and the org for existing issues/PRs with overlapping terms.
- Discover relationship support before mutation: issue forms/templates, sub-issues, task lists, linked issues, project fields, and available GraphQL mutations.

For Jira:

- Identify project key, issue types, components, labels, versions, statuses, priorities, and link types.
- Inspect existing epics/stories/tasks and issue links with available CLI/API/MCP tools.

If relationship fields/link types cannot be discovered, create a draft and ask how dependencies should be represented. Do not encode dependencies only as labels or plain text unless the user explicitly waives tracker-native relationships for this run.

## 3. Extract Work from the PRD

Read the PRD and optional design/test strategy. Extract:

- epics or milestones from major capabilities
- implementation stories small enough for one focused coding slice
- spikes for unknowns that block reliable implementation
- cross-repo tasks and external dependencies
- acceptance criteria and validation commands/checks
- non-goals to avoid accidental work creation

Each story should have exactly one primary owning repo/system. Create separate linked items for cross-repo work instead of one vague umbrella item.

## 4. Dedupe and Enrich Existing Work

Before creating anything:

- Search by title keywords, domain nouns, user flows, component names, API names, labels/components, and PRD terminology.
- Include open project items, open repo issues, relevant closed/recent issues, and competing proposals.
- Classify matches as `same`, `overlapping`, `competing`, `dependency`, `duplicate`, or `unrelated`.
- For `same` or canonical `overlapping` work, update or comment on the existing item rather than creating a new item.
- For `competing` work, link the relationship and ask for a product decision before creating duplicate scope.

## 5. Draft Item Records

Use tracker-native fields where possible. Draft each item with:

```markdown
Title: [{repo or area}] {verb-led story title}
Type: Epic | Story | Task | Spike | External dependency
Owning repo/system: {owner/repo or external system}
PRD/design refs: {paths or URLs}
User value: {why this matters}
Implementation notes: {codebase-grounded hints, not full code}
Acceptance criteria:
- [ ] {observable pass/fail behavior}
Validation:
- {test/command/manual check}
Relationships:
- parent: {item/ref or none}
- blocks: {item/ref list}
- blocked by: {item/ref list}
- relates to: {item/ref list}
Priority rationale: {why now based on dependency graph and risk}
Labels/components: {area/type only, not blockers}
```

Keep issues self-contained enough that `implement-prd-stories` can implement one unblocked item without rereading the entire PRD, while still linking to the PRD as source of truth.

## 6. Build Dependency Graph and Priority

Create a dependency graph:

- Edge direction: `A blocks B` means A should be completed before B.
- Start with items with no unresolved blockers.
- Put discovery spikes before work they de-risk.
- Put schema/contracts/migrations before API/UI dependents.
- Put cross-repo external dependencies in the graph, even when they are not in the current repo.
- Detect cycles and ask for a decision instead of guessing.

Use priority/order fields for scheduling, but relationship links are the source of truth for dependency readiness.

## 7. Mutate the Tracker Safely

Before posting, show a concise creation/update/link plan and wait unless already authorized.

When mutating:

- Create or update canonical items first.
- Add items to the target project/board.
- Set fields such as status, type, priority, milestone, component, and owning repo.
- Add tracker-native relationships: parent/child, blocks/blocked-by, duplicate, relates-to, or Jira issue links.
- Verify by refetching the items and relationships after mutation.

If a relationship mutation fails, do not silently fall back to labels/body text. Report the failed relationship and ask whether to retry, use a different relationship type, or accept a temporary textual note.

## 8. Report

Return:

```markdown
## PRD Work Items Created/Updated

**Source**: {PRD/design}
**Tracker**: {project/board}
**Mode**: draft-only | posted | partially posted

| Item | Repo/System | Type | Action | Blocked By | Blocks | Priority | Next Step |
| --- | --- | --- | --- | --- | --- | --- | --- |

### Existing Items Reused
- {item} — {why canonical}

### Relationship or Posting Problems
- {problem} — {required user/tool action}

### Next Unblocked Work
1. {item/ref} — {why ready}
```
