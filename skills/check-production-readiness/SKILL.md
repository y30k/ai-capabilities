---
name: check-production-readiness
description: Perform a strict, fail-closed production-readiness review of the exact staged change before initial PR/MR submission or an explicit direct-to-default fast track. Use when asked to prepare changes for submission, inspect every staged file and hunk, discover and run mandatory build, test, security, and performance gates, classify P0/P1/P2 blockers, verify candidate hygiene, or, when explicitly requested, fix and stage only blocker hunks. Refuse READY while pre-submission gates, regressions, unsafe staged/unstaged overlap, out-of-scope changes, or material uncertainty remain.
---

# Check Production Readiness

Treat readiness as fail-closed. The default verdict is **NOT READY** until the staged candidate proves otherwise.

## Candidate scope

Start by inspecting staged, unstaged, and untracked state. If nothing is staged, stop and ask the user to stage the intended candidate or define an explicit alternate scope. If any path has both staged and unstaged changes, stop before editing or staging it; ask the user to resolve the overlap, or obtain explicit approval for a patch-staging plan that preserves every pre-existing unstaged hunk. Never discard, overwrite, or silently absorb work outside the candidate. For a non-Git project, ask for the equivalent candidate artifact and isolation procedure.

Treat only the staged set as the candidate. Keep unstaged and untracked work out of scope except when checking candidate hygiene and overlap safety. Record the source commit and deterministic staged tree ID so `submit-change-request` can prove it is committing the exact reviewed candidate.

## Read local references first

Read [references/repo-readiness-sources.md](references/repo-readiness-sources.md) while discovering repository gates and candidate-isolation commands. Read [references/templates.md](references/templates.md) only when producing a persisted scratchpad or structured final handoff.

## Discover mandatory gates before validating

Do not guess what counts as production-ready submission. Determine the repo's actual mandatory gates from its automation and docs before running the gauntlet.

Look for the smallest command set that faithfully covers:
- tests required for merge or release
- build, compile, bundle, package, or deploy-dry-run checks
- lint, typecheck, format, static analysis, schema, migration, contract, or security checks
- browser, accessibility, visual, device, performance, load, benchmark, bundle-budget, or SLO checks when defined
- external gates that require secrets, hardware, network access, staging URLs, dashboards, or human signoff

Classify every mandatory gate as **pre-submission** or **normal-submission-created**. Pre-submission gates must run now. Required automation that cannot exist for the exact candidate until `submit-change-request` commits, pushes a feature branch, or creates/updates the PR/MR must be named explicitly and handed off; it is pending evidence, not silently waived.

If the mandatory gate set or classification is unclear, stop and ask. Unknown mandatory gates mean the candidate is **NOT READY**.

## Make performance first-class

Always assess whether the staged changes can affect application performance: latency, throughput, startup, render time, bundle size, memory, CPU, I/O, database/query volume, queue/batch duration, cost, or resource limits.

Use existing repo baselines, budgets, benchmarks, SLOs, and dashboards as the source of truth. Document a reusable measurement path, and create or persist it only when authorized, so future runs can compare results. If a performance-sensitive change has no usable baseline, establish read-only evidence or an authorized minimal repeatable baseline before declaring readiness:
- choose metrics and inputs that match the changed user or operator path
- run the smallest reliable repo-appropriate measurement locally, or name the blocked external measurement
- record command, environment, dataset/input, iterations, metric values, and comparison target
- when baseline persistence is authorized, stage an update to the repo's accepted baseline artifact; otherwise report the intended artifact or required handoff-only waiver and remain **NOT READY**

Do not invent universal thresholds. When evidence shows avoidable performance cost, improve and remeasure only when fixes are authorized; otherwise report the proposed fix and remain **NOT READY**. Do not lower budgets, bless slower baselines, or regenerate performance snapshots blindly.

## Workflow

