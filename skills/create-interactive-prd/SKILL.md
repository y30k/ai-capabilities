---
name: create-interactive-prd
description: |
  Guide a gated, planning-only workflow that turns a product idea into a problem-first, hypothesis-driven PRD through user interviews, market and repository research, feasibility assessment, generation, and validation. Use when the user asks to create or revise a PRD, product requirements document, product or feature requirements specification, interactive PRD, or evidence-backed product specification from an idea. Read repository files for feasibility, but do not modify source code or implement; stop after PRD validation for user review.
---

# Create Interactive PRD

Use this skill to run an interactive PRD interview directly in the coding-agent chat. The workflow focuses on the problem before the solution, gathers evidence before scope, verifies codebase claims by reading files, then generates and validates an implementation-ready PRD.

## Boundary

This is a **planning and requirements skill only**. It may read project files to verify feasibility, but it must not modify source code, implement features, create branches, or open PRs. After validating the PRD, stop and ask the user to review it. Implementation requires separate explicit requests. For full AI-DLC flow, use `create-technical-design`, then `create-test-strategy`, then `create-prd-work-items`, then `implement-prd-stories` after work items are approved and unblocked.

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
2. Explore the codebase deeply. Use search and file reads to find related functionality, APIs, UI components, database tables, types, tests, and conventions. If no repository is available, state the limitation, mark repository-dependent findings and feasibility `TBD — needs research`, and never invent paths or symbols.
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

After deep dive answers, assess the smallest codebase-grounded solution when a repository is available:

1. Read actual files for related endpoints, queries, schemas, components, types, and tests.
2. Identify what partially solves the problem today.
3. Identify the smallest change that solves the core problem.
4. Identify primitives needed: query, schema, component, prop, endpoint, command, job, event, config, or documentation.
5. Identify risks and assumptions needing validation.

When no repository is available, do not perform steps 1–4 as if evidence exists. Keep existing primitives, file paths, smallest code change, and feasibility `TBD — needs research`; identify only product-level risks and assumptions, and mark repository validation `NOT RUN — repository unavailable`.

Present:

```markdown
**What Already Exists:**
- `{file:line}` — {verified primitive and what it does}
- Or: TBD — needs research; repository unavailable and no primitives verified

**Smallest Change to Solve the Problem:**
- {change}: extend/modify `{file}` — {what to do}
- Or: TBD — needs research; implementation path not verified

**Technical Context:**
- Feasibility: HIGH/MEDIUM/LOW because {repository-grounded reason}, or TBD — needs research; repository validation NOT RUN
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

Use every template section in the documented order. Do not omit or duplicate sections; mark unknown content `TBD — needs research`.

### Phase 5 — Validate PRD

After writing the PRD, read it back and verify every technical claim against the codebase:

- File paths exist.
- Endpoint names and routes are accurate.
- Table, column, event, and config names match actual schema/code.
- Component, function, type, and interface names are accurate.
- Proposed new work does not duplicate an existing primitive.

If corrections are needed, edit the PRD directly and add `## Validation Notes` documenting corrections. If repository evidence was available and no corrections are needed, state that all technical references were verified. If no repository was available, keep feasibility and repository-dependent claims `TBD — needs research`, state that repository validation was NOT RUN, and never label the technical references verified.

Report:

```markdown
## PRD Validation Result

**File**: `{prd-path}`
**Repository validation**: PASSED | NOT RUN — repository unavailable
**Checks**: {N} file paths, {N} endpoints, {N} DB/schema references, {N} components/functions/types
**Corrections**: {count}

### Summary
- **Problem**: {one line}
- **Solution**: {one line}
- **Key Metric**: {primary success metric}

### Recommended Next Step
Review the PRD. After explicit approval, use `create-technical-design` to refine implementation architecture, `create-test-strategy` to define validation, then `create-prd-work-items` to create dependency-linked tracker stories. Use `implement-prd-stories` only after a story is approved and unblocked.
```

## Documentation Output

Write the PRD to the Output Location above. Write any additional generated documentation under repository-root `docs/`, never under agent-state directories such as `.agents/`, `.pi/`, `.codex/`, or `.claude/`.
