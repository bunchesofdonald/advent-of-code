from day12 import read_graph, gentle_path

puzzle_input = """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi""".split(
    "\n"
)


def test_read_graph():
    graph, start, end = read_graph(puzzle_input)
    assert graph == {
        (0, 0): 0,
        (1, 0): 0,
        (2, 0): 1,
        (3, 0): 16,
        (4, 0): 15,
        (5, 0): 14,
        (6, 0): 13,
        (7, 0): 12,
        (0, 1): 0,
        (1, 1): 1,
        (2, 1): 2,
        (3, 1): 17,
        (4, 1): 24,
        (5, 1): 23,
        (6, 1): 23,
        (7, 1): 11,
        (0, 2): 0,
        (1, 2): 2,
        (2, 2): 2,
        (3, 2): 18,
        (4, 2): 25,
        (5, 2): 25,
        (6, 2): 23,
        (7, 2): 10,
        (0, 3): 0,
        (1, 3): 2,
        (2, 3): 2,
        (3, 3): 19,
        (4, 3): 20,
        (5, 3): 21,
        (6, 3): 22,
        (7, 3): 9,
        (0, 4): 0,
        (1, 4): 1,
        (2, 4): 3,
        (3, 4): 4,
        (4, 4): 5,
        (5, 4): 6,
        (6, 4): 7,
        (7, 4): 8,
    }

    assert start == (0, 0)
    assert end == (5, 2)


def test_gentle_path():
    graph, start, end = read_graph(puzzle_input)
    assert gentle_path(graph, start, end) == 31
