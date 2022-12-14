from day14 import Point, drop_sand, fill_cave, read_cave_graph


puzzle_input = """498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9""".split(
    "\n"
)


def test_read_cave_graph():
    assert read_cave_graph(puzzle_input) == {
        Point(498, 4): "#",
        Point(498, 5): "#",
        Point(498, 6): "#",
        Point(497, 6): "#",
        Point(496, 6): "#",
        Point(503, 4): "#",
        Point(502, 4): "#",
        Point(502, 5): "#",
        Point(502, 6): "#",
        Point(502, 7): "#",
        Point(502, 8): "#",
        Point(502, 9): "#",
        Point(501, 9): "#",
        Point(500, 9): "#",
        Point(499, 9): "#",
        Point(498, 9): "#",
        Point(497, 9): "#",
        Point(496, 9): "#",
        Point(495, 9): "#",
        Point(494, 9): "#",
    }


def test_drop_sand():
    graph = read_cave_graph(puzzle_input)
    graph = drop_sand(graph)
    assert graph[Point(500, 8)] == "*"


def test_fill_cave():
    graph = read_cave_graph(puzzle_input)
    graph = fill_cave(graph)

    assert sum([1 for value in graph.values() if value == "*"]) == 24


def test_fill_cave_with_floor():
    graph = read_cave_graph(puzzle_input)
    graph = fill_cave(graph, cave_floor=True)

    assert sum([1 for value in graph.values() if value == "*"]) == 93
