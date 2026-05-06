# Code Health Workflow

## 1. Scope

Clarify target area, allowed behavior changes, validation commands, and risk tolerance.

## 2. Baseline

- Inspect project structure and dependency boundaries.
- Identify tests and commands that prove behavior.
- Capture current failures before changing code.

## 3. Architecture Sweep Path

1. Find complexity hotspots, duplicated patterns, dead code, leaky abstractions, and unclear boundaries.
2. Read representative files before judging.
3. Prioritize changes by user value, risk, and reversibility.
4. Produce a plan with phases and validation for each phase.

## 4. Safe Refactor Path

1. Choose one small refactor slice.
2. Preserve public behavior and interfaces unless explicitly approved.
3. Make mechanical changes first, semantic changes second.
4. Run targeted validation after each slice.
5. Stop and report if validation fails unexpectedly.

## 5. Report

Include changed files, complexity removed, behavior preserved, validation results, and follow-up opportunities.
