from collections import namedtuple
import sys
from typing import List
from typing import Optional
from typing import Tuple


Move = namedtuple("Move", "x y")
Location = namedtuple("Location", "x y")


def get_board_size(instructions: str) -> int:
    return max([int(line.split(" ")[1]) for line in instructions.split("\n")[:-1]])


def print_board(board_size: int, head_location: Optional[HeadLocation] = None) -> None:
    for y_idx in range(board_size):
        for x_idx in range(board_size):
            print("." if (x_idx, y_idx) != head_location else "H", end=" ")
        print()


def update_location(
    location: Location,
    move: Move,
) -> Location:
    return Location(location.x + move.x, location.y + move.y)


def instruction_to_move(instruction: str) -> Move:
    direction, distance = instruction.split(" ")
    distance = int(distance)
    if direction.lower() == "U":
        return Move(-1 * distance, 0)
    elif direction.lower() == "D":
        return Move(distance, 0)
    elif direction.lower() == "L":
        return Move(0, -1 * distance)
    elif direction.lower() == "R":
        return Move(0, distance)
    else:
        raise ValueError(f'direction {direction} unrecognized!')


for line in instructions.split("\n")[:-1]:
    move = instruction_to_move(line)
    # moves: List[Move]

    head = update_location(head, move)
    # for move in moves:
    #   head = update_location(head, move)
    #   if calculate_distance(tail, head) > 1:
    #       tail = update_location(tail, get_best_move(head, tail))

    if distance(head, tail) > 1:
        tail = update_location(tail, get_best_move(head, tail))
        # we need to update tail and head at the same time, since a direction could have distance 4


# How many positions does the tail of the rope visit at least once?
# Tail stays adjacent to Head

def main() -> int:
    with open(sys.argv[1], "r") as f:
        instructions = f.read()
    size = get_board_size(instructions)
    print_board(size, (4, 4))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
