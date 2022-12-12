#!/usr/bin/env python3

from __future__ import annotations

from dataclasses import dataclass
import fileinput
import math
import operator

from rich import print
from rich.traceback import install

install(show_locals=True)


@dataclass
class Monkey:
    monkeys: list[Monkey]
    identifier: int
    items: list[int]
    operation_operator: str
    operation_argument: str
    test_number: int
    next_true: int
    next_false: int
    worry_level_divisor: int
    number_of_inspections: int = 0

    def execute_turn(self):
        for item in self.items:
            worry_level = item
            if self.operation_operator == "*":
                if self.operation_argument == "old":
                    worry_level *= worry_level
                else:
                    worry_level *= int(self.operation_argument)
            if self.operation_operator == "+":
                if self.operation_argument == "old":
                    worry_level += worry_level
                else:
                    worry_level += int(self.operation_argument)

            if self.worry_level_divisor == 1:
                if self.operation_argument != "old":
                    divisor = math.lcm(*(monkey.test_number for monkey in self.monkeys))
                    worry_level %= divisor
            else:
                worry_level //= self.worry_level_divisor

            self.number_of_inspections += 1
            if worry_level % self.test_number == 0:
                self.monkeys[self.next_true].items.append(worry_level)
            else:
                self.monkeys[self.next_false].items.append(worry_level)
        self.items = []


def process_part1(lines: list[str]) -> str:
    monkeys: list[Monkey] = []
    monkey, items, operation, argument, test, true, false = 0, [], "", "", 1, 1, 2
    for line in lines:
        line = line.lstrip()
        if line.startswith("Monkey"):
            monkey = int(line[len("Monkey ") : -1])
        if line.startswith("Starting items"):
            items = list(map(int, line[len("Starting items: ") :].split(", ")))
        if line.startswith("Operation"):
            operation = line[len("Operation: new = old ")]
            argument = line[len("Operation: new = old * ") :]
        if line.startswith("Test"):
            test = int(line[len("Test: divisible by ") :])
        if line.startswith("If true"):
            true = int(line[len("If true: throw to monkey ") :])
        if line.startswith("If false"):
            false = int(line[len("If false: throw to monkey ") :])
        if not line:
            monkeys.append(Monkey(monkeys, monkey, items, operation, argument, test, true, false, 3))
    monkeys.append(Monkey(monkeys, monkey, items, operation, argument, test, true, false, 3))

    for round in range(20):
        for monkey in monkeys:
            monkey.execute_turn()

    monkeys = sorted(monkeys, key=lambda monkey: -monkey.number_of_inspections)
    result = monkeys[0].number_of_inspections * monkeys[1].number_of_inspections

    return str(result)


def process_part2(lines: list[str]) -> str:
    monkeys: list[Monkey] = []
    monkey, items, operation, argument, test, true, false = 0, [], "", "", 1, 1, 2
    for line in lines:
        line = line.lstrip()
        if line.startswith("Monkey"):
            monkey = int(line[len("Monkey ") : -1])
        if line.startswith("Starting items"):
            items = list(map(int, line[len("Starting items: ") :].split(", ")))
        if line.startswith("Operation"):
            operation = line[len("Operation: new = old ")]
            argument = line[len("Operation: new = old * ") :]
        if line.startswith("Test"):
            test = int(line[len("Test: divisible by ") :])
        if line.startswith("If true"):
            true = int(line[len("If true: throw to monkey ") :])
        if line.startswith("If false"):
            false = int(line[len("If false: throw to monkey ") :])
        if not line:
            monkeys.append(Monkey(monkeys, monkey, items, operation, argument, test, true, false, 1))
    monkeys.append(Monkey(monkeys, monkey, items, operation, argument, test, true, false, 1))

    for round in range(10000):
        for monkey in monkeys:
            monkey.execute_turn()

    monkeys = sorted(monkeys, key=lambda monkey: -monkey.number_of_inspections)
    result = monkeys[0].number_of_inspections * monkeys[1].number_of_inspections

    return str(result)


def test_part1():
    lines = [line.rstrip("\n") for line in fileinput.input("input-testing.txt")]
    solution = process_part1(lines)
    assert solution == "10605"
    print("testing part 1: ✓")


def test_part2():
    lines = [line.rstrip("\n") for line in fileinput.input("input-testing.txt")]
    solution = process_part2(lines)
    assert solution == "2713310158"
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
