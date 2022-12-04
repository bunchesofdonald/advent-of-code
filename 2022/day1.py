def get_calorie_counts(data: list[str]) -> list[int]:
    counts = []
    calories_in_bag = 0
    for line in data:
        try:
            calories = int(line)
        except ValueError:
            # The line wasn't an integer, the current elf's calorie count must
            # be done.
            counts.append(calories_in_bag)
            calories_in_bag = 0
        else:
            # The line was an integer so add it to the current calorie count
            # in the bag.
            calories_in_bag += calories

    return counts


def sum_top_n_calorie_counts(calorie_counts: list[int], n: int) -> int:
    return sum(sorted(calorie_counts, reverse=True)[:n])


if __name__ == '__main__':
    with open("day1.txt") as infile:
        calorie_counts = get_calorie_counts(infile.readlines())

    print(sum_top_n_calorie_counts(calorie_counts, n=1))
    print(sum_top_n_calorie_counts(calorie_counts, n=3))
