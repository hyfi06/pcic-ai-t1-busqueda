from typing import List, Optional
from algorithms.models import State
import copy


class Board(State[List[str]]):
    def __init__(
        self,
        values: Optional[List[List[str]]] = None,
    ) -> None:
        if values is None:
            values = [
                ['' for _ in range(3)]
                for _ in range(3)
            ]
        domain_per_variable = [
            [
                ['X', 'O'] if values[i][j] == '' else []
                for j in range(3)
            ]
            for i in range(3)
        ]
        self._successors = None
        super().__init__(values, domain_per_variable)

    @property
    def is_terminal(self) -> bool:
        return is_terminal(self)

    def successors(self, player: str) -> List['Board']:
        if not self._successors:
            self._successors = []
            for i in range(3):
                for j in range(3):
                    if len(self.domain_per_variable[i][j]) != 0:
                        new_values = copy.deepcopy(self.variables)
                        new_values[i][j] = player
                        self._successors.append(self.__class__(new_values))

        return self._successors

    def utility(self, player: str) -> float:
        win = winner(self)
        if win == 'Tie':
            return 0
        elif win == f"Win {player}":
            return 1
        else:
            return -1

    # def __lt__(self, other: 'Board'):
    #     return str(self) > str(other)


class Game():
    def __init__(self, agent_x, agent_o) -> None:
        self.agent_x = agent_x
        self.agent_o = agent_o
        self.board = Board()
        self.next_agent = 'X'

    @property
    def is_over(self) -> bool:
        return self.board.is_terminal

    def next(self) -> None:
        if self.next_agent == 'X':
            self.board = self.agent_x('X', self.board)
            self.next_agent = 'O'
        else:
            self.board = self.agent_o('O', self.board)
            self.next_agent = 'X'

    def result(self) -> str:
        return winner(self.board)


def is_terminal(board: Board) -> bool:
    if all(
        board.variables[i][j] != ''
        for j in range(3)
        for i in range(3)
    ):
        return True

    if any(
        len([cell for cell in row if cell == 'X']) == 3 or len(
            [cell for cell in row if cell == 'O']) == 3
        for row in board.variables
    ):
        return True

    columns = [
        [board.variables[i][j] for i in range(3)]
        for j in range(3)
    ]

    if any(
        len([cell for cell in column if cell == 'X']) == 3 or len(
            [cell for cell in column if cell == 'O']) == 3
        for column in columns
    ):
        return True

    diagonals = [
        [board.variables[i][i] for i in range(3)],
        [board.variables[i][-1-i] for i in range(3)],
    ]

    if any(
        len([cell for cell in diagonal if cell == 'X']) == 3 or len(
            [cell for cell in diagonal if cell == 'O']) == 3
        for diagonal in diagonals
    ):
        return True

    return False


def winner(board: Board) -> str:
    columns = [
        [board.variables[i][j] for i in range(3)]
        for j in range(3)
    ]
    diagonals = [
        [board.variables[i][i] for i in range(3)],
        [board.variables[i][-1-i] for i in range(3)],
    ]
    if any(
        len([cell for cell in row if cell == 'X']) == 3
        for row in board.variables
    ) or any(
        len([cell for cell in column if cell == 'X']) == 3
        for column in columns
    ) or any(
        len([cell for cell in diagonal if cell == 'X']) == 3
        for diagonal in diagonals
    ):
        return 'Win X'
    elif any(
        len([cell for cell in row if cell == 'O']) == 3
        for row in board.variables
    ) or any(
        len([cell for cell in column if cell == 'O']) == 3
        for column in columns
    ) or any(
        len([cell for cell in diagonal if cell == 'O']) == 3
        for diagonal in diagonals
    ):
        return 'Win O'
    else:
        return 'Tie'
