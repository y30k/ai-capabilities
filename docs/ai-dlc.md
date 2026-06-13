# AI Development Life Cycle (AI-DLC)

This repository manages a set of reusable AI-agent skills that together form an AI Development Life Cycle (AI-DLC): a gated, artifact-driven process for taking work from initial readiness and discovery through implementation, PR review remediation, release, observation, and backlog feedback.

The AI-DLC is not meant to add ceremony for its own sake. It exists to keep AI-assisted development from skipping critical handoffs: requirements before design, design before tickets, validation before code, dependency checks before implementation, review before remediation, reviewer-thread replies before pushing fixes, review before release, and observation after shipping.

If you are unsure which skill to use, start with `run-ai-dlc`. It is the meta-skill that routes work to the right phase, gate, and artifact.

## Why This Process Exists

A review of the project-local skills originally staged in `.pi/skills/` and now managed from this repository's `skills/` directory found that the original set was strong in these areas:

- PRD creation
- GitHub issue fixing
- Feature implementation
- Pull request review
- Production readiness checks
- Release preparation and execution
- Maintenance digests and backlog triage

The main gaps were between PRD approval and coding, plus after release:

1. No dedicated technical design/ADR handoff after PRD approval.
2. PRD story creation was conflated with coding in `implement-prd-stories`.
3. No tracker-native PRD-to-stories workflow using GitHub Projects/Jira relationships.
4. No standalone test strategy/validation matrix before implementation.
5. No dependency-aware board management to select unblocked work.
6. No post-release observation/learning loop.
7. No AI-DLC orchestrator skill to route between all phases.

A follow-up review gap was also identified after the initial lifecycle work: existing PR review support could optionally implement safe fixes, but there was no dedicated workflow for reading unresolved PR review threads, addressing each issue, replying on the original threads, and pushing the update commit.

The current AI-DLC closes those gaps with dedicated skills for technical design, test strategy, work-item decomposition, delivery-board management, PR review-thread remediation, post-release observation, and lifecycle orchestration.

## Core Principles

- **Use the smallest useful gate.** Lightweight changes do not need a full PRD, but large or ambiguous work should not jump directly to code.
- **Keep planning and coding separate.** Planning/design skills create reviewable artifacts. Coding skills require approved inputs and explicit permission before source-code edits.
- **Ground technical claims in the repository.** Requirements, designs, and test strategies should cite actual files, APIs, schemas, tests, and deployment behavior when making technical assertions.
- **Use tracker-native relationships for delivery state.** `blocks`, `blocked by`, `parent/child`, `duplicate`, and `related` should live in GitHub Projects, GitHub Issues, or Jira relationship fields where supported, not only in labels or prose.
- **Implement one approved, unblocked slice at a time.** AI agents should not batch unrelated work or code items with unresolved dependency blockers.
- **Close reviewer feedback in the original thread.** When a PR receives review comments, address each thread with a clear disposition, validation evidence, and a pushed fix or explicit owner decision.
- **Treat release as unfinished until observed.** A version tag, deploy, or package publish is not the end of the lifecycle; rollout health and follow-up work must be captured.
- **Feed learnings back into the backlog.** Incidents, user feedback, missing telemetry, technical debt, and product learnings become issues, PRDs, or code-health work.

## Recommended AI-DLC Order

