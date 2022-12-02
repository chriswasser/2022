#!/usr/bin/env python3

import fileinput
from enum import auto, Enum


class Selection(Enum):
    ROCK = auto()
    PAPER = auto()
    SCISSORS = auto()


class Result(Enum):
    LOSS = auto()
    DRAW = auto()
    WIN = auto()


def score_game1(lines: list[str]) -> int:
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
    return total_score


def score_game2(lines: list[str]) -> int:
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
    return total_score


def test_task1():
    lines = [line.rstrip() for line in fileinput.input("test")]
    solution = score_game1(lines)
    assert solution == 15
    print("tests for task 1: ok")


def solve_task1():
    lines = [line.rstrip() for line in fileinput.input("input")]
    solution = score_game1(lines)
    print(f"answer to task 1: {solution}")


def test_task2():
    lines = [line.rstrip() for line in fileinput.input("test")]
    solution = score_game2(lines)
    assert solution == 12
    print("tests for task 2: ok")


def solve_task2():
    lines = [line.rstrip() for line in fileinput.input("input")]
    solution = score_game2(lines)
    print(f"answer to task 2: {solution}")


def main():
    test_task1()
    solve_task1()
    test_task2()
    solve_task2()


if __name__ == "__main__":
    main()
