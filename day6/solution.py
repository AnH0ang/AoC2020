import re
from typing import List, Dict, Set, Callable


def main() -> None:
    with open("input.txt", "r") as f:
        answers: List[List[Set[str]]]
        answers = [[set(answer) for answer in group.split("\n")]
                   for group in f.read().split("\n\n")]

    # solution 1
    print(sum([len(set.union(*group)) for group in answers]))

    # solution 2
    print(sum([len(set.intersection(*group)) for group in answers]))


if __name__ == "__main__":
    main()
