from collections import defaultdict
from bresenham import bresenham
from dataclasses import dataclass
import math


@dataclass
class Point:
    x: int
    y: int


@dataclass
class Line:
    p1: Point
    p2: Point

    @property
    def is_vertical(self) -> bool:
        return self.p1.x == self.p2.x

    @property
    def is_horizontal(self) -> bool:
        return self.p1.y == self.p2.y

    @property
    def is_axial(self) -> bool:
        return self.is_vertical or self.is_horizontal

    @property
    def is_diagonal(self) -> bool:
        return not self.is_axial

    @property
    def points(self) -> list:
        return list(bresenham(self.p1.x, self.p1.y, self.p2.x, self.p2.y))


def parse_input(input):
    lines = []
    max_x = max_y = 0
    for row in input:
        axis_one, axis_two = row.split(' -> ')
        x1, y1 = axis_one.split(',')
        x2, y2 = axis_two.split(',')

        x1 = int(x1)
        y1 = int(y1)
        x2 = int(x2)
        y2 = int(y2)

        max_x = max(max_x, x1, x2)
        max_y = max(max_y, y1, y2)

        lines.append(Line(Point(x1, y1), Point(x2, y2)))

    return lines, max_x, max_y


def plot_map(lines, axial_only=True):
    plot = defaultdict(int)

    for line in lines:
        if axial_only and not line.is_axial:
            continue

        for x, y in bresenham(line.p1.x, line.p1.y, line.p2.x, line.p2.y):
            plot[(x, y)] += 1

    return plot


if __name__ == '__main__':
    input = """0,9 -> 5,9
    8,0 -> 0,8
    9,4 -> 3,4
    2,2 -> 2,1
    7,0 -> 7,4
    6,4 -> 2,0
    0,9 -> 2,9
    3,4 -> 1,4
    0,0 -> 8,8
    5,5 -> 8,2"""

    with open('day5.txt') as infile:
        lines, max_x, max_y = parse_input(infile.readlines())

    plot = plot_map(lines, axial_only=False)
    count = 0
    for overlap_count in plot.values():
        if overlap_count >= 2:
            count += 1
    print(count)
