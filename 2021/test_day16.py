import unittest

import day16


PUZZLE_INPUT = "38006F45291200"


class ParseInputTestCase(unittest.TestCase):
    def test_example(self):
        assert day16.parse_input(PUZZLE_INPUT) == (
            '00111000000000000110111101000101001010010001001000000000'
        )


class DecodePacketTestCase(unittest.TestCase):
    def test_example(self):
        packet = day16.parse_input('D2FE28')
        assert day16.decode_packet(packet) == [{
            'version': 6,
            'type_id': 4,
            'value': 2021
        }]

        packet = day16.parse_input('38006F45291200')
        assert day16.decode_packet(packet) == {
            'version': 1,
            'type_id': 6,
        }
