

def main():
    tasks = {}

    while True:
        user_command = input("Enter command ")

        if user_command == "add task":
            task_id = len(tasks)
            task_title, task_description, task_priority, task_tags = get_info(tasks)

            task = add_task(task_id, task_title, task_description, task_priority, task_tags)
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

                       


def get_info(tasks):
        allowed_priorities = ["low", "medium", "high"]

        while True:
            task_title = input("Enter title ")
            if len(task_title) < 1:
                continue
            if valid_task_input(tasks, "title", task_title) == True:
                break
   

        while True:
            task_description = input("enter description ")
            if len(task_description) < 1:
                continue
            if valid_task_input(tasks, "description", task_description) == True:
                break


        while True:
            task_priority = input("Enter task priority ")
            if len(task_priority) < 1:
                 continue

            elif task_priority not in allowed_priorities:
                print("Invalid priority, choose between: low, medium, high")
            
            elif valid_task_input(tasks, "priority", task_priority) == True:
                break

            
        task_tags = input("Enter task tags ")

        return task_title, task_description, task_priority, task_tags


def add_task(id, title, description, priority, tags):
    task = {
        f"task-{id}": {
            "title": title,
            "description": description,
            "priority": priority,
            "tags": tags,
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




# Try to use get_into() function in edit_task(), liiks like it's gonna be possible instead of writing additional code
# then gonna do the delete_task with pop() function for dict
#  possibly status validation and mark complete then


main()