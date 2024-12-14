from dataclasses import dataclass
import re
from tqdm import tqdm


@dataclass
class Robot:
    px: int
    py: int
    vx: int
    vy: int


def solve(input_: str, seconds: int, grid_n_rows: int, grid_n_cols: int) -> int:
    robots = []
    for line in input_.strip().split("\n"):
        nums = [int(n) for n in re.findall(r"-?\d+", line)]
        robots.append(Robot(px=nums[0], py=nums[1], vx=nums[2], vy=nums[3]))

    with open("output.txt", "a") as outfile:
        for s in tqdm(range(seconds)):
            for robot in robots:
                robot.px = (robot.px + robot.vx) % grid_n_cols
                robot.py = (robot.py + robot.vy) % grid_n_rows

            # Write grids to file, search it for e.g. "xxxxxx" to find dense spots
            # Then, visually inspect grids to check for a christmas tree
            rows = []
            for i in range(grid_n_rows):
                row = ""
                for j in range(grid_n_cols):
                    cell = " "
                    robots_in_cell = len([r for r in robots if r.px == j and r.py == i])
                    if robots_in_cell > 0:
                        cell = "x"
                    row += cell
                row += "\n"
                rows.append(row)

            if any("xxxxxx" in row for row in rows):
                outfile.write(f"\n\nAfter: {s+1} seconds\n")
                outfile.writelines(rows)


if __name__ == "__main__":
    with open("input.txt") as f:
        input_ = f.read()

    ans = solve(input_, 10000, 103, 101)
