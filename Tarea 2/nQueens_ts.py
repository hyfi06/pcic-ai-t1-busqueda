import copy
import sys
import time
import random

from typing import List

from algorithms.taboo_search import taboo_search, State


class nQueens(State[int]):
    def get_num_conflicts(self) -> int:
        conflicts: int = 0
        for idx, value1 in list(enumerate(self.variables))[:-1]:
            for jdx, value2 in list(enumerate(self.variables))[idx+1:]:
                if value1 == value2:
                    conflicts += 1
                if abs(value1 - value2) == abs(idx - jdx):
                    conflicts += 1
        return conflicts


def nq_height(state: nQueens) -> int:
    return -state.get_num_conflicts()


def nq_neighborhood(state: nQueens) -> List[nQueens]:
    new_states: List[nQueens] = list()
    for (idx, value) in enumerate(state.variables):
        if value > min(state.domain_per_variable[idx]):
            new_state = copy.deepcopy(state)
            new_state.variables[idx] = value - 1
            new_states.append(new_state)
        if value < max(state.domain_per_variable[idx]):
            new_state = copy.deepcopy(state)
            new_state.variables[idx] = value + 1
            new_states.append(new_state)
    return new_states


def nq_goal(state: nQueens) -> bool:
    return state.get_num_conflicts() == 0


def nq_time() -> bool:
    return True


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
    print(time.strftime('%c'))
    n: int = int(sys.argv[1])
    main(n)
    print(time.strftime('%c'))
