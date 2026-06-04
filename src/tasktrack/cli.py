"""Command-line interface. Parses args, calls core, prints results."""

import argparse

from . import core, storage


def main(argv=None):
    parser = argparse.ArgumentParser(prog="tasktrack", description="A simple task tracker.")
    sub = parser.add_subparsers(dest="command", required=True)

    add_p = sub.add_parser("add", help="add a new task")
    add_p.add_argument("title", help="what the task is")

    list_p = sub.add_parser("list", help="list tasks")
    list_p.add_argument("--all", action="store_true", help="include completed tasks")

    done_p = sub.add_parser("done", help="mark a task complete")
    done_p.add_argument("id", type=int)

    rm_p = sub.add_parser("rm", help="delete a task")
    rm_p.add_argument("id", type=int)

    args = parser.parse_args(argv)
    tasks = storage.load()

    if args.command == "add":
        task = core.add(tasks, args.title)
        storage.save(tasks)
        print(f"Added #{task['id']}: {task['title']}")

    elif args.command == "list":
        shown = [t for t in tasks if args.all or not t["done"]]
        if not shown:
            print("No tasks.")
        for t in shown:
            mark = "x" if t["done"] else " "
            print(f"[{mark}] {t['id']}. {t['title']}")

    elif args.command == "done":
        task = core.complete(tasks, args.id)
        if task is None:
            print(f"No task with id {args.id}.")
        else:
            storage.save(tasks)
            print(f"Completed #{task['id']}: {task['title']}")

    elif args.command == "rm":
        if core.remove(tasks, args.id):
            storage.save(tasks)
            print(f"Removed #{args.id}")
        else:
            print(f"No task with id {args.id}.")


if __name__ == "__main__":
    main()
