---
name: improve-code-health
description: |
  Review and improve code health through read-only architecture or maintainability audits and explicitly authorized behavior-preserving refactors, complexity reduction, and dependency cleanup. Use when the user asks for an architecture sweep, codebase health review, maintainability findings, simplification plan, safe refactor, complexity reduction, dependency cleanup, or behavior-preserving cleanup.
---

# Improve Code Health

Use this skill to improve maintainability without changing intended behavior.

## Paths

- **architecture sweep**: map structure, complexity, boundaries, and high-leverage simplifications.
- **safe refactor**: execute scoped refactors with continuous validation.

Treat architecture sweeps, audits, reviews, and planning requests as read-only. Edit source code only when the user explicitly requests a refactor or implementation, or approves a proposed refactor slice. Staging requires a separate exact Git-index plan unless the user already asked to stage or prepare a submission candidate. Ask before behavior or interface changes, destructive operations, cross-repository work, weakening checks, credentials or production use, or remote submission.

Read `references/workflow.md` before starting.

## Documentation Output

Persist audit findings or refactor plans under `docs/improve-code-health/` or a user-specified path under `docs/` only when the user requests or authorizes a repository artifact. Otherwise return audit/planning results in chat and keep the run fully read-only. Never store generated documentation in agent-state directories such as `.agents/`, `.pi/`, `.codex/`, or `.claude/`.
