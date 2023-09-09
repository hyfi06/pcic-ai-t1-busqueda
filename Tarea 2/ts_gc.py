import copy
import sys
import random

from typing import List
from elapsed_time.decorators import execution_time
from elapsed_time.tools import timer
from algorithms.taboo_search import taboo_search
from graph_c import gc_read, gc_print, Gc


def gc_height(state: Gc) -> int:
    return - state.get_num_conflicts() - state.num_colors()


def gc_neighborhood(state: Gc) -> List[Gc]:
    new_states: List[Gc] = list()
    for idx, color1 in list(enumerate(state.variables))[:-1]:
        for jdx in [i for i in Gc.edges[idx] if i > idx]:
            if color1 == state.variables[jdx]:
                state.variables[jdx] = min(
                    set(range(1, len(Gc.edges)+1)).difference(
                        set([state.variables[j] for j in Gc.edges[jdx]])))

    new_state = copy.deepcopy(state)
    new_states.append(new_state)
    max_color = max(set(state.variables))
    max_color_idx: List[int] = list()
    new_state_half = copy.deepcopy(state)
    for idx, color in list(enumerate(state.variables)):
        new_state_half.variables[idx] = color//2
        if color == max_color and max_color != 1:
            max_color_idx.append(idx)
    new_states.append(new_state_half)

    for color in range(1, max_color//2):
        new_state_menor = copy.deepcopy(state)
        for idx in max_color_idx:
            new_state_menor.variables[idx] = color
        new_states.append(new_state_menor)
    return new_states


def gc_goal(state: Gc) -> bool:
    if state.get_num_conflicts() == 0 and state.num_colors() < Gc.min_colors:
        Gc.min_colors = state.num_colors()
        gc_print(state)
        return True
    return False


@execution_time
def main(fileName: str, max_time) -> None:
    Gc.min_colors, Gc.edges = gc_read(fileName)
    initial_state = Gc(
        [random.randint(1, Gc.min_colors + 1) for _ in range(Gc.min_colors)],
        []
    )
    solution = taboo_search(
        initial_state,
        gc_height,
        gc_neighborhood,
        gc_goal,
        timer(max_time),
        False
    )


if __name__ == "__main__":
    fileName: str = sys.argv[1]
    max_time: int = 60*24
    try:
        max_time = int(sys.argv[2])
    except IndexError:
        pass
    main(fileName, max_time)
