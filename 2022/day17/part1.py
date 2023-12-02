rock_types = [
    "####",
    ".#.\n###\n.#.",
    "..#\n..#\n###",
    "#\n#\n#\n#",
    "##\n##"
]

input_file_path = "day17/input.txt"

with open(input_file_path, 'r') as infile:
    input = list(infile.read())

k = 0
f = -1
top = 0
floor = [(0, i) for i in range(7)]
occupied = list(floor)

for i in range(1, 2023):
    rock_type = rock_types[(i-1) % len(rock_types)]
    rock_width = len(list(rock_type.split("\n")[0]))
    bottom = max([c[0] for c in occupied]) + 4

    rock_coordinates = []
    for j, row in enumerate(reversed(rock_type.split("\n"))):
        for k, pixel in enumerate(row):
            if pixel == "#":
                rock_coordinates.append((bottom + j, 2 + k))

    # print(f"Rock {i} begins falling and occupies the following coordinates: {rock_coordinates}")

    while True:
        f += 1
        jet_pattern = input[f % len(input)]
        if jet_pattern == ">":
            if max([c[1] for c in rock_coordinates]) >= 6:
                # print(f"Rock {i} can't move any further to the right because of the chamber wall")
                pass
            elif any([c in occupied for c in [(c[0], c[1]+1) for c in rock_coordinates]]):
                # print(f"Rock {i} can't move any further to the right because of another rock")
                pass
            else:
                rock_coordinates = [(c[0], c[1]+1) for c in rock_coordinates]
                # print(f"Rock {i} is pushed to the right; the right edge is now at {max([c[1] for c in rock_coordinates])}")
        else:
            if min([c[1] for c in rock_coordinates]) <= 0:
                # print(f"Rock {i} can't move any further to the left because of the chamber wall")
                pass
            elif any([c in occupied for c in [(c[0], c[1]-1) for c in rock_coordinates]]):
                # print(f"Rock {i} can't move any further to the left because of another rock")
                pass
            else:
                rock_coordinates = [(c[0], c[1]-1) for c in rock_coordinates]
                # print(f"Rock {i} is pushed to the left; the left edge is now at {min([c[1] for c in rock_coordinates])}")

        if any([c in occupied for c in [(c[0]-1, c[1]) for c in rock_coordinates]]):
            # print(f"Rock {i} falls one unit, causing it to come to rest at {rock_coordinates}")
            for c in rock_coordinates:
                occupied.append(c)
            # print()
            break
        else:
            # print(f"Rock {i} falls one unit")
            bottom -= 1
            rock_coordinates = [(c[0]-1, c[1]) for c in rock_coordinates]

# for r in reversed(range(max([c[0] for c in occupied]) + 3)):
#     row = ""
#     for c in range(7):
#         if (r, c) in occupied:
#             row += "#"
#         else:
#             row += "."
#     print(row)

print(max([c[0] for c in occupied]))
