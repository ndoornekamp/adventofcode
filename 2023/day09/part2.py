
input_file_path = '2023/day09/input.txt'

with open(input_file_path, 'r') as f:
    input = f.read().splitlines()

ans = 0
for line in input:
    original_sequence = [int(v) for v in line.split(" ")]
    sequences = [original_sequence]

    sequence = original_sequence
    while not all(v == 0 for v in sequence):
        differences = [j-i for i, j in zip(sequence[:-1], sequence[1:])]
        sequences = [differences] + sequences
        sequence = differences

    for sequence in sequences:
        print(sequence)

    sequences[0] = [0] + sequences[0]
    for i, sequence in enumerate(sequences[1:], start=1):
        sequence.insert(0, sequence[0] - sequences[i-1][0])

    for sequence in sequences:
        print(sequence)
    print()

    ans += sequences[-1][0]

print(ans)
