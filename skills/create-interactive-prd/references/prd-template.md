# PRD Template

Read this before Phase 4 generation. Fill every section from the interview, market/codebase research, and technical feasibility work. Use `TBD — needs research` for unknowns.

## Table of Contents

- Problem Statement, Evidence, Proposed Solution, and Key Hypothesis
- Non-goals, Success Metrics, and Open Questions
- Users and Context
- Solution Detail and MVP Scope
- Technical Approach and Risks
- Implementation Phases and Dependencies
- Decisions Log, Research Summary, and Validation Notes

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

**Feasibility**: {HIGH/MEDIUM/LOW, or TBD — needs research when repository evidence is unavailable}

**Verified Existing Primitives**

| Primitive | Location | Notes |
|-----------|----------|-------|
| {endpoint/component/query/type/schema, or TBD — needs research} | `{file:line, or repository unavailable}` | {what exists and how it can be extended, or not verified} |

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
  Add as many rows as the approved scope needs.
  STATUS: pending | in-progress | complete
  PARALLEL and DEPENDS reference other phase numbers when known; otherwise use "-".
-->

| # | Phase | Description | Status | Parallel | Depends |
|---|-------|-------------|--------|----------|---------|
| {N} | {Phase name} | {What this phase delivers} | pending | {phase numbers or -} | {phase numbers or -} |

### Phase Details

**Phase {N}: {Name}**
- **Goal**: {What to achieve}
- **Scope**: {Bounded deliverables}
- **Success signal**: {How to know it is done}

{Repeat for each phase.}

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

{Added after validation. Document corrections; when repository validation ran and passed, state: "All technical references verified against codebase. No corrections needed." When no repository was available, state: "Repository validation NOT RUN — repository unavailable. Feasibility and repository-dependent claims remain TBD — needs research."}

---

*Generated: {ISO timestamp}*
*Status: DRAFT — validated technical references where possible; requires user review before implementation*
```
