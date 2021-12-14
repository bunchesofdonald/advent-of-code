from collections import Counter


def parse_input(input):
    template = input[0].strip()
    rules = {}
    for line in input[2:]:
        pair, element = line.strip().split(' -> ')
        rules[pair] = element

    return template, rules


def get_pairs(polymer):
    for pair in zip(*[polymer[i:] for i in range(2)]):
        yield ''.join(pair)


def polymer_element_count(template, rules, steps=10):
    pairs = Counter(pair for pair in get_pairs(template))
    chars = Counter(template)

    for _ in range(steps):
        new_pairs = Counter()
        for pair, count in list(pairs.items()):
            if pair in rules:
                element = rules[pair]
                new_pairs[f'{pair[0]}{element}'] += count
                new_pairs[f'{element}{pair[1]}'] += count
                chars[element] += count

        pairs = new_pairs

    return max(chars.values()) - min(chars.values())


if __name__ == '__main__':
    with open('day14.txt') as infile:
        template, rules = parse_input(infile.readlines())

    print(polymer_element_count(template, rules, steps=10))
    print(polymer_element_count(template, rules, steps=40))
