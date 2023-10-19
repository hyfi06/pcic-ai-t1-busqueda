from typing import List


class BayesianNetwork:
    def __init__(self) -> None:
        self.adjacencies_table = dict()

    def add_node(self, node_label: str, adjacencies: list[AdjacencyItem]) -> None:
        self.adjacencies_table[node_label] = adjacencies

    def get_border(self, node: str) -> list[AdjacencyItem]:
        return self.adjacencies_table[node]

    def __str__(self) -> str:
        return self.adjacencies_table.__str__()

    def clear(self) -> None:
        self.adjacencies_table = dict()

    def get_nodes(self) -> set[str]:
        return set(self.adjacencies_table.keys())
