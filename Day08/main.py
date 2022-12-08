#!/usr/bin/env python3

import fileinput
import math
from typing import Callable, Generator, Iterable, TypeVar

import numpy as np
from rich import print
from rich.traceback import install

install(show_locals=True)

T = TypeVar("T")


def process_part1(lines: list[str]) -> str:
    forest = np.array([[int(tree) for tree in line] for line in lines], dtype=np.int8)

    visible = 0
    for (i, j) in np.ndindex(forest.shape):
        tree = forest[i, j]
        visible += (
            False
            or np.all(forest[:i, j] < tree)
            or np.all(forest[i + 1 :, j] < tree)
            or np.all(forest[i, :j] < tree)
            or np.all(forest[i, j + 1 :] < tree)
        )
    return str(visible)


def until(predicate: Callable[[T], bool], iterable: Iterable[T]) -> Generator[T, None, None]:
    for item in iterable:
        yield item
        if predicate(item):
            break


# alternative implementation of count_until which composes generators instead of performing a manual loop
def count_until2(predicate: Callable[[T], bool], iterable: Iterable[T]) -> int:
    iterator = iter(iterable)
    iterator = until(predicate, iterator)
    iterator = map(lambda _: 1, iterator)
    return sum(iterator)


def count_until(predicate: Callable[[T], bool], iterable: Iterable[T]) -> int:
    count = 0
    for item in iterable:
        count += 1
        if predicate(item):
            break
    return count


def process_part2(lines: list[str]) -> str:
    forest = np.array([[int(tree) for tree in line] for line in lines], dtype=np.int8)

    result = 0
    for (i, j) in np.ndindex(forest.shape):
        tree = forest[i, j]

        totals = [
            count_until(lambda other: other >= tree, forest[:i, j][::-1]),
            count_until(lambda other: other >= tree, forest[i + 1 :, j]),
            count_until(lambda other: other >= tree, forest[i, :j][::-1]),
            count_until(lambda other: other >= tree, forest[i, j + 1 :]),
        ]

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
