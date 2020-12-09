import regex as re
from typing import List, Dict, Set, Callable, Tuple
from functools import lru_cache


def is_sum_of_first_n(l: List[int], idx: int, preamble: int = 25) -> bool:
    for i in range(preamble+1):
        for j in range(i):
            if l[idx - i] + l[idx - j] == l[idx]:
                return True
    return False


def solution_1(l: List[int]) -> int:
    for i, n in enumerate(l):
        if i > 25 and (not is_sum_of_first_n(l, i, 25)):
            return n
    return -1


def solution_2(l: List[int], goal: int) -> int:
    beg: int = 0
    end: int = 1
    cur_sum: int = sum(l[beg:end])

    while (cur_sum != goal):
        if cur_sum < goal:
            cur_sum += l[end]
            end += 1
        if cur_sum > goal:
            cur_sum -= l[beg]
            beg += 1

    return min(l[beg:end]) + max(l[beg:end])


def main() -> None:
    numbers: List[int] = [int(n) for n in open(
        "input.txt", "r").read().split("\n")]

    silver: int = solution_1(numbers)
    print(silver)

    gold = solution_2(numbers, silver)
    print(gold)


if __name__ == "__main__":
    main()
