from day_8.solution import get_scenic_score
from day_8.solution import get_view_distances


def test_get_view_distances():
    inp = [
        [1, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 2, 1, 1],
        [1, 1, 1, 1]
    ]
    expected = {
        "n": 2,
        "s": 1,
        "e": 2,
        "w": 1
    }
    got = get_view_distances(inp, 1, 2)
    assert got == expected


def test_get_scenic_score():
    inp = [
        [1, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 2, 1, 1],
        [1, 1, 1, 1]
    ]
    expected = 4
    got = get_scenic_score(inp, 1, 2)
    assert got == expected

