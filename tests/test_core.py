"""Tests for the core logic — no disk, no CLI."""

from tasktrack import core


def test_add_assigns_incrementing_ids():
    tasks = []
    core.add(tasks, "first")
    core.add(tasks, "second")
    assert [t["id"] for t in tasks] == [1, 2]


def test_complete_marks_done():
    tasks = []
    core.add(tasks, "thing")
    core.complete(tasks, 1)
    assert tasks[0]["done"] is True


def test_complete_unknown_id_returns_none():
    assert core.complete([], 99) is None


def test_remove_deletes_task():
    tasks = []
    core.add(tasks, "thing")
    assert core.remove(tasks, 1) is True
    assert tasks == []


def test_remove_unknown_id_returns_false():
    assert core.remove([], 99) is False
