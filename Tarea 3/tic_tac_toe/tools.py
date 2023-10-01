from elapsed_time.tools import print_time
from tic_tac_toe.models import Board


def print_board(board: Board):
    n = len(board.variables)
    print_time()
    print("-" * (n * 4 + 1))
    for i in range(n):
        for j in range(n):
            print(f"| {board.variables[i][j]:1s} ", end="")
        print("|")
        print("-" * (n * 4 + 1))
    print()
