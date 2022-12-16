from day15 import Sensor, coverage_at_row, read_sensors, find_uncovered_point

puzzle_input = """Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3""".split(
    "\n"
)


def test_read_sensors():
    assert read_sensors(puzzle_input) == [
        Sensor(location=(2, 18), nearest_beacon=(-2, 15)),
        Sensor(location=(9, 16), nearest_beacon=(10, 16)),
        Sensor(location=(13, 2), nearest_beacon=(15, 3)),
        Sensor(location=(12, 14), nearest_beacon=(10, 16)),
        Sensor(location=(10, 20), nearest_beacon=(10, 16)),
        Sensor(location=(14, 17), nearest_beacon=(10, 16)),
        Sensor(location=(8, 7), nearest_beacon=(2, 10)),
        Sensor(location=(2, 0), nearest_beacon=(2, 10)),
        Sensor(location=(0, 11), nearest_beacon=(2, 10)),
        Sensor(location=(20, 14), nearest_beacon=(25, 17)),
        Sensor(location=(17, 20), nearest_beacon=(21, 22)),
        Sensor(location=(16, 7), nearest_beacon=(15, 3)),
        Sensor(location=(14, 3), nearest_beacon=(15, 3)),
        Sensor(location=(20, 1), nearest_beacon=(15, 3)),
    ]


def test_coverage_at_row():
    sensors = read_sensors(puzzle_input)
    assert coverage_at_row(sensors, 10) == 26


def test_find_uncovered_point():
    sensors = read_sensors(puzzle_input)
    assert find_uncovered_point(sensors, 0, 20) == (14, 11)
