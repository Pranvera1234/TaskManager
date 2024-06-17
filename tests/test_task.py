

# --- Test Task --- #
# test_task.py
import unittest
from task import Task


class TestTask(unittest.TestCase):
    def setUp(self):
        # Create a new Task instance before each test
        self.task = Task("OOP Classes", "Complete a class with unit tests") 

    
    def test_mark_as_complete(self):
        # Test if mark_as_complete method correctly sets mark_as_complete to True
        self.task.mark_as_complete()
        self.assertEqual(self.task.mark_as_complete, True)
    
    
    def test_mark_as_incomplete(self):
        # Test if mark_as_incomplete method correctly sets mark_as_complete to False
        self.task.mark_as_incomplete()
        self.assertEqual(self.task.mark_as_incomplete, False)

    
    def test_set_grade_100(self):
        # Test if set_grade method correctly sets grade
        self.task.set_grade(100)
        self.assertEqual(self.task.grade, 100)


    def test_set_grade_30(self):
        # Test if set_grade method correctly sets grade
        self.task.set_grade(30)
        self.assertEqual(self.task.grade, 30)

    def test_submit(self):
        # Test if submit method correctly sets has_been_completed to True and is_graded to False
        self.task.submit()
        self.assertTrue(self.task.has_been_completed)
        self.assertFalse(self.task.is_graded)


if __name__ == '__main__':
    unittest.main()