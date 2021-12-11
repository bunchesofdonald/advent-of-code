import math
import statistics


def parse_input(input):
    return [int(number) for number in input.split(',')]


def triangle_number(n):
    return (n * (n + 1)) // 2


def naive_fuel_cost(positions):
    median_position = int(statistics.median(positions))
    return sum(abs(position - median_position) for position in positions)


def actual_fuel_cost(positions):
    avg_position = statistics.mean(positions)
    return min(
        sum(triangle_number(abs(position - math.floor(avg_position))) for position in positions),
        sum(triangle_number(abs(position - math.ceil(avg_position))) for position in positions),
    )


if __name__ == '__main__':
    with open('day7.txt') as infile:
        positions = parse_input(infile.read())

    print(naive_fuel_cost(positions))
    print(actual_fuel_cost(positions))
