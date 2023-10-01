from tic_tac_toe.models import Game
from tic_tac_toe.tools import print_board
from algorithms import minimax


def main():
    game = Game(minimax.agent, minimax.agent)
    print_board(game.board)

    while not game.is_over:
        game.next()
        print_board(game.board)

    print(game.result())


if __name__ == "__main__":
    main()
