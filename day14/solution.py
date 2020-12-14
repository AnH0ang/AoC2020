import regex as re
from typing import List, Dict, Set, Callable, Tuple, Counter, Match
from functools import lru_cache
from collections import Counter
from itertools import combinations, product
from copy import deepcopy
from functools import reduce


def possible_adresses(fluk_adress: str) -> List[str]:
    if "X" in fluk_adress:
        return possible_adresses(fluk_adress.replace("X", "0", 1)) + possible_adresses(fluk_adress.replace("X", "1", 1))
    else:
        return [fluk_adress]


def part1():
    mask: str
    memory: Dict[int, List[str]] = {}
    for line in open("input.txt", "r").read().splitlines():
        if line.startswith("mask"):
            mask = line.split(" ")[2]
        elif line.startswith("mem"):
            r: Match[str] = re.match(r"mem\[(\d+)\] = (\d+)", line)
            adress = int(r.group(1))
            value = "{0:b}".format(int(r.group(2))).rjust(36, "0")
            memory[adress] = [value[i] if mask[i] == "X" else mask[i]
                              for i in range(36)]

    silver = sum(int("".join(v), 2) for v in memory.values())
    print(silver)


def part2():
    mask: str
    memory: Dict[int, int] = {}
    for line in open("input.txt", "r").read().splitlines():
        if line.startswith("mask"):
            mask = line.split(" ")[2]
        elif line.startswith("mem"):
            r: Match[str] = re.match(r"mem\[(\d+)\] = (\d+)", line)
            adress = "{0:b}".format(int(r.group(1))).rjust(36, "0")
            value = int(r.group(2))
            fluk_adress = "".join(
                [mask[i] if mask[i] in "X1" else adress[i] for i in range(36)])
            for adress in possible_adresses(fluk_adress):
                memory[int(adress, 2)] = value

    gold = sum(memory.values())
    print(gold)


def main() -> None:
    part1()
    part2()


if __name__ == "__main__":
    main()
