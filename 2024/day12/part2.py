from textwrap import dedent


def solve(input: str) -> int:
    grid = []

    for i, row in enumerate(input.strip().split("\n")):
        r = []
        for j, crop in enumerate(row):
            r.append(crop)
        grid.append(r)

    n_rows = len(grid)
    n_cols = len(grid[0])

    regions = []
    for i, row in enumerate(grid):
        for j, crop in enumerate(row):
            if any([(i, j) in r for r in regions]):
                continue

            region = {(i, j)}
            while True:
                region_size_before = len(region)
                for plot in region.copy():
                    for d in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
                        neighbor = (plot[0] + d[0], plot[1] + d[1])

                        if (
                            neighbor[0] in range(n_rows)
                            and neighbor[1] in range(n_cols)
                            and grid[neighbor[0]][neighbor[1]] == crop
                        ):
                            region.add(neighbor)

                if region_size_before == len(region):
                    break

            regions.append(region)

    ans = 0
    for region in regions:
        ans += get_sides(region) * len(region)

    return ans


def get_sides(region):
    nof_sides = 0

    row_min = min([r for r, c in region])
    row_max = max([r for r, c in region])
    col_min = min([c for r, c in region])
    col_max = max([c for r, c in region])

    # top/bottom sides
    for row in range(row_min, row_max + 2):
        p1 = False
        p2 = False

        # per column, check cells on prev and current row
        for c in range(col_min, col_max + 1):
            x1 = (row - 1, c) in region
            x2 = (row, c) in region

            if x1 == p1 and x2 == p2:  # same as previous col -> no new side
                continue

            if x1 != x2:  # rows are not in the same region
                nof_sides += 1

            p1 = x1
            p2 = x2

    # left/right sides
    for c in range(col_min, col_max + 2):
        p1 = False
        p2 = False

        # per row, check cells on prev and current col
        for row in range(row_min, row_max + 1):
            x1 = (row, c - 1) in region
            x2 = (row, c) in region

            if x1 == p1 and x2 == p2:  # same as previous row  -> no new side
                continue

            if x1 != x2:  # cols are not in the same region
                nof_sides += 1

            p1 = x1
            p2 = x2

    return nof_sides


def test_solve_small():
    input = dedent("""
        AAAA
        BBCD
        BBCC
        EEEC
    """)
    assert solve(input) == 80


def test_solve_e():
    input = dedent("""
        EEEEE
        EXXXX
        EEEEE
        EXXXX
        EEEEE
    """)
    assert solve(input) == 236


def test_solve_a():
    input = dedent("""
        AAAAAA
        AAABBA
        AAABBA
        ABBAAA
        ABBAAA
        AAAAAA
    """)
    assert solve(input) == 368


def test_solve():
    input = dedent("""
        RRRRIICCFF
        RRRRIICCCF
        VVRRRCCFFF
        VVRCCCJFFF
        VVVVCJJCFE
        VVIVCCJJEE
        VVIIICJJEE
        MIIIIIJJEE
        MIIISIJEEE
        MMMISSJEEE
    """)
    assert solve(input) == 1206


if __name__ == "__main__":
    with open("input.txt") as f:
        input = f.read()

    ans = solve(input)
    print(ans)
