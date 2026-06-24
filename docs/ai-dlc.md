# AI Development Life Cycle (AI-DLC)

AI-DLC is this repository's operating model for AI-assisted software delivery. It combines reusable agent skills, explicit artifacts, human approval gates, validation evidence, CI/CD feedback, review discipline, release readiness, production observation, and backlog learning into one lifecycle.

Use AI-DLC when you want an AI coding agent to move safely from an idea or issue to reviewed, validated, shipped, and observed software without skipping the handoffs that make software delivery reliable.

If you are unsure which skill to use next, start with `run-ai-dlc`. It is the lifecycle router for choosing the right phase, skill, gate, and input artifact.

## Why AI-DLC Is Valuable

AI agents can create code quickly, but speed without lifecycle discipline creates familiar SDLC failure modes faster: unclear requirements, unreviewed design choices, missing tests, blocked dependencies, untracked work, brittle CI, review churn, unsafe releases, and no production feedback loop.

AI-DLC addresses that by making each transition explicit:

- **Intent before implementation** — clarify problem, scope, success, and non-goals before coding large or ambiguous work.
- **Design before decomposition** — turn approved requirements into architecture, contracts, rollout, rollback, observability, and risk decisions before tickets are created.
- **Validation before code and review** — plan test strategy, acceptance checks, and nonfunctional gates before implementation and carry that evidence into PR/MR submission.
- **Dependency-aware delivery** — use tracker-native relationships so agents only implement unblocked work.
- **Small, approved slices** — implement one ready story or fix at a time and validate before moving on.
- **Reviewable submissions** — commit only the intended diff, create or update a PR/MR by default, and watch connected CI/CD before review/readiness decisions. Direct-to-default fast track is a non-default exception that requires explicit wording.
- **Reviewer feedback closure** — answer reviewer threads where they were raised, tie fixes to validation evidence, then push updates and recheck automation.
- **Fail-closed readiness** — treat production readiness as unproven until required local, CI/CD, security, performance, and external gates are known and passed or explicitly waived.
- **Release is not the end** — observe rollout health, incidents, telemetry gaps, and user/operator feedback, then feed learnings back into issues, PRDs, or code-health work.

## How AI-DLC Builds on SDLC Evolution

AI-DLC is not a replacement for decades of software delivery practice. It is a practical adaptation of SDLC, Agile, DevOps, secure SDLC, SRE, and AI governance ideas for AI-agent-assisted development.

| SDLC evolution | What it contributed | How AI-DLC applies it |
| --- | --- | --- |
| Traditional SDLC | Structured phases such as planning, design, implementation, testing, deployment, and maintenance. | Keeps visible phases and exit gates so agents do not jump from request to code to release without evidence. |
| Waterfall and phase-gate methods | Clear handoffs, approval points, and traceable artifacts. | Uses approval gates for PRDs, technical design, test strategy, tracker items, implementation, submission, readiness, and release. |
| Iterative, incremental, and spiral models | Smaller increments, risk discovery, and feedback loops instead of one large delivery bet. | Encourages one approved, unblocked slice at a time, with validation and rerouting when risk or blockers appear. |
| Agile | Customer collaboration, working software, adaptability, and regular feedback. | Supports lightweight paths for small approved changes while requiring stronger artifacts when ambiguity or risk grows. |
| DevOps and CI/CD | Continuous integration, delivery automation, cross-functional ownership, and faster feedback. | Adds `submit-change-request` to commit/push/create PRs or MRs, monitor CI/CD, and make automation state explicit. |
| Secure SDLC and NIST SSDF-style practices | Security and supply-chain risk reduction across design, implementation, release, and maintenance. | Requires security/privacy consideration in design, test strategy, production readiness, CI/CD triage, and follow-up work. |
| SRE and observability | SLOs, monitoring, rollback criteria, postmortems, and production learning. | Uses `observe-release` after release/deploy and feeds incidents, telemetry gaps, and user feedback back into the backlog. |
| AI lifecycle and AI governance | Human oversight, risk mapping, evaluation, deployment monitoring, and continuous improvement for AI-enabled systems. | Keeps humans in control of approvals and irreversible actions while using agents for repeatable planning, coding, review, validation, and monitoring work. |

The result is a lifecycle that preserves SDLC rigor while making AI agents useful: agents can accelerate each phase, but the phase gates keep ownership, evidence, and accountability visible.

