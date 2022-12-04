def _get_section_range(section) -> set:
    start, end = section.split('-')
    start = int(start)
    end = int(end)

    return {i for i in range(start, end + 1)}


def get_sections(input: list[str]) -> list[tuple[set, set]]:
    sections = []
    for line in input:
        one, two = line.strip().split(',')
        sections.append((_get_section_range(one), _get_section_range(two)))

    return sections


def do_sections_overlap(section_pair: tuple[set, set]) -> bool:
    first, second = section_pair
    return len(first & second) > 0


def are_sections_contained(section_pair: tuple[set, set]) -> bool:
    first, second = section_pair
    return first & second == second or first & second == first


def count_overlaps(sections: list[tuple[set, set]]) -> int:
    return sum(1 for section_pair in sections if do_sections_overlap(section_pair))


def count_contains(sections: list[tuple[set, set]]) -> int:
    return sum(1 for section_pair in sections if are_sections_contained(section_pair))


if __name__ == "__main__":
    with open("day4.txt") as infile:
        sections = get_sections(infile.readlines())

    print(count_contains(sections))
    print(count_overlaps(sections))
