
import unittest

import day12


PUZZLE_INPUT = """start-A
start-b
A-c
A-b
b-d
A-end
b-end"""


class ParseInputTestCase(unittest.TestCase):
    def test_example(self):
        graph = day12.parse_input(PUZZLE_INPUT.split('\n'))
        assert graph == {
            'start': ['A',  'b'],
            'A': ['start',  'c',  'b',  'end'],
            'b': ['start',  'A',  'd',  'end'],
            'c': ['A'],
            'd': ['b'],
            'end': ['A',  'b']
        }


class FindAllPathsTestCase(unittest.TestCase):
    def test_example(self):
        graph = day12.parse_input(PUZZLE_INPUT.split('\n'))
        paths = day12.find_all_paths(graph, 'start',  'end')
        expected = [
            ['start', 'A', 'b', 'A', 'c', 'A', 'end'],
            ['start', 'A', 'b', 'A', 'end'],
            ['start', 'A', 'b', 'end'],
            ['start', 'A', 'c', 'A', 'b', 'A', 'end'],
            ['start', 'A', 'c', 'A', 'b', 'end'],
            ['start', 'A', 'c', 'A', 'end'],
            ['start', 'A', 'end'],
            ['start', 'b', 'A', 'c', 'A', 'end'],
            ['start', 'b', 'A', 'end'],
            ['start', 'b', 'end'],
        ]

        assert len(paths) == len(expected)
        for path in paths:
            assert path in expected


class FindAllPathsSpecialTestCase(unittest.TestCase):
    def test_example(self):
        graph = day12.parse_input(PUZZLE_INPUT.split('\n'))
        paths = day12.find_all_paths_special(graph, 'start', 'end')
        print(paths)
        expected = [
            ['start', 'A', 'c', 'A', 'c', 'A', 'b', 'A', 'end'],
            ['start', 'A', 'c', 'A', 'c', 'A', 'b', 'end'],
            ['start', 'A', 'c', 'A', 'c', 'A', 'end'],
            ['start', 'A', 'c', 'A', 'b', 'A', 'c', 'A', 'end'],
            ['start', 'A', 'c', 'A', 'b', 'A', 'b', 'A', 'end'],
            ['start', 'A', 'c', 'A', 'b', 'A', 'b', 'end'],
            ['start', 'A', 'c', 'A', 'b', 'A', 'end'],
            ['start', 'A', 'c', 'A', 'b', 'd', 'b', 'A', 'end'],
            ['start', 'A', 'c', 'A', 'b', 'd', 'b', 'end'],
            ['start', 'A', 'c', 'A', 'b', 'end'],
            ['start', 'A', 'c', 'A', 'end'],
            ['start', 'A', 'b', 'A', 'c', 'A', 'c', 'A', 'end'],
            ['start', 'A', 'b', 'A', 'c', 'A', 'b', 'A', 'end'],
            ['start', 'A', 'b', 'A', 'c', 'A', 'b', 'end'],
            ['start', 'A', 'b', 'A', 'c', 'A', 'end'],
            ['start', 'A', 'b', 'A', 'b', 'A', 'c', 'A', 'end'],
            ['start', 'A', 'b', 'A', 'b', 'A', 'end'],
            ['start', 'A', 'b', 'A', 'b', 'end'],
            ['start', 'A', 'b', 'A', 'end'],
            ['start', 'A', 'b', 'd', 'b', 'A', 'c', 'A', 'end'],
            ['start', 'A', 'b', 'd', 'b', 'A', 'end'],
            ['start', 'A', 'b', 'd', 'b', 'end'],
            ['start', 'A', 'b', 'end'],
            ['start', 'A', 'end'],
            ['start', 'b', 'A', 'c', 'A', 'c', 'A', 'end'],
            ['start', 'b', 'A', 'c', 'A', 'b', 'A', 'end'],
            ['start', 'b', 'A', 'c', 'A', 'b', 'end'],
            ['start', 'b', 'A', 'c', 'A', 'end'],
            ['start', 'b', 'A', 'b', 'A', 'c', 'A', 'end'],
            ['start', 'b', 'A', 'b', 'A', 'end'],
            ['start', 'b', 'A', 'b', 'end'],
            ['start', 'b', 'A', 'end'],
            ['start', 'b', 'd', 'b', 'A', 'c', 'A', 'end'],
            ['start', 'b', 'd', 'b', 'A', 'end'],
            ['start', 'b', 'd', 'b', 'end'],
            ['start', 'b', 'end']
        ]

        assert len(paths) == len(expected)
        for path in paths:
            assert path in expected
