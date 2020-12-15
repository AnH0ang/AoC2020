import regex as re
from typing import List, Dict, Set, Callable, Tuple, Counter, Match
from functools import lru_cache
from collections import Counter
from itertools import combinations, product
from copy import deepcopy
from functools import reduce


def main() -> None:
    # read in number list
    start_nb: List[int] = [int(i) for i in open(
        "input.txt", "r").read().split(",")]

    # init values
    turn: int = 1
    current_nb: int
    previous_nb: int = start_nb[0]
    nb2prevturn: Dict[int, int] = {}

    # iteration step
    while turn < 2020:
        if turn < len(start_nb):
            current_nb = start_nb[turn]
        elif previous_nb in nb2prevturn:
            current_nb = turn - nb2prevturn[previous_nb]
        else:
            current_nb = 0

        nb2prevturn[previous_nb] = turn
        previous_nb = current_nb
        turn += 1

    print(current_nb)


if __name__ == "__main__":
    main()
