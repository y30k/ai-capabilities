# FOSS Tooling and Infrastructure

Use this reference when a user asks how to make high-quality web UI iteration repeatable, visual, and measurable.

## Minimal Stack

Stand up this first in most repos:

- Root design artifacts: `DESIGN.md` plus `styles.json`/`Styles.json`.
- Persistent agent rules: `AGENTS.md` UI section that requires the design artifacts.
- Static advisory audit: this skill's `scripts/ui_static_audit.py` in local scripts or CI.
- Browser screenshots: Playwright Test for deterministic viewport captures.
- Accessibility smoke checks: `@axe-core/playwright` or `axe-core` where a browser harness exists.

## Component Workshop

Choose one if the app has reusable components or multiple screens:

- **Storybook**: broad ecosystem, docs, interaction tests, a11y addon, visual-regression integrations.
- **Ladle**: lightweight React component workshop with fast startup.
- **Histoire**: useful for Vue/Svelte component stories.

Keep stories close to real app states: empty, loading, error, dense content, mobile layout, and dark mode if supported.

## Visual Regression

FOSS options:

- **Playwright Test screenshots**: `expect(page).toHaveScreenshot()` for app-level or component-level golden screenshots.
- **BackstopJS**: scenario-based visual regression over URLs and viewports.
- **Loki**: screenshot testing for Storybook stories.
- **RegSuit**: visual regression workflow with pluggable storage.
- **pixelmatch** or **looks-same**: low-level image diff tools for custom scripts.

Start with a small golden set: primary dashboard/page, one form, one modal/sheet, one empty state, and one mobile navigation state.

## Accessibility and Quality Gates

- **axe-core / @axe-core/playwright**: browser-level accessibility assertions.
- **eslint-plugin-jsx-a11y**: React static accessibility linting.
- **pa11y**: CLI accessibility checks for rendered pages.
- **Lighthouse CI**: performance/accessibility/best-practices budgets for key routes.
- **stylelint**: CSS quality, with custom rules or conventions for token usage.

## Design Tokens

- **Style Dictionary**: generate CSS variables, Tailwind config fragments, TypeScript constants, or platform tokens from JSON.
- **Tailwind CSS theme extension**: map `styles.json` roles into `tailwind.config.*` or CSS variables.
- **Ajv**: validate `styles.json` against a JSON Schema if token drift becomes a problem.

Prefer one source of truth. Do not maintain divergent token values in JSON, Tailwind, CSS variables, and component code without generation or checks.

## UI Libraries

Use only if they match the app stack and are approved for dependencies:

- **shadcn/ui** with **Radix UI** primitives for accessible React components.
- **Lucide** or **Phosphor** for consistent iconography.
- **class-variance-authority** and **tailwind-merge** for component variants.
- **Tailwind CSS** with neutral palette and semantic tokens for fast consistent styling.

If the project already has a component system, extend it instead of adding another library.

## Design and Reference Management

- **Penpot**: FOSS design tool alternative for collaborative UI source files.
- Local `docs/ui-references/` or `docs/design-references/`: store user-approved screenshots, source URLs, and notes about principles applied.
- Do not commit copyrighted third-party screenshots unless the repo policy allows it; source links and extracted principles are usually safer.

## CI Script Examples

Adapt names to the project package manager:

```json
{
  "scripts": {
    "ui:audit": "python3 skills/design-polished-web-ui/scripts/ui_static_audit.py --root . app components",
    "test:visual": "playwright test --grep @visual",
    "test:a11y": "playwright test --grep @a11y",
    "storybook": "storybook dev -p 6006",
    "lighthouse": "lhci autorun"
  }
}
```

For projects that will not vendor this skill, copy `ui_static_audit.py` into a repo-local script path such as `scripts/ui_static_audit.py` and update the script command.
