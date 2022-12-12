#!/usr/bin/env python3

import fileinput
import math

import networkx as nx
import numpy as np
from rich import print
from rich.traceback import install

install(show_locals=True)


def process_part1(lines: list[str]) -> str:
    heightmap = np.array([[tree for tree in line] for line in lines], dtype=np.string_)

    graph = nx.DiGraph()

    start: tuple[int, int] = (0, 0)
    end: tuple[int, int] = (0, 0)
    for index in np.ndindex(heightmap.shape):
        graph.add_node(tuple(index))
        if heightmap[*index] == b"S":
            start = tuple(index)
            heightmap[*index] = b"a"
        if heightmap[*index] == b"E":
            end = tuple(index)
            heightmap[*index] = b"z"

    for (x, y) in np.ndindex(heightmap.shape):
        if x - 1 >= 0:
            if ord(heightmap[x - 1, y]) - ord(heightmap[x, y]) >= -1:
                graph.add_edge((x - 1, y), (x, y))
            if ord(heightmap[x, y]) - ord(heightmap[x - 1, y]) >= -1:
                graph.add_edge((x, y), (x - 1, y))

        if y - 1 >= 0:
            if ord(heightmap[x, y - 1]) - ord(heightmap[x, y]) >= -1:
                graph.add_edge((x, y - 1), (x, y))
            if ord(heightmap[x, y]) - ord(heightmap[x, y - 1]) >= -1:
                graph.add_edge((x, y), (x, y - 1))

        if x + 1 < heightmap.shape[0]:
            if ord(heightmap[x + 1, y]) - ord(heightmap[x, y]) >= -1:
                graph.add_edge((x + 1, y), (x, y))
            if ord(heightmap[x, y]) - ord(heightmap[x + 1, y]) >= -1:
                graph.add_edge((x, y), (x + 1, y))

        if y + 1 < heightmap.shape[1]:
            if ord(heightmap[x, y + 1]) - ord(heightmap[x, y]) >= -1:
                graph.add_edge((x, y + 1), (x, y))
            if ord(heightmap[x, y]) - ord(heightmap[x, y + 1]) >= -1:
                graph.add_edge((x, y), (x, y + 1))

    result = nx.shortest_path_length(graph, start, end)
    assert isinstance(result, int)

    return str(result)


def process_part2(lines: list[str]) -> str:
    heightmap = np.array([[tree for tree in line] for line in lines], dtype=np.string_)

    graph = nx.DiGraph()

    end: tuple[int, int] = (0, 0)
    for index in np.ndindex(heightmap.shape):
        graph.add_node(tuple(index))
        if heightmap[*index] == b"S":
            heightmap[*index] = b"a"
        if heightmap[*index] == b"E":
            end = tuple(index)
            heightmap[*index] = b"z"

    for (x, y) in np.ndindex(heightmap.shape):
        if x - 1 >= 0:
            if ord(heightmap[x - 1, y]) - ord(heightmap[x, y]) >= -1:
                graph.add_edge((x - 1, y), (x, y))
            if ord(heightmap[x, y]) - ord(heightmap[x - 1, y]) >= -1:
                graph.add_edge((x, y), (x - 1, y))

        if y - 1 >= 0:
            if ord(heightmap[x, y - 1]) - ord(heightmap[x, y]) >= -1:
                graph.add_edge((x, y - 1), (x, y))
            if ord(heightmap[x, y]) - ord(heightmap[x, y - 1]) >= -1:
                graph.add_edge((x, y), (x, y - 1))

        if x + 1 < heightmap.shape[0]:
            if ord(heightmap[x + 1, y]) - ord(heightmap[x, y]) >= -1:
                graph.add_edge((x + 1, y), (x, y))
            if ord(heightmap[x, y]) - ord(heightmap[x + 1, y]) >= -1:
                graph.add_edge((x, y), (x + 1, y))

        if y + 1 < heightmap.shape[1]:
            if ord(heightmap[x, y + 1]) - ord(heightmap[x, y]) >= -1:
                graph.add_edge((x, y + 1), (x, y))
            if ord(heightmap[x, y]) - ord(heightmap[x, y + 1]) >= -1:
                graph.add_edge((x, y), (x, y + 1))

    result = math.inf
    for index in np.ndindex(heightmap.shape):
        if heightmap[*index] == b"a":
            try:
                length = nx.shortest_path_length(graph, tuple(index), end)
                assert isinstance(length, int)
                result = min(length, result)
            except nx.NetworkXNoPath:
                pass
    return str(result)


def test_part1():
    lines = [line.rstrip("\n") for line in fileinput.input("input-testing.txt")]
    solution = process_part1(lines)
    assert solution == "31"
    print("testing part 1: ✓")


def test_part2():
    lines = [line.rstrip("\n") for line in fileinput.input("input-testing.txt")]
    solution = process_part2(lines)
    assert solution == "29"
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
