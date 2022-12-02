import pytest

from day_2 import calculate_hand
from day_2 import calculate_outcome
from day_2 import calculate_total_score
from day_2 import rewrite_outcomes_to_hands


@pytest.mark.parametrize("hand,score", [("X", 1), ("Y", 2), ("Z", 3)])
def test_calculate_hand(hand, score):
    assert calculate_hand(hand) == score


@pytest.mark.parametrize(
    "opp,me,score",
    [
        ("A", "X", 3),
        ("B", "Y", 3),
        ("C", "Z", 3),
        ("A", "Y", 6),
        ("B", "Z", 6),
        ("C", "X", 6),
        ("A", "Z", 0),
        ("B", "X", 0),
        ("C", "Y", 0),
    ],
)
def test_calculate_outcome(opp, me, score):
    assert calculate_outcome(opp, me) == score


@pytest.mark.parametrize(
    "opp,outcome,mine",
    [
        ("A", "X", "Z"),
        ("A", "Y", "X"),
        ("A", "Z", "Y"),
        ("B", "X", "X"),
        ("B", "Y", "Y"),
        ("B", "Z", "Z"),
        ("C", "X", "Y"),
        ("C", "Y", "Z"),
        ("C", "Z", "X"),
    ],
)
def test_rewrite_outcomes_to_hands(opp, outcome, mine):
    text = f"{opp} {outcome}"
    expected = f"{opp} {mine}"
    assert rewrite_outcomes_to_hands(text) == expected
