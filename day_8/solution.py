import math
from typing import Dict
from typing import List
import sys


def get_view_distances(matrix: List[List[int]], x: int, y: int) -> Dict[str, int]:
    """Get view distances of a tree in the matrix."""
    distances = {
        "n": 0,
        "s": 0,
        "e": 0,
        "w": 0
    }
    # check number is in range
    # check height
    for n in range(y-1, -1, -1):
        distances['n'] += 1
        if matrix[n][x] >= matrix[y][x]:
            break

    for s in range(y+1, len(matrix), 1):
        distances['s'] += 1
        if matrix[s][x] >= matrix[y][x]:
            break

    for e in range(x+1, len(matrix[0]), 1):
        distances['e'] += 1
        if matrix[y][e] >= matrix[y][x]:
            break

    for w in range(x-1, -1, -1):
        distances['w'] += 1
        if matrix[y][w] >= matrix[y][x]:
            break

    return distances


def get_scenic_score(matrix: List[List[int]], x: int, y: int):
    """Calculate scenic score of a tree."""
    return math.prod(get_view_distances(matrix, x, y).values())


def is_tree_visible(matrix: List[List[int]], x: int, y: int):
    """Determine if a tree is visible in any of the four directions."""
    x_max, y_max = len(matrix[0]), len(matrix)

    # south
    visible_from_south = True
    if y < y_max:
        for t_y in range(y + 1, y_max):
            if matrix[t_y][x] >= matrix[y][x]:
                visible_from_south = False
                break
    if visible_from_south:
        return True

    # north
    visible_from_north = True
    if y > 0:
        for t_y in range(y-1, -1, -1):
            if matrix[t_y][x] >= matrix[y][x]:
                visible_from_north = False
                break
    if visible_from_north:
        return True

    # east
    visible_from_east = True
    if x > 0:
        for t_x in range(x-1, -1, -1):
            if matrix[y][t_x] >= matrix[y][x]:
                visible_from_east = False
                break
    if visible_from_east:
        return True

    # west
    visible_from_west = True
    if x > 0:
        for t_x in range(x + 1, x_max):
            if matrix[y][t_x] >= matrix[y][x]:
                visible_from_west = False
                break
    if visible_from_west:
        return True

    return False


def main() -> int:
    input_path = sys.argv[1]
    with open(input_path, 'r') as f:
        matrix = [[int(y) for y in list(x.strip())] for x in f.readlines()]

    # iterate thru matrix in all four directions
    visible_trees = 0
    highest_scenic = 0
    for y in range(0, len(matrix)):
        for x in range(0, len(matrix[0])):
            visible_trees += 1 if is_tree_visible(matrix, x, y) else 0
            scenic_score = get_scenic_score(matrix, x, y)
            if scenic_score > highest_scenic:
                highest_scenic = scenic_score
                highest_x, highest_y = x, y
                details = get_view_distances(matrix, x, y)
    print(visible_trees)
    print(highest_scenic)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
