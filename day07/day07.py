from collections import defaultdict
from pathlib import Path

input_file_path = "day07/input.txt"

with open(input_file_path, 'r') as infile:
    input = infile.read()

commands = [line.strip() for line in input.split("$") if line]

cwd = Path("/")
dir_sizes = defaultdict(int)

for command in commands[1:]:
    if command.startswith("cd"):
        cwd = cwd / command[3:]
        cwd = cwd.resolve()

    elif command.startswith("ls"):
        ls_output = command.split("\n")[1:]

        for line in ls_output:
            if line.startswith("dir"):
                pass
            else:
                size, file_name = line.split(" ")

                dir_sizes[cwd] += int(size)
                for dir in cwd.parents:
                    dir_sizes[dir] += int(size)

print(sum([size for size in dir_sizes.values() if size < 100_000]))

# Part 2
space_required = 30_000_000
space_available = 70_000_000 - dir_sizes[Path("/")]
space_to_clear = space_required - space_available

print(min([(dir, size) for dir, size in dir_sizes.items() if size > space_to_clear], key=lambda t: t[1]))
