#!/usr/bin/env python3
"""Focus Forge: a tiny CLI for planning and completing tasks."""

from __future__ import annotations

import argparse
import json
import os
import sys
from dataclasses import dataclass
from datetime import datetime
from typing import List

DEFAULT_STORE = ".focus_forge.json"


@dataclass
class Task:
    title: str
    created_at: str
    completed_at: str | None = None

    @property
    def is_done(self) -> bool:
        return self.completed_at is not None

    def to_dict(self) -> dict:
        return {
            "title": self.title,
            "created_at": self.created_at,
            "completed_at": self.completed_at,
        }

    @classmethod
    def from_dict(cls, payload: dict) -> "Task":
        return cls(
            title=payload["title"],
            created_at=payload["created_at"],
            completed_at=payload.get("completed_at"),
        )


def now_iso() -> str:
    return datetime.utcnow().replace(microsecond=0).isoformat() + "Z"


def load_tasks(path: str) -> List[Task]:
    if not os.path.exists(path):
        return []
    with open(path, "r", encoding="utf-8") as handle:
        payload = json.load(handle)
    return [Task.from_dict(item) for item in payload.get("tasks", [])]


def save_tasks(path: str, tasks: List[Task]) -> None:
    payload = {"tasks": [task.to_dict() for task in tasks]}
    with open(path, "w", encoding="utf-8") as handle:
        json.dump(payload, handle, indent=2)


def format_task(task: Task, index: int) -> str:
    status = "✓" if task.is_done else "•"
    completed = f" (done {task.completed_at})" if task.is_done else ""
    return f"{index}. [{status}] {task.title} (created {task.created_at}){completed}"


def cmd_add(args: argparse.Namespace) -> int:
    tasks = load_tasks(args.store)
    tasks.append(Task(title=args.title, created_at=now_iso()))
    save_tasks(args.store, tasks)
    print(f"Added task #{len(tasks)}: {args.title}")
    return 0


def cmd_list(args: argparse.Namespace) -> int:
    tasks = load_tasks(args.store)
    if not tasks:
        print("No tasks yet. Add one with 'add'.")
        return 0
    for index, task in enumerate(tasks, start=1):
        if args.all or not task.is_done:
            print(format_task(task, index))
    return 0


def cmd_done(args: argparse.Namespace) -> int:
    tasks = load_tasks(args.store)
    if args.index < 1 or args.index > len(tasks):
        print("Task index out of range.", file=sys.stderr)
        return 1
    task = tasks[args.index - 1]
    if task.is_done:
        print("Task already completed.")
        return 0
    task.completed_at = now_iso()
    save_tasks(args.store, tasks)
    print(f"Completed task #{args.index}: {task.title}")
    return 0


def cmd_next(args: argparse.Namespace) -> int:
    tasks = load_tasks(args.store)
    for task in tasks:
        if not task.is_done:
            print(task.title)
            return 0
    print("No pending tasks.")
    return 0


def cmd_reset(args: argparse.Namespace) -> int:
    save_tasks(args.store, [])
    print("All tasks cleared.")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Focus Forge: a tiny CLI for planning and completing tasks."
    )
    parser.add_argument(
        "--store",
        default=DEFAULT_STORE,
        help="Path to the JSON store (default: .focus_forge.json)",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("title", help="Task description")
    add_parser.set_defaults(func=cmd_add)

    list_parser = subparsers.add_parser("list", help="List tasks")
    list_parser.add_argument(
        "--all", action="store_true", help="Include completed tasks"
    )
    list_parser.set_defaults(func=cmd_list)

    done_parser = subparsers.add_parser("done", help="Mark a task as done")
    done_parser.add_argument("index", type=int, help="Task number to complete")
    done_parser.set_defaults(func=cmd_done)

    next_parser = subparsers.add_parser("next", help="Show the next pending task")
    next_parser.set_defaults(func=cmd_next)

    reset_parser = subparsers.add_parser("reset", help="Clear all tasks")
    reset_parser.set_defaults(func=cmd_reset)

    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
