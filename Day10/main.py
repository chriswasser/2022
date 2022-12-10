#!/usr/bin/env python3

import fileinput

from rich import print
from rich.traceback import install

install(show_locals=True)


def process_part1(lines: list[str]) -> str:
    history = []
    register = 1
    for line in lines:
        match line.split(" "):
            case ["noop"]:
                history.append(register)
            case ["addx", number]:
                history.append(register)
                history.append(register)
                register += int(number)
    history.append(register)

    start, step = 20, 40
    score = 0
    for index, register in enumerate(history[start - 1 :: step]):
        score += (start + step * index) * register
    return str(score)


def process_part2(lines: list[str]) -> str:
    history = []
    register = 1
    for line in lines:
        match line.split(" "):
            case ["noop"]:
                history.append(register)
            case ["addx", number]:
                history.append(register)
                history.append(register)
                register += int(number)
    history.append(register)

    height, width = 6, 40
    result = ""
    for row in range(height):
        for column in range(width):
            register = history[row * width + column]
            result += "#" if register <= column + 1 and column + 1 <= register + 2 else "."
        result += "\n"
    return result[:-1]


def test_part1():
    lines = [line.rstrip("\n") for line in fileinput.input("input-testing.txt")]
    solution = process_part1(lines)
    assert solution == "13140"
    print("testing part 1: ✓")


def test_part2():
    lines = [line.rstrip("\n") for line in fileinput.input("input-testing.txt")]
    solution = process_part2(lines)
    assert (
        solution
        == """##..##..##..##..##..##..##..##..##..##..
###...###...###...###...###...###...###.
####....####....####....####....####....
#####.....#####.....#####.....#####.....
######......######......######......####
#######.......#######.......#######....."""
    )
    print("testing part 2: ✓")


def solve_part1():
    lines = [line.rstrip("\n") for line in fileinput.input("input-solving.txt")]
    solution = process_part1(lines)
    print(f"solving part 1: {solution}")


def solve_part2():
    lines = [line.rstrip("\n") for line in fileinput.input("input-solving.txt")]
    solution = process_part2(lines)
    print(f"solving part 2:\n{solution}")


def main():
    test_part1()
    solve_part1()
    test_part2()
    solve_part2()


if __name__ == "__main__":
    main()
