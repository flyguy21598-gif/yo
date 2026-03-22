from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Iterable, List, Set

from .models import Phase, Pipeline, PipelineState, Task


@dataclass(frozen=True)
class PhaseProgress:
    phase_id: str
    phase_name: str
    completed: int
    total: int

    @property
    def percent(self) -> int:
        if self.total == 0:
            return 100
        return int((self.completed / self.total) * 100)


class PipelineValidationError(ValueError):
    pass


class PipelinePlanner:
    def __init__(self, pipeline: Pipeline, state: PipelineState | None = None) -> None:
        self.pipeline = pipeline
        self.state = state or PipelineState()

    def validate(self) -> None:
        tasks = self.pipeline.tasks_by_id
        if len(tasks) != sum(len(phase.tasks) for phase in self.pipeline.phases):
            raise PipelineValidationError("duplicate task IDs detected")

        phase_ids = {phase.id for phase in self.pipeline.phases}
        for phase_id in self.pipeline.execution_order:
            if phase_id not in phase_ids:
                raise PipelineValidationError(f"execution order references unknown phase: {phase_id}")

        for track_name, phase_list in self.pipeline.release_tracks.items():
            for phase_id in phase_list:
                if phase_id not in phase_ids:
                    raise PipelineValidationError(
                        f"release track {track_name} references unknown phase: {phase_id}"
                    )

        for task in tasks.values():
            for dependency in task.depends_on:
                if dependency not in tasks:
                    raise PipelineValidationError(
                        f"task {task.id} depends on unknown task {dependency}"
                    )

        self._assert_acyclic(tasks.values())

    def _assert_acyclic(self, tasks: Iterable[Task]) -> None:
        graph: Dict[str, List[str]] = {task.id: list(task.depends_on) for task in tasks}
        visiting: Set[str] = set()
        visited: Set[str] = set()

        def visit(task_id: str) -> None:
            if task_id in visited:
                return
            if task_id in visiting:
                raise PipelineValidationError(f"cycle detected at {task_id}")
            visiting.add(task_id)
            for dependency in graph[task_id]:
                visit(dependency)
            visiting.remove(task_id)
            visited.add(task_id)

        for task_id in graph:
            visit(task_id)

    def ready_tasks(self) -> List[Task]:
        tasks = self.pipeline.tasks_by_id
        ready = []
        for task in tasks.values():
            if self.state.is_complete(task.id):
                continue
            if all(self.state.is_complete(dep) for dep in task.depends_on):
                ready.append(task)
        return sorted(ready, key=lambda task: task.id)

    def phase_progress(self) -> List[PhaseProgress]:
        progress = []
        for phase in self.pipeline.phases:
            completed = sum(1 for task in phase.tasks if self.state.is_complete(task.id))
            progress.append(
                PhaseProgress(
                    phase_id=phase.id,
                    phase_name=phase.name,
                    completed=completed,
                    total=len(phase.tasks),
                )
            )
        return progress

    def complete_task(self, task_id: str) -> Task:
        task = self.pipeline.tasks_by_id.get(task_id)
        if task is None:
            raise PipelineValidationError(f"unknown task: {task_id}")
        missing = [dep for dep in task.depends_on if not self.state.is_complete(dep)]
        if missing:
            raise PipelineValidationError(
                f"task {task_id} cannot be completed before dependencies: {', '.join(missing)}"
            )
        self.state.mark_complete(task_id)
        return task

    def phase_by_id(self, phase_id: str) -> Phase:
        for phase in self.pipeline.phases:
            if phase.id == phase_id:
                return phase
        raise PipelineValidationError(f"unknown phase: {phase_id}")

    def release_track_status(self, track_name: str) -> Dict[str, object]:
        phases = self.pipeline.release_tracks.get(track_name)
        if phases is None:
            raise PipelineValidationError(f"unknown release track: {track_name}")
        entries = []
        all_complete = True
        for phase_id in phases:
            phase = self.phase_by_id(phase_id)
            total = len(phase.tasks)
            completed = sum(1 for task in phase.tasks if self.state.is_complete(task.id))
            is_complete = completed == total
            if not is_complete:
                all_complete = False
            entries.append(
                {
                    "phase_id": phase_id,
                    "phase_name": phase.name,
                    "completed": completed,
                    "total": total,
                    "is_complete": is_complete,
                }
            )
        return {"track": track_name, "is_complete": all_complete, "phases": entries}
