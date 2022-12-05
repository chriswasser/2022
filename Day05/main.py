#!/usr/bin/env python3

import fileinput
import string

from rich import print
from rich.traceback import install

install(show_locals=True)


def process_part1(lines: list[str]) -> str:
    num_stacks = len(lines[0]) // 4 + 1

    stacks = [[] for _ in range(num_stacks)]
    for index, stack in enumerate(stacks):
        column = 1 + index * 4
        for line in lines:
            if line[column] in string.digits:
                break
            if line[column] in string.ascii_uppercase:
                stack.append(line[column])
    stacks = [list(reversed(stack)) for stack in stacks]

    for line in lines:
        if not line.startswith("move"):
            continue
        _, num_letters, _, from_stack, _, to_stack = line.split(" ")
        for _ in range(int(num_letters)):
            stacks[int(to_stack) - 1].append(stacks[int(from_stack) - 1].pop())

    result = ""
    for stack in stacks:
        if stack:
            result += stack.pop()
        else:
            result += ""
    return result


def process_part2(lines: list[str]) -> str:
    num_stacks = len(lines[0]) // 4 + 1

    stacks = [[] for _ in range(num_stacks)]
    for index, stack in enumerate(stacks):
        column = 1 + index * 4
        for line in lines:
            if line[column] in string.digits:
                break
            if line[column] in string.ascii_uppercase:
                stack.append(line[column])
    stacks = [list(reversed(stack)) for stack in stacks]

    for line in lines:
        if not line.startswith("move"):
            continue
        _, num_letters, _, from_stack, _, to_stack = line.split(" ")
        to_move = reversed([stacks[int(from_stack) - 1].pop() for _ in range(int(num_letters))])
        stacks[int(to_stack) - 1].extend(to_move)

    result = ""
    for stack in stacks:
        if stack:
            result += stack.pop()
        else:
            result += ""
    return result


def test_part1():
    lines = [line.rstrip("\n") for line in fileinput.input("input-testing.txt")]
    solution = process_part1(lines)
    assert solution == "CMZ"
    print("testing part 1: ✓")


def test_part2():
    lines = [line.rstrip("\n") for line in fileinput.input("input-testing.txt")]
    solution = process_part2(lines)
    assert solution == "MCD"
    print("testing part 2: ✓")


def solve_part1():
    lines = [line.rstrip("\n") for line in fileinput.input("input-solving.txt")]
    solution = process_part1(lines)
    print(f"solving part 1: {solution}")


def solve_part2():
    lines = [line.rstrip("\n") for line in fileinput.input("input-solving.txt")]
    solution = process_part2(lines)
    print(f"solving part 2: {solution}")


def main():
    test_part1()
    solve_part1()
    test_part2()
    solve_part2()


if __name__ == "__main__":
    main()
