import re
from collections import defaultdict
from copy import deepcopy


def get_pos(line: str) -> tuple[int, int]:
    curr_pos: list[int] = [0, 0]
    for direction in re.findall(r"ne|nw|se|sw|e|w", line):
        if direction == "e":
            curr_pos[0] += 1
        elif direction == "w":
            curr_pos[0] += -1
        elif direction == "ne":
            curr_pos[0] += 1
            curr_pos[1] -= 1
        elif direction == "nw":
            curr_pos[1] -= 1
        elif direction == "se":
            curr_pos[1] += 1
        elif direction == "sw":
            curr_pos[0] -= 1
            curr_pos[1] += 1
    return tuple(curr_pos)


def get_neighbors(pos: tuple[int, int]) -> list[tuple[int, int]]:
    neighbors = []
    for diff in [[1, 0], [-1, 0], [1, -1], [0, -1], [0, 1], [-1, 1], [0, 0]]:
        neighbors.append(tuple([x + y for x, y in zip(pos, diff)]))
    return neighbors


def main() -> None:
    tiles: defaultdict[tuple[int, int], int] = defaultdict(int)

    # solution 1
    for line in open("input.txt", "r").read().splitlines():
        tiles[get_pos(line)] ^= 1
    silver = sum(tiles.values())
    print(silver)

    # solution 2
    new_tiles: defaultdict[tuple[int, int], int]
    for _ in range(100):
        new_tiles = deepcopy(tiles)
        for pos in list(tiles):
            for neighbor_pos in get_neighbors(pos):
                if tiles[neighbor_pos]:
                    if (c := sum(tiles[n] for n in get_neighbors(neighbor_pos))) == 1 or c > 3:
                        new_tiles[neighbor_pos] = 0
                else:
                    if sum(tiles[n] for n in get_neighbors(neighbor_pos)) == 2:
                        new_tiles[neighbor_pos] = 1
        new_tiles = defaultdict(int, {k: v for k, v in new_tiles.items() if v})
        tiles = new_tiles
    gold = sum(tiles.values())
    print(gold)


if __name__ == "__main__":
    main()
