from dataclasses import dataclass
from pathlib import Path
import sys
from typing import List


@dataclass
class File:
    name: str
    size: int

@dataclass
class Directory:
    name: str
    files: List[File]
    subdirectories: List['Directory']

    @property
    def size(self):
        return sum([z.size for z in self.subdirectories]) + sum([z.size for z in self.files])


def construct_file_system(inp: str) -> Directory:
    reference = {
        "/": Directory("", [], [])
    }
    current_path = Path("/")
    for line in inp.split("\n"):
        if line[:4] == "$ cd":
            target = line[5:]
            current_path = Path(current_path, target).resolve()
            if str(current_path) not in reference:
                reference[str(current_path)] = Directory(target, [], [])
        elif line[:4] == "$ ls":
            continue
        elif line[:3] == "dir":
            name = line[4:]
            fullname = Path(current_path, name)
            this = Directory(name, [], [])
            reference[str(fullname)] = this
            reference[str(current_path)].subdirectories.append(this)
        else:
            try:
                size, name = line.strip().split(" ")
            except:
                break
            fullname = Path(current_path, name)
            this = File(name, int(size))
            reference[str(fullname)] = this
            reference[str(current_path)].files.append(this)
    return reference


def main() -> int:
    with open(sys.argv[1], "r") as f:
        fs = construct_file_system(f.read())
    # part 1
    directories_under_100k_total = 0
    for i in fs.values():
        directories_under_100k_total += i.size if isinstance(i, Directory) and i.size <= 100000 else 0
    print(directories_under_100k_total)

    # part 2
    remaining_space_needed = 30000000 - (70000000 - fs['/'].size)
    size_of_candidate = float('inf')
    for i in fs.values():
        if not isinstance(i, Directory):
            continue
        if i.size >= remaining_space_needed and i.size < size_of_candidate:
            size_of_candidate = i.size
    print(size_of_candidate)


if __name__ == "__main__":
    raise SystemExit(main())
