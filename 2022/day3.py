import string

item_priorities = list(string.ascii_letters)

Rucksack = tuple[str, str]


class Rucksack:
    def __init__(self, items: str):
        self.pivot = int(len(items) / 2)
        self.items = items

    @property
    def compartments(self) -> tuple[str, str]:
        return (self.items[:self.pivot], self.items[self.pivot:])

    @property
    def unique_items(self) -> set:
        return set(self.items)

def parse_rucksacks(input: list[str]) -> list[Rucksack]:
    rucksacks = []
    for line in input:
        line = line.strip()
        if not line:
            continue

        rucksacks.append(Rucksack(line))

    return rucksacks

def unique_item(rucksack: Rucksack) -> str:
    compartments = rucksack.compartments
    item = set(compartments[0]) & set(compartments[1])
    assert len(item) == 1
    return list(item)[0]


def item_priority(item: str) -> int:
    return item_priorities.index(item) + 1


def unique_item_by_group(rucksacks: list[Rucksack], group_size: int=3) -> list[str]:
    items = []
    for i in range(0, len(rucksacks), group_size):
        group = rucksacks[i:i + group_size]
        item = set.intersection(*[set(r.unique_items) for r in group])
        assert len(item) == 1
        items.append(list(item)[0])

    return items


if __name__ == "__main__":
    with open("day3.txt") as infile:
        rucksacks = parse_rucksacks(infile.readlines())

    unique_items = [unique_item(rucksack) for rucksack in rucksacks]
    priorities = [item_priority(item) for item in unique_items]
    print(sum(priorities))

    group_items = unique_item_by_group(rucksacks)
    group_priorities = [item_priority(item) for item in group_items]
    print(sum(group_priorities))
