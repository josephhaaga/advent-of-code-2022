from typing import List
from typing import Tuple
"""
    [C]     [R]     [L]
[F] [M] [Z] [H]     [W]         [H]
[R] [H] [M] [C] [P] [C]     [N] [W]
[W] [T] [P] [J] [C] [G] [W] [P] [J]
 1   2   3   4   5   6   7   8   9

move 2 from 4 to 9
move 5 from 2 to 9
move 1 from 5 to 1
move 3 from 1 to 4
"""

Stack = List[str]  # ["W", "F", "R"]
Instruction = Tuple[int, int, int]  # (amount, source, destination) => (2, 4, 9)


def parse_input(filepath: str) -> Tuple[List[Stack], List[Instruction]]:
    """Parse input.txt into Stacks and Instructions."""
    with open(filepath, 'r') as f:
        lines = f.readlines()
    pivot = lines.index("\n") # switches from Stacks to Instructions

    # parse stacks
    number_of_stacks = int(lines[pivot-1].split(" ")[-2])
    stacks = [[] for _ in range(number_of_stacks)]
    for line in lines[pivot-2::-1]:
        letters: List[str] = [line[i+1] for i in range(0, len(line), 4)]
        for index, letter in enumerate(letters):
            if letter != ' ':
                stacks[index] += [letter]

    # parse instructions
    instructions = []
    for line in lines[pivot+1:]:
        _, amount, __, src, ___, dest = line.split(" ")
        instructions += [(int(amount), int(src), int(dest.replace("\n", "")))]

    return (stacks, instructions)


# run the instructions
def run_instructions(stacks: List[Stack], instructions: List[Instruction]) -> List[Stack]:
    for instruction in instructions:
        amount, src, dest = instruction
        src, dest = src - 1, dest - 1 # zero-indexed lists
        while amount > 0:
            try:
                stacks[dest].append(stacks[src].pop(-1))
            except IndexError:
                continue
            amount -= 1
    return stacks


def get_items_on_top_of_each_stack(stacks: List[Stack]) -> str:
    answer = ''
    for stack in stacks:
        answer += stack.pop(-1)
    return answer
# output the results


def main() -> int:
    stacks, instructions = parse_input("input.txt")
    result = run_instructions(stacks, instructions)
    # part 1
    print(get_items_on_top_of_each_stack(result))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

