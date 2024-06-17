# tests.py
import unittest
from business_logic import TaskService
from task import Task


class TestTaskService(unittest.TestCase):
    def test_add_task(self):
        """Test the add_task method of TaskService."""
        # Arrange
        task_service = TaskService()
        initial_task_count = len(task_service.get_all_tasks())  # Get initial task count
        new_task = Task(task_id=1, title="First Task", description="OOP Classes")
        # Act
        task_service.add_task(new_task)
        # Assert
        updated_task_count = len(task_service.get_all_tasks())  # Get updated task count
        self.assertEqual(updated_task_count, initial_task_count + 1) # Check if the task count increased by 1
        task_service.display_tasks()
        self.assertIn(new_task, task_service.get_all_tasks())  # Check that the newly created task is there

    def test_remove_task(self):
        """Test the add_task method of TaskService."""
        # Arrange
        task_service = TaskService()
        initial_task_count = len(task_service.get_all_tasks())  # Get initial task count
        new_task = Task(task_id=2, title="Second Task", description="OOP Class Tests")
        # Act
        task_service.add_task(new_task)
        # Assert
        updated_task_count = len(task_service.get_all_tasks())  # Get updated task count
        self.assertEqual(updated_task_count, initial_task_count + 1) # Check if the task count increased by 1
        task_service.display_tasks()
        task_service.remove_task(new_task)
        self.assertNotIn(new_task, task_service.get_all_tasks())  # Check that the newly created task is there
          
    
   
if __name__ == "__main__":
    unittest.main()
