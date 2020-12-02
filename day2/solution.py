import re
from typing import Tuple

def parse_line(line: str) -> Tuple[int]:
    p = re.compile("(\d+)-(\d+) (\w): (\w+)")
    r = re.match(p, line)
    return r.groups()

def word_has_number_of_chars(min_n: int, max_n: int, char: str, word: str) -> bool:
    occurrences = len(re.findall(char, word))
    return (min_n <= occurrences) and (occurrences <= max_n)

def word_has_one_char_at_index(index1: int, index2: int, char: str, word: str) -> bool:
    has_char_at_idx1 = (len(word) >= (index1)) and (word[index1-1] == char)
    has_char_at_idx2 = (len(word) >= (index2)) and (word[index2-1] == char)
    return has_char_at_idx1 != has_char_at_idx2

def main() -> None:
    count_1: int = 0
    count_2: int = 0

    with open("input.txt", "r") as f:
        for line in f:
            nb_1, nb_2, char, password = parse_line(line)
            nb_1 = int(nb_1)
            nb_2 = int(nb_2)

            if word_has_number_of_chars(nb_1, nb_2, char, password):
                count_1 += 1

            if word_has_one_char_at_index(nb_1, nb_2, char, password):
                count_2 += 1

    print(count_1, count_2)

if __name__ == "__main__":
    main()