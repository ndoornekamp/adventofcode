import numpy as np

input_file_path = "day09/input.txt"

with open(input_file_path, 'r') as infile:
    input = infile.read()

tail_locations = []

knot_locations = [np.array((0, 0)) for _ in range(10)]

head_movements = {
    "U": np.array((1, 0)),
    "D": np.array((-1, 0)),
    "R": np.array((0, 1)),
    "L": np.array((0, -1))
}

for head_motion in input.split("\n"):
    direction, steps = head_motion.split(" ")

    for _ in range(int(steps)):
        knot_locations[0] = knot_locations[0] + head_movements[direction]

        for i in range(1, 10):
            location_delta = np.subtract(knot_locations[i-1], knot_locations[i])

            xdiff = abs(location_delta[0])
            ydiff = abs(location_delta[1])
            if xdiff + ydiff <= 1:
                # print("Head and knot touching directly or overlap")
                pass
            elif xdiff == 1 and ydiff == 1:
                # print("Head and tail touching diagonally")
                pass
            else:
                if xdiff == 0 or ydiff == 0:
                    # print("Tail moves straight")
                    knot_movement = np.array([int(location_delta[0]/2), int(location_delta[1]/2)])
                else:
                    # print("Tail moves diagonally")
                    knot_movement = np.array([max(-1, min(1, location_delta[0])), max(-1, min(1, location_delta[1]))])

                knot_locations[i] = knot_locations[i] + knot_movement

        tail_locations.append(knot_locations[-1])

unique_tail_locations = []
for tail_location in tail_locations:
    if list(tail_location) in unique_tail_locations:
        continue
    else:
        unique_tail_locations.append(list(tail_location))
print(len(unique_tail_locations))
