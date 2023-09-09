import copy
import sys

from typing import List
from elapsed_time.decorators import execution_time
from algorithms.backtracking import backtracking
from graph_c import gc_read, Gc, gc_print


def next_gc(state: Gc) -> List[Gc]:
    idx = state.variable_order()[0]
    new_states: List[Gc] = list()
    new_state = copy.deepcopy(state)
    new_state.variables[idx] = new_state.domain_per_variable[idx].pop(0)
    new_state.domain_per_variable[idx] = []
    for i in Gc.edges[idx]:
        try:
            new_state.domain_per_variable[i].remove(
                new_state.variables[idx])
        except ValueError:
            pass
    new_states.append(new_state)

    return new_states


def goal_gc(state: Gc) -> bool:
    if state.is_complete:
        gc_print(state)
        return True
    return False


@execution_time
def main(fileName: str) -> None:
    num_vertices, Gc.edges = gc_read(fileName)
    initial_state = Gc(
        [0]*num_vertices,
        [list(range(1, num_vertices+1)) for _ in range(num_vertices)]
    )
    solution = backtracking(
        initial_state,
        next_gc,
        goal_gc
    )


if __name__ == "__main__":
    fileName: str = sys.argv[1]
    main(fileName)
