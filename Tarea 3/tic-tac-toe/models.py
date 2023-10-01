from typing import List
from algorithms.models import State


class Board(State[List[str]]):

    def utility(self, player) -> bool:
        if all(
            all(len(domain) == 0 for domain in row)
            for row in self.domain_per_variable
        ):
            return None

        if any(
            all(
                data == player for data in row
            ) for row in self.variables
        ):
            return 1
        if any(
            all(
                row[i] == 'X' for row in self.variables
            ) for i in range(len(self.variables))
        ):
            return 1
        if all(
            row[i][i]
            for i, row in enumerate(self.variables)
        ) or all(
            row[i][-1-i]
            for i, row in enumerate(self.variables)
        ):
            return True
    raise False


def print_board(board: Board):
    for row in board.variables:
        print(" | ".join(row))
        print("-"*9)
