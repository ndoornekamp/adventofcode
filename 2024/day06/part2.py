from textwrap import dedent
from grid import Grid
from tqdm import tqdm

DIRECTION_SYMBOL_MAP = {
    "^": (-1, 0),
    ">": (0, 1),
    "v": (1, 0),
    "<": (0, -1),
}
SYMBOLS = DIRECTION_SYMBOL_MAP.keys()
DIRECTIONS = list(DIRECTION_SYMBOL_MAP.values())


def solve(input: str) -> int:
    grid = Grid.from_txt(input)

    # Use of sets is critical for performance here. Having obstacles and visted_states sets instead of lists
    # causes a performance improvement of >100x (~6 seconds vs. >10 minutes)
    original_obstacles = set()
    for i, row in enumerate(grid.rows):
        for j, cell in enumerate(row):
            if cell == "#":
                original_obstacles.add((i, j))
            elif cell in SYMBOLS:
                guard_location = (i, j)
                guard_direction = DIRECTION_SYMBOL_MAP[cell]

    initial_location = guard_location
    initial_direction = guard_direction

    original_path = set()
    while True:
        next_location = (guard_location[0] + guard_direction[0], guard_location[1] + guard_direction[1])

        if (
            next_location[0] < 0
            or next_location[1] < 0
            or next_location[0] >= len(grid.rows)
            or next_location[1] >= len(grid.rows[0])
        ):
            break

        if next_location in original_obstacles:
            next_location = guard_location
            guard_direction = DIRECTIONS[(DIRECTIONS.index(guard_direction) + 1) % 4]
        else:
            original_path.add(next_location)

        guard_location = next_location

    ans = 0
    # For each location in the original path, try placing an additional obstacle
    for obstacle_position in tqdm(original_path):
        guard_direction = initial_direction
        guard_location = initial_location

        obstacles = original_obstacles.union({obstacle_position})
        visited_states = set()
        while True:
            if (guard_location, guard_direction) in visited_states:
                ans += 1  # Found a loop!
                break

            visited_states.add((guard_location, guard_direction))
            next_location = (guard_location[0] + guard_direction[0], guard_location[1] + guard_direction[1])

            if (
                next_location[0] < 0
                or next_location[1] < 0
                or next_location[0] >= len(grid.rows)
                or next_location[1] >= len(grid.rows[0])
            ):
                break

            if next_location in obstacles:
                next_location = guard_location
                guard_direction = DIRECTIONS[(DIRECTIONS.index(guard_direction) + 1) % 4]

            guard_location = next_location

    return ans


def test_solve():
    input = dedent("""
        ....#.....
        .........#
        ..........
        ..#.......
        .......#..
        ..........
        .#..^.....
        ........#.
        #.........
        ......#...
    """)
    assert solve(input) == 6


if __name__ == "__main__":
    with open("input.txt") as f:
        input = f.read()

    ans = solve(input)
    print(ans)
