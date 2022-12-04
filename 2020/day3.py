from math import prod

TREE = '#'


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, other):
        self.x += other.x
        self.y += other.y
        return self

    def __repr__(self):
        return f'({self.x}, {self.y})'


def tree_count(tree_map, slope=None):
    if not slope:
        slope = Point(3, 1)

    start = Point(0, 0)
    next_point = start.add(slope)

    count = 0
    while next_point.y < len(tree_map):
        width = len(tree_map[next_point.y])
        if tree_map[next_point.y][next_point.x % width] == TREE:
            count += 1

        next_point = next_point.add(slope)

    return count


if __name__ == "__main__":
    tree_map = []

    with open('day3.txt') as infile:
        for line in infile.readlines():
            tree_map.append(line.strip())

    counts = []
    slopes = [
        Point(1, 1),
        Point(3, 1),
        Point(5, 1),
        Point(7, 1),
        Point(1, 2),
    ]

    for slope in slopes:
        counts.append(tree_count(tree_map, slope))

    print(counts[1])
    print(prod(counts))
