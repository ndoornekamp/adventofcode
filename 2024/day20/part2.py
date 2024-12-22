from textwrap import dedent

import pytest
from tqdm import tqdm


def at_most_twenty_squares_away():
    out = set()
    for i in range(21):
        for j in range(21):
            if i + j <= 20:
                out.add((i, j))
                out.add((i, -j))
                out.add((-i, j))
                out.add((-i, -j))
    return out


def solve(input: str, minimum_savings: int) -> int:
    walls = set()

    n_rows = len(input.strip().split("\n"))
    n_cols = len(input.strip().split("\n")[0])

    for i, row in enumerate((input.strip().split("\n"))):
        for j, cell in enumerate(row):
            if cell == "#":
                walls.add((i, j))
            elif cell == "E":
                end = (i, j)
            elif cell == "S":
                start = (i, j)

    # If I'd read correctly in part 1, I'd known there's a unique path from S to E
    pos = start
    regular_path = [start]
    while pos != end:
        for d in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            neighbor = (pos[0] + d[0], pos[1] + d[1])
            if neighbor not in walls and neighbor not in regular_path:
                pos = neighbor
                regular_path.append(neighbor)

    # Follow the regular path and take note of any cheat that would join the path more squares ahead than the
    # lenght of the cheat
    ans = 0
    cheat_moves = at_most_twenty_squares_away()
    location_idx = {location: index for index, location in enumerate(regular_path)}
    for pos in tqdm(regular_path):
        for d in cheat_moves:
            cheat_end = (pos[0] + d[0], pos[1] + d[1])

            if cheat_end not in walls and cheat_end[0] > 0 and cheat_end[0] < n_rows and cheat_end[1] > 0 and cheat_end[1] < n_cols:
                cheat_length = abs(d[0]) + abs(d[1])
                savings = location_idx.get(cheat_end) - location_idx.get(pos) - cheat_length

                if savings >= minimum_savings:
                    ans += 1

    return ans


@pytest.mark.parametrize(("minimum_savings", "expected_n_cheats"), [(76, 3), (74, 3 + 4), (72, 3 + 4 + 22)])
def test_solve(minimum_savings, expected_n_cheats):
    input = dedent("""
        ###############
        #...#...#.....#
        #.#.#.#.#.###.#
        #S#...#.#.#...#
        #######.#.#.###
        #######.#.#...#
        #######.#.###.#
        ###..E#...#...#
        ###.#######.###
        #...###...#...#
        #.#####.#.###.#
        #.#...#.#.#...#
        #.#.#.#.#.#.###
        #...#...#...###
        ###############
    """)
    assert solve(input, minimum_savings) == expected_n_cheats


if __name__ == "__main__":
    with open("input.txt") as f:
        input = f.read()

    ans = solve(input, 100)  # 28852 is too low
    print(ans)
