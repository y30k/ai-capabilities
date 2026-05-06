---
name: create-interactive-prd
description: |
  Guide an AI coding agent through a planning-only interactive PRD workflow: problem-first,
  hypothesis-driven product requirements created through gated user questions,
  market/codebase research, technical feasibility assessment, PRD generation, and
  validation. Use when the user asks to create, write, or plan a PRD, product
  requirements document, feature spec, interactive PRD, plan a feature, or turn an
  idea into an implementation-ready product spec. Reads code for feasibility but does
  not modify source code or implement. Stops after PRD validation for user review.
---

# Create Interactive PRD

Use this skill to run an interactive PRD interview directly in the coding-agent chat. The workflow focuses on the problem before the solution, gathers evidence before scope, verifies codebase claims by reading files, then generates and validates an implementation-ready PRD.

## Boundary

This is a **planning and requirements skill only**. It may read project files to verify feasibility, but it must not modify source code, implement features, create branches, or open PRs. After validating the PRD, stop and ask the user to review it. Implementation requires a separate explicit request, such as using `implement-prd-stories` after the PRD is approved.

## Core Rules

- Run the workflow as a gated conversation. Ask each question set, then stop and wait for the user's answers.
- Start with primitives and problems, not features or implementation ideas.
- Do research before proposing scope: market context if web/search tools are available, and codebase context if a repository exists.
- Before any technical claim, read actual project files. Cite exact paths and line numbers when possible.
- Prefer extending existing APIs, components, schemas, and flows over creating new ones.
- If information is missing, write `TBD — needs research`; do not invent filler.
- Do not generate the PRD until the final gate is answered.

## Output Location

Default PRD path:

```text
docs/prds/{kebab-case-feature-name}.prd.md
```

Create the directory before writing. Use a user-provided path if they specify one. Do not write PRDs into the skill directory.

## Workflow

### Phase 1 — Initiate

If the user supplied a feature idea, restate it in 2-3 sentences and ask whether the understanding is correct. If the input is vague or empty, ask what they want to build.

Then ask all Foundation Questions together and wait:

1. **Who** has this problem? Be specific — not just "users" but what type of person or role?
2. **What** problem are they facing? Describe the observable pain, not the assumed need.
3. **Why** can't they solve it today? What alternatives exist and why do they fail?
4. **Why now?** What changed that makes this worth building?
5. **How** will you know if you solved it? What would success look like?

### Phase 2 — Grounding: Market and Codebase Research

After foundation answers:

1. Search for similar products, competitor approaches, common patterns, anti-patterns, and recent trends. If web search is unavailable, say so and mark market evidence as TBD unless the user provides sources.
2. Explore the codebase deeply. Use search and file reads to find related functionality, APIs, UI components, database tables, types, tests, and conventions.
3. Summarize what already exists before suggesting anything new.

Present:

```markdown
**What I found:**
- {Market insights with source links, or TBD if unavailable}
- {Codebase findings with file:line references}
- {Key insight that may change the approach}
```

Then ask all Deep Dive Questions and wait:

1. **Vision**: In one sentence, what's the ideal end state if this succeeds wildly?
2. **Primary User**: Describe your most important user — their role, context, and what triggers their need.
3. **Job to Be Done**: Complete: "When [situation], I want to [motivation], so I can [outcome]."
4. **Non-Users**: Who is explicitly NOT the target?
5. **Constraints**: What limitations exist? Consider time, budget, technical, legal, regulatory, or organizational constraints.

### Phase 3 — Technical Feasibility

After deep dive answers, assess the smallest codebase-grounded solution:

1. Read actual files for related endpoints, queries, schemas, components, types, and tests.
2. Identify what partially solves the problem today.
3. Identify the smallest change that solves the core problem.
4. Identify primitives needed: query, schema, component, prop, endpoint, command, job, event, config, or documentation.
5. Identify risks and assumptions needing validation.

Present:

```markdown
**What Already Exists (verified by reading code):**
- `{file:line}` — {endpoint/component/query/type and what it does}

**Smallest Change to Solve the Problem:**
- {change}: extend/modify `{file}` — {what to do}

**Technical Context:**
- Feasibility: HIGH/MEDIUM/LOW because {reason}
- Key risk: {main concern}
- Estimated phases: {rough breakdown}
```

Then ask all Scope Questions and wait:

1. **MVP Definition**: What's the absolute minimum to test if this works?
2. **Must Have vs Nice to Have**: What 2-3 things MUST be in v1? What can wait?
3. **Key Hypothesis**: Complete: "We believe [capability] will [solve problem] for [users]. We'll know we're right when [measurable outcome]."
4. **Out of Scope**: What are you explicitly NOT building?
5. **Open Questions**: What uncertainties could change the approach?

### Phase 4 — Generate PRD

Before writing, read `references/prd-template.md`. Generate a complete PRD using all user answers, research findings, and verified codebase evidence.

Required sections:

1. Problem Statement
2. Evidence
3. Proposed Solution
4. Key Hypothesis
5. What We're NOT Building
6. Success Metrics
7. Open Questions
8. Users & Context
9. Solution Detail, including MoSCoW table and MVP scope
10. Technical Approach with verified file paths, symbols, schemas, and endpoints
11. Implementation Phases with status, dependencies, and parallelism notes
12. Decisions Log
13. Research Summary

### Phase 5 — Validate PRD

After writing the PRD, read it back and verify every technical claim against the codebase:

- File paths exist.
- Endpoint names and routes are accurate.
- Table, column, event, and config names match actual schema/code.
- Component, function, type, and interface names are accurate.
- Proposed new work does not duplicate an existing primitive.

If corrections are needed, edit the PRD directly and add `## Validation Notes` documenting corrections. If none are needed, add that all technical references were verified.

Report:

```markdown
## PRD Validated

**File**: `{prd-path}`
**Checks**: {N} file paths, {N} endpoints, {N} DB/schema references, {N} components/functions/types
**Corrections**: {count}

### Summary
- **Problem**: {one line}
- **Solution**: {one line}
- **Key Metric**: {primary success metric}

### Recommended Next Step
Review the PRD. After explicit approval, use `implement-prd-stories` or another coding skill to implement it.
```

## Documentation Output

When writing plans, reports, PRDs, briefs, findings, story tracking, scratch notes, or other generated documentation, write them under the repository-root `docs/` directory, preferably `docs/create-interactive-prd/...` or the specific `docs/` path named in the workflow. Do not use `.agents/`, `.pi/`, `.codex/`, `.claude/`, or other agent-specific directories for generated documentation.
