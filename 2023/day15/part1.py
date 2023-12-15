
input_file_path = '2023/day15/input.txt'

with open(input_file_path, 'r') as f:
    input = f.read().strip().split(",")


def hash(string: str) -> int:
    current_value = 0
    for char in string:
        current_value += ord(char)
        current_value = (17 * current_value) % 256
    return current_value


assert hash("HASH") == 52
assert hash("rn=1") == 30

ans = 0
for string in input:
    ans += hash(string)

print(ans)  # 511513 is too high
