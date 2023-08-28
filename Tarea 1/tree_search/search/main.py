from typing import Callable, TypeAlias
from pqueue.models import PQueue
from graph.models import LabeledGraph

GoalFunction: TypeAlias = Callable[[str], bool]
NodeLabel: TypeAlias = str
EdgeWeight: TypeAlias = int
Strategy: TypeAlias = Callable[[
    int,
    PQueue[tuple[str, int]],
    list[tuple[str, int]],
    LabeledGraph
], None]


def tree_search(
    strategy: Strategy,
    graph: LabeledGraph,
    initial_node: str,
    goal_test: GoalFunction
):
    border: PQueue[tuple[NodeLabel, EdgeWeight]] = PQueue()
    border.push((0, (initial_node, 0)))
    tree: LabeledGraph = LabeledGraph()
    tree.add_node(initial_node, [])
    while len(border):
        (priority, (node, _)) = border.pop()
        print(f"{node}")
        if goal_test(node):
            result: list[tuple[NodeLabel, EdgeWeight]] = [(node, 0)]
            iter_node = node
            while len(tree.get_border(iter_node)):
                [(iter_node, iter_weight)] = tree.get_border(iter_node)
                result.insert(0, (iter_node, iter_weight))
            print(tree)
            return result
        else:
            expanded_border = [
                item for item in graph.get_border(node)
                if item[0] not in tree.get_nodes()
            ]
            cost: int = tree.get_border(node)[0][1] if len(
                tree.get_border(node)) else 0

            for item in expanded_border:
                tree.add_node(
                    item[0],
                    [(node, cost + item[1])]
                )
            strategy(
                priority,
                border,
                expanded_border,
                tree
            )
    return []
