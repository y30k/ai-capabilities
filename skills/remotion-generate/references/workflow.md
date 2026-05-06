# Remotion Generation Workflow

## 1. Confirm Project

- Check for Remotion dependencies and config.
- Identify composition entry points and existing style/assets.
- If this is not a Remotion project, ask whether to add one or stop.

## 2. Understand Creative Brief

Clarify duration, dimensions, data inputs, branding, text, audio, animation style, and output format.

## 3. Implement

- Reuse existing components and assets where possible.
- Keep timing and constants explicit.
- Prefer deterministic data fixtures for previews.
- Handle missing assets with placeholders only if approved.

## 4. Preview and Render

Run available preview/render commands. If rendering is too expensive or unavailable, provide exact commands and what remains unverified.

## 5. Report

Include composition ID, changed files, render command, output path if produced, and known limitations.
