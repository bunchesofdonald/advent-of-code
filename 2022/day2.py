import enum

class Move:
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


def read_strategy_guide(input):
    mapping = {
        'A': Move.ROCK,
        'B': Move.PAPER,
        'C': Move.SCISSORS,
        'X': Move.ROCK,
        'Y': Move.PAPER,
        'Z': Move.SCISSORS
    }

    guide = []
    for line in input:
        if line:
            them, you = line.strip().split(' ')
            guide.append({'them': mapping[them], 'you': mapping[you]})

    return guide


def improved_strategy_guide(input):
    mapping = {
        'A': Move.ROCK,
        'B': Move.PAPER,
        'C': Move.SCISSORS,
    }

    guide = []
    for line in input:
        if line:
            them, you = line.strip().split(' ')
            them = mapping[them]

            if you == 'X':  # Lose
                if them == Move.ROCK:
                    your_move = Move.SCISSORS
                elif them == Move.PAPER:
                    your_move = Move.ROCK
                elif them == Move.SCISSORS:
                    your_move = Move.PAPER
            elif you == 'Y':  # Draw
                if them == Move.ROCK:
                    your_move = Move.ROCK
                elif them == Move.PAPER:
                    your_move = Move.PAPER
                elif them == Move.SCISSORS:
                    your_move = Move.SCISSORS
            elif you == 'Z':  # Win
                if them == Move.ROCK:
                    your_move = Move.PAPER
                elif them == Move.PAPER:
                    your_move = Move.SCISSORS
                elif them == Move.SCISSORS:
                    your_move = Move.ROCK


            guide.append({'them': them, 'you': your_move})

    return guide


def win_lose_or_draw(them: Move, you: Move) -> int:
    if them == Move.ROCK:
        if you == Move.ROCK:
            return 3
        elif you == Move.PAPER:
            return 6
        elif you == Move.SCISSORS:
            return 0
    elif them == Move.PAPER:
        if you == Move.ROCK:
            return 0
        elif you == Move.PAPER:
            return 3
        elif you == Move.SCISSORS:
            return 6
    elif them == Move.SCISSORS:
        if you == Move.ROCK:
            return 6
        elif you == Move.PAPER:
            return 0
        elif you == Move.SCISSORS:
            return 3

def score_strategy_guide(guide):
    score = 0
    for round in guide:
        score += win_lose_or_draw(**round)
        score += round['you']

    return score


if __name__ == '__main__':
    with open("day2.txt") as infile:
        lines = infile.readlines()

    guide = read_strategy_guide(lines)
    improved = improved_strategy_guide(lines)

    print(score_strategy_guide(guide))
    print(score_strategy_guide(improved))
