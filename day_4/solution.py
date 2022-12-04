from typing import Tuple


def does_fully_overlap(a: Tuple[int], b: Tuple[int]) -> bool:
    if (a[0] <= b[0] and a[1] >= b[1]) or (a[0] >= b[0] and a[1] <= b[1]):
        return True
    return False


def main() -> int:
    with open('input.txt', 'r') as f:
        lines = f.read().split("\n")
    # part 1
    total = 0
    lines_processed = 0
    for line in lines:
        try:
            tuples = [tuple([int(x) for x in l.split("-")]) for l in line.split(",")]
        except ValueError:
            continue
        try:
            overlaps: bool = does_fully_overlap(tuples[0], tuples[1])
        except IndexError:
            continue
        if overlaps:
            total += 1
        lines_processed += 1
        # increment total if overlaps
    print(f"Total lines: {lines_processed}")
    print(f"Overlaps: {total}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
