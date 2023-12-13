input_file_path = "2023/day13/input.txt"

with open(input_file_path, "r") as f:
    input = f.read()


def row_is_mirrored_at_idx(row, idx):
    distance_to_edge = min(idx, len(row) - idx - 2)

    str_left = row[idx - distance_to_edge: idx + 1]
    str_right = "".join(list(reversed(row[idx + 1: idx + 2 + distance_to_edge])))

    return str_left == str_right


ans = 0
for pattern in input.split("\n\n"):
    print("\nPattern")
    rows = pattern.split("\n")
    for i, row in enumerate(rows):
        # Check if a line between rows i and i+1 could be a mirror
        # If it is, row i has to be equal to row i+1, row i-1 to row i+2, etc.

        if i == len(rows) - 1:
            continue

        # Problem: set the next range properly
        distance_to_edge = min(i, len(rows) - i - 2)
        if all([rows[i - j] == rows[i + 1 + j] for j in range(distance_to_edge + 1)]):
            print(f"Mirror between rows {i + 1} and {i + 2}")
            ans += 100 * (i + 1)

    n_cols = len(rows[0])
    for col_idx in range(n_cols - 1):
        # For every column index, check if for every row, the numbers after that index are the reverse of the numbers
        # before the index

        if all([row_is_mirrored_at_idx(row, col_idx) for row in rows]):
            print(f"Mirror between columns {col_idx + 1} and {col_idx + 2}")
            ans += col_idx + 1

print(ans)  # 28558 is too low
