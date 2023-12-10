
input_file_path = '2023/day10/input.txt'

with open(input_file_path, 'r') as f:
    input = f.read().splitlines()


def tiles_are_connected(tile1, coordinate1, tile2, coordinate2):
    # Instead of determining what type of tile S was originally, hardcode it here
    if tile1 == "S":
        tile1 = "|"

    if tile2 == "S":
        tile2 = "|"

    if tile1 in ["F", "L", "-"]:  # tile 1 connects to east
        if coordinate1[0] == coordinate2[0] and coordinate2[1] == coordinate1[1] + 1:  # tile 2 is east of tile 1
            if tile2 in ["J", "7", "-"]:  # tile 2 connects to west
                return True

    if tile1 in ["F", "7", "|"]:  # tile 1 connects to south
        if coordinate1[1] == coordinate2[1] and coordinate2[0] == coordinate1[0] + 1:  # tile 2 is south of tile 1
            if tile2 in ["L", "J", "|"]:  # tile 2 connects to north
                return True

    if tile1 in ["J", "7", "-"]:  # tile 1 connects to west
        if coordinate1[0] == coordinate2[0] and coordinate2[1] == coordinate1[1] - 1:  # tile 2 is west of tile 1
            if tile2 in ["F", "L", "-"]:  # tile 2 connects to east
                return True

    if tile1 in ["L", "J", "|"]:  # tile 1 connects to north
        if coordinate1[1] == coordinate2[1] and coordinate2[0] == coordinate1[0] - 1:  # tile 2 is north of tile 1
            if tile2 in ["F", "7", "|"]:  # tile 2 connects to south
                return True

    return False


grid = {}
for i, line in enumerate(input):
    for j, tile in enumerate(line):
        grid[(i, j)] = tile

start_coordinate = [c for c, t in grid.items() if t == "S"][0]
print(f"{start_coordinate=}")

step_count = 0
traversed = []
current_coordinate = start_coordinate
ans = None
while ans is None:
    adjacent_coordinates = [
        (current_coordinate[0], current_coordinate[1] + 1),  # East of current
        (current_coordinate[0], current_coordinate[1] - 1),  # West of current
        (current_coordinate[0] + 1, current_coordinate[1]),  # North of current
        (current_coordinate[0] - 1, current_coordinate[1]),  # South of current
    ]

    for adjacent_coordinate in adjacent_coordinates:
        if adjacent_coordinate not in traversed:
            if grid.get(adjacent_coordinate, None) == "S" and step_count < 2:
                continue

            if tiles_are_connected(
                grid[current_coordinate],
                current_coordinate,
                grid.get(adjacent_coordinate, None),
                adjacent_coordinate,
            ):
                traversed.append(adjacent_coordinate)
                step_count += 1
                current_coordinate = adjacent_coordinate

                if current_coordinate == start_coordinate:
                    ans = step_count/2
                break


# Ray casting algorithm: https://en.wikipedia.org/wiki/Point_in_polygon#Ray_casting_algorithm
# Given the path cycle (list of traversed coordinates), a given point is inside the path if when we go straight east, we
# cross the path an even odd of times. We cross the path if we encounter a L, J, or | that is part of the path.
# Alternatively, we could count |, F or 7 as a crossing, but not all of L, J, F and 7 to avoid double-counting.

n_cols = len(input[0])
ans = 0
for coordinate in grid:

    if coordinate in traversed:
        continue

    crossings = 0
    row, col = coordinate
    while col <= n_cols:
        col += 1

        if (row, col) in traversed and grid[(row, col)] in ["F", "7", "|", "S"]:
            crossings += 1

    if crossings % 2 == 1:
        print(f"{coordinate} is enclosed by the path")
        ans += 1

print(ans)
