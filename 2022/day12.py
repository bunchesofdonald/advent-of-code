import string
import heapq
import math

Point = tuple[int, int]
Graph = dict[Point, int]


def read_graph(input: list[str]) -> tuple[Graph, Point, Point]:
    graph: dict[Point, int] = {}
    start = None
    end = None

    lines = [line.strip() for line in input]

    for y in range(len(lines)):
        for x in range(len(lines[0])):
            if lines[y][x] == "S":
                start = (x, y)
                terrain = string.ascii_lowercase.index("a")
            elif lines[y][x] == "E":
                end = (x, y)
                terrain = string.ascii_lowercase.index("z")
            else:
                terrain = string.ascii_lowercase.index(lines[y][x])
            graph[(x, y)] = terrain

    assert start
    assert end

    return graph, start, end


def adjacent_points(graph: Graph, point: Point) -> list[Point]:
    x, y = point
    points = [
        (x - 1, y),
        (x + 1, y),
        (x, y - 1),
        (x, y + 1),
    ]

    return [p for p in points if p in graph]


def gentle_path(graph: Graph, start: Point, end: Point) -> float:
    unvisited = set(graph.keys())
    distances = {point: math.inf for point in unvisited}
    distances[start] = 0
    frontier = [(distances[start], start)]
    heapq.heapify(frontier)

    while frontier:
        _, current_node = heapq.heappop(frontier)
        neighbors = adjacent_points(graph, current_node)

        for neighbor in neighbors:
            if neighbor in unvisited:
                if graph[neighbor] - graph[current_node] <= 1:
                    new_distance = distances[current_node] + 1
                else:
                    continue

                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    heapq.heappush(frontier, (new_distance, neighbor))

        unvisited.remove(current_node)

    return distances[end]


def shortest_gentle_path(graph: Graph, end: Point) -> float:
    starting_points = [point for point, value in graph.items() if value == 0]
    path_lengths = []
    for start in starting_points:
        path_lengths.append(gentle_path(graph, start, end))

    return min(path_lengths)


if __name__ == "__main__":
    with open("day12.txt") as infile:
        graph, start, end = read_graph(infile.readlines())

    print(gentle_path(graph, start, end))
    print(shortest_gentle_path(graph, end))
