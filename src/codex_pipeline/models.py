from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List


@dataclass(frozen=True)
class Task:
    id: str
    title: str
    owner: str
    deliverables: List[str]
    acceptance_criteria: List[str]
    depends_on: List[str] = field(default_factory=list)


@dataclass(frozen=True)
class Phase:
    id: str
    name: str
    goal: str
    gate: str
    tasks: List[Task]


@dataclass(frozen=True)
class Pipeline:
    name: str
    version: str
    objective: str
    default_mode: str
    global_rules: Dict[str, object]
    agents: List[Dict[str, object]]
    phases: List[Phase]
    execution_order: List[str]
    release_tracks: Dict[str, List[str]]
    automation: Dict[str, object]

    @property
    def tasks_by_id(self) -> Dict[str, Task]:
        return {
            task.id: task
            for phase in self.phases
            for task in phase.tasks
        }


@dataclass
class PipelineState:
    completed_tasks: List[str] = field(default_factory=list)

    def is_complete(self, task_id: str) -> bool:
        return task_id in self.completed_tasks

    def mark_complete(self, task_id: str) -> None:
        if task_id not in self.completed_tasks:
            self.completed_tasks.append(task_id)
            self.completed_tasks.sort()
