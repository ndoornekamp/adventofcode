
import math
import re


input_file_path = '2023/day08/input.txt'

with open(input_file_path, 'r') as f:
    input = f.read().splitlines()

instructions = input[0]

nodes = {}
for line in input[2:]:
    m = re.findall(r"[A-Z0-9]{3}", line)
    nodes[m[0]] = (m[1], m[2])


start_locations = [node for node in nodes if node.endswith("A")]
path_lengths = []
for start_location in start_locations:
    i = 0
    current_location = start_location
    while not current_location.endswith("Z"):
        instruction = instructions[i % len(instructions)]
        if instruction == "R":
            next_location = nodes[current_location][1]
        else:
            next_location = nodes[current_location][0]

        current_location = next_location
        i += 1
    print(f"Ghost starting at {start_location} takes {i} steps to get to an end node")
    path_lengths.append(i)

# Ghosts will all be at an end node at the least common multiple of their path lengths
print(math.lcm(*path_lengths))
