
input_file_path = '2023/day06/input.txt'

with open(input_file_path, 'r') as f:
    input = f.read().splitlines()

durations = [int(d) for d in input[0].split(" ") if d.isdigit()]
record_distances = [int(d) for d in input[1].split(" ") if d.isdigit()]

ans = 1
for duration, record_distance in zip(durations, record_distances):
    nof_durations_beating_record_distance = 0
    for hold_seconds in range(duration):
        distance_traveled = (duration - hold_seconds) * hold_seconds

        if distance_traveled > record_distance:
            nof_durations_beating_record_distance += 1

    ans *= nof_durations_beating_record_distance

print(ans)