from typing import TypeVar, Generic, Callable, Optional
S = TypeVar('S')
T = TypeVar('T')


class PQueue(Generic[S, T]):
    def __init__(self, sort_function: Optional[Callable] = lambda item: item[0]) -> None:
        self.queue_list: list[tuple[S, T]] = list()
        self.sort_function = sort_function

    def push(self, priority: S, item: T) -> None:
        self.queue_list.append((priority, item))
        self.queue_list.sort(key=self.sort_function)

    def pop(self) -> tuple[S, T]:
        return self.queue_list.pop(0)

    def get_items(self) -> set[T]:
        return set([item for (_, item) in self.queue_list]) if len(self.queue_list) else set()

    def __len__(self) -> int:
        return self.queue_list.__len__()

    def __str__(self) -> str:
        return self.queue_list.__str__()
