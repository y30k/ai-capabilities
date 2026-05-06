# AI Capabilities

A project-local collection of reusable AI-agent skills. Each skill is a self-contained folder under `skills/` with a `SKILL.md` manifest and optional supporting references.

## Repository Layout

```text
skills/
  <skill-name>/
    SKILL.md
    agents/openai.yaml
    references/        # optional, loaded as needed
    LICENSE.txt        # present when skill content is adapted from licensed sources
```

Local agent state and working skills under `.pi/` are intentionally ignored by git.

## Generated Documentation Convention

When a skill creates plans, PRDs, review reports, implementation notes, story tracking, standup briefs, readiness scratchpads, or other durable documentation, write it under the repository-root `docs/` directory. Do not use agent-specific state directories for generated documentation.

Examples:

- PRDs: `docs/prds/{feature}.prd.md`
- Feature plans: `docs/develop-feature/{slug}/implementation-plan.md`
- GitHub issue findings: `docs/github-issues/{issue}/findings.md`
- PRD implementation tracking: `docs/prd-implementations/{prd-slug}/stories.md`

## Skill Groups

### Original skills

These skills were created from scratch for this repository and related y30k/Capelry projects.

Current original skills:

- `check-production-readiness` — strict fail-closed release-candidate review for staged changes, including mandatory gate discovery, P0/P1/P2 fixes, performance readiness, baseline handling, and final READY/NOT READY verdict discipline.

Add future original skills here as they are developed.

### Workflow-inspired coding-agent skills

These skills were inspired by workflows from [coleam00/Archon](https://github.com/coleam00/Archon), which is MIT licensed. They were rewritten as portable AI-agent skills rather than external workflow-runner definitions. They do not require Archon to run.

Current workflow-inspired skills:

- `agent-smoke-test` — portable capability checks for coding agents
- `create-agent-workflow` — design reusable agent workflows
- `create-interactive-prd` — planning-only interactive PRD creation
- `develop-feature` — plan-gated feature implementation
- `fix-github-issue` — selectable-rigor GitHub issue fixing
- `implement-prd-stories` — implement approved PRDs story by story
- `improve-code-health` — architecture review and safe refactoring
- `maintainer-standup` — maintainer status briefing
- `manage-github-issues` — create, dedupe, and triage issues
- `release` — gated release preparation and execution
- `remotion-generate` — Remotion composition generation
- `resolve-merge-conflicts` — safe merge conflict resolution
- `review-pull-request` — adaptive/comprehensive PR review

## Planning vs. Coding Boundaries

Planning/design/requirements skills should stop at reviewable artifacts. Coding skills should require explicit approval before source-code changes when they consume plans, PRDs, or generated requirements.

Examples:

- `create-interactive-prd` creates and validates a PRD, then stops for user review.
- `implement-prd-stories` starts after PRD approval and implements small verified stories.

## Using These Skills

Point your coding agent at the relevant `skills/<name>/SKILL.md`, or copy/symlink skills into the agent's supported skill directory.

For agents that understand project-local Agent Skills, this repository can be used directly from the `skills/` directory.

## Attribution

Several skills in this repository were inspired by workflow ideas and structure from:

- Repository: [coleam00/Archon](https://github.com/coleam00/Archon)
- License: MIT
- Copyright: Cole Medin

The adapted skills in this repository are portable skill documents and supporting references, not vendored Archon workflow files.
