
input_file_path = '2023/day18/input.txt'

with open(input_file_path, 'r') as f:
    input = f.read().splitlines()


def move(t1, t2):
    return (t1[0] + t2[0], t1[1] + t2[1])


start = (0, 0)
directions = {"R": (0, 1), "D": (1, 0), "L": (0, -1), "U": (-1, 0)}

location = start
trench = []
for line in input:
    direction, n_steps, color = line.split(" ")

    for _ in range(int(n_steps)):
        new_location = move(location, directions[direction])
        trench.append(new_location)
        location = new_location

# Shoelace formula: area inside polygon = sum(x1 * y2 - x2 * y1) / 2
sum = 0
for i in range(len(trench) - 1):
    x1, y1 = trench[i]
    x2, y2 = trench[i + 1]
    sum += x1 * y2 - x2 * y1

# Shoelace formula assumes we traverse the polygon so if you go from (x1, y1) to (x2, y2), the interior is to your
# right. If that is not the case, the area will be negative.
area = abs(sum) / 2

# Pick's theorem: A = i + b/2 - 1 ==> i = A - b/2 + 1
n_interior_points = int(area - len(trench) / 2 + 1)
print(n_interior_points + len(trench))
