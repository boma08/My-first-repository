import tasks as t

tasks = t.load_todo_list()

while True:
    print("\nTo-Do List functions")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Delete a task")
    print("4. Exit")

    choice = input("\nEnter an option from the above selection: ")

    if choice == "1":
        t.add_task(tasks)
    elif choice == "2":
        t.view_tasks(tasks)
    elif choice == "3":
        t.delete_task(tasks)
    elif choice == "4":
        t.save_task(tasks)
        print("Good bye!")
        break
    else:
        print("Invalid input, please enter a valid option.")