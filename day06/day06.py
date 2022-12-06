input_file_path = "day06/input.txt"

with open(input_file_path, 'r') as infile:
    input = infile.read()

print(input)

nbuf = 14
for i in range(nbuf, len(input)):
    buffer = input[i-nbuf:i]
    if len(buffer) == len(set(buffer)):
        # Buffer contains nbuf unique characters
        print(i)
        break