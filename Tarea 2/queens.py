from algorithms.models import State


class nQueens(State[int]):
    def get_num_conflicts(self) -> int:
        conflicts: int = 0
        for idx, value1 in list(enumerate(self.variables))[:-1]:
            for jdx, value2 in list(enumerate(self.variables))[idx+1:]:
                if value1 == value2:
                    conflicts += 1
                if abs(value1 - value2) == abs(idx - jdx):
                    conflicts += 1
        return conflicts
