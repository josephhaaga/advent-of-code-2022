from collections import namedtuple
import sys
from typing import List
from typing import Optional
from typing import Tuple


Move = namedtuple("Move", "dx dy")
Location = namedtuple("Location", "x y")


def update_location(
    location: Location,
    move: Move,
) -> Location:
    return Location(location.x + move.dx, location.y + move.dy)


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


def get_best_move(a: Location, b: Location) -> Move:
    """Returns the Move that makes `a` adjacent to `b`."""
    distance = (b.x - a.x, b.y - a.y)
    if -1 <= distance[0] <= 1 and -1 <= distance[1] <= 1:
        return Move(0, 0)
    delta_x, delta_y = distance # 2, -2
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
    # Part 1
    head = Location(20, 20)
    tail = Location(20, 20)
    tail_locations = [tail]
    for line in instructions.split("\n")[:-1]:
        moves: List[Move] = instruction_to_moves(line)
        for move in moves:
            head: Location = update_location(head, move)
            best_move: Move = get_best_move(tail, head)
            tail: Location = update_location(tail, best_move)
            tail_locations += [tail]
    answer = len(set(tail_locations))
    print(answer)
    assert answer == 6037

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
