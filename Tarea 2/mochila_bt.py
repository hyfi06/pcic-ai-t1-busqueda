import copy
import sys
import time

from typing import List, Tuple
from abc import abstractproperty

from algorithms.backtracking import State, backtracking, T


class Ks(State[int]):
    size: int = 0

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
            if self.variables[idx]
        ])

    @abstractproperty
    def is_valid(self) -> bool:
        return self.get_weight() <= Ks.size


def ks_goal(state: Ks) -> bool:
    return state.is_valid and max([len(domain) for domain in state.domain_per_variable]) == 0 and min(state.variables) != 0

# import pdb; pdb.set_trace()


def ks_next_states(state: Ks) -> List[Ks]:
    list_of_idx: List[int] = state.variable_order()
    new_states = list()
    for idx in list_of_idx:
        new_state = copy.deepcopy(state)
        new_state.variables[idx] = new_state.domain_per_variable[idx].pop(0)
        new_state.domain_per_variable[idx] = []
        for i in range(len(state.domain_per_variable)):
            # import pdb; pdb.set_trace()
            try:
                new_state.domain_per_variable[i].remove(
                    new_state.variables[idx])
            except ValueError:
                pass
            try:
                new_state.domain_per_variable[i].remove(
                    new_state.variables[idx]+abs(i-idx))
            except ValueError:
                pass
            try:
                new_state.domain_per_variable[i].remove(
                    new_state.variables[idx]-abs(i-idx))
            except ValueError:
                pass
        new_states.append(new_state)
    return new_states


def main(fileName: str):
    initial_state = Ks(
        [0]*n,
        [list(range(1, n+1)) for i in range(n)]
    )
    solution = backtracking(
        initial_state,
        ks_next_states,
        ks_goal
    )
    print(solution)


if __name__ == "__main__":
    print(time.strftime('%c'))
    fileName: str = sys.argv[1]
    main(fileName)
    print(time.strftime('%c'))
