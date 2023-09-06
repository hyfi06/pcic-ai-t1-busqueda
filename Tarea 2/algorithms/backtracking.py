from typing import TypeAlias, TypeVar, Callable, Generic, Type
from abc import abstractproperty
from pQueue.model import PQueue


T = TypeVar('T')


class State(Generic[T]):
    def __init__(self, values: list[T], domain_per_variable: list[list[T]]) -> None:
        self.variables: list[T] = values
        self.domain_per_variable: list[list[T]] = domain_per_variable

    def variable_order(self) -> list[int]:
        idx_domains: list[tuple[int, list[T]]] = list(
            enumerate(self.domain_per_variable))
        idx_domains.sort(key=lambda enum: len(enum[1]))
        return [
            idx for (idx, domain) in idx_domains
            if len(domain)
        ]

    @abstractproperty
    def is_valid(self) -> bool:
        valid: bool = True

        for idx, value1 in list(enumerate(self.variables))[:-1]:
            if value1 != 0:
                continue
            if len(self.domain_per_variable[idx]) == 0:
                valid = False
                break
        return valid

    def __str__(self) -> str:
        return self.variables.__str__()


U = TypeVar('U', bound=State)
NextFunction: TypeAlias = Callable[[Type[U]], list[Type[U]]]
GoalTest: TypeAlias = Callable[[Type[U]], bool]


def backtracking(
    initial_state: Type[U],
    next_states: NextFunction,
    goal_test: GoalTest
) -> set[str]:
    edge: PQueue[tuple[int, int], Type[U]] = PQueue()
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
            new_states: list[Type[U]] = [
                new_state for new_state in next_states(state)
                if str(new_state) not in visited_states and new_state.is_valid
            ]
            for idx, new_state in enumerate(new_states):
                edge.push((priority[0]-1, idx), new_state)
    return solutions
