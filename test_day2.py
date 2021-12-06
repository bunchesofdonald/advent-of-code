import unittest

from day2 import better_end_point, end_point

COMMANDS_EXAMPLE = [
    'forward 5', 'down 5', 'forward 8', 'up 3', 'down 8', 'forward 2']


class EndPointTestCase(unittest.TestCase):
    def test_example(self):
        assert end_point(COMMANDS_EXAMPLE) == (15, 10)


class BetterEndPointTestCase(unittest.TestCase):
    def test_example(self):
        assert better_end_point(COMMANDS_EXAMPLE) == (15, 60)
