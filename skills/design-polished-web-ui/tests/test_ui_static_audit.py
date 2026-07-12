#!/usr/bin/env python3
"""Regression tests for the bundled UI static audit CLI."""

from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "ui_static_audit.py"


class UiStaticAuditCliTest(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.root = Path(self.temp_dir.name)
        (self.root / "DESIGN.md").write_text("# Design\n", encoding="utf-8")
        (self.root / "styles.json").write_text("{}\n", encoding="utf-8")

    def tearDown(self) -> None:
        self.temp_dir.cleanup()

    def run_audit(
        self,
        *paths: str,
        root: Path | None = None,
        json_output: bool = True,
        fail_on_findings: bool = False,
        extra_args: tuple[str, ...] = (),
        timeout: float = 10.0,
    ) -> subprocess.CompletedProcess[str]:
        command = [
            sys.executable,
            str(SCRIPT),
            "--root",
            str(root or self.root),
            *extra_args,
            *(paths or (".",)),
        ]
        if json_output:
            command.append("--json")
        if fail_on_findings:
            command.append("--fail-on-findings")
        return subprocess.run(command, capture_output=True, text=True, check=False, timeout=timeout)

    def findings(self, result: subprocess.CompletedProcess[str]) -> list[dict[str, object]]:
        self.assertEqual(result.returncode, 0, result.stderr)
        parsed = json.loads(result.stdout)
        self.assertIsInstance(parsed, list)
        for finding in parsed:
            self.assertEqual(
                set(finding),
                {"check", "path", "line", "excerpt", "guidance"},
            )
        return parsed

    def test_root_relative_scan_is_stable_and_matches_single_quoted_style(self) -> None:
        src = self.root / "src"
        src.mkdir()
        (src / "a.tsx").write_text(
            "<button style='color: #fff'>Save changes now</button>\n",
            encoding="utf-8",
        )
        (src / "b.tsx").write_text(
            '<div className="m-[13px]">Coming soon</div>\n',
            encoding="utf-8",
        )
        ignored = src / "node_modules"
        ignored.mkdir()
        (ignored / "ignored.tsx").write_text(
            '<div style={{ color: "#000" }}>Placeholder</div>\n',
            encoding="utf-8",
        )

        first = self.run_audit("src")
        second = self.run_audit("src")
        self.assertEqual(first.stdout, second.stdout)
        findings = self.findings(first)
        checks = {finding["check"] for finding in findings}
        self.assertTrue(
            {
                "hardcoded-color",
                "inline-style",
                "placeholder-copy",
                "tailwind-arbitrary-value",
                "verbose-button-copy",
            }.issubset(checks)
        )
        self.assertFalse(any("node_modules" in str(item["path"]) for item in findings))

    def test_overlapping_inputs_emit_each_finding_once(self) -> None:
        src = self.root / "src"
        src.mkdir()
        target = src / "a.tsx"
        target.write_text("<button>Save changes now</button>\n", encoding="utf-8")

        findings = self.findings(self.run_audit("src", "src/a.tsx", "src"))
        identities = [
            (item["check"], item["path"], item["line"], item["excerpt"])
            for item in findings
        ]
        self.assertEqual(len(identities), len(set(identities)))
        self.assertEqual(
            sum(item["check"] == "verbose-button-copy" for item in findings),
            1,
        )

    def test_missing_root_and_scan_path_fail_closed(self) -> None:
        missing_path = self.run_audit("missing")
        self.assertEqual(missing_path.returncode, 2)
        self.assertIn("scan path does not exist", missing_path.stderr)

        missing_root = self.run_audit(".", root=self.root / "missing-root")
        self.assertEqual(missing_root.returncode, 2)
        self.assertIn("--root must be an existing directory", missing_root.stderr)

    def test_invalid_utf8_and_missing_artifacts_are_reported_separately(self) -> None:
        bare = self.root / "bare"
        bare.mkdir()
        (bare / "bad.html").write_bytes(b"\xff\xfe")

        findings = self.findings(self.run_audit(".", root=bare))
        checks = {finding["check"] for finding in findings}
        self.assertEqual(
            checks,
            {"unreadable-file", "missing-design-guidance", "missing-design-tokens"},
        )

    def test_rejects_out_of_root_paths_and_file_symlinks(self) -> None:
        with tempfile.TemporaryDirectory() as outside_dir:
            outside = Path(outside_dir) / "secret.css"
            outside.write_text(".token { color: #abc123; }\n", encoding="utf-8")

            direct = self.run_audit(str(outside))
            self.assertEqual(direct.returncode, 2)
            self.assertIn("escapes --root", direct.stderr)
            self.assertNotIn("abc123", direct.stdout + direct.stderr)

            src = self.root / "src"
            src.mkdir()
            link = src / "leak.css"
            try:
                link.symlink_to(outside)
            except OSError as exc:
                self.skipTest(f"symlinks unavailable: {exc}")

            linked = self.run_audit("src")
            self.assertEqual(linked.returncode, 2)
            self.assertIn("escapes --root", linked.stderr)
            self.assertNotIn("abc123", linked.stdout + linked.stderr)

    def test_explicit_artifact_overrides_and_suppression(self) -> None:
        project = self.root / "custom-artifacts"
        (project / "docs").mkdir(parents=True)
        (project / "docs" / "ui-guidance.txt").write_text("Design guidance\n", encoding="utf-8")
        (project / "theme.css").write_text(":root { --brand: blue; }\n", encoding="utf-8")
        (project / "app.tsx").write_text("<button>Save</button>\n", encoding="utf-8")

        explicit = self.findings(
            self.run_audit(
                ".",
                root=project,
                extra_args=(
                    "--design-guidance",
                    "docs/ui-guidance.txt",
                    "--design-tokens",
                    "theme.css",
                ),
            )
        )
        explicit_checks = {finding["check"] for finding in explicit}
        self.assertNotIn("missing-design-guidance", explicit_checks)
        self.assertNotIn("missing-design-tokens", explicit_checks)

        suppressed = self.findings(
            self.run_audit(".", root=project, extra_args=("--skip-artifact-checks",))
        )
        suppressed_checks = {finding["check"] for finding in suppressed}
        self.assertNotIn("missing-design-guidance", suppressed_checks)
        self.assertNotIn("missing-design-tokens", suppressed_checks)

    def test_explicit_artifact_overrides_reject_escapes(self) -> None:
        project = self.root / "override-escape"
        project.mkdir()
        outside = self.root / "outside-guidance.md"
        outside.write_text("# External\n", encoding="utf-8")

        direct = self.run_audit(
            ".",
            root=project,
            extra_args=("--design-guidance", str(outside)),
        )
        self.assertEqual(direct.returncode, 2)
        self.assertIn("escapes --root", direct.stderr)

        link = project / "guidance.md"
        try:
            link.symlink_to(outside)
        except OSError as exc:
            self.skipTest(f"symlinks unavailable: {exc}")
        linked = self.run_audit(
            ".",
            root=project,
            extra_args=("--design-guidance", "guidance.md"),
        )
        self.assertEqual(linked.returncode, 2)
        self.assertIn("escapes --root", linked.stderr)

    def test_default_artifact_symlinks_must_stay_inside_root(self) -> None:
        project = self.root / "artifact-project"
        project.mkdir()
        (project / "styles.json").write_text("{}\n", encoding="utf-8")
        (project / "app.tsx").write_text("<button>Save</button>\n", encoding="utf-8")
        outside = self.root / "outside-design.md"
        outside.write_text("# External design\n", encoding="utf-8")
        try:
            (project / "DESIGN.md").symlink_to(outside)
        except OSError as exc:
            self.skipTest(f"symlinks unavailable: {exc}")

        findings = self.findings(self.run_audit(".", root=project))
        checks = {finding["check"] for finding in findings}
        self.assertIn("missing-design-guidance", checks)
        self.assertNotIn("missing-design-tokens", checks)

    def test_tailwind_config_is_an_equivalent_token_source(self) -> None:
        project = self.root / "tailwind-project"
        project.mkdir()
        (project / "DESIGN.md").write_text("# Design\n", encoding="utf-8")
        (project / "tailwind.config.ts").write_text("export default {};\n", encoding="utf-8")
        (project / "app.tsx").write_text("<button>Save</button>\n", encoding="utf-8")

        findings = self.findings(self.run_audit(".", root=project))
        checks = {finding["check"] for finding in findings}
        self.assertNotIn("missing-design-guidance", checks)
        self.assertNotIn("missing-design-tokens", checks)

    def test_skip_names_are_relative_to_scan_root(self) -> None:
        project = self.root / "build" / "project"
        project.mkdir(parents=True)
        (project / "DESIGN.md").write_text("# Design\n", encoding="utf-8")
        (project / "styles.json").write_text("{}\n", encoding="utf-8")
        (project / "app.tsx").write_text('<div style="color: #fff">Text</div>\n', encoding="utf-8")

        findings = self.findings(self.run_audit(".", root=project))
        self.assertTrue(any(item["check"] == "hardcoded-color" for item in findings))

    def test_finding_heavy_file_completes_within_linear_budget(self) -> None:
        src = self.root / "src"
        src.mkdir()
        (src / "many.css").write_text(".x { color: #fff; }\n" * 40_000, encoding="utf-8")

        result = self.run_audit("src", timeout=5.0)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(len(json.loads(result.stdout)), 40_000)

    def test_fail_on_findings_returns_one(self) -> None:
        src = self.root / "src"
        src.mkdir()
        (src / "a.html").write_text('<div style="#fff">Text</div>\n', encoding="utf-8")

        result = self.run_audit("src", fail_on_findings=True)
        self.assertEqual(result.returncode, 1)
        self.assertTrue(json.loads(result.stdout))


if __name__ == "__main__":
    unittest.main()
