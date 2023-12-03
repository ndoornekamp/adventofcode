
import re


input_file_path = '2023/day03/input.txt'

with open(input_file_path, 'r') as f:
    input = f.read().splitlines()

symbol_coordinates = []
for i, line in enumerate(input):
    symbols = re.finditer(r"[^\d.]", line)
    for symbol in symbols:
        symbol_coordinates.append((i, symbol.span()[0]))


def coordinate_is_adjacent_to_symbol(coordinate, symbol_coordinate):
    coordinates_adjacent_to_symbol = []
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            coordinates_adjacent_to_symbol.append((symbol_coordinate[0] + i, symbol_coordinate[1] + j))

    return coordinate in coordinates_adjacent_to_symbol


ans = 0
for i, line in enumerate(input):
    numbers = re.finditer(r"(\d+)", line)
    for number in numbers:
        for j in range(*number.span()):
            if any(coordinate_is_adjacent_to_symbol((i, j), symbol_coordinate) for symbol_coordinate in symbol_coordinates):
                ans += int(number.group(1))
                break

print(ans)
