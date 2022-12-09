from enum import Enum
import sys

class Direction(Enum):
    NORTH = 1
    SOUTH = 2
    EAST = 3
    WEST = 4



def apply_in_direction(matrix: List[List[int]]: direction: str, callback: Callable) -> List[List[Any]]:


def main() -> int:
    input_path = sys.argv[1]
    with open(input_path, 'r') as f:
        matrix = [[int(y) for y in list(x.strip())] for x in f.readlines()]

    # iterate thru matrix in all four directions
    breakpoint()
    # combine results and sum
    # solve
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
