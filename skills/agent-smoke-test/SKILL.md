---
name: agent-smoke-test
description: |
  Run portable smoke tests for any AI coding agent or automation environment: instruction following, structured output, file operations, shell/tool availability, loop/gate behavior, and repository safety. Use when validating a new agent, model, provider, workspace, or integration; when smoke tests differ only by coding agent; or before trusting a long-running workflow.
---

# Agent Smoke Test

Use this skill to verify what the current coding agent can reliably do in a project. It replaces provider-specific smoke skills with one portable checklist.

## Runbook

1. Ask what level to run if unclear: **quick** (chat only), **tools** (read/write/shell), or **workflow** (loop/gate/recovery behavior).
2. Read `references/workflow.md`.
3. Run only safe checks by default. Do not modify project source unless the user approves; write scratch files under `.agents/smoke-test/`.
4. Report capabilities, failures, and recommended guardrails for future tasks.
