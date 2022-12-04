import math


def syntax_check(lines):
    syntax_score = 0
    syntax_scoring = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137
    }
    autocomplete_scores = []
    autocomplete_scoring = {
        '(': 1,
        '[': 2,
        '{': 3,
        '<': 4
    }
    pairs = {
        ')': '(',
        ']': '[',
        '}': '{',
        '>': '<',
    }

    opening_characters = {character for character in pairs.values()}
    closing_characters = {character for character in pairs.keys()}

    for line in lines:
        open = []
        syntax_error = False

        for character in line:
            if character in opening_characters:
                open.append(character)
            elif character in closing_characters:
                last_open = open.pop()
                if last_open != pairs[character]:
                    syntax_score += syntax_scoring[character]
                    syntax_error = True
                    break

        if not syntax_error:
            line_score = 0
            for character in open[::-1]:
                line_score *= 5
                line_score += autocomplete_scoring[character]
            autocomplete_scores.append(line_score)

    middle_index = math.floor(len(autocomplete_scores) / 2)
    middle_score = sorted(autocomplete_scores)[middle_index]

    return syntax_score, middle_score


if __name__ == '__main__':
    with open('day10.txt') as infile:
        lines = infile.readlines()

    print(syntax_check(lines))
