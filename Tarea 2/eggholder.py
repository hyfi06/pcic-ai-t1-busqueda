from algorithms.models import State, Individual
from math import sin, sqrt
from elapsed_time.tools import print_time


class EggHolder(State[float]):
    min_value: float = 0.0

    def get_value(self) -> float:
        x, y = self.variables
        term1: float = -(y+47) * sin(sqrt(abs(y+x/2+47)))
        term2: float = -x * sin(sqrt(abs(x-(y+47))))
        return term1 + term2


def eh_height(state: EggHolder) -> float:
    return -state.get_value()


def eh_goal(state: EggHolder) -> bool:
    if state.min_value > state.get_value():
        state.__class__.min_value = state.get_value()
        eh_print(state)
        return True
    return False


def eh_print(state: EggHolder) -> None:
    print_time()
    print(f"x1:{state.variables[0]} y:{state.variables[1]}")
    print(f"Value: {state.get_value()}", end='\n\n')
