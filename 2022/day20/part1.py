from dataclasses import dataclass


input_file_path = "day20/input.txt"

with open(input_file_path, 'r') as infile:
    input = infile.read()


@dataclass
class Number:
    value: int
    original_index: int


current_list = [Number(value=int(number), original_index=i) for i, number in enumerate(input.split("\n"))]

testcases = [
    [1, 2, -3, 3, -2, 0, 4],
    [2, 1, -3, 3, -2, 0, 4],
    [1, -3, 2, 3, -2, 0, 4],
    [1, 2, 3, -2, -3, 0, 4],
    [1, 2, -2, -3, 0, 3, 4],
    [1, 2, -3, 0, 3, 4, -2],
    [1, 2, -3, 0, 3, 4, -2],
    [1, 2, -3, 4, 0, 3, -2]
]

for i in range(len(current_list)):
    number = [number for number in current_list if number.original_index == i][0]
    current_index = current_list.index(number)

    new_index = (current_index + number.value) % (len(current_list) - 1)

    if new_index == 0:
        new_index = len(current_list) - 1

    # print(f"{number.value} moves from index {current_index} to index {new_index}")
    current_list.pop(current_index)
    current_list.insert(new_index, number)

    # print([number.value for number in current_list])
    if input_file_path == "day20/test_input.txt":
        assert testcases[i+1] == [number.value for number in current_list]

index_of_zero = current_list.index([number for number in current_list if number.value == 0][0])

if input_file_path == "day20/test_input.txt":
    assert current_list[(1000 + index_of_zero) % len(current_list)].value == 4
    assert current_list[(2000 + index_of_zero) % len(current_list)].value == -3
    assert current_list[(3000 + index_of_zero) % len(current_list)].value == 2

ans = sum([
    current_list[(1000 + index_of_zero) % len(current_list)].value,
    current_list[(2000 + index_of_zero) % len(current_list)].value,
    current_list[(3000 + index_of_zero) % len(current_list)].value,
])

# 8554 is too high for test input
print(ans)
