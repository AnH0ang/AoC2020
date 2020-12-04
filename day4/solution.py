import re
from typing import List, Dict, Set, Callable

REQUIRED_FIELDS: Set[str] = set(
    ['byr', 'ecl', 'eyr', 'hcl', 'hgt', 'iyr', 'pid'])


def validate_byr(input: str) -> bool:
    return (1920 <= int(input)) and (int(input) <= 2002)


def validate_iyr(input: str) -> bool:
    return (2010 <= int(input)) and (int(input) <= 2020)


def validate_eyr(input: str) -> bool:
    return (2020 <= int(input)) and (int(input) <= 2030)


def validate_hgt(input: str) -> bool:
    if input.endswith("cm"):
        return (150 <= int(input[:-2])) and (int(input[:-2]) <= 193)
    elif input.endswith("in"):
        return (59 <= int(input[:-2])) and (int(input[:-2]) <= 76)
    else:
        return False


def validate_hcl(input: str) -> bool:
    return bool(re.match(r"^#[a-f0-9]{6}$", input))


def validate_ecl(input: str) -> bool:
    return input in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]


def validate_pid(input: str) -> bool:
    return bool(re.match(r"^[a-f0-9]{9}$", input))


VALIDATORS: Dict[str, Callable[[str], bool]] = {
    "byr": validate_byr,
    "iyr": validate_iyr,
    "eyr": validate_eyr,
    "hgt": validate_hgt,
    "hcl": validate_hcl,
    "ecl": validate_ecl,
    "pid": validate_pid
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
