import copy
import sys
from algorithms.backtracking import State, backtracking
import time


class nQueens(State[int]):
    @property
    def is_valid(self) -> bool:
        return super().is_valid


def nQueens_goal(state: nQueens) -> bool:
    return state.is_valid and max([len(domain) for domain in state.domain_per_variable]) == 0 and min(state.variables) != 0

# import pdb; pdb.set_trace()


def nQueens_next_states(state: nQueens) -> list[nQueens]:
    list_of_idx: list[int] = state.variable_order()
    new_states = list()
    for idx in list_of_idx:
        new_state = copy.deepcopy(state)
        new_state.variables[idx] = new_state.domain_per_variable[idx].pop(0)
        # new_state.domain_per_variable[idx] = []
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


def main(n: int):
    initial_state = nQueens(
        [0]*n,
        [list(range(1, n+1)) for i in range(n)]
    )
    solution = backtracking(
        initial_state,
        nQueens_next_states,
        nQueens_goal
    )
    print(solution)


if __name__ == "__main__":
    print(time.strftime('%c'))
    n: int = int(sys.argv[1])
    main(n)
    print(time.strftime('%c'))
