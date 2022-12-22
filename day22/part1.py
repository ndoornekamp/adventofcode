import re

import numpy as np

input_file_path = "day22/input.txt"

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

location = open_tiles[0]
direction_idx = 0
direction = directions[direction_idx]

for instruction in matches:
    print(instruction)
    number_of_steps = int(instruction[:-1])

    for _ in range(number_of_steps):
        next_location = tuple(location + direction)
        if (next_location not in wall_tiles) and (next_location not in open_tiles):
            print(f"Next location should be {next_location}, which is not on the board")
            if direction_idx == 0:  # Moving right -> wrap to left
                next_location = min([tile for tile in open_tiles + wall_tiles if location[0] == tile[0]], key=lambda x: x[1])
            elif direction_idx == 2:  # Moving left -> wrap to right
                next_location = max([tile for tile in open_tiles + wall_tiles if location[0] == tile[0]], key=lambda x: x[1])
            elif direction_idx == 1:  # Moving down -> wrap up
                next_location = min([tile for tile in open_tiles + wall_tiles if location[1] == tile[1]], key=lambda x: x[0])
            elif direction_idx == 3:  # Moving up -> wrap to down
                next_location = max([tile for tile in open_tiles + wall_tiles if location[1] == tile[1]], key=lambda x: x[0])
            else:
                raise
            print(f"Next location becomes {next_location} instead")

        if next_location in wall_tiles:
            print(f"Next location {next_location} is a wall tile - stopping and moving on to changing direction")
            break
        elif next_location in open_tiles:
            print(f"Next location {next_location} is an open tile - moving there")
            location = next_location
        else:
            raise

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
    for _ in range(number_of_steps):
        next_location = tuple(location + direction)
        if (next_location not in wall_tiles) and (next_location not in open_tiles):
            print(f"Next location should be {next_location}, which is not on the board")
            if direction_idx == 0:  # Moving right -> wrap to left
                next_location = min([tile for tile in open_tiles + wall_tiles if location[0] == tile[0]], key=lambda x: x[1])
            elif direction_idx == 2:  # Moving left -> wrap to right
                next_location = max([tile for tile in open_tiles + wall_tiles if location[0] == tile[0]], key=lambda x: x[1])
            elif direction_idx == 1:  # Moving down -> wrap up
                next_location = min([tile for tile in open_tiles + wall_tiles if location[1] == tile[1]], key=lambda x: x[0])
            elif direction_idx == 3:  # Moving up -> wrap to down
                next_location = max([tile for tile in open_tiles + wall_tiles if location[1] == tile[1]], key=lambda x: x[0])
            else:
                raise
            print(f"Next location becomes {next_location} instead")

        if next_location in wall_tiles:
            print(f"Next location {next_location} is a wall tile - stopping and moving on to changing direction")
            break
        elif next_location in open_tiles:
            print(f"Next location {next_location} is an open tile - moving there")
            location = next_location
        else:
            raise

# 131016 is too low
print(f"Final row: {location[0] + 1}, final column {location[1] + 1}, final facing {direction_idx}")
print(f"Password: {1000 * (location[0] + 1) + 4 * (location[1] + 1) + direction_idx}")