| Phase | Primary skill | Why this phase matters | Exit gate |
| --- | --- | --- | --- |
| 0. Agent/workspace readiness | `agent-smoke-test` | Verifies tools, repository safety, and guardrails before meaningful work starts. | Tools, repo safety, and guardrails understood |
| 1. Discovery and PRD | `create-interactive-prd` | Turns an idea into a problem-first, evidence-backed, codebase-grounded PRD. | Validated PRD approved |
| 2. Technical design | `create-technical-design` | Converts approved requirements into implementation-ready architecture, ADRs, contracts, rollout/rollback, observability, and risk decisions. | Design/ADR/contracts approved |
| 3. Test strategy | `create-test-strategy` | Maps requirements, design choices, and risks to acceptance, regression, integration, performance, security, accessibility, and release validation. | Validation matrix and gates approved |
| 4. Work-item decomposition | `create-prd-work-items` | Creates or updates deduped, cross-repo GitHub/Jira work items with tracker-native relationships and dependency-based priority. | Deduped tracker items created/approved with relationships and validation |
| 5. Board readiness | `manage-delivery-board` | Finds blocked and unblocked work, duplicates, stale items, relationship problems, and the next implementation-ready queue. | Next-ready queue has no unresolved blockers |
| 6. Implementation | `implement-prd-stories` | Implements one approved, unblocked tracker/local story at a time with validation after each slice. | One unblocked story implemented and validated |
| 7. PR review | `review-pull-request` | Reviews behavior, risks, tests, maintainability, and release impact before merge. | Findings documented and owner disposition clear |
| 8. PR review remediation | `address-pr-review-comments` | Fetches unresolved review threads, addresses approved issues, replies on original threads before pushing, then commits and pushes validated fixes. | Review threads replied to; fixes validated and pushed |
| 9. Integration hygiene | `resolve-merge-conflicts` | Resolves merge/rebase conflicts safely and reruns validation after integration changes. | Conflicts resolved and validation rerun |
| 10. Production readiness | `check-production-readiness` | Runs a strict, fail-closed staged release-candidate review before exposing changes to users. | READY/CONDITIONALLY READY verdict |
| 11. Release | `release` | Handles versioning, changelog/release notes, tags, publishing, and deployment ceremony with approval gates. | Version/tag/publish/deploy complete |
| 12. Observe rollout | `observe-release` | Verifies production or staging health, SLOs, logs, metrics, dashboards, flags, incidents, and rollback criteria. | Health state and follow-up work recorded |
| 13. Feedback/maintenance | `maintainer-standup`, `manage-github-issues`, `improve-code-health` | Triage learnings, bugs, stale work, and maintainability findings back into the backlog. | Learnings triaged back into backlog |

### Preferred Feature Flow

For a new feature that is large enough to need a PRD, use this sequence:

```text
agent-smoke-test
→ create-interactive-prd
→ create-technical-design
→ create-test-strategy
→ create-prd-work-items
→ manage-delivery-board
→ implement-prd-stories
→ review-pull-request
→ address-pr-review-comments, if reviewers request changes
→ resolve-merge-conflicts, if needed
→ check-production-readiness
→ release
→ observe-release
→ maintainer-standup / manage-github-issues / improve-code-health
```

Important ordering details:

- `create-technical-design` runs after PRD approval and before tracker decomposition so stories are based on an intentional architecture.
- `create-test-strategy` should run before or alongside work-item creation so every story carries acceptance criteria and validation.
- `create-prd-work-items` owns durable PRD-to-story decomposition; `implement-prd-stories` should not be the primary decomposition skill.
- `manage-delivery-board` runs before coding sessions to ensure the selected work is truly unblocked.
- `address-pr-review-comments` runs after review when feedback requires changes, so every reviewer thread gets a disposition before the fix commit is pushed.
- `observe-release` runs after release to close the loop with production evidence and follow-up items.

## Skills Added or Updated for AI-DLC

### Added skills

- `address-pr-review-comments` — addresses GitHub PR review comments end-to-end: fetches unresolved threads, triages each concern, implements approved fixes, validates, replies on the original threads before pushing, commits, pushes, and summarizes remaining follow-up.
- `create-technical-design` — converts an approved PRD/spec into an implementation-ready technical design, ADRs, interface contracts, data/migration notes, rollout/rollback plan, observability plan, and risk review.
- `create-prd-work-items` — converts an approved PRD/design into deduped, cross-repo GitHub/Jira work items with tracker-native relationships and dependency-based priority.
- `create-test-strategy` — converts requirements, designs, or work items into an acceptance, regression, integration, performance, security, accessibility, and release validation matrix.
- `manage-delivery-board` — inspects project boards to detect blocked/unblocked work, duplicates, stale items, relationship problems, unclear acceptance criteria, and the next-ready implementation queue.
- `observe-release` — verifies post-release health, rollout/watch/rollback recommendations, production learning, and follow-up issue capture.
- `run-ai-dlc` — routes between lifecycle phases, skills, gates, and artifacts so agents choose the right process instead of improvising.

### Updated skills

- `implement-prd-stories` now implements approved, unblocked tracker/local stories instead of being the primary PRD decomposition skill.
- `create-interactive-prd` now recommends `create-technical-design` → `create-test-strategy` → `create-prd-work-items` before implementation.
- `develop-feature`, `manage-github-issues`, `maintainer-standup`, and `release` now route to the new lifecycle skills where appropriate.

## Skill Importance and Coverage

