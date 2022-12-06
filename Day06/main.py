#!/usr/bin/env python3

import fileinput

from rich import print
from rich.traceback import install

install(show_locals=True)


def process_part1(lines: list[str]) -> str:
    stream = lines[0]
    for index in range(len(stream) - 4):
        if len(set(stream[index : index + 4])) == 4:
            return str(index + 4)
    return ""


def process_part2(lines: list[str]) -> str:
    stream = lines[0]
    for index in range(len(stream) - 14):
        if len(set(stream[index : index + 14])) == 14:
            return str(index + 14)
    return ""


def test_part1():
    lines = [line.rstrip("\n") for line in fileinput.input("input-testing.txt")]
    solution = process_part1(lines)
    assert solution == "10"
    print("testing part 1: ✓")


def test_part2():
    lines = [line.rstrip("\n") for line in fileinput.input("input-testing.txt")]
    solution = process_part2(lines)
    assert solution == "29"
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
