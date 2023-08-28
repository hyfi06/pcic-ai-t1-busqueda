from typing import Callable, TypeAlias
from search.main import Strategy
from pqueue.models import PQueue
from graph.models import LabeledGraph

Heuristic: TypeAlias = Callable[[str], int]


def dfs_strategy(
    node: str,
    parent_priority: int,
    border: PQueue[tuple[str, int]],
    new_border: list[tuple[str, int]],
    tree: LabeledGraph,
) -> None:
    for item in new_border:
        if item[0] in tree.get_nodes():
            continue
        border.push((parent_priority - 1, item))
        tree.add_node(
            item[0],
            [(node, item[1])]
        )


def bfs_strategy(
    node: str,
    parent_priority: int,
    border: PQueue[tuple[str, int]],
    new_border: list[tuple[str, int]],
    tree: LabeledGraph,
) -> None:
    for item in new_border:
        if item[0] in tree.get_nodes():
            continue
        border.push((parent_priority + 1, item))
        tree.add_node(
            item[0],
            [(node, item[1])]
        )


def iterative_strategy(
    initial_node: str,
    graph: LabeledGraph
) -> Strategy:
    depth: int = 0

    def strategy(
        node: str,
        parent_priority: int,
        border: PQueue[tuple[str, int]],
        new_border: list[tuple[str, int]],
        tree: LabeledGraph,
    ) -> None:
        nonlocal depth
        nonlocal initial_node

        if depth < parent_priority:
            for item in new_border:
                if item[0] in tree.get_nodes():
                    continue
                tree.add_node(
                    item[0],
                    [(node, item[1])]
                )
                border.push((parent_priority - 1, item))

        if len(border) == 0 and len(
            graph.get_nodes().difference(tree.get_nodes())
        ):
            depth -= 1
            border.push((0, (initial_node, 0)))
            tree.clear()
            tree.add_node(initial_node, [])
    return strategy


def ucs_strategy(
    node: str,
    parent_priority: int,
    border: PQueue[tuple[str, int]],
    new_border: list[tuple[str, int]],
    tree: LabeledGraph,
) -> None:
    for item in new_border:
        cost = parent_priority + item[1]
        if item[0] not in tree.get_nodes():
            tree.add_node(
                item[0],
                [(node, item[1])]
            )
            border.push((cost, item))
        elif item[0] in {i[0]for i in border.get_items()}:
            idx = 0
            for i in range(len(border.queue_list)):
                if border.queue_list[i][1][0] == item[0]:
                    idx = i
                    break
            if cost < border.queue_list[idx][0]:
                border.queue_list[idx] = (cost, item)
                tree.add_node(
                    item[0],
                    [(node, item[1])]
                )


def greedy_strategy(heuristic: Heuristic) -> Strategy:
    def strategy(
        node: str,
        parent_priority: int,
        border: PQueue[tuple[str, int]],
        new_border: list[tuple[str, int]],
        tree: LabeledGraph,
    ) -> None:
        for item in new_border:
            if item[0] in tree.get_nodes():
                continue
            border.push((
                heuristic(item[0]),
                item
            ))
            tree.add_node(
                item[0],
                [(node, item[1])]
            )
    return strategy


def a_star_strategy(heuristic: Heuristic) -> Strategy:
    def strategy(
        node: str,
        parent_priority: int,
        border: PQueue[tuple[str, int]],
        new_border: list[tuple[str, int]],
        tree: LabeledGraph,
    ) -> None:
        for item in new_border:
            cost = item[1] + heuristic(item[0])
            if item[0] not in tree.get_nodes():
                tree.add_node(
                    item[0],
                    [(node, item[1])]
                )
                border.push((
                    cost,
                    item
                ))
            elif item[0] in {i[0]for i in border.get_items()}:
                idx = 0
                for i in range(len(border.queue_list)):
                    if border.queue_list[i][1][0] == item[0]:
                        idx = i
                        break
                if cost < border.queue_list[idx][0]:
                    border.queue_list[idx] = (
                        cost,
                        item
                    )
                    tree.add_node(
                        item[0],
                        [(node, item[1])]
                    )
    return strategy
