from unittest import TestCase


from day1 import doit


class DayOneTestCase(TestCase):
    def test_returns_product(self):
        """doit should be able to find the two numbers that add up to `n` and
        return the product of those two numbers"""
        input = [
            1721,
            979,
            366,
            299,
            675,
            1456,
        ]

        assert doit(input, 2020) == 514579
