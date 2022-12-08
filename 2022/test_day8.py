from day8 import best_scenic_score, visible_tree_count, read_topographical_map

puzzle_input = """30373
25512
65332
33549
35390""".split(
    "\n"
)


def test_read_topographical_map():
    assert read_topographical_map(puzzle_input) == [
        [3, 0, 3, 7, 3],
        [2, 5, 5, 1, 2],
        [6, 5, 3, 3, 2],
        [3, 3, 5, 4, 9],
        [3, 5, 3, 9, 0],
    ]


def test_visible_tree_count():
    forest_map = read_topographical_map(puzzle_input)
    assert visible_tree_count(forest_map) == 21


def test_best_scenic_score():
    forest_map = read_topographical_map(puzzle_input)
    assert best_scenic_score(forest_map) == 8
