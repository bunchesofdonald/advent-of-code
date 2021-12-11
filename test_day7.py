import unittest

import day7


PUZZLE_INPUT = """16,1,2,0,4,2,7,1,2,14"""


class ParseInputTestCase(unittest.TestCase):
    def test_example(self):
        assert day7.parse_input(PUZZLE_INPUT) == [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]


class NaiveFuelCost(unittest.TestCase):
    def test_example(self):
        positions = day7.parse_input(PUZZLE_INPUT)
        assert day7.naive_fuel_cost(positions) == 37


class ActualFuelCost(unittest.TestCase):
    def test_example(self):
        positions = day7.parse_input(PUZZLE_INPUT)
        assert day7.actual_fuel_cost(positions) == 168
