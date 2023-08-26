from graph.models import LabeledGraph


def read_labeled_graph(file_name: str) -> LabeledGraph:
    data = list()
    graph: LabeledGraph = LabeledGraph()
    with open(file=file_name, mode='r', encoding='utf8') as file:
        data = file.readlines()
    if len(data):
        for row in data:
            if not row:
                continue
            [label, *adjacencies] = row.split(';')
            adjacencies = [
                (item.split(',')[0], int(item.split(',')[1]))
                for item in adjacencies
            ]
            graph.add_node(label, adjacencies)
    return graph
