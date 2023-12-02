import numpy as np

input_file_path = "day09/input.txt"

with open(input_file_path, 'r') as infile:
    input = infile.read()

head_location, tail_location = np.array((0, 0)), np.array((0, 0))
head_locations, tail_locations = [], []

head_movements = {
    "U": np.array((1, 0)),
    "D": np.array((-1, 0)),
    "R": np.array((0, 1)),
    "L": np.array((0, -1))
}

for head_motion in input.split("\n"):
    direction, steps = head_motion.split(" ")

    for _ in range(int(steps)):
        head_locations.append(head_location)
        head_location = head_location + head_movements[direction]
        print(head_location)

        location_delta = np.subtract(head_location, tail_location)
        print(location_delta)

        xdiff = abs(location_delta[0])
        ydiff = abs(location_delta[1])
        if xdiff + ydiff <= 1:
            print("Head and tail touching directly or overlap")
        elif xdiff == 1 and ydiff == 1:
            print("Head and tail touching diagonally")
        else:
            if xdiff == 0 or ydiff == 0:
                print("Tail moves straight")
                tail_movement = np.array([int(location_delta[0]/2), int(location_delta[1]/2)])
            else:
                print("Tail moves diagonally")
                tail_movement = np.array([max(-1, min(1, location_delta[0])), max(-1, min(1, location_delta[1]))])

            tail_location = tail_location + tail_movement

        print(tail_location)
        tail_locations.append(tail_location)
        print()

print(len(tail_locations))
unique_tail_locations = []
for tail_location in tail_locations:
    if list(tail_location) in unique_tail_locations:
        continue
    else:
        unique_tail_locations.append(list(tail_location))
print(len(unique_tail_locations))