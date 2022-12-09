import math
from dataclasses import dataclass


@dataclass(frozen=True)
class Point:
    x: int
    y: int

    @property
    def tuple(self):
        return (self.x, self.y)


@dataclass
class Move:
    direction: str
    magnitude: int


def get_moves(input: list[str]) -> list[Move]:
    moves = []
    for line in input:
        direction, magnitude = line.strip().split(" ")
        moves.append(Move(direction=direction, magnitude=int(magnitude)))

    return moves


def rope_of_length(n) -> list[Point]:
    return [Point(x=0, y=0) for _ in range(n)]


def move_rope(knots: list[Point], direction: str):
    knots[0] = move_knot(knots[0], direction)

    for i in range(1, len(knots)):
        if not is_touching(knots[i - 1], knots[i]):
            direction = get_heading(knots[i - 1], knots[i])
            knots[i] = move_knot(knots[i], direction)

    return knots


def get_tail_positions(knots: list[Point], moves: list[Move]) -> set[Point]:
    positions = set()
    positions.add(knots[-1])

    for move in moves:
        for _ in range(move.magnitude):
            knots = move_rope(knots, move.direction)
            positions.add(knots[-1])

    return positions


def get_heading(head: Point, tail: Point) -> str:
    if head.x == tail.x:
        if head.y < tail.y:
            return "D"
        else:
            return "U"
    elif head.y == tail.y:
        if head.x < tail.x:
            return "L"
        else:
            return "R"
    else:
        if head.y < tail.y:
            if head.x < tail.x:
                return "DL"
            if head.x > tail.x:
                return "DR"
        elif head.y > tail.y:
            if head.x < tail.x:
                return "UL"
            if head.x > tail.x:
                return "UR"

    raise Exception(f"Could not determine heading. head={head} tail={tail}")


def move_knot(knot: Point, direction: str) -> Point:
    if direction == "U":
        return Point(x=knot.x, y=knot.y + 1)
    elif direction == "D":
        return Point(x=knot.x, y=knot.y - 1)
    elif direction == "R":
        return Point(x=knot.x + 1, y=knot.y)
    elif direction == "L":
        return Point(x=knot.x - 1, y=knot.y)
    elif direction == "UR":
        return Point(x=knot.x + 1, y=knot.y + 1)
    elif direction == "UL":
        return Point(x=knot.x - 1, y=knot.y + 1)
    elif direction == "DR":
        return Point(x=knot.x + 1, y=knot.y - 1)
    elif direction == "DL":
        return Point(x=knot.x - 1, y=knot.y - 1)

    raise Exception(f"Direction not supported. direction={direction}")


def is_touching(head: Point, tail: Point) -> bool:
    return math.dist(head.tuple, tail.tuple) < 2


if __name__ == "__main__":
    with open("day9.txt") as infile:
        moves = get_moves(infile.readlines())

    print(len(get_tail_positions(rope_of_length(2), moves)))
    print(len(get_tail_positions(rope_of_length(10), moves)))
