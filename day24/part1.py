from dataclasses import dataclass
import math


direction_map = {
    "<": (0, -1),
    ">": (0, 1),
    "v": (1, 0),
    "^": (-1, 0),
    "": (0, 0)
}
inv_direction_map = {v: k for k, v in direction_map.items()}

global best
global states
global blizzard_locations

best = 300
states = {}
blizzard_locations = []


@dataclass
class Blizzard:
    x: int
    y: int
    direction: tuple
    map_width: int
    map_height: int

    def move(self):
        x_new = ((self.x + self.direction[0] - 1) % self.map_width) + 1
        y_new = ((self.y + self.direction[1] - 1) % self.map_height) + 1
        return Blizzard(x_new, y_new, self.direction, self.map_width, self.map_height)

    def __hash__(self) -> int:
        return hash((self.x, self.y, self.direction))


def parse_input(input):
    global states
    open_tiles = []
    blizzards = []

    x_bounds = [0, len(input.split("\n")) - 1]
    y_bounds = [0, len(input.split("\n")[0]) - 1]

    for i, row in enumerate(input.split("\n")):
        for j, tile in enumerate(list(row)):
            if tile == ".":
                open_tiles.append((i, j))
            elif tile in "<v>^":
                direction = direction_map[tile]
                blizzards.append(Blizzard(i, j, direction, x_bounds[1] - 1, y_bounds[1] - 1))
            states[(i, j)] = float("inf")

    start = open_tiles[0]
    target = open_tiles[-1]

    return blizzards, x_bounds, y_bounds, start, target


def print_state(blizzards, x_bounds, y_bounds, elf_location, target, steps):
    blizzard_locations = [tuple(getattr(b, field) for field in ["x", "y"]) for b in blizzards]

    print(f"Took {steps} steps")
    for x in range(x_bounds[0], x_bounds[1] + 1):
        row = ""
        for y in range(y_bounds[0], y_bounds[1] + 1):
            if (x, y) == elf_location:
                row += "E"
            elif (x, y) == target:
                row += "T"
            elif x in [x_bounds[0], x_bounds[-1]] or y in [y_bounds[0], y_bounds[-1]]:
                row += "#"
            elif (x, y) in blizzard_locations:
                row += "b"
            else:
                row += "."
        print(row)
    print()


def solve(location, target, steps, x_bounds, y_bounds):
    global best
    global states
    global blizzard_locations

    distance_to_target = (target[0] - location[0]) + (target[1] - location[1])
    if distance_to_target + steps > best:
        # print(f"Still at least {distance_to_target} steps away from target, but already took {steps} steps")
        return best

    if location == target:
        if steps < best:
            print(f"Found path of length {steps}")
            best = steps
        return steps

    current_blizzard_locations = blizzard_locations[steps]

    potential_next_locations = {}
    for direction in direction_map.values():
        potential_next_location = (location[0] + direction[0], location[1] + direction[1])

        if potential_next_location == target:
            return solve(target, target, steps+1, x_bounds, y_bounds)
        elif potential_next_location in current_blizzard_locations:
            # print(f"Potential next location: {potential_next_location} is covered by a blizzard")
            continue
        elif potential_next_location == location:  # Wait in place
            potential_next_locations[potential_next_location] = solve(potential_next_location, target, steps+1, x_bounds, y_bounds)
        elif any([
            potential_next_location[0] >= x_bounds[1],
            potential_next_location[0] <= x_bounds[0],
            potential_next_location[1] >= y_bounds[1],
            potential_next_location[1] <= x_bounds[0]
        ]):
            # print(f"Potential next location: {potential_next_location} is a wall")
            # print_state(blizzards, x_bounds, y_bounds, location, target, steps)
            continue
        else:
            potential_next_locations[potential_next_location] = solve(potential_next_location, target, steps+1, x_bounds, y_bounds)

    if not potential_next_locations:
        # print("There is no possible next location!")
        # print_state(blizzards, x_bounds, y_bounds, location, target, steps)
        return float('inf')

    return min(potential_next_locations.values())


if __name__ == '__main__':
    input_file_path = "day24/input.txt"

    with open(input_file_path, 'r') as infile:
        input = infile.read()

    blizzards, x_bounds, y_bounds, start, target = parse_input(input)

    initial_blizzard_locations = blizzards

    # Cache blizzard locations
    for _ in range(best):
        blizzards = [b.move() for b in blizzards]
        blizzard_locations.append([tuple(getattr(b, field) for field in ["x", "y"]) for b in blizzards])

    # 250 is too low
    # 300 is too high
    print(solve(location=start, target=target, steps=0, x_bounds=x_bounds, y_bounds=y_bounds))