1. Confirm the candidate has staged files.
2. Discover mandatory validation, release, and performance gates; classify each as pre-submission or normal-submission-created automation.
3. Record the source commit and staged tree ID, then inspect the staged file list, diff stat, and each per-file staged diff.
4. Review every staged file and every hunk for P0, P1, and P2 issues, including performance regressions and missing/stale baselines.
5. Propose scoped fixes for every P0, P1, or P2 issue; modify files only when the user's request authorizes fixes.
6. When fixes are authorized, stage only the correction hunks and reinspect cached and working-tree diffs to prove no pre-existing unstaged hunk was absorbed. Otherwise, report the blockers and remain **NOT READY** without editing or staging.
7. Restart the staged review from the top because the candidate changed.
8. Use targeted validation only as a fast feedback loop while fixing issues.
9. Once the staged review is clean, run the full mandatory pre-submission gauntlet and record every named normal-submission-created automation gate.
10. If any gate fails, fix and stage the problem only when authorized, then restart from staged review; otherwise report the failure and remain **NOT READY**.
11. If a performance baseline is missing for a performance-sensitive change, gather read-only evidence when possible. Persist or stage a baseline only when authorized; otherwise report the required baseline or waiver decision and remain **NOT READY**.
12. Finish only when all strict verdict criteria below are satisfied.

## Severity bar

Use this default bar:

- **P0** — catastrophic ship blocker
  - broken build, deploy, startup, migration, or rollback path
  - data loss, corruption, or irreversible state risk
  - auth, permission, or security bypass
  - public contract break that makes the release unsafe
  - deterministic failing mandatory gate
  - severe performance regression that can cause outage, timeout, data backlog, or runaway cost

- **P1** — severe release-blocking regression
  - clear break in a primary workflow
  - high-confidence incorrect behavior with real-user or operator impact
  - broken accessibility, responsive, device, or API behavior on a key path
  - performance regression on a key path against an existing baseline, budget, SLO, or accepted expectation
  - avoidable resource waste on a key path with clear user, operator, capacity, or cost impact
  - flaky or missing coverage for a risky change in release scope
  - CI-relevant failure likely to block merge or destroy release confidence

- **P2** — meaningful readiness issue that should still be fixed before production
  - confusing or misleading UX defect in changed scope
  - missing edge-case handling or unsafe fallback
  - stale docs, snapshots, baselines, schemas, manifests, or tests needed to keep shipped behavior honest
  - missing initial performance baseline for a performance-sensitive change when measurement is feasible
  - temporary instrumentation, debug residue, shortcut logic, or local-only assumption that should not ship

Ignore P3 and taste-only issues unless the user asks for broader polish. Do not pad the patch with unrelated cleanup.

## Strict review rules

While reviewing the staged set:
- inspect every staged file and every diff hunk; do not spot-check
- treat uncertainty as blocking until disproven
- trace changed behavior end to end through code, tests, configs, schemas, migrations, docs, and operations when relevant
- trace performance-sensitive hot paths through caching, batching, database access, network calls, rendering, startup, concurrency, and resource cleanup when relevant
- prefer fixing the product issue over weakening or deleting the test
- do not disable checks, mute assertions, regenerate snapshots/baselines blindly, or lower thresholds just to get green
- treat unexplained flakiness or noisy measurements as readiness problems until explained
- when fixes are authorized, remove debug logs, TODO shipping hacks, commented-out code, temporary flags, and local-only assumptions from release scope; otherwise report them as blockers
- check rollback, destructive actions, partial-write paths, caching, concurrency, and out-of-order behavior when touched
- review auth, secrets, and authorization boundaries aggressively when touched
- review accessibility, focus management, theming, responsive behavior, and device-specific paths on touched UI surfaces when relevant
- keep fixes within the candidate scope; avoid unrelated refactors
- do not commit unless the user explicitly asks

## Validation policy

Targeted tests are optional helpers. They never replace the full readiness gauntlet.

