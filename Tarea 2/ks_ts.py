import copy
import sys
import time
import math

from typing import List, Tuple, Callable, Optional

from algorithms.taboo_search import State, taboo_search
from elapsed_time.decorators import execution_time


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
    items: List[Tuple[int, int]] = list()

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

    @property
    def is_full(self) -> bool:
        return len([
            item for (idx, item) in enumerate(Ks.items)
            if self.variables[idx] == 0 and self.get_weight() + item[1] < Ks.capacity
        ]) == 0

    def get_items(self) -> List[Tuple[int, Tuple[int, int]]]:
        return [
            (idx, item) for (idx, item) in enumerate(Ks.items)
            if self.variables[idx] == 1
        ]

    @property
    def is_valid(self) -> bool:
        return self.get_weight() <= Ks.capacity


def ks_height(state: Ks) -> float:
    return (1 if state.is_valid else -1) * state.get_value()


def ks_neighborhood(state: Ks) -> List[Ks]:
    new_states: List[Ks] = list()
    idx_items = [(i, item) for i, item in enumerate(state.items)]
    idx_items.sort(key=lambda enum: enum[1][1]/enum[1][0])
    idx_list_0 = [
        idx for (idx, item) in idx_items
        if state.variables[idx] == 0
    ]

    idx_list_1 = [
        idx for (idx, item) in idx_items
        if state.variables[idx] == 0
    ]

    if state.get_weight() < Ks.capacity:
        for idx in idx_list_0[:len(idx_list_0)//2]:
            new_state = copy.deepcopy(state)
            new_state.variables[idx] = 1
            new_states.append(new_state)

    if state.get_weight() > Ks.capacity:
        for idx in idx_list_1[len(idx_list_0)//2:]:
            new_state = copy.deepcopy(state)
            new_state.variables[idx] = 0
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


@execution_time
def main(fileName: str, max_time):
    (Ks.capacity, Ks.items) = read_problem(fileName)
    print(f"W:{Ks.capacity}, Items: {len(Ks.items)}")
    initial_state = Ks(
        [0]*len(Ks.items),
        [[1] for i in range(len(Ks.items))]
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
    fileName: str = sys.argv[1]
    max_time: int = 60*24
    try:
        max_time = int(sys.argv[2])
    except IndexError:
        pass
    main(fileName, max_time)
