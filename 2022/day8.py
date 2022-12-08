import functools

Forest = list[list[int]]


def read_topographical_map(input: list[str]) -> Forest:
    topographical_map = []
    for line in input:
        line = line.strip()
        topographical_map.append([int(height) for height in line])

    return topographical_map


def visible_tree_count(forest: Forest) -> int:
    edge_count = (len(forest) + len(forest[0])) * 2 - 4
    interior_count = 0

    for y in range(1, len(forest) - 1):
        for x in range(1, len(forest[y]) - 1):
            if is_tree_visible(x, y, forest):
                interior_count += 1

    return edge_count + interior_count


def is_tree_visible(x: int, y: int, forest: Forest) -> bool:
    considered_tree = forest[y][x]
    views = views_from_tree(x, y, forest)
    return any([considered_tree > max(view) for view in views])


def best_scenic_score(forest: Forest) -> int:
    scores = []
    for y in range(len(forest)):
        for x in range(len(forest[y])):
            scores.append(tree_scenic_score(x, y, forest))

    return max(scores)


def tree_scenic_score(x: int, y: int, forest: Forest) -> int:
    counts = []

    considered_tree = forest[y][x]
    views = views_from_tree(x, y, forest)

    for view in views:
        view_count = 0
        for tree in view:
            view_count += 1
            if considered_tree <= tree:
                break

        counts.append(view_count)

    return functools.reduce(lambda x, y: x * y, counts, 1)


def views_from_tree(x: int, y: int, forest: Forest) -> list[list[int]]:
    forest_height = len(forest)
    forest_width = len(forest[0])

    to_top = [forest[i][x] for i in range(0, y)][::-1]
    to_bottom = [forest[i][x] for i in range(y + 1, forest_height)]
    to_left = [forest[y][i] for i in range(0, x)][::-1]
    to_right = [forest[y][i] for i in range(x + 1, forest_width)]

    return [to_top, to_bottom, to_left, to_right]


if __name__ == "__main__":
    with open("day8.txt") as infile:
        forest = read_topographical_map(infile.readlines())

    print(visible_tree_count(forest))
    print(best_scenic_score(forest))
