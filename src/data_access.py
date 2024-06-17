from task import Task


# data_access.py
class TaskRepository:

    def __init__(self):
        self.tasks = {}

    def add_task(self, task_id, task_title, task_description):
        if task_id in self.tasks.keys():
            print("Task cannot be added, because this id exists.")
        else:
            task = Task(task_id, task_title, task_description)
            self.tasks[task_id] = task
            print(f"Task added: {task.description}.")

    def get_all_tasks(self):
        return self.tasks.values()

    def remove_task(self, task):
        task_id = task.task_id
        if task.task_id in self.tasks.keys():
            del self.tasks[task_id]
            print(f"Task with ID {task_id} removed.")
        else:
            print(f"Task with ID {task_id} not found.")

    def remove_task_withId(self, task_id):
        if task_id in self.tasks.keys():
            del self.tasks[task_id]
            print(f"Task with ID {task_id} removed.")
        else:
            print(f"Task with ID {task_id} not found.")

    def display_tasks(self):
        print("Tasks in the to-do list:")
        for task in self.tasks.values():
            task.display_task_details()

    def mark_task_as_complete(self, task_id):
        if task_id in self.tasks.keys:
            self.tasks[task_id].complete_task()
            print(f"Task with ID {task_id} marked as complete.")
        else:
            print(f"Task with ID {task_id} not found.")

    def get_task(self, task_id):
        """ Read and display information for a task based on its ID. """
        if task_id in self.tasks.keys():
            print(f"Task with ID {task_id} marked as complete.")
            return self.tasks[task_id]
        else:
            print(f"Task with ID {task_id} not found.")

    def read_task(self, task_id):
        """ Read and display information for a task based on its ID. """
        for task in self.tasks:
            if task.task_id == task_id:
                t_id = task.task_id
                title = task.title
                text = task.description
                print(f"Found- ID: {t_id}, Title: {title}, Descr: {text}\n")
                return
        print(f"Task with ID {task_id} not found.\n")

    def update_task(self, task_id, new_title, new_description):
        """ Update the title and description of a task based on its ID. """
        for task in self.tasks:
            if task.task_id == task_id:
                task.title = new_title
                task.description = new_description
                print("Task updated successfully!")
                return
        print(f"Task with ID {task_id} not found.")

    def delete_task(self, task_id):
        """ Delete a task based on its ID. """
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
