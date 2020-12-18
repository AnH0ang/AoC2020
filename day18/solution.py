from curses.ascii import isdigit
import operator
from typing import Callable, Dict, Iterable, List, Tuple, Match, Set, DefaultDict

# algorithm for infix notaiton was taken from https://www.geeksforgeeks.org/expression-evaluation/

def evaluate_line(line: str) -> int:
    operators: List[str] = []
    values: List[int] = []

    for c in line.replace(" ", ""):
        if c in "(*+":
            operators.append(c)
        elif c == ")":
            assert operators.pop() == "("
            if operators and (operators[-1] in "+*"):
                eval_operator(values, operators.pop())
        elif c.isdigit():
            values.append(int(c))
            if operators and (operators[-1] != "("):
                eval_operator(values, operators.pop())

    assert len(values) == 1
    return values.pop()


def eval_operator(values: List[int], operator: str) -> None:
    if operator == "*":
        values.append(values.pop() * values.pop())
    elif operator == "+":
        values.append(values.pop() + values.pop())


def op_precedence(operator: str) -> int:
    if operator == "+":
        return 1
    elif operator == "*":
        return 0
    else:
        return -1


def evaluate_infix_line(line: str) -> int:
    operators: List[str] = []
    values: List[int] = []
    op: str

    for c in line.replace(" ", ""):
        if isdigit(c):
            values.append(int(c))
        elif c == "(":
            operators.append(c)
        elif c == ")":
            op = operators.pop()
            while op != "(":
                eval_operator(values, op)
                op = operators.pop()
        elif c in "+*":
            while (operators and (op_precedence(operators[-1]) >= op_precedence(c))):
                eval_operator(values, operators.pop())
            operators.append(c)

    while operators:
        op = operators.pop()
        eval_operator(values, op)

    assert len(values) == 1
    return values.pop()


def main() -> None:
    silver: int = 0
    gold: int = 0
    for line in open("input.txt", "r").read().splitlines():
        silver += evaluate_line(line)
        gold += evaluate_infix_line(line)

    print(silver)
    print(gold)


if __name__ == "__main__":
    main()
