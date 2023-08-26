from graph.read import read_labeled_graph

file_name = "./Rumania.graph"


def main():
    graph = read_labeled_graph(file_name)
    print(graph)


if __name__ == "__main__":
    main()
