import sys
import random
from typing import List

from algorithms.genetic import genetic
from elapsed_time.decorators import execution_time
from elapsed_time.tools import timer
from eggholder import GenEggHolder, eh_fitness, eh_goal


@execution_time
def main(max_time) -> None:
    GenEggHolder.factor = 100.0
    GenEggHolder.domains = [
        [-int(512*GenEggHolder.factor), int(512*GenEggHolder.factor)]
        for _ in range(2)
    ]

    initial_population: List[GenEggHolder] = [
        GenEggHolder(values=[
            random.randint(min(GenEggHolder.domains[0]), max(
                GenEggHolder.domains[0]))
            for _ in range(2)
        ])
        for _ in range(100)
    ]

    solution = genetic(
        initial_population,
        eh_fitness,
        eh_goal,
        timer(max_time),
        False
    )

    print(solution)


if __name__ == "__main__":
    max_time: int = 60*24
    try:
        max_time = int(sys.argv[1])
    except IndexError:
        pass
    main(max_time)
