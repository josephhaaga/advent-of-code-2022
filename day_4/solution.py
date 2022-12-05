from typing import Tuple


def does_fully_overlap(a: Tuple[int], b: Tuple[int]) -> bool:
    if (a[0] <= b[0] and a[1] >= b[1]) or (a[0] >= b[0] and a[1] <= b[1]):
        return True
    return False

def does_overlap(a: Tuple[int], b: Tuple[int]) -> bool:
    if b[0] <= a[1] and a[0] <= b[1]:
        return True
    return False


def main() -> int:
    with open('input.txt', 'r') as f:
        lines = f.read().split("\n")
    # part 1
    fully_overlaps = 0
    partially_overlaps = 0
    lines_processed = 0
    for line in lines:
        try:
            tuples = [tuple([int(x) for x in l.split("-")]) for l in line.split(",")]
        except ValueError:
            continue
        try:
            fully_overlaps += 1 if does_fully_overlap(tuples[0], tuples[1]) else 0
            partially_overlaps += 1 if does_overlap(tuples[0], tuples[1]) else 0
        except IndexError:
            continue
        lines_processed += 1
    print(f"Total lines: {lines_processed}")
    print(f"Full Overlaps: {fully_overlaps}")
    print(f"Partial Overlaps: {partially_overlaps}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
