import json
import tempfile
import unittest
from pathlib import Path

from codex_pipeline.loader import load_pipeline, load_state, save_state
from codex_pipeline.models import PipelineState
from codex_pipeline.planner import PipelinePlanner, PipelineValidationError


PIPELINE_PATH = Path("pipeline/codex-task-pipeline.json")


class PipelinePlannerTests(unittest.TestCase):
    def setUp(self) -> None:
        self.pipeline = load_pipeline(PIPELINE_PATH)
        self.state = PipelineState()
        self.planner = PipelinePlanner(self.pipeline, self.state)

    def test_pipeline_validates(self) -> None:
        self.planner.validate()

    def test_ready_tasks_starts_with_first_core_task(self) -> None:
        ready = [task.id for task in self.planner.ready_tasks()]
        self.assertEqual(["P1-T1"], ready)

    def test_dependency_rules_block_premature_completion(self) -> None:
        with self.assertRaises(PipelineValidationError):
            self.planner.complete_task("P1-T3")

    def test_completion_unlocks_next_task(self) -> None:
        self.planner.complete_task("P1-T1")
        ready = [task.id for task in self.planner.ready_tasks()]
        self.assertIn("P1-T2", ready)
        self.assertNotIn("P1-T3", ready)

    def test_state_round_trip(self) -> None:
        self.state.mark_complete("P1-T1")
        with tempfile.TemporaryDirectory() as tmpdir:
            state_path = Path(tmpdir) / "state.json"
            save_state(state_path, self.state)
            reloaded = load_state(state_path)
        self.assertEqual(["P1-T1"], reloaded.completed_tasks)

    def test_release_track_status(self) -> None:
        status = self.planner.release_track_status("paper_trading")
        self.assertFalse(status["is_complete"])
        self.assertEqual(3, len(status["phases"]))


class PipelineShapeTests(unittest.TestCase):
    def test_pipeline_contains_five_phases(self) -> None:
        payload = json.loads(PIPELINE_PATH.read_text())["pipeline"]
        self.assertEqual(5, len(payload["phases"]))


if __name__ == "__main__":
    unittest.main()
