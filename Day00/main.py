#!/usr/bin/env python3

import fileinput

from rich import print
from rich.traceback import install

install(show_locals=True)


def test_task1():
    lines = [line.rstrip() for line in fileinput.input("test")]
    solution = None
    assert solution == None
    print("tests for task 1: ok")


def solve_task1():
    lines = [line.rstrip() for line in fileinput.input("input")]
    solution = None
    print(f"answer to task 1: {solution}")


def test_task2():
    lines = [line.rstrip() for line in fileinput.input("test")]
    solution = None
    assert solution == None
    print("tests for task 2: ok")


def solve_task2():
    lines = [line.rstrip() for line in fileinput.input("input")]
    solution = None
    print(f"answer to task 2: {solution}")


def main():
    test_task1()
    solve_task1()
    test_task2()
    solve_task2()


if __name__ == "__main__":
    main()
