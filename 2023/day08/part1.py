
import re


input_file_path = '2023/day08/input.txt'

with open(input_file_path, 'r') as f:
    input = f.read().splitlines()

instructions = input[0]

nodes = {}
for line in input[2:]:
    m = re.findall(r"[A-Z]{3}", line)
    nodes[m[0]] = (m[1], m[2])

current_location = "AAA"
end = "ZZZ"
i = 0

while current_location != end:
    instruction = instructions[i % len(instructions)]
    if instruction == "R":
        next_location = nodes[current_location][1]
    else:
        next_location = nodes[current_location][0]

    i += 1
    current_location = next_location

print(i)
