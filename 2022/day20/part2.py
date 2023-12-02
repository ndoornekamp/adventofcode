from dataclasses import dataclass
from tqdm import tqdm


input_file_path = "day20/input.txt"

with open(input_file_path, 'r') as infile:
    input = infile.read()


@dataclass
class Number:
    value: int
    original_index: int


decryption_key = 811589153
current_list = [Number(value=int(number) * decryption_key, original_index=i) for i, number in enumerate(input.split("\n"))]

for _ in tqdm(range(10)):
    for i in tqdm(range(len(current_list))):
        number = [number for number in current_list if number.original_index == i][0]
        current_index = current_list.index(number)

        new_index = (current_index + number.value) % (len(current_list) - 1)

        if new_index == 0:
            new_index = len(current_list) - 1

        # print(f"{number.value} moves from index {current_index} to index {new_index}")
        current_list.pop(current_index)
        current_list.insert(new_index, number)

        # print([number.value for number in current_list])

index_of_zero = current_list.index([number for number in current_list if number.value == 0][0])

if input_file_path == "day20/test_input.txt":
    assert current_list[(1000 + index_of_zero) % len(current_list)].value == 811589153
    assert current_list[(2000 + index_of_zero) % len(current_list)].value == 2434767459
    assert current_list[(3000 + index_of_zero) % len(current_list)].value == -1623178306

ans = sum([
    current_list[(1000 + index_of_zero) % len(current_list)].value,
    current_list[(2000 + index_of_zero) % len(current_list)].value,
    current_list[(3000 + index_of_zero) % len(current_list)].value,
])

# 8554 is too high for test input
print(ans)
