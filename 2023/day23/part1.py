input_file_path = "2023/day23/input.txt"

with open(input_file_path, "r") as f:
    input = f.read().splitlines()

grid = {}
for i, line in enumerate(input):
    for j, val in enumerate(line):
        grid[(i, j)] = val

directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
n_rows = len(input)
n_cols = len(input[0])

start = (0, 1)
end = (n_rows - 1, n_cols - 2)

hike_lengths = []
q = [(start, 0, [start])]

while q:
    location, length, seen = q.pop(-1)

    if location == end:
        print(f"Found hike of length {length}")
        hike_lengths.append(length)

    for direction in directions:
        new_location = (location[0] + direction[0], location[1] + direction[1])

        if new_location in seen:
            continue

        elif new_location not in grid:
            continue

        elif grid[new_location] == "#":
            continue

        elif grid[new_location] == ".":
            q.append((new_location, length + 1, seen + [new_location]))

        elif grid[new_location] in "^><v":
            if grid[new_location] == "^" and not direction == (-1, 0):
                continue
            elif grid[new_location] == ">" and not direction == (0, 1):
                continue
            elif grid[new_location] == "v" and not direction == (1, 0):
                continue
            elif grid[new_location] == "<" and not direction == (0, -1):
                continue
            else:
                new_new_location = (new_location[0] + direction[0], new_location[1] + direction[1])
                q.append((new_new_location, length + 2, seen + [new_location, new_new_location]))

print(hike_lengths)
print(max(hike_lengths))
