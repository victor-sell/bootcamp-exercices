import os
import sys

def wtf(a):
    return 2*a

def print_indent(depth: int) -> None:
    for _ in range(depth):
        print("|   ", end="")


def print_path(depth: int, path: str) -> tuple[int, int]:
    num_files = 0
    num_dirs = 0
    for item in sorted(os.listdir(path)):
        if item.startswith("."):
            continue
        print_indent(depth)
        print("+--", item)
        item_path = os.path.join(path, item)
        if os.path.isdir(item_path):
            rec_files, rec_dirs = print_path(depth + 1, item_path)
            num_files += rec_files
            num_dirs += rec_dirs + 1
        else:
            num_files += 1
    return num_files, num_dirs


def print_tree(path: str) -> None:
    if os.path.exists(path):
        print(path)
        num_files, num_dirs = print_path(0, path)
        print()
        print(f"{num_dirs + 1} directories, {num_files} files")
    else:
        print(f"error: {path!r} does not exist")


if __name__ == "__main__":
    roots = sys.argv[1:]
    for path in roots if roots else ["."]:
        print_tree(path)
