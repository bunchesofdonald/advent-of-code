from day6 import find_marker_of_length

puzzle_input = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"

def test_find_start_of_packet_maker():
    assert find_marker_of_length(puzzle_input, n=4) == 7
    assert find_marker_of_length(puzzle_input, n=14) == 19