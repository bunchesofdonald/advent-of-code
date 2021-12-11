def parse_input(input):
    heightmap = []
    for line in input:
        heightmap.append([int(number) for number in line.strip()])
    return heightmap


def find_low_points(heightmap):
    low_points = {}
    height = len(heightmap)
    width = len(heightmap[0])

    for y in range(height):
        for x in range(width):
            adjacent_values = []

            if x - 1 >= 0:
                adjacent_values.append(heightmap[y][x - 1])

            if x + 1 < width:
                adjacent_values.append(heightmap[y][x + 1])

            if y - 1 >= 0:
                adjacent_values.append(heightmap[y - 1][x])

            if y + 1 < height:
                adjacent_values.append(heightmap[y + 1][x])

            if all(heightmap[y][x] < value for value in adjacent_values):
                low_points[(x, y)] = heightmap[y][x] + 1

    return low_points


def find_basins(heightmap):
    basins = []
    height = len(heightmap)
    width = len(heightmap[0])

    for y in range(height):
        for x in range(width):
            if not any((x, y) in basin for basin in basins):
                if heightmap[y][x] < 9:
                    basins.append(map_basin(x, y, heightmap))

    return [len(basin) for basin in basins]


def map_basin(origin_x, origin_y, heightmap):
    height = len(heightmap)
    width = len(heightmap[0])
    adjacent_points = [(origin_x, origin_y)]
    mapped_points = []
    basin_points = set()

    if heightmap[origin_y][origin_x] < 9:
        basin_points.add((origin_x, origin_y))
    else:
        return None

    while adjacent_points:
        x, y = adjacent_points.pop()

        if (x, y) in mapped_points:
            continue
        else:
            mapped_points.append((x, y))

        basin_points.add((x, y))

        if x - 1 >= 0 and heightmap[y][x - 1] < 9:
            adjacent_points.append((x - 1, y))

        if x + 1 < width and heightmap[y][x + 1] < 9:
            adjacent_points.append((x + 1, y))

        if y - 1 >= 0 and heightmap[y - 1][x] < 9:
            adjacent_points.append((x, y - 1))

        if y + 1 < height and heightmap[y + 1][x] < 9:
            adjacent_points.append((x, y + 1))

    return basin_points


if __name__ == '__main__':
    with open('day9.txt') as infile:
        heightmap = parse_input(infile.readlines())

    low_points = find_low_points(heightmap)
    print(len(low_points))
    print(sum(low_points.values()))

    basins = sorted(find_basins(heightmap))
    result = 1
    for basin_size in basins[-3:]:
        result = result * basin_size

    print(result)
