from dataclasses import dataclass


direction_map = {
    "<": (0, -1),
    ">": (0, 1),
    "v": (1, 0),
    "^": (-1, 0),
    "": (0, 0)
}
inv_direction_map = {v: k for k, v in direction_map.items()}


@dataclass
class Blizzard:
    row: int
    col: int
    direction: tuple
    max_col: int
    max_row: int

    def move(self):
        row_new = ((self.row + self.direction[0] - 1) % self.max_row) + 1
        col_new = ((self.col + self.direction[1] - 1) % self.max_col) + 1
        return Blizzard(row_new, col_new, self.direction, self.max_col, self.max_row)

    def __hash__(self) -> int:
        return hash((self.col, self.row, self.direction))


def parse_input(input):
    open_tiles = []
    blizzards = []
    walls = []

    row_bounds = [0, len(input.split("\n")) - 1]
    col_bounds = [0, len(input.split("\n")[0]) - 1]

    for row_idx, row in enumerate(input.split("\n")):
        for col_idx, tile in enumerate(list(row)):
            if tile == ".":
                open_tiles.append((row_idx, col_idx))
            elif tile in "<v>^":
                direction = direction_map[tile]
                blizzards.append(Blizzard(row_idx, col_idx, direction, col_bounds[1] - 1, row_bounds[1] - 1))
            elif tile == "#":
                walls.append((row_idx, col_idx))

    start = open_tiles[0]
    walls.append((start[0]-1, start[1]))  # Add an extra piece of wall to prevent us from leaving the arena (stared at this for quite a while..)

    target = open_tiles[-1]
    walls.append((target[0] + 1, target[1]))  # Add an extra piece of wall to prevent us from leaving the arena (stared at this for quite a while..)

    return blizzards, walls, start, target, row_bounds, col_bounds


def print_state(blizzard_set, walls, col_bounds, row_bounds, elf_location, target):
    for row in range(row_bounds[0], row_bounds[1] + 1):
        disp = ""
        for col in range(col_bounds[0], col_bounds[1] + 1):
            if (row, col) == elf_location:
                disp += "E"
            elif (row, col) == target:
                disp += "T"
            elif (row, col) in walls:
                disp += "#"
            elif (row, col) in blizzard_set:
                disp += "b"
            else:
                disp += "."
        print(disp)
    print()


def solve(blizzards, walls, location, target, steps, row_bounds, col_bounds):
    states = {location}
    wall_set = set(walls)

    # print("Initial state:")
    # print_state(set([tuple(getattr(b, field) for field in ["row", "col"]) for b in blizzards]), wall_set, col_bounds, row_bounds, location, target)

    while target not in states:
        steps += 1
        new_states = set()

        blizzards = [b.move() for b in blizzards]
        blizzard_locations = [tuple(getattr(b, field) for field in ["row", "col"]) for b in blizzards]
        blizzard_set = set(blizzard_locations)

        # print(f"After {steps} steps there are {len(states)} reachable states")
        for current_state in states:
            potential_states = {
                (current_state[0] + drow, current_state[1] + dcol)
                for (drow, dcol) in [(0, 1), (0, -1), (1, 0), (-1, 0), (0, 0)]
            }
            new_states |= potential_states - blizzard_set - wall_set

        states = new_states

    return steps


if __name__ == '__main__':
    input_file_path = "day24/input.txt"

    with open(input_file_path, 'r') as infile:
        input = infile.read()

    blizzards, walls, start, target, row_bounds, col_bounds = parse_input(input)

    # 250 is too low
    # 300 is too high
    print(solve(blizzards=blizzards, walls=walls, location=start, target=target, steps=0, row_bounds=row_bounds, col_bounds=col_bounds))
