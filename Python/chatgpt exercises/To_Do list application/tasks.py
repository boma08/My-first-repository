to_do_list = "TO-DO list.txt"
# load To-Do list if it exists or create it if it does not exit
def load_todo_list():
    try:
        with open(to_do_list, "r") as file:
            tasks = [line.strip() for line in file.readlines()]
            return tasks
    except FileNotFoundError:
        with open(to_do_list, "a") as file:
            tasks = []
            return tasks

# view tasks
def view_tasks(tasks):
    if tasks:
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
    else:
        print("No tasks available to view.")

# save task to file
def save_task(tasks):
    with open(to_do_list, "w") as file:
        for task in tasks:
            file.write(task + "\n")

# add task
def add_task(tasks):
    description = input("Enter a description for the task: ")
    tasks.append(description)
    save_task(tasks)
    print("Task added successfully.")

# delete task
def delete_task(tasks):
    if len(tasks) == 0:
        print("No task available to delete.")
    else:
        view_tasks(tasks)
        try:
            task_index = int(input("Enter the number for the task to delete: ")) - 1
            if task_index >= 0:
                removed_task = tasks.pop(task_index)
                print(f"Task '{removed_task}' has been deleted from the To-Do list.")
            else:
                print("Invalid task number. Please choose a task number from the list: ")
                view_tasks(tasks)

        except ValueError:
            print("Invalid input. Please enter a valid number: ")
            view_tasks(tasks)
        except NameError:
            print("Invalid input. Please enter a valid number: ")
            view_tasks(tasks)
        except IndexError:
            print("Invalid input. Please enter a valid number: ")
            view_tasks(tasks)

    save_task(tasks)



