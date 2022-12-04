from day4 import count_contains, count_overlaps, do_sections_overlap, get_sections

puzzle_input = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8""".split('\n')


def test_get_sections():
    assert get_sections(puzzle_input) == [
        ({2, 3, 4}, {6, 7, 8}),
        ({2, 3}, {4, 5}),
        ({5, 6, 7}, {7, 8, 9}),
        ({2, 3, 4, 5, 6, 7, 8}, {3, 4, 5, 6, 7}),
        ({6}, {4, 5, 6}),
        ({2, 3, 4, 5, 6}, {4, 5, 6, 7, 8}),
    ]

def test_count_overlaps():
    sections = get_sections(puzzle_input)
    assert count_overlaps(sections) == 4

def test_count_contains():
    sections = get_sections(puzzle_input)
    assert count_contains(sections) == 2