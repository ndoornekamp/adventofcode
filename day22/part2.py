import re

import numpy as np

input_file_path = "day22/test_input.txt"

directions = [
    np.array((0, 1)),
    np.array((1, 0)),
    np.array((0, -1)),
    np.array((-1, 0))
]

with open(input_file_path, 'r') as infile:
    input = infile.read()

board, path = input.split("\n\n")
matches = re.findall(r"\d+[A-Z]+", path)

open_tiles = []
wall_tiles = []
for i, row in enumerate(board.split("\n")):
    for j, tile in enumerate(list(row)):
        if tile == " ":
            continue
        elif tile == ".":
            open_tiles.append((i, j))
        elif tile == "#":
            wall_tiles.append((i, j))
        else:
            raise


def move(number_of_steps, location, direction_idx):
    direction = directions[direction_idx]
    for _ in range(number_of_steps):
        next_location = tuple(location + direction)
        if (next_location not in wall_tiles) and (next_location not in open_tiles):
            print(f"Next location should be {next_location}, which is not on the board")

            if 8 <= location[0] < 12 and 0 <= location[1] < 4:  # Face 1
                if tuple(direction) == (1, 0):
                    raise
                elif tuple(direction) == (-1, 0):  # Moving off face 1 to the top of face 2
                    next_location = np.array((4, 11 - location[1]))
                    direction = (1, 0)
                elif tuple(direction) == (0, 1):  # Moving off face 1 to the right of face 6
                    next_location = np.array((11 - location[0], 15))
                    direction = (0, -1)
                elif tuple(direction) == (0, -1):  # Moving off face 1 to the top of face 3
                    next_location = np.array((4, 4 + location[0]))
                    direction = (1, 0)
                else:
                    raise
            elif 4 <= location[0] < 8 and 0 <= location[1] < 4:  # Face 2
                if tuple(direction) == (1, 0):  # Moving down off face 2 to the bottom of face 5
                    next_location = np.array((11, 11 - location[1]))
                    direction = (-1, 0)
                elif tuple(direction) == (-1, 0):  # Moving up off face 2 to the top of face 1
                    next_location = np.array((0, 11 - location[1]))
                    direction = (1, 0)
                elif tuple(direction) == (0, 1):
                    raise
                elif tuple(direction) == (0, -1):  # Moving left off face 2 to the bottom of face 6
                    next_location = np.array((11, 19 - location[0]))
                    direction = (-1, 0)
                else:
                    raise
            elif 4 <= location[0] < 8 and 4 <= location[1] < 8:  # Face 3
                if tuple(direction) == (1, 0):
                    pass
                elif tuple(direction) == (-1, 0):
                    pass
                elif tuple(direction) == (0, 1):
                    raise
                elif tuple(direction) == (0, -1):
                    raise
                else:
                    raise
            elif 4 <= location[0] < 8 and 8 <= location[1] < 12:  # Face 4
                if tuple(direction) == (1, 0):
                    raise
                elif tuple(direction) == (-1, 0):
                    raise
                elif tuple(direction) == (0, 1):
                    pass
                elif tuple(direction) == (0, -1):
                    raise
                else:
                    raise
            elif 8 <= location[0] < 12 and 8 <= location[1] < 12:  # Face 5
                if tuple(direction) == (1, 0):
                    pass
                elif tuple(direction) == (-1, 0):
                    raise
                elif tuple(direction) == (0, 1):
                    raise
                elif tuple(direction) == (0, -1):
                    pass
                else:
                    raise
            elif 8 <= location[0] < 12 and 12 <= location[1] < 16:  # Face 6
                if tuple(direction) == (1, 0):
                    pass
                elif tuple(direction) == (-1, 0):
                    pass
                elif tuple(direction) == (0, 1):
                    pass
                elif tuple(direction) == (0, -1):
                    raise
                else:
                    raise

            assert next_location in wall_tiles + open_tiles

            print(f"Next location becomes {next_location} instead")

        if next_location in wall_tiles:
            print(f"Next location {next_location} is a wall tile - stopping and moving on to changing direction")
            break
        elif next_location in open_tiles:
            print(f"Next location {next_location} is an open tile - moving there")
            location = next_location
        else:
            raise
    return location


location = open_tiles[0]
direction_idx = 0
direction = directions[direction_idx]

for instruction in matches:
    print(instruction)
    number_of_steps = int(instruction[:-1])

    location = move(number_of_steps, location, direction_idx)

    print(f"Direction was {direction}")
    turning_direction = instruction[-1]
    print(f"Turning {turning_direction}")

    if turning_direction == "R":
        direction_idx = (direction_idx + 1) % len(directions)
    elif turning_direction == "L":
        direction_idx = (direction_idx - 1) % len(directions)
    else:
        raise
    direction = directions[direction_idx]
    print(f"Direction is now {direction}")
    print()

if input[-1] in [str(i) for i in range(10)]:
    number_of_steps = int(input[-1])
    location = move(number_of_steps, location, direction_idx)

print(f"Final row: {location[0] + 1}, final column {location[1] + 1}, final facing {direction_idx}")
print(f"Password: {1000 * (location[0] + 1) + 4 * (location[1] + 1) + direction_idx}")
