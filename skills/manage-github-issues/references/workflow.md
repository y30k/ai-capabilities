# GitHub Issue Management Workflow

## Path A: Create Issue

1. Understand the problem report.
2. Check existing issues for duplicates if `gh` is available.
3. Inspect code or run a minimal reproduction when practical.
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
2. Detect duplicates and link likely canonical issues.
3. Suggest labels, priority, missing information, and owner/area.
4. Find PRs that may close or relate to issues.
5. Identify stale issues that need a nudge, closure, or reproduction request.
6. Summarize recommended actions; ask before making bulk changes.

## Output

Return a table of issues, recommended action, confidence, and commands/comments to apply if approved.
