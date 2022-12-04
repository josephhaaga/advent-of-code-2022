from typing import Tuple


# split knapsack into compartments
def split_knapsack(knapsack: str) -> Tuple[str, str]:
    l = len(knapsack) // 2
    return (knapsack[:l], knapsack[l:])

# find common item (set intersection) of two compartments
# {}.intersection({})

# calculate priority of item
def calculate_priority(item: str) -> int:
    root, intercept  = ("A", 27) if item.isupper() else ("a", 1)
    return (ord(item) - ord(root)) + intercept



def main() -> int:
    total: int = 0
    with open("input.txt", "r") as f:
        lines = f.read().split("\n")
    for line in lines:
        pocket_one, pocket_two = split_knapsack(line)
        try:
            duplicate_item = set(pocket_one).intersection(set(pocket_two)).pop()
        except KeyError:
            continue
        priority = calculate_priority(duplicate_item)
        total += priority
    # part 1
    print(total)

    n = 3
    total = 0
    groups = [lines[i:i+n] for i in range(0, len(lines), n)]
    for group in groups:
        sets = [set(a) for a in group]
        try:
            badge = sets[0].intersection(*sets[1:]).pop()
        except KeyError:
            continue
        total += calculate_priority(badge)
    # part 2
    print(total)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
