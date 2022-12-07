#!/usr/bin/env python3

from collections import defaultdict
import fileinput
from pathlib import Path, PosixPath

from rich import print
from rich.traceback import install

install(show_locals=True)


def process_part1(lines: list[str]) -> str:
    paths = defaultdict(list)
    current = Path()
    for line in lines:
        match line.split(" "):
            case ["$", "cd", "/"]:
                current = Path("/")
            case ["$", "ls"]:
                pass
            case ["$", "cd", ".."]:
                current = current.parent
            case ["$", "cd", directory]:
                current /= directory
            case ["dir", directory]:
                paths[current].append(current / directory)
            case [size, file]:
                paths[current].append(int(size))
    
    totals = defaultdict(int)
    for path in sorted(paths.keys(), key=lambda key: -len(str(key))):
        for child in paths[path]:
            if isinstance(child, int):
                totals[path] += child
            if isinstance(child, Path):
                totals[path] += totals[child]
    
    max_size = 100000
    sum_of_small_directories = sum(total for total in totals.values() if total <= max_size)

    return str(sum_of_small_directories)


def process_part2(lines: list[str]) -> str:
    paths = defaultdict(list)
    current = Path()
    for line in lines:
        match line.split(" "):
            case ["$", "cd", "/"]:
                current = Path("/")
            case ["$", "ls"]:
                pass
            case ["$", "cd", ".."]:
                current = current.parent
            case ["$", "cd", directory]:
                current /= directory
            case ["dir", directory]:
                paths[current].append(current / directory)
            case [size, file]:
                paths[current].append(int(size))
    
    totals = defaultdict(int)
    for path in sorted(paths.keys(), key=lambda key: -len(str(key))):
        for child in paths[path]:
            if isinstance(child, int):
                totals[path] += child
            if isinstance(child, Path):
                totals[path] += totals[child]

    total_space = 70000000
    update_space = 30000000
    used_space = totals[Path("/")]
    needed_space = update_space - (total_space - used_space)
    smallest_to_delete_space = next(total for total in sorted(totals.values()) if total >= needed_space)

    return str(smallest_to_delete_space)


def test_part1():
    lines = [line.rstrip("\n") for line in fileinput.input("input-testing.txt")]
    solution = process_part1(lines)
    assert solution == "95437"
    print("testing part 1: ✓")


def test_part2():
    lines = [line.rstrip("\n") for line in fileinput.input("input-testing.txt")]
    solution = process_part2(lines)
    assert solution == "24933642"
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
