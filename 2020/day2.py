from collections import defaultdict


def is_valid_password(min_count, max_count, required, password):
    counts = defaultdict(int)
    for char in password:
        counts[char] += 1

    return counts[required] >= int(min_count) and counts[required] <= int(max_count)


def valid_toboggan_password(one, two, required, password):
    pos_1 = password[int(one) - 1]
    pos_2 = password[int(two) - 1]

    return (
        (pos_1 == required and pos_2 != required)
        or (pos_2 == required and pos_1 != required)
    )


if __name__ == '__main__':
    sled_valid = 0
    toboggan_valid = 0
    with open('day2.txt') as infile:
        for line in infile.readlines():
            parts = line.strip().split(' ')
            min_count, max_count = parts[0].split('-')
            required = parts[1][0]
            password = parts[2]

            if is_valid_password(min_count, max_count, required, password):
                sled_valid += 1

            if valid_toboggan_password(min_count, max_count, required, password):
                toboggan_valid += 1

    print(sled_valid)
    print(toboggan_valid)
