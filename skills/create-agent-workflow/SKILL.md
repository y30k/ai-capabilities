---
name: create-agent-workflow
description: |
  Create reusable multi-step workflows for AI coding agents, including phase design, gates, artifacts, deterministic checks, and failure handling. Use when the user asks to create a workflow, command, runbook, automation plan, reusable agent process, or project-specific coding-agent procedure.
---

# Create Agent Workflow

Use this skill to turn a recurring agent task into a reusable workflow that any capable coding agent can follow.

## Runbook

1. Read `references/workflow.md`.
2. Identify the user's desired trigger, inputs, outputs, required tools, and safety constraints.
3. Design phases with explicit artifacts and gates.
4. Prefer deterministic commands/scripts for checks and parsing; use AI reasoning for investigation, synthesis, and judgment.
5. Save the workflow where the user wants it, or provide it inline if no target format exists.
