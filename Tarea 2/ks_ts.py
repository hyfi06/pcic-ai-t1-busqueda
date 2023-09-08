import copy
import sys
import time

from typing import List, Tuple, Callable, Optional

from algorithms.taboo_search import State, taboo_search


def read_problem(fileName) -> Tuple[int, List[Tuple[int, int]]]:
    data: List[str] = list()
    with open(fileName, mode='r') as file:
        data = file.readlines()
    fist_line: List[int] = [int(i) for i in (data.pop(0)).split(' ')]
    [objects_num, capacity] = fist_line

    items: List[Tuple[int, int]] = [
        tuple([int(i) for i in row.split(' ')])
        for row in data
        if row
    ]  # type: ignore
    assert (len(items) == objects_num)

    return (capacity, items)


class Ks(State[int]):
    capacity: int = 0
    max_value = 0

    def __init__(
        self,
        values: List[int],
        domain_per_variable: List[List[int]],
        items: List[Tuple[int, int]]
    ) -> None:
        super().__init__(values, domain_per_variable)
        self.items = items

    def get_value(self) -> int:
        return sum([
            value for (idx, (value, weight)) in enumerate(self.items)
            if self.variables[idx]
        ])

    def get_weight(self) -> int:
        return sum([
            weight for (idx, (value, weight)) in enumerate(self.items)
            if self.variables[idx] == 1
        ])

    @property
    def is_full(self) -> bool:
        return len([
            item for (idx, item) in enumerate(self.items)
            if self.variables[idx] == 0 and self.get_weight() + item[1] < Ks.capacity
        ]) == 0

    def get_items(self) -> List[Tuple[int, Tuple[int, int]]]:
        return [
            (idx, item) for (idx, item) in enumerate(self.items)
            if self.variables[idx] == 1
        ]

    @property
    def is_valid(self) -> bool:
        return self.get_weight() <= Ks.capacity


def ks_height(state: Ks) -> int:
    return state.get_value()


def ks_neighborhood(state: Ks) -> List[Ks]:
    new_states: List[Ks] = list()
    idx_items = [(i, item) for i, item in enumerate(state.items)]
    idx_items.sort(key=lambda enum: enum[1][1]/enum[1][0])

    for i, (idx, (value, weight)) in enumerate(idx_items):
        s_value = state.variables[idx]
        s_weight = state.get_weight()
        if s_value == 0 and weight + s_weight > Ks.capacity:
            continue
        if s_value == 0 and i >  len(idx_items) * 0.9:
            continue
        if s_value == 1 and i < len(idx_items) * 0.1:
            continue
        new_state = copy.deepcopy(state)
        new_state.variables[idx] = 1 - s_value
        new_states.append(new_state)

    return new_states


def ks_goal(state: Ks) -> bool:
    if state.is_valid and state.is_full and state.get_value() > Ks.max_value:
        Ks.max_value = state.get_value()
        print(time.strftime("%Y-%m-%d %H:%M:%S"))
        print(f"V:{state.get_value()} W:{state.get_weight()}")
        print("Items:")
        print(state.get_items())
        print('\n')
        return True
    return False


def ks_time(minutes: int) -> Callable[[], bool]:
    start: float = time.time()

    def stopwatch():
        current_time: float = time.time()
        diff_time: float = current_time - start
        return minutes*60.0 > diff_time

    return stopwatch

# import pdb; pdb.set_trace()


def main(fileName: str, max_time):
    (capacity, items) = read_problem(fileName)
    Ks.capacity = capacity
    print(f"W:{capacity}, Items: {len(items)}")
    initial_state = Ks(
        [0]*len(items),
        [[1] for i in range(len(items))],
        items
    )

    solution = taboo_search(
        initial_state,
        ks_height,
        ks_neighborhood,
        ks_goal,
        ks_time(max_time),
        False
    )
    # print(solution)


if __name__ == "__main__":
    print(time.strftime('%c'))
    fileName: str = sys.argv[1]
    max_time: int = 60*24
    try:
        max_time = int(sys.argv[2])
    except IndexError:
        pass
    main(fileName, max_time)
    print(time.strftime('%c'))
