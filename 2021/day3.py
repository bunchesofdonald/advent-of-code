def inverse_binary(binary):
    return ''.join(
        [
            '0' if char == '1' else '1'
            for char in binary
        ]
    )


def most_common_binary(report):
    first = report[0]
    most_common = []

    for index in range(len(first)):
        characters_at_index = [
            line[index] for line in report
        ]

        ones_count = characters_at_index.count('1')
        zeros_count = characters_at_index.count('0')

        most_common.append('0' if zeros_count > ones_count else '1')

    return ''.join(most_common)


def power_consumption(report):
    most_common = most_common_binary(report)
    gamma_rate = int(''.join(most_common), 2)
    epsilon_rate = int(''.join(inverse_binary(most_common)), 2)

    return gamma_rate * epsilon_rate


def life_support_rating(report):
    first = report[0]

    generator_report = report.copy()

    for index in range(len(first)):
        characters_at_index = [
            line[index] for line in generator_report
        ]

        ones_count = characters_at_index.count('1')
        zeros_count = characters_at_index.count('0')

        if zeros_count > ones_count:
            generator_report = [
                line for line in generator_report
                if line[index] == '0'
            ]
        else:
            generator_report = [
                line for line in generator_report
                if line[index] == '1'
            ]

        if len(generator_report) == 1:
            break

    scrubber_report = set(report.copy())
    for index in range(len(first)):
        characters_at_index = [
            line[index] for line in scrubber_report
        ]

        ones_count = characters_at_index.count('1')
        zeros_count = characters_at_index.count('0')

        if ones_count < zeros_count:
            scrubber_report = [
                line for line in scrubber_report
                if line[index] == '1'
            ]
        else:
            scrubber_report = [
                line for line in scrubber_report
                if line[index] == '0'
            ]

        if len(scrubber_report) == 1:
            break

    generator_rating = int(generator_report[0], 2)
    scrubber_rating = int(scrubber_report[0], 2)

    return generator_rating * scrubber_rating


if __name__ == '__main__':
    with open('day3.txt') as infile:
        report = [
            line.strip() for line in
            infile.readlines()
        ]

    print(power_consumption(report))
    print(life_support_rating(report))
