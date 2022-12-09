from day_8.solution import get_scenic_score


def test_get_scenic_score():
    inp = [
        [1, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 2, 1, 1],
        [1, 1, 1, 1]
    ]
    expected = 8
    assert get_scenic_score(inp, 1, 2) == expected

