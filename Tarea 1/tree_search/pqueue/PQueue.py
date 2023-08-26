from typing import TypeAlias, Callable, Generic, TypeVar

T = TypeVar('T')

PriorityItem: TypeAlias = tuple[T, int]
Strategy: TypeAlias = Callable[[list[PriorityItem]], PriorityItem]


class PQueue(Generic[T]):
    queue_list: list[PriorityItem] = list()
    strategy: Strategy

    def __init__(self, pop_strategy: Strategy) -> None:
        self.strategy = pop_strategy

    def push(self, item: PriorityItem) -> None:
        self.queue_list.append(item)

    def pop(self) -> PriorityItem:
        value: PriorityItem = self.strategy(self.queue_list)
        self.queue_list.remove(value)
        return value
