#!/usr/bin/env python3

import fileinput

from rich import print
from rich.traceback import install

install(show_locals=True)


def process_part1(lines: list[str]) -> str:
    total = 0
    for line in lines:
        first, second = line.split(",")
        first_start, first_end = first.split("-")
        second_start, second_end = second.split("-")
        first_range = set(list(range(int(first_start), int(first_end) + 1)))
        second_range = set(list(range(int(second_start), int(second_end) + 1)))
        total += first_range.issuperset(second_range) or second_range.issuperset(first_range)
    return str(total)


def process_part2(lines: list[str]) -> str:
    total = 0
    for line in lines:
        first, second = line.split(",")
        first_start, first_end = first.split("-")
        second_start, second_end = second.split("-")
        first_range = set(list(range(int(first_start), int(first_end) + 1)))
        second_range = set(list(range(int(second_start), int(second_end) + 1)))
        if first_range & second_range:
            total += 1
    return str(total)


def test_part1():
    lines = [line.rstrip() for line in fileinput.input("input-testing.txt")]
    solution = process_part1(lines)
    assert solution == "2"
    print("testing part 1: ✓")


def test_part2():
    lines = [line.rstrip() for line in fileinput.input("input-testing.txt")]
    solution = process_part2(lines)
    assert solution == "4"
    print("testing part 2: ✓")


def solve_part1():
    lines = [line.rstrip() for line in fileinput.input("input-solving.txt")]
    solution = process_part1(lines)
    print(f"solving part 1: {solution}")


def solve_part2():
    lines = [line.rstrip() for line in fileinput.input("input-solving.txt")]
    solution = process_part2(lines)
    print(f"solving part 2: {solution}")


def main():
    test_part1()
    solve_part1()
    test_part2()
    solve_part2()


if __name__ == "__main__":
    main()