## First-Time User Quick Start

1. **Start with the lifecycle router** when the next step is unclear:
   - Use `run-ai-dlc`.
   - Provide the current artifact: idea, PRD, issue, branch, PR/MR, release candidate, or deployment.
2. **Choose the smallest lifecycle path that fits the risk.**
   - Small approved bug or feature: `fix-github-issue` or `develop-feature` → validation → `submit-change-request`.
   - Larger feature: PRD → design → test strategy → work items → board readiness → implementation.
   - Existing PR/MR: `review-pull-request`, then `address-pr-review-comments` when reviewers request changes.
   - Release candidate: `check-production-readiness` → `release` → `observe-release`.
3. **Respect phase gates.**
   - Planning skills produce reviewable artifacts and stop for approval.
   - Coding skills require approved inputs and validation.
   - Submission/release/production actions require explicit authorization.
4. **Write generated documentation under `docs/`.**
   - Do not store durable plans or reports in `.pi/`, `.agents/`, `.codex/`, `.claude/`, or other agent-specific directories.

## Recommended AI-DLC Order

| Phase | Purpose | Primary skill | Exit gate |
| --- | --- | --- | --- |
| 0. Agent/workspace readiness | Verify tools, repository safety, and agent guardrails before meaningful work starts. | `agent-smoke-test` | Tools, repo safety, and guardrails understood |
| 1. Discovery and PRD | Turn an idea into a problem-first, evidence-backed, codebase-grounded PRD. | `create-interactive-prd` | Validated PRD approved |
| 2. Technical design | Convert approved requirements into architecture, contracts, rollout/rollback, observability, and risk decisions. | `create-technical-design` | Design/ADR/contracts approved |
| 3. Test strategy | Map requirements, design choices, and risks to acceptance, regression, integration, performance, security, accessibility, and release validation. | `create-test-strategy` | Validation matrix and gates approved |
| 4. Work-item decomposition | Create or update deduped, cross-repo GitHub/Jira work items with tracker-native relationships and validation. | `create-prd-work-items` | Work items created/approved with relationships and validation |
| 5. Board readiness | Find blocked/unblocked work, duplicates, stale items, relationship problems, and the next implementation-ready queue. | `manage-delivery-board` | Next-ready queue has no unresolved blockers |
| 6. Implementation | Implement one approved, unblocked tracker/local story or focused fix at a time; advance story status and refresh blocked-story readiness. | `implement-prd-stories`, `develop-feature`, `fix-github-issue`, specialty implementation skills | Slice implemented and validated; story status updated; newly unblocked work moved Ready |
| 7. Change request submission | Commit intended changes, push, create/update a PR/MR by default, and watch connected CI/CD. Explicit fast-track direct-to-default is a non-default exception. | `submit-change-request` | PR/MR exists, or explicit fast-track push is complete; required automation passed or is triaged |
| 8. PR review | Review behavior, risk, tests, maintainability, and release impact. | `review-pull-request` | Findings documented and owner disposition clear |
| 9. PR review remediation | Fetch unresolved review threads, address approved issues, reply on original threads, validate, commit, push, and recheck automation when needed. | `address-pr-review-comments` | Review threads replied to; fixes validated and pushed |
| 10. Integration hygiene | Resolve merge/rebase conflicts safely and rerun validation after integration changes. | `resolve-merge-conflicts` | Conflicts resolved and validation rerun |
| 11. Production readiness | Run strict fail-closed release-candidate review before exposing changes to users. | `check-production-readiness` | READY/CONDITIONALLY READY verdict |
| 12. Release | Handle versioning, changelog/release notes, tags, publishing, package distribution, or deployment ceremony. | `release` | Version/tag/publish/deploy complete |
| 13. Observe rollout | Verify staging/production health, SLOs, logs, metrics, dashboards, flags, incidents, rollback criteria, and user/operator feedback. | `observe-release` | Health state and follow-up work recorded |
| 14. Feedback and maintenance | Triage learnings, bugs, stale work, and maintainability findings back into the backlog. | `maintainer-standup`, `manage-github-issues`, `improve-code-health` | Learnings triaged into follow-up work |

## Core Principles

