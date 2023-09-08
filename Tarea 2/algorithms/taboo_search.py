from typing import TypeVar, Callable, Generic, List, Optional, Set
from abc import abstractproperty
from pQueue.model import PQueue


T = TypeVar('T')


class State(Generic[T]):
    def __init__(self, values: List[T], domain_per_variable: List[List[T]]) -> None:
        self.variables: List[T] = values
        self.domain_per_variable: List[List[T]] = domain_per_variable

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

    def neighborhood(self):
        pass

    def __str__(self) -> str:
        return self.variables.__str__()


U = TypeVar('U', bound=State)


def taboo_search(
    initial_state: U,
    next_state: Callable[[U, Set[str]], U],
    goal_test: Callable[[U], bool],
    time: Callable[[], bool]
):
    edge: PQueue[tuple[int, int], U] = PQueue()
    taboo_list: Set[str] = set()
    solutions: set[str] = set()
    while time():
        pass
