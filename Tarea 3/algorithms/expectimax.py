from typing import Callable
from tic_tac_toe.models import Board


def agent(
    depth,
    heuristic: Callable[[str, Board], float],
    probability: Callable[[str, Board], float]
) -> Callable[[str, Board], Board]:
    def expectimax(player: str, state: Board) -> Board:
        max_value = float('-inf')
        best_state = state.successors(player)[0]
        for successor in state.successors(player):
            successor_value = value(
                player=player,
                state=successor,
                is_max=False,
                depth=depth - 1,
                heuristic=heuristic,
                probability=probability
            )
            if max_value < successor_value:
                max_value = successor_value
                best_state = successor
        return best_state
    return expectimax


def value(
    player: str,
    state: Board,
    is_max: bool,
    depth: int,
    heuristic: Callable[[str, Board], float],
    probability: Callable[[str, Board], float]
) -> float:
    if state.is_terminal:
        return state.utility(player)
    if depth == 0:
        return heuristic(player, state)
    if is_max:
        return max_value(player, state, depth, heuristic, probability)
    else:
        return exp_value(player, state, depth, heuristic, probability)


def max_value(
    player,
    state: Board,
    depth: int,
    heuristic: Callable[[str, Board], float],
    probability: Callable[[str, Board], float]
) -> float:
    v = float('-inf')
    for successor in state.successors(player):
        v = max(v, value(
            player,
            successor,
            False,
            depth-1,
            heuristic,
            probability
        ))
    return v


def exp_value(
    player: str,
    state: Board,
    depth: int,
    heuristic: Callable[[str, Board], float],
    probability: Callable[[str, Board], float]
) -> float:
    v = 0
    for successor in state.successors('O' if player == 'X' else 'X'):
        p = probability(player, state)
        v += p * value(
            player,
            successor,
            True,
            depth-1,
            heuristic,
            probability
        )
    return v
