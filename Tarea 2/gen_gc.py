import sys
import random

from elapsed_time.decorators import execution_time
from elapsed_time.tools import timer
from algorithms.genetic import genetic
from graph_c import gc_read, GenGc, gc_height, gc_goal


@execution_time
def main(fileName: str, max_time) -> None:
    GenGc.min_colors, GenGc.edges = gc_read(fileName)
    GenGc.domains = [
        [1, GenGc.min_colors]
        for _ in range(GenGc.min_colors)
    ]
    initial_population: list[GenGc] = [
        GenGc(values=[
            random.randint(1, GenGc.min_colors + 1)
            for _ in range(GenGc.min_colors)
        ])
        for _ in range(300)
    ]
    solution = genetic(
        initial_population,
        gc_height,
        gc_goal,
        timer(max_time),
    )
    print(solution)


if __name__ == "__main__":
    fileName: str = sys.argv[1]
    max_time: int = 60*24
    try:
        max_time = int(sys.argv[2])
    except IndexError:
        pass
    main(fileName, max_time)
