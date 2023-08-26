from typing import TypeAlias, Optional

AdjacencyItem: TypeAlias = tuple[str, int]
AdjacenciesTable: TypeAlias = dict[str, list[AdjacencyItem]]


class LabeledGraph:
    adjacencies_table: AdjacenciesTable = dict()

    def __init__(self, adjacencies_table: Optional[AdjacenciesTable] = None) -> None:
        if adjacencies_table:
            self.adjacencies_table = adjacencies_table

    def add_node(self, node_label: str, adjacencies: list[AdjacencyItem]):
        self.adjacencies_table[node_label] = adjacencies

    def __str__(self) -> str:
        return self.adjacencies_table.__str__()
