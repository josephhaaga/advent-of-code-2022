from typing import List
import sys


def read_instructions(path: str) -> List[str]:
    with open(path, 'r') as f:
        instructions = f.read()
    return instructions.split("\n")


def main() -> int:
    X = 1
    cycle = 0
    instructions = read_instructions(sys.argv[1])
    strengths = [X]
    for instruction in instructions:
        op, *amount = instruction.split(" ")
        if op == "noop":
            cycle += 1
        elif op == "addx":
            strengths.append(X)
            cycle += 2
            X += int(amount[0])
        strengths.append(X)
    def get_strength_at(y):
        return y * (strengths[y-1])
    print(sum([get_strength_at(x) for x in [20, 60, 100, 140, 180, 220]]))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
