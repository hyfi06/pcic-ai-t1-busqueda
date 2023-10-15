from tic_tac_toe.models import Game
from tic_tac_toe.tools import print_board, heuristic, probability
from algorithms import expectimax


def main() -> None:
    agent_e = expectimax.agent(
        3, heuristic, probability
    )
    game = Game(agent_e, agent_e)
    print_board(game.board)

    while not game.is_over:
        game.next()
        print_board(game.board)

    print(game.result())


if __name__ == "__main__":
    main()
