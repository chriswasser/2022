#!/usr/bin/env python3

import fileinput
import math

import numpy as np
from rich import print
from rich.traceback import install

install(show_locals=True)


def process_part1(lines: list[str]) -> str:
    forest = np.array([[int(tree) for tree in line] for line in lines], dtype=np.int64)
    visible = 0
    for (i, j) in np.ndindex(forest.shape):
        tree = forest[i, j]
        visible += np.all(forest[:i, j] < tree) or np.all(forest[i+1:, j] < tree) or np.all(forest[i, :j] < tree) or np.all(forest[i, j+1:] < tree)
    return str(visible)


def process_part2(lines: list[str]) -> str:
    forest = np.array([[int(tree) for tree in line] for line in lines], dtype=np.int64)

    result = 0
    for (i, j) in np.ndindex(forest.shape):
        tree = forest[i, j]

        totals = []

        total = 0
        for a in forest[:i, j][::-1]:
            if a >= tree:
                total += 1
                break
            total += 1
        totals.append(total)

        total = 0
        for a in forest[i+1:, j]:
            if a >= tree:
                total += 1
                break
            total += 1
        totals.append(total)

        total = 0
        for a in forest[i, :j][::-1]:
            if a >= tree:
                total += 1
                break
            total += 1
        totals.append(total)

        total = 0
        for a in forest[i, j+1:]:
            if a >= tree:
                total += 1
                break
            total += 1
        totals.append(total)

        result = max(result, math.prod(totals))
    return str(result)


def test_part1():
    lines = [line.rstrip("\n") for line in fileinput.input("input-testing.txt")]
    solution = process_part1(lines)
    assert solution == "21"
    print("testing part 1: ✓")


def test_part2():
    lines = [line.rstrip("\n") for line in fileinput.input("input-testing.txt")]
    solution = process_part2(lines)
    assert solution == "8"
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
