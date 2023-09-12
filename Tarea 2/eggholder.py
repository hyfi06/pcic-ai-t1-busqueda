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

    def __str__(self) -> str:
        return f"x1:{self.variables[0]} x2:{self.variables[1]}"


class GenEggHolder(Individual):
    min_value: float = 0
    factor: float = 100.0

    def get_value(self) -> float:
        x1, x2 = self.variables
        x = x1/self.factor
        y = x2/self.factor
        term1: float = -(y+47) * sin(sqrt(abs(y+x/2+47)))
        term2: float = -x * sin(sqrt(abs(x-(y+47))))
        return term1 + term2

    def __str__(self) -> str:
        return f"x1:{self.variables[0]/self.factor} x2:{self.variables[1]/self.factor}"


def eh_height(state: EggHolder) -> float:
    return -state.get_value()


def eh_goal(state: EggHolder|GenEggHolder) -> bool:
    if state.min_value > state.get_value():
        state.__class__.min_value = state.get_value()
        eh_print(state)
        return True
    return False


def eh_print(state: EggHolder|GenEggHolder) -> None:
    print_time()
    print(f"{state}")
    print(f"Value: {state.get_value()}", end='\n\n')


def eh_fitness(state: GenEggHolder) -> float:
    return -state.get_value()
