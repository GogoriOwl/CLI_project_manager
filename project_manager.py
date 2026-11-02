import json


def main():
    tasks = {}

    try:
        with open("prject_task.json", mode="r") as file:
            tasks = json.load(file)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        pass

    while True:
        user_command = input("Enter command ").strip().lower()

        if user_command == "add task":
            task_id = get_next_task_id(tasks)

            task_title, task_description, task_priority, task_tags, status = get_info(tasks)

            task = add_task(
                task_id,
                task_title,
                task_description,
                task_priority,
                task_tags,
                status,
            )

            tasks.update(task)
            save_tasks(tasks)

        elif user_command == "show tasks":
            if len(tasks) == 0:
                print("No tasks found")
            else:
                show_tasks(tasks)

        elif user_command == "view task":
            search_id = input("Enter task id ").strip()
            view_task(tasks, search_id)

        elif user_command == "change task":
            if len(tasks) == 0:
                print("Add tasks first")
                continue

            task_id = input("Enter task id ").strip()

            if find_task(tasks, task_id) is None:
                continue

            while True:
                section = input(
                    "Enter section to change "
                    "(title/description/priority/tags/status): "
                ).strip().lower()

                if section not in [
                    "title",
                    "description",
                    "priority",
                    "tags",
                    "status",
                ]:
                    print("Invalid section")
                    continue

                break

            if section == "priority":
                allowed_priorities = ["low", "medium", "high"]

                while True:
                    to_change = input("Enter new priority: ").strip().lower()

                    if to_change not in allowed_priorities:
                        print("Choose between low, medium, high")
                        continue

                    break

            elif section == "status":
                allowed_statuses = ["todo", "in progress", "done"]

                while True:
                    to_change = input("Enter new status: ").strip().lower()

                    if to_change not in allowed_statuses:
                        print("Choose between todo, in progress, done")
                        continue

                    break

            elif section == "tags":
                to_change = get_tags()

            else:
                while True:
                    to_change = input("Enter new text: ").strip()

                    if len(to_change) < 1:
                        print("Cannot be empty")
                        continue

                    break

            edit_task(tasks, task_id, section, to_change)
            save_tasks(tasks)

        elif user_command == "delete task":
            if len(tasks) == 0:
                print("Add tasks first")
                continue

            task_id = input("Enter task id ").strip()

            delete_task = find_task(tasks, task_id)

            if delete_task is not None:
                tasks.pop(delete_task)
                save_tasks(tasks)

        elif user_command == "mark done":
            task_id = input("Enter the task id ").strip()

            complete_task = find_task(tasks, task_id)

            if complete_task is not None:
                tasks[complete_task]["status"] = "done"
                save_tasks(tasks)

        elif user_command == "search":
            search_for = input("Search: ").strip()

            result = find_corespondance(tasks, search_for)

            if result:
                show_tasks(result)
            else:
                print("Tasks not found")

        elif user_command == "filter":
            filter_by = input("Filter by: ").strip().lower()

            result = tasks_filter(tasks, filter_by)

            if result:
                show_tasks(result)
            else:
                print("Tasks not found")

        elif user_command == "exit":
            break

        else:
            print("Invalid command")


def save_tasks(tasks):
    with open("prject_task.json", mode="w") as file:
        json.dump(tasks, file, indent=4)


def get_next_task_id(tasks):
    if not tasks:
        return 0

    highest_id = max(
        int(task_id.split("-")[1])
        for task_id in tasks
    )

    return highest_id + 1


def get_info(tasks):
    allowed_priorities = ["low", "medium", "high"]
    allowed_statuses = ["todo", "in progress", "done"]

    while True:
        task_title = input("Enter title ").strip()

        if len(task_title) < 1:
            continue

        if valid_task_input(tasks, "title", task_title):
            break

        print("Task with this title already exists")

    while True:
        task_description = input("Enter description ").strip()

        if len(task_description) < 1:
            continue

        break

    while True:
        task_priority = input("Enter task priority ").lower().strip()

        if task_priority not in allowed_priorities:
            print("Invalid priority, choose between: low, medium, high")
            continue

        break

    task_tags = get_tags()

    while True:
        task_status = input("Enter status ").lower().strip()

        if task_status not in allowed_statuses:
            print("Invalid status, choose between: todo, in progress, done")
            continue

        break

    return (
        task_title,
        task_description,
        task_priority,
        task_tags,
        task_status,
    )


def get_tags():
    tags = []

    print("Enter tags one by one. Type 'done' when finished.")

    while True:
        tag = input("Tag: ").strip().lower()

        if tag == "done":
            break

        if len(tag) < 1:
            continue

        if tag in tags:
            print("Tag already added")
            continue

        tags.append(tag)

    return tags


def add_task(id, title, description, priority, tags, status):
    task = {
        f"task-{id}": {
            "title": title,
            "description": description,
            "priority": priority,
            "tags": tags,
            "status": status,
        }
    }

    return task


def valid_task_input(tasks, key, user_input):
    for task in tasks.values():
        if task[key].lower() == user_input.lower():
            return False

    return True


def show_tasks(tasks):
    print(
        *(f"""
    id: {task_id}
    title: {task["title"]}
    description: {task["description"]}
    priority: {task["priority"]}
    tags: {task["tags"]}
    status: {task["status"]}
        """
            for task_id, task in tasks.items()),
        sep="\n",
    )


def view_task(tasks, search_id):
    task_id = f"task-{search_id}"

    if task_id not in tasks:
        print("No task found")
        return None

    task = tasks[task_id]

    print(
        f"""
    title: {task["title"]}
    description: {task["description"]}
    priority: {task["priority"]}
    tags: {task["tags"]}
    status: {task["status"]}
    """
    )

    return task


def edit_task(tasks, task_id, section, to_change):
    task_key = f"task-{task_id}"

    if task_key not in tasks:
        return None

    tasks[task_key][section] = to_change
    return tasks[task_key]


def find_task(tasks, id):
    task_id = f"task-{id}"

    if task_id in tasks:
        return task_id

    print("Task not found")
    return None


def find_corespondance(tasks, search_str):
    result = {}

    search_str = search_str.lower()

    for task_id, task in tasks.items():
        if (
            search_str in task["description"].lower()
            or search_str in task["title"].lower()
            or any(search_str in tag.lower() for tag in task["tags"])
        ):
            result[task_id] = task

    return result


def tasks_filter(tasks, requirement):
    result = {}

    requirement = requirement.lower()

    for task_id, task in tasks.items():
        if (
            task["status"].lower() == requirement
            or task["priority"].lower() == requirement
        ):
            result[task_id] = task

    return result


if __name__ == "__main__":
    main()