from collections import deque
from textwrap import dedent
from tqdm import tqdm


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

    shortest_path_without_cheating = shortest_path(start, end, walls)

    ans = 0
    for wall in tqdm(walls):
        if wall[0] == 0 or wall[1] == 0 or wall[0] == n_rows - 1 or wall[1] == n_cols - 1:
            continue

        walls_minus_one = walls.copy()
        walls_minus_one.remove(wall)
        shortest_path_with_cheat = shortest_path(start, end, walls_minus_one)

        if shortest_path_with_cheat < shortest_path_without_cheating:
            savings = shortest_path_without_cheating - shortest_path_with_cheat
            # print(f"Found path saving {savings} ps by removing wall {wall}")
            if savings >= minimum_savings:
                ans += 1

    return ans


def shortest_path(start, end, walls):
    shortest_paths = {}

    q = deque()
    q.append((0, start))

    while q:
        cost, pos = q.pop()

        for d in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            neighbor = (pos[0] + d[0], pos[1] + d[1])
            if neighbor not in walls:
                old_cost = shortest_paths.get(neighbor, float("inf"))
                new_cost = cost + 1
                if new_cost < old_cost:
                    shortest_paths[neighbor] = new_cost
                    q.append((new_cost, neighbor))

    return shortest_paths[end]


def test_solve():
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
    assert solve(input, 50) == 1


if __name__ == "__main__":
    with open("input.txt") as f:
        input = f.read()

    ans = solve(input, 100)
    print(ans)
