

def main():
    tasks = {}

    while True:
        user_command = input("Enter command ")

        if user_command == "add task":
            task_id = len(tasks)
            task_title, task_description, task_priority, task_tags, status = get_info(tasks)

            task = add_task(task_id, task_title, task_description, task_priority, task_tags, status)
            tasks.update(task)
            print(tasks)

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
                for task_id, task in tasks.items():
                    if task_id == f"task-{id}":
                         section = input("Enter sections to change ")
                         to_change = input("Enter text")
                        
                         edit_task(tasks, id, section, to_change)
                         break

                    else: 
                        print("no tasks found")
                        break

        elif user_command == "delete task":
            while True:
                if len(tasks) == 0:
                    print("add tasks first")
                    break
                else:
                    id = input("Enter task id ")
                    delete_task = find_task(tasks, id)
                    tasks.pop(delete_task)
                    break

                       


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
            
            elif valid_task_input(tasks, "priority", task_priority) == True:
                break

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

# rewrite all the functions that require looking for the task with find_task()
#  make mark complete
# start making search for words in tasks


main()