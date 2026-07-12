# AI Development Life Cycle (AI-DLC)

AI-DLC is this repository's operating model for AI-assisted software delivery. It combines reusable agent skills, explicit artifacts, human approval gates, validation evidence, CI/CD feedback, review discipline, release readiness, production observation, and backlog learning into one lifecycle.

Use AI-DLC when you want an AI coding agent to move safely from an idea or issue to reviewed, validated, shipped, and observed software without skipping the handoffs that make software delivery reliable.

If you are unsure which skill to use next, start with `run-ai-dlc`. It is the lifecycle router for choosing the right phase, skill, gate, and input artifact.

## Why AI-DLC Is Valuable

AI agents can create code quickly, but speed without lifecycle discipline creates familiar SDLC failure modes faster: unclear requirements, unreviewed design choices, missing tests, blocked dependencies, untracked work, brittle CI, review churn, unsafe releases, and no production feedback loop.

AI-DLC addresses that by making each transition explicit:

- **Intent before implementation** — clarify problem, scope, success, and non-goals before coding large or ambiguous work.
- **Design before decomposition** — turn approved requirements into architecture, contracts, rollout, rollback, observability, and risk decisions before tickets are created.
- **Validation before code and review** — plan test strategy before implementation, then run fail-closed production readiness on the exact staged change before PR/MR submission.
- **Dependency-aware delivery** — use tracker-native relationships so agents only implement unblocked work, then propagate verified Done/Ready transitions across repository boundaries without editing other repositories.
- **Small, approved slices** — implement one ready story or fix at a time in the current repository, validate and stage it, and mark tracked technical work Done before moving on.
- **Reviewable submissions** — submit only an exact staged candidate that passed production readiness, create or update a PR/MR by default, and watch connected CI/CD before review. Direct-to-default fast track is a non-default exception that requires explicit wording and READY evidence.
- **Reviewer feedback closure** — process only unresolved threads, reply where each concern was raised with what changed and why plus commit/validation evidence, push fixes, resolve fully addressed threads, and recheck automation.
- **Fail-closed readiness** — before submission, require all pre-submission build, test, security, performance, and external gates to pass or be explicitly waived; name feature-branch-push or PR/MR-created automation for `submit-change-request` rather than pretending it passed.
- **Release is not the end** — observe rollout health, incidents, telemetry gaps, and user/operator feedback, then feed learnings back into issues, PRDs, or code-health work.

## How AI-DLC Builds on SDLC Evolution

AI-DLC is not a replacement for decades of software delivery practice. It is a practical adaptation of SDLC, Agile, DevOps, secure SDLC, SRE, and AI governance ideas for AI-agent-assisted development.

| SDLC evolution | What it contributed | How AI-DLC applies it |
| --- | --- | --- |
| Traditional SDLC | Structured phases such as planning, design, implementation, testing, deployment, and maintenance. | Keeps visible phases and exit gates so agents do not jump from request to code to release without evidence. |
| Waterfall and phase-gate methods | Clear handoffs, approval points, and traceable artifacts. | Uses approval gates for PRDs, technical design, test strategy, tracker items, implementation, readiness, submission, review, and release. |
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
   - Small approved bug or feature: `fix-github-issue` or `develop-feature` → `check-production-readiness` → `submit-change-request`.
   - Larger feature: PRD → design → test strategy → work items → board readiness → implementation → production readiness → submission.
   - Existing PR/MR: `review-pull-request`, then `address-pr-review-comments` to process unresolved threads, perform focused validation, post traceable replies, and resolve fully addressed feedback.
   - Approved reviewed change: `release` → `observe-release`.
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
| 5. Delivery board readiness | Find blocked/unblocked work, duplicates, stale items, relationship problems, and the next implementation-ready queue. | `manage-delivery-board` | Next-ready queue has no unresolved blockers |
| 6. Implementation | Implement one approved, unblocked slice at a time. For tracked PRD stories, keep technical changes in the current repo, validate and stage them, mark the story Done, then move newly unblocked dependents to Ready across repositories. | `implement-prd-stories`, `develop-feature`, `fix-github-issue`, specialty implementation skills | Slice validates; tracked story changes are staged, Done is verified, and cross-repository dependency readiness is refreshed |
| 7. Production readiness | Run strict fail-closed review of the exact staged change before external submission. | `check-production-readiness` | READY, or CONDITIONALLY READY with only named normal-submission-created automation pending |
| 8. Change request submission | Commit the ready candidate, push, create/update a PR/MR by default, and watch connected CI/CD. Explicit fast-track direct-to-default is a non-default exception. | `submit-change-request` | PR/MR exists, or explicit fast-track push is complete; required automation passed or is explicitly waived |
| 9. PR review | Review behavior, risk, tests, maintainability, and release impact; post clear PR/MR feedback when possible. | `review-pull-request` | Findings posted or documented and owner disposition clear |
| 10. PR review remediation | Process only unresolved review threads, address approved issues, validate and commit, reply with what changed and why plus commit/evidence, push, resolve fully addressed threads, and recheck automation. | `address-pr-review-comments`, `submit-change-request` | Fixes are validated and bound to the verified updated PR/MR head; addressed threads are resolved; required automation for that exact head passed or is explicitly waived |
| 11. Integration hygiene | Resolve merge/rebase conflicts, rerun all affected validation, and refresh existing-PR automation. | `resolve-merge-conflicts`, `submit-change-request` | Resolution is bound to the verified updated PR/MR head; required automation for that exact head passed or is explicitly waived |
| 12. Release | Handle versioning, changelog/release notes, tags, publishing, package distribution, or deployment ceremony with release-specific integrity checks. | `release` | Version/tag/publish/deploy complete |
| 13. Observe rollout | Verify staging/production health, SLOs, logs, metrics, dashboards, flags, incidents, rollback criteria, and user/operator feedback. | `observe-release` | Health state and follow-up work recorded |
| 14. Feedback and maintenance | Triage learnings, bugs, stale work, and maintainability findings back into the backlog. | `maintainer-standup`, `manage-github-issues`, `improve-code-health` | Learnings triaged into follow-up work |

