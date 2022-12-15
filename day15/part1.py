import re


input_file_path = "day15/input.txt"

with open(input_file_path, 'r') as infile:
    input = infile.read()

y = 2_000_000

overlap_with_y = set()
beacons_on_y = set()

for sensor in input.split("\n"):
    match = re.search(r"Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)", sensor)
    sensor_x, sensor_y, beacon_x, beacon_y = int(match.group(1)), int(match.group(2)), int(match.group(3)), int(match.group(4))

    if beacon_y == y:
        beacons_on_y.add((beacon_x, beacon_y))

    distance_to_closest_sensor = abs(sensor_x - beacon_x) + abs(sensor_y - beacon_y)
    distance_to_y = abs(sensor_y - y)

    if distance_to_closest_sensor >= distance_to_y:
        width_of_diamond_at_y = distance_to_closest_sensor - distance_to_y
        overlap_with_y = overlap_with_y.union(set(range(sensor_x - width_of_diamond_at_y, sensor_x + width_of_diamond_at_y + 1)))

print(beacons_on_y)
print(len(overlap_with_y) - len(beacons_on_y))
