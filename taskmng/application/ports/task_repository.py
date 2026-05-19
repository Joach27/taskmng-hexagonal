from typing import Protocol

from taskmng.domain.task import Task


class TaskRepositoryPort(Protocol):
    def add(self, task: Task) -> None:
        ...

    def list_all(self) -> list[Task]:
        ...
