---
name: design-polished-web-ui
description: |
  Design, implement, audit, and visually iterate polished, accessible, responsive web interfaces using current user direction, project design artifacts, screenshots or Figma exports, existing components and tokens, and breakpoint validation. Use when the user asks to build or improve a web interface, dashboard, component, screen, flow, design system, DESIGN.md or styles.json, screenshot match, UI polish pass, responsive layout, visual regression workflow, accessibility polish, or concise UI copy in React, Next.js, Vue, Svelte, Astro, or another web stack.
---

# Design Polished Web UI

Use this skill to turn web UI work into a repeatable design-system-driven loop: gather visual direction, encode it into design artifacts, implement with existing components and tokens, visually inspect across breakpoints, reduce copy, and iterate until polished.

## Boundary

- Treat this as a coding skill when the user asks to implement UI. If the user only asks for planning, create design artifacts or recommendations and stop.
- Ask before adding dependencies, replacing the component library, introducing a new design system, committing third-party reference screenshots, or staging a submission candidate unless staging was already requested.
- Use external inspiration only for principles. Do not clone designs, bypass license restrictions, or let external references override project-specific direction.

## Source Order

Prioritize UI decisions in this order:

1. Current user instructions and acceptance criteria.
2. User-provided screenshots, Figma exports, and layout references.
3. Existing `DESIGN.md`, `styles.json`/`Styles.json`, and equivalent design artifacts.
4. Existing components, theme tokens, CSS variables, and nearby product patterns.
5. External inspiration translated into the product language.

Explicit current user direction overrides stale artifacts; ask when sources conflict materially.

## Runbook

1. **Inspect the project**
   - Discover package manager, framework, component library, styling approach, route structure, and runnable validation commands.
   - Read existing `DESIGN.md`, style JSON, Tailwind/theme config, global CSS, component primitives, and relevant screens.
   - Ask for screenshots, Figma CSS, or reference links when pixel matching or a new direction is expected and none are available.

2. **Create or refresh design artifacts when needed**
   - Read `references/design-artifacts.md` before creating/updating `DESIGN.md`, `styles.json`, or `AGENTS.md`.
   - Derive tokens from provided design sources and existing code before inventing values.
   - If no design direction exists, preserve installed fonts, icons, components, and palette. Use conservative system-font, neutral, low-decoration defaults only for unspecified choices; ask before adding a font, icon package, CSS framework, or design-system dependency.

3. **Research inspiration deliberately**
   - Read `references/visual-iteration.md` when using Mobbin, Dribbble, Pinterest, Figma, product screenshots, or browser research.
   - Search for references that match the screen type, platform, density, and product category.
   - Record sources reviewed and principles applied, such as hierarchy, spacing, grouping, density, card structure, navigation, empty states, sheets/modals, or responsive behavior.

4. **Implement through the existing system**
   - Use existing components and tokens first; add or extend reusable components when a pattern repeats.
   - Prefer the project's existing primitives. Add shadcn/ui or Radix primitives only when already present or explicitly approved.
   - Implement mobile-first responsive behavior for phone, tablet, and desktop.
   - Include real UI states: loading, empty, error, disabled, focus, hover/pressed, long content, and narrow screens when relevant.
   - Keep language minimal: short headings, one-sentence descriptions, and one- or two-word button labels when possible.

5. **Avoid unapproved polish drift**
   - Do not add random colors, gradients, glow effects, decorative noise, custom shadows, unapproved borders, hardcoded CSS, unrelated UI patterns, placeholder content, or mock data unless explicitly required.
   - Do not solve layout issues with arbitrary one-off values if a token, component prop, or theme extension should exist.

6. **Visually iterate**
   - Run the app or component workshop and capture at least mobile, tablet, and desktop views when tooling allows.
   - Compare against provided screenshots by overlay/diff when possible; otherwise critique against the source order and design checklist.
   - Run one to three refinement passes, fixing hierarchy, spacing, alignment, copy, component states, and responsive issues before broad refactors.
   - Optionally run the bundled advisory audit: `scripts/ui_static_audit.py --root . <ui-paths>`. When design sources use non-default paths, pass `--design-guidance PATH` and/or `--design-tokens PATH`; use `--skip-artifact-checks` only after explicit project-level review.
   - When modifying the audit itself, run `python3 -m unittest discover -s tests -p 'test_ui_static_audit.py'` from this skill directory; the regression suite is `tests/test_ui_static_audit.py`.

7. **Validate and report**
   - Run relevant lint, typecheck, test, build, accessibility, and visual-regression commands.
   - Summarize design sources, files changed, reusable tokens/components introduced, viewports checked, validation results, and any visual gaps.
   - Before initial PR/MR submission, obtain staging authorization unless already granted; snapshot cached/unstaged diffs, stage only the approved UI hunks, verify `git diff --cached --check` and candidate isolation, then hand the exact staged UI candidate to `check-production-readiness` and later `submit-change-request`. Without staging authorization, return the exact staging plan instead.

## Tooling Setup

Read `references/tooling.md` when the user asks for infrastructure, CI gates, visual regression, component workshops, design-token pipelines, or FOSS tooling recommendations.

## Documentation Output

Write durable inspiration notes, UI audits, screenshot indexes, and implementation reports under `docs/design-polished-web-ui/` or another user-specified path under `docs/`. Never store generated documentation in agent-state directories such as `.agents/`, `.pi/`, `.codex/`, or `.claude/`.
