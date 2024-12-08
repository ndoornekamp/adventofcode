from collections import defaultdict
from textwrap import dedent
from itertools import combinations


def solve(input: str) -> int:
    antennas_per_frequency = defaultdict(list)
    rows = input.strip().split("\n")

    n_rows = len(rows)
    n_cols = len(rows[0])

    for r, row in enumerate(rows):
        for c, cell in enumerate(row):
            if cell == ".":
                continue
            else:
                antennas_per_frequency[cell].append((r, c))

    antinodes = set()
    for frequency, antenna_coordinates in antennas_per_frequency.items():
        for pair in combinations(antenna_coordinates, r=2):
            d = (pair[0][0] - pair[1][0], pair[0][1] - pair[1][1])

            m = 0
            while pair[0][0] + m * d[0] in range(n_rows) and pair[0][1] + m * d[1] in range(n_cols):
                antinodes.add((pair[0][0] + m * d[0], pair[0][1] + m * d[1]))
                m += 1

            m = 0
            while pair[1][0] - m * d[0] in range(n_rows) and pair[1][1] - m * d[1] in range(n_cols):
                antinodes.add((pair[1][0] - m * d[0], pair[1][1] - m * d[1]))
                m += 1

    return len(antinodes)


def test_solve():
    input = dedent("""
        ............
        ........0...
        .....0......
        .......0....
        ....0.......
        ......A.....
        ............
        ............
        ........A...
        .........A..
        ............
        ............
    """)
    assert solve(input) == 34


def test_solve_small():
    input = dedent("""
        T.........
        ...T......
        .T........
        ..........
        ..........
        ..........
        ..........
        ..........
        ..........
        ..........
    """)
    assert solve(input) == 9


if __name__ == "__main__":
    with open("input.txt") as f:
        input = f.read()

    ans = solve(input)
    print(ans)
