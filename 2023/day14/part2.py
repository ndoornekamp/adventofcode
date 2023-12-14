import math


input_file_path = "2023/day14/input.txt"

with open(input_file_path, "r") as f:
    input = f.read().splitlines()


def rotate(matrix):
    """Rotates vectors clockwise"""
    return list(map(list, zip(*matrix[::-1])))


def roll_up(matrix_in):
    matrix_out = []
    for vector in [list(col) for col in zip(*matrix_in)]:
        for start_pos in range(len(vector)):
            if vector[start_pos] in (".", "#"):
                continue

            i = 1
            while True:
                if vector[start_pos - i] in ("O", "#"):
                    break
                elif start_pos - i < 0:
                    break
                else:
                    vector[start_pos - i + 1] = "."
                    vector[start_pos - i] = "O"
                    i += 1

        matrix_out.append(vector)
    return [list(col) for col in zip(*matrix_out)]


matrix = [list(col) for col in input]

n_cycles = 1_000_000_000

cycle = 0
seen_matrices = []
found_cycle = False
while cycle < n_cycles:
    cycle += 1

    for i in range(4):
        matrix = roll_up(matrix)
        matrix = rotate(matrix)

    if not found_cycle:
        if matrix in seen_matrices:
            found_cycle = True
            matrix_seen_at_idx = seen_matrices.index(matrix) + 1
            cycle_length = cycle - matrix_seen_at_idx
            n_cycles_before_end = math.floor((n_cycles - cycle) / cycle_length)
            cycle += n_cycles_before_end * cycle_length
        else:
            seen_matrices.append(matrix)

rows = [list(col) for col in zip(*matrix)]
ans = 0
for column in rows:
    for i, v in enumerate(reversed(column)):
        if v == "O":
            ans += i + 1

print(ans)