| Skill | AI-DLC role | Why it is important | Typical handoff |
| --- | --- | --- | --- |
| `agent-smoke-test` | Phase 0 readiness | Verifies agent/tool behavior before major work and reduces accidental repository damage. | Move to discovery, planning, or direct small-fix work once tools and guardrails are understood. |
| `create-interactive-prd` | Phase 1 requirements | Provides a strong problem-first PRD workflow that validates user need, scope, success metrics, non-goals, and codebase feasibility before design. | After PRD approval, use `create-technical-design`, `create-test-strategy`, and `create-prd-work-items`. |
| `create-technical-design` | Phase 2 design | Bridges PRD approval to architecture, contracts, ADRs, data/migration choices, rollout, rollback, observability, security/privacy, and risks. | Use `create-test-strategy`, then `create-prd-work-items`. |
| `create-test-strategy` | Phase 3 validation planning | Creates the validation matrix and test gates before implementation so quality is designed into each story. | Feed validation into `create-prd-work-items`, `implement-prd-stories`, `review-pull-request`, and `check-production-readiness`. |
| `create-prd-work-items` | Phase 4 planning | Provides a dedicated PRD-to-GitHub/Jira story creation workflow and uses tracker relationships for dependencies. | Use `manage-delivery-board` to identify next-ready work. |
| `manage-delivery-board` | Phase 5 delivery planning | Maintains dependency-aware board hygiene and identifies blocked vs. unblocked implementation queues. | Use `implement-prd-stories` for the top approved, unblocked item. |
| `implement-prd-stories` | Phase 6 implementation | Codes only approved, unblocked work and validates one slice at a time. | Send changes to `review-pull-request`; update tracker/story state when authorized. |
| `develop-feature` | Phase 6 implementation | Handles smaller approved features outside the formal PRD flow and can route larger PRD work into the full lifecycle. | Validate, then prepare/review PR; use formal AI-DLC when scope grows. |
| `design-polished-web-ui` | Phase 6 specialty implementation | Improves web UI quality with design artifacts, existing components, visual iteration, responsive checks, copy reduction, and FOSS visual/a11y tooling. | Validate UI changes, then send through review/readiness as appropriate. |
| `fix-github-issue` | Phase 6 bug/issue implementation | Provides issue-driven bug fixing with reproduction, evidence, and appropriate rigor. | Validate fix, then review/readiness/release as appropriate. |
| `review-pull-request` | Phase 7 review | Covers adaptive, comprehensive, maintainer, and validation review before merge. | Use `address-pr-review-comments` when reviewers request changes; use readiness checks for release candidates. |
| `address-pr-review-comments` | Phase 8 review remediation | Closes the loop on PR feedback by fetching unresolved review threads, implementing approved fixes, replying on original threads before push, committing, pushing, and reporting remaining items. | Return to review/readiness once replies are posted and fixes are pushed. |
| `resolve-merge-conflicts` | Phase 9 integration | Resolves conflicts safely and ensures validation is rerun after integration changes. | Return to review/readiness once conflicts are resolved. |
| `check-production-readiness` | Phase 10 readiness | Provides a strict fail-closed staged-candidate readiness review with mandatory gate discovery, P0/P1/P2 fixes, performance readiness, baseline handling, and final verdict discipline. | Proceed to `release` only after READY or accepted CONDITIONAL readiness. |
| `release` | Phase 11 release | Handles gated release preparation and execution: repository state, versions, changelog, approval, commit/tag/release, and optional package distribution. | Use `observe-release` after release or deployment completes. |
| `observe-release` | Phase 12 observe/learn | Adds the missing post-release health check and feedback loop for metrics, logs, SLOs, incidents, flags, rollback criteria, and follow-up work. | Feed issues to `manage-github-issues`, PRDs to `create-interactive-prd`, technical debt to `improve-code-health`, or hotfixes to `release`. |
| `maintainer-standup` | Phase 13 maintenance | Produces repository/project digests for status, reviews, issues, stale work, and next actions. | Use `manage-delivery-board` when dependency-aware sequencing is needed. |
| `manage-github-issues` | Phase 13 backlog | Creates, dedupes, and triages issues; PRD story work belongs in `create-prd-work-items`. | Use `fix-github-issue` for coding; use `create-prd-work-items` for approved PRD story decomposition. |
| `improve-code-health` | Phase 13 code health | Supports architecture sweeps and safe refactoring paths based on maintainability findings. | Use `create-test-strategy` if validation is weak, then implementation/review/readiness skills. |
| `create-agent-workflow` | Support | Creates reusable workflows when a gap is process-level rather than tied to a durable skill. | Use when repeated process needs should become a runbook. |
| `skill-creator` | Support | Creates or updates durable skills when a recurring capability gap should be encoded for future agents. | Use after identifying a missing specialized skill; this may live outside this repository depending on the agent setup. |
| `run-ai-dlc` | Support/meta | Provides the lifecycle router and gate map for choosing the right skill, artifact, and next step. | Hands off to the phase-specific skill. |
| `remotion-generate` | Specialty implementation | Supports domain-specific Remotion video generation outside the general AI-DLC. | Use when the implementation domain is Remotion composition generation. |

