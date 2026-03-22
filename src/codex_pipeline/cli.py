from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Iterable

from .loader import load_pipeline, load_state, save_state
from .planner import PipelinePlanner, PipelineValidationError


DEFAULT_PIPELINE_PATH = Path("pipeline/codex-task-pipeline.json")
DEFAULT_STATE_PATH = Path("pipeline/pipeline-state.json")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Codex task pipeline utility")
    parser.add_argument("command", choices=["validate", "summary", "next", "complete", "track"])
    parser.add_argument("value", nargs="?", help="Task ID for complete, track name for track")
    parser.add_argument("--pipeline", default=str(DEFAULT_PIPELINE_PATH))
    parser.add_argument("--state", default=str(DEFAULT_STATE_PATH))
    return parser


def _format_ready_tasks(tasks: Iterable[object]) -> str:
    lines = []
    for task in tasks:
        lines.append(f"- {task.id}: {task.title} ({task.owner})")
    return "\n".join(lines) if lines else "- no unblocked tasks"


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    pipeline = load_pipeline(args.pipeline)
    state = load_state(args.state)
    planner = PipelinePlanner(pipeline, state)

    try:
        planner.validate()
        if args.command == "validate":
            print(f"valid pipeline: {pipeline.name}@{pipeline.version}")
            return 0

        if args.command == "summary":
            print(f"Pipeline: {pipeline.name} ({pipeline.version})")
            print(f"Objective: {pipeline.objective}")
            for progress in planner.phase_progress():
                print(
                    f"- {progress.phase_id}: {progress.phase_name} "
                    f"[{progress.completed}/{progress.total} complete, {progress.percent}%]"
                )
            return 0

        if args.command == "next":
            print(_format_ready_tasks(planner.ready_tasks()))
            return 0

        if args.command == "complete":
            if not args.value:
                parser.error("complete requires a task ID")
            task = planner.complete_task(args.value)
            save_state(args.state, state)
            print(f"completed {task.id}: {task.title}")
            return 0

        if args.command == "track":
            if not args.value:
                parser.error("track requires a release track name")
            print(json.dumps(planner.release_track_status(args.value), indent=2))
            return 0
    except PipelineValidationError as exc:
        print(f"error: {exc}")
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
