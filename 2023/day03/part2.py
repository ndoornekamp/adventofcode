
from collections import defaultdict
import math
import re


input_file_path = '2023/day03/input.txt'

with open(input_file_path, 'r') as f:
    input = f.read().splitlines()

gear_coordinates = []
for i, line in enumerate(input):
    gears = re.finditer(r"\*", line)
    for gear in gears:
        gear_coordinates.append((i, gear.span()[0]))


def coordinates_are_adjacent(coordinate1, coordinate2):
    coordinates_adjacent_to_coordinate_2 = []
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            coordinates_adjacent_to_coordinate_2.append((coordinate2[0] + i, coordinate2[1] + j))

    return coordinate1 in coordinates_adjacent_to_coordinate_2


numbers_adjacent_to_gears = defaultdict(set)
for i, line in enumerate(input):
    numbers = re.finditer(r"(\d+)", line)
    for number in numbers:
        for j in range(*number.span()):
            number_coordinate = (i, j)

            for gear_coordinate in gear_coordinates:
                if coordinates_are_adjacent(number_coordinate, gear_coordinate):
                    numbers_adjacent_to_gears[gear_coordinate].add(number)

ans = 0
for gear, adjacent_numbers in numbers_adjacent_to_gears.items():
    if len(adjacent_numbers) < 2:
        continue

    assert len(adjacent_numbers) == 2

    gear_ratio = math.prod([int(match.group(1)) for match in adjacent_numbers])
    ans += gear_ratio

print(ans)
