from typing import TypeAlias, TypeVar, Callable, Generic
from abc import abstractproperty
from pQueue.model import PQueue


T = TypeVar('T')


class State(Generic[T]):
    def __init__(self, domain: list[T], values: list[T], domain_per_variable: list[list[T]]) -> None:
        self.domain: list[T] = domain
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
    def is_valid(self) -> bool:  # type: ignore
        pass

    def __str__(self) -> str:
        return self.variables.__str__()


NextFunction: TypeAlias = Callable[[State[T]], list[State[T]]]
GoalTest: TypeAlias = Callable[[State[T]], bool]


def backtracking(
    initial_state: State[T],
    next_states: NextFunction[T],
    goal_test: GoalTest
) -> State | None:
    edge: PQueue[tuple[int, int], State] = PQueue()
    edge.push((0, 0), initial_state)
    visited_states: set[str] = set()
    while len(edge):
        (priority, state) = edge.pop()
        print(f"{priority} - {state}")
        visited_states.add(str(state))
        if goal_test(state):
            return state
        else:
            new_states: list[State] = [
                new_state for new_state in next_states(state)
                if str(new_state) not in visited_states and new_state.is_valid
            ]
            for idx, new_state in enumerate(new_states):
                edge.push((priority[0]-1, idx), new_state)
    return None
