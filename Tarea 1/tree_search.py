from graph.read import read_labeled_graph
from search import tree_search, strategies
from search.algorithms import Strategy


file_name = "./Rumania.txt"


def bucharest_heuristic(node: str) -> int:
    distance_to_bucharest: dict[str, int] = {
        'Arad': 366,
        'Bucharest': 0,
        'Craiova': 160,
        'Dobreta': 242,
        'Eforie': 161,
        'Fagaras': 178,
        'Giurgiu': 77,
        'Hirsova': 151,
        'Iasi': 226,
        'Lugoj': 244,
        'Mehadia': 241,
        'Neamt': 234,
        'Oradea': 280,
        'Pitesti': 98,
        'Rimnicu Vilcea': 193,
        'Sibiu': 253,
        'Timisoara': 329,
        'Urziceni': 80,
        'Vaslui': 199,
        'Zerind': 374,
    }
    return distance_to_bucharest[node]


def main():
    graph = read_labeled_graph(file_name)
    initial_node = 'Arad'
    def goal_test(node): return node == 'Bucharest'

    strategies_map: dict[str, Strategy] = {
        'dfs': strategies.dfs_strategy,
        'bfs': strategies.bfs_strategy,
        'iterative': strategies.iterative_strategy(initial_node, graph),
        'ucs': strategies.ucs_strategy,
        'greedy': strategies.greedy_strategy(bucharest_heuristic),
        'A*': strategies.a_star_strategy(bucharest_heuristic)
    }

    for (name, strategy) in strategies_map.items():
        print(f'---{name}---')
        result = tree_search(
            strategy=strategy,
            graph=graph,
            initial_node=initial_node,
            goal_test=goal_test
        )
        print(result)
        if len(result):
            print(
                f"Cost {sum([i[1] for i in result])}:{'->'.join([i[0] for i in result])}"
            )
        else:
            print("Fail")
        print("\n")


if __name__ == "__main__":
    main()
