import math
import heapq
import utils


def parse_input(lines):
    graph = {}

    lines = [line.strip() for line in lines]
    height = len(lines)
    width = len(lines[0])

    for y in range(height):
        for x in range(width):
            graph[(x, y)] = int(lines[y][x])

    return graph, height, width


def expand_graph(graph, n, height, width):
    expanded = {}
    expanded_mapping = []
    for i in range(n):
        expanded_mapping.append([j + i for j in range(n)])

    for i in range(n):
        for j in range(n):
            for x, y in graph.keys():
                additive = expanded_mapping[i][j]
                new_value = graph[(x, y)] + additive
                if new_value > 9:
                    new_value -= 9

                new_x = x + (j * width)
                new_y = y + (i * height)
                expanded[(new_x, new_y)] = new_value

    return expanded, height * n, width * n


def lowest_risk_path(graph, height, width):
    start = (0, 0)
    unvisited = set(graph.keys())
    distances = {point: math.inf for point in unvisited}
    distances[start] = 0
    frontier = [(distances[start], start)]
    heapq.heapify(frontier)

    while frontier:
        _, current_node = heapq.heappop(frontier)
        neighbors = utils.adjacent_points(
            *current_node, height, width, include_diagonals=False)

        for neighbor in neighbors:
            if neighbor in unvisited:
                new_distance = distances[current_node] + graph[neighbor]
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    heapq.heappush(frontier, (new_distance, neighbor))

        unvisited.remove(current_node)

    return distances[(width - 1, height - 1)]


if __name__ == '__main__':
    with open('day15.txt') as infile:
        graph, height, width = parse_input(infile.readlines())

    print(lowest_risk_path(graph, height, width))

    expanded_graph, height, width = expand_graph(graph, 5, height, width)
    print(lowest_risk_path(expanded_graph, height, width))
