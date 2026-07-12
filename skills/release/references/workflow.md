# Release Workflow

## 1. Parse Intent

Identify release type, target version, branch, package manager, changelog scope, and whether publishing is authorized.

## 2. Preflight

- Inspect staged, unstaged, and untracked state without modifying it.
- Identify the release branch and upstream, previous release point, version sources, package metadata, repository release policy, signing or provenance requirements, and release-specific integrity commands for versioning, changelog, packaging, signing, artifacts, tags, and publishing.
- Verify the release source OID has pre-submission production-readiness evidence plus completed PR/MR review and, when applicable, remediation/integration evidence bound to the provider-verified final head with required CI/CD for that exact OID, or an explicitly authorized fast-track record. Treat missing or stale-head evidence as a release blocker; verify it rather than rerunning a separate readiness phase.
- Fetch remote tag or release state only when network access is authorized.
- Stop before any version edit, commit, tag, push, hosted release, or publish when the target is ambiguous, the candidate is unexpectedly dirty, the target version or tag already exists locally or remotely, or a mandatory gate fails.
- Record any explicit waiver with its scope and approver; never treat general risk acceptance as authorization to publish.

## 3. Draft and Approve Actions

- Collect commits since the previous tag or release point.
- Draft changelog or release notes grouped by feature, fix, breaking change, documentation, and maintenance.
- Propose the version, reviewed source commit, target branch/tag, expected release-file edits, and release-specific validation plan.
- Present an action manifest that separately lists file edits, release commit, tag creation, tag push, hosted release creation, and each artifact or registry publish, with dependencies between them.
- Reject an invalid manifest before execution. Choose one source node: when release files change, enforce `approved release-file edits → release commit`; when no release files change, use the already reviewed clean `HEAD`. From that source node enforce `tag creation → tag push → hosted release` whenever those actions apply; a downstream action cannot be approved or executed while its applicable predecessor is omitted or failed. Every artifact/registry publish must declare its applicable source dependency—at minimum the chosen clean source commit, plus tag creation/tag push when repository policy or artifact identity is tag-based. Never let a hosting API implicitly create an unapproved remote tag, and never tag an older `HEAD` while approved release files remain uncommitted.
- Ask the user to approve the draft and each externally visible or irreversible action. Approval of notes or version does not authorize commit, tag, push, release creation, or publishing.

## 4. Execute

Only after action-specific approval:

1. Update only approved version and changelog files.
2. Run only applicable release-specific integrity checks caused by the approved version, changelog, packaging, signing, artifact, tag, or publish mechanics; do not rerun the full implementation-readiness gauntlet.
3. If release files changed, require the approved release-commit action, commit only those files, and record the resulting full SHA as the expected tag target. If no release files changed, record the already reviewed clean `HEAD` as the expected tag target.
4. Immediately before tagging, require a clean repository state, verify `HEAD` equals the expected tag-target SHA, and recheck that the version/tag is collision-free locally and remotely. Create the approved tag explicitly at that SHA and verify the tag resolves to it.
5. Perform tag push, hosted release creation, and each publish only when its manifest dependencies succeeded, stopping on the first failure.
6. Never overwrite or move an existing tag, force-push, expose credentials, or blindly retry a publish that may have succeeded.
7. When an action partially succeeds, preserve evidence and report the exact safe recovery step instead of continuing automatically.

## 5. Report

Include the reviewed source commit, resulting release commit, verified tag-target SHA, and previous release point; version files changed; release-specific commands and exit results; dependency-valid approved action manifest; created local and remote identifiers or URLs, artifact checksums when available, skipped or blocked actions, partial-failure recovery, and the next observation window. Hand completed releases to `observe-release`.
