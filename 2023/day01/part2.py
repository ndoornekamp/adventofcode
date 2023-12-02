import regex as re

input_file_path = "day01/input.txt"

with open(input_file_path, 'r') as f:
    input = f.read().splitlines()

spelled_digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
digits = [str(i) for i in range(1, 10)]
regex = "|".join(spelled_digits + digits)


def get_digit_value(digit_str) -> int:
    return int(digit_str) if digit_str in digits else spelled_digits.index(digit_str) + 1


ans = 0
for line in input:
    all_digits = re.findall(regex, line, overlapped=True)
    print(all_digits, get_digit_value(all_digits[0]), get_digit_value(all_digits[-1]))
    ans += 10 * get_digit_value(all_digits[0]) + get_digit_value(all_digits[-1])

print(ans)
