import sys
import random

from typing import List

from elapsed_time.decorators import execution_time
from elapsed_time.tools import timer
from algorithms.genetic import genetic
from queens import GenQueens, nq_goal, nq_height, nq_time


@execution_time
def main(n: int):
    GenQueens.domains = [[1, n]for _ in range(n)]
    initial_population: List[GenQueens] = [
        GenQueens(values=random.choices(range(1, n+1), k=n))
        for _ in range(n)
    ]

    solution = genetic(
        initial_population,
        nq_height,
        nq_goal,
        nq_time,
    )
    print(solution)


if __name__ == "__main__":
    n: int = int(sys.argv[1])
    main(n)
