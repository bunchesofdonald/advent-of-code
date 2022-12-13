from day13 import compare_pairs, get_indice_sum, read_packet_data

puzzle_input = """[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]""".split(
    "\n"
)


def test_read_packet_data():
    assert read_packet_data(puzzle_input) == [
        [1, 1, 3, 1, 1],
        [1, 1, 5, 1, 1],
        [[1], [2, 3, 4]],
        [[1], 4],
        [9],
        [[8, 7, 6]],
        [[4, 4], 4, 4],
        [[4, 4], 4, 4, 4],
        [7, 7, 7, 7],
        [7, 7, 7],
        [],
        [3],
        [[[]]],
        [[]],
        [1, [2, [3, [4, [5, 6, 7]]]], 8, 9],
        [1, [2, [3, [4, [5, 6, 0]]]], 8, 9],
    ]


def test_compare_pairs():
    pairs = read_packet_data(puzzle_input)

    assert compare_pairs(pairs[0], pairs[1]) == -1
    assert compare_pairs(pairs[2], pairs[3]) == -1
    assert compare_pairs(pairs[4], pairs[5]) == 1
    assert compare_pairs(pairs[6], pairs[7]) == -1
    assert compare_pairs(pairs[8], pairs[9]) == 1
    assert compare_pairs(pairs[10], pairs[11]) == -1
    assert compare_pairs(pairs[12], pairs[13]) == 1
    assert compare_pairs(pairs[14], pairs[15]) == 1


def test_get_indice_sum():
    packet_data = read_packet_data(puzzle_input)
    assert get_indice_sum(packet_data) == 13
