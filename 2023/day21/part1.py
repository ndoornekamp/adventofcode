
input_file_path = '2023/day21/input.txt'

with open(input_file_path, 'r') as f:
    input = f.read().splitlines()

grid = {}
for i, line in enumerate(input):
    for j, val in enumerate(line):
        grid[(i, j)] = val

starting_position = [c for c in grid if grid[c] == "S"][0]


def reachable_after_1_step(grid, starting_position):
    reachable = set()
    for direction in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        position = (starting_position[0] + direction[0], starting_position[1] + direction[1])
        if grid.get(position, None) in ("S", "."):
            reachable.add(position)

    return reachable


n_steps = 64
starting_positions = [starting_position]

for n in range(n_steps):
    reachable = set()
    for position in starting_positions:
        reachable = reachable.union(reachable_after_1_step(grid, position))

    print(f"Able to reach {len(reachable)} positions after {n + 1} steps")
    starting_positions = reachable

    # for i in range(len(input)):
    #     for j in range(len(input[0])):
    #         if (i, j) in reachable:
    #             print("O", end="")
    #         else:
    #             print(grid[(i, j)], end="")
    #     print()

