# Agent Workflow Authoring Workflow

## 1. Understand the Recurring Task

Ask for or infer:

- Trigger phrases and examples.
- Required inputs and expected outputs.
- Tools available to the agent.
- What must never happen without approval.
- How success is verified.

## 2. Choose a Shape

| Shape | Use when |
| --- | --- |
| linear phases | Most tasks have a fixed order |
| branching | Bug vs feature, small vs large, safe vs risky |
| map-reduce review | Multiple independent review lanes should be synthesized |
| loop | Work must repeat until tests, checks, or user acceptance pass |
| gated | Human decision or approval is required |

## 3. Design the Artifact Chain

For each phase define:

| Phase | Reads | Writes | Success check |
| --- | --- | --- | --- |
| investigate | user request, repo | findings.md | claims cite files |
| plan | findings.md | plan.md | user can execute it |
| implement | plan.md | code changes | tests pass |
| report | diff, tests | summary.md | risks visible |

## 4. Add Safety and Recovery

- Gate destructive actions, releases, migrations, or external writes.
- Include rollback notes for risky edits.
- If a tool is missing, define a manual or lower-fidelity fallback.
- Bound loops with max iterations and an exit report.

## 5. Validate the Workflow

Run a dry pass on a trivial task. Confirm:

- Phase order is unambiguous.
- Artifacts provide enough context for downstream phases.
- Deterministic checks are executable in the project.
- User gates ask clear questions.
