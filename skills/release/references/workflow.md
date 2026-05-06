# Release Workflow

## 1. Parse Intent

Identify release type, target version, branch, package manager, changelog scope, and whether publishing is authorized.

## 2. Preflight

- Ensure the working tree state is understood.
- Check current branch and remote.
- Run smoke tests or the project's fastest confidence checks.
- Detect version files and package metadata.
- Stop before publishing if preflight fails unless the user explicitly accepts risk.

## 3. Draft

- Collect commits since the previous tag or release point.
- Draft changelog/release notes grouped by feature, fix, breaking change, docs, maintenance.
- Propose version bump.
- Ask the user to approve the changelog and version.

## 4. Execute

Only after approval:

1. Update version/changelog files.
2. Run validation again.
3. Commit release changes if requested.
4. Create tag or release PR according to project convention.
5. Publish or create hosted release only with explicit authorization.
6. Update package distribution metadata if applicable.

## 5. Report

Include version, tag/PR/release URL, validation results, published artifacts, and follow-up checks.
