
from collections import OrderedDict
import math


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

boxes = [OrderedDict() for _ in range(256)]
for step in input:
    if "=" in step:
        label = step.split("=")[0]
        box = hash(label)

        focal_length = int(step.split("=")[1])
        boxes[box][label] = focal_length
    elif "-" in step:
        label = step.split("-")[0]
        box = hash(label)

        print(f"Remove lens with label {label} from box {box}")
        if label in boxes[box]:
            del boxes[box][label]
    else:
        raise

ans = 0
for i, box in enumerate(boxes):
    for j, (label, focal_length) in enumerate(box.items()):
        print(label, i + 1, j + 1, focal_length)
        ans += math.prod((i + 1, j + 1, focal_length))

print(ans)
