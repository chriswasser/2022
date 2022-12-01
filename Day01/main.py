#!/usr/bin/env python3

import fileinput
import heapq


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


def test_task1():
    lines = [
        "1000",
        "2000",
        "3000",
        "",
        "4000",
        "",
        "5000",
        "6000",
        "",
        "7000",
        "8000",
        "9000",
        "",
        "10000",
    ]
    solution = max(calculate_calories(lines))
    assert solution == 24000
    print("tests for task 1: ok")


def solve_task1():
    lines = [line.rstrip() for line in fileinput.input()]
    solution = max(calculate_calories(lines))
    print(f"answer to task 1: {solution}")


def test_task2():
    lines = [
        "1000",
        "2000",
        "3000",
        "",
        "4000",
        "",
        "5000",
        "6000",
        "",
        "7000",
        "8000",
        "9000",
        "",
        "10000",
    ]
    solution = sum(heapq.nlargest(3, calculate_calories(lines)))
    assert solution == 45000
    print("tests for task 2: ok")


def solve_task2():
    lines = [line.rstrip() for line in fileinput.input()]
    solution = sum(heapq.nlargest(3, calculate_calories(lines)))
    print(f"answer to task 2: {solution}")


def main():
    test_task1()
    solve_task1()
    test_task2()
    solve_task2()


if __name__ == "__main__":
    main()
