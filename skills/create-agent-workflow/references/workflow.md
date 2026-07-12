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

| Phase | Reads | Writes | Tools/commands | Action | Success evidence | Failure/retry | Approval required |
| --- | --- | --- | --- | --- | --- | --- | --- |
| investigate | user request, repo | findings.md | read/search commands | verify context | claims cite files | report missing inputs | no |
| plan | findings.md | plan.md | deterministic validators | bound the work | executable plan | revise once, then escalate | user approval |
| implement | approved plan | code changes | repo-defined checks | apply approved slice | checks and acceptance pass | bounded repair or stop | as scoped |
| report | diff, check results | summary.md | status/diff commands | synthesize evidence | risks and outcomes visible | N/A | no |

Copy exact project commands from repository configuration; do not invent commands. Define expected exit codes or machine-readable output, a timeout or iteration bound where relevant, and the artifact passed to the next phase.

## 4. Add Safety and Recovery

- Gate destructive actions, releases, migrations, or external writes.
- Include rollback notes for risky edits.
- If a tool is missing, define a manual or lower-fidelity fallback.
- Bound loops with max iterations and an exit report.

## 5. Validate the Workflow

Simulate a trivial representative path read-only by default. Walk each phase, artifact handoff, gate, failure branch, and retry bound without executing the workflow's implementation or mutation steps. Run repository commands only when they are demonstrably read-only; obtain explicit authorization before any command writes files, changes code/configuration, mutates external state, or executes the representative implementation.

Record simulated decisions separately from observed evidence. For commands not authorized or not run, write `NOT RUN` and the expected exit/artifact contract instead of inventing results. When an authorized dry run executes a command, record its actual exit status and produced artifact. Then confirm:

- Phase order is unambiguous.
- Artifacts provide enough context for downstream phases.
- Deterministic checks are executable or have an explicit `NOT RUN` prerequisite.
- User gates ask clear questions.
- No simulation side effect is represented as an observed successful run.
