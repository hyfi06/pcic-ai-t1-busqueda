from typing import TypeVar, Callable, Generic, List, Type
from abc import abstractproperty
from pQueue.model import PQueue

T = TypeVar('T')


class State(Generic[T]):
    def __init__(self, values: List[T], domain_per_variable: List[List[T]]) -> None:
        self.variables: List[T] = values
        self.domain_per_variable: List[List[T]] = domain_per_variable

    def variable_order(self) -> List[int]:
        idx_domains: List[tuple[int, List[T]]] = list(
            enumerate(self.domain_per_variable))
        idx_domains.sort(key=lambda enum: len(enum[1]))
        return [
            idx for (idx, domain) in idx_domains
            if len(domain)
        ]

    @abstractproperty
    def is_valid(self) -> bool:
        valid: bool = True

        for idx, value1 in list(enumerate(self.variables)):
            if value1 != 0:
                continue
            if len(self.domain_per_variable[idx]) == 0:
                valid = False
                break
        return valid

    def __str__(self) -> str:
        return self.variables.__str__()


U = TypeVar('U', bound=State)


def backtracking(
    initial_state: U,
    next_states: Callable[[U], List[U]],
    goal_test: Callable[[U], bool]
) -> set[str]:
    edge: PQueue[tuple[int, int], U] = PQueue()
    edge.push((0, 0), initial_state)
    visited_states: set[str] = set()
    solutions: set[str] = set()
    while len(edge):
        (priority, state) = edge.pop()
        # print(f"{priority} - {state}: {state.domain_per_variable}")
        visited_states.add(str(state))
        if goal_test(state):
            solutions.add(str(state))
            break  # fist solution
        else:
            new_states: list[U] = [
                new_state for new_state in next_states(state)
                if str(new_state) not in visited_states and new_state.is_valid
            ]
            for idx, new_state in enumerate(new_states):
                edge.push((priority[0]-1, idx), new_state)
    return solutions
