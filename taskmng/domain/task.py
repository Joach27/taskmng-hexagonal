from dataclasses import dataclass


@dataclass(frozen=True)
class Task:
    id: str
    title: str
    completed: bool = False
