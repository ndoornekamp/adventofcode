from heapq import heappop, heappush


input_file_path = "2023/day17/input.txt"

with open(input_file_path, "r") as f:
    input = f.read().splitlines()

grid = {}
for i, row in enumerate(input):
    for j, val in enumerate(row):
        grid[(i, j)] = int(val)

start = (0, 0)
end = (len(input) - 1, len(input[0]) - 1)

# cost, current_location, direction, n_steps_straight
q = [(0, (0, 0), (1, 0), 0)]
seen = set()
shortest_paths = {}
DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

path_lengths = []
while q:
    total_length, current_location, current_direction, n_steps_straight = heappop(q)

    if current_location == end and n_steps_straight >= 4:
        path_lengths.append(total_length)

    if (current_location, current_direction, n_steps_straight) in seen:
        continue

    seen.add((current_location, current_direction, n_steps_straight))

    for direction in DIRECTIONS:
        if direction != current_direction and n_steps_straight < 4:
            continue  # Not able to do less than 4 steps straight

        if direction == current_direction and n_steps_straight >= 10:
            continue  # Not able to do more than 10 steps straight

        if direction == (-1 * current_direction[0], -1 * current_direction[1]):
            continue  # Not able to turn around

        new_x = current_location[0] + direction[0]
        new_y = current_location[1] + direction[1]

        if (new_x, new_y) not in grid:
            continue

        length = total_length + grid[(new_x, new_y)]

        if (new_x, new_y, direction, n_steps_straight) in shortest_paths:
            if length < shortest_paths[(new_x, new_y, direction, n_steps_straight)]:
                shortest_paths[(new_x, new_y, direction, n_steps_straight)] = length
            else:
                continue

        heappush(q, (length, (new_x, new_y), direction, 1 if direction != current_direction else n_steps_straight + 1))

print(path_lengths)
print(min(path_lengths))
