from collections import defaultdict


def parse_input(input):
    return [
        int(number) for number in input.split(',')
    ]


def spawn_laternfish(starting_fish, days=80):
    fish_by_age = defaultdict(int)
    possible_ages = [0, 1, 2, 3, 4, 5, 6, 7, 8]

    for fish_age in starting_fish:
        fish_by_age[fish_age] += 1

    for _ in range(days):
        for age in possible_ages:
            next_age = age - 1
            fish_by_age[next_age] = fish_by_age[age]
            fish_by_age[age] = 0

        if count_at_spawn_age := fish_by_age.get(-1):
            fish_by_age[8] = count_at_spawn_age
            fish_by_age[6] += count_at_spawn_age
            fish_by_age[-1] = 0

    return sum(fish_by_age.values())


if __name__ == '__main__':
    with open('day6.txt') as infile:
        starting_fish = parse_input(infile.read())

    print(spawn_laternfish(starting_fish, days=80))
    print(spawn_laternfish(starting_fish, days=256))
