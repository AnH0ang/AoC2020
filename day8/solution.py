import regex as re
from typing import List, Dict, Set, Callable, Tuple
from functools import lru_cache


def calc_terminatation_ptr(first_ptr: int, start_register: int, instructions: List[Tuple[str, int]]):
    command_ptr: int = first_ptr
    register: int = start_register
    visited: List[bool] = [False] * len(instructions)
    end_ptr: int = len(instructions) - 1

    while True:
        if command_ptr == end_ptr:
            return end_ptr, register
        elif visited[command_ptr]:
            return command_ptr, register
        else:
            visited[command_ptr] = True

        operator, argument = instructions[command_ptr]
        if operator == "nop":
            command_ptr = command_ptr + 1
        elif operator == "acc":
            command_ptr += 1
            register +=  argument
        elif operator == "jmp":
            command_ptr += argument


def main() -> None:
    instructions:  List[Tuple[str, int]] = []
    for line in open("input.txt", "r"):
        operator, argument = line.split(" ")
        instructions += [(operator, int(argument))]

    # solution 1
    _, term_reg = calc_terminatation_ptr(0, 0, instructions)
    print(term_reg)

    # solution 2
    command_ptr: int = 0
    register = 0
    end_ptr: int = len(instructions) - 1

    while True:
        operator, argument = instructions[command_ptr]
        if operator == "nop":
            term_ptr, term_reg = calc_terminatation_ptr(
                command_ptr+argument, register, instructions)
            if term_ptr == end_ptr:
                print(term_reg)
                break
            command_ptr += 1
        elif operator == "acc":
            register += argument
            command_ptr += 1
        elif operator == "jmp":
            term_ptr, term_reg = calc_terminatation_ptr(
                command_ptr+1, register, instructions)
            if term_ptr == end_ptr:
                print(term_reg)
                break
            command_ptr += argument


if __name__ == "__main__":
    main()
