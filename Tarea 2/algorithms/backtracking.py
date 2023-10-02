from typing import TypeVar, Callable, List, Optional
from pQueue.model import PQueue
from algorithms.models import State


U = TypeVar('U', bound=State)


def backtracking(
    initial_state: U,
    next_states: Callable[[U], List[U]],
    goal_test: Callable[[U], bool],
    fist_solution: Optional[bool] = True
) -> set[str]:
    edge: PQueue[tuple[int, int], U] = PQueue()
    edge.push((0, 0), initial_state)
    visited_states: set[str] = set()
    solutions: set[str] = set()
    while len(edge):
        (priority, state) = edge.pop()
        # print(f"{priority} - {state}")
        visited_states.add(str(state))
        if goal_test(state):
            solutions.add(str(state))
            if fist_solution:
                break
        else:
            new_states: list[U] = [
                new_state for new_state in next_states(state)
                if str(new_state) not in visited_states and new_state.is_valid
            ]
            for idx, new_state in enumerate(new_states):
                edge.push((priority[0]-1, idx), new_state)
    return solutions
