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

    return cheapest_path_route(grid, pos, d, 0, end, False)


DIRECTIONS = [(0, 1), (-1, 0), (0, -1), (1, 0)]
seen = {}


def cheapest_path_route(grid, pos, d, cost, end, turned_previous_move):
    if pos == end:
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
        next_moves.append([grid, (pos[0] + d[0], pos[1] + d[1]), d, cost + 1, end, False])

    # Turn
    if not turned_previous_move:
        d_cw = DIRECTIONS[(DIRECTIONS.index(d) + 1) % 4]
        next_moves.append([grid, (pos[0], pos[1]), d_cw, cost + 1000, end, True])
        d_ccw = DIRECTIONS[(DIRECTIONS.index(d) - 1) % 4]
        next_moves.append([grid, (pos[0], pos[1]), d_ccw, cost + 1000, end, True])

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
    assert solve(input) != sys.maxsize, "Found no solution"
    assert solve(input) == 7036


if __name__ == '__main__':
    with open('input.txt') as f:
        input = f.read()

    ans = solve(input)
    print(ans)
