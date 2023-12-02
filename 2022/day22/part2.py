import re
import numpy as np

from tqdm import tqdm

input_file_path = "day22/input.txt"

if input_file_path == "day22/input.txt":
    from cube import move
    face_size = 50
elif input_file_path == "day22/test_input.txt":
    from cube_test import move
    face_size = 4
else:
    raise

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

for instruction in tqdm(matches):
    number_of_steps = int(instruction[:-1])
    location, direction_idx = move(number_of_steps, location, direction_idx, directions, open_tiles, wall_tiles, face_size)

    # print(f"Direction was {direction}")
    turning_direction = instruction[-1]
    # print(f"Turning {turning_direction}")

    if turning_direction == "R":
        direction_idx = (direction_idx + 1) % len(directions)
    elif turning_direction == "L":
        direction_idx = (direction_idx - 1) % len(directions)
    else:
        raise
    direction = directions[direction_idx]
    # print(f"Direction is now {direction}")
    # print()

if input[-1] in [str(i) for i in range(10)]:
    number_of_steps = int(input[-1])
    location, _ = move(number_of_steps, location, direction_idx, directions, open_tiles, wall_tiles, face_size)


password = 1000 * (location[0] + 1) + 4 * (location[1] + 1) + direction_idx
assert password == 4578

print(f"Final row: {location[0] + 1}, final column {location[1] + 1}, final facing {direction_idx}")
print(f"Password: {password}")
