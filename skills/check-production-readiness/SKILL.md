---
name: check-production-readiness
description: Perform a strict, fail-closed production-readiness review for a staged release candidate in any project. Use when an agent must inspect every staged file and diff hunk, fix and stage P0/P1/P2 blockers, discover and run mandatory gates, assess performance, set baselines when none exist, and refuse READY while gates, regressions, unstaged tracked changes, or uncertainty remain.
---

# Check Production Readiness

Treat readiness as fail-closed. The default verdict is **NOT READY** until the staged candidate proves otherwise.

## Candidate scope

Start by checking for staged changes. If nothing is staged, stop and ask the user to stage the intended release candidate, or to define an explicit alternate candidate scope. If the project is not Git-backed, ask for the equivalent candidate diff/artifact and inspection commands.

Do not treat unstaged work as part of the candidate. This skill is optimized for final readiness of the staged set.

## Read local references first

Read these before starting:
- [references/repo-readiness-sources.md](references/repo-readiness-sources.md)
- [references/templates.md](references/templates.md)

## Discover mandatory gates before validating

Do not guess what counts as release readiness. Determine the repo's actual mandatory gates from its automation and docs before running the gauntlet.

Look for the smallest command set that faithfully covers:
- tests required for merge or release
- build, compile, bundle, package, or deploy-dry-run checks
- lint, typecheck, format, static analysis, schema, migration, contract, or security checks
- browser, accessibility, visual, device, performance, load, benchmark, bundle-budget, or SLO checks when defined
- external gates that require secrets, hardware, network access, staging URLs, dashboards, or human signoff

If the mandatory gate set is unclear, stop and ask. Unknown mandatory gates mean the candidate is **NOT READY**.

## Make performance first-class

Always assess whether the staged changes can affect application performance: latency, throughput, startup, render time, bundle size, memory, CPU, I/O, database/query volume, queue/batch duration, cost, or resource limits.

Use existing repo baselines, budgets, benchmarks, SLOs, and dashboards as the source of truth. Leave a reusable measurement path so future runs can compare results. If a performance-sensitive change has no usable baseline, establish a minimal repeatable baseline before declaring readiness:
- choose metrics and inputs that match the changed user or operator path
- run the smallest reliable repo-appropriate measurement locally, or name the blocked external measurement
- record command, environment, dataset/input, iterations, metric values, and comparison target
- stage an update to the repo's accepted baseline artifact when one exists; otherwise ask where to persist it or get an explicit handoff-only waiver

Do not invent universal thresholds. When evidence shows avoidable performance cost, improve it within scope and remeasure. Do not lower budgets, bless slower baselines, or regenerate performance snapshots blindly.

## Workflow

1. Confirm the candidate has staged files.
2. Discover mandatory validation, release, and performance gates.
3. Inspect the staged set: file list, diff stat, and each per-file staged diff.
4. Review every staged file and every hunk for P0, P1, and P2 issues, including performance regressions and missing/stale baselines.
5. Fix every P0, P1, or P2 issue you find.
6. Stage every correction immediately.
7. Restart the staged review from the top because the candidate changed.
8. Use targeted validation only as a fast feedback loop while fixing issues.
9. Once the staged review is clean, run the full mandatory repo-specific readiness gauntlet.
10. If any gate fails, fix the problem, stage the fix, and restart from staged review.
11. If a performance baseline is missing for a performance-sensitive change, create or record the baseline, persist and stage any durable artifact or get an explicit handoff-only waiver, and restart from staged review.
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
- remove debug logs, TODO shipping hacks, commented-out code, temporary flags, and local-only assumptions from release scope
- check rollback, destructive actions, partial-write paths, caching, concurrency, and out-of-order behavior when touched
- review auth, secrets, and authorization boundaries aggressively when touched
- review accessibility, focus management, theming, responsive behavior, and device-specific paths on touched UI surfaces when relevant
- keep fixes within the candidate scope; avoid unrelated refactors
- do not commit unless the user explicitly asks

## Validation policy

Targeted tests are optional helpers. They never replace the full readiness gauntlet.

Before declaring readiness:
- run the repo's exact mandatory wrapper commands when possible
- mirror the union of relevant CI or release gates locally when possible
- prefer a local command set that is equal to or stricter than CI
- run mandatory performance gates and compare against known baselines, budgets, or SLOs
- establish and record an initial baseline for performance-sensitive changes that lack one
- rerun the full gauntlet after the last fix, even if earlier subsets already passed

For a repo-defined mandatory external gate that cannot run because of missing credentials, services, devices, staging URLs, dashboards, or access:
- name the blocked gate explicitly
- name the missing prerequisite explicitly
- surface the blocked state as soon as it is discovered
- do not claim READY unless the gate passes or the user/release owner explicitly waives it

This skill has no generic standing waivers. Only repo docs, release-owner direction, or an explicit user waiver for the current run can waive a mandatory gate.

## Feed back missed failures

If a later PR, branch-promotion, deployment, monitoring, or CI failure exposes a gap this skill did not catch:
- fix and stage the product correction first
- rerun this skill until the staged candidate is green again
- update this skill's references or templates so the missed gate, prerequisite, performance signal, or failure pattern is discovered earlier next time
- keep the update scoped to the durable lesson, not incidental noise from one run

## Final verdict rules

Use these rules strictly:

- **READY**
  - all mandatory gates are known
  - all mandatory local gates passed
  - all mandatory external gates passed, were repo-approved-equivalent locally, or were explicitly waived
  - performance-sensitive changes have passing gates or a durable recorded baseline, or an explicit handoff-only baseline waiver, with no unresolved regression
  - no P0, P1, or P2 issues remain
  - no unstaged tracked changes or equivalent out-of-scope candidate changes, and no generated validation artifacts remain

- **NOT READY**
  - any mandatory gate failed or is unknown
  - any mandatory external gate is blocked without explicit waiver
  - any unresolved performance regression, required missing baseline, or unresolved baseline persistence decision remains
  - any P0, P1, or P2 issue remains
  - any unstaged tracked change or equivalent out-of-scope candidate change, or generated validation artifact remains

- **CONDITIONALLY READY**
  - use only when local mandatory gates passed but a clearly named external or organizational signoff remains pending and the user explicitly accepts that pending state
  - do not use this for unknown gates, unresolved performance baselines, failed checks, or as a softer synonym for READY

## Candidate hygiene

By the end:
- all intended corrections must be staged
- no unstaged tracked changes or equivalent out-of-scope candidate changes may remain
- no validation artifacts created by this run should be left untracked
- the final staged diff should reflect exactly what is being proposed for production

## Example requests

- "Do a strict production-readiness pass on the staged changes."
- "Review the staged diff file by file, fix any P0/P1/P2 issues, stage the fixes, and run all required gates."
- "Treat this as a release candidate and fail closed until the repo's mandatory checks and performance baselines are satisfied."
- "Get this branch truly production-ready, not just test-green."

## Documentation Output

When writing plans, reports, PRDs, briefs, findings, story tracking, scratch notes, or other generated documentation, write them under the repository-root `docs/` directory, preferably `docs/check-production-readiness/...` or the specific `docs/` path named in the workflow. Do not use `.agents/`, `.pi/`, `.codex/`, `.claude/`, or other agent-specific directories for generated documentation.
