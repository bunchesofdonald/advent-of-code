from functools import cmp_to_key
import json


def read_packet_data(input: list[str]) -> list:
    return [json.loads(line.strip()) for line in input if line.strip()]


def compare_pairs(first, second) -> int:
    if isinstance(first, int) and isinstance(second, int):
        if first == second:
            return 0
        elif first < second:
            return -1
        else:
            return 1
    elif isinstance(first, int) and isinstance(second, list):
        return compare_pairs([first], second)
    elif isinstance(first, list) and isinstance(second, int):
        return compare_pairs(first, [second])
    elif isinstance(first, list) and isinstance(second, list):
        if first and second:
            result = compare_pairs(first[0], second[0])
            if result == 0:
                return compare_pairs(first[1:], second[1:])
            else:
                return result
        elif first and not second:
            return 1
        elif not first and not second:
            return 0
        else:
            return -1


def get_indice_sum(packet_data: list) -> int:
    indice_sum = 0
    for pair_i, i in enumerate(range(0, len(packet_data), 2), start=1):
        if compare_pairs(packet_data[i], packet_data[i + 1]) == -1:
            indice_sum += pair_i

    return indice_sum


if __name__ == "__main__":
    with open("day13.txt") as infile:
        packet_data = read_packet_data(infile.readlines())

    print(get_indice_sum(packet_data))

    dividers = [
        [[2]],
        [[6]],
    ]

    packet_data += dividers
    packet_data.sort(key=cmp_to_key(compare_pairs))
    print((packet_data.index(dividers[0]) + 1) * (packet_data.index(dividers[1]) + 1))
