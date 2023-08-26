from typing import TypeAlias, TypeVar, Generic, Optional

T = TypeVar('T', str, int)
AdjacencyItem: TypeAlias = tuple[T, int]
AdjacenciesTable: TypeAlias = dict[T, list[AdjacencyItem]]


class LabeledGraph(Generic[T]):
    adjacencies_table: AdjacenciesTable = dict()

    def __init__(self, adjacencies_table: Optional[AdjacenciesTable]) -> None:
        if adjacencies_table:
            self.adjacencies_table = adjacencies_table

    def add_node(self, node_label: T, adjacencies: list[AdjacencyItem]):
        self.adjacencies_table[node_label] = adjacencies
