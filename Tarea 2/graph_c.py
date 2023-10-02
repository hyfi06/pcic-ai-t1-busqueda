from typing import List, Tuple, Dict
from algorithms.models import State, Individual
from elapsed_time.tools import print_time


def gc_read(fileName) -> Tuple[int, Dict[int, List[int]]]:
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

    assert len(edges_list) == num_edges

    edges_dic: Dict[int, List[int]] = dict()
    for v1, v2 in edges_list:
        try:
            edges_dic[v1].append(v2)
        except KeyError:
            edges_dic[v1] = [v2]
        try:
            edges_dic[v2].append(v1)
        except KeyError:
            edges_dic[v2] = [v1]

    assert len(edges_dic) == num_vertices

    return num_vertices, edges_dic


class Gc(State[int]):
    edges: Dict[int, List[int]] = dict()
    min_colors: int = 0

    def num_colors(self) -> int:
        return len(set(self.variables).difference({0}))

    @property
    def is_complete(self) -> bool:
        return min(self.variables) != 0

    @property
    def is_valid(self) -> bool:
        return True

    def get_num_conflicts(self) -> int:
        conflicts: int = 0
        for idx, color1 in list(enumerate(self.variables))[:-1]:
            for jdx in [i for i in self.edges[idx] if i > idx]:
                if color1 == self.variables[jdx]:
                    conflicts += 1
        return conflicts


class GenGc(Gc, Individual):
    pass


def gc_print(state: Gc):
    print_time()
    print(f"Colors: {state.num_colors()}")
    print(f"Coloration:")
    print(state, end='\n\n')


def gc_height(state: Gc) -> int:
    return - state.get_num_conflicts() - state.num_colors()


def gc_goal(state: Gc) -> bool:
    if state.get_num_conflicts() == 0 and state.num_colors() < state.min_colors:
        state.__class__.min_colors = state.num_colors()
        gc_print(state)
        return True
    return False
