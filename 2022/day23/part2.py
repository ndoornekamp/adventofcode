import time

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

round = 0
elves_moved = 1

tic = time.perf_counter()
while elves_moved > 0:
    print(f"Round {round + 1} ({time.perf_counter() - tic:0.1f}s)")
    proposed_positions = {}
    for elf in elves:
        if not any([(elf[0] + x, elf[1] + y) in elves for x in [-1, 0, 1] for y in [-1, 0, 1] if not (x, y) == (0, 0)]):
            continue

        for i in range(4):
            proposed_direction = directions[(round + i) % len(directions)]
            if not any([(elf[0] + step[0], elf[1] + step[1]) in elves for step in directions_to_check[proposed_direction]]):
                proposed_positions[elf] = (elf[0] + proposed_direction[0], elf[1] + proposed_direction[1])
                break

    proposed_positions_resolved = {}
    for elf, proposed_position in proposed_positions.items():
        elves_proposing_same_position = [e for e, pos in proposed_positions.items() if pos == proposed_position]
        if len(elves_proposing_same_position) > 1:
            pass
        else:
            proposed_positions_resolved[elf] = proposed_position

    elves_new = []
    elves_moved = 0
    for elf in elves:
        if elf in proposed_positions_resolved:
            elves_moved += 1
            elves_new.append(proposed_positions_resolved[elf])
        else:
            elves_new.append(elf)
    elves = list(elves_new)

    round += 1

# 1000 is too low
# 5000 is too high
