from tqdm import tqdm

input_file_path = "day18/test_input.txt"

with open(input_file_path, 'r') as infile:
    input = infile.read()

coordinates = []
for coordinate in input.split("\n"):
    x, y, z = coordinate.split(",")
    coordinates.append((int(x), int(y), int(z)))

exposed_sides = 0
for c1 in tqdm(coordinates):
    if not any([(c1[0] + 1 == c2[0] and c1[1] == c2[1] and c1[2] == c2[2]) for c2 in coordinates]):
        # c1 is not covered by any other cube in the positive x-direction
        exposed_sides += 1

    if not any([(c1[0] - 1 == c2[0] and c1[1] == c2[1] and c1[2] == c2[2]) for c2 in coordinates]):
        # c1 is not covered by any other cube in the negative x-direction
        exposed_sides += 1

    if not any([(c1[0] == c2[0] and c1[1] + 1 == c2[1] and c1[2] == c2[2]) for c2 in coordinates]):
        # c1 is not covered by any other cube in the positive y-direction
        exposed_sides += 1

    if not any([(c1[0] == c2[0] and c1[1] - 1 == c2[1] and c1[2] == c2[2]) for c2 in coordinates]):
        # c1 is not covered by any other cube in the negative y-direction
        exposed_sides += 1

    if not any([(c1[0] == c2[0] and c1[1] == c2[1] and c1[2] + 1 == c2[2]) for c2 in coordinates]):
        # c1 is not covered by any other cube in the positive z-direction
        exposed_sides += 1

    if not any([(c1[0] == c2[0] and c1[1] == c2[1] and c1[2] - 1 == c2[2]) for c2 in coordinates]):
        # c1 is not covered by any other cube in the negative z-direction
        exposed_sides += 1

print(exposed_sides)