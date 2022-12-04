from collections import defaultdict


def parse_input(input):
    graph = defaultdict(list)
    for line in input:
        start, end = line.strip().split('-')
        graph[start].append(end)
        graph[end].append(start)

    return graph


def find_all_paths(graph, start, end, path=[]):
    path = path.copy() + [start]
    if start == end:
        return [path]

    paths = []
    for node in graph[start]:
        if node not in path or node == node.upper():
            paths += find_all_paths(graph, node, end, path)

    return paths


def find_all_paths_special(graph, start, end, path=[]):
    path = path.copy() + [start]
    if start == end:
        return [path]

    visited_lower_cased = defaultdict(int)
    for visited in path:
        if visited == visited.lower():
            visited_lower_cased[visited] += 1

    paths = []
    for node in graph[start]:
        can_traverse_node = (
            (
                node in path
                and node not in ['start', 'end']
                and node.lower() == node
                and max(visited_lower_cased.values()) < 2
            )
            or node not in path
            or node == node.upper()
        )
        if can_traverse_node:
            paths += find_all_paths_special(graph, node, end, path)

    return paths


if __name__ == '__main__':
    with open('day12.txt') as infile:
        graph = parse_input(infile.readlines())

    paths = find_all_paths(graph, 'start', 'end')
    print(len(paths))

    paths = find_all_paths_special(graph, 'start', 'end')
    print(len(paths))
