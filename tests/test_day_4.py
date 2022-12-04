import pytest

from day_4.solution import does_fully_overlap

@pytest.mark.parametrize('a, b, fully_overlaps', [
    ((1, 3), (2, 2), True),
    ((1, 3), (4, 6), False),
    ((1, 3), (0, 4), True),
    ((0, 4), (1, 3), True),
    ((4, 6), (1, 3), False),
    ((1, 3), (2, 4), False),
    ((2, 4), (1, 3), False),
])
def test_does_fully_overlap(a, b, fully_overlaps):
    assert does_fully_overlap(a, b) == fully_overlaps

