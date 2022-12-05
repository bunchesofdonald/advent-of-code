from day5 import do_procedures, read_crates_and_procedures

puzzle_input = """    [D]
[N] [C]
[Z] [M] [P]
 1   2   3

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2""".split('\n')


def test_read_crates_and_procedures():
    crates, procedures = read_crates_and_procedures(puzzle_input)
    assert crates == [
        ['N', 'Z', ],
        ['D', 'C', 'M', ],
        ['P', ]
    ]

    assert procedures == [
        (1, 1, 0),
        (3, 0, 2),
        (2, 1, 0),
        (1, 0, 1),
    ]


def test_do_procedures():
    crates, procedures = read_crates_and_procedures(puzzle_input)
    print(crates)
    crates = do_procedures(crates, procedures)
    print(crates)
    assert crates == [
        ['C'],
        ['M'],
        ['Z', 'N', 'D', 'P']
    ]

def test_do_procedures_9001():
    crates, procedures = read_crates_and_procedures(puzzle_input)
    crates = do_procedures(crates, procedures, mode=9001)
    assert crates == [
        ['M'],
        ['C'],
        ['D', 'N', 'Z', 'P']
    ]