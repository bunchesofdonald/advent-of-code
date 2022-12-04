if __name__ == '__main__':
    with open('day6.txt') as infile:
        groups = []
        group = []
        for line in infile.readlines():
            line = line.strip()
            if not line:
                groups.append(group)
                group = []
                continue

            group.append(set(line))

        groups.append(group)

    # Part 1
    count = 0
    for group in groups:
        result = set()
        for person in group:
            result.update(person)
        count += len(result)
    print(count)

    # Part 2
    count = 0
    for group in groups:
        result = set(group[0])
        for person in group[1:]:
            result = result.intersection(person)
        count += len(result)
    print(count)
