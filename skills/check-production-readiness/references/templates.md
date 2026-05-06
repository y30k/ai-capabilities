# Readiness templates

Use these as strict defaults and adapt to the actual repo and staged change set.

## Review scratchpad template

```md
# Production readiness review

## Scope
- staged files:
- key changed areas:
- discovered validation sources:

## Mandatory gates discovered
- `command` — source of truth
- `command` — source of truth

## External mandatory gates
- `command or step` — prerequisite/status

## Performance readiness
- changed performance-sensitive paths:
- existing baselines/budgets/SLOs:
- measurement command(s):
- environment/input/iterations:
- result vs baseline:
- new or updated baseline artifact:

## P0
- [ ] issue

## P1
- [ ] issue

## P2
- [ ] issue

## Follow-up fixes staged
- path — short note

## Targeted validation run
- `command` — result

## Full gauntlet run
- `command` — result

## Skill feedback updates
- path — durable lesson added for future readiness passes
```

## Final handoff template

```md
Production-readiness pass complete.

Verdict:
- READY | NOT READY | CONDITIONALLY READY

Fixed and staged:
- path — what was corrected

Mandatory validation run:
- `command` — passed
- `command` — passed

Performance readiness:
- baseline/budget/SLO source — result
- `measurement command` — metric, baseline, comparison, passed/failed
- baseline artifact — staged | handoff-only waiver

External mandatory gates:
- `command or step` — passed | blocked | waived

Blocked prerequisites:
- prerequisite

Readiness skill updates:
- path — durable lesson added for future readiness passes

Final git status:
- no unstaged tracked changes or equivalent out-of-scope candidate changes
- no validation artifacts created by this run
- staged diff ready for review
```

## Verdict discipline

Use `READY` only when every mandatory gate is known and satisfied, performance-sensitive changes have passing gates or durable recorded baselines (or an explicit handoff-only baseline waiver), no P0/P1/P2 issues remain, and candidate hygiene is clean.

Use `NOT READY` for any failed gate, unknown gate, blocked unwaived external gate, unresolved performance regression, required missing baseline, unresolved baseline persistence decision, remaining P0/P1/P2 issue, or unstaged tracked/generated artifact from this run.

Use `CONDITIONALLY READY` only when the user explicitly accepts a named pending external or organizational signoff after local mandatory gates passed. Do not use it for unknown gates or missing performance evidence.

## Review heuristics

Use these prompts while reviewing each file:
- Can this break deploy, startup, auth, migrations, data integrity, rollback, or a primary workflow?
- Can this slow a key path, increase resource cost, grow payloads/bundles, add N+1 work, or hide performance regressions that should be fixed or baselined?
- Is changed behavior covered by the repo's required tests, checks, performance gates, and baselines?
- Did the fix leave docs, baselines, manifests, schemas, snapshots, fixtures, or generated expectations stale?
- Is there a smaller, safer correction that solves the same issue?
- Does the final staged set remain coherent after the latest fix?
- Did I mirror mandatory CI/release gates instead of guessing or taking shortcuts?

## Severity reminder

Ship blockers for this skill are P0, P1, and P2. Do not downgrade issues just to reach a green verdict.
