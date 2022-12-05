import pytest
import tempfile

from day_5.solution import parse_input
from day_5.solution import run_instructions
from day_5.solution import run_instructions_cratemover_9001
from day_5.solution import get_items_on_top_of_each_stack

@pytest.fixture
def input_file():
    with tempfile.NamedTemporaryFile() as f:
        with open(f.name, 'w') as z:
            z.writelines(
                [
                    "    [C]    \n",
                    "[F] [M] [Z]\n",
                    "[R] [H] [M]\n",
                    "[W] [T] [P]\n",
                    " 1   2   3 \n",
                    "\n",
                    "move 2 from 1 to 3\n",
                    "move 1 from 1 to 2\n",
                ]
            )
        yield f.name


def test_parse_input(input_file):
    assert parse_input(input_file) == (
        [
            ["W", "R", "F"],
            ["T", "H", "M", "C"],
            ["P", "M", "Z"],
        ],
        [
            (2, 1, 3),
            (1, 1, 2)
        ]
    )


def test_run_instructions():
    stacks = [
        ["W", "R", "F"],
        ["T", "H", "M", "C"],
        ["P", "M", "Z"],
    ]
    instructions = [
        (2, 1, 3),
        (1, 1, 2)
    ]
    expected = [
        [],
        ["T", "H", "M", "C", "W"],
        ["P", "M", "Z", "F", "R"],
    ]
    assert run_instructions(stacks, instructions) == expected


def test_run_instructions_cratemover_9001():
    stacks = [
        ["W", "R", "F"],
        ["T", "H", "M", "C"],
        ["P", "M", "Z"],
    ]
    instructions = [
        (2, 1, 3),
        (1, 1, 2)
    ]
    expected = [
        [],
        ["T", "H", "M", "C", "W"],
        ["P", "M", "Z", "R", "F"],
    ]
    assert run_instructions_cratemover_9001(stacks, instructions) == expected


def test_get_items_on_top_of_each_stack():
    assert get_items_on_top_of_each_stack([["A", "B", "C"], ["D", "E"]]) == "CE"

