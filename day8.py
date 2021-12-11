from collections import defaultdict

segment_to_numbers = {
    frozenset('abcefg'): 0,
    frozenset('cf'): 1,
    frozenset('acdeg'): 2,
    frozenset('acdfg'): 3,
    frozenset('bcdf'): 4,
    frozenset('abdfg'): 5,
    frozenset('abdefg'): 6,
    frozenset('acf'): 7,
    frozenset('abcdefg'): 8,
    frozenset('abcdfg'): 9,
}

segment_count_to_numbers = defaultdict(list)
for segments, number in segment_to_numbers.items():
    segment_count_to_numbers[len(segments)].append(number)


def parse_input(input):
    signal_patterns = []
    output_values = []

    for line in input:
        signal_patterns_string, output_value_string = line.strip().split(' | ')
        signal_patterns.append([
            frozenset(pattern) for pattern in
            signal_patterns_string.split(' ')
        ])
        output_values.append([
            frozenset(value) for value in
            output_value_string.split(' ')
        ])

    return signal_patterns, output_values


def decode_all(signal_patterns, output_values, decoder):
    total_count = 0
    for i in range(0, len(signal_patterns)):
        output = decoder(signal_patterns[i], output_values[i])
        total_count += output

    return total_count


def naive_decode(signal_patterns, output_value):
    decoded_patterns = {}
    decoded = []
    for pattern in signal_patterns:
        numbers = segment_count_to_numbers.get(len(pattern), [])
        if len(numbers) == 1:
            decoded_patterns[pattern] = numbers[0]

    count = 0
    for pattern in output_value:
        if pattern in decoded_patterns:
            count += 1
            decoded.append(decoded_patterns[pattern])

    return len(decoded)


def full_decode(signal_patterns, output_value):
    signal_wire_mapping = {}

    decoded_patterns = {
        0: None,
        1: next(filter(lambda p: len(p) == 2, signal_patterns)),
        2: None,
        3: None,
        4: next(filter(lambda p: len(p) == 4, signal_patterns)),
        5: None,
        6: None,
        7: next(filter(lambda p: len(p) == 3, signal_patterns)),
        8: next(filter(lambda p: len(p) == 7, signal_patterns)),
        9: None,
    }

    one_four_seven_segments = decoded_patterns[1] | decoded_patterns[4] | decoded_patterns[7]
    signal_wire_mapping['a'] = list(decoded_patterns[7] - decoded_patterns[1])[0]

    for pattern in signal_patterns:
        if len(pattern - one_four_seven_segments) == 1:
            signal_wire_mapping['g'] = list(pattern - one_four_seven_segments)[0]
            break

    one_four_seven_and_g_segments = one_four_seven_segments | set(signal_wire_mapping['g'])
    for pattern in signal_patterns:
        if len(pattern) == 5 and len(pattern - one_four_seven_and_g_segments) == 1:
            signal_wire_mapping['e'] = list(pattern - one_four_seven_and_g_segments)[0]
            decoded_patterns[2] = pattern
            break

    for pattern in signal_patterns:
        if len(pattern) == 5 and len(pattern - decoded_patterns[2]) == 1:
            signal_wire_mapping['f'] = list(pattern - decoded_patterns[2])[0]
            decoded_patterns[3] = pattern
            break

    signal_wire_mapping['c'] = list(decoded_patterns[1] - set(signal_wire_mapping['f']))[0]
    signal_wire_mapping['d'] = list(decoded_patterns[3] - (decoded_patterns[1] | decoded_patterns[7] | set(signal_wire_mapping['g'])))[0]
    signal_wire_mapping['b'] = list(decoded_patterns[8] - (decoded_patterns[2] | decoded_patterns[3]))[0]

    reverse_signal_wire_mapping = {}
    for actual, wrong in signal_wire_mapping.items():
        reverse_signal_wire_mapping[wrong] = actual

    crosswired_mapping = {}
    # Ensure all the decoded patterns are known
    for pattern in signal_patterns:
        actual = []
        for char in pattern:
            actual.append(reverse_signal_wire_mapping[char])

        crosswired_mapping[pattern] = segment_to_numbers[frozenset(actual)]

    return int(''.join([str(crosswired_mapping[value]) for value in output_value]))


if __name__ == '__main__':
    with open('day8.txt') as infile:
        signal_patterns, output_values = parse_input(infile.readlines())

    print(decode_all(signal_patterns, output_values, naive_decode))
    print(decode_all(signal_patterns, output_values, full_decode))
