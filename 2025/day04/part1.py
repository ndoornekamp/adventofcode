from textwrap import dedent


def solve(input: str) -> int:
    grid = {}
    ans = 0
    input = input.strip()
    n_rows = len(input.split("\n"))
    n_cols = len(input.split("\n")[0])

    for col, line in enumerate(input.split("\n")):
        for row, val in enumerate(line):
            grid[(row, col)] = val

    for (row, col), val in grid.items():
        if grid[(row, col)] != "@":
            continue

        n_adjacent_rolls = 0
        for dr, dc in ((0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (1, 1), (-1, 1), (1, -1)):

            if row + dr == -1 or row + dr == n_rows or col + dc == -1 or col + dc == n_cols:
                continue

            if grid[(row + dr, col + dc)] == "@":
                n_adjacent_rolls += 1

        if n_adjacent_rolls < 4:
            ans += 1

    return ans


def test_solve():
    input = dedent("""
        ..@@.@@@@.
        @@@.@.@.@@
        @@@@@.@.@@
        @.@@@@..@.
        @@.@@@@.@@
        .@@@@@@@.@
        .@.@.@.@@@
        @.@@@.@@@@
        .@@@@@@@@.
        @.@.@@@.@.
    """)
    assert solve(input) == 13


if __name__ == "__main__":
    with open("input.txt") as f:
        input = f.read()

    ans = solve(input)
    print(ans)
