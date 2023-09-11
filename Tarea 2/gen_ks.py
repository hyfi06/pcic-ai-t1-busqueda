import sys
import random
from typing import List

from algorithms.genetic import genetic
from elapsed_time.decorators import execution_time
from elapsed_time.tools import timer
from ks import ks_read, GenKs, ks_goal


def ks_fitness(state: GenKs) -> float:
    return (-1 if GenKs.capacity < state.get_weight() else 1) * state.get_value()


@execution_time
def main(fileName: str, max_time) -> None:
    GenKs.capacity, GenKs.items = ks_read(fileName)
    num_items = len(GenKs.items)

    GenKs.domains = [
        [0, 1]
        for _ in range(num_items)
    ]

    print(f"W:{GenKs.capacity}, Items: {num_items}")

    initial_population: List[GenKs] = [
        GenKs(values=[1 if j == i else 0 for j in range(0, num_items)])
        for i in range(500)
    ]
    solution = genetic(
        initial_population,
        ks_fitness,
        ks_goal,
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
