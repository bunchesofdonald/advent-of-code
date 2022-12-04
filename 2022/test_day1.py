from day1 import get_calorie_counts, sum_top_n_calorie_counts

puzzle_input = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
""".split('\n')


def test_get_calorie_counts():
    counts = get_calorie_counts(puzzle_input)
    assert counts == [6000, 4000, 11000, 24000, 10000]

def test_sum_top_n_calorie_counts():
    counts = get_calorie_counts(puzzle_input)
    assert sum_top_n_calorie_counts(counts, n=1) == 24000
    assert sum_top_n_calorie_counts(counts, n=3) == 45000
