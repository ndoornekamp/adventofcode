from textwrap import dedent


def solve(input: str) -> int:
    grid = {}
    trail_heads = []
    for i, row in enumerate(input.strip().split("\n")):
        for j, cell in enumerate(row):
            if cell != ".":
                grid[(i, j)] = int(cell)

            if cell == "0":
                trail_heads.append((i, j))

    return sum(n_paths_to_top(trail_head, grid) for trail_head in trail_heads)


def n_paths_to_top(current_location, grid) -> int:
    if grid[current_location] == 9:
        return 1

    next_steps = []
    for neighbor in [
        (current_location[0] - 1, current_location[1]),
        (current_location[0] + 1, current_location[1]),
        (current_location[0], current_location[1] - 1),
        (current_location[0], current_location[1] + 1),
    ]:
        if neighbor in grid and grid[neighbor] == grid[current_location] + 1:
            next_steps.append(neighbor)

    return sum(n_paths_to_top(n, grid) for n in next_steps)


def test_solve_example_1():
    input = dedent("""
        012345
        123456
        234567
        345678
        4.6789
        56789.
    """)
    assert solve(input) == 227


def test_solve_example_2():
    input = dedent("""
        89010123
        78121874
        87430965
        96549874
        45678903
        32019012
        01329801
        10456732
    """)
    assert solve(input) == 81


if __name__ == "__main__":
    with open("input.txt") as f:
        input = f.read()

    ans = solve(input)
    print(ans)
