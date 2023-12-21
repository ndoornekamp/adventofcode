input_file_path = "2023/day21/test_input.txt"

with open(input_file_path, "r") as f:
    input = f.read().splitlines()

n_repeats = 5
data_repeated = []
for i in range(n_repeats):
    for line in input:
        data_repeated.append(n_repeats * line.replace("S", "."))
input = data_repeated

n_rows = len(input)
n_cols = len(input[0])

grid = {}
for i, line in enumerate(input):
    for j, val in enumerate(line):
        for ii in range(n_repeats):
            for jj in range(n_repeats):
                grid[(i + ii * n_rows, j + jj * n_cols)] = val
                grid[(i - ii * n_rows, j - jj * n_cols)] = val

starting_position = (n_rows // 2, n_cols // 2)


def reachable_after_1_step(grid, starting_position):
    reachable = set()
    for direction in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        position = (starting_position[0] + direction[0], starting_position[1] + direction[1])
        if grid.get(position, None) in ("S", "."):
            reachable.add(position)

    return reachable


n_steps = 50
starting_positions = [starting_position]

for n in range(n_steps):
    reachable = set()
    for position in starting_positions:
        reachable = reachable.union(reachable_after_1_step(grid, position))

    print(f"Able to reach {len(reachable)} positions after {n + 1} steps")
    starting_positions = reachable
