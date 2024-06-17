
# --- Task Class --- #
class Task:
    """ Class representing a Task entity with attributes: task_id, title, and description. """
    def __init__(self, task_id, title, description):
        """ Initialize a new Task instance. """
        self.task_id = task_id
        self.title = title
        self.description = description


    # Declare the class variable, with default value, for tasks. 
    has_been_completed = False
    is_graded = False
    grade = 0

    # Method to change 'has_been_completed' task from False to True.
    def mark_as_complete(self) :
        self.has_been_completed = True

    # Method to change 'has_been_completed' emails from True to False.
    def mark_as_incomplete(self) :
        self.has_been_completed = False

    # Method to change 'is_graded' task from False to True.
    def set_grade(self, grade) :
        self.grade = grade
        self.is_graded = True

    # Method to change 'has_been_completed' and 'is_graded' task from True to False.
    def submit(self) :
        self.has_been_completed = False
        self.is_graded = False

# Sample data
tasks_data = [
    Task(1, "Task 1", "Description for Task 1"),
    Task(2, "Task 2", "Description for Task 2"),
    Task(3, "Task 3", "Description for Task 3"),
]
