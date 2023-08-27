from search.main import Strategy
from pqueue.models import PQueue
from graph.models import LabeledGraph


def dfs_strategy(
    node: str,
    node_priority: int,
    border: PQueue[tuple[str, int]],
    visited_nodes: set[str],
    graph: LabeledGraph,
) -> None:
    new_border = [
        item for item in graph.get_border(node)
        if item[0] not in visited_nodes
    ]
    for item in new_border:
        border.push((item, node_priority-1))


def bfs_strategy(
    node: str,
    node_priority: int,
    border: PQueue[tuple[str, int]],
    visited_nodes: set[str],
    graph: LabeledGraph,
) -> None:
    new_border = [
        item for item in graph.get_border(node)
        if item[0] not in visited_nodes
    ]
    for item in new_border:
        border.push((item, node_priority+1))


def ucs_strategy(
    node: str,
    node_priority: int,
    border: PQueue[tuple[str, int]],
    visited_nodes: set[str],
    graph: LabeledGraph,
) -> None:
    new_border = [
        item for item in graph.get_border(node)
        if item[0] not in visited_nodes
    ]
    for item in new_border:
        border.push((item, item[1]))


def greedy_strategy(heuristic) -> Strategy:
    def strategy(
        node: str,
        node_priority: int,
        border: PQueue[tuple[str, int]],
        visited_nodes: set[str],
        graph: LabeledGraph,
    ) -> None:
        new_border = [
            item for item in graph.get_border(node)
            if item[0] not in visited_nodes
        ]
        for item in new_border:
            border.push((item, heuristic(item[0])))
    return strategy


def a_star_strategy(heuristic) -> Strategy:
    def strategy(
        node: str,
        node_priority: int,
        border: PQueue[tuple[str, int]],
        visited_nodes: set[str],
        graph: LabeledGraph,
    ) -> None:
        new_border = [
            item for item in graph.get_border(node)
            if item[0] not in visited_nodes
        ]
        for item in new_border:
            border.push(
                (item, item[1] + heuristic(item[0]))
            )
    return strategy


def iterative_strategy(initial_node: str) -> Strategy:
    depth: int = 0

    def strategy(
        node: str,
        node_priority: int,
        border: PQueue[tuple[str, int]],
        visited_nodes: set[str],
        graph: LabeledGraph,
    ) -> None:
        nonlocal depth
        nonlocal initial_node
        new_border = [
            item for item in graph.get_border(node)
            if item[0] not in visited_nodes
        ]
        if depth < node_priority:
            for item in new_border:
                border.push((item, node_priority-1))
        elif len(border) == 0:
            depth -= 1
            border.push(((initial_node, 0), 0))
            visited_nodes.clear()
    return strategy
