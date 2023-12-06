
input_file_path = '2023/day06/input.txt'

with open(input_file_path, 'r') as f:
    input = f.read().splitlines()

duration = int("".join([c for c in input[0].split(":")[1] if c.isdigit()]))
record_distance = int("".join([c for c in input[1].split(":")[1] if c.isdigit()]))

ans = 0
for hold_seconds in range(duration):
    distance_traveled = (duration - hold_seconds) * hold_seconds

    if distance_traveled > record_distance:
        ans += 1

print(ans)

# Alternatively: solve duration*hold_seconds - hold_seconds ** 2 == record_distance for hold_seconds;
# the answer is the number of integers between the two solutions.