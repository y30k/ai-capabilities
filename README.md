# AI Capabilities

A project-local collection of reusable AI-agent skills. Each skill is a self-contained folder under `skills/` with a `SKILL.md` manifest and optional supporting references.

The repository now organizes its skills around an **AI Development Life Cycle (AI-DLC)**: workspace readiness, discovery/PRD, technical design, test strategy, work-item decomposition, board readiness, implementation, production readiness, change-request submission with CI/CD verification, review, review-comment remediation, integration, release, observation, and feedback.

See [`docs/ai-dlc.md`](docs/ai-dlc.md) for the full process, rationale, phase order, gates, and skill handoffs.

## Repository Layout

```text
docs/
  ai-dlc.md          # canonical AI-DLC process documentation
skills/
  <skill-name>/
    SKILL.md
    agents/openai.yaml
    references/        # optional, loaded as needed
    LICENSE.txt        # present when skill content is adapted from licensed sources
```

Local agent state and working skills under `.pi/` are intentionally ignored by git.

## AI-DLC Quick Start

When you do not know which skill should run next, use `run-ai-dlc` first. It routes work to the right phase, gate, and artifact.

For a new feature that needs a PRD, the recommended order is:

```text
agent-smoke-test
→ create-interactive-prd
→ create-technical-design
→ create-test-strategy
→ create-prd-work-items
→ manage-delivery-board
→ implement-prd-stories
→ check-production-readiness
→ submit-change-request
→ review-pull-request
→ address-pr-review-comments, if reviewers request changes
→ submit-change-request, to monitor updated CI when needed
→ resolve-merge-conflicts, if needed
→ submit-change-request, to refresh integration CI when needed
→ release
→ observe-release
→ maintainer-standup / manage-github-issues / improve-code-health
```

Small approved changes can use `develop-feature` or `fix-github-issue` directly, then `check-production-readiness` before `submit-change-request` and review. Larger or ambiguous work should move through the full PRD/design/test/work-item path before coding.

## Generated Documentation Convention

When a skill creates plans, PRDs, review reports, implementation notes, story tracking, standup briefs, readiness scratchpads, release observations, or other durable documentation, write it under the repository-root `docs/` directory. Do not use agent-specific state directories for generated documentation.

Examples:

- PRDs: `docs/prds/{feature}.prd.md`
- Technical designs: `docs/technical-designs/{feature}.md`
- Test strategies: `docs/test-strategies/{feature}.md`
- PRD work-item drafts/reports: `docs/prd-work-items/{feature}.md`
- Delivery-board reports: `docs/delivery-board/{project-or-date}.md`
- Feature plans: `docs/develop-feature/{slug}/implementation-plan.md`
- GitHub issue findings: `docs/github-issues/{issue}/findings.md`
- PRD implementation tracking: `docs/implement-prd-stories/{story}.md`
- Change-request submission notes: `docs/submit-change-request/{pr-or-branch}.md`
- PR review-response notes: `docs/address-pr-review-comments/{pr-number}.md`
- Release observations: `docs/release-observations/{version-or-date}.md`
- AI-DLC lifecycle plans: `docs/ai-dlc/{topic}.md`

## Skill Groups

### Repository-original and AI-DLC lifecycle skills

These skills were created from scratch for this repository and related y30k/Capelry projects. They include the skills that fill the AI-DLC gaps between PRD approval and coding, between validated implementation and PR review, plus the post-release observation loop.

Current repository-original skills:

- `address-pr-review-comments` — process unresolved GitHub review threads, implement and validate in-scope fixes, stage and commit, reply on each original thread with what changed and why plus commit/validation evidence, push normally, resolve fully addressed threads, then paginate all threads and repeat for newly arrived feedback; a direct request authorizes this default sequence unless a user or repository policy requires an approval checkpoint.
- `check-production-readiness` — strict fail-closed pre-submission review for the exact staged change, including mandatory gate discovery, authorized P0/P1/P2 fixes, performance readiness, baseline handling, and READY/CONDITIONALLY READY/NOT READY verdict discipline.
- `create-technical-design` — approved PRD/spec to implementation-ready technical design, ADRs, contracts, rollout/rollback, observability, and risks.
- `create-test-strategy` — requirements/design/work items to acceptance, regression, integration, performance, security, accessibility, and release validation matrix.
- `create-prd-work-items` — approved PRD/design to deduped, dependency-linked GitHub/Jira work items with tracker-native relationships.
- `design-polished-web-ui` — design, implement, visually iterate, and validate polished responsive web UI using design artifacts, existing components, inspiration sources, and FOSS visual/a11y tooling.
- `manage-delivery-board` — project-board inspection, blocked/unblocked queue management, stale-item cleanup, duplicate detection, and implementation handoff.
- `observe-release` — post-release health verification, rollout/watch/rollback recommendation, production learning, and follow-up issue capture.
- `run-ai-dlc` — lifecycle router for choosing the right skill, gate, and artifact at each AI-DLC phase.
- `submit-change-request` — verify and commit the exact production-readiness source/tree identity, push a branch, create or update a PR/MR by default, support explicit fast-track direct-to-default as a non-default exception, and monitor connected CI/CD across common providers.

