# tests.py
import unittest
from business_logic import TaskService
from task import Task


class TestTaskService(unittest.TestCase):
    def test_add_task(self):
        """Test the add_task method of TaskService."""
        # Arrange
        task_service = TaskService()

        # Get initial task count
        initial_task_count = len(task_service.get_all_tasks())
        new_task = Task(
            task_id=1, title="First Task", description="OOP Classes"
        )
        # Act
        task_service.add_task(new_task)

        # Get updated task count
        updated_task_count = len(task_service.get_all_tasks())
        # Check if the task count increased by 1
        self.assertEqual(updated_task_count, initial_task_count + 1)
        task_service.display_tasks()
        # Check that the newly created task is there
        self.assertIn(new_task, task_service.get_all_tasks())

    def test_remove_task(self):
        """Test the remove_task method of TaskService."""
        # Arrange
        task_service = TaskService()
        # Get initial task count
        initial_task_count = len(task_service.get_all_tasks())
        new_task = Task(
            task_id=2, title="Second Task", description="OOP Class Tests"
        )
        # Act
        task_service.add_task(new_task)
        # Get updated task count
        updated_task_count = len(task_service.get_all_tasks())
        # Check if the task count increased by 1
        self.assertEqual(updated_task_count, initial_task_count + 1)
        task_service.display_tasks()
        task_service.remove_task(new_task.task_id)
        # Check that the newly created task is NOT there
        self.assertNotIn(new_task, task_service.get_all_tasks())
        # Get updated task count
        updated_task_count = len(task_service.get_all_tasks())
        # Check if the task count decreased by 1
        self.assertEqual(updated_task_count, initial_task_count)


if __name__ == "__main__":
    unittest.main()
