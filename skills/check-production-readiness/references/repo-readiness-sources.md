# Repo readiness sources

Read these sources before running a readiness pass. Stay project-agnostic: use the repo's own language, framework, package manager, task runner, CI, docs, and release process as the source of truth.

## Table of Contents

- [Start from staged reality](#start-from-staged-reality)
- [Discover mandatory gates first](#discover-mandatory-gates-first)
- [Build a strict repo-specific readiness gauntlet](#build-a-strict-repo-specific-readiness-gauntlet)
- [Performance baseline workflow](#performance-baseline-workflow)
- [External or environment-bound gates](#external-or-environment-bound-gates)
- [Validation strategy](#validation-strategy)
- [What to review carefully](#what-to-review-carefully)
- [Strict readiness completion criteria](#strict-readiness-completion-criteria)

## Start from staged reality

For Git-backed repos, inspect the candidate first. If the project is not Git-backed, ask for the equivalent candidate diff/artifact and inspection commands before continuing:

```bash
git status --short
git rev-parse HEAD
git write-tree
git diff --cached --name-only
git diff --cached --stat
```

Then inspect each staged file individually:

```bash
path="path/to/file"
git diff --cached -- "$path"
```

Before editing, inspect `git status --short` for paths with both index and working-tree changes. Stop on staged/unstaged overlap unless the user resolves it or authorizes a patch-staging plan.

After each authorized correction, inspect both views, stage only the correction hunks, and inspect both views again:

```bash
path="path/to/file"
git diff -- "$path"
git diff --cached -- "$path"
git add -p -- "$path"  # or a repository-approved patch-staging equivalent
git diff -- "$path"
git diff --cached -- "$path"
git status --short
```

Never use whole-file `git add <path>` when the path had pre-existing unstaged content. Finish only when no unstaged tracked changes or equivalent out-of-scope candidate changes remain and no validation artifacts created by this run remain untracked.

## Discover mandatory gates first

Do not start the pre-submission gauntlet until you know what the repo treats as mandatory for merge, release, deploy, or production acceptance.

Use the repo's own sources in this order when available:
1. release, deploy, operations, SLO/SLA, performance, or runbook docs
2. CI workflows for pull requests, main, release branches, tags, or deploys
3. wrapper commands in package managers or task runners
4. raw tool commands only when the repo has no wrappers

Common places to inspect:
- root and workspace `package.json`
- `Makefile`, `justfile`, `Taskfile.yml`, `turbo.json`, `nx.json`, `bazel`/`buck` configs
- language files such as `pyproject.toml`, `tox.ini`, `Cargo.toml`, `go.mod`, `pom.xml`, `build.gradle`, `mix.exs`, `.csproj`, `Gemfile`
- CI configs such as `.github/workflows/*`, `.gitlab-ci.yml`, `circle.yml`, `azure-pipelines.yml`, `.buildkite/*`
- release, deploy, ops, monitoring, observability, or incident docs
- benchmark, load-test, profiling, bundle-budget, and performance-budget configs

Useful discovery commands include:

```bash
find . -maxdepth 4 \( -name package.json -o -name Makefile -o -name justfile -o -name Taskfile.yml -o -name pyproject.toml -o -name tox.ini -o -name Cargo.toml -o -name go.mod -o -name pom.xml -o -name build.gradle -o -name Gemfile -o -name '*.csproj' -o -name '*.sln' -o -name '*.yml' -o -name '*.yaml' \)
rg -n "test|build|lint|typecheck|format|check|e2e|integration|security|migration|deploy|release|smoke" .github .gitlab-ci.yml . 2>/dev/null
rg -n "bench|benchmark|perf|performance|latency|throughput|p95|p99|SLO|SLA|budget|bundle|lighthouse|web-vitals|load test|stress|k6|locust|jmeter|wrk|artillery|autocannon|profile|APM|observability" . 2>/dev/null
```

Classify every discovered gate:

- **pre-submission** — runnable against the local staged candidate and required before commit, PR/MR creation, or direct push
- **normal-submission-created** — created only after `submit-change-request` commits the exact candidate, pushes its feature branch, or creates/updates the PR/MR, such as branch pipelines, required status checks, preview deploys, or merge-request pipelines

If mandatory gates or their classification remain unclear, stop and ask. Unknown gates mean the candidate is **NOT READY**.

## Build a strict repo-specific readiness gauntlet

Assemble the smallest command set that safely covers the union of mandatory pre-submission gates. Keep a separate list of feature-branch-push and PR/MR-created normal-submission automation for the handoff.

That usually means covering, when present and relevant:
- unit, integration, end-to-end, smoke, and contract tests
- build, compile, package, bundle, or deploy dry-runs
- lint, typecheck, format verification, static analysis, generated-code checks, schema checks
- migration, data-integrity, security, dependency, and compatibility checks
- accessibility, visual, responsive, browser/device, and localization checks
- performance, load, benchmark, bundle-budget, memory, startup, and SLO checks
- docs, manifests, snapshots, fixtures, API specs, or release-note checks required by the repo

If multiple pre-submission workflows cover the changed scope, run their union or a stricter safe superset. Do not cherry-pick the easiest green subset. Do not pretend to run normal-submission-created automation locally; identify its exact trigger, workflow, and status context instead.

## Performance baseline workflow

Use existing baselines first: benchmark outputs, perf snapshots, bundle budgets, SLO/SLA docs, dashboard thresholds, load-test expectations, historical CI artifacts, or release docs.

When a performance-sensitive change has no usable baseline:
1. Identify the affected user/operator path and the metric that would reveal harm.
2. Prefer an existing local benchmark, test, profiler, load-test script, or bundle analyzer.
3. If none exists, use the least invasive repeatable measurement that fits the repo, then ask before adding a new framework.
4. Run enough iterations to distinguish signal from noise; use stable inputs and note warmup/cold-start behavior when relevant.
5. Record command, environment, data/input size, iterations, raw results, chosen baseline value, and confidence.
6. Use an existing measurement path or an ephemeral read-only measurement when possible, and describe any reusable script, configuration, or baseline artifact that should be added.
7. Create, persist, or stage that reusable path or artifact only when authorized. Otherwise report the proposed artifact or required handoff-only waiver and keep the verdict **NOT READY**.

Treat these as readiness problems:
- regression beyond an existing budget, SLO, or accepted baseline
- avoidable performance waste on a touched key path when a scoped fix is feasible
- missing or stale baseline for a performance-sensitive staged change when measurement is feasible
- unresolved decision about where to persist a new baseline
- benchmark noise large enough to hide likely regression
- changed behavior that improves correctness by adding cost without any measurement on the affected path
- baseline updates that simply bless slower behavior without justification

## External or environment-bound gates

Some mandatory gates cannot run locally without extra setup, for example:
- real-device, hosted-browser, staging, preview, or production smoke checks
- cloud integration suites or synthetic monitors
- deploy, publish, migration, or rollback dry-runs requiring secrets or infrastructure
- APM, observability, SLO, or error-budget checks requiring dashboard access
- load or stress tests requiring shared environments or approved windows

If a required gate is created only by committing/pushing the exact candidate to a feature branch or creating/updating its PR/MR, record its trigger, workflow, and status context and hand it to `submit-change-request`; this supports **CONDITIONALLY READY** without pretending the gate passed. Default-branch-push automation for fast track does not qualify and must have an explicit named waiver reflected in a READY verdict.

For every other unavailable gate requiring secrets, accounts, VPN access, hardware, base URLs, datasets, or dashboard permissions:
- do not fake the result
- do not quietly omit the check
- record the exact blocked command or validation step
- record the exact missing prerequisite
- surface the blocked gate immediately and ask for an explicit waiver when needed
- treat the candidate as **NOT READY** unless the gate passes, is replaced by an equivalent repo-approved local gate, or is explicitly waived by the user or release owner

This skill has no global standing waivers. A waiver must come from repo documentation, release-owner direction, or the user for the current run.

## Validation strategy

Use this order:
1. targeted validation after each fix
2. full strict pre-submission gauntlet once staged review is clean
3. if any step fails, fix and stage only when authorized, then restart staged review; otherwise report the failure and remain **NOT READY**
4. rerun the full pre-submission gauntlet after the final fix
5. hand named normal-submission-created automation to `submit-change-request`

Do not assume a previously clean review remains clean after a test-driven fix.

## What to review carefully

Prioritize these risk areas in staged changes:
- auth, authorization, secrets, networking, and trust boundaries
- destructive actions, deletion, restore, rollback, recovery, and partial-write paths
- API, schema, migration, persistence, serialization, and compatibility changes
- caching, batching, concurrency, queues, background jobs, retries, idempotency, and ordering
- performance hot paths: N+1 work, query plans, payload size, bundle size, render loops, startup, blocking I/O, memory growth, CPU spikes, cold/warm cache behavior, and cost drivers
- UI flows: accessibility, focus, responsive layout, theming, localization, browser/device differences, and async/lazy-loading timing
- tests and wrappers that depend on ports, servers, clocks, randomness, parallelism, environment variables, or teardown order
- generated files, snapshots, baselines, manifests, fixtures, API specs, schemas, or docs that must track intentional changes
- release notes or ops docs when the release process depends on them staying accurate

## Strict readiness completion criteria

A staged candidate is **READY** only when all of these are true:
- staged diff has no remaining P0, P1, or P2 issues
- every mandatory gate is known and classified
- every mandatory pre-submission local and external gate passes, is repo-approved-equivalent locally, or is explicitly waived
- no normal-submission-created automation remains pending
- performance-sensitive changes have passing performance gates or a durable recorded baseline, or an explicit handoff-only baseline waiver, with no unresolved regression
- no unstaged tracked changes remain
- no validation artifacts created by this run remain untracked
- staged corrections are included in the candidate set

A staged candidate is **CONDITIONALLY READY** only when every READY criterion holds except clearly named feature-branch-push or PR/MR-created automation remains pending for `submit-change-request` on the normal PR/MR path.

A staged candidate is **NOT READY** when a gate fails, is unknown or unclassified, a pre-submission external gate is blocked without waiver, performance evidence is unresolved, a P0/P1/P2 issue remains, or candidate hygiene is not clean.
