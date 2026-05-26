import json
import subprocess
import tempfile
import unittest
from pathlib import Path

import yo


class TestYoBlueprint(unittest.TestCase):
    def test_deterministic_seed(self):
        first = yo.build_blueprint("focus", seed="alpha")
        second = yo.build_blueprint("focus", seed="alpha")
        self.assertEqual(first, second)

    def test_json_render_includes_keys(self):
        blueprint = yo.build_blueprint("focus", seed="alpha")
        payload = json.loads(yo.render_json(blueprint))
        for key in [
            "title",
            "tagline",
            "power_core",
            "unique_edge",
            "protocol",
            "metrics",
            "leverage",
            "threats",
            "invocation",
        ]:
            self.assertIn(key, payload)

    def test_sanitized_theme(self):
        blueprint = yo.build_blueprint("*** strategic clarity!!!", seed="x")
        self.assertIn("Strategic Clarity", blueprint.title)

    def test_multiple_variations_count(self):
        blueprints = yo.build_blueprints("focus", seed="alpha", count=3)
        self.assertEqual(len(blueprints), 3)
        self.assertEqual(len({bp.title for bp in blueprints}), 3)

    def test_profile_changes_protocol_language(self):
        blueprints = yo.build_blueprints("focus", seed="alpha", count=1, profile="founder")
        protocol = blueprints[0].protocol
        self.assertIn("strategic bet", protocol[0])
        self.assertIn("customer-facing artifact", protocol[3])

    def test_short_invalid_theme_raises(self):
        with self.assertRaises(yo.YoError):
            yo.build_blueprint("!!", seed="alpha")

    def test_cli_output_file_write(self):
        root = Path(__file__).resolve().parents[1]
        with tempfile.TemporaryDirectory() as tmpdir:
            out = Path(tmpdir) / "nested" / "blueprint.md"
            proc = subprocess.run(
                [
                    "python",
                    str(root / "yo.py"),
                    "strategic clarity",
                    "--output",
                    str(out),
                ],
                capture_output=True,
                text=True,
                check=False,
            )
            self.assertEqual(proc.returncode, 0)
            self.assertTrue(out.exists())
            self.assertIn("Engine", out.read_text(encoding="utf-8"))

    def test_cli_json_count(self):
        root = Path(__file__).resolve().parents[1]
        proc = subprocess.run(
            [
                "python",
                str(root / "yo.py"),
                "focus",
                "--count",
                "2",
                "--json",
                "--seed",
                "alpha",
            ],
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(proc.returncode, 0)
        payload = json.loads(proc.stdout)
        self.assertEqual(len(payload), 2)

    def test_invalid_count_fails(self):
        root = Path(__file__).resolve().parents[1]
        proc = subprocess.run(
            ["python", str(root / "yo.py"), "focus", "--count", "0"],
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertNotEqual(proc.returncode, 0)
        self.assertIn("count must be between 1 and 20", proc.stderr)

    def test_cli_profile_flag(self):
        root = Path(__file__).resolve().parents[1]
        proc = subprocess.run(
            [
                "python",
                str(root / "yo.py"),
                "focus",
                "--profile",
                "creator",
                "--seed",
                "alpha",
            ],
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(proc.returncode, 0)
        self.assertIn("audience outcome", proc.stdout)
        self.assertIn("publishable artifact", proc.stdout)


if __name__ == "__main__":
    unittest.main()