Before declaring readiness:
- run the repo's exact mandatory pre-submission wrapper commands when possible
- mirror the union of relevant CI or release gates locally when possible
- prefer a local command set that is equal to or stricter than post-submission CI
- run mandatory performance gates and compare against known baselines, budgets, or SLOs
- establish and record an initial baseline for performance-sensitive changes that lack one
- identify every feature-branch-push or PR/MR-created automation gate for `submit-change-request`
- rerun the full pre-submission gauntlet after the last fix, even if earlier subsets already passed

A mandatory gate that only exists after committing/pushing the exact candidate to a feature branch or creating/updating its PR/MR may remain pending only when its workflow or status context is known and `submit-change-request` will monitor it. Record it under normal-submission-created automation and use **CONDITIONALLY READY**. This exception never applies to direct-to-default fast track.

For any other mandatory external gate that cannot run because of missing credentials, services, devices, staging URLs, dashboards, or access:
- name the blocked gate explicitly
- name the missing prerequisite explicitly
- surface the blocked state as soon as it is discovered
- do not claim READY or CONDITIONALLY READY unless the gate passes or the user or release owner explicitly waives it

This skill has no generic standing waivers. Only repo docs, release-owner direction, or an explicit user waiver for the current run can waive a mandatory gate.

## Feed back missed failures

If a later PR, branch promotion, deployment, monitoring, or CI failure exposes a gap this skill did not catch:
- fix and stage the product correction first when authorized
- rerun readiness until the staged candidate is green again
- record a concise recommended skill improvement in the handoff
- modify this skill package only when the user explicitly asks to update it

## Final verdict rules

Use these rules strictly:

- **READY**
  - all mandatory gates are known and classified
  - all mandatory pre-submission local and external gates passed, were repo-approved-equivalent locally, or were explicitly waived
  - no normal-submission-created automation gate remains pending
  - performance-sensitive changes have passing gates or a durable recorded baseline, or an explicit handoff-only baseline waiver, with no unresolved regression
  - no P0, P1, or P2 issues remain
  - no unstaged tracked changes or equivalent out-of-scope candidate changes, and no generated validation artifacts remain

- **NOT READY**
  - any mandatory gate failed, is unknown, or cannot be classified
  - any mandatory pre-submission external gate is blocked without explicit waiver
  - any unresolved performance regression, required missing baseline, or unresolved baseline persistence decision remains
  - any P0, P1, or P2 issue remains
  - any unstaged tracked change or equivalent out-of-scope candidate change, or generated validation artifact remains

- **CONDITIONALLY READY**
  - all READY criteria hold except that clearly named feature-branch-push or PR/MR-created automation remains pending for `submit-change-request`
  - do not use this for default-branch-push automation, organizational signoffs, unknown gates, unresolved performance baselines, failed checks, or as a softer synonym for READY
  - never use CONDITIONALLY READY for direct-to-default fast track; every pending gate requires an explicit named waiver

## Candidate hygiene

By the end:
- all intended corrections must be staged
- no unstaged tracked changes or equivalent out-of-scope candidate changes may remain
- no validation artifacts created by this run should be left untracked
- the final staged diff should reflect exactly what will be submitted

## Example requests

- "Do a strict production-readiness pass on the staged changes."
- "Review the staged diff file by file, fix any P0/P1/P2 issues, stage the fixes, and run all required gates."
- "Treat this staged change as the PR candidate and fail closed until mandatory pre-submission checks and performance evidence are satisfied."
- "Get this staged change production-ready before I submit the PR."

## Handoff

After a **READY** or **CONDITIONALLY READY** verdict, hand the source commit, staged tree ID, exact staged candidate, verdict, validation evidence, and named normal-submission-created automation gates to `submit-change-request`. Do not commit, push, create a PR/MR, or fast-track from this skill.

## Documentation Output

Write requested readiness scratchpads and reports under `docs/check-production-readiness/` or another user-specified path under `docs/`. Include them in the candidate only when explicitly intended; otherwise remove artifacts created by the run without touching pre-existing files. Never store generated documentation in agent-state directories.