## Core Principles

- **Use the smallest useful gate.** Lightweight changes do not need a full PRD. Large, ambiguous, risky, cross-repo, or product-shaping work should not jump directly to code.
- **Keep planning and coding separate.** Planning/design skills create reviewable artifacts. Coding skills require approved inputs and explicit permission before source-code edits when consuming plans, PRDs, or tracker items.
- **Ground technical claims in the repository.** Requirements, designs, and test strategies should cite actual files, APIs, schemas, tests, deployment behavior, and operational constraints when making technical assertions.
- **Use tracker-native relationships for dependency truth.** `blocks`, `blocked by`, `parent/child`, `duplicate`, and `related` should live in GitHub Projects, GitHub Issues, Jira links, or equivalent relationship fields where supported, not only in labels or prose.
- **Implement one approved, unblocked slice at a time.** Do not batch unrelated work or code items with unresolved blockers.
- **Make readiness and submission state explicit.** After implementation validation, run production readiness on the exact staged diff, then commit only that candidate, create or update a PR/MR by default, and record CI/CD state before review. Use direct-to-default fast track only when the user explicitly asks for that git-context path and readiness is READY.
- **Close reviewer feedback in the original thread.** Exclude resolved threads; for each unresolved concern, post a traceable disposition explaining what changed and why with commit/validation evidence, then resolve it only after the fix or answer is complete and delivered.
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
| `implement-prd-stories` | Approved, unblocked tracker work implemented in the current repo by default, with validated staging, verified Done transition, and cross-repository dependent-story Ready updates. | Staged Done story → `check-production-readiness`; newly unblocked items → Ready queue |
| `develop-feature` | Smaller approved features, existing plans/specs, app briefs, or direct implementation requests outside the full PRD flow. | Validated change → `check-production-readiness` |
| `fix-github-issue` | Issue-driven bug fixing, reproduction, investigation, planning, implementation, validation, or validation-only work. | Validated fix → `check-production-readiness` |
| `design-polished-web-ui` | Responsive web UI/UX implementation, polish, visual iteration, accessibility checks, and screenshot/Figma-informed changes. | Validated UI change → `check-production-readiness` |
| `remotion-generate` | Remotion video compositions, previews, renders, and troubleshooting. | Validated composition/render → `check-production-readiness` or project-specific handoff |
| `check-production-readiness` | Strict review of the exact staged candidate, mandatory pre-submission gate discovery, authorized P0/P1/P2 fixes, performance readiness, and verdict. | READY/CONDITIONALLY READY → `submit-change-request` |
| `submit-change-request` | Consume readiness evidence, commit/push/create-or-update PR/MR, monitor CI/CD, or explicitly fast-track to default when requested. | PR/MR → `review-pull-request`; fast track → release/observation as appropriate |

### Readiness, submission, review, release, and operations