- **Use the smallest useful gate.** Lightweight changes do not need a full PRD. Large, ambiguous, risky, cross-repo, or product-shaping work should not jump directly to code.
- **Keep planning and coding separate.** Planning/design skills create reviewable artifacts. Coding skills require approved inputs and explicit permission before source-code edits when consuming plans, PRDs, or tracker items.
- **Ground technical claims in the repository.** Requirements, designs, and test strategies should cite actual files, APIs, schemas, tests, deployment behavior, and operational constraints when making technical assertions.
- **Use tracker-native relationships for dependency truth.** `blocks`, `blocked by`, `parent/child`, `duplicate`, and `related` should live in GitHub Projects, GitHub Issues, Jira links, or equivalent relationship fields where supported, not only in labels or prose.
- **Implement one approved, unblocked slice at a time.** Do not batch unrelated work or code items with unresolved blockers.
- **Make submission state explicit.** After validation, commit only the intended diff, create/update a PR/MR by default, and record CI/CD state before review or readiness. Use direct-to-default fast track only when the user explicitly asks for that git-context path.
- **Close reviewer feedback in the original thread.** When a PR/MR receives review comments, address each thread with a clear disposition, validation evidence, and a pushed fix or explicit owner decision.
- **Treat readiness as fail-closed.** Unknown required gates, blocked external checks, unexplained validation failures, and unresolved P0/P1/P2 issues mean not ready.
- **Observe after release.** A version tag, deploy, or package publish is incomplete until rollout health and follow-up work are captured.
- **Feed learnings back.** Incidents, user feedback, missing telemetry, technical debt, and product insights become issues, PRDs, code-health work, or future release tasks.

## Lifecycle Coverage by Skill

### Planning and design

| Skill | Use for | Typical handoff |
| --- | --- | --- |
| `create-interactive-prd` | New product ideas, ambiguous features, problem discovery, success metrics, non-goals, and codebase feasibility. | Approved PRD → `create-technical-design` |
| `create-technical-design` | Architecture, ADRs, contracts, data/migration notes, rollout/rollback, observability, security/privacy, and risk review. | Approved design → `create-test-strategy` |
| `create-test-strategy` | Acceptance, regression, integration, performance, accessibility, security, and release validation planning. | Validation matrix → `create-prd-work-items`, implementation, review, readiness |
| `create-prd-work-items` | PRD/design decomposition into deduped, dependency-linked GitHub/Jira work items. | Tracker items → `manage-delivery-board` |
| `manage-delivery-board` | Board hygiene, blocked/unblocked queue, dependency cleanup, duplicate detection, stale item triage, implementation handoff. | Next ready item → `implement-prd-stories` |

### Implementation and submission

| Skill | Use for | Typical handoff |
| --- | --- | --- |
| `implement-prd-stories` | Approved, unblocked PRD stories or tracker work items, one slice at a time, including routine status progression and post-completion blocked-story readiness sweeps. | Validated change → `submit-change-request`; newly unblocked stories → Ready queue |
| `develop-feature` | Smaller approved features, existing plans/specs, app briefs, or direct implementation requests outside the full PRD flow. | Validated change → `submit-change-request` |
| `fix-github-issue` | Issue-driven bug fixing, reproduction, investigation, planning, implementation, validation, or validation-only work. | Validated fix → `submit-change-request` |
| `design-polished-web-ui` | Responsive web UI/UX implementation, polish, visual iteration, accessibility checks, and screenshot/Figma-informed changes. | Validated UI change → `submit-change-request` |
| `remotion-generate` | Remotion video compositions, previews, renders, and troubleshooting. | Validated composition/render → `submit-change-request` or project-specific handoff |
| `submit-change-request` | Commit/push/create-or-update PR/MR, monitor CI/CD, or explicitly fast-track to default when requested. | PR/MR → `review-pull-request`; fast track → readiness/release/observation as appropriate |

### Review, readiness, release, and operations

