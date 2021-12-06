import unittest

from day1 import depth_increase_rate, depth_increase_rate_window

DEPTHS_EXAMPLE = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]


class DepthIncreaseRateTestCase(unittest.TestCase):
    def test_example(self):
        assert depth_increase_rate(DEPTHS_EXAMPLE) == 7


class DepthIncreaseRateWindowTestCase(unittest.TestCase):
    def test_example(self):
        assert depth_increase_rate_window(DEPTHS_EXAMPLE) == 5
