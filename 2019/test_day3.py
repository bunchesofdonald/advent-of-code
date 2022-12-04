from unittest import TestCase

from day3 import plot_wire


class Day3TestCase(TestCase):
    def test_day3p1(self):
        plot_wire(["R75", "D30", "R83", "U83", "L12", "D49", "R71", "U7", "L72"])
