from typing import TypeAlias, Generic, TypeVar

T = TypeVar('T')

PriorityItem: TypeAlias = tuple[T, int]


class PQueue(Generic[T]):
    queue_list: list[PriorityItem[T]] = list()

    def push(self, item: PriorityItem[T]) -> None:
        self.queue_list.append(item)

    def pop(self) -> PriorityItem[T]:
        pItem = self.queue_list[0]
        min_priority: int = pItem[1]
        for item in self.queue_list:
            if item[1] < min_priority:
                pItem = item
                min_priority = pItem[1]

        self.queue_list.remove(pItem)
        return pItem

    def __len__(self) -> int:
        return self.queue_list.__len__()
