import copy
import sys
import time

from typing import List, Tuple, Dict
from algorithms.backtracking import State, backtracking


def read_problem(fileName) -> Tuple[int, Dict[int, List[int]]]:
    data: List[str] = list()
    with open(fileName, mode='r') as file:
        data = file.readlines()
    fist_line: List[int] = [int(i) for i in (data.pop(0)).split(' ')]
    [num_vertices, num_edges] = fist_line

    edges_list: List[List[int]] = [
        [int(i) for i in row.split(' ')]
        for row in data
        if row
    ]

    edges_dic: Dict[int, List[int]] = dict()
    for (v1, v2) in edges_list:
        try:
            edges_dic[v1].append(v2)
        except KeyError:
            edges_dic[v1] = [v2]
        try:
            edges_dic[v2].append(v1)
        except KeyError:
            edges_dic[v2] = [v1]

    assert (len(edges_dic) == num_vertices)

    return (num_vertices, edges_dic)


class Gc(State[int]):

    def __init__(self, values: List[int], domain_per_variable: List[List[int]], edges: Dict[int, List[int]]) -> None:
        super().__init__(values, domain_per_variable)
        self.edges = edges

    def num_colors(self) -> int:
        return len(set(self.variables).difference({0}))

    @property
    def is_complete(self) -> bool:
        return min(self.variables) != 0

    @property
    def is_valid(self) -> bool:
        return True


def next_gc(state: Gc) -> List[Gc]:
    idx = state.variable_order()[0]
    new_states: List[Gc] = list()
    new_state = copy.deepcopy(state)
    new_state.variables[idx] = new_state.domain_per_variable[idx].pop(0)
    new_state.domain_per_variable[idx] = []
    for i in state.edges[idx]:
        try:
            new_state.domain_per_variable[i].remove(
                new_state.variables[idx])
        except ValueError:
            pass
    new_states.append(new_state)

    return new_states


def goal_gc(state: Gc) -> bool:
    if state.is_complete:
        print(f"Colores: {state.num_colors()} Coloración: {state}")
        return True
    return False


def main(fileName: str) -> None:
    (num_vertices, edges) = read_problem(fileName)
    initial_state = Gc(
        [0]*num_vertices,
        [list(range(1, num_vertices+1)) for i in range(num_vertices)],
        edges
    )
    solution = backtracking(
        initial_state,
        next_gc,
        goal_gc
    )


if __name__ == "__main__":
    print(time.strftime('%c'))
    fileName: str = sys.argv[1]
    main(fileName)
    print(time.strftime('%c'))
