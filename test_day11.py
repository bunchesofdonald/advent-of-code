import unittest

import day11


PUZZLE_INPUT = """5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526"""


class FlashCountTestCase(unittest.TestCase):
    def test_example(self):
        octopuses = day11.parse_input(PUZZLE_INPUT.split('\n'))
        assert day11.flash_count(octopuses) == 1656


class SyncedFlashTestCase(unittest.TestCase):
    def test_example(self):
        octopuses = day11.parse_input(PUZZLE_INPUT.split('\n'))
        assert day11.synced_flash(octopuses) == 195
