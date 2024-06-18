from task import Task
from utilities import readTasks, appendTask, rewriteTasks


# data_access.py
class TaskRepository:

    # Initialise method with empty tasks.
    def __init__(self):
        self.tasks = readTasks()

    # Method to add a task.
    def add_task(self, task):
        if task.task_id in self.tasks.keys():
            print("Task cannot be added, because this id exists.")
        else:
            self.tasks[task.task_id] = task
            appendTask(task)
            print(f"Task added: {task.description}.")

    # Method to get all tasks.
    def get_all_tasks(self):
        return self.tasks.values()

    # Method to remove a task.
    def remove_task(self, task):
        task_id = task.task_id
        if task.task_id in self.tasks.keys():
            del self.tasks[task_id]
            print(f"Task with ID {task_id} removed.")
        else:
            print(f"Task with ID {task_id} not found.")

    # Method to remove a task by id.
    def remove_task_withId(self, task_id):
        if task_id in self.tasks.keys():
            del self.tasks[task_id]
            rewriteTasks(self.tasks.values())
            print(f"Task with ID {task_id} removed.")
        else:
            print(f"Task with ID {task_id} not found.")

    # Method to print the tasks.
    def display_tasks(self):
        if len(self.tasks) == 0:
            print("There are no tasks. Please Add a task first.")
        else:
            print("Tasks in the to-do list:")
            for task in self.tasks.values():
                task.display_task_details()

    # Method to mark task as complete by id.
    def mark_task_as_complete(self, task_id):
        if task_id in self.tasks.keys:
            self.tasks[task_id].complete_task()
            print(f"Task with ID {task_id} marked as complete.")
        else:
            print(f"Task with ID {task_id} not found.")

    # Method to get a task by id.
    def get_task(self, task_id):
        """Read and display information for a task based on its ID."""
        if task_id in self.tasks.keys():
            print(f"Task with ID {task_id} marked as complete.")
            return self.tasks[task_id]
        else:
            print(f"Task with ID {task_id} not found.")

    # Method to print a task by getting it by id.
    def read_task(self, task_id):
        """Read and display information for a task based on its ID."""
        for task in self.tasks:
            if task.task_id == task_id:
                t_id = task.task_id
                title = task.title
                text = task.description
                print(f"Found- ID: {t_id}, Title: {title}, Descr: {text}\n")
                return
        print(f"Task with ID {task_id} not found.\n")

    # Method to update a task by getting it by id.
    def update_task(self, task_id, new_title, new_description):
        """Update the title and description of a task based on its ID."""
        for task in self.tasks:
            if task.task_id == task_id:
                task.title = new_title
                task.description = new_description
                print("Task updated successfully!")
                return
        print(f"Task with ID {task_id} not found.")

    # Method to delete a task by getting it by id.
    def delete_task(self, task_id):
        """Delete a task based on its ID."""
        for i, task in enumerate(self.tasks):
            if task.task_id == task_id:
                del self.tasks[i]
                print("Task deleted successfully!")
                return
        print(f"Task with ID {task_id} not found.")


# Sample data
tasks_data = [
    Task(1, "Task 1", "Description for Task 1"),
    Task(2, "Task 2", "Description for Task 2"),
    Task(3, "Task 3", "Description for Task 3"),
]
