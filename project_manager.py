

def main():
    tasks = {}

    while True:

        user_command = input("Enter command ")

        if user_command == "add task":
            task_id = len(tasks)
            get_info(tasks)
      

            task = add_task(task_id, task_title, task_description, task_priority, task_tags)
            tasks.update(task)
            print(tasks)



def get_info():
        task_title = input("Enter title ")
        task_description = input("enter description ")
        task_priority = input("Enter task priority ")
        task_tags = input("Enter task tags ")


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



# Create a small reusable function that would loop through a category that I'd need
# Next complete the function get_info() that would validate and store the values 


main()