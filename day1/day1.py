import heapq

input_file_path = "day1/input.txt"

with open(input_file_path, 'r') as infile:
    input = infile.readlines()

totals = []
i = 0

for line in input:
    if str(line.strip('\n')) == "":
        i += 1
    else:
        if len(totals) <= i:
            totals.append(0)

        totals[i] += int(line.strip('\n'))

print(max(totals))

top_3_indices = heapq.nlargest(3, range(len(totals)), totals.__getitem__)
print(top_3_indices)

top_3_calories = totals[top_3_indices[0]] + totals[top_3_indices[1]] + totals[top_3_indices[2]]
print(top_3_calories)
