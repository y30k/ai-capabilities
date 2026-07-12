# Remotion Generation Workflow

## 1. Confirm Project

- Check for Remotion dependencies and config.
- Identify composition entry points and existing style/assets.
- If this is not a Remotion project, ask whether to add one or stop.

## 2. Understand Creative Brief

Clarify duration, dimensions, data inputs, branding, text, audio, animation style, and output format. Classify props and asset URLs for credentials, signed access, customer/employee data, or other private production values; replace them with redacted schemas or deterministic synthetic fixtures before commands or reports.

## 3. Implement

- Reuse existing components and assets where possible.
- Keep timing and constants explicit.
- Prefer deterministic data fixtures for previews.
- Handle missing assets with placeholders only if approved.

## 4. Apply Remotion Rules

- Read the lockfile, `package.json` scripts, Remotion config, root and composition registrations, and installed-version CLI help before choosing commands.
- Reuse registered composition IDs and project asset-loading conventions.
- Drive deterministic animation from `useCurrentFrame()` and the composition `fps`; follow existing interpolation and sequence patterns instead of wall-clock timers or CSS transitions.
- Keep network data out of renders unless the project already snapshots or validates it.
- Inject required secrets only through the project's approved environment/secret mechanism. Never embed secret or private prop values in CLI arguments, shell history, tool output, committed fixtures, or durable documentation.
- Do not guess CLI flags or silently change dimensions, fps, duration, codecs, or input props.

## 5. Preview and Render

Enumerate compositions with the installed project script or CLI and verify the target ID, dimensions, fps, duration, and redacted prop schema. Run the cheapest existing validation first, such as typecheck, tests, or a short preview or still, then run the project render command with secret-safe injection. Ask before a full render when cost, duration, external services, or overwrite risk is material. Record a sanitized reproducible command, exit status, output path, and anything not rendered; replace sensitive arguments/values with named placeholders before logging.

## 6. Stage for Submission When Authorized

Before an initial readiness handoff, obtain staging authorization unless the user already requested candidate preparation. Snapshot `git status --short`, working-tree diffs, cached diffs, and all untracked paths. Inspect every intended untracked composition, asset, fixture, or output for scope and sensitive data before adding it to the explicit path/hunk allowlist. Stop on overlap or unrelated pre-staged content unless an isolation plan is approved; stage only allowlisted files/hunks. Then verify cached and unstaged views, `git diff --cached --check`, that every intended tracked/untracked file is cached, and that no unrelated file was absorbed. Do not commit or push.

## 7. Report

Include composition ID, changed files, fps, frame count or duration, dimensions, redacted prop schema or synthetic fixture name, validation output, sanitized render command and exit status, output path if produced, locally verified audio/assets, redaction performed, and known limitations. Never persist raw secrets, signed URLs, or private prop values. Before initial PR/MR submission, hand off to `check-production-readiness` only when the candidate is staged and verified; otherwise return the staging plan. Use `submit-change-request` only after readiness.
