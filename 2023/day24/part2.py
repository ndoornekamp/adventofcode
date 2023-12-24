import z3

input_file_path = "2023/day24/input.txt"

with open(input_file_path, "r") as f:
    input = f.read().splitlines()

# Find (x, y, z, dx, dy, dz) such that for every stone there is some time at which the stone intersects with the rock
# This is a system of linear equations, so we'll use z3 to do the heavy lifting for us
x, dx, y, dy, z, dz = z3.Reals("x dx y dy z dz")
solver = z3.Solver()

# Fun trick: assuming there is a solution, only three equations need to be considered, as three points on the
# trajectory of the rock are enough to uniquely determine it.
for i, line in enumerate(input[:3]):
    t = z3.Real(f"t{i}")  # Time at which this stone intersects with the rock

    coordinate, direction = line.split(" @ ")
    coordinate = [int(c) for c in coordinate.split(", ")]
    direction = [int(d) for d in direction.split(", ")]

    solver.add(
        coordinate[0] + direction[0] * t == x + dx * t,
        coordinate[1] + direction[1] * t == y + dy * t,
        coordinate[2] + direction[2] * t == z + dz * t,
    )

solver.check()
model = solver.model()

ans = model[x].as_long() + model[y].as_long() + model[z].as_long()
print(ans)
