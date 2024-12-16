import sys
from textwrap import dedent

sys.setrecursionlimit(50000)


def solve(input: str) -> int:
    grid = {}
    for i, line in enumerate(input.strip().split("\n")):
        for j, cell in enumerate(line):
            if cell == "S":
                pos = (i, j)
                d = (0, 1)
                grid[(i, j)] = "."
            elif cell == "E":
                end = (i, j)
                grid[(i, j)] = "."
            else:
                grid[(i, j)] = cell

    return cheapest_path_route(grid, pos, d, 0, end, False, {pos})


DIRECTIONS = [(0, 1), (-1, 0), (0, -1), (1, 0)]
seen = {}
cheapest_path_cost = sys.maxsize
cheapest_path_tiles = set()


def cheapest_path_route(grid, pos, d, cost, end, turned_previous_move, path_tiles: set[tuple[int, int]]):
    if pos == end:
        global cheapest_path_cost
        global cheapest_path_tiles
        if cost < cheapest_path_cost:
            cheapest_path_cost = cost
            cheapest_path_tiles = path_tiles
        elif cost == cheapest_path_cost:
            cheapest_path_tiles = cheapest_path_tiles.union(path_tiles)

        return cost

    if (pos, d, turned_previous_move) in seen and seen[(pos, d, turned_previous_move)] < cost:
        return sys.maxsize
    else:
        seen[(pos, d, turned_previous_move)] = cost

    if cost > 100000:
        return sys.maxsize

    next_moves = []
    # Keep moving in same direction
    if grid[(pos[0] + d[0], pos[1] + d[1])] == ".":
        next_moves.append(
            [
                grid,
                (pos[0] + d[0], pos[1] + d[1]),
                d,
                cost + 1,
                end,
                False,
                path_tiles.union({(pos[0] + d[0], pos[1] + d[1])}),
            ]
        )

    # Turn
    if not turned_previous_move:
        d_cw = DIRECTIONS[(DIRECTIONS.index(d) + 1) % 4]
        next_moves.append([grid, (pos[0], pos[1]), d_cw, cost + 1000, end, True, path_tiles])
        d_ccw = DIRECTIONS[(DIRECTIONS.index(d) - 1) % 4]
        next_moves.append([grid, (pos[0], pos[1]), d_ccw, cost + 1000, end, True, path_tiles])

    if not next_moves:
        return sys.maxsize

    return min(cheapest_path_route(*m) for m in next_moves)


def test_solve():
    input = dedent("""
        ###############
        #.......#....E#
        #.#.###.#.###.#
        #.....#.#...#.#
        #.###.#####.#.#
        #.#.#.......#.#
        #.#.#####.###.#
        #...........#.#
        ###.#.#####.#.#
        #...#.....#.#.#
        #.#.#.###.#.#.#
        #.....#...#.#.#
        #.###.#.#.#.#.#
        #S..#.....#...#
        ###############
    """)
    solve(input)
    assert len(cheapest_path_tiles) == 45


if __name__ == "__main__":
    with open("input.txt") as f:
        input = f.read()

    solve(input)
    print(len(cheapest_path_tiles))
