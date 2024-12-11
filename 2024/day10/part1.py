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

    scores = []
    for trail_head in trail_heads:
        r = reachable_tops(trail_head, grid)
        scores.append(len(r))

    return sum(scores)


def reachable_tops(current_location, grid) -> set[tuple[int, int]]:
    if grid[current_location] == 9:
        return {current_location}

    next_steps = []
    for neighbor in [
        (current_location[0] - 1, current_location[1]),
        (current_location[0] + 1, current_location[1]),
        (current_location[0], current_location[1] - 1),
        (current_location[0], current_location[1] + 1),
    ]:
        if neighbor in grid and grid[neighbor] == grid[current_location] + 1:
            next_steps.append(neighbor)

    ans = set()
    for n in next_steps:
        ans.update(reachable_tops(n, grid))

    return ans


def test_solve_example_2():
    input = dedent("""
        ...0...
        ...1...
        ...2...
        6543456
        7.....7
        8.....8
        9.....9
    """)
    assert solve(input) == 2


def test_solve_example_4():
    input = dedent("""
        ..90..9
        ...1.98
        ...2..7
        6543456
        765.987
        876....
        987....
    """)
    assert solve(input) == 4


def test_solve_example_36():
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
    assert solve(input) == 36


if __name__ == "__main__":
    with open("input.txt") as f:
        input = f.read()

    ans = solve(input)
    print(ans)
