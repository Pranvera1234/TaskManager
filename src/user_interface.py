# user_interface.py
from business_logic import TaskService


def start_application():
    """ Start the Task Management Application."""
    task_service = TaskService()

    while True:
        print("Task Management Application")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":

            tasks = task_service.get_all_tasks()
            print("Tasks:")
            for task in tasks:
                print(f"- {task}")
        elif choice == "2":
            new_task = input("Enter task description: ")
            task_service.add_task(new_task)
            print("Task added successfully!")
        elif choice == "3":
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again!")
