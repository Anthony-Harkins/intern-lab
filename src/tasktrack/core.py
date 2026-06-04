"""Task logic — pure functions, no I/O. Easy to test in isolation."""


def add(tasks, title):
    """Append a new task and return it. IDs are 1-based and incrementing."""
    next_id = max((t["id"] for t in tasks), default=0) + 1
    task = {"id": next_id, "title": title, "done": False}
    tasks.append(task)
    return task


def complete(tasks, task_id):
    """Mark a task done. Returns the task, or None if the id is unknown."""
    for task in tasks:
        if task["id"] == task_id:
            task["done"] = True
            return task
    return None


def remove(tasks, task_id):
    """Delete a task. Returns True if something was removed."""
    before = len(tasks)
    tasks[:] = [t for t in tasks if t["id"] != task_id]
    return len(tasks) != before
