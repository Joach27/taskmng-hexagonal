from uuid import uuid4

from taskmng.application.ports.task_repository import TaskRepositoryPort
from taskmng.domain.task import Task


class TaskService:
    def __init__(self, repository: TaskRepositoryPort) -> None:
        self._repository = repository

    def create_task(self, title: str) -> Task:
        cleaned_title = title.strip()
        if not cleaned_title:
            raise ValueError("Task title cannot be empty")

        task = Task(id=str(uuid4()), title=cleaned_title)
        self._repository.add(task)
        return task

    def list_tasks(self) -> list[Task]:
        return self._repository.list_all()