| Skill | Use for | Typical handoff |
| --- | --- | --- |
| `review-pull-request` | Adaptive, comprehensive, maintainer, or validation-focused PR/MR review. | Findings → owner disposition or `address-pr-review-comments` |
| `address-pr-review-comments` | Existing review threads that need replies, approved fixes, validation, commit, push, and CI/CD recheck. | Updated branch → `submit-change-request` monitor mode or another review pass |
| `resolve-merge-conflicts` | Merge, rebase, cherry-pick, or branch conflicts. | Resolved branch → `submit-change-request` |
| `check-production-readiness` | Strict staged release-candidate review, mandatory gate discovery, P0/P1/P2 fixes, performance readiness, and final verdict. | READY/CONDITIONALLY READY → `release` |
| `release` | Versioning, changelog, tag, package publish, deployment ceremony, and release notes. | Release/deploy → `observe-release` |
| `observe-release` | Post-release or post-deployment health, SLOs, logs, dashboards, feature flags, incidents, rollback recommendation, and follow-up capture. | Learnings → backlog, PRD, issue, code health, hotfix |

### Support and maintenance

| Skill | Use for |
| --- | --- |
| `run-ai-dlc` | Lifecycle routing, end-to-end plans, phase/gate selection, and skill handoffs. |
| `agent-smoke-test` | Agent/workspace readiness and basic guardrail validation. |
| `maintainer-standup` | Repository status digests, recent commits, PRs, issues, review priorities, stale work, and next actions. |
| `manage-github-issues` | Issue creation, deduplication, backlog triage, stale-item digests, and issue hygiene without implementing fixes. |
| `improve-code-health` | Architecture review, safe refactoring, complexity reduction, dependency cleanup, and maintainability improvements. |
| `create-agent-workflow` | Reusable workflows when a recurring gap is process-level rather than a specialized skill. |
| `skill-creator` | New or updated skills when a recurring capability gap should become durable agent guidance. |

## Common Workflows

### New feature that needs product clarity

```text
agent-smoke-test, if workspace/agent readiness is unknown
→ create-interactive-prd
→ create-technical-design
→ create-test-strategy
→ create-prd-work-items
→ manage-delivery-board
→ implement-prd-stories
→ submit-change-request
→ review-pull-request
→ address-pr-review-comments, if reviewers request changes
→ submit-change-request, to monitor updated CI/CD when needed
→ resolve-merge-conflicts, if needed
→ check-production-readiness, when release-bound
→ release
→ observe-release
→ maintainer-standup / manage-github-issues / improve-code-health
```

### Existing issue or bug

```text
fix-github-issue, smoke-first when reproduction is unclear
→ submit-change-request
→ review-pull-request
→ address-pr-review-comments, if reviewers request changes
→ submit-change-request, to monitor updated CI/CD when needed
→ check-production-readiness, if release-bound
→ release / observe-release, when shipping
```

### Small approved change

```text
develop-feature or fix-github-issue
→ validation
→ submit-change-request
→ review-pull-request, if PR/MR path
→ address-pr-review-comments, if reviewers request changes
```

Use the full PRD/design/work-item path if scope, risk, ambiguity, or dependency complexity grows.

### Explicit fast track

Fast track is a non-default `submit-change-request` path that bypasses PR/MR creation and pushes directly to the repository default branch.

Use it only when the user explicitly says a git-context phrase such as "fast track", "bypass PR", "skip pull request", "push directly to main/default", or "commit straight to main". Generic phrases like "push it" or "ship it" are not enough by themselves.

Fast track still requires:

- exact intended diff and commit set
- known default branch
- repository policy allowing direct push
- passing validation or explicit named waivers
- no force push or history rewrite
- default-branch CI/CD monitoring after push
- readiness/release/observation handoff when production-bound

### Backlog, maintenance, and code health

```text
maintainer-standup
→ manage-delivery-board, when sequencing or dependency readiness matters
→ manage-github-issues, create-prd-work-items, improve-code-health, or implementation skills
```

For refactors or technical debt:

```text
improve-code-health
→ create-test-strategy, if validation is weak
→ develop-feature or implement-prd-stories, for approved changes
→ submit-change-request
→ review/readiness/release as appropriate
```

## Gate Checklist

Before moving between phases, verify the relevant gate:

