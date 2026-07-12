# Readiness templates

Use these as strict defaults and adapt to the actual repo and staged change set. If you persist a readiness scratchpad or handoff document, write it under `docs/check-production-readiness/` in the repository root.

## Table of Contents

- [Review scratchpad template](#review-scratchpad-template)
- [Final handoff template](#final-handoff-template)
- [Verdict discipline](#verdict-discipline)
- [Review heuristics](#review-heuristics)
- [Severity reminder](#severity-reminder)

## Review scratchpad template

```md
# Production readiness review

## Scope
- source commit (`git rev-parse HEAD`):
- staged tree ID (`git write-tree`):
- exact staged files:
- staged/unstaged overlap result:
- key changed areas:
- discovered validation sources:

## Mandatory pre-submission gates
- `command` — source of truth; exit status; environment/timestamp
- `command` — source of truth; exit status; environment/timestamp

## Normal-submission-created automation
- `check/workflow/status` — source of truth; why it cannot run before submission; monitoring owner

## Other external mandatory gates
- `command or step` — prerequisite/status; evidence URL; observed time
- waiver, if any — scope; approver; date

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

## Recommended skill improvement (not applied)
- durable lesson and proposed package location
```

## Final handoff template

```md
Production-readiness pass complete.

Verdict:
- READY | NOT READY | CONDITIONALLY READY

Candidate:
- source commit (`git rev-parse HEAD`)
- staged tree ID (`git write-tree`)
- exact staged files
- staged/unstaged overlap result

Fixed and staged:
- path — what was corrected

Mandatory pre-submission validation run:
- `command` — passed
- `command` — passed

Normal-submission-created automation:
- `check/workflow/status` — pending; hand off to `submit-change-request`

Performance readiness:
- baseline/budget/SLO source — result
- `measurement command` — metric, baseline, comparison, passed/failed
- baseline artifact — staged | handoff-only waiver

Other external mandatory gates:
- `command or step` — passed | blocked | waived; evidence URL; observed time
- waiver — scope; approver; date

Blocked prerequisites:
- prerequisite

Recommended skill improvement (not applied):
- durable lesson and proposed package location

Final candidate evidence:
- `git diff --cached --stat` — result

Final git status:
- no unstaged tracked changes or equivalent out-of-scope candidate changes
- no validation artifacts created by this run
- staged diff ready for submission
```

## Verdict discipline

Use `READY` only when every mandatory gate is known and classified, all mandatory pre-submission gates are satisfied, no normal-submission-created automation remains pending, performance-sensitive changes have passing gates or durable recorded baselines (or an explicit handoff-only baseline waiver), no P0/P1/P2 issues remain, and candidate hygiene is clean.

Use `NOT READY` for any failed, unknown, or unclassified gate; blocked unwaived pre-submission external gate; unresolved performance regression; required missing baseline; unresolved baseline persistence decision; remaining P0/P1/P2 issue; or unstaged tracked/generated artifact from this run.

Use `CONDITIONALLY READY` only when all pre-submission readiness criteria pass and the only pending evidence is clearly named feature-branch-push or PR/MR-created automation assigned to `submit-change-request` for the normal PR/MR path. Do not use it for organizational signoffs, default-branch-push automation, unknown gates, failed checks, missing performance evidence, or direct-to-default fast track.

## Review heuristics

Use these prompts while reviewing each file:
- Can this break deploy, startup, auth, migrations, data integrity, rollback, or a primary workflow?
- Can this slow a key path, increase resource cost, grow payloads/bundles, add N+1 work, or hide performance regressions that should be fixed or baselined?
- Is changed behavior covered by the repo's required tests, checks, performance gates, and baselines?
- Did the fix leave docs, baselines, manifests, schemas, snapshots, fixtures, or generated expectations stale?
- Is there a smaller, safer correction that solves the same issue?
- Does the final staged set remain coherent after the latest fix?
- Did I run every mandatory pre-submission gate and name each normal-submission-created automation gate instead of guessing or taking shortcuts?

## Severity reminder

Ship blockers for this skill are P0, P1, and P2. Do not downgrade issues just to reach a green verdict.
