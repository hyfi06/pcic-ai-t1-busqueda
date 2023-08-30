from typing import Generic, TypeVar, TypeAlias
from pqueue.models import PQueue
from graph.models import LabeledGraph

T = TypeVar('T')

NodeLabel: TypeAlias = str
KpItem: TypeAlias = tuple[int, int]


class CompleteGraph(Generic[T]):
    def __init__(self, data: list[T]) -> None:
        self.data: list[T] = data

    def get_border(self, node: str) -> list[tuple[str, T]]:
        return [
            (str(idx), value)
            for idx, value in enumerate(self.data)
            if str(idx) != node
        ]


def read_problem(fileName) -> tuple[int, list[tuple[int, int]]]:
    data = []
    with open(fileName, mode='r') as file:
        data = file.readlines()
    data = [
        tuple([int(i) for i in row.split(' ')])for row in data
        if row
    ]
    [objects_num, size] = data.pop(0)
    assert (len(data) == objects_num)

    return (size, data)


def heuristic(node: tuple[int, int]) -> float:
    (value, weight) = node
    return float(weight) / value


def main():
    (size, data) = read_problem('./ks_10000_0')
    print(f"Bag size: {size}\n")
    initial_node = '0'
    minimal_h = heuristic(data[0])
    for idx, item in enumerate(data):
        if heuristic(item) < minimal_h and item[1] < size:
            initial_node = str(idx)
            minimal_h = heuristic(item)

    graph: CompleteGraph[KpItem] = CompleteGraph(data)
    initial_item = data[int(initial_node)]
    border = PQueue()
    border.push((0, (initial_node, initial_item[1])))
    tree = LabeledGraph()
    tree.add_node(initial_node, [])
    visit_nodes = set()
    while len(border):
        (priority, (node, pack_weight)) = border.pop()
        print(f"{priority} - {node}:{data[int(node)]}")
        visit_nodes.add(node)
        expanded_border = [
            i for i in graph.get_border(node)
            if i[0] not in visit_nodes and pack_weight + i[1][1] < size
        ]

        if len(expanded_border) == 0:
            break
        else:
            for new_node in expanded_border:
                border.queue_list.clear()
                border.push((
                    heuristic(new_node[1]),
                    (new_node[0], pack_weight+new_node[1][1])
                ))
                tree.add_node(new_node[0], [(node, new_node[1][1])])

    result = [(node, data[int(node)][1])]
    iter_node = node
    while len(tree.get_border(iter_node)):
        [(iter_node, iter_value)] = tree.get_border(iter_node)
        result.insert(0, (iter_node, iter_value))
    total_value = sum([data[int(i[0])][1] for i in result])
    total_weight = sum([i[1] for i in result])
    print(
        f"TotalWeight: {total_weight}, TotalValue: {total_value}, Choses: {'->'.join([i[0] for i in result])}"
    )


if __name__ == "__main__":
    main()
