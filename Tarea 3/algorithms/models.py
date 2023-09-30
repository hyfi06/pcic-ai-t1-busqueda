from typing import TypeVar, Generic, List
from abc import abstractproperty

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
            if value1:
                continue
            if len(self.domain_per_variable[idx]) == 0:
                valid = False
                break
        return valid

    def __str__(self) -> str:
        return self.variables.__str__()
