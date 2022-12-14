import math
from dataclasses import dataclass


@dataclass(frozen=True)
class Point:
    x: int
    y: int


Graph = dict[Point, str]


class AbyssalException(Exception):
    """Raised when a grain of sand drops into the Abyss"""


class CaveFullException(Exception):
    """Raised when no more grains of sand can drop into the cave"""


def points_in_line(start: Point, end: Point) -> list[Point]:
    if start.x == end.x:
        # Horizontal line
        highest = min(start.y, end.y)
        lowest = max(start.y, end.y)
        return [Point(start.x, y) for y in range(highest, lowest + 1)]
    else:
        # Vertical line
        leftest = min(start.x, end.x)
        rightest = max(start.x, end.x)
        return [Point(x, start.y) for x in range(leftest, rightest + 1)]


def read_cave_graph(input: list[str]) -> Graph:
    cave: Graph = {}

    for row in input:
        row = row.strip()
        start = None
        end = None
        for segment in row.split(" -> "):
            if start is None:
                start_x, start_y = segment.split(",")
                start = Point(x=int(start_x), y=int(start_y))
            else:
                end_x, end_y = segment.split(",")
                end = Point(x=int(end_x), y=int(end_y))
                for point in points_in_line(start, end):
                    cave[point] = "#"

                start = end

    return cave


def drop_sand(cave: Graph, origin=Point(500, 0), cave_floor=False) -> Graph:
    sand = Point(x=origin.x, y=origin.y)
    lowest_y = max(point.y for point, value in cave.items() if value == "#")
    if cave_floor:
        if cave.get(origin) == "*":
            raise CaveFullException()

        lowest_y += 2

    at_rest = False
    last = None

    while not at_rest:
        last = sand

        if sand.y + 1 > lowest_y:
            raise AbyssalException("Sand fell into the Abyss")

        options = [
            Point(x=sand.x, y=sand.y + 1),
            Point(x=sand.x - 1, y=sand.y + 1),
            Point(x=sand.x + 1, y=sand.y + 1),
        ]

        def open_space(option):
            if cave_floor:
                return option.y < lowest_y and option not in cave

            return option not in cave

        options = [option for option in options if open_space(option)]

        if options:
            sand = options[0]

        if sand == last:
            at_rest = True

    cave[sand] = "*"
    return cave


def fill_cave(cave: Graph, cave_floor=False) -> Graph:
    while True:
        try:
            cave = drop_sand(cave, cave_floor=cave_floor)
        except (AbyssalException, CaveFullException):
            break

    return cave


if __name__ == "__main__":
    with open("day14.txt") as infile:
        cave = read_cave_graph(infile.readlines())

    filled_cave = fill_cave(cave.copy())
    print(sum([1 for value in filled_cave.values() if value == "*"]))

    filled_cave = fill_cave(cave.copy(), cave_floor=True)
    print(sum([1 for value in filled_cave.values() if value == "*"]))
