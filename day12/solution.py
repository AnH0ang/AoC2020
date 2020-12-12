import regex as re
from typing import List, Dict, Set, Callable, Tuple, Counter, Match
from functools import lru_cache
from collections import Counter
from itertools import combinations, product
from copy import deepcopy

import numpy as np
from numpy import ndarray


class Starship1:
    coordinate: ndarray = np.array([0, 0])
    direction: int = 0
    cardinal2vector: Dict[str, ndarray] = {
        "E": np.array([1, 0]),
        "S": np.array([0, -1]),
        "W": np.array([-1, 0]),
        "N": np.array([0, 1]),
    }
    direction2vector: Dict[int, ndarray] = {
        0: np.array([1, 0]),
        1: np.array([0, -1]),
        2: np.array([-1, 0]),
        3: np.array([0, 1])
    }

    def move_direction(self, s: str, val: int) -> None:
        self.coordinate += self.cardinal2vector[s] * val

    def rotate_ship(self, s: str, val: int) -> None:
        sign = 1 if s == "R" else -1
        self.direction = (self.direction + sign * (val / 90)) % 4

    def move_foreward(self, val: int) -> None:
        self.coordinate += self.direction2vector[self.direction] * val

    def execute_command(self, s: str, val: int) -> None:
        if s in "ESWN":
            self.move_direction(s, val)
        elif s in "LR":
            self.rotate_ship(s, val)
        elif s == "F":
            self.move_foreward(val)

    @property
    def manhattan_distance(self) -> int:
        return np.sum(np.abs(self.coordinate))

class Starship2(Starship1):
    pass

def main() -> None:
    # parse seats
    instructions: List[Tuple[str, int]] = []
    for line in open("input.txt", "r"):
        r: Match[str] = re.match(r"(\w)(\d+)", line)
        instructions.append((r.group(1), int(r.group(2))))

    ship1 = Starship()
    for action, val in instructions:
        ship1.execute_command(action, val)

    print(ship1.manhattan_distance)



if __name__ == "__main__":
    main()
