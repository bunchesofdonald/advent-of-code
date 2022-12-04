from unittest import TestCase

from day3 import Point, tree_count

TREE_MAP = (
    "..##.......",
    "#...#...#..",
    ".#....#..#.",
    "..#.#...#.#",
    ".#...##..#.",
    "..#.##.....",
    ".#.#.#....#",
    ".#........#",
    "#.##...#...",
    "#...##....#",
    ".#..#...#.#"
)


class TreeCountTestCase(TestCase):
    def test_knows_how_many_trees(self):
        """tree_count should know how many trees are in the 3,1 slope"""
        assert tree_count(TREE_MAP) == 7

    def test_multiple_slopes(self):
        """tree_count should be able to calculate multiple slopes"""
        assert tree_count(TREE_MAP, slope=Point(1, 1)) == 2
        assert tree_count(TREE_MAP, slope=Point(3, 1)) == 7
        assert tree_count(TREE_MAP, slope=Point(5, 1)) == 3
        assert tree_count(TREE_MAP, slope=Point(7, 1)) == 4
        assert tree_count(TREE_MAP, slope=Point(1, 2)) == 2
