import re

from tqdm import tqdm

input_file_path = "2023/day12/input.txt"

with open(input_file_path, "r") as f:
    input = f.read().splitlines()


def satisfies_spec(conditions, spec):
    matches = re.findall("#+", conditions)
    match_lengths = [len(m) for m in matches]
    return match_lengths == spec


def n_valid_arragements(conditions, spec, position):
    if position == len(conditions):
        return 1 if satisfies_spec(conditions, spec) else 0

    else:
        if conditions[position] == "?":
            return sum([
                n_valid_arragements(conditions[:position] + "#" + conditions[position + 1:], spec, position=position + 1),
                n_valid_arragements(conditions[:position] + "." + conditions[position + 1:], spec, position=position + 1)
            ])
        else:
            return n_valid_arragements(conditions, spec, position=position + 1)


ans = 0
for line in tqdm(input):
    conditions = line.split(" ")[0]
    spec = [int(s) for s in line.split(" ")[1].split(",")]

    ans += n_valid_arragements(conditions, spec, 0)

print(ans)
