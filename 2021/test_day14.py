import unittest

import day14

PUZZLE_INPUT = """NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C"""


class ParseInputTestCase(unittest.TestCase):
    def test_example(self):
        template, rules = day14.parse_input(PUZZLE_INPUT.split('\n'))
        assert template == 'NNCB'
        assert rules == {
            'CH': 'B',
            'HH': 'N',
            'CB': 'H',
            'NH': 'C',
            'HB': 'C',
            'HC': 'B',
            'HN': 'C',
            'NN': 'C',
            'BH': 'H',
            'NC': 'B',
            'NB': 'B',
            'BN': 'B',
            'BB': 'N',
            'BC': 'B',
            'CC': 'N',
            'CN': 'C',
        }


class PolymerElementCountTestCase(unittest.TestCase):
    def test_example(self):
        template, rules = day14.parse_input(PUZZLE_INPUT.split('\n'))
        assert day14.polymer_element_count(template, rules, steps=1) == 1
        assert day14.polymer_element_count(template, rules, steps=2) == 5
        assert day14.polymer_element_count(template, rules, steps=3) == 7
        assert day14.polymer_element_count(template, rules, steps=4) == 18
