import copy
import sys

from typing import List
from algorithms.backtracking import backtracking
from ks import ks_read, Ks, ks_goal
from elapsed_time.decorators import execution_time


def ks_next_states(state: Ks) -> List[Ks]:
    list_of_idx: List[int] = state.variable_order()
    new_states: List[Ks] = list()
    for idx in list_of_idx[:min(len(list_of_idx), 3)]:
        new_state = copy.deepcopy(state)
        new_state.variables[idx] = new_state.domain_per_variable[idx].pop(0)
        new_states.append(new_state)
    return new_states


@execution_time
def main(fileName: str):
    Ks.capacity, Ks.items = ks_read(fileName)
    num_items = len(Ks.items)

    print(f"W:{Ks.capacity}, Items: {num_items}")
    initial_state = Ks(
        [0] * num_items,
        [list(range(1, 2)) for i in range(num_items)],
    )
    solution = backtracking(
        initial_state,
        ks_next_states,
        ks_goal,
    )


if __name__ == "__main__":
    fileName: str = sys.argv[1]
    main(fileName)
