from tqdm import tqdm

input_file_path = "day18/input.txt"

with open(input_file_path, 'r') as infile:
    input = infile.read()

coordinates = []
for coordinate in input.split("\n"):
    x, y, z = coordinate.split(",")
    coordinates.append((int(x), int(y), int(z)))

# A side is exposed if:
#   1. It is not adjacent to rock, and
#   2. It is not adjacent to an air pocket
exposed_sides = 0
for c in tqdm(coordinates):
    if (c[0] + 1, c[1], c[2]) not in coordinates:
        exposed_sides += 1

    if (c[0] - 1, c[1], c[2]) not in coordinates:
        exposed_sides += 1

    if (c[0], c[1] + 1, c[2]) not in coordinates:
        exposed_sides += 1

    if (c[0], c[1] - 1, c[2]) not in coordinates:
        exposed_sides += 1

    if (c[0], c[1], c[2] + 1) not in coordinates:
        exposed_sides += 1

    if (c[0], c[1], c[2] - 1) not in coordinates:
        exposed_sides += 1

print(exposed_sides)