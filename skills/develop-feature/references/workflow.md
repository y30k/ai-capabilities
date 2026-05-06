# Feature Development Workflow

## Common Setup

1. Clarify the input: approved idea, existing plan/spec, or app brief. If the input is an unreviewed PRD, route to `create-interactive-prd` for planning or `implement-prd-stories` after approval.
2. Inspect the repository for stack, commands, patterns, tests, and contribution rules.
3. Create `.agents/artifacts/develop-feature/{slug}/` for plans and validation notes when useful.
4. Keep changes small and reversible.

## Planning Gate

When this workflow creates or materially changes an implementation plan, stop before source-code edits and ask for user approval. Implementation begins only after the user approves the plan or explicitly pre-authorizes implementation.

## Path A: Idea to PR

1. Restate the idea and ask key scope questions if missing.
2. Research existing code paths and similar features.
3. Write a short implementation plan with tasks, risks, non-goals, and validation commands.
4. Present the plan and wait for approval.
5. Implement approved tasks incrementally.
6. Run validation.
7. Summarize diff and draft PR body.

## Path B: Plan to PR

1. Read the plan and extract tasks, dependencies, acceptance criteria, and out-of-scope items.
2. Confirm the plan is approved. If not, summarize it and ask before coding.
3. Implement in dependency order.
4. Run validation after meaningful milestones.
5. Draft PR body referencing the plan and completed checks.

## Path C: Implement Only

Use when the user explicitly wants direct coding, not planning ceremony.

1. Read the plan/spec/request.
2. Confirm the first implementation slice is clear.
3. Implement the smallest complete slice.
4. Run validation.
5. Report changed files, tests, and remaining work.

## Path D: Guided Plan-Implement-Validate

Loop until the user accepts or a max iteration count is reached:

1. **Plan**: propose the next small slice.
2. **Gate**: ask user to approve or revise.
3. **Implement**: make only approved changes.
4. **Validate**: run checks and inspect results.
5. **Feedback**: ask whether to continue, adjust, or stop.

## Path E: Adversarial Build

Use for large greenfield builds or high-risk features. Preserve the same approval boundary: plan first, implement only after approval.

1. Builder proposes the smallest working version and validation plan.
2. User approves the build slice.
3. Builder implements the approved slice.
4. Reviewer attacks assumptions, edge cases, UX, tests, security, and maintainability.
5. Builder fixes the highest-value findings.
6. Repeat until validation passes or diminishing returns are clear.

## Final Report

Include:

- What was built.
- Changed files.
- Validation commands and results.
- Remaining risks or follow-ups.
- PR title/body if requested.
