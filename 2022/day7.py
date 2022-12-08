from typing import Union
import os


Filesystem = dict[str, dict[str, Union[str, int]]]


def read_filesystem(input: list[str]) -> Filesystem:
    cwd = "/"
    filesystem = {"/": {"type": "directory"}}

    for line in input:
        line = line.strip()
        if line.startswith("$ cd"):
            change_to = line.split(" ")[-1]
            cwd = os.path.abspath(os.path.join(cwd, change_to))
        elif line.startswith("$ ls"):
            pass
        elif line.startswith("dir"):
            directory_name = line.split(" ")[-1]
            path = os.path.abspath(os.path.join(cwd, directory_name))
            filesystem[path] = {"type": "directory"}
        else:
            size, filename = line.split(" ")
            path = os.path.abspath(os.path.join(cwd, filename))
            filesystem[path] = {"type": "file", "size": int(size)}

    for path, item in filesystem.items():
        if item["type"] == "directory":
            item["size"] = sum(
                [
                    i["size"]
                    for p, i in filesystem.items()
                    if i["type"] == "file" and p.startswith(path)
                ]
            )

    return filesystem


def find_directories(
    filesystem: Filesystem, size__lt: int = None, size__gte: int = None
) -> Filesystem:
    found = {}
    for path, item in filesystem.items():
        if item["type"] == "file":
            continue
        elif size__lt and item["size"] < size__lt:
            found[path] = item
        elif size__gte and item["size"] >= size__gte:
            found[path] = item

    return found


def get_disk_usage(filesystem: Filesystem) -> tuple[int, int, int]:
    total = 70000000
    used = filesystem["/"]["size"]
    unused = total - used

    return total, used, unused


if __name__ == "__main__":
    with open("day7.txt") as infile:
        filesystem = read_filesystem(infile.readlines())

    small_dirs = find_directories(filesystem, size__lt=100000)
    print(sum(i["size"] for i in small_dirs.values()))

    total, used, unused = get_disk_usage(filesystem)
    need_to_free = 30000000 - unused

    large_enough = find_directories(filesystem, size__gte=need_to_free)
    print(min(i["size"] for i in large_enough.values()))
