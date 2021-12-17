import unittest

import day15


PUZZLE_INPUT = """1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581"""


class LowestRiskPath(unittest.TestCase):
    def test_example(self):
        graph, height, width = day15.parse_input(PUZZLE_INPUT.split('\n'))
        assert day15.lowest_risk_path(graph, height, width) == 40

        expanded_graph, height, width = day15.expand_graph(graph, 5, height, width)
        assert day15.lowest_risk_path(expanded_graph, height, width) == 315