## Tracker Guidance for PRD Stories

For PRD decomposition into GitHub Projects or Jira:

1. Use `create-prd-work-items` with the PRD path and project URL.
2. Search existing items before creating new ones.
3. Update canonical existing items when similar or competing work already exists.
4. Model `blocks`, `blocked by`, `parent/child`, `duplicate`, and `related` with tracker-native relationships, not labels or prose.
5. Use labels/tags only for implementation area, type, component, repo, or lifecycle metadata.
6. Use `manage-delivery-board` to identify the next unblocked work.
7. Use `implement-prd-stories` to code that next unblocked item.

This guidance matters because labels and issue-body prose are easy for agents to misread. Tracker-native relationships let board tooling and AI agents agree on the actual dependency graph.

## Gate Checklist

Before moving between phases, verify the relevant gate:

- **Workspace gate:** tools work, repository state is understood, and safety constraints are clear.
- **PRD gate:** problem, users, evidence, success metrics, non-goals, open questions, and technical claims are documented and approved.
- **Design gate:** architecture, contracts, data, migrations, rollout, rollback, observability, security/privacy, and risks are addressed.
- **Test strategy gate:** requirements and risks map to acceptance criteria, commands, data, environments, nonfunctional checks, and release gates.
- **Tracker gate:** work items are deduped, owned by repo/system, small enough to implement, linked with relationships, and include validation.
- **Board readiness gate:** the next item has no unresolved blockers and has acceptance criteria plus validation.
- **Implementation gate:** each slice is implemented and validated before moving to the next slice.
- **Review gate:** PR findings are documented and dispositioned by an owner.
- **Review remediation gate:** actionable review threads have replies on the original threads, fixes are validated, and the update commit is pushed.
- **Integration gate:** conflicts are resolved and validation is rerun.
- **Production gate:** mandatory build/test/security/performance/external gates are known and passed or explicitly waived.
- **Observation gate:** release health, rollout decision, incidents, missing telemetry, and follow-up work are recorded.
- **Feedback gate:** learnings are triaged into issues, PRDs, code-health work, or future releases.

## Common Routing Patterns

### New feature idea

Use the full lifecycle:

```text
create-interactive-prd
→ create-technical-design
→ create-test-strategy
→ create-prd-work-items
→ manage-delivery-board
→ implement-prd-stories
→ review-pull-request
→ address-pr-review-comments, if reviewers request changes
→ check-production-readiness
→ release
→ observe-release
```

### Existing issue or bug

Use `fix-github-issue` in smoke-first mode when reproduction is unclear, then `review-pull-request`, `address-pr-review-comments` if reviewers request changes, `check-production-readiness` if the fix is part of a release candidate, and `release`/`observe-release` when shipping.

### Small approved change

Use `develop-feature` or `fix-github-issue`, validate the change, then use `review-pull-request` and `address-pr-review-comments` as appropriate. Escalate to the full PRD/design/work-item path if scope or risk grows.

### Backlog or project maintenance

Use `maintainer-standup` for a digest, `manage-delivery-board` for blocked/unblocked sequencing, and `manage-github-issues` or `create-prd-work-items` for follow-up creation or cleanup.

### Refactor or technical debt

Use `improve-code-health`; add `create-test-strategy` if validation is weak; then use `develop-feature` or `implement-prd-stories` for approved changes, followed by review and readiness gates.

## Documentation Outputs

Generated documentation should be written under the repository-root `docs/` directory, not under `.pi/`, `.agents/`, `.codex/`, `.claude/`, or other agent-specific state directories.

Common output locations:

- PRDs: `docs/prds/{feature}.prd.md`
- Technical designs: `docs/technical-designs/{feature}.md`
- Test strategies: `docs/test-strategies/{feature}.md`
- PRD work-item drafts/reports: `docs/prd-work-items/{feature}.md`
- Delivery-board reports: `docs/delivery-board/{project-or-date}.md`
- Implementation notes: `docs/implement-prd-stories/{story}.md`
- PR review-response notes: `docs/address-pr-review-comments/{pr-number}.md`
- Release notes or release scratchpads: `docs/release/{version}.md`
- Release observations: `docs/release-observations/{version-or-date}.md`
- AI-DLC lifecycle plans or assessments: `docs/ai-dlc/{topic}.md`

## When to Create More Process

If none of the existing skills match the needed phase, do not bury a new process in ad hoc chat.

- Use `create-agent-workflow` for a reusable but non-skill-specific runbook.
- Use `skill-creator` for a new specialized skill with triggers, workflow, gates, and references.
