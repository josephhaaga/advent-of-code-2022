from dataclasses import dataclass
from pathlib import Path
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
            reference[fullname] = this
            reference[str(current_path)].subdirectories.append(this)
        else:
            try:
                size, name = line.strip().split(" ")
            except:
                break
            fullname = Path(current_path, name)
            this = File(name, int(size))
            reference[fullname] = this
            reference[str(current_path)].files.append(this)
    return reference["/"]

