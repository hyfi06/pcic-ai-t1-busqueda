import copy
import sys
import random

from typing import List
from elapsed_time.decorators import execution_time
from elapsed_time.tools import timer
from algorithms.taboo_search import taboo_search
from eggholder import EggHolder, eh_height, eh_goal


def eh_neighborhood(state: EggHolder) -> List[EggHolder]:
    depth = 50
    x0_b = state.variables[0] - min(state.domain_per_variable[0])
    x0_f = max(state.domain_per_variable[0]) - state.variables[0]
    x1_b = state.variables[1] - min(state.domain_per_variable[1])
    x1_f = max(state.domain_per_variable[1]) - state.variables[1]
    new_states: List[EggHolder] = list()

    for d in range(1, depth+1):
        new_state_f_s = copy.deepcopy(state)
        new_state_f_s.variables[0] = state.variables[0] + x0_f/(2*d)
        new_state_b_s = copy.deepcopy(state)
        new_state_b_s.variables[0] = state.variables[0] - x0_b/(2*d)
        new_state_s_f = copy.deepcopy(state)
        new_state_s_f.variables[1] = state.variables[1] + x1_f/(2*d)
        new_state_s_b = copy.deepcopy(state)
        new_state_s_b.variables[1] = state.variables[1] - x1_b/(2*d)

        new_state_f_f = copy.deepcopy(state)
        new_state_f_f.variables[0] = state.variables[0] + x0_f/(2*d)
        new_state_f_f.variables[1] = state.variables[1] + x1_f/(2*d)
        new_state_b_b = copy.deepcopy(state)
        new_state_b_b.variables[0] = state.variables[0] - x0_b/(2*d)
        new_state_b_b.variables[1] = state.variables[1] - x1_b/(2*d)
        new_state_b_f = copy.deepcopy(state)
        new_state_b_f.variables[0] = state.variables[0] - x0_b/(2*d)
        new_state_b_f.variables[1] = state.variables[1] + x1_f/(2*d)
        new_state_f_b = copy.deepcopy(state)
        new_state_f_b.variables[0] = state.variables[0] + x0_f/(2*d)
        new_state_f_b.variables[1] = state.variables[1] - x1_b/(2*d)
        new_states.extend([
            new_state_f_s, new_state_b_s, new_state_s_f, new_state_s_b,
            new_state_f_f, new_state_b_b, new_state_b_f, new_state_f_b
        ])
    return new_states


@execution_time
def main(max_time) -> None:

    initial_state = EggHolder(
        [random.uniform(-512, 512), random.uniform(-512, 512)],
        [[-512, 512], [-512, 512]]
    )
    solution = taboo_search(
        initial_state,
        eh_height,
        eh_neighborhood,
        eh_goal,
        timer(max_time),
        False
    )
    # print(solution)


if __name__ == "__main__":
    max_time: int = 60*24
    try:
        max_time = int(sys.argv[1])
    except IndexError:
        pass
    main(max_time)
