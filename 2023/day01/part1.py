input_file_path = "day01/test_input.txt"

with open(input_file_path, 'r') as f:
    input = f.read().splitlines()

ans = 0
for line in input:
    digits = [int(char) for char in line if char.isdigit()]
    ans += digits[0] * 10 + digits[-1]

print(ans)