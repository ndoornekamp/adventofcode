import numpy as np

input_file_path = "day14/input.txt"

with open(input_file_path, 'r') as infile:
    input = infile.read()

grid = np.zeros((300, 900))
max_rock_y_coordinate = 0
for rock_formation in input.split("\n"):
    coordinates = rock_formation.split(" -> ")
    for i, start_coordinate in enumerate(coordinates):
        if i == len(coordinates) - 1:
            continue  # Last coordinate = end of last rock formation line

        col_start, row_start = start_coordinate.split(",")
        col_end, row_end = coordinates[i+1].split(",")

        col_start, row_start, col_end, row_end = int(col_start), int(row_start), int(col_end), int(row_end)

        if col_start == col_end:
            # print(f"Vertical line from {min(row_start, row_end)} to {max(row_start, row_end)+1}")
            for d in range(min(row_start, row_end), max(row_start, row_end)+1):
                if d > max_rock_y_coordinate:
                    max_rock_y_coordinate = d
                grid[d][col_start] = 1
        else:
            assert row_start == row_end
            # print(f"Horizontal line from {min(col_start, col_end)} to {max(col_start, col_end)+1}")
            for d in range(min(col_start, col_end), max(col_start, col_end)+1):
                grid[row_start][d] = 1

print(f"The floor is at y-coordinate {max_rock_y_coordinate}")
for col in range(0, 900):
    grid[max_rock_y_coordinate+2][col] = 1

nof_units = 0
while True:
    nof_units += 1
    sand_location = (0, 500)

    while True:
        for d in [(1, 0), (1, -1), (1, 1)]:
            new_sand_location = tuple(np.array(sand_location) + np.array(d))

            if grid[new_sand_location] == 0:
                sand_location = new_sand_location
                break
        else:  # Sand came to rest
            grid[sand_location] = 1
            if sand_location == (0, 500):
                print(f"{nof_units} came to rest before blocking the source")
                raise
            break
