import re
from typing import List, Dict, Set, Callable

REQUIRED_FIELDS: Set[str] = set(
    ['byr', 'ecl', 'eyr', 'hcl', 'hgt', 'iyr', 'pid'])


def validate_hgt(input: str) -> bool:
    if input.endswith("cm"):
        return (150 <= int(input[:-2])) and (int(input[:-2]) <= 193)
    elif input.endswith("in"):
        return (59 <= int(input[:-2])) and (int(input[:-2]) <= 76)
    else:
        return False


VALIDATORS: Dict[str, Callable[[str], bool]] = {
    "byr": lambda input: (1920 <= int(input)) and (int(input) <= 2002),
    "iyr": lambda input: (2010 <= int(input)) and (int(input) <= 2020),
    "eyr": lambda input: (2020 <= int(input)) and (int(input) <= 2030),
    "hgt": validate_hgt,
    "hcl": lambda input: bool(re.match(r"^#[a-f0-9]{6}$", input)),
    "ecl": lambda input: input in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"],
    "pid": lambda input: bool(re.match(r"^[a-f0-9]{9}$", input))
}


def main() -> None:
    # Parse Passports
    with open("input.txt", "r") as f:
        passport_list: List[Dict[str, str]]
        passport_list = [dict(field.split(":") for field in batch.split())
                         for batch in f.read().split("\n\n")]

    # Task 1: Passports with all required fields
    validate_passports: List[Dict[str, str]]
    validate_passports = [passport
                          for passport in passport_list
                          if REQUIRED_FIELDS <= set(passport.keys())]
    print(len(validate_passports))

    # Task 2: Passport with correct fields
    correct_passports: List[Dict[str, str]]
    correct_passports = [passport
                         for passport in validate_passports
                         if all([VALIDATORS[arg](passport[arg]) for arg in REQUIRED_FIELDS])]
    print(len(correct_passports))


if __name__ == "__main__":
    main()
