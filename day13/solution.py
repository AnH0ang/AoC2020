from typing import List, Dict, Set, Callable, Tuple, Counter, Match
from functools import lru_cache
from collections import Counter
from itertools import combinations, product
from copy import deepcopy
from functools import reduce

# Code for Chinese remainder theorem was taken from  https://rosettacode.org/wiki/Chinese_remainder_theorem

def chinese_remainder(n: List[int], a: List[int]) -> int:
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod


def mul_inv(a: int, b: int) -> int:
    b0 = b
    x0, x1 = 0, 1
    if b == 1:
        return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += b0
    return x1


def main() -> None:
    with open("input.txt", "r") as f:
        timestamp: int = int(f.readline())
        bus_ids: List[str] = f.readline().split(",")

    # solution 1
    waiting_times: List[Tuple[int, int]]
    waiting_times = [(int(id) - timestamp % int(id), int(id))
                     for id in bus_ids
                     if id != "x"]
    min_wait, min_idx = min(waiting_times)
    print(min_wait * min_idx)

    # solution 2
    remainder: List[Tuple[int, int]]
    remainder = [(int(id), int(id) - i)
                 for (i, id) in enumerate(bus_ids)
                 if id != "x"]
    print(chinese_remainder(*zip(*remainder)))


if __name__ == "__main__":
    main()
