from day3 import item_priority, parse_rucksacks, unique_item, unique_item_by_group

puzzle_input = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
""".split('\n')

def test_parse_rucksacks():
    assert [r.compartments for r in parse_rucksacks(puzzle_input)] == [
        ('vJrwpWtwJgWr', 'hcsFMMfFFhFp'),
        ('jqHRNqRjqzjGDLGL', 'rsFMfFZSrLrFZsSL'),
        ('PmmdzqPrV', 'vPwwTWBwg'),
        ('wMqvLMZHhHMvwLH', 'jbvcjnnSBnvTQFn'),
        ('ttgJtRGJ', 'QctTZtZT'),
        ('CrZsJsPPZsGz', 'wwsLwLmpwMDw'),
    ]


def test_unique_item():
    rucksacks = parse_rucksacks(puzzle_input)
    assert unique_item(rucksacks[0]) == 'p'
    assert unique_item(rucksacks[1]) == 'L'
    assert unique_item(rucksacks[2]) == 'P'
    assert unique_item(rucksacks[3]) == 'v'
    assert unique_item(rucksacks[4]) == 't'
    assert unique_item(rucksacks[5]) == 's'


def test_item_priority():
    assert item_priority('a') == 1
    assert item_priority('z') == 26
    assert item_priority('A') == 27
    assert item_priority('Z') == 52


def test_unique_item_by_group():
    rucksacks = parse_rucksacks(puzzle_input)
    assert unique_item_by_group(rucksacks) == ['r', 'Z']
