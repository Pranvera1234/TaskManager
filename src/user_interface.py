# user_interface.py
from business_logic import TaskService
from task import Task


# Method to start the user interface.
def start_application():
    """Start the Task Management Application."""
    task_service = TaskService()

    while True:
        print("Task Management Application")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("Tasks:")
            task_service.display_tasks()
        elif choice == "2":
            task_id = int(input("Enter task id: "))
            task_title = input("Enter task title: ")
            task_description = input("Enter task description: ")
            task = Task(task_id, task_title, task_description)
            task_service.add_task(task)
            print("Task added successfully!")
        elif choice == "3":
            task_id = input("Enter task id: ")
            task_service.remove_task(task_id)
        elif choice == "4":
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again!")
