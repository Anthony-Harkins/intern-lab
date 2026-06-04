"""Load and save tasks to a JSON file. The only layer that touches disk."""

import json
from pathlib import Path

DATA_FILE = Path.home() / ".tasktrack" / "tasks.json"


def load():
    """Return the list of tasks (empty list if no file yet)."""
    if not DATA_FILE.exists():
        return []
    return json.loads(DATA_FILE.read_text(encoding="utf-8"))


def save(tasks):
    """Write the list of tasks back to disk."""
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    DATA_FILE.write_text(json.dumps(tasks, indent=2), encoding="utf-8")
