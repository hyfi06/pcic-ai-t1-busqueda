import copy
import sys
import random
from typing import List

from algorithms.taboo_search import taboo_search
from elapsed_time.decorators import execution_time
from elapsed_time.tools import timer
from ks import ks_read, Ks, ks_goal


def ks_height(state: Ks) -> float:
    return state.get_value() / (Ks.capacity - state.get_weight())


def ks_neighborhood(state: Ks) -> List[Ks]:
    new_states: List[Ks] = list()

    idx_items = [(i, item) for i, item in enumerate(Ks.items)]
    idx_items.sort(key=lambda enum: enum[1][1]/enum[1][0])

    idx_list_0 = [
        idx for (idx, item) in idx_items
        if state.variables[idx] == 0 and state.get_weight()+item[1] < Ks.capacity
    ]

    while state.get_weight() < Ks.capacity and len(idx_list_0):
        state.variables[idx_list_0.pop(0)] = 1
    new_state_0 = copy.deepcopy(state)
    new_states.append(new_state_0)

    idx_list_1 = [
        idx for (idx, item) in idx_items
        if state.variables[idx] == 1
    ]

    while state.get_weight() > Ks.capacity and len(idx_list_1):
        state.variables[idx_list_1.pop()] = 0
    new_state_1 = copy.deepcopy(state)
    new_states.append(new_state_1)

    while len(idx_list_0) and len(idx_list_1):
        idx_0 = idx_list_0.pop(0)
        idx_1 = idx_list_1.pop()
        new_state = copy.deepcopy(state)
        new_state.variables[idx_0] = 1
        new_state.variables[idx_1] = 0
        new_states.append(new_state)
    return new_states


@execution_time
def main(fileName: str, max_time) -> None:
    Ks.capacity, Ks.items = ks_read(fileName)
    num_items = len(Ks.items)

    print(f"W:{Ks.capacity}, Items: {num_items}")
    initial_state = Ks(
        [random.randint(0, 1) for _ in range(num_items)],
        [[1] for _ in range(num_items)]
    )

    solution = taboo_search(
        initial_state,
        ks_height,
        ks_neighborhood,
        ks_goal,
        timer(max_time),
    )

    print(solution)


if __name__ == "__main__":
    fileName: str = sys.argv[1]
    max_time: int = 60*24
    try:
        max_time = int(sys.argv[2])
    except IndexError:
        pass
    main(fileName, max_time)
