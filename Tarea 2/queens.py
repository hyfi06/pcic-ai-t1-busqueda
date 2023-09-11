from algorithms.models import State, Individual


class nQueens(State[int]):
    def get_num_conflicts(self) -> int:
        conflicts: int = 0
        for idx, value1 in list(enumerate(self.variables))[:-1]:
            for jdx, value2 in list(enumerate(self.variables))[idx+1:]:
                if value1 == value2:
                    conflicts += 1
                if abs(value1 - value2) == abs(idx - jdx):
                    conflicts += 1
            if value1 > len(self.variables):
                conflicts += 1
        if self.variables[-1] > len(self.variables):
            conflicts += 1
        return conflicts


class GenQueens (nQueens, Individual):
    pass


def nq_goal(state: nQueens) -> bool:
    return state.get_num_conflicts() == 0


def nq_time() -> bool:
    return True

def nq_height(state: nQueens) -> int:
    return -state.get_num_conflicts()
