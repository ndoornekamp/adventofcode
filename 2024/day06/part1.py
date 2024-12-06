from textwrap import dedent
from grid import Grid

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

    obstacles = []
    for i, row in enumerate(grid.rows):
        for j, cell in enumerate(row):
            if cell == "#":
                obstacles.append((i, j))
            elif cell in SYMBOLS:
                guard_location = (i, j)
                guard_direction = DIRECTION_SYMBOL_MAP[cell]

    visited_locations = set()
    visited_locations.add(guard_location)
    while True:
        next_location = (guard_location[0] + guard_direction[0], guard_location[1] + guard_direction[1])

        if (
            next_location[0] < 0
            or next_location[1] < 0
            or next_location[0] >= len(grid.rows)
            or next_location[1] >= len(grid.rows[0])
        ):
            break  # Guard moved off the grid

        if next_location in obstacles:
            next_location = guard_location
            guard_direction = DIRECTIONS[(DIRECTIONS.index(guard_direction) + 1) % 4]
        else:
            visited_locations.add(next_location)

        guard_location = next_location

    return len(visited_locations)


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
    assert solve(input) == 41


if __name__ == '__main__':
    with open('input.txt') as f:
        input = f.read()

    ans = solve(input)
    print(ans)
