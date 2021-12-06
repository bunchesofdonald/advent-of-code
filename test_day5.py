import unittest

import day5


PUZZLE_INPUT = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2"""


class LineTestCase(unittest.TestCase):
    def test_is_axial(self):
        assert day5.Line(day5.Point(0, 1), day5.Point(0, 8)).is_vertical
        assert day5.Line(day5.Point(0, 1), day5.Point(8, 1)).is_horizontal
        assert day5.Line(day5.Point(0, 0), day5.Point(8, 8)).is_diagonal


class ParseInputTestCase(unittest.TestCase):
    def test_parses_input_to_lines(self):
        assert day5.parse_input(PUZZLE_INPUT.split('\n')) == (
            [
                day5.Line(day5.Point(0, 9), day5.Point(5, 9)),
                day5.Line(day5.Point(8, 0), day5.Point(0, 8)),
                day5.Line(day5.Point(9, 4), day5.Point(3, 4)),
                day5.Line(day5.Point(2, 2), day5.Point(2, 1)),
                day5.Line(day5.Point(7, 0), day5.Point(7, 4)),
                day5.Line(day5.Point(6, 4), day5.Point(2, 0)),
                day5.Line(day5.Point(0, 9), day5.Point(2, 9)),
                day5.Line(day5.Point(3, 4), day5.Point(1, 4)),
                day5.Line(day5.Point(0, 0), day5.Point(8, 8)),
                day5.Line(day5.Point(5, 5), day5.Point(8, 2)),
            ],
            9,
            9
        )


class PlotMapTestCase(unittest.TestCase):
    def test_example_axial_only(self):
        lines, *_ = day5.parse_input(PUZZLE_INPUT.split('\n'))
        plot = day5.plot_map(lines, axial_only=True)
        assert plot == {
            (0, 9): 2,
            (1, 9): 2,
            (2, 9): 2,
            (3, 9): 1,
            (4, 9): 1,
            (5, 9): 1,
            (9, 4): 1,
            (8, 4): 1,
            (7, 4): 2,
            (6, 4): 1,
            (5, 4): 1,
            (4, 4): 1,
            (3, 4): 2,
            (2, 2): 1,
            (2, 1): 1,
            (7, 0): 1,
            (7, 1): 1,
            (7, 2): 1,
            (7, 3): 1,
            (2, 4): 1,
            (1, 4): 1,
        }

    def test_example_all(self):
        lines, *_ = day5.parse_input(PUZZLE_INPUT.split('\n'))
        plot = day5.plot_map(lines, axial_only=False)
        assert plot == {
            (0, 9): 2,
            (1, 9): 2,
            (2, 9): 2,
            (3, 9): 1,
            (4, 9): 1,
            (5, 9): 1,
            (8, 0): 1,
            (7, 1): 2,
            (6, 2): 1,
            (5, 3): 2,
            (4, 4): 3,
            (3, 5): 1,
            (2, 6): 1,
            (1, 7): 1,
            (0, 8): 1,
            (9, 4): 1,
            (8, 4): 1,
            (7, 4): 2,
            (6, 4): 3,
            (5, 4): 1,
            (3, 4): 2,
            (2, 2): 2,
            (2, 1): 1,
            (7, 0): 1,
            (7, 2): 1,
            (7, 3): 2,
            (4, 2): 1,
            (3, 1): 1,
            (2, 0): 1,
            (2, 4): 1,
            (1, 4): 1,
            (0, 0): 1,
            (1, 1): 1,
            (3, 3): 1,
            (5, 5): 2,
            (6, 6): 1,
            (7, 7): 1,
            (8, 8): 1,
            (8, 2): 1
        }
