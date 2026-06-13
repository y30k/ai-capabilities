#!/usr/bin/env python3
"""Static UI polish audit for web projects.

Heuristically flags design-system drift and copy bloat. It is advisory by default;
use --fail-on-findings in CI after tuning ignores.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, asdict
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
        re.compile(r"\bstyle\s*=\s*(?:\{\{|\")"),
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
        "Avoid unapproved gradients, glow, noise, blur, and custom shadow effects.",
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


def iter_files(paths: Iterable[Path]) -> Iterable[Path]:
    for path in paths:
        if not path.exists():
            continue
        if path.is_file():
            if path.suffix in EXTENSIONS:
                yield path
            continue
        for child in path.rglob("*"):
            if any(part in SKIP_DIRS for part in child.parts):
                continue
            if child.is_file() and child.suffix in EXTENSIONS:
                yield child


def line_number(text: str, index: int) -> int:
    return text.count("\n", 0, index) + 1


def clean_text(html: str) -> str:
    return " ".join(TAG_RE.sub(" ", html).split())


def excerpt(line: str) -> str:
    stripped = line.strip()
    return stripped[:180] + ("…" if len(stripped) > 180 else "")


def audit_file(path: Path, root: Path) -> list[Finding]:
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return []

    findings: list[Finding] = []
    rel = str(path.relative_to(root)) if path.is_relative_to(root) else str(path)
    lines = text.splitlines()

    for check, pattern, guidance in CHECKS:
        for match in pattern.finditer(text):
            line = line_number(text, match.start())
            findings.append(Finding(check, rel, line, excerpt(lines[line - 1] if line - 1 < len(lines) else ""), guidance))

    for match in BUTTON_RE.finditer(text):
        label = clean_text(match.group(1))
        words = WORD_RE.findall(label)
        if len(words) > 2 or len(label) > 22:
            line = line_number(text, match.start())
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
            line = line_number(text, match.start())
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
    args = parser.parse_args()

    root = Path(args.root).resolve()
    paths = [Path(p).resolve() for p in args.paths]
    findings: list[Finding] = []
    for file_path in iter_files(paths):
        findings.extend(audit_file(file_path, root))

    design_files = {"DESIGN.md", "styles.json", "Styles.json"}
    if root.exists() and not any((root / name).exists() for name in design_files):
        findings.insert(
            0,
            Finding(
                "missing-design-artifacts",
                str(root),
                1,
                "DESIGN.md and styles.json not found",
                "Create design artifacts or confirm the project uses an equivalent design-system source.",
            ),
        )

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
