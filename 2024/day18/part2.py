from collections import deque
import re
from textwrap import dedent


def solve(input: str, grid_size: int) -> tuple[int, int]:
    corrupted_all = []
    for line in input.strip().split("\n"):
        m = re.findall(r"\d+", line)
        x, y = int(m[0]), int(m[1])
        corrupted_all.append((x, y))

    # Set start of this range with some trial-and-error for a quick answer
    for n_bytes in range(2500, len(corrupted_all)):
        print(f"{corrupted_all[n_bytes]} just fell")
        corrupted = set(corrupted_all[:n_bytes+1])

        pos = (0, 0)
        to_check = deque()
        to_check.append(pos)
        shortest_paths = {pos: 0}

        while to_check:
            cur = to_check.pop()
            for d in ((1, 0), (-1, 0), (0, -1), (0, 1)):
                neighbor = (cur[0] + d[0], cur[1] + d[1])
                if neighbor[0] in range(grid_size) and neighbor[1] in range(grid_size) and neighbor not in corrupted:
                    old_cost = shortest_paths.get(neighbor, float("inf"))
                    new_cost = 1 + shortest_paths[cur]
                    if new_cost < old_cost:
                        shortest_paths[neighbor] = new_cost
                        to_check.append(neighbor)

        goal = (grid_size - 1, grid_size - 1)

        if goal in shortest_paths:
            print(f"With {n_bytes} corrupted bytes: found a way out in {shortest_paths[goal]} steps")
        else:
            print(f"With {n_bytes} corrupted bytes: no way out")
            return corrupted_all[n_bytes]
    raise


def test_solve():
    input = dedent("""
        5,4
        4,2
        4,5
        3,0
        2,1
        6,3
        2,4
        1,5
        0,6
        3,3
        2,6
        5,1
        1,2
        5,5
        2,5
        6,5
        1,4
        0,4
        6,4
        1,1
        6,1
        1,0
        0,5
        1,6
        2,0
    """)
    assert solve(input, 7) == (6, 1)


if __name__ == "__main__":
    with open("input.txt") as f:
        input = f.read()

    ans = solve(input, 71)
    print(ans)
