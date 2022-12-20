from tqdm import tqdm

input_file_path = "day18/input.txt"

with open(input_file_path, 'r') as infile:
    input = infile.read()

rock_coordinates = []
for coordinate in input.split("\n"):
    x, y, z = coordinate.split(",")
    rock_coordinates.append((int(x), int(y), int(z)))

x_range = (min([c[0] for c in rock_coordinates]) - 1, max([c[0] for c in rock_coordinates]) + 2)
y_range = (min([c[1] for c in rock_coordinates]) - 1, max([c[1] for c in rock_coordinates]) + 2)
z_range = (min([c[2] for c in rock_coordinates]) - 1, max([c[2] for c in rock_coordinates]) + 2)

all_coordinates = []
for x in tqdm(range(x_range[0], x_range[1])):
    for y in range(y_range[0], y_range[1]):
        for z in range(z_range[0], z_range[1]):
            c = (x, y, z)
            all_coordinates.append(c)

non_pocket_air = [(x_range[0], y_range[0], z_range[0])]
assert non_pocket_air[0] not in rock_coordinates

non_pocket_air = set(non_pocket_air)
while True:
    start_len = len(non_pocket_air)
    for c in all_coordinates:
        if c in rock_coordinates:
            continue

        if any([
            (c[0] + 1, c[1], c[2]) in non_pocket_air,
            (c[0] - 1, c[1], c[2]) in non_pocket_air,
            (c[0], c[1] + 1, c[2]) in non_pocket_air,
            (c[0], c[1] - 1, c[2]) in non_pocket_air,
            (c[0], c[1], c[2] + 1) in non_pocket_air,
            (c[0], c[1], c[2] - 1) in non_pocket_air
        ]):
            non_pocket_air.add(c)
    if len(non_pocket_air) == start_len:
        break

air_pockets = [c for c in all_coordinates if c not in non_pocket_air and c not in rock_coordinates]
print(f"Found {len(air_pockets)} that are (part of) an air pocket")

# A side is exposed if:
#   1. It is not adjacent to rock, and
#   2. It is not adjacent to an air pocket
exposed_sides = 0
for c in tqdm(rock_coordinates):
    if (c[0] + 1, c[1], c[2]) in non_pocket_air:
        exposed_sides += 1

    if (c[0] - 1, c[1], c[2]) in non_pocket_air:
        exposed_sides += 1

    if (c[0], c[1] + 1, c[2]) in non_pocket_air:
        exposed_sides += 1

    if (c[0], c[1] - 1, c[2]) in non_pocket_air:
        exposed_sides += 1

    if (c[0], c[1], c[2] + 1) in non_pocket_air:
        exposed_sides += 1

    if (c[0], c[1], c[2] - 1) in non_pocket_air:
        exposed_sides += 1

# 2585 is too low
# 2600 is too low
print(exposed_sides)