from tic_tac_toe.models import Game
from tic_tac_toe.tools import print_board, heuristic, probability
from algorithms import expectimax, minimax
from random import random


def main() -> None:
    agent_m = minimax.agent
    agent_e = expectimax.agent(
        3, heuristic, probability
    )
    if random() < 0.5:
        print('X: Minimax vs O: Expectimax')
        game = Game(agent_m, agent_e)
    else:
        print('X: Expectimax vs O: Minimax')
        game = Game(agent_e, agent_m)
    print_board(game.board)

    while not game.is_over:
        game.next()
        print_board(game.board)

    print(game.result())


if __name__ == "__main__":
    main()
