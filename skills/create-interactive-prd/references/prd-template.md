# PRD Template

Read this before Phase 4 generation. Fill every section from the interview, market/codebase research, and technical feasibility work. Use `TBD — needs research` for unknowns.

```markdown
# {Product or Feature Name}

## Problem Statement

{2-3 sentences: who has what problem, the observable pain, and the cost of not solving it.}

## Evidence

- {User quote, data point, market/source finding, or codebase observation}
- {Another piece of evidence}
- {If none: "Assumption — needs validation through [method]"}

## Proposed Solution

{One concrete paragraph explaining what to build and why this approach beats alternatives. Prefer extending existing primitives over creating new ones.}

## Key Hypothesis

We believe {capability} will {solve problem} for {users}.
We'll know we're right when {measurable outcome}.

## What We're NOT Building

- {Out-of-scope item 1} — {why}
- {Out-of-scope item 2} — {why}

## Success Metrics

| Metric | Target | How Measured |
|--------|--------|--------------|
| {Primary metric} | {Specific target} | {Method} |
| {Secondary metric} | {Specific target} | {Method} |

## Open Questions

- [ ] {Unresolved question 1}
- [ ] {Unresolved question 2}

---

## Users & Context

**Primary User**
- **Who**: {specific description}
- **Current behavior**: {what they do today}
- **Trigger**: {moment that creates the need}
- **Success state**: {what done looks like}

**Job to Be Done**
When {situation}, I want to {motivation}, so I can {outcome}.

**Non-Users**
{Who this is not for and why.}

---

## Solution Detail

### Core Capabilities (MoSCoW)

| Priority | Capability | Rationale |
|----------|------------|-----------|
| Must | {Capability} | {Why essential} |
| Must | {Capability} | {Why essential} |
| Should | {Capability} | {Why important but not blocking} |
| Could | {Capability} | {Nice to have} |
| Won't | {Capability} | {Explicitly deferred and why} |

### MVP Scope

{Absolute minimum needed to validate the hypothesis.}

### User Flow

{Critical path: shortest journey to value.}

---

## Technical Approach

**Feasibility**: {HIGH/MEDIUM/LOW}

**Verified Existing Primitives**

| Primitive | Location | Notes |
|-----------|----------|-------|
| {endpoint/component/query/type/schema} | `{file:line}` | {what exists and how it can be extended} |

**Architecture Notes**
- {Key technical decision and why}
- {Dependency or integration point}
- {Anything unverified marked as needs verification}

**Technical Risks**

| Risk | Likelihood | Mitigation |
|------|------------|------------|
| {Risk} | {HIGH/MEDIUM/LOW} | {How to handle or validate} |

---

## Implementation Phases

<!--
  STATUS: pending | in-progress | complete
  PARALLEL: phases that can run concurrently, e.g. "with 3" or "-"
  DEPENDS: phases that must complete first, e.g. "1, 2" or "-"
  PLAN: link to generated plan file once created
-->

| # | Phase | Description | Status | Parallel | Depends | Plan |
|---|-------|-------------|--------|----------|---------|------|
| 1 | {Phase name} | {What this phase delivers} | pending | - | - | - |
| 2 | {Phase name} | {What this phase delivers} | pending | - | 1 | - |
| 3 | {Phase name} | {What this phase delivers} | pending | with 4 | 2 | - |
| 4 | {Phase name} | {What this phase delivers} | pending | with 3 | 2 | - |
| 5 | {Phase name} | {What this phase delivers} | pending | - | 3, 4 | - |

### Phase Details

**Phase 1: {Name}**
- **Goal**: {What to achieve}
- **Scope**: {Bounded deliverables}
- **Success signal**: {How to know it is done}

**Phase 2: {Name}**
- **Goal**: {What to achieve}
- **Scope**: {Bounded deliverables}
- **Success signal**: {How to know it is done}

{Continue for each phase.}

### Parallelism Notes

{Explain which phases can run in parallel and why.}

---

## Decisions Log

| Decision | Choice | Alternatives | Rationale |
|----------|--------|--------------|-----------|
| {Decision} | {Choice} | {Options considered} | {Why this one} |

---

## Research Summary

**Market Context**
{Key findings, links, known gaps, and assumptions.}

**Technical Context**
{Key codebase findings with path/line references and remaining verification needs.}

---

## Validation Notes

{Added after validation. Document corrections, or state: "All technical references verified against codebase. No corrections needed."}

---

*Generated: {ISO timestamp}*
*Status: DRAFT — validated technical references where possible; requires user review before implementation*
```
