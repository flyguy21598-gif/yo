from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict

from .models import Phase, Pipeline, PipelineState, Task



def _build_task(payload: Dict[str, Any]) -> Task:
    return Task(
        id=payload["id"],
        title=payload["title"],
        owner=payload["owner"],
        deliverables=list(payload.get("deliverables", [])),
        acceptance_criteria=list(payload.get("acceptance_criteria", [])),
        depends_on=list(payload.get("depends_on", [])),
    )


def _build_phase(payload: Dict[str, Any]) -> Phase:
    return Phase(
        id=payload["id"],
        name=payload["name"],
        goal=payload["goal"],
        gate=payload["gate"],
        tasks=[_build_task(task) for task in payload.get("tasks", [])],
    )


def load_pipeline(path: str | Path) -> Pipeline:
    pipeline_path = Path(path)
    data = json.loads(pipeline_path.read_text())
    payload = data["pipeline"]
    return Pipeline(
        name=payload["name"],
        version=payload["version"],
        objective=payload["objective"],
        default_mode=payload["default_mode"],
        global_rules=dict(payload.get("global_rules", {})),
        agents=list(payload.get("agents", [])),
        phases=[_build_phase(phase) for phase in payload.get("phases", [])],
        execution_order=list(payload.get("execution_order", [])),
        release_tracks=dict(payload.get("release_tracks", {})),
        automation=dict(payload.get("automation", {})),
    )


def load_state(path: str | Path) -> PipelineState:
    state_path = Path(path)
    if not state_path.exists():
        return PipelineState()
    data = json.loads(state_path.read_text())
    return PipelineState(completed_tasks=list(data.get("completed_tasks", [])))


def save_state(path: str | Path, state: PipelineState) -> None:
    state_path = Path(path)
    state_path.write_text(
        json.dumps({"completed_tasks": state.completed_tasks}, indent=2) + "\n"
    )
