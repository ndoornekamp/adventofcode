import math


input_file_path = "2023/day13/input.txt"

with open(input_file_path, "r") as f:
    input_text = f.read()


def row_is_mirrored_at_idx(row, idx):
    distance_to_edge = min(idx, len(row) - idx - 2)

    str_left = "".join(row[idx - distance_to_edge: idx + 1])
    str_right = "".join(list(reversed(row[idx + 1: idx + 2 + distance_to_edge])))

    return str_left == str_right


ans = 0
for pattern in input_text.split("\n\n"):
    n_cols = len(pattern.split("\n")[0])
    n_rows = len(pattern.split("\n"))

    rows = pattern.split("\n")

    # Calculate the old answer - we want to find a different one
    # Not exactly DRY, but can't be bothered to refactor
    for i, row in enumerate(rows):
        # Check if a line between rows i and i+1 could be a mirror
        # If it is, row i has to be equal to row i+1, row i-1 to row i+2, etc.

        if i == len(rows) - 1:
            continue

        distance_to_edge = min(i, len(rows) - i - 2)
        if all([rows[i - j] == rows[i + 1 + j] for j in range(distance_to_edge + 1)]):
            print(f"Old answer: Mirror between rows {i + 1} and {i + 2}")
            old_ans = 100 * (i + 1)

    for col_idx in range(n_cols - 1):
        # For every column index, check if for every row, the numbers after that index are the reverse of the numbers
        # before the index

        if all([row_is_mirrored_at_idx(row, col_idx) for row in rows]):
            print(f"Old answer: Mirror between columns {col_idx + 1} and {col_idx + 2}")
            old_ans = col_idx + 1

    # Brute-force try every replacement and see if we find a new mirror line
    for replacement_idx in range(n_cols * n_rows):
        rows = [list(r) for r in pattern.split("\n")]

        replacement_row = math.floor(replacement_idx/n_cols)
        replacement_col = replacement_idx % n_cols

        if rows[replacement_row][replacement_col] == ".":
            rows[replacement_row][replacement_col] = "#"
        else:
            rows[replacement_row][replacement_col] = "."

        for i, row in enumerate(rows):
            # Check if a line between rows i and i+1 could be a mirror
            # If it is, row i has to be equal to row i+1, row i-1 to row i+2, etc.

            if i == len(rows) - 1:
                continue

            distance_to_edge = min(i, len(rows) - i - 2)
            if all([rows[i - j] == rows[i + 1 + j] for j in range(distance_to_edge + 1)]):
                if old_ans != 100 * (i + 1):
                    print(f"New answer: Mirror between rows {i + 1} and {i + 2}")
                    ans += (100 * (i + 1))/2  # We'll find every new line twice -> divide by two

        for col_idx in range(n_cols - 1):
            # For every column index, check if for every row, the numbers after that index are the reverse of the
            # numbers before the index

            if col_idx == 2 and replacement_idx == 120:
                print()

            if all([row_is_mirrored_at_idx(row, col_idx) for row in rows]):
                if old_ans != col_idx + 1:
                    print(f"New answer: Mirror between columns {col_idx + 1} and {col_idx + 2}")
                    ans += (col_idx + 1)/2  # We'll find every new line twice -> divide by two

print(int(ans))
