from typing import List
import sys


def get_max_possible_scenic_score(matrix: List[List[int]]):
    """Determine the max possible scenic score of any tree in the matrix."""
    center_x, center_y = len(matrix[0]) // 2, len(matrix) // 2
    corner_x, corner_y = len(matrix[0]) - 1, len(matrix) - 1
    return max((center_x * center_x * center_y * center_y), (corner_x * corner_y))


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
    for y in range(0, len(matrix)):
        for x in range(0, len(matrix[0])):
            visible_trees += 1 if is_tree_visible(matrix, x, y) else 0

    largest_view_distance = get_max_possible_scenic_score(matrix)
    print(visible_trees)
    print(largest_view_distance)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
