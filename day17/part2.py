import math

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
end = 1_000_000_000_001

states = []
i = 0
while True:
    i += 1
    state = ((i-1) % len(rock_types), f % len(input), max([c[0] for c in occupied]), i)
    states.append(state)

    similar_states = [s for s in states if s[0] == state[0] and s[1] == state[1]]
    if len(similar_states) == 3:
        if similar_states[1][2] - similar_states[0][2] == similar_states[2][2] - similar_states[1][2]:
            if similar_states[1][3] - similar_states[0][3] == similar_states[2][3] - similar_states[1][3]:
                cycle_length = similar_states[1][3] - similar_states[0][3]
                cycle_start = similar_states[0][3]
                cycle_height_increase = similar_states[1][2] - similar_states[0][2]
                print(f"Found cycle of length {cycle_length} starting at {cycle_start}")
                print(f"Every cycle, the height increases by {cycle_height_increase}")

                nof_full_cycles = math.floor((end - cycle_start)/cycle_length)
                height_increase_during_full_cycles = nof_full_cycles * cycle_height_increase
                i = cycle_start + nof_full_cycles * cycle_length
                print(f"Should resume simulation at i={i}; height of {similar_states[0][2] + height_increase_during_full_cycles}")

                cycles_to_run = end - i
                equivalent_start_point = i % cycle_length
                equivalent_end_point = equivalent_start_point + cycles_to_run
                print(f"This is equivalent to the height increase between i={equivalent_start_point} and i={equivalent_end_point}")
                equivalent_end_state_height = [s for s in states if s[3] == equivalent_end_point][0][2]
                ans = equivalent_end_state_height + height_increase_during_full_cycles
                print(ans)
                break

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

            if len(occupied) > 1000:
                occupied = occupied[-1000:]
            # print()
            break
        else:
            # print(f"Rock {i} falls one unit")
            bottom -= 1
            rock_coordinates = [(c[0]-1, c[1]) for c in rock_coordinates]
