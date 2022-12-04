import unittest

import day6


PUZZLE_INPUT = """3,4,3,1,2"""


class ParseInputTestCase(unittest.TestCase):
    def test_example(self):
        assert day6.parse_input(PUZZLE_INPUT) == [3, 4, 3, 1, 2]


class SpawnLaternfishTestCase(unittest.TestCase):
    def test_example(self):
        starting_fish = day6.parse_input(PUZZLE_INPUT)
        assert day6.spawn_laternfish(starting_fish, days=18) == 26
        assert day6.spawn_laternfish(starting_fish, days=80) == 5934
