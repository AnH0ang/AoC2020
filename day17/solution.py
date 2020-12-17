import regex as re
from collections import defaultdict
from typing import Callable, Dict, Iterable, List, Tuple, Match, Set, DefaultDict
from itertools import product
from copy import deepcopy

# types
Coordinate = Tuple[int, ...]
Field = DefaultDict[Coordinate, int]

# global variables
curr_field: Field
next_field: Field


def update_pos(pos: Coordinate) -> None:
    if curr_field[pos]:
        if sum((curr_field[p] for p in get_neighbors(pos))) not in [3, 4]:
            next_field[pos] = 0
    else:
        if sum((curr_field[p] for p in get_neighbors(pos))) == 3:
            next_field[pos] = 1


def get_neighbors(pos: Coordinate) -> Iterable[Coordinate]:
    return list(product(*[range(p-1, p+2) for p in pos]))


def main() -> None:
    global curr_field, next_field

    for i in [1, 2]:
        curr_field = defaultdict(int)
        next_field = defaultdict(int)

        for x, line in enumerate(open("input.txt").read().splitlines()):
            for y, char in enumerate(line):
                curr_field[(x, y) + (0,) * i] = 0 if char == "." else 1

        for _ in range(6):
            next_field = deepcopy(curr_field)
            for pos in list(curr_field):
                if curr_field[pos]:
                    for p in get_neighbors(pos):
                        update_pos(p)
            curr_field = next_field

        print(sum(curr_field.values()))


if __name__ == "__main__":
    main()
