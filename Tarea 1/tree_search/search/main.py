__all__ = ['tree_search']

from typing import Callable, TypeAlias
from pqueue.models import PQueue
from graph.models import LabeledGraph

GoalFunction: TypeAlias = Callable[[str], bool]
Strategy: TypeAlias = Callable[[
    str, int, PQueue[tuple[str, int]],
    set[str], LabeledGraph
], None]


def tree_search(
    strategy: Strategy,
    graph: LabeledGraph,
    initial_node: str,
    goal_test: GoalFunction
):
    border: PQueue[tuple[str, int]] = PQueue()
    border.push(((initial_node, 0), 0))
    tree: LabeledGraph = LabeledGraph()
    visited_nodes: set[str] = set()
    prev_node: str = ''
    while len(border):
        ((curr_node, weight), priority) = border.pop()
        tree.add_node(
            curr_node,
            [(prev_node, weight)] if prev_node else []
        )
        visited_nodes.add(curr_node)
        if goal_test(curr_node):
            result: list[tuple[str, int]] = [(curr_node, 0)]
            iter_node = curr_node
            while len(tree.get_border(iter_node)):
                [(iter_node, iter_weight)] = tree.get_border(iter_node)
                result.insert(0, (iter_node, iter_weight))

            return result
        else:
            prev_node = curr_node
            strategy(
                curr_node,
                priority,
                border,
                visited_nodes,
                graph,
            )
    return None
