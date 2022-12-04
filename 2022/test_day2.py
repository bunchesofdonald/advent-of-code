from day2 import Move, improved_strategy_guide, read_strategy_guide, score_strategy_guide

puzzle_input = """A Y
B X
C Z
""".split('\n')

def test_read_strategy_guide():
    strategy_guide = read_strategy_guide(puzzle_input)
    assert strategy_guide == [
        {'them': Move.ROCK, 'you': Move.PAPER},
        {'them': Move.PAPER, 'you': Move.ROCK},
        {'them': Move.SCISSORS, 'you': Move.SCISSORS},
    ]

def test_improved_strategy_guide():
    strategy_guide = improved_strategy_guide(puzzle_input)
    assert strategy_guide == [
        {'them': Move.ROCK, 'you': Move.ROCK},
        {'them': Move.PAPER, 'you': Move.ROCK},
        {'them': Move.SCISSORS, 'you': Move.ROCK},
    ]


def test_score_strategy_guide():
    strategy_guide = read_strategy_guide(puzzle_input)
    assert score_strategy_guide(strategy_guide) == 15