### Workflow-inspired coding-agent skills

These skills were inspired by workflows from [coleam00/Archon](https://github.com/coleam00/Archon), which is MIT licensed. They were rewritten as portable AI-agent skills rather than external workflow-runner definitions. They do not require Archon to run.

Current workflow-inspired skills:

- `agent-smoke-test` — portable capability checks for coding agents.
- `create-agent-workflow` — design reusable agent workflows.
- `create-interactive-prd` — planning-only interactive PRD creation.
- `develop-feature` — plan-gated feature implementation for approved smaller features or specs.
- `fix-github-issue` — selectable-rigor GitHub issue fixing.
- `implement-prd-stories` — implement approved, unblocked stories only in the current repository by default; validate and stage each story, apply the tracker's actual completion status, and move newly unblocked dependency-linked stories to Ready across repositories only after Done is genuinely satisfied.
- `improve-code-health` — architecture review and safe refactoring.
- `maintainer-standup` — maintainer status briefing.
- `manage-github-issues` — create, dedupe, and triage issues.
- `release` — release preparation and execution with release-mechanics-specific integrity gates.
- `remotion-generate` — Remotion composition generation.
- `resolve-merge-conflicts` — safe merge conflict resolution.
- `review-pull-request` — adaptive/comprehensive PR review that posts clear findings on the PR/MR when possible.

## Planning vs. Coding Boundaries

Planning, design, requirements, board-management, and release-observation skills should stop at reviewable artifacts or explicitly authorized tracker changes. Coding skills should require explicit approval before source-code changes when they consume plans, PRDs, generated requirements, or tracker items.

Examples:

- `create-interactive-prd` creates and validates a PRD, then stops for user review.
- `create-technical-design` turns an approved PRD into a technical handoff, then stops for approval.
- `create-test-strategy` defines validation gates before implementation.
- `create-prd-work-items` creates or updates tracker stories only after permission.
- `manage-delivery-board` identifies the next unblocked work item.
- `implement-prd-stories` starts after work-item approval, keeps technical changes in the current repository unless explicitly authorized otherwise, stages validated story changes, applies tracker-accurate completion semantics, and performs cross-repository dependency-driven Ready transitions only from verified Done.
- `check-production-readiness` reviews the exact staged change before initial submission or fast track and hands READY or CONDITIONALLY READY evidence to `submit-change-request`; fast track requires READY.
- `submit-change-request` commits, pushes, creates/updates PRs or MRs, and monitors CI/CD only with authorization; direct-to-default fast track is non-default and requires explicit fast-track/bypass-PR wording.
- `address-pr-review-comments` excludes resolved threads from remediation, posts traceable what/why/commit/validation replies, implements in-scope fixes, and resolves fully addressed threads after verified delivery; it reports completion only after a final all-pages query at the exact PR head finds zero unresolved threads, while a direct request authorizes staging, commit, replies, normal push, and resolution unless approval is explicitly required.
- `observe-release` verifies health and captures follow-up work after release; it should not rollback or mutate production without explicit authorization.

## Using These Skills

Point your coding agent at the relevant `skills/<name>/SKILL.md`, or copy/symlink skills into the agent's supported skill directory.

For agents that understand project-local Agent Skills, this repository can be used directly from the `skills/` directory.

Recommended entry points:

- Use `skills/run-ai-dlc/SKILL.md` for lifecycle routing and end-to-end planning.
- Use `skills/create-interactive-prd/SKILL.md` for new product discovery and PRDs.
- Use `skills/create-technical-design/SKILL.md`, `skills/create-test-strategy/SKILL.md`, and `skills/create-prd-work-items/SKILL.md` after PRD approval.
- Use `skills/manage-delivery-board/SKILL.md` before implementation sessions that depend on GitHub Projects, GitHub Issues, or Jira.
- Use `skills/design-polished-web-ui/SKILL.md` when building, polishing, or visually iterating responsive web UI.
- Use `skills/check-production-readiness/SKILL.md` on the exact staged change before initial PR/MR submission or fast track; fast track requires READY.
- Use `skills/submit-change-request/SKILL.md` after READY or CONDITIONALLY READY to open a PR/MR and watch CI/CD, or after focused review remediation or conflict resolution to update an existing PR/MR.
- Use `skills/address-pr-review-comments/SKILL.md` after PR reviewers leave requested changes or threaded feedback to address.
- Use `skills/observe-release/SKILL.md` after release or deployment.

## Attribution

Several skills in this repository were inspired by workflow ideas and structure from:

- Repository: [coleam00/Archon](https://github.com/coleam00/Archon)
- License: MIT
- Copyright: Cole Medin

The adapted skills in this repository are portable skill documents and supporting references, not vendored Archon workflow files.
