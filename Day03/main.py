#!/usr/bin/env python3

import fileinput
from itertools import zip_longest
import string

from rich import print
from rich.traceback import install

install(show_locals=True)


# taken from: https://docs.python.org/3/library/itertools.html#itertools-recipes
def grouper(iterable, n, *, incomplete="fill", fillvalue=None):
    "Collect data into non-overlapping fixed-length chunks or blocks"
    # grouper('ABCDEFG', 3, fillvalue='x') --> ABC DEF Gxx
    # grouper('ABCDEFG', 3, incomplete='strict') --> ABC DEF ValueError
    # grouper('ABCDEFG', 3, incomplete='ignore') --> ABC DEF
    args = [iter(iterable)] * n
    if incomplete == "fill":
        return zip_longest(*args, fillvalue=fillvalue)
    if incomplete == "strict":
        return zip(*args, strict=True)
    if incomplete == "ignore":
        return zip(*args)
    else:
        raise ValueError("Expected fill, strict, or ignore")


def score_character(character: str) -> int:
    assert len(character) == 1

    if character in string.ascii_lowercase:
        return ord(character) - ord("a") + 1
    if character in string.ascii_uppercase:
        return ord(character) - ord("A") + 27

    raise ValueError(f"cannot score invalid character '{character}'")


def process_part1(lines: list[str]) -> str:
    total = 0
    for rucksack in lines:
        middle = len(rucksack) // 2
        first, second = rucksack[:middle], rucksack[middle:]
        common = set(first) & set(second)
        total += score_character(common.pop())
    return str(total)


def process_part2(lines: list[str]) -> str:
    total = 0
    for group in grouper(lines, 3):
        rucksacks = [set(rucksack) for rucksack in group]
        common = set.intersection(*rucksacks)
        total += score_character(common.pop())
    return str(total)


def test_part1():
    lines = [line.rstrip("\n") for line in fileinput.input("input-testing.txt")]
    solution = process_part1(lines)
    assert solution == "157"
    print("testing part 1: ✓")


def test_part2():
    lines = [line.rstrip("\n") for line in fileinput.input("input-testing.txt")]
    solution = process_part2(lines)
    assert solution == "70"
    print("testing part 2: ✓")


def solve_part1():
    lines = [line.rstrip("\n") for line in fileinput.input("input-testing.txt")]
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
