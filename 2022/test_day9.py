from day9 import Move, Point, get_moves, get_tail_positions, rope_of_length

puzzle_input = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2""".split(
    "\n"
)


def test_get_moves():
    assert get_moves(puzzle_input) == [
        Move(direction="R", magnitude=4),
        Move(direction="U", magnitude=4),
        Move(direction="L", magnitude=3),
        Move(direction="D", magnitude=1),
        Move(direction="R", magnitude=4),
        Move(direction="D", magnitude=1),
        Move(direction="L", magnitude=5),
        Move(direction="R", magnitude=2),
    ]


def test_get_tail_positions_two_knots():
    moves = get_moves(puzzle_input)
    rope = rope_of_length(2)
    assert get_tail_positions(rope, moves) == {
        Point(x=0, y=0),
        Point(x=1, y=0),
        Point(x=2, y=0),
        Point(x=3, y=0),
        Point(x=4, y=1),
        Point(x=4, y=2),
        Point(x=3, y=2),
        Point(x=2, y=2),
        Point(x=1, y=2),
        Point(x=4, y=3),
        Point(x=3, y=3),
        Point(x=2, y=4),
        Point(x=3, y=4),
    }
