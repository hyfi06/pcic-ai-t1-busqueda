from tic_tac_toe.models import Game
from tic_tac_toe.tools import print_board, heuristic, probability
from algorithms import expectimax


def main():
    game = Game(
        expectimax.agent(
            3, heuristic, probability
        ), expectimax.agent(
            3, heuristic, probability
        ))
    print_board(game.board)

    while not game.is_over:
        game.next()
        print_board(game.board)

    print(game.result())


if __name__ == "__main__":
    main()
