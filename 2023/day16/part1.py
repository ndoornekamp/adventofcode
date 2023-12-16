from dataclasses import dataclass


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

    while True:
        for beam in beams:
            # print(f"There are now {len(beams)} beams")
            new_loc = (beam.location[0] + beam.direction[0], beam.location[1] + beam.direction[1])

            if new_loc not in grid:
                # print("End of grid")
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
                    beams.append(Beam(direction=(-1, 0), location=new_loc))
                else:
                    raise

            elif grid[new_loc] == "-":
                if beam.direction[0] == 0:
                    pass
                elif beam.direction[0] in (-1, 1):
                    beam.direction = (0, 1)
                    beams.append(Beam(direction=(0, -1), location=new_loc))
                else:
                    raise

            else:
                raise

        n_energized_tiles_history.append(len(energized_tiles))

        if len(n_energized_tiles_history) > 3 and len(set(n_energized_tiles_history[-3:])) == 1:
            break

    return len(energized_tiles)


starting_beams = [Beam(direction=(0, 1), location=(0, -1))]
print(solve(starting_beams=starting_beams))
