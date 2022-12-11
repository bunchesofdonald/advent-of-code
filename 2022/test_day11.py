import operator

from day11 import Monkey, init_monkeys, play_catch

puzzle_input = """Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1""".split(
    "\n"
)


def test_init_monkeys():
    monkeys = init_monkeys(puzzle_input)
    assert len(monkeys) == 4
    assert [m.as_dict() for m in monkeys] == [
        {"items": [79, 98], "operation": (operator.mul, "19"), "test": (23, 2, 3)},
        {
            "items": [54, 65, 75, 74],
            "operation": (operator.add, "6"),
            "test": (19, 2, 0),
        },
        {"items": [79, 60, 97], "operation": (operator.mul, "old"), "test": (13, 1, 3)},
        {"items": [74], "operation": (operator.add, "3"), "test": (17, 0, 1)},
    ]


def test_play_catch():
    monkeys = init_monkeys(puzzle_input)
    play_catch(monkeys, rounds=20)

    assert monkeys[0].items == [10, 12, 14, 26, 34]
    assert monkeys[1].items == [245, 93, 53, 199, 115]
    assert monkeys[2].items == []
    assert monkeys[3].items == []

    assert monkeys[0].inspected_count == 101
    assert monkeys[1].inspected_count == 95
    assert monkeys[2].inspected_count == 7
    assert monkeys[3].inspected_count == 105
