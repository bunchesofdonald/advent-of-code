import re
from dataclasses import dataclass


Point = tuple[int, int]


def manhattan_distance(point1: Point, point2: Point) -> int:
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])


@dataclass
class Sensor:
    location: Point
    nearest_beacon: Point

    def distance_to_beacon(self) -> int:
        if not hasattr(self, "_distance"):
            self._distance = manhattan_distance(self.location, self.nearest_beacon)
        return self._distance

    def in_range(self, point: Point):
        return manhattan_distance(self.location, point) <= self.distance_to_beacon()

    def border_points(self) -> set[Point]:
        dist = self.distance_to_beacon() + 1

        points = {
            # Center line
            (self.location[0] - dist, self.location[1]),
            (self.location[0] + dist, self.location[1]),
        }

        # Top triangle
        for y_dist_from_sensor in range(dist - 1, 0, -1):
            extent = dist - y_dist_from_sensor
            points.add(
                (self.location[0] - extent, self.location[1] - y_dist_from_sensor)
            )
            points.add(
                (self.location[0] + extent, self.location[1] - y_dist_from_sensor)
            )

        # Bottom triangle
        for y_dist_from_sensor in range(0, dist + 1):
            extent = dist - y_dist_from_sensor
            points.add(
                (self.location[0] - extent, self.location[1] + y_dist_from_sensor)
            )
            points.add(
                (self.location[0] + extent, self.location[1] + y_dist_from_sensor)
            )

        return points


def read_sensors(input: list[str]) -> list[Sensor]:
    sensors = []
    for line in input:
        match = re.search(
            r"x=(?P<sensor_x>-?\d+), y=(?P<sensor_y>-?\d+):.+x=(?P<beacon_x>-?\d+), y=(?P<beacon_y>-?\d+)",
            line,
        )
        point_data = match.groupdict()
        sensors.append(
            Sensor(
                location=(int(point_data["sensor_x"]), int(point_data["sensor_y"])),
                nearest_beacon=(
                    int(point_data["beacon_x"]),
                    int(point_data["beacon_y"]),
                ),
            )
        )

    return sensors


def coverage_at_row(sensors: list[Sensor], row) -> int:
    min_x = min(
        [sensor.location[0] - sensor.distance_to_beacon() for sensor in sensors]
    )
    max_x = max(
        [sensor.location[0] + sensor.distance_to_beacon() for sensor in sensors]
    )
    beacons_in_row = len(
        {sensor.nearest_beacon for sensor in sensors if sensor.nearest_beacon[1] == row}
    )

    count = 0
    for x in range(min_x, max_x + 1):
        for sensor in sensors:
            if sensor.in_range((x, row)):
                count += 1
                break

    return count - beacons_in_row


def find_uncovered_point(sensors, min_cord, max_cord) -> Point:
    checked_points = 0
    points_to_check = set()

    def in_bounds(point: Point):
        return not (
            point[0] < min_cord
            or point[0] > max_cord
            or point[1] < min_cord
            or point[1] > max_cord
        )

    print("Getting list of points to check...")
    for sensor in sensors:
        for point in sensor.border_points():
            if in_bounds(point):
                points_to_check.add(point)

    print("Checking for point not in range...")
    for point in points_to_check:
        in_range = False
        for sensor in sensors:
            if sensor.in_range(point):
                in_range = True
                break

        checked_points += 1

        if not in_range:
            return point


if __name__ == "__main__":
    with open("day15.txt") as infile:
        sensors = read_sensors(infile.readlines())

    print(coverage_at_row(sensors, row=2_000_000))

    uncovered = find_uncovered_point(sensors, 0, 4_000_000)
    print((uncovered[0] * 4_000_000) + uncovered[1])
