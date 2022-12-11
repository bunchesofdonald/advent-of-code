import functools
import operator
from dataclasses import dataclass
from typing import Callable, Union


@dataclass
class Operation:
    operator: Callable[[int, int], int]
    number: Union[int, str]


@dataclass
class Test:
    divisor: int
    if_true: int
    if_false: int


class Monkey:
    def __init__(
        self, items: list[int], operation: Operation, test: Test, reduced_worry: bool
    ):
        self.items: list[int] = items
        self.operation: Operation = operation
        self.test: Test = test
        self.reduced_worry = reduced_worry
        self.lcm = 1
        self.inspected_count = 0

    def throw(self) -> list[tuple[int, int]]:
        thrown_items = []

        for item in self.items:
            worry_level = self.calculate_worry_level(item)
            if worry_level % self.test.divisor == 0:
                monkey = self.test.if_true
            else:
                monkey = self.test.if_false

            thrown_items.append((monkey, worry_level))
            self.inspected_count += 1

        self.items = []

        return thrown_items

    def catch(self, item):
        self.items.append(item)

    def calculate_worry_level(self, item: int) -> int:
        number_or_string = self.operation.number

        try:
            n = int(number_or_string)
        except ValueError:
            n = item

        worry = self.operation.operator(item, n)

        if self.reduced_worry:
            worry = int(worry / 3)
        else:
            worry = worry % self.lcm

        return worry

    def as_dict(self) -> dict:
        return {
            "items": self.items,
            "operation": (self.operation.operator, self.operation.number),
            "test": (self.test.divisor, self.test.if_true, self.test.if_false),
        }


def init_monkeys(input: list[str], reduced_worry=True) -> list[Monkey]:
    monkeys = []

    operator_map = {"*": operator.mul, "+": operator.add}

    for i in range(0, len(input), 7):
        items = [int(item) for item in input[i + 1].strip().split(": ")[-1].split(", ")]
        operator_char, number = input[i + 2].strip().split("= old ")[-1].split(" ")
        test_divisor = int(input[i + 3].strip().split(" ")[-1])
        if_true = int(input[i + 4].strip().split(" ")[-1])
        if_false = int(input[i + 5].strip().split(" ")[-1])

        operation = Operation(operator_map[operator_char], number)
        test = Test(test_divisor, if_true, if_false)
        monkeys.append(Monkey(items, operation, test, reduced_worry))

    if not reduced_worry:
        lcm = functools.reduce(
            lambda x, y: x * y, (monkey.test.divisor for monkey in monkeys), 1
        )
        for monkey in monkeys:
            monkey.lcm = lcm

    return monkeys


def play_catch(monkeys, rounds: int = 20):
    for round in range(rounds):
        for monkey in monkeys:
            thrown = monkey.throw()
            for to_monkey, item in thrown:
                monkeys[to_monkey].catch(item)


if __name__ == "__main__":
    with open("day11.txt") as infile:
        monkey_data = infile.readlines()

    monkeys = init_monkeys(monkey_data, reduced_worry=True)
    play_catch(monkeys)
    by_activity = sorted([monkey.inspected_count for monkey in monkeys], reverse=True)
    print(by_activity[0] * by_activity[1])

    monkeys = init_monkeys(monkey_data, reduced_worry=False)
    play_catch(monkeys, rounds=10000)
    by_activity = sorted([monkey.inspected_count for monkey in monkeys], reverse=True)
    print(by_activity[0] * by_activity[1])
