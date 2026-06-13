# Design Artifacts

Use this reference when creating or refreshing `DESIGN.md`, `styles.json`/`Styles.json`, or persistent agent instructions for a web UI project.

## Workflow

1. Gather source material in priority order:
   - Existing `DESIGN.md`, style JSON, Tailwind/theme config, CSS variables, component files.
   - User-provided screenshots, flows, Figma CSS/style exports, brand assets, and product copy.
   - Existing production UI patterns in the app.
   - External inspiration notes, only after internal sources are understood.
2. Extract the design language: type scale, color roles, spacing rhythm, radius, elevation, density, layout grid, component anatomy, interaction states, and copy tone.
3. Normalize values into reusable tokens. Prefer existing token names. If none exist, start with conservative defaults: Inter, Tailwind neutral palette, simple radii, restrained shadows, and Lucide or Phosphor icons.
4. Write human guidance in `DESIGN.md` and machine-readable tokens in `styles.json`.
5. If the repo uses `AGENTS.md` or the user asks for persistent guidance, update it to require agents to follow `DESIGN.md` and `styles.json` for UI work.

## DESIGN.md Template

```markdown
# Design System

## Product UI Thesis
Describe the intended feel in one paragraph: audience, platform, density, tone, and the most important visual principle.

## Source Order
1. DESIGN.md
2. styles.json / existing theme tokens
3. Provided screenshots, Figma exports, and layout images
4. Existing app design system and reusable components
5. External inspiration, translated into this product language

## Foundations
- Typography: font families, scale, weights, line heights, tracking, heading/body usage.
- Color: neutral scale, semantic roles, surface hierarchy, text contrast, borders, states.
- Spacing: base unit, section spacing, card padding, control gaps, responsive rhythm.
- Shape: radius rules by component size and container hierarchy.
- Elevation: approved shadows/borders and when to use none.
- Icons: approved set, stroke/weight, sizing, alignment.

## Layout and Responsiveness
Document mobile-first behavior, breakpoints, max widths, grids, navigation changes, safe areas, and overflow rules.

## Components
For each primary component, document anatomy, variants, states, spacing, and content rules.

## Content Rules
Document voice, title length, description length, button-label rules, empty-state guidance, and prohibited placeholder copy.

## Interaction and Accessibility
Document keyboard behavior, focus rings, reduced motion, loading states, validation states, ARIA/label requirements, and contrast expectations.

## Do / Do Not
List approved patterns and explicit bans: random colors, unapproved shadows, decorative gradients/glow/noise, hardcoded CSS, unrelated patterns, placeholder content, and mock data.

## Validation
List required lint/build/tests, responsive viewports, accessibility checks, and visual-regression process.
```

## styles.json Starter Schema

Preserve an existing schema if present. Otherwise create a compact, versioned object like this:

```json
{
  "version": 1,
  "sources": [
    {
      "type": "screenshot|figma|existing-app|external-reference",
      "name": "Short source name",
      "pathOrUrl": "Local path or URL when available",
      "notes": "Design principles extracted, not copied"
    }
  ],
  "defaults": {
    "fontFamily": "Inter",
    "icons": "lucide|phosphor",
    "componentLibrary": "existing|shadcn-ui|radix|custom",
    "cssStrategy": "tailwind|css-modules|css-variables|other"
  },
  "tokens": {
    "fontFamily": {
      "sans": ["Inter", "ui-sans-serif", "system-ui", "sans-serif"]
    },
    "fontSize": {
      "xs": "0.75rem",
      "sm": "0.875rem",
      "base": "1rem",
      "lg": "1.125rem",
      "xl": "1.25rem",
      "2xl": "1.5rem",
      "3xl": "1.875rem"
    },
    "colors": {
      "neutral": {
        "50": "#fafafa",
        "100": "#f5f5f5",
        "200": "#e5e5e5",
        "300": "#d4d4d4",
        "400": "#a3a3a3",
        "500": "#737373",
        "600": "#525252",
        "700": "#404040",
        "800": "#262626",
        "900": "#171717",
        "950": "#0a0a0a"
      },
      "semantic": {
        "background": "neutral.50",
        "surface": "#ffffff",
        "surfaceMuted": "neutral.100",
        "border": "neutral.200",
        "text": "neutral.950",
        "textMuted": "neutral.600",
        "primary": "neutral.950",
        "primaryText": "#ffffff",
        "danger": "#dc2626",
        "success": "#16a34a",
        "warning": "#d97706"
      }
    },
    "space": {
      "1": "0.25rem",
      "2": "0.5rem",
      "3": "0.75rem",
      "4": "1rem",
      "5": "1.25rem",
      "6": "1.5rem",
      "8": "2rem",
      "10": "2.5rem",
      "12": "3rem",
      "16": "4rem"
    },
    "radius": {
      "sm": "0.375rem",
      "md": "0.5rem",
      "lg": "0.75rem",
      "xl": "1rem",
      "full": "9999px"
    },
    "shadow": {
      "none": "none",
      "sm": "0 1px 2px rgba(15, 23, 42, 0.06)",
      "md": "0 8px 24px rgba(15, 23, 42, 0.08)"
    }
  },
  "components": {
    "button": {
      "labelMaxWords": 2,
      "height": { "sm": "2rem", "md": "2.5rem", "lg": "3rem" },
      "radius": "md",
      "primary": { "background": "primary", "text": "primaryText" }
    },
    "card": {
      "background": "surface",
      "border": "1px solid token(colors.semantic.border)",
      "radius": "xl",
      "padding": { "mobile": "4", "desktop": "6" }
    }
  },
  "responsive": {
    "mobileFirst": true,
    "viewports": ["390x844", "768x1024", "1440x900"],
    "breakpoints": { "sm": "640px", "md": "768px", "lg": "1024px", "xl": "1280px" }
  },
  "forbidden": [
    "unapproved gradients",
    "glow effects",
    "decorative noise",
    "random colors",
    "hardcoded CSS that bypasses tokens",
    "placeholder copy",
    "mock data in production UI"
  ]
}
```

## AGENTS.md Snippet

```markdown
## UI/UX Implementation Rules

For web UI work, strictly follow `DESIGN.md` and `styles.json`/`Styles.json` before changing layout, styling, copy, or components. Use existing reusable components and theme tokens first. Implement mobile-first responsive behavior across phone, tablet, and desktop. Do not add random colors, decorative gradients/glow/noise, unapproved shadows/borders, hardcoded CSS, placeholder copy, or mock data unless the task explicitly requires it.
```
