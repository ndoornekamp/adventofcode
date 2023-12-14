input_file_path = '2023/day14/input.txt'

with open(input_file_path, 'r') as f:
    input = f.read().splitlines()


def roll(vectors_in):
    vectors_out = []
    for vector in [list(col) for col in zip(*vectors_in)]:
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

        vectors_out.append(vector)
    return vectors_out

ans = 0
columns_out = roll(input)
for column in columns_out:
    for i, v in enumerate(reversed(column)):
        if v == "O":
            ans += i + 1

print(ans)