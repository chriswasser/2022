#!/usr/bin/env python3

import fileinput


def test_task1():
    lines = [line.rstrip() for line in fileinput.input()]
    assert True
    print("tests for task 1: ok")


def solve_task1():
    lines = [line.rstrip() for line in fileinput.input()]

    calories = []
    current = 0
    for line in lines:
        if line:
            current += int(line)
        else:
            calories.append(current)
            current = 0
    calories.append(current)

    solution = max(calories)
    print(f"answer to task 1: {solution}")


def test_task2():
    lines = [line.rstrip() for line in fileinput.input()]
    assert True
    print("tests for task 2: ok")


def solve_task2():
    lines = [line.rstrip() for line in fileinput.input()]
    calories = []
    current = 0
    for line in lines:
        if line:
            current += int(line)
        else:
            calories.append(current)
            current = 0
    calories.append(current)

    calories.sort()

    solution = sum(calories[-3:])
    print(f"answer to task 2: {solution}")


def main():
    test_task1()
    solve_task1()
    test_task2()
    solve_task2()


if __name__ == "__main__":
    main()
