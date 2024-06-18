from task import Task
from config import FILENAME


# Method to write all tasks in a file.
def appendTask(task):
    # open the file with write access
    file = open(FILENAME, "a")
    # write the task
    file.write(str(task.task_id) + "-" + task.title + "-" + task.description + "\n")
    # close the file
    file.close()


# Method to rewrite all tasks in a file.
def rewriteTasks(tasks):
    # open the file with write access
    file = open(FILENAME, "w")
    # write the task
    for task in tasks:
        file.write(
            str(task.task_id) + "-" + task.title + "-" + task.description + "\n"
        )
    # close the file
    file.close()


# Method to read all tasks in the file.
def readTasks():
    # open the file with read access
    file = open(FILENAME, "r")
    lines = file.readlines()

    tasks = {}

    for line in lines:
        words = line.split("-")
        if len(words) == 3:
            task_id = int(words[0])
            title = words[1]
            description = words[2]
            task = Task(task_id, title, description)
            tasks[task_id] = task
    # close the file
    file.close()
    return tasks
