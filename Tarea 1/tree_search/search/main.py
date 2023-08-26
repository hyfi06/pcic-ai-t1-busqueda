__all__ = ['tree_search']

from typing import TypeVar
from pqueue.models import PQueue
from graph.models import LabeledGraph

T = TypeVar('T')


def tree_search(strategy, graph: LabeledGraph, initial_node: str, goal_test):
    border = PQueue()
    border.push((initial_node, 0))
    visited_nodes = set()
    while len(border):
        graph.set_pointer(border.pop()[0])
        visited_nodes.add(graph.get_pointer())
        if goal_test(graph.get_pointer()):
            return graph.get_pointer()
        else:
            strategy(
                visited_nodes,
                border,
                graph.get_border(graph.get_pointer())
            )

    return None
