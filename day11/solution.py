import regex as re
from typing import List, Dict, Set, Callable, Tuple, Counter
from functools import lru_cache
from collections import Counter
from itertools import combinations, product
from copy import deepcopy


def get_adjacent_seats(row: int, col: int, seats: List[List[str]]) -> List[str]:
    neighbors: List[str] = []
    for (i, j) in [(row-1, col-1), (row-1, col), (row-1, col+1),
                   (row, col-1), (row, col+1),
                   (row+1, col-1), (row+1, col), (row+1, col+1)]:
        if (i >= 0 and i < len(seats) and j >= 0 and j < len(seats[0])):
            neighbors.append(seats[i][j])

    return neighbors


def get_next_visible_seat(row: int, col: int, drow: int, dcol: int, seats: List[List[str]]) -> List[str]:
    row += drow
    col += dcol
    while (row >= 0 and row < len(seats) and col >= 0 and col < len(seats[0])):
        if seats[row][col] != ".":
            return [seats[row][col]]
        row += drow
        col += dcol
    return []


def get_visible_seats(row: int, col: int, seats: List[List[str]]) -> List[str]:
    neighbors: List[str] = []
    for (i, j) in [(-1, -1), (-1, 0), (-1, +1),
                   (0, -1), (0, +1),
                   (+1, -1), (+1, 0), (+1, +1)]:
        neighbors += get_next_visible_seat(row, col, i, j, seats)
    return neighbors


def print_seats(seats: List[List[str]]) -> None:
    for row in seats:
        print("".join(row))
    print("")


def count_occupied(seats: List[List[str]]) -> int:
    return sum([row.count("#") for row in seats])


def simulate_one_round_silver(seats: List[List[str]]) -> List[List[str]]:
    next_state: List[List[str]] = deepcopy(seats)
    for (i, j) in product(range(len(seats)), range(len(seats[0]))):
        if (seats[i][j] == "L") and (get_adjacent_seats(i, j, seats).count("#") == 0):
            next_state[i][j] = "#"
        elif (seats[i][j] == "#") and (get_adjacent_seats(i, j, seats).count("#") >= 4):
            next_state[i][j] = "L"
    return next_state


def simulate_one_round_gold(seats: List[List[str]]) -> List[List[str]]:
    next_state: List[List[str]] = deepcopy(seats)
    for (i, j) in product(range(len(seats)), range(len(seats[0]))):
        if (seats[i][j] == "L") and (get_visible_seats(i, j, seats).count("#") == 0):
            next_state[i][j] = "#"
        elif (seats[i][j] == "#") and (get_visible_seats(i, j, seats).count("#") >= 5):
            next_state[i][j] = "L"
    return next_state


def simulate_till_equilibrium(seats: List[List[str]],
                              transition_fkt: Callable[[
                                  List[List[str]]], List[List[str]]]
                              ) -> List[List[str]]:
    current_seats = deepcopy(seats)
    while 1:
        next_seats = transition_fkt(current_seats)
        if current_seats == next_seats:
            break
        current_seats = next_seats
    return current_seats


def main() -> None:
    # parse seats
    seats: List[List[str]]
    seats = [list(line) for line in open("input.txt", "r").read().split("\n")]

    # solution 1
    end_seats = simulate_till_equilibrium(seats, simulate_one_round_silver)
    print(count_occupied(end_seats))

    # solution 2
    end_seats = simulate_till_equilibrium(seats, simulate_one_round_gold)
    print(count_occupied(end_seats))


if __name__ == "__main__":
    main()
