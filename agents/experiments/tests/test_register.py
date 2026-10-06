"""Offline checks for registration parity and preserving project files."""

import json
from pathlib import Path
import re
import subprocess
import sys
import tempfile
import tomllib
import unittest

SOURCE = Path(__file__).resolve().parents[1]
SCRIPT = SOURCE / "scripts/register.py"
NAMES = {"experiment-planner", "experiment-runner", "experiment-analyst", "experiment-reporter"}


class RegistrationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.project = Path(self.temp.name) / "project"

    def run_cli(self, *args):
        return subprocess.run(
            [sys.executable, "-B", str(SCRIPT), "--output", str(self.project), *args],
            capture_output=True, text=True, encoding="utf-8",
        )

    def snapshot(self):
        if not self.project.exists():
            return {}
        return {str(p.relative_to(self.project)): p.read_bytes()
                for p in self.project.rglob("*") if p.is_file()}

    def test_both_formats_preserve_full_instructions_and_metadata(self):
        result = self.run_cli()
        self.assertEqual(result.returncode, 0, result.stderr)
        claude = list((self.project / ".claude/agents").glob("*.md"))
        codex = list((self.project / ".codex/agents").glob("*.toml"))
        self.assertEqual({p.stem for p in claude}, NAMES)
        self.assertEqual({p.stem for p in codex}, NAMES)
        common = (SOURCE / "common.md").read_text(encoding="utf-8").strip()
        records = (SOURCE.parents[1] / "skills/setup-experiments/references/records.md").read_text(
            encoding="utf-8"
        ).strip()
        for path in codex:
            config = tomllib.loads(path.read_text(encoding="utf-8"))
            markdown = (self.project / f".claude/agents/{path.stem}.md").read_text(encoding="utf-8")
            _, frontmatter, body = markdown.split("---\n", 2)
            metadata = dict(line.split(": ", 1) for line in frontmatter.strip().splitlines())
            self.assertEqual(json.loads(metadata["name"]), config["name"])
            self.assertEqual(json.loads(metadata["description"]), config["description"])
            self.assertEqual(metadata["model"], "inherit")
            # Configuration only registers roles; it leaves execution permissions and model selection intact.
            self.assertEqual(set(config), {"name", "description", "developer_instructions"})
            role = (SOURCE / f"roles/{path.stem}.md").read_text(encoding="utf-8").strip()
            expected = f"{common}\n\n{records}\n\n{role}\n"
            self.assertEqual(config["developer_instructions"], expected)
            self.assertTrue(body.endswith(expected))
            self.assertIn("実験", expected)

    def test_codex_registration_fragment_resolves_all_role_files(self):
        self.assertEqual(self.run_cli("--agent", "codex").returncode, 0)
        directory = self.project / ".codex"
        fragment = tomllib.loads((directory / "experiment-agents.toml").read_text(encoding="utf-8"))
        self.assertEqual(set(fragment), {"agents"})
        self.assertEqual(set(fragment["agents"]), NAMES)
        for name, declaration in fragment["agents"].items():
            path = directory / declaration["config_file"]
            config = tomllib.loads(path.read_text(encoding="utf-8"))
            self.assertEqual(config["name"], name)
            self.assertEqual(config["description"], declaration["description"])
        self.assertFalse((directory / "config.toml").exists())

    def test_check_is_read_only_even_for_missing_project(self):
        self.assertEqual(self.run_cli("--check").returncode, 1)
        self.assertFalse(self.project.exists())
        self.assertEqual(self.run_cli().returncode, 0)
        before = self.snapshot()
        self.assertEqual(self.run_cli("--check").returncode, 0)
        self.assertEqual(self.snapshot(), before)

    def test_update_refuses_all_writes_before_overwriting_local_changes(self):
        self.assertEqual(self.run_cli().returncode, 0)
        edited = self.project / ".claude/agents/experiment-runner.md"
        edited.write_text("Local instructions\n", encoding="utf-8")
        missing = self.project / ".codex/agents/experiment-reporter.toml"
        missing.unlink()
        before = self.snapshot()
        self.assertEqual(self.run_cli().returncode, 1)
        self.assertEqual(self.snapshot(), before)
        self.assertEqual(self.run_cli("--check").returncode, 1)
        self.assertEqual(self.snapshot(), before)
        sentinel = self.project / ".codex/config.toml"
        sentinel.write_text('model = "project-choice"\n', encoding="utf-8")
        self.assertEqual(self.run_cli("--force").returncode, 0)
        self.assertEqual(sentinel.read_text(encoding="utf-8"), 'model = "project-choice"\n')
        self.assertTrue(missing.exists())
        self.assertNotEqual(edited.read_text(encoding="utf-8"), "Local instructions\n")
        before = self.snapshot()
        self.assertEqual(self.run_cli().returncode, 0)
        self.assertEqual(self.snapshot(), before)

    def test_selecting_one_platform_leaves_other_platform_untouched(self):
        self.assertEqual(self.run_cli("--agent", "codex").returncode, 0)
        self.assertFalse((self.project / ".claude").exists())
        self.assertEqual(self.run_cli("--agent", "codex", "--check").returncode, 0)
        self.assertEqual(self.run_cli("--agent", "claude-code", "--check").returncode, 1)
        before = self.snapshot()
        self.assertEqual(self.run_cli("--agent", "claude-code").returncode, 0)
        for path, content in before.items():
            self.assertEqual((self.project / path).read_bytes(), content)

    def test_plugin_is_self_contained_and_preserves_shared_instructions(self):
        self.assertEqual(self.run_cli("--agent", "claude-plugin").returncode, 0)
        plugin = self.snapshot()
        self.assertEqual(len(plugin), 10)
        self.assertFalse((self.project / ".claude").exists())
        self.assertFalse((self.project / ".codex").exists())
        self.assertFalse((self.project / "docs").exists())
        self.assertEqual({p.stem for p in (self.project / "agents").glob("*.md")}, NAMES)
        standalone = self.run_cli("--agent", "claude-code")
        self.assertEqual(standalone.returncode, 0, standalone.stderr)
        for name in NAMES:
            self.assertEqual(
                (self.project / f"agents/{name}.md").read_bytes(),
                (self.project / f".claude/agents/{name}.md").read_bytes(),
            )
        original = SOURCE.parents[1] / "skills/setup-experiments"
        for relative in ("SKILL.md", "references/records.md"):
            self.assertEqual(
                (self.project / "skills/setup-experiments" / relative).read_text(encoding="utf-8"),
                (original / relative).read_text(encoding="utf-8"),
            )
        for relative in plugin:
            path = self.project / relative
            if path.suffix != ".md":
                continue
            for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", path.read_text(encoding="utf-8")):
                if "://" in target or target.startswith("#"):
                    continue
                resolved = (path.parent / target.split("#")[0]).resolve()
                self.assertTrue(resolved.is_relative_to(self.project.resolve()), target)
                self.assertTrue(resolved.is_file(), target)
        workflow = (self.project / "skills/run-experiments/references/workflow.md").read_text(
            encoding="utf-8"
        )
        for name in NAMES | {"setup-experiments"}:
            self.assertIn(f"`experiments:{name}`", workflow)
            self.assertNotIn(f"`{name}`", workflow)

    def test_plugin_update_preserves_manifest_and_readme(self):
        self.assertEqual(self.run_cli("--agent", "claude-plugin").returncode, 0)
        readme = self.project / "README.md"
        readme.write_text("Maintained separately\n", encoding="utf-8")
        manifest = self.project / ".claude-plugin/plugin.json"
        manifest.parent.mkdir()
        manifest.write_text('{"name": "experiments", "version": "0.2.0"}\n', encoding="utf-8")
        edited = self.project / "skills/setup-experiments/SKILL.md"
        edited.write_text("Local instructions\n", encoding="utf-8")
        missing = self.project / "agents/experiment-reporter.md"
        missing.unlink()
        before = self.snapshot()
        self.assertEqual(self.run_cli("--agent", "claude-plugin", "--check").returncode, 1)
        self.assertEqual(self.snapshot(), before)
        self.assertEqual(self.run_cli("--agent", "claude-plugin").returncode, 1)
        self.assertEqual(self.snapshot(), before)
        self.assertEqual(self.run_cli("--agent", "claude-plugin", "--force").returncode, 0)
        self.assertEqual(readme.read_bytes(), before["README.md"])
        self.assertEqual(manifest.read_bytes(), before[str(Path(".claude-plugin/plugin.json"))])
        self.assertTrue(missing.exists())
        self.assertEqual(self.run_cli("--agent", "claude-plugin", "--check").returncode, 0)

    def test_marketplace_points_to_current_generated_plugin(self):
        root = SOURCE.parents[1]
        marketplace = json.loads((root / ".claude-plugin/marketplace.json").read_text(encoding="utf-8"))
        entry = next(p for p in marketplace["plugins"] if p["name"] == "experiments")
        plugin = (root / entry["source"]).resolve()
        self.assertTrue(plugin.is_relative_to(root.resolve()))
        manifest = json.loads((plugin / ".claude-plugin/plugin.json").read_text(encoding="utf-8"))
        self.assertEqual(manifest["name"], entry["name"])
        self.assertTrue((plugin / "README.md").is_file())
        self.assertEqual(
            (plugin / "LICENSE").read_text(encoding="utf-8"),
            (root / "LICENSE").read_text(encoding="utf-8"),
        )
        result = subprocess.run(
            [sys.executable, "-B", str(SCRIPT), "--agent", "claude-plugin",
             "--output", str(plugin), "--check"],
            capture_output=True, text=True, encoding="utf-8",
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)


if __name__ == "__main__":
    unittest.main()
