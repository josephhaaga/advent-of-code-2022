from dataclasses import dataclass
from dataclasses import field
import re
import sys
from typing import Callable
from typing import List


name_pattern = re.compile("Monkey (\d+):")
items_pattern = re.compile("Starting items: ([\d, ]+)")
operation_pattern = re.compile("Operation: new = (.+)")
test_pattern = re.compile("Test: divisible by (\d+)")
true_pattern = re.compile("If true: throw to monkey (\d+)")
false_pattern = re.compile("If false: throw to monkey (\d+)")


@dataclass
class Monkey:
    name: str
    operation: str
    test: str
    items: List[int]
    true: int
    false: int
    num_inspections: int = 0

    def give(self, item) -> None:
        self.items.append(item)

    def inspect_items(self, monkeys) -> None:
        while len(self.items) > 0:
            self.num_inspections += 1
            old = self.items.pop(0)
            new = eval(self.operation)
            new /= 3
            monkeys[
                self.true
                if new % int(self.test) == 0
                else self.false
            ].give(new)
        assert len(self.items) == 0


def parse_instructions_into_monkeys(filepath: str) -> List[Monkey]:
    with open(filepath, 'r') as f:
        instructions = f.read().split("\n\n")
    result = {}
    for instruction in instructions:
        lines = instruction.split("\n")
        name = re.search(name_pattern, lines[0]).groups(0)[0]
        items = [int(x) for x in re.search(items_pattern, lines[1]).groups(0)[0].split(", ")]
        operation = re.search(operation_pattern, lines[2]).groups(0)[0]
        test = re.search(test_pattern, lines[3]).groups(0)[0]
        true = re.search(true_pattern, lines[4]).groups(0)[0]
        false = re.search(false_pattern, lines[5]).groups(0)[0]
        monkey = Monkey(name, operation, test, items, true, false)
        result[monkey.name] = monkey
    return result


def main() -> int:
    # parse instructions into monkeys
    monkeys: Mapping[Monkey] = parse_instructions_into_monkeys(sys.argv[1])
    for round_ in range(20):
        for i in range(len(monkeys)):
            name = str(i)
            monkey = monkeys[name]
            print(f"Processing monkey {name}")
            monkey.inspect_items(monkeys)
    print()
    x = sorted(monkeys.values(), key=lambda x: x.num_inspections)
    breakpoint()
    print(x[-2].num_inspections * x[-1].num_inspections)
    return 0



if __name__ == "__main__":
    raise SystemExit(main())