- **Workspace gate:** tools work, repository state is understood, and safety constraints are clear.
- **PRD gate:** problem, users, evidence, success metrics, non-goals, open questions, and technical claims are documented and approved.
- **Design gate:** architecture, contracts, data, migrations, rollout, rollback, observability, security/privacy, and risks are addressed.
- **Test strategy gate:** requirements and risks map to acceptance criteria, commands, data, environments, nonfunctional checks, and release gates.
- **Tracker gate:** work items are deduped, owned by repo/system, small enough to implement, linked with relationships, and include validation.
- **Board readiness gate:** the next item has no unresolved blockers and has acceptance criteria plus validation.
- **Implementation gate:** each slice is implemented and validated before moving to the next slice.
- **Change request gate:** intended diff is committed and pushed; PR/MR exists unless explicit fast-track direct-to-default was requested and completed; required CI/CD checks are passing, explicitly waived, or clearly triaged with evidence.
- **Review gate:** PR/MR findings are documented and dispositioned by an owner.
- **Review remediation gate:** actionable review threads have replies on the original threads, fixes are validated, and the update commit is pushed; use `submit-change-request` to recheck CI/CD when needed.
- **Integration gate:** conflicts are resolved and validation is rerun.
- **Production gate:** mandatory build/test/security/performance/external gates are known and passed or explicitly waived.
- **Observation gate:** release health, rollout decision, incidents, missing telemetry, and follow-up work are recorded.
- **Feedback gate:** learnings are triaged into issues, PRDs, code-health work, or future releases.

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

## Documentation Outputs

Generated documentation should be written under the repository-root `docs/` directory, not under `.pi/`, `.agents/`, `.codex/`, `.claude/`, or other agent-specific state directories.

Common output locations:

- PRDs: `docs/prds/{feature}.prd.md`
- Technical designs: `docs/technical-designs/{feature}.md`
- Test strategies: `docs/test-strategies/{feature}.md`
- PRD work-item drafts/reports: `docs/prd-work-items/{feature}.md`
- Delivery-board reports: `docs/delivery-board/{project-or-date}.md`
- Feature plans: `docs/develop-feature/{slug}/implementation-plan.md`
- GitHub issue findings: `docs/github-issues/{issue}/findings.md`
- Implementation notes: `docs/implement-prd-stories/{story}.md`
- Change-request submission notes: `docs/submit-change-request/{pr-or-branch}.md`
- PR review reports: `docs/review-pull-request/{pr-number}.md`
- PR review-response notes: `docs/address-pr-review-comments/{pr-number}.md`
- Release notes or release scratchpads: `docs/release/{version}.md`
- Release observations: `docs/release-observations/{version-or-date}.md`
- AI-DLC lifecycle plans or assessments: `docs/ai-dlc/{topic}.md`

## When to Create More Process

If none of the existing skills match the needed phase, do not bury a new process in ad hoc chat.

- Use `create-agent-workflow` for a reusable but non-skill-specific runbook.
- Use `skill-creator` for a new specialized skill with triggers, workflow, gates, and references.

## Research Basis and Further Reading

This documentation is grounded in SDLC and AI-delivery research discovered through SearXNG and then adapted to this repository's skill set:

- IBM, [What is the Software Development Lifecycle (SDLC)?](https://www.ibm.com/think/topics/sdlc) — SDLC as a structured and iterative way to build, deploy, and maintain software.
- Atlassian, [Software development life cycle](https://www.atlassian.com/agile/software-development/sdlc) — common SDLC phases and methodology variants.
- Agile Manifesto, [Manifesto for Agile Software Development](https://agilemanifesto.org/) — working software, customer collaboration, and responding to change.
- Red Hat, [What is CI/CD?](https://www.redhat.com/en/topics/devops/what-is-ci-cd) — CI/CD as a way to streamline and accelerate the software development lifecycle.
- DORA, [Capabilities catalog](https://dora.dev/capabilities/) — research-backed capabilities that improve software delivery and operations performance.
- NIST, [Secure Software Development Framework](https://csrc.nist.gov/projects/ssdf) — secure development practices across the software lifecycle.
- NIST, [AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) — governance, mapping, measurement, and management of AI risk.
- IBM, [What is the AI lifecycle?](https://www.ibm.com/think/topics/ai-lifecycle) and Palo Alto Networks, [AI development lifecycle](https://www.paloaltonetworks.com/cyberpedia/ai-development-lifecycle) — iterative AI system planning, development, deployment, monitoring, and improvement.
- AWS DevOps Blog, [AI-Driven Development Life Cycle](https://aws.amazon.com/blogs/devops/ai-driven-development-life-cycle/) — AI-assisted software delivery with human oversight and structured workflow.
- Google SRE, [Site Reliability Engineering](https://sre.google/sre-book/table-of-contents/) — monitoring, release engineering, incident response, and production learning.
