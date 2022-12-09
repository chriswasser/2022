#!/usr/bin/env python3

import fileinput

import numpy as np
from rich import print
from rich.traceback import install

install(show_locals=True)

import numpy.typing as npt


def is_disconnected(head: npt.NDArray[np.int64], tail: npt.NDArray[np.int64]) -> bool:
    return np.linalg.norm(head - tail) > np.sqrt(2)


def process_part1(lines: list[str]) -> str:
    deltas = {
        "R": np.array([0, 1], dtype=np.int64),
        "L": np.array([0, -1], dtype=np.int64),
        "U": np.array([1, 0], dtype=np.int64),
        "D": np.array([-1, 0], dtype=np.int64),
    }

    head_position = np.array([0, 0], dtype=np.int64)
    head_positions = [head_position.copy()]
    for line in lines:
        direction, steps = line.split(" ")

        delta = deltas[direction]
        for _ in range(int(steps)):
            head_position += delta
            head_positions.append(head_position.copy())

    tail_position = np.array([0, 0], dtype=np.int64)
    tail_positions = [tail_position.copy()]
    for head_position in head_positions:
        if is_disconnected(head_position, tail_position):
            tail_position += np.clip(head_position - tail_position, -1, 1)
        tail_positions.append(tail_position.copy())

    return str(len(set(tuple(tail_position) for tail_position in tail_positions)))


def process_part2(lines: list[str]) -> str:
    deltas = {
        "R": np.array([0, 1], dtype=np.int64),
        "L": np.array([0, -1], dtype=np.int64),
        "U": np.array([1, 0], dtype=np.int64),
        "D": np.array([-1, 0], dtype=np.int64),
    }

    head_position = np.array([0, 0], dtype=np.int64)
    head_positions = [head_position.copy()]
    for line in lines:
        direction, steps = line.split(" ")

        delta = deltas[direction]
        for _ in range(int(steps)):
            head_position += delta
            head_positions.append(head_position.copy())

    knots = 9
    tail_positions: list[npt.NDArray[np.int64]] = []
    for _ in range(knots):
        tail_position = np.array([0, 0], dtype=np.int64)
        tail_positions = [tail_position.copy()]
        for head_position in head_positions:
            if is_disconnected(head_position, tail_position):
                tail_position += np.clip(head_position - tail_position, -1, 1)
            tail_positions.append(tail_position.copy())
        head_positions = tail_positions

    return str(len(set(tuple(tail_position) for tail_position in tail_positions)))


def test_part1():
    lines = [line.rstrip("\n") for line in fileinput.input("input-testing.txt")]
    solution = process_part1(lines)
    assert solution == "88"
    print("testing part 1: ✓")


def test_part2():
    lines = [line.rstrip("\n") for line in fileinput.input("input-testing.txt")]
    solution = process_part2(lines)
    assert solution == "36"
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
