---
name: design-polished-web-ui
description: |
  Design, implement, and iterate polished responsive web UI/UX using project design artifacts, screenshots or Figma style exports, existing components, premium inspiration, and visual/accessibility validation. Use when the user asks to build or improve a web interface, dashboard, component, screen, flow, design system, DESIGN.md/styles.json, screenshot match, UI polish pass, responsive layout, visual regression workflow, or concise UI copy. Applies to web stacks such as React, Next.js, Vue, Svelte, Astro, Tailwind, ShadCN/Radix, CSS modules, and custom component systems.
---

# Design Polished Web UI

Use this skill to turn web UI work into a repeatable design-system-driven loop: gather visual direction, encode it into design artifacts, implement with existing components and tokens, visually inspect across breakpoints, reduce copy, and iterate until polished.

## Boundary

- Treat this as a coding skill when the user asks to implement UI. If the user only asks for planning, create design artifacts or recommendations and stop.
- Ask before adding dependencies, replacing the component library, introducing a new design system, or committing third-party reference screenshots.
- Use external inspiration only for principles. Do not clone designs, bypass license restrictions, or let external references override project-specific direction.

## Source Order

Prioritize UI decisions in this order:

1. `DESIGN.md` and `styles.json`/`Styles.json`.
2. Provided screenshots, Figma exports, layout images, and user instructions.
3. Existing app design system, theme tokens, CSS variables, and reusable components.
4. Existing product UI patterns in nearby screens.
5. External premium UI inspiration translated into the product language.

## Runbook

1. **Inspect the project**
   - Discover package manager, framework, component library, styling approach, route structure, and runnable validation commands.
   - Read existing `DESIGN.md`, style JSON, Tailwind/theme config, global CSS, component primitives, and relevant screens.
   - Ask for screenshots, Figma CSS, or reference links when pixel matching or a new direction is expected and none are available.

2. **Create or refresh design artifacts when needed**
   - Read `references/design-artifacts.md` before creating/updating `DESIGN.md`, `styles.json`, or `AGENTS.md`.
   - Derive tokens from provided design sources and existing code before inventing values.
   - If no design direction exists, default to Inter, Lucide or Phosphor icons, Tailwind neutral palette, modern minimal spacing, restrained borders/shadows, and consistent reusable components.

3. **Research inspiration deliberately**
   - Read `references/visual-iteration.md` when using Mobbin, Dribbble, Pinterest, Figma, product screenshots, or browser research.
   - Search for references that match the screen type, platform, density, and product category.
   - Record sources reviewed and principles applied, such as hierarchy, spacing, grouping, density, card structure, navigation, empty states, sheets/modals, or responsive behavior.

4. **Implement through the existing system**
   - Use existing components and tokens first; add or extend reusable components when a pattern repeats.
   - Prefer ShadCN/Radix/Coss UI-style primitives only when already present or explicitly approved.
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
   - Optionally run the bundled advisory audit: `scripts/ui_static_audit.py --root . <ui-paths>`.

7. **Validate and report**
   - Run relevant lint, typecheck, test, build, accessibility, and visual-regression commands.
   - Summarize design sources, files changed, reusable tokens/components introduced, viewports checked, validation results, and any visual gaps.

## Tooling Setup

Read `references/tooling.md` when the user asks for infrastructure, CI gates, visual regression, component workshops, design-token pipelines, or FOSS tooling recommendations.

## Documentation Output

When writing durable notes, inspiration summaries, UI audits, screenshots indexes, or implementation reports, write them under the repository-root `docs/` directory, preferably `docs/design-polished-web-ui/`. Do not use `.agents/`, `.pi/`, `.codex/`, `.claude/`, or other agent-specific directories for generated documentation.
