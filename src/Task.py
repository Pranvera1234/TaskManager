class Task:
    """ Class representing a Task entity with attributes: task_id, title, and description. """
    def __init__(self, task_id, title, description):
        """ Initialize a new Task instance. """
        self.task_id = task_id
        self.title = title
        self.description = description


 

# Sample data
tasks_data = [
    Task(1, "Task 1", "Description for Task 1"),
    Task(2, "Task 2", "Description for Task 2"),
    Task(3, "Task 3", "Description for Task 3"),
]
