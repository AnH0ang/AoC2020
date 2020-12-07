import regex as re
from typing import List, Dict, Set, Callable, Tuple
from functools import lru_cache

import networkx as nx
from networkx.classes.digraph import DiGraph


def parse_input() -> DiGraph:
    G = nx.DiGraph()
    for line in open("input.txt", "r"):
        match = re.match(
            r"(\w+ \w+) bags contain (((\d+) (\w+ \w+) bags?((.)|(, )))*|(no other bags.))$", line)
        outer_color = match.group(1)
        content = list(zip(match.captures(4), match.captures(5)))

        G.add_node(outer_color)
        for number_str, color in content:
            G.add_node(color)
            G.add_edge(outer_color, color, weight=int(number_str))

    return G


@lru_cache(10000)
def containing_bags(G: DiGraph, col: str) -> int:
    return_val: int = 1

    neighbor: str
    for neighbor in G.neighbors(col):
        return_val += containing_bags(G, neighbor) * \
            G.get_edge_data(col, neighbor)["weight"]

    return return_val


def main() -> None:
    G: DiGraph = parse_input()

    # solution 1
    print(len(nx.descendants(nx.reverse(G), "shiny gold")))

    # solution 2
    print(containing_bags(G, "shiny gold") - 1)


if __name__ == "__main__":
    main()
