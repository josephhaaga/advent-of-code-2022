from day_7.solution import construct_file_system
from day_7.solution import Directory
from day_7.solution import File

inp = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
"""

def test_construct_file_system():
    expected = Directory('/', [
        File("b.txt", 14848514),
        File("c.dat", 8504156)
    ], [
        Directory("a", [
            File("f", 29116),
            File("g", 2557),
            File("h.lst", 62596)
        ], [
            Directory("e", [
                File("i", 584)
            ], [])
        ]),
        Directory("d", [
            File("j", 4060174),
            File("d.log",8033020),
            File("d.ext",5626152),
            File("k", 7214296),
        ], []),
    ])
    assert construct_file_system(inp) == expected
