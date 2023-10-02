import copy
import sys
import random

from typing import List
from elapsed_time.decorators import execution_time
from elapsed_time.tools import timer
from algorithms.taboo_search import taboo_search
from eggholder import EggHolder, eh_height, eh_goal


def eh_neighborhood(state: EggHolder) -> List[EggHolder]:
    x0_min = state.variables[0] - min(state.domain_per_variable[0])
    x0_max = max(state.domain_per_variable[0]) - state.variables[0]
    x1_min = state.variables[1] - min(state.domain_per_variable[1])
    x1_max = max(state.domain_per_variable[1]) - state.variables[1]
    steps = 100
    new_states: List[EggHolder] = list()
    for x_i in range(-steps, steps):
        for y_i in range(-steps, steps):
            new_state = copy.deepcopy(state)
            new_state.variables[0] = new_state.variables[0] + \
                (x_i - steps) * x0_min / (2*steps) + \
                (x_i + steps)*x0_max/(2*steps)
            new_state.variables[1] = new_state.variables[1] + \
                (y_i - steps) * x1_min / (2*steps) + \
                (y_i + 100)*x1_max/(2*steps)
            new_states.append(new_state)
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
