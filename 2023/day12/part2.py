from functools import cache
import re

from tqdm import tqdm

input_file_path = "2023/day12/test_input.txt"

with open(input_file_path, "r") as f:
    input = f.read().splitlines()


def satisfies_spec(conditions, spec):
    matches = re.findall("#+", conditions)
    match_lengths = tuple([len(m) for m in matches])
    return match_lengths == spec


# @cache
def n_valid_arrangements(conditions, spec, position):
    if position == len(conditions):
        return 1 if satisfies_spec(conditions, spec) else 0

    if conditions.count("#") > sum(spec):
        return 0

    if conditions.count("?") + conditions.count("#") < sum(spec):
        return 0

    if conditions[position] == "?":
        return sum(
            [
                n_valid_arrangements(
                    conditions[:position] + "#" + conditions[position + 1:],
                    spec,
                    position=position + 1,
                ),
                n_valid_arrangements(
                    conditions[:position] + "." + conditions[position + 1:],
                    spec,
                    position=position + 1,
                ),
            ]
        )
    else:
        return n_valid_arrangements(
            conditions,
            spec,
            position=position + 1,
        )


ans = 0
for line in tqdm(input):
    conditions = "?".join([line.split(" ")[0] for _ in range(5)])
    spec = tuple([int(s) for s in line.split(" ")[1].split(",")] * 5)

    # ans += solve(conditions, spec, 0)
    print(n_valid_arrangements(conditions, spec, 0, ))

print(ans)
