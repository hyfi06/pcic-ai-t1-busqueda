from typing import List, Tuple
from algorithms.models import State
from elapsed_time.tools import print_time


def ks_read(fileName) -> Tuple[int, List[Tuple[int, int]]]:
    data: List[str] = list()
    with open(fileName, mode='r') as file:
        data = file.readlines()
    items: List[Tuple[int, int]] = [
        tuple([int(i) for i in row.split(' ')])
        for row in data
        if row
    ]  # type: ignore
    objects_num, capacity = items.pop(0)
    assert len(items) == objects_num

    return (capacity, items)


class Ks(State[int]):
    capacity: int = 0
    max_value = 0
    items: List[Tuple[int, int]] = list()

    def variable_order(self) -> List[int]:
        idx_items = list(enumerate(Ks.items))
        idx_items.sort(key=lambda enum: enum[1][1]/enum[1][0])
        return [
            idx for (idx, item) in idx_items
            if self.variables[idx] == 0 and self.get_weight() + item[1] < Ks.capacity
        ]

    def get_value(self) -> int:
        return sum([
            value for (idx, (value, weight)) in enumerate(Ks.items)
            if self.variables[idx]
        ])

    def get_weight(self) -> int:
        return sum([
            weight for (idx, (value, weight)) in enumerate(Ks.items)
            if self.variables[idx] == 1
        ])

    def get_items(self) -> List[Tuple[int, Tuple[int, int]]]:
        return [
            (idx, item) for (idx, item) in enumerate(self.items)
            if self.variables[idx] == 1
        ]

    @property
    def is_full(self) -> bool:
        return len([
            item for (idx, item) in enumerate(self.items)
            if self.variables[idx] == 0 and self.get_weight() + item[1] < Ks.capacity
        ]) == 0

    @property
    def is_valid(self) -> bool:
        return self.get_weight() <= Ks.capacity


def ks_print(state: Ks) -> None:
    print_time()
    print(f"V:{state.get_value()} W:{state.get_weight()}")
    print("Items:")
    print(state.get_items(), end='\n\n')


def ks_goal(state: Ks) -> bool:
    if state.is_valid and state.is_full and state.get_value() > Ks.max_value:
        Ks.max_value = state.get_value()
        ks_print(state)
        return True
    return False