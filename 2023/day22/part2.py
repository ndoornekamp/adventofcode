from tqdm import tqdm


input_file_path = "2023/day22/input.txt"

with open(input_file_path, "r") as f:
    input = f.read().splitlines()


class Brick:
    coordinates: list[tuple[int, int, int]]
    name: str | None

    def __init__(self, start: tuple[int, int, int], end: tuple[int, int, int], name: str | None = None):
        self.name = name

        if start == end:
            orientation = (0, 0, 0)
            length = 1
        elif start[0] == end[0] and start[1] == end[1]:
            orientation = (0, 0, 1)
            length = abs(start[2] - end[2])
        elif start[0] == end[0] and start[2] == end[2]:
            orientation = (0, 1, 0)
            length = abs(start[1] - end[1])
        elif start[1] == end[1] and start[2] == end[2]:
            orientation = (1, 0, 0)
            length = abs(start[0] - end[0])
        else:
            raise

        self.coordinates = []
        for i in range(length + 1):
            self.coordinates.append(
                (start[0] + i * orientation[0], start[1] + i * orientation[1], start[2] + i * orientation[2])
            )

    def __repr__(self) -> str:
        if self.name:
            return self.name
        return f"Brick({self.coordinates[0]}~{self.coordinates[-1]})"

    def fall(self, settled_bricks: list["Brick"], update: bool = True) -> bool:
        new_brick_coordinates = [(c[0], c[1], c[2] - 1) for c in self.coordinates]

        if any(c[2] == 0 for c in new_brick_coordinates):
            # print(f"Brick {self} cannot fall - it is at the bottom")
            return True

        for s in settled_bricks:
            settled_brick_coordinates = [(c[0], c[1], c[2]) for c in s.coordinates if s != self]

            if any(c in settled_brick_coordinates for c in new_brick_coordinates):
                # print(f"Brick {self} cannot fall - it is blocked by {s}")
                return True

        if update:
            self.coordinates = new_brick_coordinates
        # print(f"Brick {self} falls")
        return False


falling_bricks = []
all_bricks = []
for i, line in enumerate(input):
    start, end = line.split("~")
    start = tuple(int(c) for c in start.split(","))
    end = tuple(int(c) for c in end.split(","))

    brick = Brick(start, end)
    falling_bricks.append(brick)
    all_bricks.append(str(brick))

# Sort bricks by z-coordinate
falling_bricks = sorted(falling_bricks, key=lambda b: min(c[2] for c in b.coordinates))

settled_bricks = []
for brick in tqdm(falling_bricks):
    settled = False

    while not settled:
        settled = brick.fall(settled_bricks=settled_bricks)

    settled_bricks.append(brick)

# print("\n---\n")

ans = 0
for brick in tqdm(settled_bricks):
    # print(f"\nChecking if {brick} can safely be disintegrated")
    bricks_with_brick_removed = [b for b in settled_bricks.copy() if b != brick]

    n_bricks_that_would_fall = sum(
        not b.fall(settled_bricks=bricks_with_brick_removed, update=True) for b in bricks_with_brick_removed
    )
    # print(f"Disintegrating {brick} would cause {n_bricks_that_would_fall} bricks to fall")
    ans += n_bricks_that_would_fall

print(ans)  # 55105 is too low
