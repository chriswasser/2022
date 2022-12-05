#!/usr/bin/env python3

import fileinput
import heapq

from rich import print
from rich.traceback import install

install(show_locals=True)


def calculate_calories(lines: list[str]) -> list[int]:
    calories = []
    current = 0
    for line in lines:
        if line:
            current += int(line)
        else:
            calories.append(current)
            current = 0
    calories.append(current)
    return calories


def process_part1(lines: list[str]) -> str:
    return str(max(calculate_calories(lines)))


def process_part2(lines: list[str]) -> str:
    return str(sum(heapq.nlargest(3, calculate_calories(lines))))


def test_part1():
    lines = [line.rstrip("\n") for line in fileinput.input("input-testing.txt")]
    solution = process_part1(lines)
    assert solution == "24000"
    print("testing part 1: ✓")


def test_part2():
    lines = [line.rstrip("\n") for line in fileinput.input("input-testing.txt")]
    solution = process_part2(lines)
    assert solution == "45000"
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
