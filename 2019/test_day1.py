from unittest import TestCase

from day1 import full_fuel_cost, naieve_fuel_cost


class Day1TestCase(TestCase):
    def test_day1(self):
        assert naieve_fuel_cost(2) == 0
        assert naieve_fuel_cost(12) == 2
        assert naieve_fuel_cost(14) == 2
        assert naieve_fuel_cost(1969) == 654
        assert naieve_fuel_cost(100756) == 33583

    def test_day1p2(self):
        assert full_fuel_cost(12) == 2
        assert full_fuel_cost(1969) == 966
        assert full_fuel_cost(100756) == 50346
