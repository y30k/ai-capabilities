# Visual Iteration Workflow

Use this reference while implementing or polishing a web UI, especially when screenshots, Figma exports, or inspiration sources are involved.

## Research and Inspiration

1. Search or review references that match the product context, platform, density, and screen type. Useful query patterns:
   - `premium mobile app dashboard UI`
   - `AI chat interface mobile UI`
   - `finance app card layout UI`
   - `settings screen mobile app design`
   - `bottom sheet interaction design`
   - `onboarding flow UI`
   - `enterprise SaaS dashboard UI`
   - `dark mode mobile UI`
   - `iOS glass card interface`
   - `minimal professional app UI`
2. Prefer premium references from Mobbin, Dribbble, Pinterest, Figma community files, best-in-class products in the same category, or user-provided screenshots.
3. Do not copy a design directly. Extract principles only: hierarchy, grouping, spacing, density, navigation, card structure, empty states, sheet/modal behavior, responsive behavior, and micro-interactions.
4. Do not let external inspiration override `DESIGN.md`, style JSON, screenshots, existing components, or approved theme tokens.
5. Record sources reviewed and the principles applied. If web access is unavailable, say so and ask for screenshots/links instead of inventing URLs.

## Implementation Loop

Run one to three tight iterations:

1. **Baseline**
   - Discover package manager, app framework, component library, Tailwind/theme config, and runnable dev commands.
   - Capture the current UI if it exists.
   - Identify target viewports: at minimum phone (`390x844`), tablet (`768x1024`), desktop (`1440x900`).
2. **Build**
   - Use existing components, tokens, and layout primitives before adding new abstractions.
   - Implement mobile-first responsive layout, then scale up.
   - Add real states: loading, empty, error, disabled, focus, hover/pressed, and long-content behavior when relevant.
3. **Capture**
   - Use Playwright, an in-app browser, Storybook/Ladle screenshots, or manual browser screenshots.
   - Capture the same viewports after each iteration.
   - When a target screenshot exists, compare by visual overlay or diff; otherwise compare against the design artifact checklist.
4. **Critique**
   - Check hierarchy: primary action, title, supporting copy, status, navigation.
   - Check spacing: consistent section rhythm, card padding, control gaps, alignment, and whitespace.
   - Check polish: icon sizing, truncation, empty states, focus rings, hit targets, motion restraint, and scroll behavior.
   - Check consistency: no random color, hardcoded CSS, unrelated component style, or unapproved effect.
5. **Refine**
   - Fix the highest-impact visual issues first.
   - Reduce copy after layout stabilizes.
   - Re-run screenshots and project validation commands.

## Copy Reduction Pass

Apply this after the first working UI exists:

- Shorten page headers to the fewest clear words.
- Keep descriptions to one useful sentence; remove marketing filler.
- Keep button labels to one word, or two when clarity requires it.
- Replace vague labels like `Submit`, `Click here`, and `Learn more` with action-specific labels.
- Use real product content. Do not leave lorem ipsum, placeholder text, mock data, or fake metrics.
- Prefer scannable empty states: title, one sentence, one primary action.

## Accessibility and Interaction Checklist

- Use semantic landmarks and headings in logical order.
- Ensure controls have accessible names and keyboard focus behavior.
- Keep visible focus rings; do not remove outlines without a replacement.
- Verify color contrast for normal text, muted text, borders, and disabled states.
- Provide responsive hit targets near 44px for touch controls when possible.
- Respect reduced motion for non-essential animations.
- Avoid hover-only functionality on touch screens.
- Validate overflow, truncation, and wrapping for long names, translations, and narrow screens.

## Reporting

Summarize final UI work with:

- Design sources used and principles applied.
- Files changed and reusable components/tokens introduced.
- Screenshots captured or visual checks performed by viewport.
- Validation commands run and results.
- Known follow-up if visual parity could not be fully verified.
