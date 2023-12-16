from dataclasses import dataclass

from tqdm import tqdm


input_file_path = "2023/day16/input.txt"

with open(input_file_path, "r") as f:
    input = f.read().splitlines()

grid = {}
for i, row in enumerate(input):
    for j, val in enumerate(row):
        grid[(i, j)] = val


@dataclass
class Beam:
    direction: tuple
    location: tuple


def solve(starting_beams: list[Beam]) -> int:
    beams = starting_beams
    energized_tiles = set()
    n_energized_tiles_history = []
    seen = set()

    while True:
        for i, beam in enumerate(beams):
            # print(f"There are now {len(beams)} beams")
            new_loc = (beam.location[0] + beam.direction[0], beam.location[1] + beam.direction[1])

            if new_loc not in grid:
                del beams[i]
                continue

            beam.location = new_loc
            energized_tiles.add(new_loc)

            if grid[new_loc] == ".":
                pass

            elif grid[new_loc] == "\\":
                if beam.direction == (0, 1):
                    beam.direction = (1, 0)
                elif beam.direction == (1, 0):
                    beam.direction = (0, 1)
                elif beam.direction == (-1, 0):
                    beam.direction = (0, -1)
                elif beam.direction == (0, -1):
                    beam.direction = (-1, 0)
                else:
                    raise

            elif grid[new_loc] == "/":
                if beam.direction == (0, 1):
                    beam.direction = (-1, 0)
                elif beam.direction == (1, 0):
                    beam.direction = (0, -1)
                elif beam.direction == (-1, 0):
                    beam.direction = (0, 1)
                elif beam.direction == (0, -1):
                    beam.direction = (1, 0)
                else:
                    raise

            elif grid[new_loc] == "|":
                if beam.direction[1] == 0:
                    pass
                elif beam.direction[1] in (-1, 1):
                    beam.direction = (1, 0)
                    if ((-1, 0), new_loc) not in seen:
                        beams.append(Beam(direction=(-1, 0), location=new_loc))
                else:
                    raise

            elif grid[new_loc] == "-":
                if beam.direction[0] == 0:
                    pass
                elif beam.direction[0] in (-1, 1):
                    beam.direction = (0, 1)
                    if ((0, -1), new_loc) not in seen:
                        beams.append(Beam(direction=(0, -1), location=new_loc))
                else:
                    raise

            else:
                raise

            seen.add((beam.direction, beam.location))
        n_energized_tiles_history.append(len(energized_tiles))

        if len(n_energized_tiles_history) > 10 and len(set(n_energized_tiles_history[-10:])) == 1:
            break

    return len(energized_tiles)


possible_starting_beams = []
n_rows = len(input)
n_cols = len(input[0])

for i in range(n_rows):
    possible_starting_beams.append(Beam(direction=(0, 1), location=(i, -1)))
    possible_starting_beams.append(Beam(direction=(0, -1), location=(i, n_cols)))

for j in range(n_cols):
    possible_starting_beams.append(Beam(direction=(1, 0), location=(-1, j)))
    possible_starting_beams.append(Beam(direction=(-1, 0), location=(n_rows, j)))

ans = 0
for starting_beam in tqdm(possible_starting_beams):
    n_energized_tiles = solve(starting_beams=[starting_beam])

    if n_energized_tiles > ans:
        ans = n_energized_tiles

print(ans)
