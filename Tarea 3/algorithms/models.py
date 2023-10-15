from typing import TypeVar, Generic, List
from abc import abstractproperty

T = TypeVar('T')


class State(Generic[T]):
    def __init__(self, values: List[T], domain_per_variable: List[List[T]]) -> None:
        self.variables: List[T] = values
        self.domain_per_variable: List[List[T]] = domain_per_variable

    @abstractproperty
    def is_valid(self) -> bool:
        valid: bool = True

        for idx, value1 in list(enumerate(self.variables)):
            if value1:
                continue
            if len(self.domain_per_variable[idx]) == 0:
                valid = False
                break
        return valid

    @abstractproperty
    def is_terminal(self) -> bool:  # type: ignore
        pass

    def __str__(self) -> str:
        return self.variables.__str__()
