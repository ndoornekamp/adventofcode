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
        perimeter = 0
        for plot in region:
            # Number of lines this plot contributes to the region perimeter is 4 minus the nuber of neighboring plots
            # in the same region
            perimeter += 4
            for d in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
                neighbor = (plot[0] + d[0], plot[1] + d[1])
                if neighbor in region:
                    perimeter -= 1

        ans += perimeter * len(region)

    return ans


def test_solve_small():
    input = dedent("""
        AAAA
        BBCD
        BBCC
        EEEC
    """)
    assert solve(input) == 140


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
    assert solve(input) == 1930


if __name__ == "__main__":
    with open("input.txt") as f:
        input = f.read()

    ans = solve(input)
    print(ans)
