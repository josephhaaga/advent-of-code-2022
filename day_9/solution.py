from collections import namedtuple
import sys
from typing import List
from typing import Optional
from typing import Tuple


Distance = namedtuple("Distance", "x y")
Move = namedtuple("Move", "x y")
Location = namedtuple("Location", "x y")


def get_board_size(instructions: str) -> int:
    return max([int(line.split(" ")[1]) for line in instructions.split("\n")[:-1]])


def print_board(board_size: int, head_location: Optional[Location] = None) -> None:
    for y_idx in range(board_size):
        for x_idx in range(board_size):
            print("." if (x_idx, y_idx) != head_location else "H", end=" ")
        print()


def update_location(
    location: Location,
    move: Move,
) -> Location:
    return Location(location.x + move.x, location.y + move.y)


def instruction_to_moves(instruction: str) -> List[Move]:
    direction, distance = instruction.split(" ")
    distance = int(distance)
    dirs = {
        "U": (-1, 0),
        "D": (1, 0),
        "L": (0, -1),
        "R": (0, 1)
    }
    return [Move(*dirs[direction]) for _ in range(distance)]


def calculate_distance(a: Location, b: Location) -> Distance:
    """Calculate the [x, y] distance between `a` and `b`."""
    return Distance(b.x-a.x, b.y-a.y)


def get_best_move(tail: Location, distance: Distance) -> Move:
    """Returns the Move that makes `tail` adjacent to `head`."""
    delta_x, delta_y = distance.x, distance.y # 2, -2
    if delta_x < 0:
        delta_x = -1
    elif delta_x > 1:
        delta_x = 1
    if delta_y < 0:
        delta_y = -1
    elif delta_y > 1:
        delta_y = 1
    return Move(delta_x, delta_y)


# How many positions does the tail of the rope visit at least once?
# Tail stays adjacent to Head

def main() -> int:
    with open(sys.argv[1], "r") as f:
        instructions = f.read()
    size = get_board_size(instructions)
    print_board(size, (4, 4))
    # Part 1
    tail_locations = []
    head = Location(20, 20)
    tail = Location(20, 20)
    tail_locations += [tail]
    for line in instructions.split("\n")[:-1]:
        moves: List[Move] = instruction_to_moves(line)
        for move in moves:
            head: Location = update_location(head, move)
            distance: Distance = calculate_distance(tail, head)
            if not (-1 <= distance[0] <= 1 and -1 <= distance[1] <= 1):
                best_move: Move = get_best_move(tail, distance)
                tail: Location = update_location(tail, best_move)
                tail_locations += [tail]
    print(len(set(tail_locations)))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
