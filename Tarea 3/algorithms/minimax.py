from typing import Tuple
from tic_tac_toe.models import Board


def agent(player: str, state: Board) -> Board:
    max_value = float('-inf')
    best_state = state.successors(player)[0]
    alpha = float("-inf")
    beta = float("+inf")
    for successor in state.successors(player):
        successor_value = value(
            player=player,
            state=successor,
            is_max=False,
            alpha=alpha,
            beta=beta
        )
        if max_value < successor_value:
            max_value = successor_value
            best_state = successor
    return best_state


def value(player: str, state: Board, is_max: bool, alpha: float, beta: float) -> float:
    v = 0
    if state.is_terminal:
        v = state.utility(player)
    elif is_max:
        v, alpha, beta = max_value(player, state, alpha, beta)
    else:
        v, alpha, beta = min_value(player, state, alpha, beta)
    return v


def max_value(player, state: Board, alpha: float, beta: float) -> Tuple[float, float, float]:
    v = float('-inf')
    for successor in state.successors(player):
        v = max(v, value(
            player,
            successor,
            False,
            alpha,
            beta
        ))
        if v >= beta:
            return (v, alpha, beta)
        alpha = max(alpha, v)
    return (v, alpha, beta)


def min_value(player, state: Board, alpha: float, beta: float) -> Tuple[float, float, float]:
    v = float('+inf')
    for successor in state.successors('O' if player == 'X' else 'X'):
        v = min(v, value(
            player,
            successor,
            True,
            alpha,
            beta
        ))
        if v <= alpha:
            return (v, alpha, beta)
        beta = min(beta, v)
    return (v, alpha, beta)
