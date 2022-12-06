import math
import re

input_file_path = "day05/test_input.txt"

with open(input_file_path, 'r') as infile:
    input = infile.read()

initial_stacks, instructions = input.split("\n\n")

nof_stacks = math.floor(len(initial_stacks.split("\n")[-1])/3)
stacks = [[] for _ in range(nof_stacks)]

for line in initial_stacks.split("\n"):
    for match in re.finditer(r"\[(.)\]", line):
        stack = int(match.start()/4)
        crate = match.group(1)
        stacks[stack].insert(0, crate)

for instruction in instructions.split("\n"):
    amount, source, destination = re.match(r"move (\d+) from (\d+) to (\d+)", instruction).groups()

    amount = int(amount)
    source = int(source)
    destination = int(destination)

    # Part 1
    # for _ in range(amount):
    #     crate = stacks[source-1].pop()
    #     stacks[destination-1].append(crate)

    # Part 2
    to_move = stacks[source-1][-amount:]
    stacks[source-1] = stacks[source-1][:-amount]
    stacks[destination-1] += to_move

print(stacks)

message = ""
for stack in stacks:
    if stack:
        message += stack[-1]
print(message)
