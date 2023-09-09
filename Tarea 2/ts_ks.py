import copy
import sys

from typing import List, Tuple, Callable, Optional

from algorithms.taboo_search import State, taboo_search
from elapsed_time.decorators import execution_time
from elapsed_time.tools import timer
from ks import ks_read, Ks, ks_print, ks_goal


def ks_height(state: Ks) -> float:
    return state.get_value() / (Ks.capacity - state.get_weight())


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


@execution_time
def main(fileName: str, max_time):
    Ks.capacity, Ks.items = ks_read(fileName)
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
        timer(max_time),
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
