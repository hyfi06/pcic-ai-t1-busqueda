from typing import Any, Callable


class PQueue:
    queue_list: list[tuple[int, Any]] = list()
    strategy: Callable[[list[tuple[int, Any]]], tuple[int, Any]]

    def __init__(self, pop_strategy: Callable[[list[tuple[int, Any]]], tuple[int, Any]]) -> None:
        self.strategy = pop_strategy

    def push(self, item: tuple[int, Any]) -> None:
        self.queue_list.append(item)

    def pop(self) -> tuple[int, Any]:
        value: tuple[int, Any] = self.strategy(self.queue_list)
        self.queue_list.remove(value)
        return value
