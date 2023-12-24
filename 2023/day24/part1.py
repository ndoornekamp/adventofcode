import numpy as np
from tqdm import tqdm


input_file_path = "2023/day24/input.txt"

with open(input_file_path, "r") as f:
    input = f.read().splitlines()

hail_stones = []
for line in input:
    coordinate, direction = line.split(" @ ")
    coordinate = np.array([int(c) for c in coordinate.split(", ")[:-1]])
    direction = np.array([int(d) for d in direction.split(", ")[:-1]])
    hail_stones.append((coordinate, direction))


def get_intersect(a, b, c, d):
    """
    https://en.wikipedia.org/wiki/Line%E2%80%93line_intersection#Given_two_points_on_each_line
    Assuming there is an intersection: We've already checked for parallel lines
    """
    t = ((a[0] - c[0]) * (c[1] - d[1]) - (a[1] - c[1]) * (c[0] - d[0])) / (
        (a[0] - b[0]) * (c[1] - d[1]) - (a[1] - b[1]) * (c[0] - d[0])
    )

    return a[0] + t * (b[0] - a[0]), a[1] + t * (b[1] - a[1])


x_lower = 200000000000000 if input_file_path == "2023/day24/input.txt" else 7
y_lower = x_lower
x_upper = 400000000000000 if input_file_path == "2023/day24/input.txt" else 27
y_upper = x_upper

ans = 0
for i, stone1 in enumerate(tqdm(hail_stones)):
    for stone2 in hail_stones[i + 1:]:
        print()
        print(f"{stone1[0]} @ {stone1[1]}")
        print(f"{stone2[0]} @ {stone2[1]}")

        cross_product = np.cross(stone1[1], stone2[1])
        if not np.any(cross_product):
            print(f"Stones {stone1} and {stone2} are parallel\n")
            continue

        x_intersect, y_intersect = get_intersect(stone1[0], stone1[0] + stone1[1], stone2[0], stone2[0] + stone2[1])

        # Check if intersection is in the test area
        if x_lower <= x_intersect <= x_upper and y_lower <= y_intersect <= y_upper:
            print(f"Squares {stone1} and {stone2} intersect at ({x_intersect}, {y_intersect}) - inside the test area")

            # Intersection is in the future if the delta between intersection and start has the same sign as the
            # velocity, for both stones, for both x and y
            d_to_intersect1 = x_intersect - stone1[0][0], y_intersect - stone1[0][1]
            d_to_intersect2 = x_intersect - stone2[0][0], y_intersect - stone2[0][1]

            if all(
                [
                    np.sign(d_to_intersect1[0]) == np.sign(stone1[1][0]),
                    np.sign(d_to_intersect1[1]) == np.sign(stone1[1][1]),
                    np.sign(d_to_intersect2[0]) == np.sign(stone2[1][0]),
                    np.sign(d_to_intersect2[1]) == np.sign(stone2[1][1]),
                ]
            ):
                print("Intersection is in the future")
                ans += 1
            else:
                print("Intersection is in the past")

        else:
            print(f"Squares {stone1} and {stone2} intersect at ({x_intersect}, {y_intersect}) - outside the test area")

print(ans)
