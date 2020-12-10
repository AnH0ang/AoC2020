import regex as re
from typing import List, Dict, Set, Callable, Tuple, Counter
from functools import lru_cache
from collections import Counter

joltages: List[int] = []

@lru_cache(100)
def nb_of_combinations(start: int, goal: int) -> int:
    global joltages

    if start == goal:
        return 1
    else:
        return sum([nb_of_combinations(start+i, goal)
                    for i in range(1, 4)
                    if (start + i) in joltages])


def main() -> None:
    global joltages

    # parse list
    joltages = sorted([int(n) for n in open(
        "input.txt", "r").read().split("\n")])
    joltages.append(joltages[-1] + 3)
    joltages = [0] + joltages

    # solution 1
    joltage_diff: List[int] = [x - y for x,
                               y in zip(joltages[1:], joltages[:-1])]
    diff_counter: Counter[int] = Counter(joltage_diff)
    silver: int = (diff_counter[1] * diff_counter[3])
    print(silver)

    # solution 2
    gold: int = nb_of_combinations(0, joltages[-1])
    print(gold)

if __name__ == "__main__":
    main()