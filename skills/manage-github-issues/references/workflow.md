# GitHub Issue Management Workflow

## Path A: Create Issue

1. Understand the problem report.
2. Check existing issues for duplicates if `gh` is available.
3. Inspect code read-only or run a minimal, non-destructive reproduction when practical; report when reproduction is unsafe or unavailable.
4. Draft the issue with:
   - title
   - problem statement
   - reproduction steps
   - expected vs actual behavior
   - environment
   - evidence/logs/screenshots if provided
   - suspected area and labels
5. Ask before posting unless the user explicitly authorized posting.

## Path B: Triage Backlog

1. List relevant open issues.
2. Identify likely duplicates and propose the canonical issue and links.
3. Suggest labels, priority, missing information, and owner/area.
4. Find PRs that may close or relate to issues.
5. Identify stale issues that need a nudge, closure, or reproduction request.
6. Summarize proposed actions and ask before any GitHub mutation unless the user already authorized it.

## Output

- **Create:** Return the proposed title and issue body, duplicate-search result, reproduction status, suggested labels, and whether posting is pending approval.
- **Triage:** Return a table with issue, evidence, proposed action, confidence, and exact comment or field change pending approval.
- Distinguish confirmed facts from suspected causes; do not present a likely duplicate or fix as certain without evidence.
