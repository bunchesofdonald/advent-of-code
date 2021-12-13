import copy

import utils


def parse_input(lines):
    octopuses = []
    for line in lines:
        octopuses.append([int(energy) for energy in line.strip()])
    return octopuses


def flash_count(octopuses, n=100):
    count = 0
    for _ in range(n):
        to_flash = set()
        for y in range(len(octopuses)):
            for x in range(len(octopuses[y])):
                octopuses[y][x] += 1
                if octopuses[y][x] > 9:
                    to_flash.add((x, y))

        while to_flash:
            count += 1
            x, y = to_flash.pop()
            octopuses[y][x] = 0
            for other_x, other_y in utils.adjacent_points(x, y):
                if octopuses[other_y][other_x] > 0:
                    octopuses[other_y][other_x] += 1
                if octopuses[other_y][other_x] > 9:
                    to_flash.add((other_x, other_y))

    return count


def synced_flash(octopuses):
    n = 0
    all_flashed = False
    while not all_flashed:
        flash_count = 0
        n += 1
        to_flash = set()
        for y in range(len(octopuses)):
            for x in range(len(octopuses[y])):
                octopuses[y][x] += 1
                if octopuses[y][x] > 9:
                    to_flash.add((x, y))

        while to_flash:
            flash_count += 1
            x, y = to_flash.pop()
            octopuses[y][x] = 0
            for other_x, other_y in utils.adjacent_points(x, y):
                if octopuses[other_y][other_x] > 0:
                    octopuses[other_y][other_x] += 1
                if octopuses[other_y][other_x] > 9:
                    to_flash.add((other_x, other_y))

        all_flashed = flash_count == 100

    return n


if __name__ == '__main__':
    with open('day11.txt') as infile:
        octopuses = parse_input(infile.readlines())

    print(flash_count(copy.deepcopy(octopuses)))
    print(synced_flash(copy.deepcopy(octopuses)))
