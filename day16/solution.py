from matplotlib import collections
import regex as re
from collections import defaultdict
from typing import Callable, Dict, List, Tuple, Match, Set, DefaultDict

name2range: Dict[str, Set[int]] = {}
idx2names: DefaultDict[int, Set[str]] = defaultdict(set)
tickets: List[List[int]] = []
valid_tickets: List[List[int]] = []
name_list: List[str]


def main() -> None:
    rules_block, my_ticket_block, tickets_block = map(
        lambda x: x.split("\n"), open("input.txt", "r").read().split("\n\n"))

    for line in rules_block:
        m: Match[str] = re.match(r"(.+): (\d+)-(\d+) or (\d+)-(\d+)", line)
        name2range[m.group(1)] = {*range(int(m.group(2)), int(m.group(3))+1),
                                  *range(int(m.group(4)), int(m.group(5))+1)}

    # solution 1
    tickets = [[int(x) for x in line.split(",")] for line in tickets_block[1:]]
    silver: int = 0
    for t in tickets:
        is_valid = True
        for nb in t:
            if not any(nb in r for r in name2range.values()):
                silver += nb
                is_valid = False
        if is_valid:
            valid_tickets.append(t)
    print(silver)

    # solution 2
    my_ticket = [int(x) for x in my_ticket_block[1].split(",")]
    valid_tickets.append(my_ticket)

    for idx in range(len(name2range)):
        col_items = {t[idx] for t in valid_tickets}
        for name, nb_range in name2range.items():
            if all(map(lambda x: x in nb_range, col_items)):
                idx2names[idx] |= {name}

    name_list = [""] * len(name2range)
    while idx2names:
        min_idx = sorted(idx2names, key=lambda k: len(idx2names[k]))[0]
        name = idx2names[min_idx].pop()
        name_list[min_idx] = name
        for nbset in idx2names.values():
            nbset.discard(name)
        idx2names.pop(min_idx)

    gold: int = 1
    for idx, name in enumerate(name2range):
        if name.startswith("departure"):
            gold *= my_ticket[idx]
    print(gold)


if __name__ == "__main__":
    main()
