from typing import List
import sys


def read_instructions(path: str) -> List[str]:
    with open(path, 'r') as f:
        instructions = f.read()
    return instructions.split("\n")


def main() -> int:
    instructions = read_instructions(sys.argv[1])
    # part 1
    X = 1
    cycle = 0
    positions = []
    for instruction in instructions:
        op, *amount = instruction.split(" ")
        if op == "noop":
            cycle += 1
        elif op == "addx":
            positions.append(X)
            cycle += 2
            X += int(amount[0])
        positions.append(X)

    # part 1
    def get_strength_at(y):
        return y * (positions[y-2])
    print(sum([get_strength_at(x) for x in [20, 60, 100, 140, 180, 220]]))

    # part 2
    for cycle_idx, position in enumerate(positions):
        if (cycle_idx + 1) % 40 in range(position - 1, position + 2):
            print("#", end='')
        else:
            print(".", end='')
        if (cycle_idx + 1) % 40 == 0:
            print()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
