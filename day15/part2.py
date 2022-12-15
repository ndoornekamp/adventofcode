import re

from tqdm import tqdm


input_file_path = "day15/input.txt"
# input_file_path = "day15/test_input.txt"

with open(input_file_path, 'r') as infile:
    input = infile.read()

x_min = y_min = 0
x_max = y_max = 4000000
# x_max = y_max = 20

sensors = []
for sensor in input.split("\n"):
    match = re.search(r"Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)", sensor)
    sensor_x, sensor_y, beacon_x, beacon_y = int(match.group(1)), int(match.group(2)), int(match.group(3)), int(match.group(4))
    sensors.append([sensor_x, sensor_y, beacon_x, beacon_y])


def sensor_coverage_at_y(sensor, y):
    sensor_x, sensor_y, beacon_x, beacon_y = sensor
    distance_to_closest_sensor = abs(sensor_x - beacon_x) + abs(sensor_y - beacon_y)
    distance_to_y = abs(sensor_y - y)

    if distance_to_closest_sensor >= distance_to_y:
        width_of_diamond_at_y = distance_to_closest_sensor - distance_to_y

        return sensor_x - width_of_diamond_at_y, sensor_x + width_of_diamond_at_y
    else:
        return None, None


for y in tqdm(range(y_min, y_max+1)):
    sensor_ranges = [sensor_coverage_at_y(sensor, y) for sensor in sensors]
    sensor_ranges = [sensor_range for sensor_range in sensor_ranges if sensor_range[0]]

    for range_a in sensor_ranges:
        for range_b in sensor_ranges:
            if range_a == range_b:
                continue

            if range_a[0] == range_b[1] + 2:
                # print(f"Exactly one space between {range_a} and {range_b} at y={y}")
                x = range_b[1] + 1  # Candidate x coordinate
                if not any([r[0] < x <= r[1] for r in sensor_ranges]):
                    print(x * 4000000 + y)
