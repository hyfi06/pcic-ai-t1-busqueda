from typing import TypeAlias, Optional

AdjacencyItem: TypeAlias = tuple[str, int]
AdjacenciesTable: TypeAlias = dict[str, list[AdjacencyItem]]


class LabeledGraph:
    def __init__(self, adjacencies_table: Optional[AdjacenciesTable] = None) -> None:
        self.adjacencies_table: AdjacenciesTable = adjacencies_table if adjacencies_table else dict()

    def add_node(self, node_label: str, adjacencies: list[AdjacencyItem]) -> None:
        self.adjacencies_table[node_label] = adjacencies

    def get_border(self, node: str) -> list[AdjacencyItem]:
        return self.adjacencies_table[node]

    def __str__(self) -> str:
        return self.adjacencies_table.__str__()
