import regex as re
from typing import List, Dict, Set, Callable, Tuple, Counter, Match
from functools import lru_cache
from collections import Counter
from itertools import combinations, product
from copy import deepcopy

import numpy as np
from numpy import ndarray


class Starship1:
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
        3: np.array([0, 1]),
    }
    def __init__(self) -> None:
        self.coordinate: ndarray = np.array([0, 0])
        self.direction: int = 0

    def move_ship(self, cardinal: str, val: int) -> None:
        self.coordinate += self.cardinal2vector[cardinal] * val

    def rotate_ship(self, rotation: str, val: int) -> None:
        sign = 1 if rotation == "R" else -1
        self.direction = (self.direction + sign * val/90) % 4

    def move_foreward(self, val: int) -> None:
        self.coordinate += self.direction2vector[self.direction] * val

    def execute_command(self, action: str, val: int) -> None:
        if action in "ESWN":
            self.move_ship(action, val)
        elif action in "LR":
            self.rotate_ship(action, val)
        elif action == "F":
            self.move_foreward(val)

    @property
    def manhattan_distance(self) -> int:
        return np.sum(np.abs(self.coordinate))

class Starship2:
    cardinal2vector: Dict[str, ndarray] = {
        "E": np.array([1, 0]),
        "S": np.array([0, -1]),
        "W": np.array([-1, 0]),
        "N": np.array([0, 1]),
    }

    def __init__(self) -> None:
        self.coordinate: ndarray = np.array([0, 0])
        self.waypoint: ndarray = np.array([10, 1])

    def move_waypoint(self, s: str, val: int) -> None:
        self.waypoint += self.cardinal2vector[s] * val

    def rotate_waypoint(self, s: str, val: int) -> None:
        for _ in range(int(val/90)):
            if s == "R":
                self.waypoint = np.array([self.waypoint[1], -self.waypoint[0]])
            else:
                self.waypoint = np.array([-self.waypoint[1], self.waypoint[0]])

    def move_foreward(self, val: int) -> None:
        self.coordinate += self.waypoint * val

    def execute_command(self, action: str, val: int) -> None:
        if action in "ESWN":
            self.move_waypoint(action, val)
        elif action in "LR":
            self.rotate_waypoint(action, val)
        elif action == "F":
            self.move_foreward(val)

    @property
    def manhattan_distance(self) -> int:
        return np.sum(np.abs(self.coordinate))


def main() -> None:
    # parse seats
    instructions: List[Tuple[str, int]] = []
    for line in open("input.txt", "r"):
        r: Match[str] = re.match(r"(\w)(\d+)", line)
        instructions.append((r.group(1), int(r.group(2))))

    # solution 1
    ship1 = Starship1()
    for action, val in instructions:
        ship1.execute_command(action, val)
    print(ship1.manhattan_distance)

    # solution 2
    ship2 = Starship2()
    for action, val in instructions:
        ship2.execute_command(action, val)
    print(ship2.manhattan_distance)

if __name__ == "__main__":
    main()