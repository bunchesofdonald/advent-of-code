import math


PLANE_ROWS = 127
PLANE_COLS = 7


def get_seat_id(encoded):
    encoded_row = encoded[:7]
    encoded_col = encoded[-3:]

    row = partition(0, PLANE_ROWS, encoded_row)
    col = partition(0, PLANE_COLS, encoded_col)

    return row * 8 + col


def partition(lower_max, upper_max, steps):
    for step in steps:
        if step == 'F' or step == 'L':
            upper_max = lower_max + math.floor((upper_max - lower_max) / 2)
        else:
            lower_max = math.ceil((upper_max + lower_max) / 2)

    return lower_max


def find_the_gap(seat_ids):
    seat_ids = sorted(seat_ids)
    expected = seat_ids[0] + 1
    for seat in seat_ids[1:]:
        if seat != expected:
            return expected

        expected = seat + 1


if __name__ == '__main__':
    with open('day5.txt') as infile:
        seat_ids = [
            get_seat_id(line.strip())
            for line in infile.readlines()
        ]

    print(find_the_gap(seat_ids))
