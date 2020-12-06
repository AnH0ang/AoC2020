import functools
from typing import List

def main() -> None:
    tree_map: List[str] = []
    for line in open("input.txt", "r"):
        tree_map.append(line[:-1])

    # solution 1
    tree_counter: int = 0
    for i, line in enumerate(tree_map):
        idx: int = i * 3
        width: int = len(line)
        if line[idx % width] == '#':
            tree_counter += 1
    print(tree_counter)


    # solution 2
    tree_counter_list: List[int] = []
    for dx, dy in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
        tree_counter: int = 0
        for i, line in enumerate(tree_map[::dy]):
            idx: int = dx * i
            width : int = len(line)
            if line[idx % width] == '#':
                tree_counter += 1
        tree_counter_list.append(tree_counter)
    print(functools.reduce((lambda x, y: x * y), tree_counter_list))

if __name__ == "__main__":
    main()
