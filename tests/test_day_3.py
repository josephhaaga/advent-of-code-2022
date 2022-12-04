import pytest

from day_3.solution import split_knapsack
from day_3.solution import calculate_priority


@pytest.mark.parametrize('knapsack, pockets', [
    ("abcd", ("ab", "cd")),
    ("xx", ("x", "x"))
])
def test_split_knapsack(knapsack, pockets):
    assert split_knapsack(knapsack) == pockets


@pytest.mark.parametrize('item, priority', [
    ('a', 1),
    ('z', 26),
    ('A', 27),
    ('Z', 52),
])
def test_calculate_priority(item, priority):
    assert calculate_priority(item) == priority


