import unittest

import day9


PUZZLE_INPUT = """2199943210
3987894921
9856789892
8767896789
9899965678"""


class ParseInputTestCase(unittest.TestCase):
    def test_example(self):
        heightmap = day9.parse_input(PUZZLE_INPUT.split('\n'))
        assert heightmap == [
            [2, 1, 9, 9, 9, 4, 3, 2, 1, 0],
            [3, 9, 8, 7, 8, 9, 4, 9, 2, 1],
            [9, 8, 5, 6, 7, 8, 9, 8, 9, 2],
            [8, 7, 6, 7, 8, 9, 6, 7, 8, 9],
            [9, 8, 9, 9, 9, 6, 5, 6, 7, 8],
        ]


class FindLowPointsTestCase(unittest.TestCase):
    def test_example(self):
        heightmap = day9.parse_input(PUZZLE_INPUT.split('\n'))
        assert day9.find_low_points(heightmap) == {
            (1, 0): 2,
            (9, 0): 1,
            (2, 2): 6,
            (6, 4): 6,
        }


class FindBasinsTestCase(unittest.TestCase):
    def test_example(self):
        heightmap = day9.parse_input(PUZZLE_INPUT.split('\n'))
        assert day9.find_basins(heightmap) == [
            3, 9, 14, 9
        ]
