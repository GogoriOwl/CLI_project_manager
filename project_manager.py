

def main():
    tasks = {}

    while True:

        user_command = input("Enter command ")

        if user_command == "add task":
            task_id = len(tasks)
            print(task_id)

            task_title = input("Enter title ")
            task_description = input("enter description ")
            task_priority = input("Enter task priority ")
            task_tags = input("Enter task tags ")

            task = add_task(task_id, task_title, task_description, task_priority, task_tags)
            tasks.update(task)
            print(tasks)





def add_task(id, title, description, priority, tags):
    task = {
        f"task-{id}": {
            "titdle": title,
            "description": description,
            "priority": priority,
            "tags": tags,
        }
    }

    return task


main()