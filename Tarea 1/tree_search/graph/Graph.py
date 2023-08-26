from typing import NewType, TypeVar, Generic

T = TypeVar('T')
AdjacencyItem = NewType("AdjacencyList", tuple[T, int])
AdjacencyTable = NewType("AdjacencyTable", dict[T, list[AdjacencyItem]])


class Graph(Generic[T]):
    adjacency_table: AdjacencyTable = dict()

    def __init__(self) -> None:
        pass
