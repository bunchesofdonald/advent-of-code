from unittest import TestCase

from day5 import get_seat_id


class GetSeatIdTestCase(TestCase):
    def test_gets_seat_id(self):
        """get_seat_id should know how to decode the seat ID from a BSP
        string"""
        assert get_seat_id('FBFBBFFRLR') == 357
        assert get_seat_id('BFFFBBFRRR') == 567
        assert get_seat_id('FFFBBBFRRR') == 119
        assert get_seat_id('BBFFBBFRLL') == 820