| Skill | Use for | Typical handoff |
| --- | --- | --- |
| `review-pull-request` | Adaptive, comprehensive, maintainer, or validation-focused PR/MR review, posting clear findings on the PR/MR when possible. | Findings → owner disposition or `address-pr-review-comments` |
| `address-pr-review-comments` | Unresolved review threads needing approved fixes, traceable what/why/commit/validation replies, push, verified resolution when fully addressed, and CI/CD recheck. | Resolved addressed threads and updated branch → `submit-change-request` monitor mode or another review pass |
| `resolve-merge-conflicts` | Merge, rebase, cherry-pick, or branch conflicts. | Resolved branch → focused validation → `submit-change-request` |
| `release` | Versioning, changelog, tag, package publish, deployment ceremony, release notes, and release-specific integrity checks. | Release/deploy → `observe-release` |
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
→ check-production-readiness
→ submit-change-request
→ review-pull-request
→ address-pr-review-comments, if reviewers request changes
→ submit-change-request, to monitor updated CI/CD when needed
→ resolve-merge-conflicts, if needed
→ submit-change-request, to refresh integration CI when needed
→ release
→ observe-release
→ maintainer-standup / manage-github-issues / improve-code-health
```

### Existing issue or bug

```text
fix-github-issue, smoke-first when reproduction is unclear
→ check-production-readiness
→ submit-change-request
→ review-pull-request
→ address-pr-review-comments, if reviewers request changes
→ submit-change-request, to monitor updated CI/CD when needed
→ release / observe-release, when shipping
```

### Small approved change

```text
develop-feature or fix-github-issue
→ validation
→ check-production-readiness
→ submit-change-request
→ review-pull-request, if PR/MR path
→ address-pr-review-comments, if reviewers request changes
```

Use the full PRD/design/work-item path if scope, risk, ambiguity, or dependency complexity grows.

### Explicit fast track

Fast track is a non-default `submit-change-request` path that bypasses PR/MR creation and pushes directly to the repository default branch.

Use it only when the user explicitly says a git-context phrase such as "fast track", "bypass PR", "skip pull request", "push directly to main/default", or "commit straight to main". Generic phrases like "push it" or "ship it" are not enough by themselves.

Fast track still requires:

- READY production-readiness evidence for the exact source commit and staged tree, with every otherwise pending gate explicitly waived
- a known default branch whose fetched tip matches the reviewed source commit
- repository policy allowing direct push
- no force push or history rewrite
- default-branch CI/CD monitoring after push
- release/observation handoff when production-bound

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
→ check-production-readiness
→ submit-change-request
→ review/release as appropriate
```

## Gate Checklist

Before moving between phases, verify the relevant gate:

- **Workspace gate:** tools work, repository state is understood, and safety constraints are clear.
- **PRD gate:** problem, users, evidence, success metrics, non-goals, open questions, and technical claims are documented and approved.
- **Design gate:** architecture, contracts, data, migrations, rollout, rollback, observability, security/privacy, and risks are addressed.
- **Test strategy gate:** requirements and risks map to acceptance criteria, commands, data, environments, nonfunctional checks, and release gates.
- **Tracker gate:** work items are deduped, owned by repo/system, small enough to implement, linked with relationships, and include validation.
- **Board readiness gate:** the next item has no unresolved blockers and has acceptance criteria plus validation.
- **Implementation gate:** each slice is implemented and validated before moving on; a tracked PRD story also has all story-owned changes staged, a verified Done transition, and a verified cross-repository sweep that moves every newly unblocked dependent to Ready.
- **Production gate:** the exact staged candidate has no unresolved P0/P1/P2 issue; mandatory pre-submission build, test, security, performance, and external gates pass; feature-branch-push or PR/MR-created automation is named for `submit-change-request`.
- **Change request gate:** READY or CONDITIONALLY READY evidence covers the initial source commit and staged tree, with READY required for fast track; the resulting commit tree matches, is pushed, and has a PR/MR unless explicit fast-track direct-to-default was requested and completed; required CI/CD checks are passing or explicitly waived. Failed, blocked, timed-out, or unknown required checks are triaged with evidence but block progression.
- **Review gate:** PR/MR findings are documented and dispositioned by an owner.
- **Review remediation gate:** only unresolved threads enter the worklist; addressed threads have traceable replies and verified resolution; all affected validation passes on the provider-verified exact updated PR/MR head; and required automation for that same head passes or is explicitly waived.
- **Integration gate:** conflicts are resolved, all affected validation is rerun, the resolution is bound to the verified updated PR/MR head, and required automation for that exact head passes or is explicitly waived.
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
7. Use `implement-prd-stories` to code that next unblocked item in the current repository.
8. On technical completion, stage the story changes, verify its Done transition, and move newly unblocked dependency-linked stories to Ready regardless of owning repository.

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
