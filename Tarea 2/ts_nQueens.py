import copy
import sys
import random

from typing import List

from algorithms.taboo_search import taboo_search, State
from elapsed_time.decorators import execution_time
from queens import nQueens


def nq_height(state: nQueens) -> int:
    return -state.get_num_conflicts()


def nq_neighborhood(state: nQueens) -> List[nQueens]:
    new_states: List[nQueens] = list()
    for (idx, value) in enumerate(state.variables):
        for j in state.domain_per_variable[idx]:
            if abs(value-j) % 2 == 1:
                new_state = copy.deepcopy(state)
                new_state.variables[idx] = j
                new_states.append(new_state)
    return new_states


def nq_goal(state: nQueens) -> bool:
    return state.get_num_conflicts() == 0


def nq_time() -> bool:
    return True


@execution_time
def main(n: int):
    random_sol: List[int] = list(range(1, n+1))
    random.shuffle(random_sol)
    initial_state = nQueens(
        random_sol,
        [list(range(1, n+1)) for i in range(n)]
    )
    solution = taboo_search(
        initial_state,
        nq_height,
        nq_neighborhood,
        nq_goal,
        nq_time,
    )
    print(solution)


if __name__ == "__main__":
    n: int = int(sys.argv[1])
    main(n)
