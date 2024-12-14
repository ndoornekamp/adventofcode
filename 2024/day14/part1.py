from collections import defaultdict
from dataclasses import dataclass
import math
import re
from textwrap import dedent


@dataclass
class Robot:
    px: int
    py: int
    vx: int
    vy: int


def solve(input: str, seconds: int, grid_n_rows: int, grid_n_cols: int) -> int:
    robots = []
    for line in input.strip().split("\n"):
        nums = [int(n) for n in re.findall(r"-?\d+", line)]
        robots.append(Robot(px=nums[0], py=nums[1], vx=nums[2], vy=nums[3]))

    for _ in range(seconds):
        for robot in robots:
            robot.px = (robot.px + robot.vx) % grid_n_cols
            robot.py = (robot.py + robot.vy) % grid_n_rows

    grid = []
    for i in range(grid_n_rows):
        row = []
        for j in range(grid_n_cols):
            cell = "."
            robots_in_cell = len([r for r in robots if r.px == j and r.py == i])
            if robots_in_cell > 0:
                cell = robots_in_cell
            row.append(cell)
        grid.append(row)

    bx = grid_n_cols // 2
    by = grid_n_rows // 2

    robots_per_quadrant = defaultdict(int)
    for robot in robots:
        if robot.px > bx and robot.py > by:
            robots_per_quadrant[1] += 1
        elif robot.px < bx and robot.py > by:
            robots_per_quadrant[2] += 1
        elif robot.px < bx and robot.py < by:
            robots_per_quadrant[3] += 1
        elif robot.px > bx and robot.py < by:
            robots_per_quadrant[4] += 1

    return math.prod(robots_per_quadrant.values())


def test_solve():
    input = dedent("""
        p=0,4 v=3,-3
        p=6,3 v=-1,-3
        p=10,3 v=-1,2
        p=2,0 v=2,-1
        p=0,0 v=1,3
        p=3,0 v=-2,-2
        p=7,6 v=-1,-3
        p=3,0 v=-1,-2
        p=9,3 v=2,3
        p=7,3 v=-1,2
        p=2,4 v=2,-3
        p=9,5 v=-3,-3
    """)
    assert solve(input, 100, 7, 11) == 12


if __name__ == "__main__":
    with open("input.txt") as f:
        input = f.read()

    ans = solve(input, 100, 103, 101)
    print(ans)
