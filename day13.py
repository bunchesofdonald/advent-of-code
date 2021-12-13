from collections import defaultdict
import re


def parse_input(input):
    dots = []
    folds = []

    for line in input:
        line = line.strip()
        if match := re.match(r'(\d+),(\d+)', line):
            x, y = match.groups()
            dots.append((int(x), int(y)))
        elif match := re.match(r'fold along ([xy])=(\d+)', line):
            axis, number = match.groups()
            direction = 'up' if axis == 'y' else 'left'
            folds.append((direction, int(number)))

    return dots, folds


def draw_dots(dots):
    paper = []
    max_x = max(x for x, _ in dots) + 1
    max_y = max(y for _, y in dots) + 1

    for _ in range(max_y):
        paper.append(['.' for _ in range(max_x)])

    for x, y in dots:
        paper[y][x] = '#'

    return paper


def fold_left(paper, line):
    folded_paper = []
    for y in range(len(paper)):
        folded_paper.insert(y, [])
        for x in range(line):
            sibling_column = len(paper[0]) - (x + 1)
            if paper[y][sibling_column] == '#' or paper[y][x] == '#':
                value = '#'
            else:
                value = '.'

            folded_paper[y].append(value)

    return folded_paper


def fold_up(paper, line):
    folded_paper = []

    for y in range(len(paper[:line])):
        folded_paper.insert(y, [])
        for x in range(len(paper[y])):
            sibling_row = len(paper) - (y + 1)
            if paper[sibling_row][x] == '#' or paper[y][x] == '#':
                value = '#'
            else:
                value = '.'

            folded_paper[y].append(value)

    return folded_paper


def fold_paper(paper, folds):
    for direction, number in folds:
        match direction:
            case 'up':
                paper = fold_up(paper, number)
            case 'left':
                paper = fold_left(paper, number)

    return paper


if __name__ == '__main__':
    with open('day13.txt') as infile:
        dots, folds = parse_input(infile.readlines())

    paper = draw_dots(dots)
    folded_paper = fold_paper(paper, folds[:1])
    counts = defaultdict(int)
    for row in folded_paper:
        for col in row:
            counts[col] += 1

    folded_paper = fold_paper(paper, folds)
    for row in folded_paper:
        print(''.join(row))
