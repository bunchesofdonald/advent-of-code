import operator


def make_grid(size):
    return [["."] * size] * size


def find_intersections():
    pass


def get_origin(grid):
    return (0, len(grid[0]) - 1)


def plot_wire(path, grid):
    x, y = get_origin(grid)
    for step in path:
        direction = step[0]
        distance = int(step[1:])

        if direction in ['U', 'D']:
            func = operator.sub if direction == 'U' else operator.add
            for i in range(distance):
                new_y = func(y, i)
                grid[new_y][x] = '+'
        else:
            func = operator.sub if direction == 'L' else operator.add
            for i in range(distance):
                new_x = func(x, i)
                grid[new_y][x] = '+'


if __name__ == "__main__":
    grid = make_grid(100)
    plot_wire(["R75", "D30", "R83", "U83", "L12", "D49", "R71", "U7", "L72"])
