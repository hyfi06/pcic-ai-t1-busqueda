__all__ = ['tree_search']

from typing import TypeVar
from pqueue.models import PQueue, Strategy
from graph.models import LabeledGraph

T = TypeVar('T')


def tree_search(strategy: Strategy, graph: LabeledGraph, initial_node: str, goal_test):
    graph.set_pointer(initial_node)
    border = PQueue(strategy)
