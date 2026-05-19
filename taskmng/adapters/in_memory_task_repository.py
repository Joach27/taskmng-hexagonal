from taskmng.domain.task import Task


class InMemoryTaskRepository:
    def __init__(self) -> None:
        self._tasks: list[Task] = []

    def add(self, task: Task) -> None:
        self._tasks.append(task)

    def list_all(self) -> list[Task]:
        return list(self._tasks)
