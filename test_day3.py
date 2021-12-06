import unittest

import day3


DIAGNOSTIC_REPORT = [
    '00100',
    '11110',
    '10110',
    '10111',
    '10101',
    '01111',
    '00111',
    '11100',
    '10000',
    '11001',
    '00010',
    '01010',
]


class PowerConsumptionTestCase(unittest.TestCase):
    def test_example(self):
        assert day3.power_consumption(DIAGNOSTIC_REPORT) == 198


class LifeSupportRatingTestCase(unittest.TestCase):
    def test_example(self):
        assert day3.life_support_rating(DIAGNOSTIC_REPORT) == 230
