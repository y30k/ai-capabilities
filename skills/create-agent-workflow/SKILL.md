---
name: create-agent-workflow
description: |
  Design reusable multi-step workflows for AI coding agents with triggers, inputs and outputs, phases, artifacts, approval gates, executable validation, recovery, and bounded failure handling. Use when the user asks for an agent workflow, agent command or prompt, coding-agent runbook, reusable agent process, or project-specific procedure for planning, implementation, review, or automation.
---

# Create Agent Workflow

Use this skill to turn a recurring agent task into a reusable workflow that any capable coding agent can follow.

## Runbook

1. Read `references/workflow.md`.
2. Identify the user's desired trigger, inputs, outputs, required tools, and safety constraints.
3. Define each phase's reads, writes, tools/commands, action, success evidence, failure/retry behavior, and approval gate.
4. Prefer repository-defined deterministic commands/scripts for checks and parsing; use AI reasoning for investigation, synthesis, and judgment.
5. Simulate a representative path read-only by default, record gate decisions, and bound every loop or retry. Execute commands or a real dry run only when they are non-mutating or the user explicitly authorizes every file, implementation, or external mutation involved.
6. Save the executable workflow in the user-requested or project-conventional location, or provide it inline when no target format exists.

## Documentation Output

Write ancillary plans, reports, findings, and scratch notes under `docs/create-agent-workflow/` or another user-specified documentation path. Keep executable workflow definitions, commands, prompts, and configuration in the requested or project-conventional location, including agent-specific directories when that is the deliverable.
