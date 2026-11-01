import json

def main():
    tasks = {}

    try:
        with open("prject_task.json", mode="r") as file:
            tasks = json.load(file)
    except FileNotFoundError, json.decoder.JSONDecodeError:
        pass

    while True:
        user_command = input("Enter command ")

        if user_command == "add task":
            task_id = len(tasks)
            task_title, task_description, task_priority, task_tags, status = get_info(tasks)

            task = add_task(task_id, task_title, task_description, task_priority, task_tags, status)
            tasks.update(task)

            with open("prject_task.json", mode="w") as file:
                json.dump(tasks, file)


        elif user_command == "show tasks":
            if len(tasks) == 0:
                print("no tasks found")
            else: show_tasks(tasks)

        elif user_command == "view task":
            search_id = input("Enter task id ")
            view_task(tasks, search_id)

        elif user_command == "change task":
            while True:
                if len(tasks) == 0:
                        print("add tasks first")
                        break
                
                id = input("Enter task id ")
                
                if find_task(tasks, id) == None:
                         break
                else:
                    section = input("Enter sections to change ")
                    to_change = input("Enter text")
                        
                    edit_task(tasks, id, section, to_change)
                    break


        elif user_command == "delete task":
            while True:
                if len(tasks) == 0:
                    print("add tasks first")
                    break
                else:
                    id = input("Enter task id ")
                    delete_task = find_task(tasks, id)
                    if delete_task == None:
                        break
                    else:
                        tasks.pop(delete_task)
                        break

        elif user_command == "mark done":
            id = input("Enter the task id ")
            complete_task = find_task(tasks, id)
            if complete_task:
                tasks[complete_task]["status"] = "done"

        elif user_command == "search":
            search_for = input("Search: ")
            result = find_corespondance(tasks, search_for)

            for task_id, str in result.items():
                print(f'{task_id}: {str}', sep="\n")

        elif user_command == "filter":
            filter_by = input("filter by: ")
            result = tasks_filter(tasks, filter_by)

            if result:
                show_tasks(result)
            else: print("tasks not found")
                       










def get_info(tasks):
        allowed_priorities = ["low", "medium", "high"]
        allowed_statuses = ["todo", "in progress", "done"]

        while True:
            task_title = input("Enter title ").strip()
            if len(task_title) < 1:
                continue
            if valid_task_input(tasks, "title", task_title) == True:
                break
   

        while True:
            task_description = input("enter description ").strip()
            if len(task_description) < 1:
                continue
            if valid_task_input(tasks, "description", task_description) == True:
                break


        while True:
            task_priority = input("Enter task priority ").lower().strip()
            if len(task_priority) < 1:
                 continue

            elif task_priority not in allowed_priorities:
                print("Invalid priority, choose between: low, medium, high")
                continue
            else: break

        while True:
            task_tags = input("Enter task tags ")
            if len(task_tags) > 1:
                break

        while True:
            task_status = input("Enter status ")
            if task_status not in allowed_statuses:
                print("Invalid status, choose between: todo, in progress, done")
                continue
            else: break
            

        return task_title, task_description, task_priority, task_tags, task_status


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
          if task[key] == user_input:
               return False
          
     return True


def show_tasks(tasks):

    print(*(f'''
    id: {task_id}
    title: {task["title"]}
    description: {task["description"]}
    priority: {task["priority"]}
    tags: {task["tags"]}
    status: {task["status"]}

    ''' for task_id, task in tasks.items()), sep="\n\n")

def view_task(tasks, search_id):
    for task_id, task in tasks.items():
        if task_id == f"task-{search_id}":
            print(f'''
            title: {task["title"]}
            description: {task["description"]}
            priority: {task["priority"]}
            tags: {task["tags"]}
            ''')
        else:
            print("No tasks found")


def edit_task(tasks, task_id, section, to_change):

    for id, task in tasks.items():
        if id == f"task-{task_id}":
            task[section] = to_change
            print(task)


def find_task(tasks, id):

        for task_id, task in tasks.items():
            if task_id == f"task-{id}":
                return task_id

            else: 
                print("Task not found")
            

def find_corespondance(tasks, search_str):
    result = {}

    for task_id, task in tasks.items():
        if search_str.lower() in task["description"].lower() or search_str in task["title"].lower() or search_str in task["tags"].lower():
            result.update({task_id: task["description"]})


    return result

def tasks_filter(tasks, requirement):
    result = {}

    for task_id, task in tasks.items():
        if task['status'] == requirement or task['priority'] == requirement:
            result.update({task_id: task})

    return result




# next gonna make persistance + start making pytest


main()