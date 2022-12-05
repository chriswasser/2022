#!/usr/bin/env python3

import fileinput
from enum import auto, Enum

from rich import print
from rich.traceback import install

install(show_locals=True)


class Selection(Enum):
    ROCK = auto()
    PAPER = auto()
    SCISSORS = auto()


class Result(Enum):
    LOSS = auto()
    DRAW = auto()
    WIN = auto()


def process_part1(lines: list[str]) -> str:
    opponent_map = {
        "A": Selection.ROCK,
        "B": Selection.PAPER,
        "C": Selection.SCISSORS,
    }
    myself_map = {
        "X": Selection.ROCK,
        "Y": Selection.PAPER,
        "Z": Selection.SCISSORS,
    }
    result_map: dict[tuple[Selection, Selection], Result] = {
        (Selection.ROCK, Selection.ROCK): Result.DRAW,
        (Selection.ROCK, Selection.PAPER): Result.WIN,
        (Selection.ROCK, Selection.SCISSORS): Result.LOSS,
        (Selection.PAPER, Selection.ROCK): Result.LOSS,
        (Selection.PAPER, Selection.PAPER): Result.DRAW,
        (Selection.PAPER, Selection.SCISSORS): Result.WIN,
        (Selection.SCISSORS, Selection.ROCK): Result.WIN,
        (Selection.SCISSORS, Selection.PAPER): Result.LOSS,
        (Selection.SCISSORS, Selection.SCISSORS): Result.DRAW,
    }
    selection_score = {
        Selection.ROCK: 1,
        Selection.PAPER: 2,
        Selection.SCISSORS: 3,
    }
    result_score = {
        Result.LOSS: 0,
        Result.DRAW: 3,
        Result.WIN: 6,
    }

    total_score = 0
    for line in lines:
        opponent, myself = line.split(" ")
        total_score += (
            selection_score[myself_map[myself]] + result_score[result_map[opponent_map[opponent], myself_map[myself]]]
        )
    return str(total_score)


def process_part2(lines: list[str]) -> str:
    opponent_map = {
        "A": Selection.ROCK,
        "B": Selection.PAPER,
        "C": Selection.SCISSORS,
    }
    myself_map: dict[tuple[Selection, Result], Selection] = {
        (Selection.ROCK, Result.LOSS): Selection.SCISSORS,
        (Selection.ROCK, Result.DRAW): Selection.ROCK,
        (Selection.ROCK, Result.WIN): Selection.PAPER,
        (Selection.PAPER, Result.LOSS): Selection.ROCK,
        (Selection.PAPER, Result.DRAW): Selection.PAPER,
        (Selection.PAPER, Result.WIN): Selection.SCISSORS,
        (Selection.SCISSORS, Result.LOSS): Selection.PAPER,
        (Selection.SCISSORS, Result.DRAW): Selection.SCISSORS,
        (Selection.SCISSORS, Result.WIN): Selection.ROCK,
    }
    result_map = {
        "X": Result.LOSS,
        "Y": Result.DRAW,
        "Z": Result.WIN,
    }
    selection_score = {
        Selection.ROCK: 1,
        Selection.PAPER: 2,
        Selection.SCISSORS: 3,
    }
    result_score = {
        Result.LOSS: 0,
        Result.DRAW: 3,
        Result.WIN: 6,
    }

    total_score = 0
    for line in lines:
        opponent, result = line.split(" ")
        total_score += (
            selection_score[myself_map[opponent_map[opponent], result_map[result]]] + result_score[result_map[result]]
        )
    return str(total_score)


def test_part1():
    lines = [line.rstrip("\n") for line in fileinput.input("input-testing.txt")]
    solution = process_part1(lines)
    assert solution == "15"
    print("testing part 1: ✓")


def test_part2():
    lines = [line.rstrip("\n") for line in fileinput.input("input-testing.txt")]
    solution = process_part2(lines)
    assert solution == "12"
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
