import unittest

from taskmng.adapters.in_memory_task_repository import InMemoryTaskRepository
from taskmng.application.services.task_service import TaskService


class TaskServiceTests(unittest.TestCase):
    def setUp(self) -> None:
        self.repository = InMemoryTaskRepository()
        self.service = TaskService(self.repository)

    def test_create_task_persists_and_returns_task(self) -> None:
        task = self.service.create_task("Buy groceries")

        self.assertEqual("Buy groceries", task.title)
        self.assertFalse(task.completed)
        self.assertTrue(task.id)
        self.assertEqual([task], self.service.list_tasks())

    def test_create_task_strips_title(self) -> None:
        task = self.service.create_task("  Finish report  ")

        self.assertEqual("Finish report", task.title)

    def test_create_task_rejects_empty_title(self) -> None:
        with self.assertRaisesRegex(ValueError, "Task title cannot be empty"):
            self.service.create_task("   ")


if __name__ == "__main__":
    unittest.main()
