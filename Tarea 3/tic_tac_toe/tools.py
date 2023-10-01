from elapsed_time.tools import print_time
from tic_tac_toe.models import Board


def print_board(board: Board) -> None:
    n = len(board.variables)
    print_time()
    print("-" * (n * 4 + 1))
    for i in range(n):
        for j in range(n):
            print(f"| {board.variables[i][j]:1s} ", end="")
        print("|")
        print("-" * (n * 4 + 1))
    print()


def heuristic(player: str, board: Board) -> float:
    columns = [
        [board.variables[i][j] for i in range(3)]
        for j in range(3)
    ]
    diagonals = [
        [board.variables[i][i] for i in range(3)],
        [board.variables[i][-1-i] for i in range(3)],
    ]

    def x_o_count(p, n):
        return len([
            row
            for row in board.variables + columns + diagonals
            if sum([cell == p for cell in row]) == n and sum([cell == '' for cell in row]) == 3-n
        ])

    player_1 = x_o_count(player, 1)
    player_2 = x_o_count(player, 2)
    opponent_1 = x_o_count('O'if player == 'X' else 'X', 1)
    opponent_2 = x_o_count('O'if player == 'X' else 'X', 2)

    return (3 * player_2 + player_1 - 3*opponent_2 - opponent_1)/6


def probability(player: str, board: Board) -> float:
    num = sum([
        len([cell for cell in row if cell == ''])
        for row in board.variables
    ]) + 1
    return 1/num
