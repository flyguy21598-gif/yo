import json
import os
import tempfile
import unittest

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

    def test_output_file_write(self):
        blueprint = yo.build_blueprint("focus", seed="alpha")
        output = yo.render_markdown(blueprint)
        with tempfile.TemporaryDirectory() as tmpdir:
            path = os.path.join(tmpdir, "out.md")
            with open(path, "w", encoding="utf-8") as handle:
                handle.write(output)
            with open(path, "r", encoding="utf-8") as handle:
                self.assertEqual(handle.read(), output)


if __name__ == "__main__":
    unittest.main()
