
def display_tasks():
    """ Display information for all tasks. """
    print("Tasks:")
    for task in tasks_data:
        print(f"ID: {task.task_id}, Title: {task.title}, Description:
{task.description}")
print()

def read_task(task_id):
    """ Read and display information for a task based on its ID. """
    for task in tasks_data:
        if task.task_id == task_id:
            print(f"Task found - ID: {task.task_id}, Title:
            {task.title}, Description: {task.description}\n")
            return
        print(f"Task with ID {task_id} not found.\n")

def update_task(task_id, new_title, new_description):
    """ Update the title and description of a task based on its ID. """
    for task in tasks_data:
        if task.task_id == task_id:
            task.title = new_title
            task.description = new_description
            print(f"Task updated successfully!\n")
            return
    print(f"Task with ID {task_id} not found.\n")

def delete_task(task_id):
    """ Delete a task based on its ID. """
    for i, task in enumerate(tasks_data):
        if task.task_id == task_id:
            del tasks_data[i]
            print(f"Task deleted successfully!\n")
            return
        print(f"Task with ID {task_id} not found.\n")