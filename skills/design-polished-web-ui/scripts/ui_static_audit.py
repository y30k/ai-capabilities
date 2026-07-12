#!/usr/bin/env python3
"""Static UI polish audit for web projects.

Heuristically flags design-system drift and copy bloat. It is advisory by default;
use --fail-on-findings in CI after tuning ignores.
"""

from __future__ import annotations

import argparse
from bisect import bisect_right
import json
import os
import re
import sys
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable

SKIP_DIRS = {
    ".git",
    ".hg",
    ".svn",
    ".next",
    ".nuxt",
    ".svelte-kit",
    "node_modules",
    "bower_components",
    "dist",
    "build",
    "out",
    "coverage",
    "vendor",
}

DESIGN_GUIDANCE_CANDIDATES = (
    "DESIGN.md",
    "design.md",
    "STYLEGUIDE.md",
    "docs/DESIGN.md",
    "docs/design.md",
    "docs/design-system.md",
)

DESIGN_TOKEN_CANDIDATES = (
    "styles.json",
    "Styles.json",
    "tokens.json",
    "design-tokens.json",
    "tailwind.config.js",
    "tailwind.config.cjs",
    "tailwind.config.mjs",
    "tailwind.config.ts",
)

EXTENSIONS = {
    ".astro",
    ".css",
    ".htm",
    ".html",
    ".js",
    ".jsx",
    ".mjs",
    ".sass",
    ".scss",
    ".svelte",
    ".ts",
    ".tsx",
    ".vue",
}

CHECKS = [
    (
        "hardcoded-color",
        re.compile(r"(?<![A-Za-z0-9_])#[0-9A-Fa-f]{3,8}\b|\b(?:rgb|rgba|hsl|hsla)\s*\("),
        "Prefer theme tokens from styles.json/Tailwind config over raw colors.",
    ),
    (
        "inline-style",
        re.compile(r"\bstyle\s*=\s*(?:\{\{|[\"'])"),
        "Prefer reusable components, class utilities, or design tokens over inline styles.",
    ),
    (
        "tailwind-arbitrary-value",
        re.compile(r"\b(?:bg|text|border|ring|shadow|from|via|to|rounded|p|px|py|m|mx|my|gap|w|h|min-w|max-w|min-h|max-h|top|right|bottom|left)-\[[^\]]+\]"),
        "Review arbitrary Tailwind values; promote repeated values into tokens/components.",
    ),
    (
        "decorative-effect",
        re.compile(r"gradient|glow|noise|text-shadow|box-shadow|drop-shadow|shadow-\[|backdrop-blur|blur-", re.IGNORECASE),
        "Review gradients, glow, noise, blur, and shadow effects; confirm they use approved tokens and project patterns.",
    ),
    (
        "placeholder-copy",
        re.compile(r"lorem ipsum|placeholder|dummy|mock data|sample data|todo copy|coming soon", re.IGNORECASE),
        "Replace placeholder/mock copy with real product content or empty states.",
    ),
]

BUTTON_RE = re.compile(r"<(?:button|Button)\b[^>]*>(.*?)</(?:button|Button)>", re.DOTALL)
HEADING_RE = re.compile(r"<h([1-3])\b[^>]*>(.*?)</h\1>", re.DOTALL | re.IGNORECASE)
TAG_RE = re.compile(r"<[^>]+>|\{[^}]*\}")
WORD_RE = re.compile(r"[A-Za-z0-9][A-Za-z0-9'’-]*")


@dataclass
class Finding:
    check: str
    path: str
    line: int
    excerpt: str
    guidance: str


def walk_files(path: Path) -> Iterable[Path]:
    if path.is_file():
        yield path
        return

    def raise_walk_error(exc: OSError) -> None:
        raise exc

    for directory, dirnames, filenames in os.walk(path, onerror=raise_walk_error):
        dirnames[:] = sorted(name for name in dirnames if name not in SKIP_DIRS)
        for filename in sorted(filenames):
            yield Path(directory) / filename


def iter_files(paths: Iterable[Path], root: Path) -> Iterable[Path]:
    seen: set[Path] = set()
    for path in sorted(set(paths), key=str):
        for child in walk_files(path):
            if not child.is_file() or child.suffix not in EXTENSIONS:
                continue
            resolved = child.resolve()
            if not resolved.is_relative_to(root):
                raise ValueError(f"scan target escapes --root: {child}")
            if resolved in seen:
                continue
            seen.add(resolved)
            yield resolved


def line_number(newline_offsets: list[int], index: int) -> int:
    return bisect_right(newline_offsets, index) + 1


def clean_text(html: str) -> str:
    return " ".join(TAG_RE.sub(" ", html).split())


def excerpt(line: str) -> str:
    stripped = line.strip()
    return stripped[:180] + ("…" if len(stripped) > 180 else "")


