# AI Development Life Cycle Skill Map

## Phase Order

| Phase | Purpose | Primary Skill | Exit Gate |
| --- | --- | --- | --- |
| 0. Agent/workspace readiness | Verify tools, repo safety, and agent behavior | `agent-smoke-test` | Tooling and guardrails understood |
| 1. Discovery and PRD | Define problem, users, evidence, scope, and success | `create-interactive-prd` | Validated PRD approved by user |
| 2. Technical design | Convert approved requirements into architecture and contracts | `create-technical-design` | Design approved; open questions isolated |
| 3. Test strategy | Map requirements and risks to validation gates | `create-test-strategy` | Validation matrix/gates approved |
| 4. Work-item decomposition | Create deduped, dependency-linked tracker items with validation | `create-prd-work-items` | Items exist or draft is approved; relationships verified |
| 5. Delivery board readiness | Identify unblocked, implementation-ready work | `manage-delivery-board` | Next-ready queue has no unresolved blockers |
| 6. Implementation | Code one approved, unblocked slice at a time | `implement-prd-stories`, `develop-feature`, or `fix-github-issue` | Slice passes story validation |
| 7. PR review | Review risk, behavior, tests, and maintainability | `review-pull-request` | Findings documented and dispositioned |
| 8. PR review remediation | Address requested changes and reviewer threads | `address-pr-review-comments` | Thread replies posted; fixes validated and pushed |
| 9. Integration hygiene | Resolve branch/rebase/merge conflicts safely | `resolve-merge-conflicts` | Conflicts resolved and validation rerun |
| 10. Production readiness | Fail-closed staged release-candidate review | `check-production-readiness` | READY/CONDITIONALLY READY verdict |
| 11. Release | Version, changelog, tag, publish, and release | `release` | Release artifact/deploy complete |
| 12. Observe rollout | Verify production/staging health and capture learnings | `observe-release` | Healthy/watch/block/rollback decision recorded |
| 13. Feedback and maintenance | Feed issues, tech debt, and product learnings back into backlog | `maintainer-standup`, `manage-github-issues`, `improve-code-health` | Follow-up items triaged |

## Support Skills

- `create-agent-workflow` — create reusable process when a recurring gap is not skill-specific.
- `skill-creator` — create or update a durable skill for repeated specialized work.
- `review-pull-request` `fix-review-findings` mode — implement safe findings from a review run when thread replies are not required.
- `remotion-generate` — specialty implementation skill for Remotion video projects.

## Common Routing

### New feature idea

`create-interactive-prd` → `create-technical-design` → `create-test-strategy` → `create-prd-work-items` → `manage-delivery-board` → `implement-prd-stories` → `review-pull-request` → `address-pr-review-comments` if reviewers request changes → `check-production-readiness` → `release` → `observe-release`.

### Existing issue or bug

`fix-github-issue` in smoke-first mode when reproduction is unclear → `review-pull-request` → `address-pr-review-comments` if reviewers request changes → `check-production-readiness` if release candidate → `release`/`observe-release` when shipping.

### Small approved change

`develop-feature` or `fix-github-issue` → validation → `review-pull-request` → `address-pr-review-comments` if reviewers request changes.

### Backlog/project maintenance

`maintainer-standup` → `manage-delivery-board` → `manage-github-issues` or `create-prd-work-items` for follow-up.

### Refactor/technical debt

`improve-code-health` → `create-test-strategy` if validation is weak → `develop-feature`/`implement-prd-stories` for approved changes → review/review-remediation/readiness.

## Gate Checklist

Before moving phases, verify:

- **PRD gate**: problem, users, success, non-goals, and technical claims are documented and approved.
- **Design gate**: contracts, data, migration, rollout, rollback, observability, security/privacy, and risks are addressed.
- **Test strategy gate**: requirements and risks map to acceptance criteria, commands, data, environments, and nonfunctional checks.
- **Tracker gate**: work items are deduped, owned by repo/system, small enough, linked with relationships, and include validation.
- **Readiness gate**: next item has no unresolved blocker relationships and has acceptance criteria plus validation.
- **Implementation gate**: each slice validates before moving to the next.
- **Review gate**: findings are documented and dispositioned by owner.
- **Review remediation gate**: reviewer threads have replies, approved fixes are validated, and the update commit is pushed.
- **Production gate**: mandatory tests/build/security/performance/external gates are known and passed/waived.
- **Observation gate**: release health and follow-up work are recorded.

## Gap Handling

If none of the existing skills match the needed phase, do not bury new process in ad hoc chat. Use:

1. `create-agent-workflow` for a reusable but non-skill-specific runbook.
2. `skill-creator` for a new specialized skill with triggers, workflow, gates, and references.
