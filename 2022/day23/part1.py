import numpy as np

from tqdm import tqdm

input_file_path = "day23/input.txt"

with open(input_file_path, 'r') as infile:
    input = infile.read()

elves = []
for i, row in enumerate(input.split("\n")):
    for j, position in enumerate(list(row)):
        if position == "#":
            elves.append((i, j))

N = (-1, 0)
NE = (-1, 1)
NW = (-1, -1)
S = (1, 0)
SE = (1, 1)
SW = (1, -1)
W = (0, -1)
E = (0, 1)

directions = [N, S, W, E]
directions_to_check = {
    N: [N, NE, NW],
    S: [S, SE, SW],
    W: [W, NW, SW],
    E: [E, NE, SE]
}

# rectangle_width = max([e[0] for e in elves]) - min([e[0] for e in elves]) + 1
# rectangle_height = max([e[1] for e in elves]) - min([e[1] for e in elves]) + 1
# print("Initial state")
# for i in range(min([e[0] for e in elves]), min([e[0] for e in elves]) + rectangle_width):
#     row = ""
#     for j in range(min([e[1] for e in elves]), min([e[1] for e in elves]) + rectangle_height):
#         if (i, j) in elves:
#             row += "#"
#         else:
#             row += "."
#     print(row)
# print()

for round in tqdm(range(10)):
    proposed_positions = {}
    for elf in elves:
        if not any([tuple(np.array(elf) + np.array((x, y))) in elves for x in [-1, 0, 1] for y in [-1, 0, 1] if not (x, y) == (0, 0)]):
            # print(f"The elf at {elf} has no direct neighbors, so it does not do anything this round")
            continue

        for i in range(4):
            proposed_direction = directions[(round + i) % len(directions)]
            if not any([tuple(np.array(elf) + np.array(step)) in elves for step in directions_to_check[proposed_direction]]):
                proposed_positions[elf] = tuple(np.array(elf) + np.array(proposed_direction))
                # print(f"The elf at {elf} proposes to move {proposed_direction} to {tuple(np.array(elf) + np.array(proposed_direction))}")
                break

        # if elf not in proposed_positions:
        #     print(f"The elf at {elf} is unable to move anywhere")

    proposed_positions_resolved = {}
    for elf, proposed_position in proposed_positions.items():
        elves_proposing_same_position = [e for e, pos in proposed_positions.items() if pos == proposed_position]
        if len(elves_proposing_same_position) > 1:
            pass
            # print(f"{len(elves_proposing_same_position) - 1} other elves were proposing to move to {proposed_position}, so the elf at {elf} will remain in their current position")
        else:
            proposed_positions_resolved[elf] = proposed_position

    elves_new = []
    for elf in elves:
        if elf in proposed_positions_resolved:
            elves_new.append(proposed_positions_resolved[elf])
            # print(f"The elf at {elf} moves to {proposed_positions_resolved[elf]}")
        else:
            elves_new.append(elf)
            # print(f"The elf at {elf} remains in their current position")
    elves = list(elves_new)

    rectangle_width = max([e[0] for e in elves]) - min([e[0] for e in elves]) + 1
    rectangle_height = max([e[1] for e in elves]) - min([e[1] for e in elves]) + 1

    # print(f"End of round {round + 1}")
    # for i in range(min([e[0] for e in elves]), min([e[0] for e in elves]) + rectangle_width):
    #     row = ""
    #     for j in range(min([e[1] for e in elves]), min([e[1] for e in elves]) + rectangle_height):
    #         if (i, j) in elves:
    #             row += "#"
    #         else:
    #             row += "."
    #     print(row)
    # print()

rectangle_width = max([e[0] for e in elves]) - min([e[0] for e in elves]) + 1
rectangle_height = max([e[1] for e in elves]) - min([e[1] for e in elves]) + 1
nof_rectangle_tiles = rectangle_height * rectangle_width
print(f"The rectangle is {rectangle_width} wide and {rectangle_height} high -> {nof_rectangle_tiles} tiles")

nof_ground_tiles = nof_rectangle_tiles - len(elves)
print(f"Of those, {len(elves)} are covered by elves, so there are {nof_ground_tiles} ground tiles remaining")
