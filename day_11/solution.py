from dataclasses import dataclass
from dataclasses import field
import re
import sys
from typing import Callable
from typing import List


@dataclass
class Monkey:
    name: str
    operation: Callable[int, int]
    test: Callable[int, Callable]
    items: List[int] = field(default_factory=list)
    num_inspections: int = 0


name_pattern = re.compile("Monkey (\d+):")
items_pattern = re.compile("Starting items: ([\d, ]+)")
operation_pattern = re.compile("Operation: new = (.+)\n")
test_pattern = re.compile("Test: divisible by (\d+)")
true_pattern = re.compile("If true: throw to monkey (\d+)")
false_pattern = re.compile("If false: throw to monkey (\d+)")

def parse_instructions_into_monkeys(filepath: str) -> List[Monkey]:
    with open(filepath, 'r') as f:
        instructions = f.read().split("\n\n")
    for instruction in instructions:
        lines = instruction.split("\n")
        name = re.search(name_pattern, lines[0]).groups(0)[0]
        items = [int(x) for x in re.search(items_pattern, lines[1]).groups(0)[0].split(", ")]
        operation = re.search(operation_pattern, lines[2]).groups(0)[0]
        breakpoint()
    breakpoint()
    return None


def main() -> int:
    # parse instructions into monkeys
    monkeys: List[Monkey] = parse_instructions_into_monkeys(sys.argv[1])

    for round_ in range(20):
        for monkey in monkeys:
            pass
            # monkey inspects all items
    print(product)
    return 0



if __name__ == "__main__":
    raise SystemExit(main())
