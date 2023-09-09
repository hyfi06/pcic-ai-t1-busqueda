import copy
import sys
import time

from typing import List, Tuple

from algorithms.backtracking import State, backtracking


def read_problem(fileName) -> Tuple[int, List[Tuple[int, int]]]:
    data: List[str] = list()
    with open(fileName, mode='r') as file:
        data = file.readlines()
    items: List[Tuple[int, int]] = [
        tuple([int(i) for i in row.split(' ')])
        for row in data
        if row
    ]  # type: ignore
    [objects_num, capacity] = items.pop(0)
    assert (len(items) == objects_num)

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


def ks_goal(state: Ks) -> bool:
    if state.is_valid and state.is_full and state.get_value() > Ks.max_value:
        Ks.max_value = state.get_value()
        print(
            f"V:{state.get_value()} W:{state.get_weight()} Items:{state.get_items()}")
        return True
    return False

# import pdb; pdb.set_trace()


def ks_next_states(state: Ks) -> List[Ks]:
    list_of_idx: List[int] = state.variable_order()
    new_states: List[Ks] = list()
    for idx in list_of_idx[:min(len(list_of_idx), 3)]:
        new_state = copy.deepcopy(state)
        new_state.variables[idx] = new_state.domain_per_variable[idx].pop(0)
        new_states.append(new_state)
    return new_states


def main(fileName: str):
    Ks.capacity, Ks.items = read_problem(fileName)

    print(f"W:{Ks.capacity}, Items: {len(Ks.items)}")
    initial_state = Ks(
        [0]*len(Ks.items),
        [list(range(1, 2)) for i in range(len(Ks.items))],
    )
    solution = backtracking(
        initial_state,
        ks_next_states,
        ks_goal,
        False
    )
    # print(solution)


if __name__ == "__main__":
    print(time.strftime('%c'))
    fileName: str = sys.argv[1]
    main(fileName)
    print(time.strftime('%c'))
