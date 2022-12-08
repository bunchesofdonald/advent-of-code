from day7 import read_filesystem, find_directories, get_disk_usage

puzzle_input = """$ cd /
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
7214296 k""".split(
    "\n"
)


def test_read_filesystem():
    assert read_filesystem(puzzle_input) == {
        "/": {"type": "directory", "size": 48381165},
        "/a": {"type": "directory", "size": 94853},
        "/a/e": {"type": "directory", "size": 584},
        "/a/e/i": {"type": "file", "size": 584},
        "/a/f": {"type": "file", "size": 29116},
        "/a/g": {"type": "file", "size": 2557},
        "/a/h.lst": {"type": "file", "size": 62596},
        "/b.txt": {"type": "file", "size": 14848514},
        "/c.dat": {"type": "file", "size": 8504156},
        "/d": {"type": "directory", "size": 24933642},
        "/d/j": {"type": "file", "size": 4060174},
        "/d/d.log": {"type": "file", "size": 8033020},
        "/d/d.ext": {"type": "file", "size": 5626152},
        "/d/k": {"type": "file", "size": 7214296},
    }


def test_find_directories():
    filesystem = read_filesystem(puzzle_input)
    assert find_directories(filesystem, size__lt=100000) == {
        "/a": {"type": "directory", "size": 94853},
        "/a/e": {"type": "directory", "size": 584},
    }


def test_get_disk_usage():
    filesystem = read_filesystem(puzzle_input)
    assert get_disk_usage(filesystem) == (70000000, 48381165, 21618835)
