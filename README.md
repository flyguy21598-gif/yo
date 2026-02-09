# Focus Forge

Focus Forge is a tiny, single-file CLI I always wanted: a calm, no-frills planner that lets me capture tasks fast, focus on the next one, and close the loop when it's done. It stores everything in a local JSON file so it's easy to inspect or back up.

## Why this exists

I wanted a tool that:

- Works offline and doesn't require setup or accounts.
- Keeps data in a human-readable file.
- Makes the next action obvious.

## Usage

Run it from the repo root:

```bash
python3 src/focus_forge.py add "Draft outline for the proposal"
python3 src/focus_forge.py add "Review with team"
python3 src/focus_forge.py list
python3 src/focus_forge.py done 1
python3 src/focus_forge.py next
```

### Commands

- `add <title>`: Add a new task.
- `list [--all]`: Show pending tasks (or all tasks with `--all`).
- `done <index>`: Mark a task as complete.
- `next`: Show the next pending task title.
- `reset`: Clear all tasks.

### Storage

By default, data is stored in `.focus_forge.json` in the working directory. You can override the path:

```bash
python3 src/focus_forge.py --store /path/to/tasks.json list
```

## Next step task (queued)

When you say **continue**, I'll implement:

- `export` command to save tasks to CSV/Markdown for sharing.
