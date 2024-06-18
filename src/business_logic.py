# business_logic.py
from data_access import TaskRepository
from task import Task


class TaskService:
    # Initialise method to initialise the taskRepository.
    def __init__(self):
        """Initialise the TaskService with a TaskRepository."""
        self.task_repository = TaskRepository()

    # Method to get all tasks.
    def get_all_tasks(self):
        """Get all tasks from the data source."""
        return self.task_repository.get_all_tasks()

    # Method to add a task.
    def add_task(self, task):
        """Add a new task to the data source."""
        self.task_repository.add_task(task)

    # Method to get a task by task_id.
    def get_task(self, task):
        """Get task from the data source."""
        self.task_repository.get_task(task.task_id)

    # Method to print all tasks.
    def display_tasks(self):
        """Display task from the data source."""
        self.task_repository.display_tasks()

    # Method to remove_task a task by id.
    def remove_task(self, task_id):
        """Remove task from the data source."""
        self.task_repository.remove_task_withId(task_id)


# Sample data
tasks_data = [
    Task(1, "Task 1", "Description for Task 1"),
    Task(2, "Task 2", "Description for Task 2"),
    Task(3, "Task 3", "Description for Task 3"),
]