def audit_file(path: Path, root: Path) -> list[Finding]:
    rel = str(path.relative_to(root)) if path.is_relative_to(root) else str(path)
    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError) as exc:
        return [
            Finding(
                "unreadable-file",
                rel,
                1,
                f"{type(exc).__name__}: {exc}",
                "Make the file readable UTF-8 text or exclude it explicitly before relying on audit results.",
            )
        ]

    findings: list[Finding] = []
    lines = text.splitlines()
    newline_offsets = [index for index, char in enumerate(text) if char == "\n"]

    for check, pattern, guidance in CHECKS:
        for match in pattern.finditer(text):
            line = line_number(newline_offsets, match.start())
            findings.append(Finding(check, rel, line, excerpt(lines[line - 1] if line - 1 < len(lines) else ""), guidance))

    for match in BUTTON_RE.finditer(text):
        label = clean_text(match.group(1))
        words = WORD_RE.findall(label)
        if len(words) > 2 or len(label) > 22:
            line = line_number(newline_offsets, match.start())
            findings.append(
                Finding(
                    "verbose-button-copy",
                    rel,
                    line,
                    label[:180],
                    "Keep button labels to one or two direct words when possible.",
                )
            )

    for match in HEADING_RE.finditer(text):
        label = clean_text(match.group(2))
        words = WORD_RE.findall(label)
        if len(words) > 9 or len(label) > 72:
            line = line_number(newline_offsets, match.start())
            findings.append(
                Finding(
                    "verbose-heading-copy",
                    rel,
                    line,
                    label[:180],
                    "Shorten headings to improve hierarchy and scanability.",
                )
            )

    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description="Run an advisory static audit for web UI polish.")
    parser.add_argument("paths", nargs="*", default=["."], help="Files or directories to scan")
    parser.add_argument("--root", default=".", help="Repository root for relative paths")
    parser.add_argument("--json", action="store_true", help="Print JSON instead of text")
    parser.add_argument("--fail-on-findings", action="store_true", help="Exit non-zero when findings are present")
    parser.add_argument(
        "--design-guidance",
        action="append",
        default=[],
        metavar="PATH",
        help="Equivalent human-readable design source relative to --root (repeatable)",
    )
    parser.add_argument(
        "--design-tokens",
        action="append",
        default=[],
        metavar="PATH",
        help="Equivalent token/theme source relative to --root (repeatable)",
    )
    parser.add_argument(
        "--skip-artifact-checks",
        action="store_true",
        help="Suppress DESIGN/token source findings after explicit project-level review",
    )
    args = parser.parse_args()

    root = Path(args.root).resolve()
    if not root.is_dir():
        parser.error(f"--root must be an existing directory: {root}")

    def resolve_input(raw_path: str, kind: str) -> Path:
        candidate = Path(raw_path)
        resolved = candidate.resolve() if candidate.is_absolute() else (root / candidate).resolve()
        if not resolved.is_relative_to(root):
            parser.error(f"{kind} escapes --root: {raw_path}")
        if not resolved.exists():
            parser.error(f"{kind} does not exist: {raw_path} (resolved to {resolved})")
        return resolved

    paths = [resolve_input(raw_path, "scan path") for raw_path in args.paths]

    findings: list[Finding] = []
    try:
        for file_path in iter_files(paths, root):
            findings.extend(audit_file(file_path, root))
    except (OSError, ValueError) as exc:
        parser.error(str(exc))

    def has_contained_artifact(candidates: Iterable[Path]) -> bool:
        for candidate in candidates:
            if not candidate.is_file():
                continue
            resolved = candidate.resolve()
            if resolved.is_relative_to(root) and resolved.is_file():
                return True
        return False

    if not args.skip_artifact_checks:
        guidance_paths = (
            [resolve_input(path, "design guidance path") for path in args.design_guidance]
            if args.design_guidance
            else [root / path for path in DESIGN_GUIDANCE_CANDIDATES]
        )
        token_paths = (
            [resolve_input(path, "design token path") for path in args.design_tokens]
            if args.design_tokens
            else [root / path for path in DESIGN_TOKEN_CANDIDATES]
        )

        if not has_contained_artifact(guidance_paths):
            findings.append(
                Finding(
                    "missing-design-guidance",
                    str(root),
                    1,
                    "No recognized human-readable design source found",
                    "Create DESIGN.md, pass --design-guidance PATH, or explicitly use --skip-artifact-checks.",
                )
            )
        if not has_contained_artifact(token_paths):
            findings.append(
                Finding(
                    "missing-design-tokens",
                    str(root),
                    1,
                    "No recognized token or theme source found",
                    "Create styles.json, pass --design-tokens PATH, or explicitly use --skip-artifact-checks.",
                )
            )

    findings.sort(key=lambda finding: (finding.path, finding.line, finding.check, finding.excerpt))

    if args.json:
        print(json.dumps([asdict(finding) for finding in findings], indent=2))
    elif findings:
        print(f"UI static audit: {len(findings)} finding(s)\n")
        for finding in findings:
            location = f"{finding.path}:{finding.line}"
            print(f"- [{finding.check}] {location}")
            print(f"  {finding.excerpt}")
            print(f"  {finding.guidance}")
    else:
        print("UI static audit: no findings")

    return 1 if findings and args.fail_on_findings else 0


if __name__ == "__main__":
    sys.exit(main())
