import re
from typing import List, Dict, Set, Callable

def main() -> None:
    # Parse Passports
    boarding_ids: List[int]  = []
    boarding_code: str
    for boarding_code in open("input.txt", "r"):
        binary_code: str = boarding_code[:10].translate(str.maketrans("FBLR", "0101"))
        boarding_ids.append(int(binary_code, 2))

    # solution 1
    print(max(boarding_ids))

    # solution 2
    min_id: int = (min(boarding_ids) | 0b111) + 1
    max_id: int = max(boarding_ids) | 0b000
    diff_set: Set[int] = set(range(min_id, max_id)) - set(boarding_ids)
    print(diff_set.pop())

if __name__ == "__main__":
    main()
