---
name: agent-smoke-test
description: |
  Evaluate an AI coding agent, model/provider integration, tool harness, or workspace with portable, evidence-recorded smoke probes for instruction following, strict structured output, safe file/shell tools, multi-turn recovery, and approval gates. Use when onboarding or comparing agents, models, providers, workspaces, or tool integrations; diagnosing harness regressions; or checking prerequisites before long-running automation.
---

# Agent Smoke Test

## Subject Boundary

Test a clearly identified subject agent through a separate session, API, CLI, or harness and retain its raw responses or tool events. Do not treat the evaluator's behavior in the current conversation as independent evidence. If no isolated subject channel exists, run only harness/workspace checks and mark agent-behavior checks `NOT RUN`.

## Runbook

1. Select **quick** (chat probes), **tools** (safe read/write/shell probes), or **workflow** (multi-turn, gate, and recovery probes); ask when the requested depth is unclear.
2. Read `references/workflow.md` and record the subject, model/provider, harness, permissions, workspace, and invocation mechanism.
3. Run read-only checks by default. For write probes, use a uniquely named owned temporary directory outside the repository when possible; never modify source or pre-existing files.
4. Report raw evidence, pass/fail/not-run results, cleanup status, limitations, and recommended guardrails.

## Documentation Output

Persist a report under `docs/agent-smoke-test/` only when the user requests one. Never store generated documentation in agent-state directories such as `.agents/`, `.pi/`, `.codex/`, or `.claude/`.
